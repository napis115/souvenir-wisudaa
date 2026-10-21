# -*- coding: utf-8 -*-
import os, re, json, shutil
from urllib.parse import quote
from html import escape as E
from content import *

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
if os.path.exists(OUT):
    shutil.rmtree(OUT)
for sub in ["assets/css", "assets/js", "assets/img/paket", "assets/img/galeri", "assets/img/blog", "assets/img/og", "paket", "blog"]:
    os.makedirs(os.path.join(OUT, sub), exist_ok=True)

def write(path, text, mode="w"):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, mode, encoding=None if "b" in mode else "utf-8") as f:
        f.write(text)

def u(p, d):  # path relatif sesuai kedalaman folder
    return ("../" * d) + p

def wa(msg):
    return f"https://wa.me/{WA}?text=" + quote(msg)

def wa_btn(msg, src, label="Chat WhatsApp", cls="btn btn-wa"):
    return (f'<a class="{cls}" target="_blank" rel="noopener noreferrer" data-wa-source="{src}" '
            f'href="{wa(msg)}">{label}</a>')

def by_slug(lst, s):
    return next(x for x in lst if x["slug"] == s)

# ---------------------------------------------------------------- aset gambar
def svg_img(w, h, label, sub=""):
    cx, cy = w / 2, h / 2 - h * 0.05
    k = min(w, h) / 400
    cap = (f'<polygon points="{cx-90*k},{cy-20*k} {cx},{cy-60*k} {cx+90*k},{cy-20*k} {cx},{cy+20*k}" fill="url(#g)"/>'
           f'<path d="M{cx-50*k},{cy-2*k} v{40*k} q{50*k},{30*k} {100*k},0 v{-40*k}" fill="none" stroke="url(#g)" stroke-width="{6*k}"/>'
           f'<path d="M{cx+90*k},{cy-20*k} v{60*k}" stroke="url(#g)" stroke-width="{5*k}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1C1C1F"/><stop offset="1" stop-color="#0B0B0C"/></linearGradient>'
            f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#C9A24B"/><stop offset="1" stop-color="#E3C373"/></linearGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#b)"/>'
            f'<rect x="{12*k}" y="{12*k}" width="{w-24*k}" height="{h-24*k}" rx="{18*k}" fill="none" stroke="#C9A24B" stroke-opacity=".5" stroke-width="{2*k}"/>'
            f'{cap}'
            f'<text x="{cx}" y="{h*0.78}" text-anchor="middle" font-family="Georgia,serif" font-size="{26*k}" fill="#F4F1EA">{E(label)}</text>'
            f'<text x="{cx}" y="{h*0.78+30*k}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{14*k}" fill="#A9A59B">{E(sub)}</text></svg>')

write("assets/img/hero.svg", svg_img(800, 800, "Souvenir Wisuda Custom", "Ganti dengan foto produk asli"))
write("assets/img/icon.svg", svg_img(256, 256, "", ""))
for p in PACKAGES:
    write(f"assets/img/paket/{p['slug']}.svg", svg_img(800, 600, p["name"], "Ganti dengan foto produk asli"))
for i, (c, cl, cap) in enumerate(GALLERY, 1):
    write(f"assets/img/galeri/foto-{i}.svg", svg_img(1000, 1000, cl, "Ganti dengan foto asli"))
for b in POSTS:
    write(f"assets/img/blog/{b['slug']}.svg", svg_img(1200, 675, b["cat"], "Ganti dengan foto cover"))

# gambar raster (OG, favicon) dengan Pillow
from PIL import Image, ImageDraw, ImageFont
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def og_png(name, title, sub="Souvenir Wisuda Custom"):
    im = Image.new("RGB", (1200, 630), (11, 11, 12))
    d = ImageDraw.Draw(im)
    d.rectangle([24, 24, 1176, 606], outline=(201, 162, 75), width=3)
    d.rectangle([80, 120, 140, 126], fill=(201, 162, 75))
    d.text((80, 70), BRAND, font=ImageFont.truetype(FB, 34), fill=(201, 162, 75))
    f = ImageFont.truetype(FB, 62)
    words, lines, cur = title.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > 1040 and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    y = 180
    for ln in lines[:4]:
        d.text((80, y), ln, font=f, fill=(244, 241, 234)); y += 82
    d.text((80, 540), sub + "  •  WhatsApp 0822-1122-1909", font=ImageFont.truetype(FR, 28), fill=(169, 165, 155))
    im.save(os.path.join(OUT, f"assets/img/og/{name}.png"), optimize=True)

ic = Image.new("RGB", (180, 180), (11, 11, 12))
dd = ImageDraw.Draw(ic)
dd.polygon([(90, 40), (160, 72), (90, 104), (20, 72)], fill=(201, 162, 75))
dd.arc([55, 80, 125, 140], 0, 180, fill=(201, 162, 75), width=8)
dd.line([(160, 72), (160, 120)], fill=(201, 162, 75), width=6)
ic.save(os.path.join(OUT, "assets/img/apple-touch-icon.png"))
ic.resize((32, 32)).save(os.path.join(OUT, "favicon.ico"))
ic.resize((512, 512)).save(os.path.join(OUT, "assets/img/logo.webp"), "WEBP")

# ---------------------------------------------------------------- CSS & JS
md = open(os.path.join(ROOT, "design.md"), encoding="utf-8").read()
css = re.search(r"## 3\. Override Bootstrap.*?```css\n(.*?)```", md, re.S).group(1)
css = css.replace('url("/assets/img/hero.webp") center/cover no-repeat', 'radial-gradient(900px 400px at 80% 20%, rgba(201,162,75,.16), transparent)')
css += """
/* ---- tambahan implementasi ---- */
.hero{background:radial-gradient(900px 420px at 85% 15%,rgba(201,162,75,.16),transparent),var(--wd-black);min-height:auto;padding-block:3rem}
.hero img{border-radius:22px;border:1px solid var(--wd-border);box-shadow:0 10px 30px rgba(0,0,0,.45)}
.answer-block{border-left:3px solid var(--wd-gold);padding-left:1rem;color:var(--wd-text);margin-bottom:1.5rem}
.tldr{background:var(--wd-surface);border:1px solid var(--wd-gold);border-radius:14px;padding:1rem 1.25rem}
.prose{max-width:70ch}.prose h2{margin-top:2.25rem}.prose p,.prose li{font-size:1.05rem}
.num{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:var(--wd-gold);color:#0B0B0C;font-weight:700}
.icon-box{background:var(--wd-surface);border:1px solid var(--wd-border);border-radius:14px;padding:1.25rem;height:100%}
.footer-wd{background:var(--wd-surface);border-top:1px solid var(--wd-gold)}
.footer-wd a{color:var(--wd-text-muted);text-decoration:none}.footer-wd a:hover{color:var(--wd-gold)}
.pill{border:1px solid var(--wd-border);border-radius:999px;padding:.35rem .9rem;color:var(--wd-text);text-decoration:none;display:inline-block;margin:0 .35rem .5rem 0}
.pill:hover{border-color:var(--wd-gold);color:var(--wd-gold)}
.sticky-side{position:sticky;top:90px}
.cta-bar{display:none}
@media(max-width:991.98px){
 .has-cta-bar{padding-bottom:78px}.has-cta-bar .wa-float{display:none}
 .cta-bar{display:block;position:fixed;left:0;right:0;bottom:0;z-index:1040;background:rgba(11,11,12,.96);border-top:1px solid var(--wd-gold);padding:.75rem 1rem}
 .cta-bar .btn{width:100%}
}
.lightbox .nav-l,.lightbox .nav-r{position:absolute;top:50%;font-size:2.5rem;color:var(--wd-text);text-decoration:none;padding:0 1rem}
.lightbox .nav-l{left:.5rem}.lightbox .nav-r{right:.5rem}
.card-wd .stretched a{color:inherit}
"""
write("assets/css/custom.css", css)
write("assets/js/main.js", """document.addEventListener('click',function(e){var a=e.target.closest('[data-wa-source]');if(!a)return;var p={source:a.getAttribute('data-wa-source'),page_path:location.pathname};if(window.gtag){gtag('event','click_whatsapp',p);}else if(window.dataLayer){window.dataLayer.push(Object.assign({event:'click_whatsapp'},p));}});
""")

