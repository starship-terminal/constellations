// State logic behind the snippet copy button, kept free of React and the DOM
// so it can be tested with the node runner.

export type CopyState = "idle" | "copied" | "failed";

/** How long "Copied" / "Copy failed" shows before the button reverts. */
export const COPY_RESET_MS = 1800;

/** Run `copy(text)` and report the state the button should show. */
export async function copyOutcome(text: string, copy: (t: string) => Promise<void>): Promise<"copied" | "failed"> {
  try {
    await copy(text);
    return "copied";
  } catch {
    return "failed";
  }
}

type Timer = ReturnType<typeof setTimeout>;

/** Show `next` now and the idle label COPY_RESET_MS later. A previous pending
    revert (`pending`) is cancelled first, so a second click restarts the
    countdown instead of reverting early. Returns the new timer. */
export function flash(show: (s: CopyState) => void, next: CopyState, pending?: Timer): Timer {
  clearTimeout(pending);
  show(next);
  return setTimeout(() => show("idle"), COPY_RESET_MS);
}

export function copyLabel(state: CopyState): string {
  return state === "copied" ? "Copied" : state === "failed" ? "Copy failed" : "Copy";
}
