import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
import {build} from 'esbuild';
import {fileURLToPath} from 'node:url';
// Paths below are relative to the package folder; dependencies live in tools/node_modules.
process.chdir(path.join(path.dirname(fileURLToPath(import.meta.url)),'..'));
const require=createRequire(import.meta.url), t=require('@shopify/polaris-tokens');
// The primitive ramps ship in the tokens package but its index does not export them.
const tokensSrc=path.join(path.dirname(require.resolve('@shopify/polaris-tokens')),'../src');
const colorsPath=path.join(tokensSrc,'colors.js'), ramps=require(colorsPath);
// Which ramp step each semantic colour names: rebuild the themes from source with every
// step replaced by a marker, then read the markers back. Values stay those of `t`.
const aliases=(()=>{
 const drop=()=>{for(const k of Object.keys(require.cache))if(k.startsWith(tokensSrc))delete require.cache[k]};
 const marked=Object.fromEntries(Object.entries(ramps).map(([hue,steps])=>[hue,Object.fromEntries(Object.keys(steps).map(s=>[s,`@@${hue}.${s}@@`]))]));
 drop();require.cache[colorsPath]={id:colorsPath,filename:colorsPath,loaded:true,exports:marked};
 const meta=require(path.join(tokensSrc,'themes/index.js')).metaThemes;drop();
 const out={};
 for(const [theme,groups] of Object.entries(meta)){out[theme]={};for(const [name,{value}] of Object.entries(groups.color)){
  const m=/^@@([a-zA-Z]+)\.(\d+)@@$/.exec(value);
  if(m){if(ramps[m[1]][m[2]]!==t.themes[theme].color[name])throw new Error(`alias ${theme}.${name} does not match its value`);out[theme][name]=`${m[1]}.${m[2]}`}
 }}
 return out;
})();
const source='/tmp/polaris-reference-source-20260925';
const write=(p,v)=>fs.writeFileSync(p,typeof v==='string'?v:JSON.stringify(v,null,2));
for(const dir of ['assets','tokens','raw','icons','licenses'])fs.mkdirSync(dir,{recursive:true});
write('raw/polaris-themes.raw.json',t.themes);
write('raw/polaris-metadata.json',t.metaThemes);
write('raw/polaris-colors.raw.json',ramps);
// Neutral first, then the hues in the package's order.
const rampOrder=Object.entries(ramps).sort(([a],[b])=>(b==='gray')-(a==='gray'));
const studio={core:{color:Object.fromEntries(rampOrder.map(([hue,steps])=>[hue,Object.fromEntries(Object.entries(steps).map(([step,value])=>[step,{value,type:'color',description:'@shopify/polaris-tokens 9.4.2 / colors.js primitive ramp'}]))]))}};
for(const [theme,groups] of Object.entries(t.themes)){
 const out={};
 for(const [group,values] of Object.entries(groups)){out[group]={};for(const [name,value]of Object.entries(values)){
 let type=group==='color'&&name!=='color-scheme'?'color':name.includes('font-family')?'fontFamilies':name.includes('font-weight')?'fontWeights':name.includes('radius')?'borderRadius':name.includes('font-size')?'fontSizes':group==='space'?'spacing':/^[-\d.]+(rem|px)$/.test(value)?'sizing':'other';
 const alias=group==='color'&&aliases[theme][name];
 out[group][name]={value:alias?`{color.${alias}}`:value,type,description:`@shopify/polaris-tokens 9.4.2 / ${theme}`};
 }}studio[theme]=out;
}
// Named sizes, focus ring and layout values the components set in their own CSS. Not
// tokens in @shopify/polaris-tokens, so each says which stylesheet it was read from.
// Aliases point at the theme sets (`{height.height-600}`) and resolve per theme.
const src=f=>`Measured CSS: read from polaris-react/src/components/${f} at archive commit 3f7954ae`;
const component={
 size:{
  'button-micro-min-height':['{height.height-600}','Button/Button.module.css L215-225 .sizeMicro, md and up'],
  'button-micro-min-height-narrow':['{height.height-700}','Button/Button.module.css L215-225 .sizeMicro, below md'],
  'button-medium-min-height':['{height.height-700}','Button/Button.module.css L227-238 .sizeSlim, .sizeMedium, md and up'],
  'button-medium-min-height-narrow':['{height.height-800}','Button/Button.module.css L227-238 .sizeSlim, .sizeMedium, below md'],
  'button-large-min-height':['{height.height-800}','Button/Button.module.css L240-250 .sizeLarge, md and up'],
  'button-large-min-height-narrow':['{height.height-900}','Button/Button.module.css L240-250 .sizeLarge, below md'],
  'control-height':['2rem','AppProvider/global.css L47-50 --pg-control-height; TextField and Select minimum height'],
  'text-field-slim-min-height':['1.75rem','TextField/TextField.module.css L333-339 .slim'],
  'tab-height':['{height.height-700}','Tabs/Tabs.module.css L56-79 .Tab'],
  'tag-large-min-height':['1.5rem','Tag/Tag.module.css L169-195 .sizeLarge'],
  'choice-control':['1.125rem','Choice/Choice.module.css L110-130 --pc-choice-size, md and up (checkbox and radio box)'],
  'choice-control-narrow':['1.25rem','Choice/Choice.module.css L110-130 --pc-choice-size, below md'],
  'action-list-item-min-height':['{space.space-800}','ActionList/ActionList.module.css L7-30 .Item'],
  'icon':['1.25rem','Icon/Icon.module.css L1-9 .Icon; the only icon size, no size prop'],
  'avatar-xs':['1.25rem','Avatar/Avatar.module.css L3-7 --pc-avatar-xs-size'],
  'avatar-sm':['1.5rem','Avatar/Avatar.module.css L3-7 --pc-avatar-sm-size'],
  'avatar-md':['1.75rem','Avatar/Avatar.module.css L3-7 --pc-avatar-md-size (the default)'],
  'avatar-lg':['2rem','Avatar/Avatar.module.css L3-7 --pc-avatar-lg-size'],
  'avatar-xl':['2.5rem','Avatar/Avatar.module.css L3-7 --pc-avatar-xl-size'],
  'thumbnail-extra-small':['1.5rem','Thumbnail/Thumbnail.module.css L3-6'],
  'thumbnail-small':['2.5rem','Thumbnail/Thumbnail.module.css L3-6'],
  'thumbnail-medium':['3.75rem','Thumbnail/Thumbnail.module.css L3-6 (the default)'],
  'thumbnail-large':['5rem','Thumbnail/Thumbnail.module.css L3-6'],
  'spinner-small':['1.25rem','Spinner/Spinner.module.css L1-15'],
  'spinner-large':['2.75rem','Spinner/Spinner.module.css L1-15 (the default)'],
 },
 focusRing:{
  'width':['{border.border-width-050}','Button/Button.module.css L86-96 :focus-visible outline width; the same on field, select, checkbox and radio backdrops'],
  'offset':['{space.space-025}','Button/Button.module.css L86-96 :focus-visible outline-offset'],
  'color':['{color.color-border-focus}','Button/Button.module.css L86-96 :focus-visible outline colour'],
 },
 layout:{
  'page-max-width':['62.375rem','Page/Page.module.css L7-10: primary max 662 + secondary max 320 + 16 px'],
  'page-narrow-max-width':['41.375rem','Page/Page.module.css L23-26 narrowWidth: --pg-layout-width-primary-max'],
  'page-inline-padding':['{space.space-600}','Page/Page.module.css L7-10, sm and up'],
  'layout-primary-min':['30rem','AppProvider/global.css L7-52 --pg-layout-width-primary-min'],
  'layout-primary-max':['41.375rem','AppProvider/global.css L7-52 --pg-layout-width-primary-max'],
  'layout-secondary-min':['15rem','AppProvider/global.css L7-52 --pg-layout-width-secondary-min'],
  'layout-secondary-max':['20rem','AppProvider/global.css L7-52 --pg-layout-width-secondary-max'],
  'layout-one-half':['28.125rem','Layout/Layout.module.css L33-64 oneHalf flex basis'],
  'layout-one-third':['15rem','Layout/Layout.module.css L33-64 oneThird flex basis'],
  'layout-gap':['1rem','Layout/Layout.module.css L1-26 section margin'],
  'grid-columns-xs':[6,'Grid/Grid.module.css L4-57 --pc-grid-columns-xs'],
  'grid-columns-sm':[6,'Grid/Grid.module.css L4-57 --pc-grid-columns-sm'],
  'grid-columns-md':[6,'Grid/Grid.module.css L4-57 --pc-grid-columns-md'],
  'grid-columns-lg':[12,'Grid/Grid.module.css L4-57 --pc-grid-columns-lg'],
  'grid-columns-xl':[12,'Grid/Grid.module.css L4-57 --pc-grid-columns-xl'],
  'grid-gap':['{space.space-400}','Grid/Grid.module.css L4-57, every breakpoint'],
  'navigation-width':['15rem','AppProvider/global.css L7-52 --pg-navigation-width (Frame, md and up)'],
  'top-bar-height':['3.5rem','AppProvider/global.css L7-52 --pg-top-bar-height'],
  'modal-width':['38.75rem','Modal/components/Dialog/Dialog.module.css L1-89 regular max width'],
  'modal-width-small':['23.75rem','Modal/components/Dialog/Dialog.module.css L1-89 small'],
  'modal-width-large':['61.25rem','Modal/components/Dialog/Dialog.module.css L1-89 large, lg and up'],
  'toast-max-width':['31.25rem','Frame/components/Toast/Toast.module.css L2-9'],
 },
};
const typeOf=(group,v)=>typeof v==='number'?'other':group==='focusRing'&&String(v).includes('color')?'color':'sizing';
for(const [group,entries] of Object.entries(component))studio.core[group]=Object.fromEntries(Object.entries(entries).map(([name,[value,cite]])=>[name,{value,type:typeOf(group,value),description:src(cite)}]));
write('tokens.json',studio);
const flat=Object.assign({},...Object.values(t.themes.light));
write('assets/tokens.json',flat);
write('tokens/light.css',`:root{\n${Object.entries(flat).map(([k,v])=>`  --p-${k}: ${v};`).join('\n')}\n}`);
if(fs.existsSync(source)){
 for(const f of fs.readdirSync(source+'/polaris-icons/icons'))if(f.endsWith('.svg')||f.endsWith('.yml'))fs.copyFileSync(source+'/polaris-icons/icons/'+f,'icons/'+f);
 fs.copyFileSync(source+'/LICENSE.md','licenses/SHOPIFY-LICENSE.md');
 const iconLicense=source+'/polaris-icons/LICENSE.md';if(fs.existsSync(iconLicense))fs.copyFileSync(iconLicense,'licenses/ICONS-LICENSE.md');
}
write('assets/library.json',{boards:fs.readdirSync('boards').filter(f=>f.endsWith('.svg')).sort(),components:fs.readdirSync('components').filter(f=>f.endsWith('.svg')).sort(),version:crypto.createHash('sha256').update(fs.readdirSync('boards').map(f=>fs.readFileSync('boards/'+f)).join('')).digest('hex').slice(0,12)});
write('assets/icons.json',fs.readdirSync('icons').filter(f=>f.endsWith('.svg')));
fs.copyFileSync('tools/node_modules/@shopify/polaris/build/esm/styles.css','assets/polaris.css');
fs.copyFileSync('tools/node_modules/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2','assets/inter.woff2');
fs.copyFileSync('tools/node_modules/@fontsource-variable/inter/LICENSE','licenses/INTER-OFL.txt');
await build({absWorkingDir:process.cwd(),entryPoints:['./tools/gallery.jsx'],bundle:true,minify:true,outfile:'assets/gallery.js',define:{'process.env.NODE_ENV':'"production"'},loader:{'.png':'dataurl'}});
write('raw/provenance.json',{repository:'https://github.com/Shopify/polaris-react-archive',commit:'3f7954ae42fabf26d63cee68c23ceebfd7ef0972',archiveReactVersion:'13.10.1',previewReactVersion:'13.9.5',tokens:'9.4.2',icons:'9.3.1',date:'2026-09-25',note:'Archive React version unavailable in registry; previews use published 13.9.5. Inter preview supplied by Fontsource 5.2.8; glyph version can differ from archived docs.'});
console.log('Built',Object.values(ramps).reduce((n,r)=>n+Object.keys(r).length,0),'ramp steps,',Object.values(aliases).reduce((n,a)=>n+Object.keys(a).length,0),'aliased theme colours,',Object.keys(flat).length,'light tokens and',fs.readdirSync('icons').filter(f=>f.endsWith('.svg')).length,'icons');
