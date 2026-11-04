"use client";
import { useEffect, useState } from "react";
import { Palette } from "lucide-react";
import { Select } from "./shared";
type Theme = "dark" | "light" | "system";
function apply(theme: Theme) {
  document.documentElement.dataset.theme =
    theme === "system"
      ? matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light"
      : theme;
}
export function AppearanceBootstrap() {
  useEffect(() => {
    const update = () =>
      apply((localStorage.getItem("studio-theme") as Theme) || "dark");
    const media = matchMedia("(prefers-color-scheme: dark)");
    update();
    media.addEventListener("change", update);
    window.addEventListener("studio-appearance", update);
    return () => {
      media.removeEventListener("change", update);
      window.removeEventListener("studio-appearance", update);
    };
  }, []);
  return null;
}
export function AppearanceSettings() {
  const [theme, setTheme] = useState<Theme>("dark");
  useEffect(() => {
    setTheme((localStorage.getItem("studio-theme") as Theme) || "dark");
  }, []);
  return (
    <section className="settings-section">
      <div className="settings-section-label">
        <Palette size={19} />
        <div>
          <h2>Appearance</h2>
          <p>Choose the workspace theme.</p>
        </div>
      </div>
      <div className="settings-form">
        <div className="settings-field">
          <span>Theme</span>
          <Select
            label="Theme"
            value={theme}
            onChange={(value) => {
              const next = value as Theme;
              setTheme(next);
              localStorage.setItem("studio-theme", next);
              window.dispatchEvent(new Event("studio-appearance"));
            }}
            options={[
              { value: "dark", label: "Dark" },
              { value: "light", label: "Light" },
              { value: "system", label: "System" },
            ]}
          />
        </div>
      </div>
    </section>
  );
}
