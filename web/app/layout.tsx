import type { Metadata, Viewport } from "next";
import { Rail } from "@/components/Rail";
import { ToastProvider } from "@/components/Toast";
import { LightboxProvider } from "@/components/Lightbox";
import { ChatProvider, ChatDrawer } from "@/components/Chat";
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
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fafafa" },
    { media: "(prefers-color-scheme: dark)", color: "#0c0d10" },
  ],
};

const themeInit = `(function(){try{var d=document.documentElement;var t=localStorage.getItem('ds-theme');d.dataset.theme=t==='light'||t==='dark'?t:(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');if(localStorage.getItem('ds-nav')==='collapsed')d.dataset.nav='collapsed';}catch(e){document.documentElement.dataset.theme='dark'}})();`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeInit }} />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="" />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap"
        />
      </head>
      <body>
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
