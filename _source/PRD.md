# PRD — Website Souvenir Wisuda

> Versi dokumen: 1.0 · Tanggal: 20 Oktober 2026 · Target standar SEO/AEO/GEO: 2026–2027
> Placeholder yang harus diganti sebelum rilis: `[NAMA_BRAND]`, `https://www.[DOMAIN].com`, `[ALAMAT]`, `[HARGA]`, `[TAHUN_BERDIRI]`, `[AKUN_IG]`, `[AKUN_TIKTOK]`.

---

## 1. Ringkasan Produk

**[NAMA_BRAND]** adalah website katalog dan konversi untuk usaha souvenir wisuda (boneka wisuda, buket wisuda, plakat, hampers, dan souvenir custom untuk TK sampai kampus). Website bersifat **statis (HTML + Bootstrap CSS)**, tanpa keranjang belanja. Semua konversi terjadi lewat **WhatsApp ke 6282211221909**.

### 1.1 Tujuan
1. Menghasilkan chat WhatsApp berkualitas (pertanyaan paket, minta penawaran, pesan grosir).
2. Muncul di Google, Bing, dan jawaban AI (AI Overviews, ChatGPT Search, Perplexity, Gemini, Copilot) untuk pencarian seputar souvenir wisuda.
3. Membangun kepercayaan lewat galeri hasil nyata, testimoni, dan konten edukatif.

### 1.2 Target Audiens
| Segmen | Kebutuhan | Pesan utama |
|---|---|---|
| Wisudawan/wisudawati (individu) | Hadiah/souvenir wisuda untuk diri sendiri atau teman | "Kenang-kenangan wisuda yang berkesan" |
| Orang tua / keluarga | Kado untuk anak yang lulus | "Hadiah wisuda bermakna, siap kirim" |
| Panitia wisuda, sekolah, kampus, bimbel | Souvenir massal (50–1000+ pcs) | "Harga grosir, custom logo, tepat waktu" |
| Teman/pacar/sahabat | Buket & hampers wisuda | "Buket wisuda tahan lama, bisa request" |

### 1.3 KPI (90 hari pertama)
| KPI | Target |
|---|---|
| Klik tombol WhatsApp / sesi | ≥ 6% |
| Halaman terindeks Google | 100% halaman publik |
| Core Web Vitals (mobile) | LCP < 2,5 dtk · INP < 200 ms · CLS < 0,1 |
| Skor Lighthouse mobile (Perf/SEO/A11y/Best Practices) | ≥ 90 / 100 / 95 / 100 |
| Keyword halaman 1–2 (brand + "souvenir wisuda [kota]") | ≥ 10 keyword |
| Sitasi/mention di AI search untuk query brand | Dipantau bulanan (manual) |

---

## 2. Keputusan Teknis & Asumsi

| Topik | Keputusan | Alasan |
|---|---|---|
| Framework CSS | **Bootstrap 5.3.x (CSS)**, di-host sendiri (self-host) atau CDN dengan SRI | Sesuai permintaan; self-host lebih cepat & stabil |
| JavaScript | Hanya `bootstrap.bundle.min.js` (untuk toggle navbar & dropdown). Tanpa jQuery, tanpa framework JS | Dropdown/collapse Bootstrap butuh JS. Jika benar-benar ingin 0 JS, lihat §2.1 |
| Aksen interaksi tanpa JS | FAQ pakai `<details>`, lightbox galeri pakai CSS `:target` | Tetap ringan |
| Arsitektur | Situs statis multi-halaman, URL berakhiran `.html` | Sesuai permintaan struktur file |
| Penamaan file detail | **huruf kecil + tanda hubung** (`paket-boneka-wisuda.html`), bukan underscore | Google merekomendasikan hyphen sebagai pemisah kata di URL |
| Bahasa | Indonesia (`lang="id"`, locale `id_ID`) | Target pasar Indonesia |
| Konversi | WhatsApp `https://wa.me/6282211221909?text=...` | Nomor sesuai permintaan, format internasional tanpa `+`/`0` |
| Tema | Hitam dominan + aksen emas | Identik dengan toga/prestise wisuda |
| Hosting | Hosting statis apa pun (Cloudflare Pages / Netlify / cPanel). Wajib HTTPS + Brotli/Gzip | Kinerja & keamanan |
| Analitik | GA4 + Google Search Console + Bing Webmaster Tools | Ukur klik WA & indexing |

### 2.1 Opsi 0-JS (jika diminta murni CSS)
Dropdown "Paket" diganti dengan menu CSS (`:hover` + `:focus-within`) untuk desktop, dan di mobile daftar paket tampil sebagai `<details>` di dalam navbar yang dibuat sebagai checkbox-toggle. Kekurangan: aksesibilitas keyboard lebih rumit. **Default PRD ini: pakai Bootstrap bundle.**

---

## 3. Struktur Situs & URL

