# design.md — Design System Website Souvenir Wisuda

> Acuan visual untuk implementasi **Bootstrap 5.3 (CSS)**. Tema: **hitam dominan + aksen emas**, elegan, bersih, fokus ke foto produk.
> Mode: gelap permanen (`<html data-bs-theme="dark">`).

---

## 1. Prinsip Desain
1. **Hitam sebagai kanvas, foto sebagai bintang** — latar gelap membuat foto produk (boneka, buket, plakat) menonjol.
2. **Emas hanya untuk hal penting** — CTA, judul section, ikon, garis aksen. Maksimal ~10% permukaan.
3. **Konversi jelas** — tombol WhatsApp selalu terlihat dan konsisten.
4. **Ringan** — tanpa efek berat; custom CSS < 15 KB; 2 font saja.
5. **Mobile-first & aksesibel** — kontras tinggi, target sentuh besar.

---

## 2. Design Tokens

### 2.1 Warna
| Token | Hex | Pemakaian |
|---|---|---|
| `--wd-black` | `#0B0B0C` | Latar utama body |
| `--wd-surface` | `#141416` | Kartu, navbar, section selang-seling |
| `--wd-surface-2` | `#1C1C1F` | Hover kartu, input, tabel zebra |
| `--wd-border` | `#2A2A2E` | Garis tipis, divider |
| `--wd-gold` | `#C9A24B` | Aksen utama, tombol primer, ikon |
| `--wd-gold-light` | `#E3C373` | Hover emas, gradien teks |
| `--wd-gold-dark` | `#9C7A2F` | Active/pressed |
| `--wd-text` | `#F4F1EA` | Teks utama (putih hangat) |
| `--wd-text-muted` | `#A9A59B` | Teks sekunder (kontras ≥ 4,5:1 di `#0B0B0C`) |
| `--wd-wa` | `#25D366` | Tombol WhatsApp (khusus) |
| `--wd-wa-dark` | `#1EBE5A` | Hover WhatsApp |
| `--wd-danger` | `#E5534B` | Error/penting |

Rasio kontras: teks `#F4F1EA` di `#0B0B0C` ≈ 17:1; emas `#C9A24B` di hitam ≈ 8:1; teks hitam di tombol emas ≈ 8:1; teks hitam di tombol WA hijau ≈ 10:1 (gunakan teks gelap, bukan putih).

### 2.2 Tipografi
| Peran | Font | Bobot | Catatan |
|---|---|---|---|
| Heading (H1–H3, brand) | **Playfair Display** | 600, 700 | Serif elegan, nuansa wisuda |
| Body, UI, tombol | **Inter** (variable) | 400, 500, 600 | Terbaca di layar kecil |
| Fallback | `Georgia, serif` / `system-ui, sans-serif` | | |

Self-host `woff2`, subset Latin, `font-display: swap`, preload 1 font body.

Skala (mobile → desktop, gunakan `clamp()`):
| Elemen | Ukuran | Line-height |
|---|---|---|
| H1 | `clamp(2rem, 4vw + 1rem, 3.5rem)` | 1.15 |
| H2 | `clamp(1.6rem, 2.5vw + 1rem, 2.5rem)` | 1.2 |
| H3 | `clamp(1.25rem, 1.5vw + 1rem, 1.75rem)` | 1.3 |
| Body | `1rem` (16px), desktop `1.0625rem` | 1.65 |
| Small | `0.875rem` | 1.5 |
| Eyebrow (label atas heading) | `0.8rem`, uppercase, `letter-spacing: .14em`, emas | |

### 2.3 Spacing, Radius, Shadow
| Token | Nilai |
|---|---|
| Spacing section | `py-5` mobile, `py-6` custom (`5rem`) desktop |
| Container | Bootstrap `.container` (max 1140/1320) |
| Radius kecil / sedang / besar | `8px` / `14px` / `22px`; tombol pill `999px` |
| Shadow kartu | `0 10px 30px rgba(0,0,0,.45)` |
| Glow emas (hover) | `0 0 0 1px var(--wd-gold), 0 12px 32px rgba(201,162,75,.18)` |
| Garis aksen | `1px solid var(--wd-border)`; garis emas `2px` pendek di bawah heading |

### 2.4 Breakpoint (Bootstrap)
`xs <576` · `sm ≥576` · `md ≥768` · `lg ≥992` · `xl ≥1200` · `xxl ≥1400`

