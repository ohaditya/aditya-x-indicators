# Aditya X Indicators — Vercel

Migrasi dari Streamlit ke Next.js/React untuk deployment di Vercel. Konten, data, teks, aset, warna, layout, komponen, link, dan alur utama dari aplikasi Streamlit dipertahankan. Fitur Streamlit yang tidak relevan di web statis (column/layout primitives, expander, link_button, media rendering) direalisasikan dengan HTML/CSS/React yang setara.

## Struktur

- `app/` — halaman dan styling Next.js
- `public/assets/` — seluruh aset dari project asli
- `package.json` — dependency dan script
- `vercel.json` — konfigurasi Vercel
- `.env.example` — template environment variable

## Jalankan lokal

```bash
npm install
npm run build
npm start
```

Untuk mode development:

```bash
npm run dev
```

## Deploy ke Vercel

1. Upload/push folder project ini ke GitHub atau import project dari folder tersebut ke Vercel.
2. Vercel akan mendeteksi Next.js.
3. Build command: `next build`.
4. Install command: `npm install`.
5. Tidak ada secret/API key yang diperlukan oleh versi ini. Jika nanti ditambahkan, simpan di Vercel Environment Variables dan jangan commit nilai secret.

## Catatan aset

Project asli tidak menyertakan `assets/background`, `assets/indicator`, atau `assets/logo.png`, sehingga tidak dibuat-buat pada versi migrasi. Profile, testimonial, video, dan broker asset yang memang ada di archive dipertahankan.