```
/
├── index.html                  → Beranda
├── tentang.html                → Tentang (+ kontak & lokasi)
├── paket.html                  → Daftar semua paket
├── paket/
│   ├── paket-boneka-wisuda.html
│   ├── paket-buket-wisuda.html
│   ├── paket-hampers-wisuda.html
│   ├── paket-plakat-wisuda.html
│   ├── paket-souvenir-sekolah-tk-sd.html
│   └── paket-grosir-kampus-panitia.html
├── galeri.html
├── blog.html                   → Index blog
├── blog/
│   ├── ide-souvenir-wisuda-murah-berkesan.html
│   ├── cara-memilih-boneka-wisuda.html
│   ├── harga-buket-wisuda-2026.html
│   ├── souvenir-wisuda-untuk-panitia-berapa-budget.html
│   ├── ide-kado-wisuda-untuk-pacar-sahabat.html
│   ├── tips-merawat-buket-boneka-wisuda.html
│   ├── ide-souvenir-perpisahan-sekolah.html
│   └── checklist-persiapan-hari-wisuda.html
├── 404.html
├── kebijakan-privasi.html      → (footer saja)
├── syarat-ketentuan.html       → (footer saja)
├── sitemap.xml
├── robots.txt
├── llms.txt
├── site.webmanifest
├── assets/
│   ├── css/ (bootstrap.min.css, custom.css)
│   ├── js/  (bootstrap.bundle.min.js)
│   ├── fonts/ (woff2)
│   └── img/ (webp/avif + og/)
```

Aturan URL: huruf kecil, hyphen, tanpa spasi/underscore/tahun yang membuat usang (kecuali artikel harga yang memang diperbarui tahunan), path relatif konsisten (gunakan path absolut dari root `/assets/...` agar halaman di subfolder tidak rusak), **satu canonical per halaman**, tanpa duplikat `www` vs non-`www` (pilih satu, redirect 301 yang lain).

---

## 4. Navbar (Global)

Urutan: **[Logo/Brand]** · **Beranda** · **Tentang** · **Paket ▾** · **Galeri** · **Blog** · tombol **Chat WhatsApp** (CTA).

Dropdown **Paket ▾**:
- Semua Paket → `/paket.html`
- Boneka Wisuda → `/paket/paket-boneka-wisuda.html`
- Buket Wisuda → `/paket/paket-buket-wisuda.html`
- Hampers Wisuda → `/paket/paket-hampers-wisuda.html`
- Plakat Wisuda → `/paket/paket-plakat-wisuda.html`
- Souvenir Sekolah TK/SD → `/paket/paket-souvenir-sekolah-tk-sd.html`
- Grosir Kampus & Panitia → `/paket/paket-grosir-kampus-panitia.html`

Aturan: sticky-top, latar hitam, state aktif pada halaman berjalan (`aria-current="page"`), menu "Paket" **tetap bisa diklik** ke `/paket.html` (item pertama di dropdown + link pada label di desktop), mobile = offcanvas/collapse, semua link crawlable `<a href>`.

### Elemen Global Lain
- **Tombol WhatsApp melayang** (kanan-bawah) di semua halaman.
- **Breadcrumb** di semua halaman selain beranda (HTML + JSON-LD `BreadcrumbList`).
- **Footer**: logo + deskripsi 1 kalimat, menu cepat, daftar paket, kontak (WA, jam operasional, alamat/area layanan), media sosial, link kebijakan, hak cipta.
- **Skip link** "Lewati ke konten".

---

## 5. Spesifikasi WhatsApp CTA

Format dasar: `https://wa.me/6282211221909?text=<pesan ter-encode>`
Atribut wajib pada link: `target="_blank" rel="noopener noreferrer"`, `aria-label` deskriptif, dan `data-wa-source="<lokasi>"` untuk tracking.

| Lokasi | Pesan awal (sebelum URL-encode) |
|---|---|
| Navbar / umum | Halo [NAMA_BRAND], saya ingin tanya souvenir wisuda. |
| Beranda hero | Halo [NAMA_BRAND], saya mau konsultasi paket souvenir wisuda. |
| Detail paket | Halo [NAMA_BRAND], saya tertarik dengan *[Nama Paket]*. Boleh minta info harga & ketersediaan? |
| Grosir/panitia | Halo [NAMA_BRAND], saya panitia wisuda *[nama instansi]*, butuh souvenir sekitar *[jumlah]* pcs. Mohon penawaran. |
| Blog | Halo [NAMA_BRAND], saya baca artikel *[judul]*, mau tanya soal souvenir wisuda. |

Contoh ter-encode:
```
https://wa.me/6282211221909?text=Halo%20%5BNAMA_BRAND%5D%2C%20saya%20ingin%20tanya%20souvenir%20wisuda.
```
Event analitik: `click_whatsapp` dengan parameter `source`, `page_path`, `package_name`.

---

## 6. Konten Wajib Per Halaman

> Setiap halaman memiliki **tepat satu `<h1>`**, paragraf pembuka yang menjawab langsung (untuk AEO/GEO), minimal satu CTA WhatsApp, breadcrumb, dan internal link ke minimal 3 halaman lain.