# ---------------------------------------------------------------- schema helper
def org_nodes():
    return [
        {"@type": "WebSite", "@id": f"{DOMAIN}/#website", "url": f"{DOMAIN}/", "name": BRAND, "inLanguage": "id-ID",
         "publisher": {"@id": f"{DOMAIN}/#org"}},
        {"@type": ["Organization", "Store"], "@id": f"{DOMAIN}/#org", "name": BRAND, "url": f"{DOMAIN}/",
         "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/assets/img/logo.webp"},
         "image": f"{DOMAIN}/assets/img/og/index.png",
         "description": "Pembuat souvenir wisuda custom: boneka, buket, hampers, plakat, dan paket grosir.",
         "telephone": f"+{WA}", "priceRange": "Rp",
         "address": {"@type": "PostalAddress", "streetAddress": "[ALAMAT]", "addressLocality": "[KOTA]", "addressRegion": "[PROVINSI]", "postalCode": "[KODE_POS]", "addressCountry": "ID"},
         "areaServed": {"@type": "Country", "name": "Indonesia"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "08:00", "closes": "17:00"}],
         "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": f"+{WA}", "availableLanguage": ["id"], "url": f"https://wa.me/{WA}"}],
         "sameAs": ["https://www.instagram.com/AKUN_IG", "https://www.tiktok.com/@AKUN_TIKTOK"]},
    ]

