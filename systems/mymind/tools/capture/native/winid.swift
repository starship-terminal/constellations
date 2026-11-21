// Print the window id of an app's frontmost on-screen window, for `screencapture -l`.
//
//   swift tools/capture/native/winid.swift "iPhone Mirroring"
//   screencapture -o -l "$(swift tools/capture/native/winid.swift 'iPhone Mirroring')" out.png
//
// -o drops the window shadow, so the PNG is the window alone. The terminal running this needs
// Screen Recording permission (System Settings > Privacy & Security); without it the window list
// comes back without names and this exits 1.
import CoreGraphics
import Foundation

let owner = CommandLine.arguments.dropFirst().first ?? "iPhone Mirroring"
let options: CGWindowListOption = [.optionOnScreenOnly, .excludeDesktopElements]
let windows = (CGWindowListCopyWindowInfo(options, kCGNullWindowID) as? [[String: Any]]) ?? []
let match = windows.first {
    ($0[kCGWindowOwnerName as String] as? String) == owner && ($0[kCGWindowLayer as String] as? Int) == 0
}
guard let id = match?[kCGWindowNumber as String] as? Int else {
    FileHandle.standardError.write("no on-screen window owned by \(owner)\n".data(using: .utf8)!)
    exit(1)
}
print(id)