---

## 3. Override Bootstrap (`assets/css/custom.css`)

```css
:root,
[data-bs-theme="dark"] {
  --wd-black: #0B0B0C;
  --wd-surface: #141416;
  --wd-surface-2: #1C1C1F;
  --wd-border: #2A2A2E;
  --wd-gold: #C9A24B;
  --wd-gold-light: #E3C373;
  --wd-gold-dark: #9C7A2F;
  --wd-text: #F4F1EA;
  --wd-text-muted: #A9A59B;
  --wd-wa: #25D366;
  --wd-wa-dark: #1EBE5A;

  --bs-body-bg: var(--wd-black);
  --bs-body-color: var(--wd-text);
  --bs-body-font-family: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --bs-body-font-size: 1rem;
  --bs-body-line-height: 1.65;
  --bs-heading-color: var(--wd-text);
  --bs-border-color: var(--wd-border);
  --bs-link-color: var(--wd-gold);
  --bs-link-hover-color: var(--wd-gold-light);
  --bs-secondary-color: var(--wd-text-muted);
  --bs-tertiary-bg: var(--wd-surface);
  --bs-border-radius: 14px;
}

body { background: var(--wd-black); }

h1, h2, h3, .display-font {
  font-family: "Playfair Display", Georgia, serif;
  font-weight: 700;
  letter-spacing: -.01em;
}
h1 { font-size: clamp(2rem, 4vw + 1rem, 3.5rem); line-height: 1.15; }
h2 { font-size: clamp(1.6rem, 2.5vw + 1rem, 2.5rem); line-height: 1.2; }
h3 { font-size: clamp(1.25rem, 1.5vw + 1rem, 1.75rem); line-height: 1.3; }

.section { padding-block: 3.5rem; }
@media (min-width: 992px) { .section { padding-block: 5rem; } }
.section-alt { background: var(--wd-surface); }

.eyebrow {
  color: var(--wd-gold);
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: .8rem;
  font-weight: 600;
}
.title-rule::after {
  content: "";
  display: block;
  width: 56px; height: 2px;
  margin-top: .75rem;
  background: var(--wd-gold);
}

/* Fokus aksesibel */
:focus-visible { outline: 3px solid var(--wd-gold-light); outline-offset: 2px; }
.skip-link {
  position: absolute; left: -999px; top: 0;
  background: var(--wd-gold); color: #000; padding: .75rem 1rem; z-index: 2000;
}
.skip-link:focus { left: 0; }

/* Tombol */
.btn { border-radius: 999px; font-weight: 600; padding: .7rem 1.5rem; min-height: 44px; }
.btn-gold {
  --bs-btn-color: #0B0B0C; --bs-btn-bg: var(--wd-gold); --bs-btn-border-color: var(--wd-gold);
  --bs-btn-hover-color: #0B0B0C; --bs-btn-hover-bg: var(--wd-gold-light); --bs-btn-hover-border-color: var(--wd-gold-light);
  --bs-btn-active-bg: var(--wd-gold-dark); --bs-btn-active-border-color: var(--wd-gold-dark);
}
.btn-outline-gold {
  --bs-btn-color: var(--wd-gold); --bs-btn-border-color: var(--wd-gold);
  --bs-btn-hover-color: #0B0B0C; --bs-btn-hover-bg: var(--wd-gold); --bs-btn-hover-border-color: var(--wd-gold);
}
.btn-wa {
  --bs-btn-color: #0B0B0C; --bs-btn-bg: var(--wd-wa); --bs-btn-border-color: var(--wd-wa);
  --bs-btn-hover-color: #0B0B0C; --bs-btn-hover-bg: var(--wd-wa-dark); --bs-btn-hover-border-color: var(--wd-wa-dark);
}

/* Navbar */
.navbar-wd {
  background: rgba(11,11,12,.92);
  backdrop-filter: saturate(140%) blur(10px);
  border-bottom: 1px solid var(--wd-border);
}
.navbar-wd .nav-link { color: var(--wd-text); font-weight: 500; padding-inline: 1rem; }
.navbar-wd .nav-link:hover,
.navbar-wd .nav-link.active,
.navbar-wd .nav-link[aria-current="page"] { color: var(--wd-gold); }
.navbar-wd .dropdown-menu {
  background: var(--wd-surface); border: 1px solid var(--wd-border);
  border-radius: 14px; padding: .5rem; box-shadow: 0 16px 40px rgba(0,0,0,.55);
}
.navbar-wd .dropdown-item { color: var(--wd-text); border-radius: 8px; padding: .55rem .9rem; }
.navbar-wd .dropdown-item:hover,
.navbar-wd .dropdown-item:focus { background: var(--wd-surface-2); color: var(--wd-gold); }
@media (min-width: 992px) {
  .navbar-wd .dropdown:hover > .dropdown-menu { display: block; } /* hover desktop (opsional) */
}

/* Kartu */
.card-wd {
  background: var(--wd-surface); border: 1px solid var(--wd-border);
  border-radius: 14px; overflow: hidden; height: 100%;
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}
.card-wd:hover { transform: translateY(-4px); border-color: var(--wd-gold); box-shadow: 0 12px 32px rgba(201,162,75,.18); }
.card-wd img { aspect-ratio: 4/3; object-fit: cover; width: 100%; }
.badge-gold { background: var(--wd-gold); color: #0B0B0C; font-weight: 600; border-radius: 999px; }
.price { color: var(--wd-gold-light); font-weight: 700; font-size: 1.15rem; }

/* Tabel */
.table-wd { --bs-table-bg: transparent; --bs-table-color: var(--wd-text); --bs-table-border-color: var(--wd-border); --bs-table-striped-bg: var(--wd-surface-2); }
.table-wd thead th { color: var(--wd-gold); border-bottom: 2px solid var(--wd-gold); font-weight: 600; }

/* FAQ (tanpa JS) */
.faq details { background: var(--wd-surface); border: 1px solid var(--wd-border); border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: .75rem; }
.faq summary { cursor: pointer; font-weight: 600; list-style: none; display: flex; justify-content: space-between; gap: 1rem; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; color: var(--wd-gold); font-size: 1.4rem; line-height: 1; }
.faq details[open] summary::after { content: "–"; }
.faq details[open] { border-color: var(--wd-gold); }

/* Breadcrumb */
.breadcrumb { --bs-breadcrumb-divider-color: var(--wd-text-muted); --bs-breadcrumb-item-active-color: var(--wd-text-muted); font-size: .9rem; }

/* WhatsApp melayang */
.wa-float {
  position: fixed; right: 16px; bottom: 16px; z-index: 1040;
  width: 58px; height: 58px; border-radius: 50%;
  display: grid; place-items: center;
  background: var(--wd-wa); color: #0B0B0C;
  box-shadow: 0 8px 24px rgba(0,0,0,.5);
}
.wa-float:hover { background: var(--wd-wa-dark); }

/* Galeri */
.gallery-grid { display: grid; gap: .75rem; grid-template-columns: repeat(2, 1fr); }
@media (min-width: 768px) { .gallery-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 1200px) { .gallery-grid { grid-template-columns: repeat(4, 1fr); } }
.gallery-grid a { display: block; border-radius: 12px; overflow: hidden; border: 1px solid var(--wd-border); }
.gallery-grid img { aspect-ratio: 1/1; object-fit: cover; width: 100%; transition: transform .35s ease; }
.gallery-grid a:hover img { transform: scale(1.05); }

/* Lightbox CSS-only */
.lightbox { display: none; position: fixed; inset: 0; z-index: 3000; background: rgba(0,0,0,.92); place-items: center; padding: 1rem; }
.lightbox:target { display: grid; }
.lightbox img { max-height: 85vh; max-width: 100%; border-radius: 12px; }
.lightbox .close { position: absolute; top: 1rem; right: 1.25rem; font-size: 2rem; color: var(--wd-text); text-decoration: none; }

/* Hero */
.hero {
  position: relative; min-height: 78vh; display: grid; align-items: center;
  background:
    linear-gradient(180deg, rgba(11,11,12,.55) 0%, rgba(11,11,12,.92) 100%),
    url("/assets/img/hero.webp") center/cover no-repeat;
}
.text-gold-gradient {
  background: linear-gradient(90deg, var(--wd-gold), var(--wd-gold-light));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}

@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; scroll-behavior: auto !important; }
}
```

