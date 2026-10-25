// List every on-screen window owned by an app: id, layer, bounds, name. Also print the frontmost app.
import CoreGraphics
import AppKit
let owner = CommandLine.arguments.dropFirst().first ?? "Zed"
let ws = (CGWindowListCopyWindowInfo([.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID) as? [[String: Any]]) ?? []
for w in ws where (w[kCGWindowOwnerName as String] as? String) == owner {
    let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
    print(w[kCGWindowNumber as String] ?? "", "layer", w[kCGWindowLayer as String] ?? "", b["X"] ?? "", b["Y"] ?? "", b["Width"] ?? "", b["Height"] ?? "", "|", w[kCGWindowName as String] ?? "")
}
print("frontmost:", NSWorkspace.shared.frontmostApplication?.localizedName ?? "?")
