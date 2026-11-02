// Quiet 404: the display face, one line, a way home.
import Link from "next/link";

export default function NotFound() {
  return (
    <div className="page">
      <div className="g-hero">
        <h1>Nothing here</h1>
        <p className="sub">That page is not in the library.</p>
        <Link className="btn" href="/">
          Back home
        </Link>
      </div>
    </div>
  );
}
