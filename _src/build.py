"""Builds computatio.io's service and policy pages.

The home page (index.html) is edited by hand and stays the source of truth for the look:
this script copies its <style> block into assets/site.css, then writes each page in PAGES to
<slug>/index.html with the same header, footer and visit counting, and rewrites sitemap.xml.

Run from the repo root:  python3 _src/build.py
Jekyll ignores folders starting with "_", so this file is never served.
"""
import datetime, html, json, os, re, shutil, sys
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import PAGES  # noqa: E402
from answers import ANSWERS  # noqa: E402

SITE = "https://computatio.io"
TODAY = os.environ.get("BUILD_TODAY") or datetime.datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()

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
.summary{border:1px solid var(--line);border-left:4px solid var(--gold);background:var(--soft);padding:16px 18px;margin:0 0 28px}
.summary p{margin:0 0 8px}
.summary p:last-child{margin:0}
.page-hero .updated{font-size:13px;color:#aaa;margin:22px 0 0}
.page-hero .lede{font-size:19px;color:#eee;max-width:720px}
.page-hero .byline{font-size:13px;color:#aaa;margin:0}
.answer table{border-collapse:collapse;width:100%;font-size:15px;margin:12px 0 18px}
.answer th,.answer td{border:1px solid var(--line);padding:9px 10px;text-align:left;vertical-align:top}
.answer th{background:var(--soft)}
.box{border:1px solid var(--line);border-top:3px solid var(--gold);padding:18px 20px;margin:32px 0}
.box h2{margin-top:0}
ul.answers{list-style:none;padding:0}
ul.answers li{padding:12px 0;border-bottom:1px solid var(--line);font-size:17px}
ul.sources li{font-size:14px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin:16px 0}
.facts div{border:1px solid var(--line);padding:14px}
@media(max-width:820px){.split{grid-template-columns:1fr}.buybox{position:static}}
@media(max-width:700px){.page-hero{padding:28px 0 40px}.page-hero h1{font-size:28px}.page-hero p{font-size:16px}.page-hero .btn{display:block;text-align:center;margin:0 0 12px}}
"""

SPARK = '<svg class="spark" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.2 6.3L20.5 10.5l-6.3 2.2L12 19l-2.2-6.3L3.5 10.5l6.3-2.2zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z" fill="currentColor"/></svg>'


def nav(answers_live):
    ans = '<a href="/answers/">Answers</a>' if answers_live else ''
    return ('<nav><a class="logo" href="/" style="text-decoration:none;margin:0"><img src="/assets/logo.jpg" alt="" width="56" height="56" class="navlogo">Computatio</a><div>'
            '<a href="/monthly-bookkeeping/">Monthly Books</a><a href="/tax-returns/">Tax returns</a><a href="/books-cleanup/">Cleanup</a>'
            f'{ans}<a href="/about/">About</a><a href="/#book">Book a call</a>'
            f'<a class="ai-btn" href="https://bookbytellc.com/ai-accounting/">{SPARK}AI for Accounting Guides</a></div></nav>')


FOOTER = """<footer>
<div class="wrap">Computatio &middot; Bookkeeping. Tax. Advisory. &middot; Monthly bookkeeping for owner-led businesses and tax returns for self-employed owners, from San Diego, California, serving the United States. &middot; Tax returns are prepared with AI assistance and reviewed and signed off by a person. This site is not legal or tax advice.
<div class="flinks"><a href="/monthly-bookkeeping/">Monthly Books</a><a href="/tax-returns/">Tax returns</a><a href="/books-cleanup/">Books cleanup</a><a href="/answers/">Answers</a><a href="/about/">About</a><a href="/how-we-work/">How we work</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a href="/free-guide/?utm_source=computatio&amp;utm_medium=referral&amp;utm_campaign=footer">Free guide: 47 write-offs</a></div>
</div>
</footer>
<script>window.goatcounter={path:function(p){return location.host+p}}</script>
<script data-goatcounter="https://computatio.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>"""

ORG = {
    "@context": "https://schema.org",
    "@type": ["Organization", "ProfessionalService"],
    "@id": SITE + "/#org",
    "name": "Computatio",
    "legalName": "Computatio Inc.",
    "url": SITE + "/",
    "logo": SITE + "/assets/logo.jpg",
    "image": SITE + "/assets/logo.jpg",
    "description": "AI-assisted monthly bookkeeping for owner-led agencies and service businesses with 2 to 15 people, and fixed-price tax returns for self-employed owners. A person reviews and signs off on every account. Based in San Diego, California, serving the United States.",
    "email": "rogenie@computatio.io",
    "address": {"@type": "PostalAddress", "streetAddress": "13223 Black Mountain Rd, Ste 1 #728", "addressLocality": "San Diego", "addressRegion": "CA", "postalCode": "92129", "addressCountry": "US"},
    "areaServed": {"@type": "Country", "name": "United States"},
    "founder": {"@type": "Person", "@id": SITE + "/about/rogenie/#person", "name": "Rogenie Cordero"},
    "knowsAbout": ["Bookkeeping", "Bank reconciliation", "Monthly close", "Small business tax preparation", "QuickBooks Online", "Xero", "AI for bookkeeping"],
    "sameAs": ["https://bookbytellc.com/", "https://www.youtube.com/@computatio", "https://www.facebook.com/computatio777", "https://www.tiktok.com/@computatio_"],
    "priceRange": "$350-$1,500",
    "makesOffer": [
        {"@type": "Offer", "name": "Monthly Books", "url": SITE + "/monthly-bookkeeping/", "priceSpecification": {"@type": "UnitPriceSpecification", "price": "500", "priceCurrency": "USD", "unitText": "month"}},
        {"@type": "Offer", "name": "Simple Return", "url": SITE + "/tax-returns/", "price": "350", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "Self-Employed Return", "url": SITE + "/tax-returns/", "price": "600", "priceCurrency": "USD"},
        {"@type": "Offer", "name": "Books Cleanup", "url": SITE + "/books-cleanup/", "priceSpecification": {"@type": "PriceSpecification", "minPrice": "500", "maxPrice": "1500", "priceCurrency": "USD"}},
    ],
}
ORG_REF = {"@id": SITE + "/#org"}


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def plain(h):
    return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def faq_ld(body):
    """FAQPage markup built from every <dl class="faq"> on the page."""
    pairs = []
    for dl in re.findall(r'<dl class="faq">(.*?)</dl>', body, re.S):
        pairs += re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", dl, re.S)
    if not pairs:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in pairs]}


def ldscripts(items):
    return "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in items if x)


def page(p, answers_live=False):
    url = f"{SITE}{p['path']}"
    crumbs = p.get("crumbs") or [("Computatio", "/"), (p["crumb"], p["path"])]
    ld = [ORG, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": plain(n), "item": SITE + u} for i, (n, u) in enumerate(crumbs)]}]
    if p.get("service"):
        ld.append({"@context": "https://schema.org", "@type": "Service", "name": p["service"]["name"],
                   "serviceType": p["service"]["type"], "description": p["desc"], "url": url,
                   "audience": {"@type": "BusinessAudience", "audienceType": p["service"].get("audience", "Owner-led small businesses and self-employed owners")},
                   "areaServed": {"@type": "Country", "name": "United States"},
                   "provider": ORG_REF, "offers": p["service"]["offers"]})
    ld += p.get("extra_ld", [])
    ld.append(faq_ld(p["body"]))
    robots = '\n<meta name="robots" content="noindex">' if p.get("noindex") else ""
    og_img = f'<meta property="og:image" content="{SITE}{p["og_image"]}">' if p.get("og_image") else ""
    trail = " &rsaquo; ".join(f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]) + f" &rsaquo; {crumbs[-1][0]}"
    upd = f'<p class="updated">Last updated {datefmt(p["updated"])}</p>' if p.get("show_updated") and p.get("updated") else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{esc(p['desc'])}">
<link rel="canonical" href="{url}">{robots}
<meta name="theme-color" content="#111111">
<meta property="og:type" content="{p.get('og_type', 'website')}">
<meta property="og:site_name" content="Computatio">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:url" content="{url}">
{og_img}
<meta name="twitter:card" content="{"summary_large_image" if p.get("og_image") else "summary"}">
<link rel="icon" href="/assets/logo.jpg">
<link rel="stylesheet" href="/assets/fonts.css">
<link rel="stylesheet" href="/assets/site.css">
{ldscripts(ld)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
<div class="wrap">
{nav(answers_live)}
<div class="page-hero">
<p class="crumbs">{trail}</p>
{p['hero']}
{upd}
</div>
</div>
</header>
<main id="main">
{p['body']}
</main>
{FOOTER if answers_live else FOOTER.replace('<a href="/answers/">Answers</a>', '')}
</body>
</html>
"""


def datefmt(d):
    dt = datetime.date.fromisoformat(d)
    return dt.strftime("%B ") + str(dt.day) + dt.strftime(", %Y")


SERVICE_CTA = {
    "monthly": ("Monthly Books", "/monthly-bookkeeping/", "Books closed and reconciled every month, a plain-English summary by the 15th and a 30-minute review call, for $500 a month."),
    "cleanup": ("Books cleanup", "/books-cleanup/", "We catch up books that are behind for a fixed price you agree to first ($500 to $1,500), then you can roll into Monthly Books."),
    "tax": ("Tax returns", "/tax-returns/", "Fixed-price returns for the self-employed: $350 or $600, prepared with AI and reviewed and signed off by a person."),
}


def answer_page(a):
    url = f"/answers/{a['slug']}/"
    upd = a.get("updated", a["published"])
    secs = "\n".join(f"<h2>{h}</h2>\n{b}" for h, b in a["sections"])
    name, link, blurb = SERVICE_CTA[a.get("service", "monthly")]
    faq = "".join(f"<dt>{q}</dt><dd>{x}</dd>" for q, x in a.get("faq", []))
    src = "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in a.get("sources", []))
    body = f"""<section><div class="wrap prose answer">
{secs}
<div class="box cta-box"><h2>When to get help</h2>{a.get("help", "")}<p><b>{name}:</b> {blurb} <a href="{link}?utm_source=answers&amp;utm_medium=referral&amp;utm_campaign={a['slug']}">See {name}</a> or <a href="https://calendly.com/computatio" target="_blank" rel="noopener">book a free 20-minute call</a>.</p></div>
{'<h2>FAQ</h2><dl class="faq">' + faq + '</dl>' if faq else ''}
{'<h2>Sources</h2><ul class="sources">' + src + '</ul>' if src else ''}
<p class="fine">General information, not tax or legal advice for your situation. Examples use made-up numbers. Written by Computatio and reviewed by founder Rogenie Cordero.</p>
</div></section>"""
    hero = f"""<p class="eyebrow">Computatio Answers</p>
<h1>{a['question']}</h1>
<p class="lede">{a['answer']}</p>
<p class="byline">By Computatio &middot; Reviewed by Rogenie Cordero, founder &middot; Updated {datefmt(upd)}</p>"""
    art = {"@context": "https://schema.org", "@type": "Article", "headline": plain(a["question"]), "description": a["desc"],
           "datePublished": a["published"], "dateModified": upd, "mainEntityOfPage": SITE + url,
           "author": ORG_REF, "publisher": ORG_REF,
           "reviewedBy": {"@type": "Person", "@id": SITE + "/about/rogenie/#person", "name": "Rogenie Cordero"},
           "image": SITE + "/assets/logo.jpg"}
    return {"path": url, "crumb": plain(a["question"]), "crumbs": [("Computatio", "/"), ("Answers", "/answers/"), (plain(a["question"]), url)],
            "title": a.get("title", plain(a["question"]) + " | Computatio"), "desc": a["desc"], "og_type": "article",
            "hero": hero, "body": body, "extra_ld": [art], "updated": upd}


def hub_page(live):
    items = "".join(f'<li><a href="/answers/{a["slug"]}/">{a["question"]}</a><span class="fine"> &middot; {datefmt(a.get("updated", a["published"]))}</span></li>' for a in live)
    return {"path": "/answers/", "crumb": "Answers",
            "title": "Bookkeeping Answers for Small Business Owners | Computatio",
            "desc": "Straight answers to the questions owners ask about bookkeeping: what it costs, what a service should include, catching up, cash flow and profit. From Computatio.",
            "hero": """<p class="eyebrow">Computatio Answers</p><h1>Straight answers about <span>your books.</span></h1><p>What bookkeeping costs, what a monthly service should include, how to catch up, and how to tell if you&rsquo;re actually profitable. Each answer starts with the short version.</p>""",
            "body": f"""<section><div class="wrap prose"><ul class="answers">{items}</ul></div></section>""",
            "updated": live[0].get("updated", live[0]["published"]) if live else TODAY}


def main():
    index_path = os.path.join(ROOT, "index.html")
    index = open(index_path, encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", index, re.S).group(1)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    open(os.path.join(ROOT, "assets", "site.css"), "w", encoding="utf-8").write(css.strip() + "\n" + EXTRA_CSS)
    # home page: keep its structured data in step with ORG and its FAQ
    ld = ldscripts([ORG, faq_ld(index)])
    index = re.sub(r'(<script type="application/ld\+json">.*?</script>\s*)+', ld + "\n", index, count=1, flags=re.S)
    live_now = any(a["published"] <= TODAY for a in ANSWERS)
    link = '<a href="/answers/" style="color:#ccc;margin-right:14px">Answers</a>' if live_now else ''
    index = re.sub(r'<span id="answers-link">.*?</span>', f'<span id="answers-link">{link}</span>', index, count=1, flags=re.S)
    open(index_path, "w", encoding="utf-8").write(index)

    live = sorted([a for a in ANSWERS if a["published"] <= TODAY], key=lambda a: a["published"], reverse=True)
    live_slugs = {a["slug"] for a in live}
    pages = list(PAGES)
    if live:
        pages.append(hub_page(live))
        pages += [answer_page(a) for a in live]
    # remove pages for answers that aren't live (e.g. a date moved)
    adir = os.path.join(ROOT, "answers")
    if os.path.isdir(adir):
        for d in os.listdir(adir):
            if os.path.isdir(os.path.join(adir, d)) and d not in live_slugs:
                shutil.rmtree(os.path.join(adir, d))
        if not live:
            shutil.rmtree(adir)
    for p in pages:
        if p["path"] == "/404/":  # GitHub Pages serves /404.html for missing pages
            h = page(p, bool(live)).replace('<link rel="canonical" href="https://computatio.io/404/">', '')
            open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(h)
            continue
        d = os.path.join(ROOT, p["path"].strip("/"))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(p, bool(live)))
    urls = [("/", TODAY)] + [(p["path"], p.get("updated", TODAY)) for p in pages if not p.get("noindex")]
    sm = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{d}</lastmod></url>" for u, d in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')

    # status.json: read by the scorecard and the monitors. Future items show date and status only.
    cal = json.load(open(os.path.join(ROOT, "_src", "answers_calendar.json"), encoding="utf-8"))
    written = {a["slug"] for a in ANSWERS}
    items = []
    for i in cal["items"]:
        st = "held" if i.get("status") == "held" else ("written" if i["slug"] in written else "todo")
        row = {"date": i["date"], "status": st, "service": i.get("service", "monthly")}
        if i["slug"] in live_slugs:
            a = next(a for a in live if a["slug"] == i["slug"])
            row.update(title=plain(a["question"]), url=f"{SITE}/answers/{a['slug']}/")
        items.append(row)
    runs_path = os.path.join(ROOT, "_src", "answers_runs.json")
    runs = json.load(open(runs_path, encoding="utf-8")) if os.path.exists(runs_path) else []
    json.dump({"built": TODAY, "cadence": cal.get("cadence"), "items": items, "runs": runs},
              open(os.path.join(ROOT, "status.json"), "w", encoding="utf-8"), indent=1)
    print("built", len(pages), "pages;", len(live), "live answers; today", TODAY)


if __name__ == "__main__":
    main()
