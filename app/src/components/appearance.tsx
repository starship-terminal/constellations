"use client";
import { useEffect, useState } from "react";
import { AppWindow, Palette } from "lucide-react";
import { Select } from "./shared";
type Theme = "dark" | "light" | "system";
type IconChoice = "flat" | "glass";
interface AppIconApi {
  options: IconChoice[];
  get(): IconChoice;
  set(name: IconChoice): void;
}
function appIcon(): AppIconApi | undefined {
  return (window as unknown as { dsAppIcon?: AppIconApi }).dsAppIcon;
}
const ICON_OPTIONS = [
  {
    value: "flat",
    label: "Flat",
    hint: "Default",
    src: "/brand/flat/icon-192.png",
  },
  {
    value: "glass",
    label: "Glass",
    hint: "Rendered prism",
    src: "/brand/glass/icon-192.png",
  },
] as const;
// Runs before hydration inside the layout <body>: restores the icon choice
// from localStorage, swaps the tab and touch icon <link>s, sets
// <html data-icon> so the sidebar mark follows, and exposes window.dsAppIcon
// for the settings tab. Stored under ds-icon, shared with the static site.
export const iconInitScript = `(function(){try{
var KEY='ds-icon',DEFAULT='flat';
var SETS={
flat:[
{rel:'icon',href:'/brand/flat/favicon.ico',sizes:'32x32'},
{rel:'icon',href:'/brand/flat/favicon.svg',type:'image/svg+xml'},
{rel:'apple-touch-icon',href:'/brand/flat/apple-touch-icon.png'}
],
glass:[
{rel:'icon',href:'/brand/glass/favicon-16.png',type:'image/png',sizes:'16x16'},
{rel:'icon',href:'/brand/glass/favicon-32.png',type:'image/png',sizes:'32x32'},
{rel:'icon',href:'/brand/glass/favicon-48.png',type:'image/png',sizes:'48x48'},
{rel:'apple-touch-icon',href:'/brand/glass/apple-touch-icon.png'}
]
};
var current=localStorage.getItem(KEY);if(!SETS[current])current=DEFAULT;
function apply(name){
var head=document.head;
var old=head.querySelectorAll('link[rel="icon"],link[rel="apple-touch-icon"]');
var anchor=old.length?old[old.length-1].nextSibling:null;
for(var i=0;i<old.length;i++)old[i].remove();
SETS[name].forEach(function(spec){
var link=document.createElement('link');
link.rel=spec.rel;link.href=spec.href;
if(spec.type)link.type=spec.type;
if(spec.sizes)link.setAttribute('sizes',spec.sizes);
head.insertBefore(link,anchor);
});
document.documentElement.dataset.icon=name;
}
apply(current);
window.dsAppIcon={
options:Object.keys(SETS),
get:function(){return current},
set:function(name){
if(!SETS[name]||name===current)return;
current=name;
try{localStorage.setItem(KEY,name)}catch(e){}
apply(name);
document.dispatchEvent(new CustomEvent('ds-icon-change',{detail:name}));
}
};
window.addEventListener('storage',function(e){
if(e.key!==KEY)return;
var next=localStorage.getItem(KEY);if(!SETS[next])next=DEFAULT;
if(next===current)return;
current=next;apply(next);
document.dispatchEvent(new CustomEvent('ds-icon-change',{detail:next}));
});
}catch(e){}})();`;
const THEME_KEY = "studio-theme";
/** The owner's standard order: System, Dark, Light. */
export const THEME_OPTIONS = [
  { value: "system", label: "System" },
  { value: "dark", label: "Dark" },
  { value: "light", label: "Light" },
];
// Runs before hydration inside the layout <body>, ahead of any content, so a
// user never sees the wrong theme on first paint. With no stored choice it
// follows the system setting. AppearanceBootstrap keeps it
// current afterwards; both resolve the stored choice the same way.
export const themeInitScript = `(function(){var t=null,dark=true;
try{t=localStorage.getItem('${THEME_KEY}')}catch(e){}
try{dark=matchMedia('(prefers-color-scheme: dark)').matches}catch(e){}
if(t!=='dark'&&t!=='light')t=dark?'dark':'light';
document.documentElement.dataset.theme=t;
})();`;

/** A storage event that may have changed the theme: its key, or a cleared store. */
export function themeStorageChanged(key: string | null): boolean {
  return key === THEME_KEY || key === null;
}
/** No stored choice, or an unreadable store, means System. */
export function storedTheme(): Theme {
  let value: string | null = null;
  try {
    value = localStorage.getItem(THEME_KEY);
  } catch {}
  return value === "light" || value === "dark" ? value : "system";
}
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
    const update = () => apply(storedTheme());
    // Another tab changed the theme in Settings.
    const onStorage = (event: StorageEvent) => {
      if (themeStorageChanged(event.key)) update();
    };
    const media = matchMedia("(prefers-color-scheme: dark)");
    update();
    media.addEventListener("change", update);
    window.addEventListener("studio-appearance", update);
    window.addEventListener("storage", onStorage);
    return () => {
      media.removeEventListener("change", update);
      window.removeEventListener("studio-appearance", update);
      window.removeEventListener("storage", onStorage);
    };
  }, []);
  return null;
}
export function AppearanceSettings() {
  const [theme, setTheme] = useState<Theme>("system");
  const [icon, setIcon] = useState<IconChoice>("flat");
  useEffect(() => {
    setTheme(storedTheme());
    const sync = () => setIcon(appIcon()?.get() || "flat");
    const onStorage = (event: StorageEvent) => {
      if (themeStorageChanged(event.key)) setTheme(storedTheme());
    };
    sync();
    document.addEventListener("ds-icon-change", sync);
    window.addEventListener("storage", onStorage);
    return () => {
      document.removeEventListener("ds-icon-change", sync);
      window.removeEventListener("storage", onStorage);
    };
  }, []);
  return (
    <>
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
                localStorage.setItem(THEME_KEY, next);
                window.dispatchEvent(new Event("studio-appearance"));
              }}
              options={[...THEME_OPTIONS]}
            />
          </div>
        </div>
      </section>
      <section className="settings-section">
        <div className="settings-section-label">
          <AppWindow size={19} />
          <div>
            <h2>App icon</h2>
            <p>
              The icon in the browser tab, on a home screen and in the sidebar.
            </p>
          </div>
        </div>
        <div className="settings-form">
          <div className="settings-field">
            <div
              className="icon-options"
              role="radiogroup"
              aria-label="App icon"
            >
              {ICON_OPTIONS.map((option) => (
                <label
                  key={option.value}
                  className={`icon-option ${icon === option.value ? "selected" : ""}`}
                >
                  <input
                    type="radio"
                    name="app-icon"
                    value={option.value}
                    checked={icon === option.value}
                    onChange={() => {
                      setIcon(option.value);
                      appIcon()?.set(option.value);
                    }}
                  />
                  <img src={option.src} alt="" width={40} height={40} />
                  <span>
                    <strong>{option.label}</strong>
                    <small>{option.hint}</small>
                  </span>
                </label>
              ))}
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