### 6.1 Beranda — `index.html`
- **Title**: `Souvenir Wisuda Custom & Murah | Boneka, Buket, Hampers – [NAMA_BRAND]` (≤ 60 karakter ideal)
- **Meta description** (140–160 karakter): ringkas layanan + USP + CTA.
- **Section berurutan**:
  1. **Hero** — H1: "Souvenir Wisuda Custom yang Bikin Hari Kelulusan Tak Terlupakan"; subjudul; 2 tombol (Chat WhatsApp, Lihat Paket); gambar hero (LCP, `fetchpriority="high"`, tanpa lazy).
  2. **Ringkasan jawaban (answer block)** — 2–3 kalimat: apa itu [NAMA_BRAND], produk, harga mulai dari, area kirim, lama produksi.
  3. **Kategori/Paket unggulan** — 6 kartu (gambar, nama, harga mulai dari, tombol Detail + WA).
  4. **Kenapa memilih kami** — 4–6 poin (custom nama/logo, bahan, harga grosir, pengiriman, revisi desain, garansi).
  5. **Cara pemesanan** — 4 langkah (Chat WA → Pilih paket & desain → DP → Produksi & kirim).
  6. **Galeri pilihan** — 6–8 foto + link ke `/galeri.html`.
  7. **Testimoni** — 3–6 testimoni nyata (nama, instansi, foto bila ada izin). Tandai `Review` schema hanya jika benar-benar nyata & terlihat di halaman.
  8. **Klien/instansi** — logo kampus/sekolah (jika diizinkan).
  9. **Artikel terbaru** — 3 kartu blog.
  10. **FAQ** — 6–8 pertanyaan (lihat §7.4).
  11. **CTA penutup** — banner hitam-emas + tombol WA.
- **Schema**: `Organization` + `WebSite` + `LocalBusiness/Store` + `ItemList` (paket) + `FAQPage` + `BreadcrumbList` (tidak perlu di beranda).

### 6.2 Tentang — `tentang.html`
- **H1**: "Tentang [NAMA_BRAND]: Pembuat Souvenir Wisuda Custom Sejak [TAHUN_BERDIRI]"
- **Section**:
  1. Cerita singkat & misi (siapa, sejak kapan, kenapa).
  2. **Fakta cepat** (tabel/definition list): tahun berdiri, jumlah pesanan/klien terlayani, produk, area pengiriman, kapasitas produksi, jam operasional.
  3. Nilai & standar kualitas (bahan, QC, proses).
  4. **Tim/pemilik** — nama, foto, peran (sinyal E-E-A-T).
  5. Proses produksi (foto di balik layar).
  6. Legalitas/badge bila ada (NIB, marketplace, dll).
  7. **Kontak & lokasi** — alamat lengkap (NAP konsisten dengan Google Business Profile), peta (embed hanya jika tidak merusak CWV; gunakan `loading="lazy"` atau tautan), jam buka, WA, IG, TikTok.
  8. FAQ singkat + CTA WA.
- **Schema**: `AboutPage`, `Organization` (dengan `sameAs`, `founder`, `contactPoint`), `LocalBusiness`, `BreadcrumbList`.

### 6.3 Daftar Paket — `paket.html`
- **H1**: "Paket Souvenir Wisuda: Boneka, Buket, Hampers & Custom Grosir"
- **Section**:
  1. Intro jawaban langsung (kisaran harga, minimal order, waktu produksi).
  2. **Grid kartu paket** (6 paket): foto, nama, harga mulai dari, isi singkat 3 poin, label ("Terlaris", "Grosir"), tombol Detail + WA.
  3. **Tabel perbandingan paket** (harga, isi, minimal order, estimasi pengerjaan, cocok untuk) — tabel HTML sungguhan (bagus untuk AEO).
  4. Panduan memilih paket (3 skenario: pribadi, kado, panitia).
  5. Info harga grosir (tier: 10–49, 50–99, 100+).
  6. Syarat pemesanan (DP, revisi, pengiriman, estimasi).
  7. FAQ paket + CTA.
- **Schema**: `CollectionPage` + `ItemList` (setiap item `url` ke detail) + `BreadcrumbList` + `FAQPage`.

### 6.4 Detail Paket — `paket/<nama-paket>.html`
Template tunggal untuk semua paket:
- **H1**: "[Nama Paket] – Souvenir Wisuda [Kategori]"
- **Section**:
  1. **Ringkasan** (answer block): apa isinya, untuk siapa, harga mulai, minimal order, estimasi pengerjaan.
  2. **Galeri produk** (3–6 foto + 1 video pendek opsional; alt deskriptif unik).
  3. **Isi paket** (daftar item + ukuran + bahan).
  4. **Spesifikasi** (tabel: ukuran, bahan, warna, opsi kustom, berat).
  5. **Harga** — tabel tier + keterangan "harga belum termasuk ongkir"; tanggal pembaruan harga.
  6. **Opsi kustomisasi** — nama, tanggal, logo, warna toga, ucapan, kemasan.
  7. **Cocok untuk** (skenario penggunaan).
  8. **Cara pesan** (4 langkah) + tombol WA besar (pesan memuat nama paket).
  9. **Estimasi produksi & pengiriman**, kebijakan revisi/retur.
  10. **Testimoni** terkait paket.
  11. **FAQ paket** (4–6 Q&A spesifik).
  12. **Paket terkait** (3 kartu) + artikel blog terkait (2 kartu).
