# Page content for computatio.io's service and policy pages. Built by _src/build.py.
# Wording rules: never "CPA" or "accounting" for our services; say "a person reviews and signs off
# on every account"; never "PTIN preparer" or "licensed preparer". Prices are locked; change them
# here only when Rogenie changes them, and keep them matching Stripe and the home page.

STRIPE_MONTHLY = "https://buy.stripe.com/28EeVd9t36HA0783WYc7u00?client_reference_id=website"
STRIPE_SIMPLE = "https://buy.stripe.com/3cI6oH48J4zs5rs8dec7u01?client_reference_id=website"
STRIPE_SELF = "https://buy.stripe.com/fZu14n7kV3vo2fg0KMc7u02?client_reference_id=website"
CAL = "https://calendly.com/computatio"
UPDATED = "2026-10-24"

CTA_BAND = """<section class="cta-band"><div class="wrap">
<h2>Not sure which one you need?</h2>
<p>Book a free 20-minute call. We&rsquo;ll look at your situation, tell you which option fits and what it costs, and you decide.</p>
<a class="btn" href="{cal}" target="_blank" rel="noopener">Book a free call</a><a class="btn ghost" href="/#offers">Compare all prices</a>
</div></section>""".format(cal=CAL)

def usd(n):
    return {"@type": "Offer", "price": str(n), "priceCurrency": "USD"}

