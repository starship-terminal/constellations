import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
import {build} from 'esbuild';
import {fileURLToPath} from 'node:url';
// Paths below are relative to the package folder; dependencies live in tools/node_modules.
process.chdir(path.join(path.dirname(fileURLToPath(import.meta.url)),'..'));
const require=createRequire(import.meta.url), t=require('@shopify/polaris-tokens');
const source='/tmp/polaris-reference-source-20260925';
const write=(p,v)=>fs.writeFileSync(p,typeof v==='string'?v:JSON.stringify(v,null,2));
for(const dir of ['assets','tokens','icons','licenses'])fs.mkdirSync(dir,{recursive:true});
write('tokens/polaris-themes.raw.json',t.themes);
write('tokens/polaris-metadata.json',t.metaThemes);
const studio={};
for(const [theme,groups] of Object.entries(t.themes)){
 const out={};
 for(const [group,values] of Object.entries(groups)){out[group]={};for(const [name,value]of Object.entries(values)){
 let type=group==='color'&&name!=='color-scheme'?'color':name.includes('font-family')?'fontFamilies':name.includes('font-weight')?'fontWeights':name.includes('radius')?'borderRadius':name.includes('font-size')?'fontSizes':group==='space'?'spacing':/^[-\d.]+(rem|px)$/.test(value)?'sizing':'other';
 out[group][name]={value,type,description:`@shopify/polaris-tokens 9.4.2 / ${theme}`};
 }}studio[theme]=out;
}
write('tokens/polaris.tokens-studio.json',studio);
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
write('evidence/provenance.json',{repository:'https://github.com/Shopify/polaris-react-archive',commit:'3f7954ae42fabf26d63cee68c23ceebfd7ef0972',archiveReactVersion:'13.10.1',previewReactVersion:'13.9.5',tokens:'9.4.2',icons:'9.3.1',date:'2026-09-25',note:'Archive React version unavailable in registry; previews use published 13.9.5. Inter preview supplied by Fontsource 5.2.8; glyph version can differ from archived docs.'});
console.log('Built',Object.keys(flat).length,'light tokens and',fs.readdirSync('icons').filter(f=>f.endsWith('.svg')).length,'icons');