def faq_node(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def faq_html(faq):
    return '<div class="faq">' + "".join(f"<details><summary><span>{E(q)}</span></summary><p class='mb-0 mt-2 text-secondary'>{E(a)}</p></details>" for q, a in faq) + "</div>"

def crumbs(items, d):
    """items: [(nama, path|None)] setelah Beranda"""
    allc = [("Beranda", "index.html")] + items
    h = '<nav aria-label="Breadcrumb"><ol class="breadcrumb">'
    for i, (n, p) in enumerate(allc):
        if i == len(allc) - 1:
            h += f'<li class="breadcrumb-item active" aria-current="page">{E(n)}</li>'
        else:
            h += f'<li class="breadcrumb-item"><a href="{u(p, d)}">{E(n)}</a></li>'
    h += "</ol></nav>"
    node = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": (DOMAIN + "/" + ("" if p == "index.html" else p)) if p else None} for i, (n, p) in enumerate(allc)]}
    for it in node["itemListElement"]:
        if it["item"] is None:
            del it["item"]
    return h, node

# ---------------------------------------------------------------- komponen
def pkg_card(p, d):
    link = u(f"paket/{p['slug']}.html", d)
    msg = f"Halo {BRAND}, saya tertarik dengan {p['name']}. Boleh minta info harga & ketersediaan?"
    return (f'<article class="card-wd"><a href="{link}"><img src="{u("assets/img/paket/"+p["slug"]+".svg", d)}" width="800" height="600" loading="lazy" decoding="async" alt="{E(p["name"])} – {E(p["short"])}"></a>'
            f'<div class="p-3 p-lg-4 d-flex flex-column gap-2"><span class="badge badge-gold align-self-start">{E(p["label"])}</span>'
            f'<h3 class="h5 mb-0"><a class="text-reset text-decoration-none" href="{link}">{E(p["name"])}</a></h3>'
            f'<p class="text-secondary mb-1">{E(p["short"])}</p><p class="price mb-2">Mulai Rp{PRICE}</p>'
            f'<div class="d-flex gap-2 flex-wrap"><a class="btn btn-outline-gold btn-sm" href="{link}">Lihat Detail</a>'
            f'{wa_btn(msg, "kartu-paket", "Tanya via WA", "btn btn-wa btn-sm")}</div></div></article>')

def post_card(b, d):
    link = u(f"blog/{b['slug']}.html", d)
    return (f'<article class="card-wd"><a href="{link}"><img src="{u("assets/img/blog/"+b["slug"]+".svg", d)}" width="1200" height="675" loading="lazy" decoding="async" alt="Ilustrasi artikel: {E(b["title"])}"></a>'
            f'<div class="p-3 p-lg-4"><span class="eyebrow">{E(b["cat"])}</span>'
            f'<h3 class="h5 mt-1"><a class="text-reset text-decoration-none" href="{link}">{E(b["title"])}</a></h3>'
            f'<p class="text-secondary small mb-2">{E(b["tldr"][:120].rsplit(" ",1)[0])}…</p>'
            f'<time class="small text-secondary" datetime="{DATE}">20 Oktober 2026</time> · <span class="small text-secondary">4 menit baca</span></div></article>')

def section(inner, alt=False, extra=""):
    return f'<section class="section {"section-alt" if alt else ""} {extra}"><div class="container">{inner}</div></section>'

def heading(eyebrow, title, lead=""):
    return (f'<div class="mb-4"><p class="eyebrow mb-1">{E(eyebrow)}</p><h2 class="title-rule">{E(title)}</h2>'
            + (f'<p class="text-secondary mt-3">{lead}</p>' if lead else "") + "</div>")

def cta_final(d, msg, title="Siap Membuat Souvenir Wisuda Impianmu?"):
    return section(f'<div class="text-center p-4 p-lg-5 rounded-4 border" style="border-color:var(--wd-gold)!important;background:linear-gradient(135deg,#141416,#0B0B0C)">'
                   f'<h2>{E(title)}</h2><p class="text-secondary">Konsultasi gratis lewat WhatsApp. Sampaikan jumlah, desain, dan tanggal acara.</p>'
                   f'{wa_btn(msg, "cta-penutup", "Chat WhatsApp Sekarang", "btn btn-wa btn-lg")}</div>')

# ---------------------------------------------------------------- layout
def nav(d, active):
    def a(key, label, href):
        cur = ' aria-current="page"' if key == active else ""
        return f'<li class="nav-item"><a class="nav-link{" active" if key == active else ""}" href="{u(href, d)}"{cur}>{label}</a></li>'
    dd = "".join(f'<li><a class="dropdown-item" href="{u("paket/"+p["slug"]+".html", d)}">{E(p["cat"])} Wisuda</a></li>' if p["cat"] in ("Boneka", "Buket", "Hampers", "Plakat")
                 else f'<li><a class="dropdown-item" href="{u("paket/"+p["slug"]+".html", d)}">{E(p["name"].replace("Paket ", ""))}</a></li>' for p in PACKAGES)
    return (f'<a class="skip-link" href="#konten">Lewati ke konten</a>'
            f'<nav class="navbar navbar-expand-lg navbar-wd sticky-top" aria-label="Navigasi utama"><div class="container">'
            f'<a class="navbar-brand d-flex align-items-center gap-2 display-font text-gold-gradient fs-4" href="{u("index.html", d)}"><img src="{u("assets/img/logo.webp", d)}" height="40" style="height:40px;width:auto" alt="" decoding="async"><span>{BRAND}</span></a>'
            f'<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Buka menu"><span class="navbar-toggler-icon"></span></button>'
            f'<div class="collapse navbar-collapse" id="menu"><ul class="navbar-nav ms-auto align-items-lg-center gap-lg-1">'
            + a("home", "Beranda", "index.html") + a("tentang", "Tentang", "tentang.html")
            + f'<li class="nav-item dropdown"><a class="nav-link dropdown-toggle{" active" if active=="paket" else ""}" href="{u("paket.html", d)}" role="button" data-bs-toggle="dropdown" aria-expanded="false">Paket</a>'
            f'<ul class="dropdown-menu"><li><a class="dropdown-item" href="{u("paket.html", d)}">Semua Paket</a></li><li><hr class="dropdown-divider"></li>{dd}</ul></li>'
            + a("galeri", "Galeri", "galeri.html") + a("blog", "Blog", "blog.html")
            + f'<li class="nav-item ms-lg-2 mt-2 mt-lg-0">{wa_btn(f"Halo {BRAND}, saya ingin tanya souvenir wisuda.", "navbar", "Chat WhatsApp", "btn btn-wa btn-sm")}</li>'
            "</ul></div></div></nav>")

def footer(d):
    pk = "".join(f'<li><a href="{u("paket/"+p["slug"]+".html", d)}">{E(p["name"])}</a></li>' for p in PACKAGES)
    return (f'<footer class="footer-wd pt-5 pb-4"><div class="container"><div class="row g-4">'
            f'<div class="col-lg-4"><p class="display-font text-gold-gradient fs-4 mb-2 d-flex align-items-center gap-2"><img src="{u("assets/img/logo.webp", d)}" height="36" style="height:36px;width:auto" alt="" loading="lazy" decoding="async"><span>{BRAND}</span></p>'
            f'<p class="text-secondary">Souvenir wisuda custom: boneka, buket, hampers, plakat, dan paket grosir untuk kampus dan sekolah.</p>'
            f'<p class="mb-0"><a href="https://www.instagram.com/AKUN_IG" rel="noopener" target="_blank">Instagram</a> · <a href="https://www.tiktok.com/@AKUN_TIKTOK" rel="noopener" target="_blank">TikTok</a></p></div>'
            f'<div class="col-6 col-lg-2"><h2 class="h6 text-uppercase">Menu</h2><ul class="list-unstyled">'
            f'<li><a href="{u("index.html", d)}">Beranda</a></li><li><a href="{u("tentang.html", d)}">Tentang</a></li><li><a href="{u("paket.html", d)}">Paket</a></li><li><a href="{u("galeri.html", d)}">Galeri</a></li><li><a href="{u("blog.html", d)}">Blog</a></li></ul></div>'
            f'<div class="col-6 col-lg-3"><h2 class="h6 text-uppercase">Paket</h2><ul class="list-unstyled">{pk}</ul></div>'
            f'<div class="col-lg-3"><h2 class="h6 text-uppercase">Kontak</h2><address class="text-secondary mb-2">WhatsApp: <a href="{wa("Halo "+BRAND+", saya ingin tanya souvenir wisuda.")}" target="_blank" rel="noopener noreferrer" data-wa-source="footer">0822-1122-1909</a><br>Jam operasional: Senin–Sabtu, 08.00–17.00<br>[ALAMAT], [KOTA]<br>Melayani pengiriman ke seluruh Indonesia</address></div></div>'
            f'<hr class="border-secondary my-4"><div class="d-flex flex-wrap justify-content-between gap-2 small text-secondary"><span>© 2026 {BRAND}. Semua hak dilindungi.</span>'
            f'<span><a href="{u("kebijakan-privasi.html", d)}">Kebijakan Privasi</a> · <a href="{u("syarat-ketentuan.html", d)}">Syarat &amp; Ketentuan</a></span></div></div></footer>')

PAGES = []  # untuk sitemap

def page(path, key, title, desc, body, nodes, ptype="WebPage", crumb_items=None, article=None,
         noindex=False, cta_bar="", og_title=None, sitemap=True, images=None):
    d = path.count("/")
    canon = DOMAIN + "/" + ("" if path == "index.html" else path)
    stem = path.replace(".html", "")
    ogname = stem.split("/")[-1] if stem.startswith("paket/") else (stem.replace("/", "-") if stem.startswith("blog/") else stem)
    og_png(ogname, og_title or title.split(" | ")[0])
    ogimg = f"{DOMAIN}/assets/img/og/{ogname}.png"
    bc_html, bc_node = ("", None)
    if crumb_items is not None:
        bc_html, bc_node = crumbs(crumb_items, d)
        bc_html = f'<div class="container pt-3">{bc_html}</div>'
    page_node = {"@type": ptype, "@id": canon + "#webpage", "url": canon, "name": title, "description": desc,
                 "isPartOf": {"@id": f"{DOMAIN}/#website"}, "inLanguage": "id-ID", "primaryImageOfPage": {"@type": "ImageObject", "url": ogimg}}
    graph = org_nodes() + [page_node] + ([bc_node] if bc_node else []) + nodes
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
    og_type = "article" if article else "website"
    art = ""
    if article:
        art = (f'<meta property="article:published_time" content="{DATE}T08:00:00+07:00"><meta property="article:modified_time" content="{DATE}T08:00:00+07:00">'
               f'<meta property="article:author" content="{DOMAIN}/tentang.html"><meta property="article:section" content="{E(article["cat"])}"><meta property="article:tag" content="souvenir wisuda">')
    html = f"""<!DOCTYPE html>
<html lang="id" data-bs-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0B0B0C">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="id-ID" href="{canon}">
<link rel="alternate" hreflang="x-default" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="id_ID">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{ogimg}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{E(title)}">
{art}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{ogimg}">
<meta name="twitter:image:alt" content="{E(title)}">
<link rel="icon" href="{u('favicon.ico', d)}" sizes="32x32">
<link rel="icon" href="{u('assets/img/icon.svg', d)}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{u('assets/img/apple-touch-icon.png', d)}">
<link rel="manifest" href="{u('site.webmanifest', d)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" crossorigin="anonymous">
<link rel="stylesheet" href="{u('assets/css/custom.css', d)}">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>
</head>
<body class="{'has-cta-bar' if cta_bar else ''}">
{nav(d, key)}
{bc_html}
<main id="konten">
{body}
</main>
{footer(d)}
{'' if cta_bar else '<a class="wa-float" target="_blank" rel="noopener noreferrer" data-wa-source="floating" aria-label="Chat WhatsApp ' + BRAND + '" href="' + wa("Halo " + BRAND + ", saya ingin tanya souvenir wisuda.") + '"><svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.2 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.2-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.4.1.6-.1l.8-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.8-.1 1.4z"/></svg></a>'}
{cta_bar}
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer crossorigin="anonymous"></script>
<script src="{u('assets/js/main.js', d)}" defer></script>
</body>
</html>"""
    write(path, html)
    if sitemap and not noindex:
        PAGES.append((canon, images or []))

# ---------------------------------------------------------------- halaman: BERANDA
def itemlist_pkgs():
    return {"@type": "ItemList", "name": "Paket Souvenir Wisuda", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": f"{DOMAIN}/paket/{p['slug']}.html", "name": p["name"]} for i, p in enumerate(PACKAGES)]}

d = 0
home_msg = f"Halo {BRAND}, saya mau konsultasi paket souvenir wisuda."
body = f"""<header class="hero"><div class="container"><div class="row align-items-center g-4">
<div class="col-lg-7"><p class="eyebrow">Souvenir Wisuda Custom</p>
<h1>Souvenir Wisuda Custom yang Bikin Hari Kelulusan <span class="text-gold-gradient">Tak Terlupakan</span></h1>
<p class="lead text-secondary">Boneka, buket, hampers, dan plakat wisuda custom. Pesan mudah lewat WhatsApp, dikirim ke seluruh Indonesia.</p>
<div class="d-flex flex-wrap gap-2">{wa_btn(home_msg, "hero", "Chat WhatsApp", "btn btn-wa btn-lg")}<a class="btn btn-outline-gold btn-lg" href="paket.html">Lihat Paket</a></div></div>
<div class="col-lg-5"><img src="assets/img/hero.svg" width="800" height="800" fetchpriority="high" alt="Souvenir wisuda custom bertema toga hitam dan emas" class="img-fluid"></div></div></div></header>"""
body += section(f'<p class="answer-block lead mb-0"><strong>{BRAND}</strong> adalah pembuat souvenir wisuda custom: boneka wisuda, buket, hampers, dan plakat dengan nama, tanggal, dan logo kampus. Harga mulai dari Rp{PRICE}, minimal order mulai 1 pcs, pengerjaan sekitar 2–7 hari kerja, dan pengiriman ke seluruh Indonesia. Pemesanan lewat WhatsApp.</p>')
body += section(heading("Paket Unggulan", "Pilih Paket Souvenir Wisuda", "Setiap paket dapat dikustom sesuai kebutuhan acaramu.") +
                '<div class="row g-4">' + "".join(f'<div class="col-md-6 col-lg-4">{pkg_card(p, 0)}</div>' for p in PACKAGES) + "</div>", alt=True)
body += section(heading("Keunggulan", f"Kenapa Memilih {BRAND}") + '<div class="row g-3">' +
                "".join(f'<div class="col-md-6 col-lg-4"><div class="icon-box"><h3 class="h5 text-gold-gradient">{E(t)}</h3><p class="mb-0 text-secondary">{E(x)}</p></div></div>' for t, x in WHY) + "</div>")
body += section(heading("Cara Pesan", "Pesan Souvenir Wisuda dalam 4 Langkah") + '<ol class="list-unstyled row g-3">' +
                "".join(f'<li class="col-md-6 col-lg-3"><div class="icon-box"><div class="num mb-2">{i}</div><h3 class="h5">{E(t)}</h3><p class="mb-0 text-secondary">{E(x)}</p></div></li>' for i, (t, x) in enumerate(STEPS, 1)) + "</ol>", alt=True)
body += section(heading("Galeri", "Karya Pilihan") + '<div class="gallery-grid">' +
                "".join(f'<a href="galeri.html#foto-{i}"><img src="assets/img/galeri/foto-{i}.svg" width="1000" height="1000" loading="lazy" decoding="async" alt="{E(cap)}"></a>' for i, (c, cl, cap) in enumerate(GALLERY[:8], 1)) +
                '</div><p class="mt-4"><a class="btn btn-outline-gold" href="galeri.html">Lihat Semua Galeri</a></p>')
body += "<!-- TESTIMONI: tambahkan 3–6 testimoni asli pelanggan di sini (nama, instansi, kutipan). Jangan memakai testimoni palsu. -->\n"
body += section(heading("Blog", "Artikel Terbaru") + '<div class="row g-4">' +
                "".join(f'<div class="col-md-6 col-lg-4">{post_card(b, 0)}</div>' for b in POSTS[:3]) + '</div><p class="mt-4"><a class="btn btn-outline-gold" href="blog.html">Lihat Semua Artikel</a></p>', alt=True)
body += section(heading("FAQ", "Pertanyaan yang Sering Diajukan") + faq_html(HOME_FAQ))
body += cta_final(0, home_msg)
page("index.html", "home", f"Souvenir Wisuda Custom & Murah | {BRAND}",
     f"Souvenir wisuda custom: boneka, buket, hampers, plakat. Nama & logo kampus, harga grosir, kirim se-Indonesia. Pesan via WhatsApp {BRAND}.",
     body, [itemlist_pkgs(), faq_node(HOME_FAQ)], og_title="Souvenir Wisuda Custom & Murah",
     images=[f"{DOMAIN}/assets/img/og/index.png"])

# ---------------------------------------------------------------- TENTANG
d = 0
cr, _ = crumbs([("Tentang", None)], 0)
facts = [("Berdiri", "Sejak [TAHUN_BERDIRI]"), ("Produk", "Boneka, buket, hampers, plakat, souvenir grosir"), ("Pelanggan terlayani", "[JUMLAH]+ pesanan"), ("Area pengiriman", "Seluruh Indonesia"), ("Jam operasional", "Senin–Sabtu, 08.00–17.00"), ("Kontak", "WhatsApp 0822-1122-1909")]
body = section(f'<h1>Tentang {BRAND}: Pembuat Souvenir Wisuda Custom Sejak [TAHUN_BERDIRI]</h1>'
               f'<p class="answer-block lead">{BRAND} membuat souvenir wisuda custom untuk wisudawan, keluarga, sekolah, dan kampus. Kami membantu mengubah momen kelulusan menjadi kenang-kenangan yang bisa disimpan bertahun-tahun.</p>')
body += section(heading("Cerita Kami", "Dari Satu Pesanan ke Ribuan Kenangan") +
                '<div class="row g-4 align-items-center"><div class="col-lg-7"><p>[Tulis cerita singkat: siapa pendiri, kapan dan mengapa memulai, apa yang membuat produkmu berbeda.]</p>'
                '<p>Misi kami sederhana: membuat souvenir wisuda yang personal, rapi, dan tiba tepat waktu.</p></div>'
                '<div class="col-lg-5"><img class="img-fluid rounded-4" src="assets/img/hero.svg" width="800" height="800" loading="lazy" alt="Proses pembuatan souvenir wisuda custom"></div></div>', alt=True)
body += section(heading("Fakta Cepat", f"{BRAND} dalam Angka dan Fakta") + '<dl class="row">' +
                "".join(f'<dt class="col-sm-4 text-gold-gradient">{E(k)}</dt><dd class="col-sm-8">{E(v)}</dd>' for k, v in facts) + "</dl>")
body += section(heading("Standar Kualitas", "Nilai yang Kami Jaga") + '<div class="row g-3">' +
                "".join(f'<div class="col-md-4"><div class="icon-box"><h3 class="h5 text-gold-gradient">{t}</h3><p class="mb-0 text-secondary">{x}</p></div></div>' for t, x in [
                    ("Personal", "Setiap pesanan dikustom sesuai nama, tanggal, dan logo."), ("Rapi", "Bahan dan hasil akhir dicek sebelum dikemas."), ("Tepat waktu", "Estimasi pengerjaan disepakati sejak awal.")]) + "</div>", alt=True)
body += section(heading("Tim", "Orang di Balik Souvenirmu") + '<p class="text-secondary">[Tambahkan foto, nama, dan peran pemilik/tim. Sertakan legalitas/NIB bila ada.]</p>')
body += section(heading("Kontak & Lokasi", "Hubungi Kami") + f'<div class="row g-4"><div class="col-md-6"><address class="mb-3">[ALAMAT LENGKAP], [KOTA], [PROVINSI] [KODE_POS]<br>Senin–Sabtu, 08.00–17.00</address>'
                f'{wa_btn("Halo "+BRAND+", saya ingin tanya souvenir wisuda.", "tentang", "Chat WhatsApp 0822-1122-1909")}</div>'
                '<div class="col-md-6"><p class="text-secondary mb-1">Sosial media:</p><a class="pill" href="https://www.instagram.com/AKUN_IG" target="_blank" rel="noopener">Instagram</a><a class="pill" href="https://www.tiktok.com/@AKUN_TIKTOK" target="_blank" rel="noopener">TikTok</a>'
                '<!-- Tambahkan peta (tautan Google Maps) di sini --></div></div>', alt=True)
tfaq = [("Di mana lokasi usaha ini?", "Alamat lengkap tercantum di halaman ini. Pemesanan utama melalui WhatsApp dan pengiriman ke seluruh Indonesia."), ("Apakah bisa konsultasi sebelum memesan?", "Bisa. Konsultasi gratis melalui WhatsApp.")]
body += section(heading("FAQ", "Pertanyaan Seputar Kami") + faq_html(tfaq)) + cta_final(0, f"Halo {BRAND}, saya ingin tahu lebih banyak tentang souvenir wisuda.")
page("tentang.html", "tentang", f"Tentang {BRAND} – Pembuat Souvenir Wisuda Sejak [TAHUN_BERDIRI]",
     f"Kenali {BRAND}: pembuat souvenir wisuda custom. Cerita, kualitas, tim, kontak, dan lokasi. Hubungi via WhatsApp.",
     body, [faq_node(tfaq)], ptype="AboutPage", crumb_items=[("Tentang", None)], og_title=f"Tentang {BRAND}")

# ---------------------------------------------------------------- PAKET (index)
body = section(f'<h1>Paket Souvenir Wisuda: Boneka, Buket, Hampers &amp; Custom Grosir</h1>'
               f'<p class="answer-block lead">Kami menyediakan {len(PACKAGES)} paket souvenir wisuda dengan harga mulai Rp{PRICE}. Minimal order mulai 1 pcs untuk paket personal dan 50 pcs untuk grosir. Pengerjaan 2–7 hari kerja, kirim ke seluruh Indonesia.</p>'
               '<div class="row g-4">' + "".join(f'<div class="col-md-6 col-lg-4">{pkg_card(p, 0)}</div>' for p in PACKAGES) + "</div>")
rows = "".join(f'<tr><th scope="row"><a href="paket/{p["slug"]}.html">{E(p["name"])}</a></th><td>{E(", ".join(p["items"][:2]))}</td><td>{E(p["moq"])}</td><td>{E(p["dur"])}</td><td>{E(p["cocok"][0])}</td><td>Rp{PRICE}</td></tr>' for p in PACKAGES)
body += section(heading("Bandingkan", "Tabel Perbandingan Paket") +
                f'<div class="table-responsive"><table class="table table-wd table-striped align-middle"><caption class="text-secondary">Perbandingan paket souvenir wisuda {BRAND}</caption><thead><tr><th>Paket</th><th>Isi</th><th>Min. order</th><th>Pengerjaan</th><th>Cocok untuk</th><th>Harga mulai</th></tr></thead><tbody>{rows}</tbody></table></div>', alt=True)
body += section(heading("Panduan", "Bingung Memilih Paket?") + '<div class="row g-3">' + "".join(
    f'<div class="col-md-4"><div class="icon-box"><h3 class="h5 text-gold-gradient">{t}</h3><p class="mb-2 text-secondary">{x}</p><a href="paket/{s}.html">Lihat {n}</a></div></div>' for t, x, s, n in [
        ("Untuk diri sendiri", "Pilih boneka atau plakat sebagai kenang-kenangan pribadi.", "paket-boneka-wisuda", "Paket Boneka"),
        ("Untuk kado", "Buket atau hampers cocok untuk pacar, sahabat, dan keluarga.", "paket-buket-wisuda", "Paket Buket"),
        ("Untuk panitia", "Paket grosir dengan harga bertingkat dan logo instansi.", "paket-grosir-kampus-panitia", "Paket Grosir")]) + "</div>")
body += section(heading("Harga Grosir", "Harga Bertingkat untuk Jumlah Besar") +
                '<div class="table-responsive"><table class="table table-wd"><caption class="text-secondary">Tier harga grosir</caption><thead><tr><th>Jumlah</th><th>Harga per pcs</th></tr></thead><tbody>'
                f'<tr><td>1–9 pcs</td><td>Rp{PRICE}</td></tr><tr><td>10–49 pcs</td><td>Rp{PRICE}</td></tr><tr><td>50–99 pcs</td><td>Rp{PRICE}</td></tr><tr><td>100 pcs ke atas</td><td>Hubungi untuk penawaran</td></tr></tbody></table></div>', alt=True)
body += section(heading("Syarat Pemesanan", "Ketentuan Singkat") + '<ul><li>Pembayaran dengan DP, pelunasan sebelum pengiriman.</li><li>Revisi desain dilakukan sebelum produksi dimulai.</li><li>Estimasi pengerjaan disepakati saat pemesanan.</li><li>Harga belum termasuk ongkos kirim.</li></ul>'
                '<p class="small text-secondary">Harga diperbarui: 20 Oktober 2026.</p>')
pfaq = HOME_FAQ[:5]
body += section(heading("FAQ", "FAQ Paket") + faq_html(pfaq), alt=True) + cta_final(0, f"Halo {BRAND}, saya ingin konsultasi memilih paket souvenir wisuda.")
page("paket.html", "paket", f"Paket Souvenir Wisuda Boneka, Buket & Hampers | {BRAND}",
     f"Pilih paket souvenir wisuda: boneka, buket, hampers, plakat, sekolah, dan grosir. Harga mulai Rp{PRICE}, kustom nama & logo. Pesan via WhatsApp.",
     body, [{"@type": "CollectionPage", "@id": DOMAIN + "/paket.html#collection", "name": "Paket Souvenir Wisuda"}, itemlist_pkgs(), faq_node(pfaq)],
     ptype="CollectionPage", crumb_items=[("Paket", None)], og_title="Paket Souvenir Wisuda")

# ---------------------------------------------------------------- DETAIL PAKET
for p in PACKAGES:
    d = 1
    path = f"paket/{p['slug']}.html"
    msg = f"Halo {BRAND}, saya tertarik dengan {p['name']}. Boleh minta info harga & ketersediaan?"
    pf = [(f"Apa saja isi {p['name']}?", "Paket ini berisi: " + "; ".join(p["items"]) + "."),
          (f"Berapa minimal order dan lama pengerjaan {p['name']}?", f"Minimal order {p['moq']} dengan estimasi pengerjaan {p['dur']}."),
          ("Bagaimana cara memesan?", "Chat WhatsApp, pilih paket dan konfirmasi desain, lakukan DP, lalu pesanan diproduksi dan dikirim setelah pelunasan.")]
    tiers = ([("50–99 pcs", f"Rp{PRICE}"), ("100–499 pcs", f"Rp{PRICE}"), ("500 pcs ke atas", "Hubungi untuk penawaran")] if p["cat"] == "Grosir"
             else [("1–9 pcs", f"Rp{PRICE}"), ("10–49 pcs", f"Rp{PRICE}"), ("50 pcs ke atas", "Hubungi untuk penawaran")])
    related = [x for x in PACKAGES if x["slug"] != p["slug"]][:3]
    rposts = [b for b in POSTS if b["pkg"] == p["slug"]][:2] or POSTS[:2]
    ul = lambda xs: "<ul>" + "".join(f"<li>{E(x)}</li>" for x in xs) + "</ul>"
    body = section(f'<h1>{E(p["name"])} – Souvenir Wisuda {E(p["cat"])}</h1>'
        f'<p class="answer-block lead">{E(p["name"])}: {E(p["short"])} Harga mulai Rp{PRICE}, minimal order {E(p["moq"])}, pengerjaan {E(p["dur"])}.</p>'
        f'<div class="row g-4"><div class="col-lg-7"><img class="img-fluid rounded-4 border" src="../assets/img/paket/{p["slug"]}.svg" width="800" height="600" fetchpriority="high" alt="{E(p["name"])} – {E(p["short"])}">'
        f'<h2 class="mt-5 h3">Isi Paket</h2>{ul(p["items"])}'
        f'<h2 class="mt-4 h3">Spesifikasi</h2><div class="table-responsive"><table class="table table-wd"><caption class="text-secondary">Spesifikasi {E(p["name"])}</caption><tbody>' +
        "".join(f'<tr><th scope="row" style="width:35%">{E(k)}</th><td>{E(v)}</td></tr>' for k, v in p["specs"]) + '</tbody></table></div>'
        f'<h2 class="mt-4 h3">Harga</h2><div class="table-responsive"><table class="table table-wd"><caption class="text-secondary">Tier harga {E(p["name"])}</caption><thead><tr><th>Jumlah</th><th>Harga per pcs</th></tr></thead><tbody>' +
        "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in tiers) + '</tbody></table></div><p class="small text-secondary">Harga belum termasuk ongkir. Diperbarui 20 Oktober 2026.</p>'
        f'<h2 class="mt-4 h3">Opsi Kustomisasi</h2><p>Nama, tanggal wisuda, logo kampus/instansi, warna, ucapan, dan kemasan dapat disesuaikan.</p>'
        f'<h2 class="mt-4 h3">Cocok Untuk</h2>{ul(p["cocok"])}'
        f'<h2 class="mt-4 h3">Cara Pesan</h2><ol><li>Chat WhatsApp dan sampaikan kebutuhan.</li><li>Pilih paket dan konfirmasi desain.</li><li>Lakukan DP, produksi dimulai.</li><li>Pelunasan, pesanan dikemas dan dikirim.</li></ol>'
        f'<h2 class="mt-4 h3">Estimasi &amp; Kebijakan</h2><p>Estimasi pengerjaan {E(p["dur"])}. Revisi desain dilakukan sebelum produksi. Ketentuan lengkap ada di <a href="../syarat-ketentuan.html">Syarat &amp; Ketentuan</a>.</p>'
        '</div><div class="col-lg-5"><div class="sticky-side icon-box">'
        f'<span class="badge badge-gold mb-2">{E(p["label"])}</span><p class="price fs-4 mb-1">Mulai Rp{PRICE}</p><p class="text-secondary mb-1">Min. order: {E(p["moq"])}</p><p class="text-secondary">Pengerjaan: {E(p["dur"])}</p>'
        f'{wa_btn(msg, "detail-"+p["slug"], "Pesan via WhatsApp", "btn btn-wa btn-lg w-100")}</div></div></div>')
    body += "<!-- TESTIMONI paket: tambahkan testimoni asli pelanggan di sini. -->\n"
    body += section(heading("FAQ", f"FAQ {p['name']}") + faq_html(pf), alt=True)
    body += section(heading("Paket Terkait", "Paket Lain yang Mungkin Cocok") + '<div class="row g-4">' + "".join(f'<div class="col-md-6 col-lg-4">{pkg_card(x, 1)}</div>' for x in related) + '</div>'
                    '<h3 class="h5 mt-5">Artikel Terkait</h3><div class="row g-4">' + "".join(f'<div class="col-md-6">{post_card(b, 1)}</div>' for b in rposts) + "</div>")
    cb = f'<div class="cta-bar">{wa_btn(msg, "cta-bar-"+p["slug"], "Pesan via WhatsApp", "btn btn-wa btn-lg")}</div>'
    product = {"@type": "Product", "@id": f"{DOMAIN}/{path}#product", "name": p["name"], "description": p["short"],
               "image": [f"{DOMAIN}/assets/img/og/{p['slug']}.png"], "brand": {"@type": "Brand", "name": BRAND}, "category": "Souvenir Wisuda",
               "offers": {"@type": "Offer", "url": f"{DOMAIN}/{path}", "priceCurrency": "IDR", "price": PRICE_NUM, "priceValidUntil": "2027-12-31",
                          "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition", "seller": {"@id": f"{DOMAIN}/#org"}}}
    page(path, "paket", f"{p['name']} – Harga & Isi Paket | {BRAND}",
         f"{p['name']}: {p['short']} Harga mulai Rp{PRICE}, min. order {p['moq']}, pengerjaan {p['dur']}. Pesan via WhatsApp.",
         body, [product, faq_node(pf)], crumb_items=[("Paket", "paket.html"), (p["name"], None)], cta_bar=cb,
         og_title=p["name"], images=[f"{DOMAIN}/assets/img/og/{p['slug']}.png"])

# ---------------------------------------------------------------- GALERI
d = 0
cats = []
for c, cl, cap in GALLERY:
    if (c, cl) not in cats:
        cats.append((c, cl))
body = section(f'<h1>Galeri Souvenir Wisuda: Contoh Hasil Pesanan {BRAND}</h1>'
               f'<p class="answer-block lead">Lihat {len(GALLERY)} contoh souvenir wisuda dari berbagai kategori: boneka, buket, hampers, plakat, sekolah, dan grosir. Ingin desain serupa? Chat kami lewat WhatsApp.</p>'
               + '<nav aria-label="Kategori galeri">' + "".join(f'<a class="pill" href="#{c}">{cl}</a>' for c, cl in cats) + "</nav>")
body = body.replace("<section", '<section id="galeri"', 1)
nGal = len(GALLERY)
lb = ""
for c, cl in cats:
    items = "".join(f'<a href="#foto-{i}"><img src="assets/img/galeri/foto-{i}.svg" width="1000" height="1000" loading="lazy" decoding="async" alt="{E(cap)}"></a>'
                    for i, (cc, _, cap) in enumerate(GALLERY, 1) if cc == c)
    body += section(f'<h2 id="{c}" class="mb-3">{cl}</h2><div class="gallery-grid">{items}</div>', alt=(cats.index((c, cl)) % 2 == 0))
for i, (c, cl, cap) in enumerate(GALLERY, 1):
    prev_i, next_i = (i - 1 or nGal), (i % nGal + 1)
    lb += (f'<div class="lightbox" id="foto-{i}"><a class="close" href="#{c}" aria-label="Tutup">×</a><a class="nav-l" href="#foto-{prev_i}" aria-label="Sebelumnya">‹</a>'
           f'<figure class="m-0 text-center"><img src="assets/img/galeri/foto-{i}.svg" width="1000" height="1000" alt="{E(cap)}"><figcaption class="mt-2 text-secondary">{E(cap)}</figcaption></figure>'
           f'<a class="nav-r" href="#foto-{next_i}" aria-label="Berikutnya">›</a></div>')
body += lb + cta_final(0, f"Halo {BRAND}, saya suka desain di galeri. Bisa dibuatkan yang serupa?", "Mau Desain Seperti Ini?")
gnodes = {"@type": "ImageGallery", "@id": DOMAIN + "/galeri.html#gallery", "name": "Galeri Souvenir Wisuda",
          "hasPart": [{"@type": "ImageObject", "contentUrl": f"{DOMAIN}/assets/img/galeri/foto-{i}.svg", "caption": cap} for i, (c, cl, cap) in enumerate(GALLERY, 1)]}
page("galeri.html", "galeri", f"Galeri Souvenir Wisuda – Contoh Hasil Pesanan | {BRAND}",
     f"Galeri souvenir wisuda: boneka, buket, hampers, plakat, sekolah, dan grosir. Lihat contoh hasil dan pesan desain serupa via WhatsApp.",
     body, [gnodes], ptype="CollectionPage", crumb_items=[("Galeri", None)], og_title="Galeri Souvenir Wisuda")

# ---------------------------------------------------------------- BLOG index
feat = POSTS[0]
body = section(f'<h1>Blog Souvenir Wisuda: Ide, Tips &amp; Panduan Memilih Kado Kelulusan</h1>'
               f'<p class="answer-block lead">Kumpulan panduan seputar souvenir wisuda: ide hemat budget, cara memilih boneka dan buket, hitungan anggaran panitia, hingga tips perawatan.</p>'
               + "".join(f'<span class="pill">{c}</span>' for c in dict.fromkeys(b["cat"] for b in POSTS))
               + f'<div class="row g-4 mt-2"><div class="col-12 col-lg-8">{post_card(feat, 0)}</div></div>')
body += section(heading("Semua Artikel", "Artikel Terbaru") + '<div class="row g-4">' + "".join(f'<div class="col-md-6 col-lg-4">{post_card(b, 0)}</div>' for b in POSTS[1:]) + "</div>", alt=True)
body += cta_final(0, f"Halo {BRAND}, saya baca blog dan mau tanya soal souvenir wisuda.")
bl = {"@type": "Blog", "@id": DOMAIN + "/blog.html#blog", "name": f"Blog {BRAND}", "inLanguage": "id-ID",
      "blogPost": [{"@type": "BlogPosting", "headline": b["title"], "url": f"{DOMAIN}/blog/{b['slug']}.html", "datePublished": DATE} for b in POSTS]}
page("blog.html", "blog", f"Blog Souvenir Wisuda: Ide & Tips Kado Kelulusan | {BRAND}",
     "Blog souvenir wisuda: ide hemat budget, cara memilih boneka dan buket, anggaran panitia, dan tips perawatan kado kelulusan.",
     body, [bl], ptype="CollectionPage", crumb_items=[("Blog", None)], og_title="Blog Souvenir Wisuda")

# ---------------------------------------------------------------- BLOG detail
def render_blocks(blocks):
    h = ""
    for b in blocks:
        if isinstance(b, str):
            h += f"<p>{E(b)}</p>"
        elif b[0] == "ul":
            h += "<ul>" + "".join(f"<li>{E(x)}</li>" for x in b[1]) + "</ul>"
        elif b[0] == "table":
            h += ('<div class="table-responsive"><table class="table table-wd"><thead><tr>' + "".join(f"<th>{E(x)}</th>" for x in b[1]) + "</tr></thead><tbody>" +
                  "".join("<tr>" + "".join(f"<td>{E(x)}</td>" for x in r) + "</tr>" for r in b[2]) + "</tbody></table></div>")
    return h

for b in POSTS:
    path = f"blog/{b['slug']}.html"
    pk = by_slug(PACKAGES, b["pkg"])
    toc = "".join(f'<li><a href="#s{i}">{E(h)}</a></li>' for i, (h, _) in enumerate(b["secs"], 1))
    secs = "".join(f'<h2 id="s{i}">{E(h)}</h2>{render_blocks(bl_)}' for i, (h, bl_) in enumerate(b["secs"], 1))
    others = [x for x in POSTS if x["slug"] != b["slug"]][:3]
    msg = f"Halo {BRAND}, saya baca artikel {b['title']}, mau tanya soal souvenir wisuda."
    body = section(f'<article class="prose mx-auto" style="max-width:760px"><h1>{E(b["title"])}</h1>'
        f'<p class="text-secondary small">Oleh <a href="../tentang.html">Tim {BRAND}</a> · Terbit <time datetime="{DATE}">20 Oktober 2026</time> · Diperbarui <time datetime="{DATE}">20 Oktober 2026</time> · 4 menit baca</p>'
        f'<div class="tldr mb-4"><strong class="text-gold-gradient">Jawaban singkat:</strong> {E(b["tldr"])}</div>'
        f'<img class="img-fluid rounded-4 border mb-4" src="../assets/img/blog/{b["slug"]}.svg" width="1200" height="675" fetchpriority="high" alt="Ilustrasi artikel: {E(b["title"])}">'
        f'<nav aria-label="Daftar isi" class="icon-box mb-4"><p class="fw-semibold mb-2">Daftar isi</p><ol class="mb-0">{toc}</ol></nav>{secs}'
        f'<div class="icon-box my-5"><p class="eyebrow mb-1">Rekomendasi paket</p><h2 class="h4 mt-0">{E(pk["name"])}</h2><p class="text-secondary">{E(pk["short"])}</p>'
        f'<a class="btn btn-outline-gold me-2" href="../paket/{pk["slug"]}.html">Lihat Paket</a>{wa_btn(msg, "blog-"+b["slug"], "Tanya via WhatsApp", "btn btn-wa")}</div>'
        f'<h2>FAQ</h2>{faq_html(b["faq"])}'
        f'<div class="icon-box mt-5"><p class="fw-semibold mb-1">Tentang penulis</p><p class="mb-0 text-secondary">Tim {BRAND} adalah pembuat souvenir wisuda custom yang melayani pesanan perorangan, sekolah, dan kampus. <a href="../tentang.html">Kenali kami</a>.</p></div></article>')
    body += section(heading("Baca Juga", "Artikel Terkait") + '<div class="row g-4">' + "".join(f'<div class="col-md-6 col-lg-4">{post_card(x, 1)}</div>' for x in others) + "</div>", alt=True)
    body += cta_final(1, msg)
    post_node = {"@type": "BlogPosting", "@id": f"{DOMAIN}/{path}#article", "headline": b["title"], "description": b["desc"],
                 "image": [f"{DOMAIN}/assets/img/og/blog-{b['slug']}.png"], "datePublished": f"{DATE}T08:00:00+07:00", "dateModified": f"{DATE}T08:00:00+07:00",
                 "inLanguage": "id-ID", "author": {"@type": "Person", "name": f"Tim {BRAND}", "url": f"{DOMAIN}/tentang.html"},
                 "publisher": {"@id": f"{DOMAIN}/#org"}, "mainEntityOfPage": f"{DOMAIN}/{path}", "articleSection": b["cat"], "keywords": ["souvenir wisuda", b["cat"].lower()]}
    page(path, "blog", f"{b['title']} (2026) | {BRAND}", b["desc"], body, [post_node, faq_node(b["faq"])],
         crumb_items=[("Blog", "blog.html"), (b["title"], None)], article=b, og_title=b["title"],
         images=[f"{DOMAIN}/assets/img/og/blog-{b['slug']}.png"])

# ---------------------------------------------------------------- halaman pendukung
body = section(f'<div class="text-center py-5"><p class="display-font text-gold-gradient" style="font-size:5rem">404</p><h1>Halaman Tidak Ditemukan</h1><p class="text-secondary">Halaman yang kamu cari mungkin sudah dipindahkan.</p>'
               f'<div class="d-flex flex-wrap justify-content-center gap-2"><a class="btn btn-outline-gold" href="/index.html">Beranda</a><a class="btn btn-outline-gold" href="/paket.html">Paket</a><a class="btn btn-outline-gold" href="/blog.html">Blog</a>{wa_btn("Halo "+BRAND+", saya butuh bantuan.", "404")}</div></div>')
page("404.html", "", f"Halaman Tidak Ditemukan | {BRAND}", "Halaman tidak ditemukan. Kembali ke beranda atau chat WhatsApp.", body, [], noindex=True, og_title="Halaman Tidak Ditemukan")

def legal(path, title, desc, paras):
    cr_items = [(title, None)]
    b = section(f'<div class="prose"><h1>{E(title)}</h1><p class="text-secondary small">Terakhir diperbarui: 20 Oktober 2026</p>' + "".join(f"<h2>{E(h)}</h2><p>{E(t)}</p>" for h, t in paras) + "</div>")
    page(path, "", f"{title} | {BRAND}", desc, b, [], crumb_items=cr_items, og_title=title)

legal("kebijakan-privasi.html", "Kebijakan Privasi", f"Kebijakan privasi {BRAND}: data yang kami kumpulkan dan cara kami menggunakannya.", [
    ("Data yang kami kumpulkan", "Website ini tidak memiliki formulir dan tidak menyimpan data pribadi di server. Komunikasi terjadi melalui WhatsApp; nomor dan isi pesan Anda diproses oleh WhatsApp sesuai kebijakan mereka."),
    ("Penggunaan data pesanan", "Data yang Anda kirim melalui WhatsApp (nama, alamat, desain) hanya kami gunakan untuk memproses dan mengirim pesanan."),
    ("Analitik dan cookie", "Jika analitik diaktifkan, kami menggunakan data agregat untuk memahami kinerja website. [Sesuaikan bagian ini dengan alat analitik yang benar-benar dipakai]."),
    ("Hak Anda", "Anda dapat meminta penghapusan data pesanan dengan menghubungi kami melalui WhatsApp, sesuai UU Pelindungan Data Pribadi yang berlaku."),
    ("Kontak", f"Pertanyaan terkait privasi dapat dikirim ke WhatsApp 0822-1122-1909.")])
legal("syarat-ketentuan.html", "Syarat & Ketentuan", f"Syarat dan ketentuan pemesanan souvenir wisuda di {BRAND}: DP, revisi, produksi, dan pengiriman.", [
    ("Pemesanan", "Pemesanan dilakukan melalui WhatsApp. Pesanan dianggap sah setelah desain disepakati dan DP diterima."),
    ("Pembayaran", "Pembayaran dilakukan dengan DP dan pelunasan sebelum pengiriman. Besaran DP disepakati saat pemesanan."),
    ("Revisi desain", "Revisi dapat dilakukan sebelum produksi dimulai. Perubahan setelah produksi dimulai dapat dikenakan biaya."),
    ("Produksi dan pengiriman", "Estimasi pengerjaan disepakati saat pemesanan. Pengiriman memakai ekspedisi; ongkos kirim ditanggung pemesan kecuali disepakati lain."),
    ("Pembatalan dan komplain", "Ketentuan pembatalan dan klaim kerusakan disepakati saat pemesanan. Sampaikan komplain beserta foto/video secepatnya setelah barang diterima.")])

# ---------------------------------------------------------------- sitemap, robots, llms, manifest
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
for loc, imgs in PAGES:
    sm += f"<url><loc>{loc}</loc><lastmod>{DATE}</lastmod>" + "".join(f"<image:image><image:loc>{i}</image:loc></image:image>" for i in imgs) + "</url>\n"
sm += "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"""User-agent: *
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

# Opsional: blokir pelatihan model (hapus tanda # untuk mengaktifkan)
# User-agent: GPTBot
# Disallow: /
# User-agent: Google-Extended
# Disallow: /
# User-agent: ClaudeBot
# Disallow: /

Sitemap: {DOMAIN}/sitemap.xml
""")
write("llms.txt", f"""# {BRAND}
> Pembuat souvenir wisuda custom (boneka, buket, hampers, plakat) dengan pemesanan via WhatsApp 6282211221909.

## Halaman Utama
- [Paket]({DOMAIN}/paket.html): daftar paket, harga mulai, minimal order
- [Tentang]({DOMAIN}/tentang.html): profil, kontak, lokasi
- [Galeri]({DOMAIN}/galeri.html): contoh hasil pesanan
- [Blog]({DOMAIN}/blog.html): panduan dan ide souvenir wisuda

## Paket
""" + "\n".join(f"- [{p['name']}]({DOMAIN}/paket/{p['slug']}.html): {p['short']}" for p in PACKAGES) + "\n")
write("site.webmanifest", json.dumps({"name": BRAND, "short_name": BRAND, "lang": "id", "start_url": "/index.html", "display": "browser",
      "background_color": "#0B0B0C", "theme_color": "#0B0B0C",
      "icons": [{"src": "/assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}, {"src": "/assets/img/logo.webp", "sizes": "512x512", "type": "image/webp"}]}, indent=2))
print("OK", len(PAGES), "halaman terindeks")
