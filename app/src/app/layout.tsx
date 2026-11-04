import type { Metadata } from "next";
import { AppShell } from "@/components/shell";
import "./globals.css";
export const metadata: Metadata = {
  title: { default: "Studio · Design research", template: "%s · Studio" },
  description:
    "A personal design research workspace. Explore references, inspect their details, and collect your thinking.",
};
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <a href="#main-content" className="skip-link">
          Skip to content
        </a>
        <AppShell>{children}</AppShell>
      </body>
    </html>
  );
}
