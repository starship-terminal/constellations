import type { Metadata, Viewport } from "next";
import { Instrument_Serif, JetBrains_Mono } from "next/font/google";
import { headers } from "next/headers";
import { Rail } from "@/components/Rail";
import { ToastProvider } from "@/components/Toast";
import { LightboxProvider } from "@/components/Lightbox";
import { ChatProvider, ChatDrawer } from "@/components/Chat";
import { ThemeBoot } from "@/components/ThemeBoot";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "Design systems", template: "%s · Design systems" },
  description:
    "A private library of design styles captured from real products: measured tokens, components and screenshots, plus the scorecard grading each capture.",
  icons: {
    icon: [
      { url: "/media/docs/assets/icons/favicon.ico", sizes: "32x32" },
      { url: "/media/docs/assets/favicon.svg", type: "image/svg+xml" },
    ],
    apple: "/media/docs/assets/icons/apple-touch-icon.png",
  },
};

export const viewport: Viewport = {
  // Also in the bare shell Next sends for a notFound() before the stylesheet
  // loads, so the canvas starts in the OS scheme instead of white.
  colorScheme: "light dark",
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fafafa" },
    { media: "(prefers-color-scheme: dark)", color: "#0c0d10" },
  ],
};

// The two web fonts, self-hosted: next/font downloads them from Google Fonts
// when the app is built and serves the files from this app's own origin, so
// a viewer's browser never calls Google. The same faces and weights the old
// fonts.googleapis.com stylesheet asked for. globals.css reads the variables
// in --display and --mono.
const display = Instrument_Serif({
  weight: "400",
  style: ["normal", "italic"],
  subsets: ["latin"],
  display: "swap",
  variable: "--font-display",
});
const mono = JetBrains_Mono({
  weight: ["400", "500"],
  subsets: ["latin"],
  display: "swap",
  variable: "--font-mono",
});

const themeInit = `(function(){try{var d=document.documentElement;var t=localStorage.getItem('ds-theme');d.dataset.theme=t==='light'||t==='dark'?t:(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');if(localStorage.getItem('ds-nav')==='collapsed')d.dataset.nav='collapsed';}catch(e){document.documentElement.dataset.theme='dark'}})();`;

// proxy.ts sends a Content-Security-Policy with a per-request nonce
// (lib/csp.ts), so the inline theme script carries it. Reading the request
// headers also renders every page per request, which the nonce needs: a page
// prerendered at build time would hold scripts with no nonce, and the policy
// would block them.
export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const nonce = (await headers()).get("x-nonce") ?? undefined;
  return (
    <html lang="en" className={`${display.variable} ${mono.variable}`} suppressHydrationWarning>
      <head>
        <script nonce={nonce} dangerouslySetInnerHTML={{ __html: themeInit }} />
      </head>
      <body>
        <ThemeBoot />
        <ToastProvider>
          <LightboxProvider>
            <ChatProvider>
              <Rail />
              <div className="shell">{children}</div>
              <ChatDrawer />
            </ChatProvider>
          </LightboxProvider>
        </ToastProvider>
      </body>
    </html>
  );
}
