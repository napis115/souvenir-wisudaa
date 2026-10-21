# Website Souvenir Wisuda

Website statis (HTML + Bootstrap 5.3 CSS) sesuai PRD.md dan design.md.

## Logo
Timpa file `assets/img/logo.webp` dengan logo aslimu (nama file harus sama). Logo dipakai di navbar, footer, schema Organization, dan manifest. File bawaan hanyalah placeholder.

## Yang HARUS diganti sebelum rilis
Cari & ganti (find/replace di seluruh folder):
| Placeholder | Ganti dengan |
|---|---|
| `NAMA_BRAND` | nama brand |
| `https://www.namadomain.com` | domain asli |
| `[HARGA]` / `[HARGA_ANGKA]` | harga tampil / angka harga (contoh 85000) untuk schema Product |
| `[ALAMAT]`, `[KOTA]`, `[PROVINSI]`, `[KODE_POS]` | alamat usaha |
| `[TAHUN_BERDIRI]`, `[JUMLAH]` | data usaha |
| `AKUN_IG`, `AKUN_TIKTOK` | akun sosial media |

Alternatif: edit `_source/content.py` lalu jalankan `python3 build.py` (butuh Python 3 + Pillow; `design.md` satu folder). Catatan: build ulang akan menimpa `logo.webp` dengan placeholder, jadi salin ulang logomu sesudahnya.

## Lainnya
- Gambar lain di `assets/img/` masih placeholder SVG. Ganti dengan foto asli (WebP/AVIF) dan perbarui `alt`, `width`, `height`.
- Bootstrap & Google Fonts dimuat dari CDN; untuk performa maksimal, self-host.
- Tambahkan testimoni asli pada komentar `<!-- TESTIMONI -->`.
- Kirim `sitemap.xml` ke Google Search Console & Bing Webmaster Tools.
- Nomor WhatsApp: 6282211221909.
