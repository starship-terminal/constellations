import {
  AppearanceBootstrap,
  iconInitScript,
  themeInitScript,
} from "@/components/appearance";
import type { Metadata } from "next";
import { AppShell, sidebarInitScript } from "@/components/shell";
import "./globals.css";
export const metadata: Metadata = {
  title: {
    default: "Constellations · Design research",
    template: "%s · Constellations",
  },
  description:
    "A personal design research workspace. Explore references, inspect their details, and collect your thinking.",
  icons: {
    icon: [
      { url: "/brand/flat/favicon.ico", sizes: "32x32" },
      { url: "/brand/flat/favicon.svg", type: "image/svg+xml" },
    ],
    apple: "/brand/flat/apple-touch-icon.png",
  },
};
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <script dangerouslySetInnerHTML={{ __html: themeInitScript }} />
        <script dangerouslySetInnerHTML={{ __html: iconInitScript }} />
        <script dangerouslySetInnerHTML={{ __html: sidebarInitScript }} />
        <a href="#main-content" className="skip-link">
          Skip to content
        </a>
        <AppearanceBootstrap />
        <AppShell>{children}</AppShell>
      </body>
    </html>
  );
}