> Untuk LCP lebih baik, pakai `<img fetchpriority="high">` di hero ketimbang `background-image` bila memungkinkan.

---

## 4. Komponen & Markup Standar

### 4.1 Navbar
```html
<a class="skip-link" href="#konten">Lewati ke konten</a>
<nav class="navbar navbar-expand-lg navbar-wd sticky-top" aria-label="Navigasi utama">
  <div class="container">
    <a class="navbar-brand display-font text-gold-gradient fs-4" href="/index.html">[NAMA_BRAND]</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu"
            aria-controls="menu" aria-expanded="false" aria-label="Buka menu">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="menu">
      <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-1">
        <li class="nav-item"><a class="nav-link" href="/index.html">Beranda</a></li>
        <li class="nav-item"><a class="nav-link" href="/tentang.html">Tentang</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="/paket.html" role="button"
             data-bs-toggle="dropdown" aria-expanded="false">Paket</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/paket.html">Semua Paket</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="/paket/paket-boneka-wisuda.html">Boneka Wisuda</a></li>
            <li><a class="dropdown-item" href="/paket/paket-buket-wisuda.html">Buket Wisuda</a></li>
            <li><a class="dropdown-item" href="/paket/paket-hampers-wisuda.html">Hampers Wisuda</a></li>
            <li><a class="dropdown-item" href="/paket/paket-plakat-wisuda.html">Plakat Wisuda</a></li>
            <li><a class="dropdown-item" href="/paket/paket-souvenir-sekolah-tk-sd.html">Souvenir Sekolah TK/SD</a></li>
            <li><a class="dropdown-item" href="/paket/paket-grosir-kampus-panitia.html">Grosir Kampus &amp; Panitia</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="/galeri.html">Galeri</a></li>
        <li class="nav-item"><a class="nav-link" href="/blog.html">Blog</a></li>
        <li class="nav-item ms-lg-2 mt-2 mt-lg-0">
          <a class="btn btn-wa btn-sm" target="_blank" rel="noopener noreferrer" data-wa-source="navbar"
             href="https://wa.me/6282211221909?text=Halo%20%5BNAMA_BRAND%5D%2C%20saya%20ingin%20tanya%20souvenir%20wisuda.">
            Chat WhatsApp
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
Pada tiap halaman, tambahkan `aria-current="page"` + class `active` pada link yang sesuai. Untuk halaman di dalam `/paket/`, link "Paket" juga diberi `active`.

### 4.2 Tombol WhatsApp Melayang
```html
<a class="wa-float" target="_blank" rel="noopener noreferrer" data-wa-source="floating"
   aria-label="Chat WhatsApp [NAMA_BRAND]"
   href="https://wa.me/6282211221909?text=Halo%20%5BNAMA_BRAND%5D%2C%20saya%20ingin%20tanya%20souvenir%20wisuda.">
  <svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
    <path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.8-.1 1.4z"/>
  </svg>
