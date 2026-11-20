# Gallery app (web/). The library is read from the host checkout at
# request time (DESIGN_SYSTEMS_REPO), so the image only carries Node and
# pnpm. The launcher mounts that checkout over /repo and the built output
# over /web-next. Do not COPY the repo in: it is several gigabytes of LFS.
#
# First boot builds web/.next into the mounted volume, then starts. Later
# boots reuse that build. A rebuild is `rm -rf` on the volume, then restart.
FROM node:22-slim

RUN corepack enable && corepack prepare pnpm@10.10.0 --activate

WORKDIR /repo
ENV DESIGN_SYSTEMS_REPO=/repo \
    NEXT_DIST_DIR=/web-next \
    PORT=8800 \
    HOSTNAME=0.0.0.0

EXPOSE 8800

CMD ["sh", "-c", "cd /repo/web && pnpm install --frozen-lockfile && if [ ! -f /web-next/BUILD_ID ]; then pnpm exec next build; fi && pnpm exec next start -H 0.0.0.0 -p 8800"]
