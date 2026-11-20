/**
 * The per-package seed top-ups that migrations v9-v43 ran, oldest first. A
 * store below an entry's version gets that entry's categories and media
 * terms; above it, they were offered already. From v44 the seed ledger
 * offers new packages instead, so this list never grows. backfillSeedLedger
 * reads it to know what every store at v43 has been offered.
 */
export const packageTopUps: readonly {
  version: number;
  references: readonly string[];
  /** Media-only top-ups for media IDs a reference gained later. */
  media?: readonly { reference: string; ids: readonly string[] }[];
}[] = [
  { version: 9, references: ["systems:discord"] },
  { version: 10, references: ["systems:district"] },
  { version: 11, references: ["systems:dji"] },
  { version: 12, references: ["systems:framer"] },
  // Frame.io and Fourthwall.
  { version: 13, references: ["systems:frame", "systems:fourthwall"] },
  { version: 14, references: ["systems:calm"] },
  // Fresha merged without a migration and was stranded on v13/v14 stores.
  { version: 15, references: ["systems:fresha", "systems:chargetrip"] },
  // Frame.io again: its v13 top-up only reached stores below v13. Front,
  // Gladia and Glassnode merged without a migration.
  {
    version: 16,
    references: [
      "systems:classpass",
      "systems:frame",
      "systems:front",
      "systems:gladia",
      "systems:glassnode",
    ],
  },
  { version: 17, references: ["systems:clay-earth"] },
  { version: 18, references: ["systems:gofundme"] },
  { version: 19, references: ["systems:grammarly"] },
  { version: 20, references: ["systems:clearful"] },
  { version: 21, references: ["systems:glorify"] },
  { version: 22, references: ["systems:glossgenius"] },
  { version: 23, references: ["systems:grok"] },
  { version: 24, references: ["systems:clipchamp"] },
  { version: 25, references: ["systems:hashnode"] },
  { version: 26, references: ["systems:gumroad"] },
  { version: 27, references: ["systems:cofounder"] },
  { version: 28, references: ["systems:joinhandshake"] },
  { version: 29, references: ["systems:cohere"] },
  { version: 30, references: ["systems:helloivy"] },
  // Also two Handshake screenshots the seed gained after v28: only those
  // media IDs, so labels a user cleared on Handshake's older media stay
  // cleared.
  {
    version: 31,
    references: ["systems:hitchd"],
    media: [
      {
        reference: "systems:joinhandshake",
        ids: [
          "systems/joinhandshake/screenshots/home-light-consent.png",
          "systems/joinhandshake/screenshots/mobile-home-light-drawer.png",
        ],
      },
    ],
  },
  { version: 32, references: ["systems:hbomax"] },
  { version: 33, references: ["systems:grow"] },
  { version: 34, references: ["systems:headspace"] },
  // Also five Hashnode crops the seed gained after v25, by media ID for
  // the same reason.
  {
    version: 35,
    references: ["systems:homerun"],
    media: [
      {
        reference: "systems:hashnode",
        ids: [
          "systems/hashnode/components/crops/app-sidebar-dark.png",
          "systems/hashnode/components/crops/app-sidebar-default.png",
          "systems/hashnode/components/crops/feed-trending-default.png",
          "systems/hashnode/components/crops/post-card-dark.png",
          "systems/hashnode/components/crops/post-comments-link-default.png",
        ],
      },
    ],
  },
  { version: 36, references: ["systems:httpie"] },
  { version: 37, references: ["systems:coinbase"] },
  { version: 38, references: ["systems:column"] },
  { version: 39, references: ["systems:hume"] },
  // IFTTT and Intercom, Hers (v41), Leonardo (v42) and Huddlekit (v43)
  // were renumbered when they merged together; a store that reached v43
  // with the first Huddlekit build skipped v40-v42.
  { version: 40, references: ["systems:ifttt", "systems:intercom"] },
  { version: 41, references: ["systems:forhers"] },
  { version: 42, references: ["systems:leonardo"] },
  { version: 43, references: ["systems:huddlekit"] },
];
