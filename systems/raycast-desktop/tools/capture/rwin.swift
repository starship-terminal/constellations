// rwin [<title part>]: print the id of Raycast's largest on-screen window (any layer), or exit non-zero.
// Exits 2 when Raycast is not the frontmost app, so a capture never shows another app's window.
// With a title part, only windows whose title contains it count ("Main Window", "Settings", ...).
import CoreGraphics
import AppKit
let ws = (CGWindowListCopyWindowInfo([.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID) as? [[String: Any]]) ?? []
let want = CommandLine.arguments.dropFirst().first
let mine = ws.filter { ($0[kCGWindowOwnerName as String] as? String) == "Raycast"
    && (($0[kCGWindowLayer as String] as? Int) ?? 99) < 25
    && (want == nil || (($0[kCGWindowName as String] as? String) ?? "").contains(want!)) }
func area(_ w: [String: Any]) -> Double {
    let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
    return ((b["Width"] as? Double) ?? 0) * ((b["Height"] as? Double) ?? 0)
}
guard let main = mine.max(by: { area($0) < area($1) }), let id = main[kCGWindowNumber as String] as? Int, area(main) > 40000 else {
    FileHandle.standardError.write("no Raycast window\n".data(using: .utf8)!); exit(1)
}
if NSWorkspace.shared.frontmostApplication?.localizedName != "Raycast" {
    FileHandle.standardError.write("Raycast is not frontmost\n".data(using: .utf8)!); exit(2)
}
print(id)
