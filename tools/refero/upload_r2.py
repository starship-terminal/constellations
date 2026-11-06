#!/usr/bin/env python3
"""Upload a mirrored refero media tree to a Cloudflare R2 bucket.

Objects keep the /refero-media/<kind>/<slug><ext> contract as their keys, so
`<bucket public URL>/refero-media/<kind>/<slug><ext>` serves each file — the
same address catalog.py emits as `mediaBase` + `local` paths.

Credentials come from the environment or the repo's gitignored .env
(refero_media loads it on import):

    R2_ACCOUNT_ID      account id (endpoint is https://<id>.r2.cloudflarestorage.com)
    R2_ACCESS_KEY_ID   R2 API token's access key id
    R2_SECRET_ACCESS_KEY
    R2_BUCKET          default for --bucket

Usage:
    python3 tools/refero/upload_r2.py --bucket design-systems-media
        [--media-root DIR] [--workers 12] [--only videos,detail] [--dry-run]

The default media root is refero_media.default_media_root() ($DESIGN_SYSTEMS_MEDIA
or ~/services/design-systems/media/refero). Existing objects are still re-PUT;
R2 charges a class-B op per upload, so use --only/--dry-run while testing.
"""

import argparse
import concurrent.futures
import datetime
import hashlib
import hmac
import mimetypes
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import refero_media  # noqa: E402

KINDS = refero_media.KINDS
UA = {"User-Agent": "design-systems-media-uploader/1.0"}

REGION, SERVICE, ALGO = "auto", "s3", "AWS4-HMAC-SHA256"
UNSIGNED = "UNSIGNED-PAYLOAD"


def _hmac(key, msg):
    return hmac.new(key, msg.encode(), hashlib.sha256).digest()


def signed_headers(method, host, uri, key_id, secret, now):
    """SigV4 headers for one PUT. UNSIGNED-PAYLOAD skips hashing the body, which
    keeps signing cheap for multi-MB videos; R2 accepts it over TLS."""
    date = now.strftime("%Y%m%d")
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    headers = {
        "host": host,
        "x-amz-content-sha256": UNSIGNED,
        "x-amz-date": amz_date,
    }
    signed = ";".join(sorted(headers))
    canonical_headers = "".join(f"{k}:{headers[k]}\n" for k in sorted(headers))
    canonical_request = "\n".join(
        [method, urllib.parse.quote(uri), "", canonical_headers, signed, UNSIGNED])
    scope = f"{date}/{REGION}/{SERVICE}/aws4_request"
    string_to_sign = "\n".join(
        [ALGO, amz_date, scope, hashlib.sha256(canonical_request.encode()).hexdigest()])
    signing = _hmac(_hmac(_hmac(_hmac(("AWS4" + secret).encode(), date),
                                REGION), SERVICE), "aws4_request")
    headers["Authorization"] = (
        f"{ALGO} Credential={key_id}/{scope}, SignedHeaders={signed}, "
        f"Signature={hmac.new(signing, string_to_sign.encode(), hashlib.sha256).hexdigest()}")
    return headers


def upload(endpoint, bucket, key, path, creds):
    """PUT path to <endpoint>/<bucket>/<key>; retry with backoff."""
    host = urllib.parse.urlparse(endpoint).netloc
    ct = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    url = f"{endpoint}/{bucket}/{urllib.parse.quote(key)}"
    data = path.read_bytes()
    for i in range(4):
        try:
            req = urllib.request.Request(
                url, data=data, method="PUT",
                headers={**UA, "Content-Type": ct, "Content-Length": str(len(data)),
                         **signed_headers("PUT", host, f"/{bucket}/{key}",
                                          creds[0], creds[1],
                                          datetime.datetime.now(datetime.timezone.utc))})
            with urllib.request.urlopen(req, timeout=180) as r:
                if r.status >= 400:
                    raise ValueError(f"http {r.status}")
            return
        except Exception:
            if i == 3:
                raise
            time.sleep(2 ** i)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bucket", default=os.environ.get("R2_BUCKET"),
                    required="R2_BUCKET" not in os.environ)
    ap.add_argument("--prefix", default="refero-media",
                    help="object key prefix (default keeps the /refero-media contract)")
    ap.add_argument("--media-root", type=Path, default=None)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be uploaded; sends nothing")
    args = ap.parse_args()

    media_root = args.media_root or refero_media.default_media_root()
    endpoint = f"https://{os.environ.get('R2_ACCOUNT_ID', '')}.r2.cloudflarestorage.com"
    creds = (os.environ.get("R2_ACCESS_KEY_ID"),
             os.environ.get("R2_SECRET_ACCESS_KEY"))

    only = (set(KINDS) if not args.only
            else {s.strip() for s in args.only.split(",") if s.strip()})
    bad = only - set(KINDS)
    if bad:
        ap.error(f"unknown --only kinds: {', '.join(sorted(bad))}")

    jobs = []
    for kind in sorted(only):
        kind_dir = media_root / kind
        if not kind_dir.is_dir():
            continue
        ext = KINDS[kind][0]
        for path in sorted(kind_dir.iterdir()):
            if path.suffix != ext or path.name.endswith((".partial", ".compress" + ext)):
                continue
            jobs.append((kind, path, f"{args.prefix}/{kind}/{path.name}"))

    if not jobs:
        sys.exit(f"nothing to upload under {media_root}")
    print(f"{len(jobs)} objects -> {args.bucket}/{args.prefix}/ "
          f"({sum(p.stat().st_size for _, p, _ in jobs) / 1e9:.2f} GB)")

    if args.dry_run:
        for kind, path, key in jobs[:20]:
            print(f"  {key}  ({path.stat().st_size / 1e6:.1f} MB)")
        print(f"  … {len(jobs) - 20} more" if len(jobs) > 20 else "")
        return

    if not all(creds) or not os.environ.get("R2_ACCOUNT_ID"):
        sys.exit("set R2_ACCOUNT_ID, R2_ACCESS_KEY_ID and R2_SECRET_ACCESS_KEY")

    done = failed = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(upload, endpoint, args.bucket, key, path, creds):
                   (kind, path) for kind, path, key in jobs}
        for fut in concurrent.futures.as_completed(futures):
            kind, path = futures[fut]
            try:
                fut.result()
                done += 1
            except Exception as ex:
                failed += 1
                print(f"FAIL {kind}/{path.name}: {ex}", file=sys.stderr)
            if (done + failed) % 100 == 0:
                print(f"{done + failed}/{len(jobs)}")
    print(f"uploaded {done}; {failed} failed")


if __name__ == "__main__":
    main()
