# Computatio Answers: publishing runbook

The "Computatio Answers publisher" scheduled task follows this file every Tuesday and Thursday. It publishes one answer page per scheduled date on computatio.io/answers/. Rogenie Cordero chose fully automatic publishing: nothing waits for her review and nothing waits for an approval, so every run must pass the checks below before anything goes live.

Purpose: these pages answer the questions owners ask when their books are a problem or when they're choosing a bookkeeper, in a format AI tools and search engines can quote. The Outreach Desk links them in cold-email follow-ups, so accuracy and plain language matter more than length.

## Each run

1. Get today's date in America/Los_Angeles.
2. Open `_src/answers_calendar.json`. Due items have a `date` of today **or earlier** and a status of `todo` or `written`. Skip `published` and `held`.
   - Nothing due: stop. Make no commits and send no message.
3. Handle due items oldest first, one at a time, through the whole process (write, fact check, publish, run log). An earlier date means a run was missed; catch it up now and say so in the run record's `note`.
4. Status `todo`: write the answer (below), pass the fact check, and append it to `ANSWERS` in `_src/answers.py` with `slug` equal to the calendar item's slug and `published` and `updated` set to the item's date. Status `written`: re-run the fact check on its numbers, then publish.
5. Never publish an item dated in the future.

## If a due answer can't publish

If a fact the answer depends on can't be confirmed on an official or primary page opened in this run, don't publish it. Set its status to `held`, add a `note` with the reason, add a run record (`"result": "held"`), rebuild, commit and push, and send a push notification naming the question, its date and the reason. Then publish the next `todo` item from the calendar instead, dated today, if it passes the fact check; note in its record which item it replaced, and give the held item that later date. If nothing can publish, the push notification is the record.

## Answer format (every page)

Fill these fields of the answer dict (see the comment at the top of `_src/answers.py`):

- **question:** the exact question as an owner would type it into Google or ChatGPT. Keep the calendar's wording unless a clearer common phrasing exists.
- **title:** under 65 characters, starting with the search phrase, ending "| Computatio". **desc:** 140–160 characters that answer the question.
- **answer:** the direct answer in **two sentences**, with the key number and its condition ("Most small businesses pay $X to $Y a month for..., depending on..."). It must make sense quoted alone.
- **sections:** 4–6 `(heading, html)` pairs. Each heading is a follow-up question. Each section answers it in 2–4 short sentences first, then a list or table if needed. One idea per section. Required:
  - one section with a **table** (options, costs, steps or a checklist), using `<table>` with a header row;
  - one worked example, headed like "Example: a 6-person design studio", with every number labeled "made-up numbers";
  - no section about Computatio itself; that goes in `help`.
- **help:** 2–3 sentences on the signs you've outgrown doing this yourself. Plain, no hype.
- **service:** `monthly`, `cleanup` or `tax`, from the calendar item. The build adds one link to that service and the booking link.
- **faq:** 3–5 questions people also ask, each answered in one or two sentences.
- **sources:** 2–5 pages opened in this run, as `(title, url)`.

Length: 800–1,400 words. Talk to "you". Short sentences, plain words, numbers with units and dates. Name things fully ("QuickBooks Online", "the IRS", "Computatio's Monthly Books") rather than "it".

Link at least two other pages inside section text: a Computatio service page, another live answer (check `status.json` for which are live), or a BookByte guide (https://bookbytellc.com/...) that teaches the do-it-yourself method.

## Facts and sources

- Every number, rate, threshold, deadline and price must come from a page opened in this run: IRS, Social Security, state tax agencies, the Bureau of Labor Statistics, or the software vendor's own pricing or help page. Industry surveys only when no official source exists, named in the text.
- Prices from vendors (QuickBooks Online, Xero, etc.) go with "as of <Month YYYY>".
- Market price ranges for bookkeeping: only from a cited source. If none is solid, describe how pricing works without a number.
- Scheduled runs can't approve a fetch of a URL that didn't come from a search. Find each page with WebSearch first (restrict to the domain, e.g. `irs.gov`, `bls.gov`, `quickbooks.intuit.com`), then WebFetch the URL the search returned.
- Remove anything you can't confirm. If the answer can't stand without it, hold it (above).

## Never

- Never use "CPA", "CPA firm", "accounting firm", "licensed preparer" or "PTIN preparer" anywhere. Computatio provides bookkeeping and tax preparation; say "a person reviews and signs off on every account."
- Never invent clients, results, testimonials, quotes, statistics or savings. Examples use made-up numbers and say so.
- Never guarantee outcomes, refunds, audit results or savings. No hype words ("secret", "hack", "guaranteed").
- Never give advice that depends on a reader's specific situation as if it were general; say when to ask a professional.
- Never add tracking pixels, chat widgets, third-party scripts or outside fonts. GoatCounter only.
- Never change prices: Monthly Books $500/month (up to 2 bank accounts and 2 credit cards); Books Cleanup $500–$1,500 one time; returns $350 / $600 / $900.
- Never put Rogenie's name in the body. The build adds the byline ("By Computatio, reviewed by Rogenie Cordero, founder").
- Never edit pages outside `_src/answers.py`, `_src/answers_calendar.json`, `_src/answers_runs.json` and the files the build writes.

## Publish

1. Run `python3 _src/build.py` from the repo root. It must finish without errors and print the live-answer count.
2. Check the built page `answers/<slug>/index.html` exists and contains the question, the two-sentence answer, a `<table>`, the FAQ and the sources. Search it for the words in the Never list (`grep -i -E "cpa|accounting firm|guarantee"`); fix and rebuild if any appear.
3. Set the calendar item's status to `published`.
4. Add a run record (below), run the build again so `status.json` includes it, then commit with author "Rogenie Cordero <rogenie@gmail.com>" and message `Answer: <question>`, and push to main with plain git (`git push origin main`; if refused, `git pull --rebase` and push once more).
5. Live check: about 2 minutes after the push, WebSearch `site:computatio.io <question>` or fetch `https://computatio.io/answers/<slug>/` if a search returned it. If neither works, rely on the push succeeding and set `live_verified` to false.

## Run log

Append one record per answer (published or held) to the JSON list in `_src/answers_runs.json`. Never edit or delete earlier records.

```json
{"date": "YYYY-MM-DD", "at": "<ISO time with Pacific offset>", "result": "published" | "held",
 "slug": "<slug>", "facts_checked": <number>, "removed": <number>, "live_verified": true | false,
 "note": "<one line: catch-up, substitute, hold reason, or anything that failed>"}
```

## If the run can't finish

If anything stops a due answer from going live (a fetch or push refused, the build failing, a missing tool), send a push notification right away naming the question, its date and what failed. Never end silently with a due answer unpublished.