- **Schema**: `Product` + `Offer` (price, `priceCurrency: IDR`, `availability`, `itemCondition`, `url`, `seller`, `priceValidUntil`, `shippingDetails` & `hasMerchantReturnPolicy` bila kebijakan jelas), `BreadcrumbList`, `FAQPage`, `AggregateRating`/`Review` **hanya** jika ulasan asli tampil di halaman.
- Jika harga "mulai dari": tampilkan harga dasar paket terendah sebagai `Offer.price` dan jelaskan variasi di teks.

### 6.5 Galeri — `galeri.html`
- **H1**: "Galeri Souvenir Wisuda: Hasil Pesanan Nyata Pelanggan Kami"
- **Section**:
  1. Intro singkat (jumlah karya, kategori).
  2. **Filter kategori** (link-anchor/`:target` tanpa JS: Semua, Boneka, Buket, Hampers, Plakat, Sekolah, Grosir).
  3. **Grid foto** 12–36 foto, thumbnail webp + `width/height`, `loading="lazy"`, `alt` unik (contoh: "Boneka wisuda custom toga hitam nama Rina, Universitas X"), caption singkat (paket + instansi + tahun).
  4. **Lightbox CSS** (`:target`) dengan tombol tutup, navigasi berikutnya/sebelumnya.
  5. Video/Reel (embed ringan, tautan ke Instagram/TikTok) opsional.
  6. CTA: "Mau desain seperti ini? Chat kami."
- **Schema**: `CollectionPage` + `ImageGallery` dengan `ImageObject` (`contentUrl`, `caption`, `creator`, `copyrightNotice`, `license` bila relevan), `BreadcrumbList`.
- Sitemap gambar: daftarkan gambar utama di `sitemap.xml` (`image:image`).

### 6.6 Blog — `blog.html`
- **H1**: "Blog Souvenir Wisuda: Ide, Tips & Panduan Memilih Kado Kelulusan"
- **Section**: intro; artikel unggulan (hero card); grid artikel (judul, ringkasan 20–30 kata, kategori, tanggal, waktu baca, gambar); kategori (Ide, Tips, Panduan Harga, Panitia); paginasi `?page` **tidak** dipakai; gunakan `blog.html`, lalu `blog/halaman-2.html` jika perlu; CTA WA.
- **Schema**: `Blog` + `ItemList` + `BreadcrumbList`.

### 6.7 Detail Blog — `blog/<slug>.html`
- **H1** = judul artikel (selaras dengan `<title>`).
- **Struktur wajib**:
  1. Byline: penulis (nama + link ke Tentang), tanggal terbit, **tanggal diperbarui**, waktu baca.
  2. **TL;DR / jawaban singkat** (40–60 kata) tepat di bawah H1.
  3. Daftar isi (anchor link).
  4. Isi dengan H2/H3 berbentuk pertanyaan atau pernyataan jelas; paragraf pendek; minimal 1 tabel/daftar; foto asli.
  5. Kotak **"Rekomendasi paket"** dengan link internal ke detail paket + CTA WA.
  6. FAQ (3–5 Q&A).
  7. Penulis (bio singkat), artikel terkait (3), daftar sumber/referensi bila ada klaim data.
- Panjang: 800–1.500 kata; perbarui artikel harga setiap awal tahun.
- **Schema**: `BlogPosting` (`headline`, `description`, `image`, `datePublished`, `dateModified`, `author` Person dengan `url`, `publisher` Organization + `logo`, `mainEntityOfPage`, `inLanguage`, `articleSection`, `keywords`), `BreadcrumbList`, `FAQPage` bila ada FAQ.

### 6.8 Halaman Pendukung
- `404.html`: pesan ramah, link ke Beranda/Paket/Blog, CTA WA, `noindex`.
- `kebijakan-privasi.html` & `syarat-ketentuan.html`: UU PDP Indonesia (data hanya nomor/chat WA), kebijakan DP, revisi, pembatalan, pengiriman. Sinyal kepercayaan.

---

## 7. SEO, AEO, GEO — Spesifikasi Lengkap

> Catatan jujur: tidak ada metode yang menjamin ranking atau sitasi AI. Semua poin di bawah adalah praktik terbaik per Oktober 2026. Pantau perubahan di Google Search Central.

