// The reader's reduced-motion preference, for motion started from script
// (smooth scrolling, hover video) that the CSS media query cannot reach.
export const reducedMotion = (): boolean =>
  typeof window !== "undefined" && window.matchMedia?.("(prefers-reduced-motion: reduce)").matches === true;

export const scrollBehavior = (): ScrollBehavior => (reducedMotion() ? "auto" : "smooth");
