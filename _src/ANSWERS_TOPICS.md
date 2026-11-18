# Computatio Answers: topics

How topics for computatio.io/answers/ are chosen. The calendar is `_src/answers_calendar.json` (Tue and Thu). Only Rogenie or a Claude session working with her adds or reorders topics; the publisher only publishes what's there.

## Who the answers are for

1. Owner-led agencies and service businesses with 2 to 15 people (marketing, design, web, consulting, architecture), no in-house bookkeeper, usually on QuickBooks Online or Xero. They buy Monthly Books.
2. Self-employed owners and single-owner LLCs and S-corps. They buy tax returns and sometimes Monthly Books.

## What makes a good topic

- A question a real owner would type into Google or ask ChatGPT, in their words, when their books are a problem or when they're choosing help.
- Leads naturally to one Computatio service (Monthly Books, cleanup or tax returns).
- Not already covered by a live answer here, and not a do-it-yourself AI how-to (those belong on BookByte, bookbytellc.com).
- Answerable from official or primary sources.

## Priority

1. Questions behind the pain points in the Outreach Desk's cold emails (items marked `"outreach": true`), so follow-ups have something useful to link.
2. Buyer questions: cost, what a service should include, how to choose, comparisons.
3. Seasonal tax and year-end questions, dated 1–3 weeks before the deadline they relate to.
4. Questions prospects actually ask in replies and on calls. These go to the front of the queue.

## Adding a topic

Add an item to `items`: `{"date", "slug", "question", "angle", "service", "outreach", "status": "todo"}`. `slug` is short, lowercase, hyphenated and unique. `angle` is 1–2 sentences on what the answer must cover and which sources to use. Keep the calendar at least 4 weeks ahead.

## Search data

Once Search Console shows queries for computatio.io beyond the brand name, review them monthly: a query with impressions but no live answer is a candidate topic, and a live answer with impressions but no clicks gets a clearer title and first two sentences.