</a>
```

### 4.3 Kartu Paket
```html
<article class="card-wd">
  <a href="/paket/paket-boneka-wisuda.html">
    <img src="/assets/img/paket/boneka-400.webp" width="400" height="300" loading="lazy" decoding="async"
         alt="Boneka wisuda custom toga hitam dengan nama dan logo kampus">
  </a>
  <div class="p-3 p-lg-4 d-flex flex-column gap-2">
    <span class="badge badge-gold align-self-start">Terlaris</span>
    <h3 class="h5 mb-0"><a class="text-reset text-decoration-none" href="/paket/paket-boneka-wisuda.html">Paket Boneka Wisuda</a></h3>
    <p class="text-secondary mb-1">Boneka custom nama & logo, lengkap kemasan.</p>
    <p class="price mb-2">Mulai Rp[HARGA]</p>
    <div class="d-flex gap-2 flex-wrap">
      <a class="btn btn-outline-gold btn-sm" href="/paket/paket-boneka-wisuda.html">Lihat Detail</a>
      <a class="btn btn-wa btn-sm" target="_blank" rel="noopener noreferrer" data-wa-source="kartu-paket"
         href="https://wa.me/6282211221909?text=Halo%20%5BNAMA_BRAND%5D%2C%20saya%20tertarik%20dengan%20Paket%20Boneka%20Wisuda.">Tanya via WA</a>
    </div>
  </div>
