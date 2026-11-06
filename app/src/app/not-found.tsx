import Link from "next/link";
export default function NotFound() {
  return (
    <div className="page">
      <h1>That page has moved out of view.</h1>
      <p className="muted">
        Start a new research or return to your reference library.
      </p>
      <Link href="/" className="primary">
        New research
      </Link>
    </div>
  );
}
