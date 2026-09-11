import { access, readdir } from 'node:fs/promises';
const required=['index.html','styles.css','script.js','public/assets/profile','public/assets/testimonials','public/assets/videos','public/assets/broker'];
for(const p of required) await access(p);
for(const d of ['public/assets/profile','public/assets/testimonials','public/assets/videos','public/assets/broker']){
  const files=await readdir(d); if(!files.length) throw new Error(`Missing assets in ${d}`);
}
console.log('Static build verified: HTML, CSS, JS and all supplied media assets are present.');
