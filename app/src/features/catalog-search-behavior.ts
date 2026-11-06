export interface ChoicePosition {
  index: number;
  x: number;
  y: number;
}

/** Follow actual rendered rows, including responsive columns and subgroup gaps. */
export function verticalChoiceIndex(
  positions: readonly ChoicePosition[],
  current: number,
  direction: 1 | -1,
): number {
  const selected = positions.find((position) => position.index === current);
  if (!selected || !positions.length) return positions[0]?.index ?? -1;
  const ahead = positions.filter(
    (position) => (position.y - selected.y) * direction > 1,
  );
  const row = ahead.length
    ? direction === 1
      ? Math.min(...ahead.map((position) => position.y))
      : Math.max(...ahead.map((position) => position.y))
    : direction === 1
      ? Math.min(...positions.map((position) => position.y))
      : Math.max(...positions.map((position) => position.y));
  return (
    positions
      .filter((position) => Math.abs(position.y - row) < 1)
      .sort(
        (left, right) =>
          Math.abs(left.x - selected.x) - Math.abs(right.x - selected.x),
      )[0]?.index ?? current
  );
}

/** Enter on a dismissed picker reopens it without applying a stale choice. */
export function enterSearchAction(
  open: boolean,
  typed: string,
  highlight: number,
) {
  return open && (typed || highlight >= 0) ? "choose" : "open";
}

export function screenCountScope(
  platform: string,
  kind: "crop" | "screenshot",
) {
  return {
    key: `${platform}:${kind}`,
    query: new URLSearchParams({ limit: "0", platform, kind }),
  };
}

/**
 * Tab steps through the picker's groups, then lets focus leave the field:
 * past the last group (or before the first with Shift) there is no next group.
 */
export function nextPickerGroup(
  current: number,
  count: number,
  backwards: boolean,
): number | null {
  const next = current + (backwards ? -1 : 1);
  return next >= 0 && next < count ? next : null;
}
