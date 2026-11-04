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
  const [icon, setIcon] = useState<IconChoice>("flat");
  useEffect(() => {
    setTheme((localStorage.getItem("studio-theme") as Theme) || "dark");
    const sync = () => setIcon(appIcon()?.get() || "flat");
    sync();
    document.addEventListener("ds-icon-change", sync);
    return () => document.removeEventListener("ds-icon-change", sync);
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