### 7.1 SEO Teknis
- HTTPS, 1 versi domain, redirect 301 `http→https` dan `www↔non-www`.
- `robots.txt` dan `sitemap.xml` (hanya URL 200 yang indexable; `lastmod` akurat; kirim ke Search Console & Bing).
- `<link rel="canonical">` self-referencing di semua halaman; hindari parameter URL.
- `<html lang="id">`, `<link rel="alternate" hreflang="id-ID">` + `x-default` (opsional untuk situs 1 bahasa, tetap aman).
- Meta robots: `index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1`; `404.html` → `noindex`.
- Viewport meta, `theme-color`, favicon (`.ico` + SVG + `apple-touch-icon` 180px), `site.webmanifest`.
- HTML valid & semantik: `header`, `nav`, `main`, `article`, `section`, `footer`; satu `h1`, hierarki heading berurutan.
- Gambar: WebP/AVIF, `srcset` + `sizes`, `width`/`height` eksplisit (cegah CLS), `loading="lazy"` kecuali LCP, `decoding="async"`, nama file deskriptif (`boneka-wisuda-custom-toga-hitam.webp`), `alt` informatif.
- Performa: self-host font woff2 + `font-display: swap` + preload font utama; hanya muat CSS yang dipakai; Bootstrap JS dengan `defer`; cache `Cache-Control: max-age=31536000, immutable` untuk aset ber-hash; Brotli.
- Core Web Vitals: LCP < 2,5 dtk, INP < 200 ms, CLS < 0,1. Hindari embed berat di atas lipatan.
- Keamanan header: HSTS, `X-Content-Type-Options`, `Referrer-Policy: strict-origin-when-cross-origin`, CSP dasar.
- Tautan internal: setiap halaman terjangkau ≤ 3 klik; anchor text deskriptif; tidak ada orphan page.
- Tautan WA `rel="noopener noreferrer"` (tambahkan `nofollow` tidak wajib).
- IndexNow (Bing/Yandex/Copilot) saat mempublikasikan artikel/paket baru.

### 7.2 SEO On-Page — Pola Title & Description
| Halaman | Pola title | Pola description |
|---|---|---|
| Beranda | `Souvenir Wisuda Custom & Murah \| [NAMA_BRAND]` | USP + kategori + area + CTA |
| Tentang | `Tentang [NAMA_BRAND] – Pembuat Souvenir Wisuda Sejak [TAHUN]` | Cerita + pengalaman + lokasi |
| Paket | `Paket Souvenir Wisuda Boneka, Buket & Hampers \| [NAMA_BRAND]` | Kisaran harga + jenis paket |
| Detail paket | `[Nama Paket] – Harga & Isi Paket \| [NAMA_BRAND]` | Isi, harga mulai, minimal order |
| Galeri | `Galeri Souvenir Wisuda – Hasil Pesanan Nyata \| [NAMA_BRAND]` | Jumlah karya + kategori |
| Blog | `Blog Souvenir Wisuda: Ide & Tips Kado Kelulusan \| [NAMA_BRAND]` | Topik utama blog |
| Detail blog | `[Judul Artikel] ([Tahun]) \| [NAMA_BRAND]` | Jawaban ringkas + manfaat |

Riset keyword awal: souvenir wisuda, souvenir wisuda murah, boneka wisuda custom, buket wisuda, hampers wisuda, kado wisuda, souvenir wisuda sekolah, souvenir wisuda kampus, souvenir wisuda grosir, plakat wisuda, harga boneka wisuda, souvenir perpisahan sekolah (+ modifier kota/area layanan). Satu keyword utama per halaman, hindari kanibalisasi.

### 7.3 Open Graph & Social
Wajib di semua halaman:
```
og:type (website | article), og:site_name, og:locale=id_ID, og:title, og:description,
og:url (= canonical), og:image (1200×630, <1 MB, absolut https), og:image:width/height,
og:image:alt, twitter:card=summary_large_image, twitter:title, twitter:description,
twitter:image, twitter:image:alt
```
Khusus artikel: `article:published_time`, `article:modified_time`, `article:author`, `article:section`, `article:tag`.
Khusus produk: `og:type=website` (aman) atau `product` dengan `product:price:amount`/`product:price:currency=IDR` (opsional, dipakai Pinterest/Meta).
Buat gambar OG unik per halaman (hitam-emas, judul + logo).

### 7.4 AEO (Answer Engine Optimization)
- **Answer block** 40–60 kata tepat di bawah H1 setiap halaman penting: jawab "Apa", "Berapa harga", "Berapa lama", "Untuk siapa".
- Heading berbentuk pertanyaan nyata ("Berapa harga buket wisuda?").
- Format ekstraktabel: tabel harga, daftar langkah bernomor, definition list, kalimat berdiri sendiri (tidak bergantung konteks).
- Bagian **FAQ** nyata di halaman Beranda, Paket, Detail Paket, Detail Blog. Contoh pertanyaan inti:
  1. Berapa minimal order souvenir wisuda?
  2. Berapa lama pengerjaan?
  3. Apakah bisa custom nama dan logo kampus?
  4. Bagaimana sistem pembayaran (DP) dan pengiriman?
  5. Apakah ada harga grosir untuk panitia?
  6. Berapa harga boneka/buket wisuda? 
  7. Apakah bisa revisi desain?
  8. Area pengiriman mana saja?
