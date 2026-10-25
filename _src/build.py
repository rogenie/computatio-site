"""Builds computatio.io's service and policy pages.

The home page (index.html) is edited by hand and stays the source of truth for the look:
this script copies its <style> block into assets/site.css, then writes each page in PAGES to
<slug>/index.html with the same header, footer and visit counting, and rewrites sitemap.xml.

Run from the repo root:  python3 _src/build.py
Jekyll ignores folders starting with "_", so this file is never served.
"""
import datetime, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import PAGES  # noqa: E402

SITE = "https://computatio.io"
TODAY = datetime.date.today().isoformat()

EXTRA_CSS = """
/* service and policy pages */
.page-hero{padding:56px 0 60px}
.page-hero h1{font-size:40px;line-height:1.12;margin:0 0 16px;max-width:780px}
.page-hero h1 span{color:var(--gold)}
.page-hero p{font-size:18px;max-width:660px;color:#ddd;margin:0 0 26px}
.page-hero .eyebrow{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.crumbs{font-size:13px;color:#aaa;margin:0 0 18px}
.crumbs a{color:#ccc}
.prose{max-width:720px}
.prose h2{margin-top:40px}
.prose h2:first-child{margin-top:0}
.prose p,.prose li{color:#333}
.prose ul{padding-left:20px}
.prose li{margin-bottom:8px}
.split{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:40px;align-items:start}
.buybox{border:1px solid var(--line);border-top:3px solid var(--gold);background:#fff;padding:24px;position:sticky;top:20px}
.buybox .price{margin:4px 0 12px}
.buybox ul{padding-left:18px;font-size:14px;color:#444;margin:0 0 16px}
.buybox .btn{display:block;text-align:center;margin-top:10px}
.buybox .note{margin-top:12px}
.faq dt{font-weight:700;margin-top:20px}
.faq dd{margin:6px 0 0;color:#333}
table.cmp{border-collapse:collapse;width:100%;font-size:14px;margin:12px 0 0}
table.cmp th,table.cmp td{border:1px solid var(--line);padding:10px;text-align:left;vertical-align:top}
table.cmp th{background:var(--soft)}
.tablewrap{overflow-x:auto}
.cta-band{background:var(--ink);color:#fff;text-align:center}
.cta-band p{color:#ccc;max-width:560px;margin:0 auto 24px}
.cta-band .btn{margin:6px}
.fine{font-size:13px;color:#666}
footer a{color:#ccc}
.flinks{margin-top:10px}
.flinks a{margin-right:14px}
.kitwrap{max-width:720px;margin:0 auto;min-height:420px}
@media(max-width:820px){.split{grid-template-columns:1fr}.buybox{position:static}}
@media(max-width:700px){.page-hero{padding:28px 0 40px}.page-hero h1{font-size:28px}.page-hero p{font-size:16px}.page-hero .btn{display:block;text-align:center;margin:0 0 12px}}
"""

NAV = """<nav><a class="logo" href="/" style="text-decoration:none;margin:0"><img src="/assets/logo.jpg" alt="" width="56" height="56" class="navlogo">Computatio</a><div><a href="/monthly-bookkeeping/">Monthly Books</a><a href="/tax-returns/">Tax returns</a><a href="/books-cleanup/">Cleanup</a><a href="/#book">Book a call</a><a class="ai-btn" href="https://bookbytellc.com/ai-accounting/"><svg class="spark" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.2 6.3L20.5 10.5l-6.3 2.2L12 19l-2.2-6.3L3.5 10.5l6.3-2.2zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z" fill="currentColor"/></svg>AI for Accounting Guides</a></div></nav>"""

FOOTER = """<footer>
<div class="wrap">Computatio &middot; Bookkeeping. Tax. Advisory. &middot; Serving self-employed owners across the United States from San Diego, California. &middot; Tax returns are prepared with AI assistance and reviewed and signed off by a person. This site is not legal or tax advice.
<div class="flinks"><a href="/monthly-bookkeeping/">Monthly Books</a><a href="/tax-returns/">Tax returns</a><a href="/books-cleanup/">Books cleanup</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/free-guide/?utm_source=computatio&amp;utm_medium=referral&amp;utm_campaign=footer">Free guide: 47 write-offs</a></div>
</div>
</footer>
<script>window.goatcounter={path:function(p){return location.host+p}}</script>
<script data-goatcounter="https://computatio.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>"""


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def page(p):
    url = f"{SITE}{p['path']}"
    ld = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Computatio", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]}]
    if p.get("service"):
        ld.append({"@context": "https://schema.org", "@type": "Service", "name": p["service"]["name"],
                   "serviceType": p["service"]["type"], "description": p["desc"], "url": url,
                   "areaServed": {"@type": "Country", "name": "United States"},
                   "provider": {"@type": "ProfessionalService", "name": "Computatio", "url": SITE + "/"},
                   "offers": p["service"]["offers"]})
    robots = '\n<meta name="robots" content="noindex">' if p.get("noindex") else ""
    og_img = f'<meta property="og:image" content="{SITE}{p["og_image"]}">' if p.get("og_image") else ""
    ldj = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{esc(p['desc'])}">
<link rel="canonical" href="{url}">{robots}
<meta name="theme-color" content="#111111">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Computatio">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:url" content="{url}">
{og_img}
<meta name="twitter:card" content="{"summary_large_image" if p.get("og_image") else "summary"}">
<link rel="icon" href="/assets/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Oswald:wght@500&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{ldj}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
<div class="wrap">
{NAV}
<div class="page-hero">
<p class="crumbs"><a href="/">Computatio</a> &rsaquo; {p['crumb']}</p>
{p['hero']}
</div>
</div>
</header>
<main id="main">
{p['body']}
</main>
{FOOTER}
</body>
</html>
"""


def main():
    index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", index, re.S).group(1)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    open(os.path.join(ROOT, "assets", "site.css"), "w", encoding="utf-8").write(css.strip() + "\n" + EXTRA_CSS)
    for p in PAGES:
        d = os.path.join(ROOT, p["path"].strip("/"))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(p))
    urls = [("/", TODAY)] + [(p["path"], p.get("updated", TODAY)) for p in PAGES if not p.get("noindex")]
    sm = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod></url>" for u, d in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main()
