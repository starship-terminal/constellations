// Print the id of Zed's main window (the largest layer-0 window owned by Zed), or exit 1.
// Exits 2 when Zed is not the frontmost app, so a capture never shows another app's window.
import CoreGraphics
import AppKit
let ws = (CGWindowListCopyWindowInfo([.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID) as? [[String: Any]]) ?? []
let want = CommandLine.arguments.dropFirst().first   // optional: a substring of the window title
let zed = ws.filter { ($0[kCGWindowOwnerName as String] as? String) == "Zed" && ($0[kCGWindowLayer as String] as? Int) == 0
    && (want == nil || (($0[kCGWindowName as String] as? String) ?? "").contains(want!)) }
func area(_ w: [String: Any]) -> Double {
    let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
    return ((b["Width"] as? Double) ?? 0) * ((b["Height"] as? Double) ?? 0)
}
guard let main = zed.max(by: { area($0) < area($1) }), let id = main[kCGWindowNumber as String] as? Int else {
    FileHandle.standardError.write("no Zed window\n".data(using: .utf8)!); exit(1)
}
// Never capture while the owner's settings file (it holds a key) is the active item of any Zed window.
if ws.contains(where: { ($0[kCGWindowOwnerName as String] as? String) == "Zed" && (($0[kCGWindowName as String] as? String) ?? "").contains("settings.json") }) {
    FileHandle.standardError.write("settings.json is open: refusing\n".data(using: .utf8)!); exit(3)
}
if NSWorkspace.shared.frontmostApplication?.localizedName != "Zed" {
    FileHandle.standardError.write("Zed is not frontmost\n".data(using: .utf8)!); exit(2)
}
print(id)