- **Status FAQ schema 2026**: Google menghentikan tampilan FAQ rich result sejak **7 Mei 2026**; markup `FAQPage` tidak merugikan dan tetap dibaca sebagai sinyal pemahaman, serta dipakai mesin AI. **Keputusan**: tetap sertakan `FAQPage` JSON-LD, **namun teks FAQ wajib terlihat di halaman** dan tidak boleh dijadikan satu-satunya strategi.
- Jangan pakai `HowTo` schema (sudah dihentikan Google), cukup gunakan daftar bernomor HTML biasa.

### 7.5 GEO (Generative Engine Optimization)
- **Konsistensi entitas**: nama brand, alamat, nomor WA, deskripsi sama di website, Google Business Profile, Instagram, TikTok, marketplace. Tautkan lewat `sameAs`.
- **Sinyal E-E-A-T**: halaman Tentang lengkap, nama penulis + bio, foto proses nyata, testimoni nyata, tanggal diperbarui.
- **Konten orisinal**: foto & data sendiri (mis. "kisaran harga 2026 berdasarkan 200+ pesanan"), bukan konten generik.
- **Kejelasan klaim**: sebut angka, tanggal, satuan; sertakan sumber untuk data eksternal.
- **Kesegaran**: `dateModified` jujur; review artikel harga tiap Januari.
- **Akses crawler AI** (`robots.txt`): izinkan `OAI-SearchBot`, `GPTBot`, `ChatGPT-User`, `PerplexityBot`, `Perplexity-User`, `ClaudeBot`, `Claude-SearchBot`, `Google-Extended`, `Applebot-Extended`, `Bingbot` — *keputusan bisnis*: jika tidak ingin dipakai untuk pelatihan model, blokir hanya `GPTBot`, `Google-Extended`, `ClaudeBot`, `Applebot-Extended` namun biarkan crawler "search" tetap diizinkan.
- **`llms.txt`** di root (ringkasan situs + tautan halaman penting dalam Markdown). Status: standar usulan, belum dikonfirmasi dipakai Google; biaya kecil, manfaat belum pasti.
- **Brand mention eksternal**: daftar di Google Business Profile, marketplace (Tokopedia/Shopee), direktori lokal, dapatkan ulasan Google; AI search sering mengutip sumber pihak ketiga.
- **Server-rendered HTML**: semua konten penting ada di HTML awal (bukan dimuat JS) — sudah terpenuhi karena situs statis.
- Pantau: tanya 10 pertanyaan target ke ChatGPT, Perplexity, Gemini, AI Overviews tiap bulan; catat apakah brand tersitasi.

### 7.6 Structured Data (JSON-LD) — Peta per Halaman
Gunakan **satu blok `<script type="application/ld+json">` dengan `@graph`** dan `@id` saling terhubung.

| Halaman | Tipe schema |
|---|---|
| Semua | `Organization`/`LocalBusiness` (via `@id` global), `WebSite`, `WebPage` (+ subtipe), `BreadcrumbList` |
| Beranda | `WebSite`, `Organization`, `LocalBusiness`, `ItemList`, `FAQPage` |
| Tentang | `AboutPage`, `Organization` (`founder`, `sameAs`, `contactPoint`) |
| Paket | `CollectionPage`, `ItemList`, `FAQPage` |
| Detail paket | `Product`, `Offer`, `FAQPage`, `Review` (jika nyata) |
| Galeri | `CollectionPage`, `ImageGallery`, `ImageObject` |
| Blog | `Blog`, `ItemList` |
| Detail blog | `BlogPosting`, `Person` (penulis), `FAQPage` |

Aturan: data JSON-LD **harus sama** dengan konten yang terlihat; jangan memasang `AggregateRating` tanpa ulasan nyata; jangan memakai `SearchAction` (fitur sitelinks search box dihentikan Google); validasi di validator.schema.org dan Rich Results Test (tipe yang masih didukung).

### 7.7 Contoh `<head>` Standar (Detail Paket)
```html
<!DOCTYPE html>
<html lang="id" data-bs-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Paket Boneka Wisuda Custom – Harga & Isi Paket | [NAMA_BRAND]</title>
  <meta name="description" content="Paket boneka wisuda custom nama & logo kampus, harga mulai Rp[HARGA], minimal order 1 pcs, pengerjaan 3–5 hari. Pesan via WhatsApp.">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="theme-color" content="#0B0B0C">
  <link rel="canonical" href="https://www.[DOMAIN].com/paket/paket-boneka-wisuda.html">
  <link rel="alternate" hreflang="id-ID" href="https://www.[DOMAIN].com/paket/paket-boneka-wisuda.html">
  <link rel="alternate" hreflang="x-default" href="https://www.[DOMAIN].com/paket/paket-boneka-wisuda.html">

  <!-- Open Graph / Twitter -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="[NAMA_BRAND]">
  <meta property="og:locale" content="id_ID">
  <meta property="og:title" content="Paket Boneka Wisuda Custom | [NAMA_BRAND]">
  <meta property="og:description" content="Boneka wisuda custom nama & logo kampus. Pesan mudah via WhatsApp.">
  <meta property="og:url" content="https://www.[DOMAIN].com/paket/paket-boneka-wisuda.html">
  <meta property="og:image" content="https://www.[DOMAIN].com/assets/img/og/paket-boneka-wisuda.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Boneka wisuda custom berpakaian toga hitam">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Paket Boneka Wisuda Custom | [NAMA_BRAND]">
  <meta name="twitter:description" content="Boneka wisuda custom nama & logo kampus.">
  <meta name="twitter:image" content="https://www.[DOMAIN].com/assets/img/og/paket-boneka-wisuda.jpg">

  <!-- Icons -->
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="icon" href="/assets/img/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <!-- CSS -->
  <link rel="preload" href="/assets/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="/assets/css/custom.css">

  <script type="application/ld+json">{ ...lihat §8... }</script>
</head>
```

