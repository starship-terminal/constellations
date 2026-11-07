// Read Raycast's accessibility tree, so drive.py can check a target before it presses Return or clicks.
// Prints one JSON object; needs Accessibility permission (as mouse.swift does). Reads only, never acts.
//
//   ax at X Y   the element at global point (X, Y): {"owner", "window", "texts"}, where texts are the text
//               values of the nearest element there that holds any text (a label hit directly reads as its row)
//   ax results  the launcher's root search: {"query": the search field's value, "items": [["h"|"t", text], ...]}
//               in screen order, "h" for a section header ("Results", "Files"), "t" for any other text
import AppKit
import ApplicationServices
import Foundation

func attr(_ e: AXUIElement, _ n: String) -> AnyObject? { var v: AnyObject?; AXUIElementCopyAttributeValue(e, n as CFString, &v); return v }
func str(_ e: AXUIElement, _ n: String) -> String { (attr(e, n) as? String) ?? "" }
func kids(_ e: AXUIElement) -> [AXUIElement] { (attr(e, kAXChildrenAttribute) as? [AXUIElement]) ?? [] }
func classes(_ e: AXUIElement) -> [String] { (attr(e, "AXDOMClassList") as? [String]) ?? [] }
func out(_ o: Any) { print(String(data: try! JSONSerialization.data(withJSONObject: o), encoding: .utf8)!) }
func fail(_ m: String) -> Never { FileHandle.standardError.write((m + "\n").data(using: .utf8)!); exit(1) }

// The text an element shows: a static text's value (Raycast's web views carry their labels there).
func text(_ e: AXUIElement) -> String? {
  guard str(e, kAXRoleAttribute) == "AXStaticText" else { return nil }
  let v = str(e, kAXValueAttribute)
  return v.isEmpty ? nil : v
}
func texts(_ e: AXUIElement, _ depth: Int = 0) -> [String] {
  if depth > 30 { return [] }
  var t: [String] = []
  if let s = text(e) { t.append(s) }
  for c in kids(e) { t += texts(c, depth + 1) }
  return t
}

let a = CommandLine.arguments
guard AXIsProcessTrusted() else { fail("no Accessibility permission") }
switch a.count > 1 ? a[1] : "" {
case "at":
  guard a.count == 4, let x = Float(a[2]), let y = Float(a[3]) else { fail("usage: ax at X Y") }
  var hit: AXUIElement?
  guard AXUIElementCopyElementAtPosition(AXUIElementCreateSystemWide(), x, y, &hit) == .success, var e = hit else { fail("nothing at \(x),\(y)") }
  // A label hit directly reads as its row, so the row's other texts (a Pro badge, the account's name) come too.
  if str(e, kAXRoleAttribute) == "AXStaticText", let p = attr(e, kAXParentAttribute) { e = p as! AXUIElement }
  var found: [String] = []
  for _ in 0..<8 {
    found = texts(e)
    if !found.isEmpty { break }
    guard let p = attr(e, kAXParentAttribute) else { break }
    e = p as! AXUIElement
  }
  var owner = "", window = ""
  if let w = attr(e, kAXWindowAttribute) {
    let w = w as! AXUIElement
    window = str(w, kAXTitleAttribute)
    var pid: pid_t = 0
    AXUIElementGetPid(w, &pid)
    owner = NSRunningApplication(processIdentifier: pid)?.localizedName ?? ""
  }
  out(["owner": owner, "window": window, "texts": found])
case "results":
  guard let app = NSRunningApplication.runningApplications(withBundleIdentifier: "com.raycast.macos").first else { fail("Raycast is not running") }
  let root = AXUIElementCreateApplication(app.processIdentifier)
  var query: String? = nil, items: [[String]] = []
  func walk(_ e: AXUIElement, _ inResults: Bool, _ header: Bool, _ depth: Int) {
    if depth > 40 { return }
    if str(e, kAXRoleAttribute) == "AXTextField" && query == nil { query = str(e, kAXValueAttribute) }
    let results = inResults || str(e, kAXTitleAttribute) == "Root search results"
    let head = header || classes(e).contains { $0.hasPrefix("list__sectionHeaderTitle") }
    if results, let s = text(e) { items.append([head ? "h" : "t", s]) }
    for c in kids(e) { walk(c, results, head, depth + 1) }
  }
  for w in (attr(root, kAXWindowsAttribute) as? [AXUIElement]) ?? [] where str(w, kAXTitleAttribute) == "Main Window" { walk(w, false, false, 0) }
  out(["query": query.map { $0 as Any } ?? NSNull(), "items": items])
default:
  fail("usage: ax at X Y | ax results")
}
