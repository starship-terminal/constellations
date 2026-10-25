// mouse move X Y | click X Y | rclick X Y | dclick X Y | scroll X Y DY
// Global screen points (top-left origin). Posts CGEvents; needs Accessibility permission.
import CoreGraphics
import Foundation
let a = CommandLine.arguments
guard a.count >= 4, let x = Double(a[2]), let y = Double(a[3]) else { print("usage"); exit(1) }
let p = CGPoint(x: x, y: y)
func post(_ t: CGEventType, _ b: CGMouseButton = .left, clicks: Int64 = 1) {
    let e = CGEvent(mouseEventSource: nil, mouseType: t, mouseCursorPosition: p, mouseButton: b)!
    e.setIntegerValueField(.mouseEventClickState, value: clicks)
    e.post(tap: .cghidEventTap)
}
switch a[1] {
case "move":
    post(.mouseMoved)
case "click":
    post(.mouseMoved); usleep(80_000); post(.leftMouseDown); usleep(60_000); post(.leftMouseUp)
case "dclick":
    post(.mouseMoved); usleep(80_000)
    post(.leftMouseDown); post(.leftMouseUp); usleep(60_000)
    post(.leftMouseDown, clicks: 2); post(.leftMouseUp, clicks: 2)
case "rclick":
    post(.mouseMoved); usleep(80_000); post(.rightMouseDown, .right); usleep(60_000); post(.rightMouseUp, .right)
case "scroll":
    post(.mouseMoved); usleep(50_000)
    let dy = Int32(a.count > 4 ? Int(a[4]) ?? -5 : -5)
    let e = CGEvent(scrollWheelEvent2Source: nil, units: .line, wheelCount: 1, wheel1: dy, wheel2: 0, wheel3: 0)!
    e.location = p
    e.post(tap: .cghidEventTap)
default:
    print("unknown"); exit(1)
}