</article>
```

### 4.4 Hero
```html
<header class="hero">
  <div class="container">
    <div class="col-lg-7">
      <p class="eyebrow">Souvenir Wisuda Custom</p>
      <h1>Kenang-kenangan Wisuda yang <span class="text-gold-gradient">Tak Terlupakan</span></h1>
      <p class="lead text-secondary">Boneka, buket, hampers, dan plakat wisuda custom. Pesan mudah lewat WhatsApp, dikirim ke seluruh Indonesia.</p>
      <div class="d-flex flex-wrap gap-2">
        <a class="btn btn-wa btn-lg" target="_blank" rel="noopener noreferrer" data-wa-source="hero" href="https://wa.me/6282211221909?text=...">Chat WhatsApp</a>
        <a class="btn btn-outline-gold btn-lg" href="/paket.html">Lihat Paket</a>
      </div>
    </div>
  </div>
</header>
```

### 4.5 Answer Block (AEO)
```html
<p class="answer-block border-start border-2 ps-3" style="border-color:var(--wd-gold)!important">
  <strong>[NAMA_BRAND]</strong> adalah pembuat souvenir wisuda custom ... harga mulai Rp[HARGA], minimal order 1 pcs, pengerjaan 3–5 hari kerja, kirim ke seluruh Indonesia.
</p>
```

### 4.6 Breadcrumb
```html
<nav aria-label="Breadcrumb"><ol class="breadcrumb">
  <li class="breadcrumb-item"><a href="/index.html">Beranda</a></li>
  <li class="breadcrumb-item"><a href="/paket.html">Paket</a></li>
  <li class="breadcrumb-item active" aria-current="page">Paket Boneka Wisuda</li>
</ol></nav>
```

### 4.7 Footer
4 kolom (desktop): Brand + deskripsi + sosial · Menu · Paket · Kontak (WA, jam, alamat). Baris bawah: © tahun [NAMA_BRAND], Kebijakan Privasi, Syarat & Ketentuan. Latar `--wd-surface`, garis atas emas 1px.

### 4.8 Galeri + Lightbox (tanpa JS)
```html
<div class="gallery-grid">
  <a href="#foto-1"><img src="/assets/img/galeri/foto-1-thumb.webp" width="400" height="400" loading="lazy" alt="Buket wisuda boneka toga hitam untuk Rina, Universitas X"></a>
</div>
<div class="lightbox" id="foto-1">
  <a class="close" href="#galeri" aria-label="Tutup">×</a>
  <img src="/assets/img/galeri/foto-1.webp" width="1200" height="1200" alt="Buket wisuda boneka toga hitam untuk Rina, Universitas X">
