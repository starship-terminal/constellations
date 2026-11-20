/**
 * Tracks fetches that are still running, so triggers that arrive together
 * (focus plus visibilitychange) can join one fetch, while a trigger that
 * arrives after it settled starts a new one.
 */
export function createInFlightGuard() {
  let running = 0;
  return {
    /** Call when a fetch starts; call the returned function when it settles. */
    start() {
      running++;
      let ended = false;
      return () => {
        if (!ended) {
          ended = true;
          running--;
        }
      };
    },
    busy() {
      return running > 0;
    },
  };
}