PAGES = [

# ---------------------------------------------------------------- Monthly Books
{"path": "/monthly-bookkeeping/", "crumb": "Monthly Books",
 "title": "Monthly Bookkeeping for Self-Employed Owners, $500/Month | Computatio",
 "desc": "Monthly bookkeeping for freelancers, contractors and single-owner LLCs and S-corps: books closed every month, a plain-English summary by the 15th and a monthly call. $500 a month, month to month.",
 "service": {"name": "Monthly Books", "type": "Monthly bookkeeping",
             "offers": {"@type": "Offer", "priceSpecification": {"@type": "UnitPriceSpecification", "price": "500", "priceCurrency": "USD", "unitText": "month"}}},
 "hero": """<p class="eyebrow">Monthly Books &middot; $500 a month</p>
<h1>Monthly bookkeeping for self-employed owners, <span>closed and explained every month.</span></h1>
<p>Your books stay current, your accounts are reconciled every month, and you get a one-page summary in plain English by the 15th. AI does the sorting. A person reviews and signs off on every account.</p>
<a class="btn" href="%s">Start Monthly Books &mdash; $500/mo</a> &nbsp; <a class="btn ghost" href="%s" target="_blank" rel="noopener">Book a free call first</a>""" % (STRIPE_MONTHLY, CAL),
 "body": """<section><div class="wrap split">
<div class="prose">
<h2>The problem with doing your own books</h2>
<p>Most owners don&rsquo;t fall behind because bookkeeping is hard. They fall behind because it&rsquo;s never urgent. One busy month becomes three, receipts pile up in your camera roll, and personal and business charges blur together on the same card.</p>
<p>Then tax time arrives. You either spend a weekend rebuilding the year, or you pay someone to clean it up, and you still don&rsquo;t know whether you made money last quarter or how much to set aside for taxes.</p>
<h2>What you get every month</h2>
<ul>
<li><b>Every transaction categorized</b> from your bank and card accounts, using categories that match your tax return.</li>
<li><b>Accounts reconciled</b> to your bank and card statements, so the totals are right, not just the labels.</li>
<li><b>Closed books by the 15th:</b> profit and loss, balance sheet and a cash summary for the month before.</li>
<li><b>A one-page summary in plain English:</b> what came in, what went out, what changed and what to watch.</li>
<li><b>A 30-minute review call</b> each month to go through your numbers and ask anything.</li>
<li><b>A quarterly tax estimate check</b>, so estimated payments aren&rsquo;t a guess.</li>
</ul>
<h2>How it works</h2>
<ol>
<li><b>Sign up and connect your accounts.</b> We send a short checklist and set up read-only access to your bank and card feeds, or you upload statements.</li>
<li><b>AI does the first pass.</b> Our tools sort and match each transaction and flag anything unclear, such as a charge that could be personal.</li>
<li><b>A person reviews it.</b> We check the flagged items, ask you about the ones only you can answer, reconcile every account and sign off.</li>
<li><b>You get your report and call.</b> Closed books and your one-page summary by the 15th, then your monthly call.</li>
</ol>
<h2>Who it&rsquo;s for</h2>
<p>Freelancers, consultants, creators, contractors and single-owner LLCs and S-corps with up to 150 transactions and 3 bank or card accounts a month. It fits best when your books are no more than 2 months behind. If you&rsquo;re further behind, we start with a <a href="/books-cleanup/">books cleanup</a> and roll straight into Monthly Books.</p>
<h2>What&rsquo;s not included</h2>
<p>Monthly Books doesn&rsquo;t include catch-up work for past months, tax returns, payroll or sales tax filings. Tax returns are a separate fixed price; see <a href="/tax-returns/">tax returns</a>. If you need more than 150 transactions or 3 accounts a month, we quote it on a call before you start.</p>
<h2>Questions</h2>
<dl class="faq">
<dt>Is there a contract?</dt><dd>No. Monthly Books is month to month. Cancel any time with 30 days&rsquo; notice.</dd>
<dt>Which software do you use?</dt><dd>We work in QuickBooks Online or Xero. If you don&rsquo;t have either yet, we&rsquo;ll recommend one on your first call.</dd>
<dt>Do you need my bank password?</dt><dd>No. We never ask for your banking passwords. Accounts are connected with read-only bank feeds, or you upload statements.</dd>
<dt>Is a real person involved?</dt><dd>Yes. AI does the sorting and matching. A person reviews and signs off on every account before your report goes out.</dd>
<dt>Can I learn to do this myself?</dt><dd>Yes, and our free <a href="https://bookbytellc.com/ai-accounting/">AI for Accounting guides</a> show you how. Monthly Books is for owners who would rather spend that time on their business.</dd>
</dl>
</div>
<aside class="buybox" aria-label="Monthly Books price">
<h3 style="margin:0">Monthly Books</h3>
<div class="price">$500<small> / month</small></div>
<ul>
<li>Books closed every month</li>
<li>Plain-English summary by the 15th</li>
<li>30-minute monthly review call</li>
<li>Quarterly tax estimate check</li>
<li>Up to 150 transactions and 3 accounts a month</li>
<li>Month to month; cancel with 30 days&rsquo; notice</li>
</ul>
<a class="btn" href="%s">Start Monthly Books &mdash; $500/mo</a>
<a class="btn line" href="%s" target="_blank" rel="noopener">Book a free call first</a>
<p class="note">Books more than 2 months behind? <a href="/books-cleanup/">Start with a cleanup</a>.</p>
</aside>
</div></section>
""" % (STRIPE_MONTHLY, CAL) + CTA_BAND},

# ---------------------------------------------------------------- Tax returns
{"path": "/tax-returns/", "crumb": "Tax returns",
 "title": "Tax Preparation for Self-Employed and Freelancers, from $350 | Computatio",
 "desc": "Fixed-price tax returns for freelancers, sole proprietors and single-owner LLCs and S-corps across the US: $350, $600 or $900, prepared with AI and reviewed and signed off by a person.",
 "service": {"name": "Tax returns", "type": "Tax preparation",
             "offers": [dict(usd(350), name="Simple Return"), dict(usd(600), name="Self-Employed Return"), dict(usd(900), name="Owner-Operator Return")]},
 "hero": """<p class="eyebrow">Tax returns &middot; fixed prices from $350</p>
<h1>Tax returns for the self-employed, <span>at a price you know up front.</span></h1>
<p>Pick the return that matches your situation. AI drafts it from your documents, a person reviews and signs off on it, and you approve it before anything is filed.</p>
<a class="btn" href="#choose">Choose your return</a> &nbsp; <a class="btn ghost" href="%s" target="_blank" rel="noopener">Not sure? Book a free call</a>""" % CAL,
 "body": """<section class="alt" id="choose"><div class="wrap">
<h2>Three returns, three fixed prices</h2>
<p class="sub">If your return turns out to need more than the plan you paid for, we tell you before any work starts and quote the difference, or you can cancel for a full refund.</p>
<div class="grid">
<div class="card"><h3>Simple Return</h3><div class="price">$350<small> / return</small></div><p>W-2 plus light side income.</p><ul><li>Federal return, one state</li><li>Deduction review</li><li>Reviewed and signed off by a person</li></ul><a class="btn" href="%s">Start Simple Return &mdash; $350</a></div>
<div class="card"><h3>Self-Employed Return</h3><div class="price">$600<small> / return</small></div><p>Schedule C freelancers and sole proprietors, including single-member LLCs taxed as sole proprietors.</p><ul><li>Business income and expenses</li><li>Quarterly estimate check</li><li>Reviewed and signed off by a person</li></ul><a class="btn" href="%s">Start Self-Employed Return &mdash; $600</a></div>
<div class="card"><h3>Owner-Operator Return</h3><div class="price">$900<small> / return</small></div><p>LLC or S-corp owners.</p><ul><li>Business and personal returns coordinated</li><li>Owner pay and tax planning check</li><li>Reviewed and signed off by a person</li></ul><a class="btn line" href="%s" target="_blank" rel="noopener">Book a call for a quote</a></div>
</div>
</div></section>
<section><div class="wrap prose">
<h2>Which return do I need?</h2>
<div class="tablewrap"><table class="cmp">
<tr><th>Your situation</th><th>Return</th></tr>
<tr><td>A W-2 job, maybe a little side income, one state</td><td>Simple Return, $350</td></tr>
<tr><td>You freelance or run a business in your own name and get 1099s or invoice clients</td><td>Self-Employed Return, $600</td></tr>
<tr><td>You own an LLC or corporation taxed as an S-corp and pay yourself a salary from it</td><td>Owner-Operator Return, $900, quoted on a call</td></tr>
</table></div>
<h2>What to have ready</h2>
<ul>
<li>Last year&rsquo;s tax return</li>
<li>W-2s, 1099s (1099-NEC, 1099-K, 1099-INT and others) and any other tax forms you received</li>
<li>Business income and expenses for the year: a profit and loss report, or your bank and card statements</li>
<li>Estimated tax payments you made, with dates and amounts</li>
<li>Records for deductions you plan to claim, such as mileage, a home office, health insurance or retirement contributions</li>
</ul>
<p>Don&rsquo;t worry if something is missing. We send a checklist after you sign up and tell you exactly what&rsquo;s still needed.</p>
<h2>How it works</h2>
<ol>
<li><b>Choose your return and pay</b> the fixed price, or book a call if you&rsquo;re not sure.</li>
<li><b>Send your documents</b> through a secure upload.</li>
<li><b>AI drafts, a person reviews.</b> We check every figure and ask you about anything unclear.</li>
<li><b>You review and approve.</b> You get a plain-English summary of your return before anything is filed.</li>
</ol>
<h2>Questions</h2>
<dl class="faq">
<dt>Do you work with clients outside California?</dt><dd>Yes. We prepare returns for self-employed owners across the United States. Each price includes your federal return and one state return; if you need more than one state, we quote it before work starts.</dd>
<dt>Do you keep my books too?</dt><dd>If you&rsquo;d like your books handled all year, add <a href="/monthly-bookkeeping/">Monthly Books</a>. Clean books make your return faster and help you plan your estimated payments.</dd>
<dt>My books are a mess. Can you still do my return?</dt><dd>Yes, but a business return is only as good as the books behind it. If your records need work first, we&rsquo;ll recommend a <a href="/books-cleanup/">books cleanup</a> and quote it before starting.</dd>
<dt>Is a real person involved?</dt><dd>Yes. AI does the sorting and drafting. A person reviews and signs off on every return, and you approve it before filing.</dd>
</dl>
</div></section>
""" % (STRIPE_SIMPLE, STRIPE_SELF, CAL) + CTA_BAND},

# ---------------------------------------------------------------- Cleanup
{"path": "/books-cleanup/", "crumb": "Books cleanup",
 "title": "Bookkeeping Cleanup and Catch-Up for Small Businesses | Computatio",
 "desc": "Behind on your books? Computatio catches up messy or missing bookkeeping for self-employed owners: past transactions categorized and every account reconciled. $500 to $1,500, quoted up front.",
 "service": {"name": "Books Cleanup", "type": "Catch-up bookkeeping",
             "offers": {"@type": "Offer", "priceSpecification": {"@type": "PriceSpecification", "minPrice": "500", "maxPrice": "1500", "priceCurrency": "USD"}}},
 "hero": """<p class="eyebrow">Books cleanup &middot; $500&ndash;$1,500 one time</p>
<h1>Behind on your books? <span>We&rsquo;ll catch you up.</span></h1>
<p>Months of uncategorized transactions, mixed personal and business spending, accounts that never got reconciled. We clean it up for a fixed price you agree to before we start.</p>
<a class="btn" href="%s" target="_blank" rel="noopener">Book a free call for a quote</a> &nbsp; <a class="btn ghost" href="#included">What&rsquo;s included</a>""" % CAL,
 "body": """<section><div class="wrap split">
<div class="prose" id="included">
<h2>Signs you need a cleanup</h2>
<ul>
<li>You haven&rsquo;t looked at your books in months, or you never set them up.</li>
<li>Business and personal spending are mixed on the same accounts.</li>
<li>Your bookkeeping software shows hundreds of transactions &ldquo;for review.&rdquo;</li>
<li>Your account balances in the books don&rsquo;t match your bank statements.</li>
<li>Tax season is coming and you can&rsquo;t say what you earned or spent.</li>
</ul>
<h2>What&rsquo;s included</h2>
<ul>
<li><b>Past transactions categorized</b> using categories that line up with your tax return.</li>
<li><b>Every bank and card account reconciled</b> to its statements, month by month.</li>
<li><b>Personal and business spending separated</b>, with owner draws and contributions recorded properly.</li>
<li><b>A list of open questions</b> for anything only you can answer, so nothing is guessed.</li>
<li><b>Clean reports</b> at the end: profit and loss and balance sheet for the period we cleaned up.</li>
</ul>
<h2>How pricing works</h2>
<p>Cleanups run from $500 to $1,500, priced by how many transactions and months need work. On a free 20-minute call we look at your accounts, agree a fixed price and a delivery date, and only then start.</p>
<h2>After the cleanup</h2>
<p>Most owners don&rsquo;t want to end up here again. Once you&rsquo;re caught up, you can move straight into <a href="/monthly-bookkeeping/">Monthly Books</a> for $500 a month, so your books stay closed every month and tax time is just a return.</p>
<h2>Questions</h2>
<dl class="faq">
<dt>How far back can you go?</dt><dd>Usually the current tax year and, if needed, the year before. Tell us on the call how far behind you are and we&rsquo;ll say what makes sense.</dd>
<dt>I don&rsquo;t have all my receipts. Is that a problem?</dt><dd>Not for the cleanup itself: we work from your bank and card statements. We&rsquo;ll flag which expenses you should find records for.</dd>
<dt>Is a real person involved?</dt><dd>Yes. AI does the first pass on the transactions. A person reviews and signs off on every account.</dd>
</dl>
</div>
<aside class="buybox" aria-label="Books cleanup price">
<h3 style="margin:0">Books Cleanup</h3>
<div class="price">$500&ndash;$1,500<small> one time</small></div>
<ul>
<li>Past transactions categorized</li>
<li>Every account reconciled</li>
<li>Priced by transaction volume</li>
<li>Fixed quote before we start</li>
</ul>
<a class="btn" href="%s" target="_blank" rel="noopener">Book a free call for a quote</a>
<p class="note">Then keep them clean with <a href="/monthly-bookkeeping/">Monthly Books</a>.</p>
</aside>
</div></section>
""" % CAL + CTA_BAND},

# ---------------------------------------------------------------- Free guide (Kit form)
{"path": "/free-guide/", "crumb": "Free guide", "og_image": "/assets/guide-cover.png",
 "title": "Free Guide: 47 Write-Offs for the Self-Employed | Computatio",
 "desc": "Get Computatio's free guide to 47 tax write-offs for self-employed owners, each explained in plain English with the IRS rule behind it.",
 "hero": """<p class="eyebrow">Free guide</p>
<h1>47 write-offs <span>for the self-employed.</span></h1>
<p>The deductions freelancers, creators and owner-operators most often miss, each explained in plain English with the IRS rule behind it. Enter your email and we&rsquo;ll send it to you.</p>""",
 "body": """<section><div class="wrap">
<div class="kitwrap"><script async data-uid="5afb1c8fad" src="https://rogenie.kit.com/5afb1c8fad/index.js"></script></div>
<p class="fine" style="text-align:center;margin-top:18px">The signup form is provided by Kit; by signing up you agree to receive our emails, and you can unsubscribe anytime. See our <a href="/privacy/">privacy policy</a>.</p>
<p class="fine" style="text-align:center;margin-top:18px">You&rsquo;ll get a confirmation email first. Click the link in it to download the guide. Can&rsquo;t find it? Check your Promotions or Spam folder.</p>
</div></section>
<section class="alt"><div class="wrap prose">
<h2>Rather not chase deductions yourself?</h2>
<p>Write-offs are only as good as the books behind them. With <a href="/monthly-bookkeeping/">Monthly Books</a>, every transaction is categorized and reconciled each month, so deductions are captured as you go, not rebuilt in April. AI does the sorting, and a person reviews and signs off on every account.</p>
<p><a class="btn" href="/monthly-bookkeeping/">See Monthly Books</a> &nbsp; <a class="btn line" href="%s" target="_blank" rel="noopener">Book a free call</a></p>
</div></section>""" % CAL},

# ---------------------------------------------------------------- Guide thank-you (Kit redirect target)
{"path": "/free-guide/thank-you/", "crumb": "Your free guide", "noindex": True,
 "title": "Your Free Guide: 47 Write-Offs for the Self-Employed | Computatio",
 "desc": "Download Computatio's 47 write-offs guide for the self-employed, 2026 edition.",
 "hero": """<p class="eyebrow">You&rsquo;re confirmed</p>
<h1>Here&rsquo;s your guide: <span>47 write-offs for the self-employed.</span></h1>
<p>2026 edition, updated for the 2025 tax law. Save it, then use it as a checklist when you review your books and before you file.</p>
<a class="btn" href="/assets/computatio-47-write-offs-2026.pdf" download>Download the guide (PDF)</a>""",
 "body": """<section><div class="wrap prose">
<h2>Want these deductions caught for you?</h2>
<p>Most missed write-offs come from books that aren&rsquo;t kept up. With <a href="/monthly-bookkeeping/">Monthly Books</a> ($500 a month, month to month), every transaction is categorized and reconciled each month, you get a plain-English summary by the 15th, and a 30-minute call to go over your numbers. AI does the sorting; a person reviews and signs off on every account.</p>
<p><a class="btn" href="/monthly-bookkeeping/">See Monthly Books</a> &nbsp; <a class="btn line" href="%s" target="_blank" rel="noopener">Book a free 20-minute call</a></p>
<p class="fine">Prefer to learn to do it yourself? Our free <a href="https://bookbytellc.com/ai-accounting/">AI for Accounting guides</a> show you how.</p>
</div></section>""" % CAL},

# ---------------------------------------------------------------- Privacy
{"path": "/privacy/", "crumb": "Privacy policy", "updated": UPDATED,
 "title": "Privacy Policy | Computatio",
 "desc": "How Computatio collects, uses and protects your information, including the tax and financial records you share with us.",
 "hero": """<h1>Privacy policy</h1><p>Effective October 29, 2026.</p>""",
 "body": """<section><div class="wrap prose">
<p>This policy explains what information Computatio Inc. (&ldquo;Computatio,&rdquo; &ldquo;we&rdquo;) collects through computatio.io and in providing our services, how we use it and the choices you have.</p>
<h2>Information we collect</h2>
<ul>
<li><b>Contact details you give us:</b> your name, email address and what you tell us when you use our contact form, book a call or email us.</li>
<li><b>Client records:</b> if you become a client, the tax forms, bank and card statements, receipts and other financial records you share so we can do the work.</li>
<li><b>Payment details:</b> payments are processed by Stripe. We see your name, email and payment status, not your full card number.</li>
<li><b>Visit counts:</b> we use GoatCounter, which sets no cookies and doesn&rsquo;t store your IP address. It records the page visited, the referring site and general details such as browser, screen size and country.</li>
</ul>
<h2>How we use it</h2>
<ul>
<li>To answer your questions, schedule calls and provide the services you sign up for.</li>
<li>To bill you and keep the records the law requires.</li>
<li>To understand which pages are useful, using visit counts only.</li>
</ul>
<h2>Tax return information</h2>
<p>We use the information you give us for your tax return only to prepare that return and to provide the services you asked for. We don&rsquo;t use or disclose it for any other purpose unless the law allows it or you give us written consent first.</p>
<h2>Cookies, pixels and tracking</h2>
<p>We keep tracking to a minimum. Specifically:</p>
<ul>
<li><b>No advertising pixels or tracking cookies.</b> We don&rsquo;t use Meta, Google, LinkedIn, TikTok or other ad pixels, session recording, or third-party chat widgets, and we don&rsquo;t set cookies to follow you around this site or across other sites.</li>
<li><b>Visit counts:</b> GoatCounter, described above, sets no cookies and doesn&rsquo;t store your IP address.</li>
<li><b>Fonts and files</b> are served from our own site, not from third parties.</li>
<li><b>Our newsletter signup form</b> (on the free guide page) is provided by Kit. When the form loads and when you submit it, Kit receives your browser details and the information you enter, and may set a cookie to remember that you subscribed. See Kit&rsquo;s privacy policy at kit.com/privacy.</li>
<li><b>When you click to pay or book</b>, you go to Stripe or Calendly, which set their own cookies under their own policies.</li>
</ul>
<p>We don&rsquo;t allow third parties to collect information about your online activities over time and across other websites through our site, other than as described above. If we ever add advertising or analytics tools that use cookies, we&rsquo;ll update this policy first and ask for your consent where the law requires it.</p>
<h2>Do Not Track and Global Privacy Control</h2>
<p>Because we don&rsquo;t track you across websites or sell or share your information for advertising, there is nothing for a Do Not Track or Global Privacy Control signal to turn off. If you send either signal, we treat it as a request not to sell or share your personal information, which we already don&rsquo;t do.</p>
<h2>Who we share it with</h2>
<p>We don&rsquo;t sell or rent your personal information. We share it only with service providers that help us run Computatio, and only what they need: Stripe (payments), Calendly (scheduling), Formspree (our contact form), Kit (our newsletter and free guide, if you sign up), Google Workspace (email and files), the bookkeeping software we work in for you, and the AI tools we use to help prepare your work. We may also share information when the law requires it.</p>
<h2>How we protect it</h2>
<p>We limit access to client records to the people doing your work, use accounts protected by multi-factor authentication, and never ask for your banking passwords. No system is perfectly secure, and if a breach ever affects your information, we will tell you as the law requires.</p>
<h2>How long we keep it</h2>
<p>We keep client records for as long as we provide services to you and for the period afterward that tax and recordkeeping laws require, then delete them.</p>
<h2>Your choices</h2>
<p>You can ask to see, correct or delete the personal information we hold about you, subject to what we&rsquo;re required to keep by law. You can unsubscribe from our newsletter from any email. Depending on your state, you may have additional privacy rights, and we will honor them.</p>
<h2>California residents</h2>
<p>We don&rsquo;t sell or share personal information, as those terms are defined in the California Consumer Privacy Act, and we don&rsquo;t use it for cross-context behavioral advertising. To ask what we hold about you, or to correct or delete it, email rogenie@computatio.io. We won&rsquo;t treat you differently for making a request. California&rsquo;s &ldquo;Shine the Light&rdquo; law lets you ask whether we disclosed personal information to third parties for their direct marketing; we don&rsquo;t.</p>
<h2>Children</h2>
<p>Our site and services are for adults running businesses. We don&rsquo;t knowingly collect information from children under 16.</p>
<h2>Changes to this policy</h2>
<p>If we change this policy, we&rsquo;ll post the new version here with a new effective date. If a change is significant, we&rsquo;ll also tell clients and subscribers by email.</p>
<h2>Contact</h2>
<p>Questions or requests: email rogenie@computatio.io.</p>

</div></section>"""},

# ---------------------------------------------------------------- Terms
{"path": "/terms/", "crumb": "Terms of service", "updated": UPDATED,
 "title": "Terms of Service | Computatio",
 "desc": "The terms that apply when you buy a tax return, Monthly Books or a books cleanup from Computatio.",
 "hero": """<h1>Terms of service</h1><p>Last updated October 24, 2026.</p>""",
 "body": """<section><div class="wrap prose">
<p>These terms apply when you buy services from Computatio Inc. (&ldquo;Computatio,&rdquo; &ldquo;we&rdquo;) through computatio.io or after a call with us. By paying for a service, you agree to them.</p>
<h2>Our services</h2>
<p>We provide bookkeeping (Monthly Books and Books Cleanup) and tax return preparation for self-employed owners. Each service&rsquo;s scope is described on its page and at checkout. We use AI software to help with the work, and a person reviews and signs off on every account and return.</p>
<h2>Prices and payment</h2>
<ul>
<li>Fixed-price returns are paid at checkout. Owner-Operator returns and Books Cleanup are quoted before work starts.</li>
<li>Monthly Books is billed monthly in advance through Stripe until you cancel.</li>
<li>If your return or books turn out to need more than the service you paid for, we tell you before any work starts and quote the difference. You can accept the new price or cancel for a full refund.</li>
</ul>
<h2>Cancellation and refunds</h2>
<ul>
<li><b>Monthly Books:</b> cancel any time with 30 days&rsquo; notice by email. You pay for the notice period; we finish the work for the months you&rsquo;ve paid for.</li>
<li><b>Tax returns and cleanups:</b> you can cancel for a full refund before we start work. Once work has started, refunds are limited to the work not yet done.</li>
</ul>
<h2>Your responsibilities</h2>
<ul>
<li>Give us complete and accurate information and records, and tell us promptly about anything that changes.</li>
<li>Answer our questions about items only you can explain, such as whether a charge was personal or business.</li>
<li>Review your return before you approve it. You are responsible for the information on your tax return and for paying any tax due.</li>
</ul>
<h2>What we&rsquo;re responsible for</h2>
<p>We do the work with reasonable care, based on the information you give us. If we make an error, tell us and we will correct our work at no charge. We aren&rsquo;t responsible for errors caused by incomplete or inaccurate information you gave us, or for penalties and interest on tax that was owed anyway. To the extent the law allows, our total liability for any service is limited to the fees you paid for that service.</p>
<h2>Not legal advice</h2>
<p>Our services and this website don&rsquo;t provide legal advice. General information on this site and in our free guides isn&rsquo;t tax advice for your situation.</p>
<h2>Records and privacy</h2>
<p>How we handle your information is described in our <a href="/privacy/">privacy policy</a>.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of California.</p>
<h2>Contact</h2>
<p>Email rogenie@computatio.io.</p>
<p class="fine">We may update these terms. The version in effect when you buy a service applies to that service.</p>
</div></section>"""},
]