</div>
```

---

## 5. Wireframe Per Halaman (Mobile → Desktop)

### Beranda
```
[Navbar sticky]
[HERO  H1 + lead + 2 CTA + foto LCP]
[Answer block]
[Paket unggulan: grid 1/2/3 kolom × 6 kartu]
[Kenapa kami: 3×2 ikon + teks]
[Cara pesan: 4 langkah bernomor, garis emas]
[Galeri pilihan: grid 2/4 kolom + tombol Lihat Semua]
[Testimoni: 1/2/3 kolom kartu]
[Artikel terbaru: 3 kartu]
[FAQ: <details>]
[CTA penutup hitam-emas + tombol WA]
[Footer] [WA float]
```

### Tentang
```
[Breadcrumb] [H1 + answer block]
[Cerita (teks + foto) — 2 kolom]
[Fakta cepat: dl/tabel]
[Nilai & kualitas: 3 kartu]
[Tim: foto bulat + nama + peran]
[Proses produksi: strip foto]
[Kontak & lokasi: 2 kolom (info | peta/tautan)]
[FAQ] [CTA]
```

### Paket
```
[Breadcrumb] [H1 + answer block]
[Grid 6 kartu paket]
[Tabel perbandingan (scroll-x di mobile, .table-responsive)]
[Panduan memilih: 3 kartu skenario]
[Harga grosir: tabel tier]
[Syarat pemesanan] [FAQ] [CTA]
```

### Detail Paket
```
[Breadcrumb] [H1]
[Kolom kiri: galeri (1 foto besar + thumbnail)] [Kolom kanan (sticky): ringkasan, harga mulai, minimal order, CTA WA besar]
[Isi paket] [Spesifikasi (tabel)] [Harga tier]
[Opsi kustomisasi] [Cocok untuk] [Cara pesan]
[Estimasi & kebijakan] [Testimoni] [FAQ]
[Paket terkait ×3] [Artikel terkait ×2] [CTA]
```
Mobile: bar CTA WA tetap di bawah (sticky bottom) menggantikan tombol melayang pada halaman ini.

### Galeri
```
[Breadcrumb] [H1 + intro]
[Filter kategori: pill link]
[Grid foto 2/3/4 kolom]
[CTA "Mau desain seperti ini?"]
```

### Blog (index)
```
[Breadcrumb] [H1 + intro]
[Artikel unggulan: kartu besar 2 kolom]
[Grid artikel 1/2/3 kolom] [Kategori]
[CTA]
```

### Detail Blog
```
[Breadcrumb] [H1] [Byline + tanggal diperbarui + waktu baca]
[TL;DR box emas] [Gambar utama] [Daftar isi]
[Isi (lebar teks max 70ch)] [Kotak rekomendasi paket]
[FAQ] [Bio penulis] [Artikel terkait ×3] [CTA]
```

### 404
```
[Ilustrasi sederhana/ikon toga] [H1 "Halaman tidak ditemukan"] [Tombol: Beranda, Paket, Blog, WA]
```

---

## 6. Gambar & Media
| Jenis | Rasio | Ukuran | Format |
|---|---|---|---|
| Hero | 16:9 / 3:2 | 1600×900 (maks 200 KB) | AVIF/WebP |
| Kartu paket | 4:3 | 400×300 & 800×600 (`srcset`) | WebP |
| Galeri thumb / full | 1:1 | 400² / 1200² | WebP |
| Blog cover | 16:9 | 1200×675 | WebP |
| OG image | 1.91:1 | 1200×630 (<1 MB) | JPG/PNG |
| Logo | 1:1 | SVG + PNG 512² | SVG/PNG |

Gaya foto: latar gelap/netral, cahaya hangat, close-up detail (toga, bordir, kemasan), tanpa watermark besar. Nama file deskriptif, `alt` unik per gambar.

---

## 7. Ikon & Ilustrasi
Gunakan SVG inline atau sprite (Bootstrap Icons di-subset). Ikon garis (stroke) emas, ukuran 24/32 px. Hindari font-icon penuh agar ringan.

---

## 8. Motion
- Transisi 200–350 ms `ease`; hanya `transform` dan `opacity`.
- Hover kartu: naik 4 px + garis emas.
- Tanpa animasi otomatis yang berulang; hormati `prefers-reduced-motion`.

---

## 9. Aksesibilitas (Ringkas)
- Kontras minimal 4,5:1 (teks), 3:1 (komponen UI).
- Fokus terlihat (outline emas terang 3 px).
- Semua gambar punya `alt`; dekoratif `alt=""`.
- Tombol/ikon-saja punya `aria-label`.
- Urutan heading logis; landmark `header/nav/main/footer`.
- Target sentuh ≥ 44×44 px.
- Tabel pakai `<caption>`, `<th scope>`.

---

## 10. Copywriting & Tone
Hangat, profesional, singkat, tidak lebay. Kalimat aktif, bahasa Indonesia baku yang ramah ("Kamu"/"Anda" — pilih satu, konsisten). Hindari klaim tak terbukti ("terbaik se-Indonesia"). Selalu sertakan angka konkret (harga mulai, minimal order, durasi).

Contoh CTA: "Chat WhatsApp", "Minta Penawaran", "Lihat Paket", "Tanya Ketersediaan".

---

## 11. Struktur CSS & Aset
```
assets/
├── css/bootstrap.min.css      (self-host, versi 5.3.x)
├── css/custom.css             (isi §3)
├── js/bootstrap.bundle.min.js (defer)
├── fonts/inter-var.woff2, playfair-display-700.woff2
└── img/ (hero, paket, galeri, blog, og, logo, icon)
```
`@font-face` contoh:
```css
@font-face { font-family:"Inter"; src:url("/assets/fonts/inter-var.woff2") format("woff2"); font-weight:100 900; font-display:swap; }
@font-face { font-family:"Playfair Display"; src:url("/assets/fonts/playfair-display-700.woff2") format("woff2"); font-weight:700; font-display:swap; }
```

---

## 12. Checklist Desain Sebelum Rilis
- [ ] Palet & kontras lolos uji.
- [ ] Navbar, dropdown, tombol WA konsisten di semua halaman.
- [ ] Semua komponen memakai token (tidak ada warna hard-coded).
- [ ] Tidak ada layout shift (gambar punya `width/height`).
- [ ] Uji sentuhan & keyboard (Tab, Enter, Esc untuk dropdown).
- [ ] Tampilan 360 px tanpa scroll horizontal.