---

## 8. Contoh JSON-LD

### 8.1 Global (Beranda) — Organization + LocalBusiness + WebSite
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://www.[DOMAIN].com/#website",
      "url": "https://www.[DOMAIN].com/",
      "name": "[NAMA_BRAND]",
      "inLanguage": "id-ID",
      "publisher": { "@id": "https://www.[DOMAIN].com/#org" }
    },
    {
      "@type": ["Organization", "Store"],
      "@id": "https://www.[DOMAIN].com/#org",
      "name": "[NAMA_BRAND]",
      "url": "https://www.[DOMAIN].com/",
      "logo": { "@type": "ImageObject", "url": "https://www.[DOMAIN].com/assets/img/logo.png", "width": 512, "height": 512 },
      "image": "https://www.[DOMAIN].com/assets/img/og/home.jpg",
      "description": "Pembuat souvenir wisuda custom: boneka, buket, hampers, plakat, dan paket grosir.",
      "telephone": "+6282211221909",
      "priceRange": "Rp",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[ALAMAT]",
        "addressLocality": "[KOTA]",
        "addressRegion": "[PROVINSI]",
        "postalCode": "[KODE_POS]",
        "addressCountry": "ID"
      },
      "areaServed": { "@type": "Country", "name": "Indonesia" },
      "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
        "opens": "08:00", "closes": "17:00"
      }],
      "contactPoint": [{
        "@type": "ContactPoint",
        "contactType": "customer service",
        "telephone": "+6282211221909",
        "availableLanguage": ["id"],
        "url": "https://wa.me/6282211221909"
      }],
      "sameAs": ["https://www.instagram.com/[AKUN_IG]", "https://www.tiktok.com/@[AKUN_TIKTOK]"]
    }
  ]
}
```
Jika usaha tidak menerima kunjungan, hapus tipe `Store` + `openingHoursSpecification` dan pakai `Organization` dengan `areaServed`.

### 8.2 Detail Paket — Product + Breadcrumb + FAQ
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "@id": "https://www.[DOMAIN].com/paket/paket-boneka-wisuda.html#product",
      "name": "Paket Boneka Wisuda Custom",
      "description": "Boneka wisuda custom nama dan logo kampus, lengkap toga dan kemasan.",
      "image": ["https://www.[DOMAIN].com/assets/img/paket/boneka-1.webp"],
      "brand": { "@type": "Brand", "name": "[NAMA_BRAND]" },
      "sku": "BONEKA-001",
      "category": "Souvenir Wisuda",
      "offers": {
        "@type": "Offer",
        "url": "https://www.[DOMAIN].com/paket/paket-boneka-wisuda.html",
        "priceCurrency": "IDR",
        "price": "[HARGA_ANGKA]",
        "priceValidUntil": "2027-12-31",
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition",
        "seller": { "@id": "https://www.[DOMAIN].com/#org" }
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Beranda", "item": "https://www.[DOMAIN].com/" },
        { "@type": "ListItem", "position": 2, "name": "Paket", "item": "https://www.[DOMAIN].com/paket.html" },
        { "@type": "ListItem", "position": 3, "name": "Paket Boneka Wisuda" }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "Berapa lama pengerjaan boneka wisuda custom?",
        "acceptedAnswer": { "@type": "Answer", "text": "Pengerjaan 3–5 hari kerja untuk 1–20 pcs. Jumlah lebih besar mengikuti kesepakatan." }
      }]
    }
  ]
}
```

