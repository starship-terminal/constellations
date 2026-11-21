// Lyft public capture. ADAPTED_FOR = lyft.
// Photographs marketing pages and stops at empty login and driver-apply walls.
// Does not type, submit, or follow app deep links.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs
//
// Full-colour shots go to ~/.design-systems/lyft/raw-shots. quantize.py writes screenshots/.
const ADAPTED_FOR = 'lyft';

export const PAGES = [
  ['home', 'https://www.lyft.com/'],
  ['rider', 'https://www.lyft.com/rider'],
  ['driver', 'https://www.lyft.com/driver'],
  ['business', 'https://www.lyft.com/business'],
  ['safety', 'https://www.lyft.com/safety'],
  ['cities', 'https://www.lyft.com/rider/cities'],
  ['driver-cities', 'https://www.lyft.com/driver/cities'],
  ['help', 'https://help.lyft.com/hc/en-us'],
  ['login', 'https://www.lyft.com/login'],
  ['signup', 'https://www.lyft.com/drive-with-lyft'],
];

if (import.meta.url === `file://${process.argv[1]}`) {
  console.log(ADAPTED_FOR, PAGES.map((p) => p[0]).join(','));
}
