// wins.swift [owner] [titlePrefix]: list on-screen windows (id owner layer bounds title), or print the
// id of the first window of owner whose title starts with titlePrefix.
import CoreGraphics
import Foundation
let args = Array(CommandLine.arguments.dropFirst())
let ws = (CGWindowListCopyWindowInfo([.optionOnScreenOnly, .excludeDesktopElements], kCGNullWindowID) as? [[String: Any]]) ?? []
for w in ws {
    let owner = w[kCGWindowOwnerName as String] as? String ?? ""
    let title = w[kCGWindowName as String] as? String ?? ""
    let layer = w[kCGWindowLayer as String] as? Int ?? -1
    let id = w[kCGWindowNumber as String] as? Int ?? 0
    let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
    if args.count >= 1 {
        if owner != args[0] || layer != 0 { continue }
        if args.count >= 2 && !title.hasPrefix(args[1]) { continue }
        print(id); exit(0)
    }
    print(id, owner, layer, b["X"] ?? "", b["Y"] ?? "", b["Width"] ?? "", b["Height"] ?? "", title)
}
if args.count >= 1 { exit(1) }