### 8.3 Detail Blog — BlogPosting
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://www.[DOMAIN].com/blog/harga-buket-wisuda-2026.html#article",
  "headline": "Harga Buket Wisuda 2026: Kisaran & Tips Memilih",
  "description": "Kisaran harga buket wisuda 2026 per jenis dan tips memilih.",
  "image": ["https://www.[DOMAIN].com/assets/img/blog/harga-buket-wisuda-2026.webp"],
  "datePublished": "2026-10-20T08:00:00+07:00",
  "dateModified": "2026-10-20T08:00:00+07:00",
  "inLanguage": "id-ID",
  "author": { "@type": "Person", "name": "[NAMA_PENULIS]", "url": "https://www.[DOMAIN].com/tentang.html" },
  "publisher": { "@id": "https://www.[DOMAIN].com/#org" },
  "mainEntityOfPage": "https://www.[DOMAIN].com/blog/harga-buket-wisuda-2026.html",
  "articleSection": "Panduan Harga",
  "keywords": ["buket wisuda", "harga buket wisuda"]
}
```

---

## 9. File Pendukung

**robots.txt**
```
User-agent: *
Allow: /
Disallow: /404.html

# Crawler AI pencarian (diizinkan)
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Claude-SearchBot
Allow: /

# Opsional: blokir pelatihan model (ubah sesuai kebijakan)
# User-agent: GPTBot
# Disallow: /
# User-agent: Google-Extended
# Disallow: /
# User-agent: ClaudeBot
# Disallow: /

Sitemap: https://www.[DOMAIN].com/sitemap.xml
```

**sitemap.xml** — berisi semua halaman indexable dengan `<lastmod>` akurat dan, untuk galeri/paket, `<image:image>`.

**llms.txt** (Markdown, di root)
```
# [NAMA_BRAND]
> Pembuat souvenir wisuda custom (boneka, buket, hampers, plakat) dengan pemesanan via WhatsApp 6282211221909.

## Halaman Utama
- [Paket](https://www.[DOMAIN].com/paket.html): daftar paket, harga mulai, minimal order
- [Tentang](https://www.[DOMAIN].com/tentang.html): profil, kontak, lokasi
- [Blog](https://www.[DOMAIN].com/blog.html): panduan dan ide souvenir wisuda
```

---

## 10. Persyaratan Non-Fungsional

| Area | Persyaratan |
|---|---|
| Responsif | Mobile-first; uji 360, 390, 768, 1024, 1440 px; >70% trafik diperkirakan mobile |
| Aksesibilitas | WCAG 2.2 AA: kontras ≥ 4,5:1, fokus terlihat, skip link, `alt`, label `aria`, target sentuh ≥ 44 px, hormati `prefers-reduced-motion` |
| Browser | 2 versi terbaru Chrome, Safari, Firefox, Edge; Android WebView |
| Privasi | Banner persetujuan hanya jika memakai pelacak non-esensial; patuhi UU PDP |
| Keamanan | Tanpa form/penyimpanan data; semua link eksternal `noopener` |
| Pemeliharaan | Konten paket/harga di satu template; log perubahan harga; review konten kuartalan |

---

## 11. Rencana Rilis

| Fase | Isi | Durasi |
|---|---|---|
| 1. Fondasi | Design system (`design.md`), template head, navbar/footer, aset | 3–4 hari |
| 2. Halaman inti | Beranda, Tentang, Paket + 6 detail, Galeri | 5–7 hari |
| 3. Blog | Index + 8 artikel awal | 5–7 hari |
| 4. SEO & QA | Schema, sitemap, OG, CWV, a11y, tes tautan WA | 2–3 hari |
| 5. Peluncuran | Search Console, Bing, GBP, IndexNow, GA4 event WA | 1 hari |
| 6. Pasca-rilis | Pantau 30/60/90 hari, 2 artikel/bulan | berkelanjutan |

---

## 12. Checklist Penerimaan (Definition of Done)

- [ ] Navbar identik di semua halaman; dropdown Paket berfungsi di desktop & mobile.
- [ ] Semua tombol WA membuka `wa.me/6282211221909` dengan pesan yang sesuai halaman.
- [ ] Struktur file sesuai §3; semua tautan internal valid (tidak ada 404).
- [ ] Setiap halaman: 1 H1, title & description unik, canonical, OG + Twitter lengkap, JSON-LD valid.
- [ ] Answer block & FAQ tampil nyata di halaman yang ditentukan.
- [ ] Gambar: WebP/AVIF, `alt`, `width/height`, lazy (selain LCP).
- [ ] `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html`, manifest tersedia.
- [ ] Lighthouse mobile ≥ target KPI; CWV hijau.
- [ ] Teks semua `alt`, kontras, dan fokus keyboard lulus uji.
- [ ] Search Console & Bing Webmaster terverifikasi; sitemap terkirim.
- [ ] Google Business Profile dibuat/diselaraskan dengan NAP di website.
- [ ] Event `click_whatsapp` tercatat di GA4.

---

## 13. Risiko & Mitigasi

| Risiko | Mitigasi |
|---|---|
| Konten tipis/duplikat antar paket | Tulis deskripsi unik, foto unik, FAQ spesifik per paket |
| Harga usang | Tampilkan "diperbarui [tanggal]", review kuartalan |
| Schema tidak sesuai konten | Generate dari data yang sama, validasi sebelum rilis |
| Ketergantungan WA tunggal | Tambahkan fallback telepon/IG di footer |
| Perubahan kebijakan Google/AI search | Fokus pada konten bermanfaat; pantau Search Central |
