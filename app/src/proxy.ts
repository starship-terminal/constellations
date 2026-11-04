import { NextResponse, type NextRequest } from "next/server";
import { isAllowedHost } from "@/server/request-host";

// No matcher: Next runs this before every route, including reads and media.
// Host comes from the HTTP request; forwarded headers never grant access.
export function proxy(request: NextRequest) {
  if (!isAllowedHost(request.headers.get("host"))) {
    return NextResponse.json(
      {
        error:
          "This personal research app only accepts loopback hosts or its configured private origin.",
      },
      { status: 403 },
    );
  }
  return NextResponse.next();
}
