# Computatio Answers: buyer-question articles on computatio.io/answers/.
# Written and published by the "Computatio Answers publisher" scheduled task, following _src/ANSWERS_PUBLISHING.md.
# Each answer is a dict; the build shows it from its "published" date (Pacific time).
#
# {
#   "slug": "how-much-does-a-bookkeeper-cost",          # must match its calendar item
#   "published": "YYYY-MM-DD", "updated": "YYYY-MM-DD",  # updated = last fact check
#   "question": "How much does a bookkeeper cost for a small business?",   # H1, the exact question
#   "title": "...| Computatio",                          # optional search title, under 65 characters
#   "desc": "...",                                       # meta description, 140-160 characters
#   "answer": "Two-sentence direct answer with the key number and its condition.",
#   "sections": [("Question-style heading", "<p>HTML</p>"), ...],
#   "help": "<p>2-3 sentences: signs you've outgrown doing it yourself.</p>",
#   "service": "monthly" | "cleanup" | "tax",            # which service the help box links to
#   "faq": [("Question?", "Answer."), ...],               # 3-5 pairs
#   "sources": [("Title", "https://..."), ...],          # pages opened during the run
# }

ANSWERS = [
{
 "slug": "how-to-catch-up-on-bookkeeping",
 "published": "2026-11-19", "updated": "2026-11-21",
 "question": "How do I catch up on months of bookkeeping before taxes?",
 "title": "How to Catch Up on Months of Bookkeeping | Computatio",
 "desc": "Gather every bank and card statement, then reconcile each account one month at a time, oldest first, until the difference is $0.00. Then categorize and review.",
 "answer": "To catch up on months of bookkeeping, gather every bank and credit card statement for the gap, then reconcile each account one month at a time, oldest month first, until the difference in QuickBooks Online or Xero is $0.00. Once every month is reconciled and every transaction is categorized and split between business and personal, you can run a profit and loss report your tax preparer can actually use.",
 "sections": [
  ("What do I need to gather before I start?",
   "<p>Start with the documents, not the software. For most small businesses, the IRS says the business checking account is the main source for entries in the books, so your bank statements come first. Then collect the supporting documents the IRS lists: sales slips, paid bills, invoices, receipts, deposit slips and canceled checks.</p>"
   "<ul><li>Every monthly statement for each business bank account and credit card, for every month you're behind.</li>"
   "<li>Your sales records: invoices you sent, payment processor reports and any Forms 1099 you received.</li>"
   "<li>Bills and receipts for expenses, especially anything over a few hundred dollars and anything for equipment.</li>"
   "<li>Payroll reports, if you have employees, and a list of contractors you paid.</li>"
   "<li>Loan statements, so you can split principal from interest.</li></ul>"
   "<p>Download statements as PDFs from each bank's website. Bank feeds in your software can skip or duplicate transactions, so the statement is the record you check against.</p>"),
  ("What order should I do the work in?",
   "<p>Work one account at a time and go in date order. Each month's ending balance becomes the next month's beginning balance, so a mistake in an early month carries into every month after it. Finishing the oldest month first means you only fix each problem once.</p>"
   "<table><thead><tr><th>Step</th><th>What you do</th><th>You're done when</th></tr></thead><tbody>"
   "<tr><td>1. Gather</td><td>Collect statements and documents for every account and month.</td><td>You have a statement for every month, no gaps.</td></tr>"
   "<tr><td>2. Import</td><td>Get every transaction into the software from the bank feed or a statement upload.</td><td>Each month's transactions are in the books.</td></tr>"
   "<tr><td>3. Categorize</td><td>Give every transaction an income or expense category.</td><td>Nothing is left in uncategorized or &ldquo;Ask my accountant.&rdquo;</td></tr>"
   "<tr><td>4. Separate personal</td><td>Move personal spending to owner draws or owner contributions.</td><td>No personal purchases sit in business expenses.</td></tr>"
   "<tr><td>5. Reconcile</td><td>Match the books to each statement, oldest month first.</td><td>The difference is $0.00 for every month.</td></tr>"
   "<tr><td>6. Review</td><td>Read the profit and loss and balance sheet for each month.</td><td>Nothing looks out of place compared with what you know happened.</td></tr>"
   "</tbody></table>"),
  ("How does reconciling actually work?",
   "<p>Reconciling means checking that the transactions in your books match your bank or card statement for the same period. In QuickBooks Online, you enter the statement's ending balance and date, then check off matching transactions until the difference is $0.00, which Intuit says means the account is balanced. Intuit's help page also says to make sure all transactions for the statement period are added and categorized first.</p>"
   "<p>If the difference won't reach $0.00, look for duplicates from the bank feed, a missing transaction, or an amount typed wrong. Avoid forcing it with an adjustment: in its reconcile video, Intuit says to talk to your accountant before letting QuickBooks create an adjusting entry. If you want to learn the do-it-yourself method step by step, BookByte's guide on <a href=\"https://bookbytellc.com/bookkeeping/do-your-own-bookkeeping/\">how to do your own bookkeeping when you're self-employed</a> walks through it.</p>"),
  ("What do I do about personal spending in business accounts?",
   "<p>Pull it out of your business expenses instead of guessing at a deduction. If you're a sole owner, record personal purchases paid from the business account as owner draws, and business costs you paid personally as owner contributions. The IRS says you must be able to prove certain elements of an expense to deduct it, so anything you can't explain with a receipt or statement should not stay in an expense category.</p>"
   "<p>Going forward, keep one business checking account and one business card, and use them only for the business. That one habit makes next year's catch-up much smaller.</p>"),
  ("Example: a 6-person design studio six months behind",
   "<p>These are made-up numbers to show the shape of the work, not a real client.</p>"
   "<ul><li>The studio has 1 checking account and 2 credit cards, behind from May to October: 3 accounts &times; 6 months = 18 statements to reconcile (made-up numbers).</li>"
   "<li>It averages about 120 transactions a month across the 3 accounts, so about 720 transactions need a category (made-up numbers).</li>"
   "<li>In the June checking reconciliation, the difference is $1,240. The cause is a client payment that came in through the bank feed twice. Deleting the duplicate brings June to $0.00, and July then starts from the correct balance (made-up numbers).</li>"
   "<li>Owner lunches and a family streaming service on one card, about $85 a month, get moved to owner draws (made-up numbers).</li></ul>"
   "<p>If the studio had started with October instead, the duplicate in June would have made every later month look wrong, and the owner would have chased the same $1,240 five times.</p>"),
  ("What if I run out of time before the tax deadline?",
   "<p>Individuals can request up to 6 more months to file their federal return, according to the IRS, and the request has to be made by the return's original due date to avoid the late-filing penalty. But the IRS is clear that an extension of time to file is not an extension of time to pay. If you expect to owe, estimate the amount from the months you've finished and pay it by the original due date.</p>"
   "<p>Deadlines and extension forms differ for partnerships, S-corps and corporations, so ask your tax preparer which dates apply to your business. Keep your records afterward too: the IRS says to keep them as long as needed to prove the income or deductions on a return, and employment tax records for at least 4 years.</p>"),
 ],
 "help": "<p>It's time to get help when you're more than two or three months behind, when a reconciliation won't reach $0.00 after an hour of searching, or when business and personal spending are mixed across several accounts. At that point the hours you spend catching up usually cost more than the work they replace. A <a href=\"/books-cleanup/\">fixed-price books cleanup</a> gets you current, and <a href=\"/monthly-bookkeeping/\">Monthly Books</a> keeps you there; with either, a person reviews and signs off on every account.</p>",
 "service": "cleanup",
 "faq": [
  ("How long does it take to catch up on bookkeeping?", "It depends on how many accounts and months you're behind and how many transactions each month has. Count your statements and transactions first; that number tells you more than any general estimate."),
  ("Should I start with the most recent month or the oldest?", "Start with the oldest month. Each month's ending balance is the next month's beginning balance, so fixing early months first stops errors from carrying forward."),
  ("Can I just use the bank feed instead of statements?", "Use the bank feed to bring transactions in, but reconcile against the actual statement. Feeds can duplicate or miss transactions, and the statement is what proves the balance."),
  ("Does filing an extension give me more time to pay taxes?", "No. The IRS says an extension of time to file is not an extension of time to pay, so estimate and pay what you owe by the original due date."),
  ("What does a books cleanup cost?", "Pricing usually depends on the number of accounts, months behind and transaction volume. Computatio's Books Cleanup is a fixed price between $500 and $1,500, agreed before work starts."),
 ],
 "sources": [
  ("IRS: What kind of records should I keep", "https://www.irs.gov/businesses/small-businesses-self-employed/what-kind-of-records-should-i-keep"),
  ("IRS: Recordkeeping", "https://www.irs.gov/businesses/small-businesses-self-employed/recordkeeping"),
  ("IRS Topic no. 304, Extensions of time to file your tax return", "https://www.irs.gov/taxtopics/tc304"),
  ("Intuit: Reconcile an account in QuickBooks Online", "https://quickbooks.intuit.com/learn-support/en-us/help-article/statement-reconciliation/reconcile-account-quickbooks-online/L3XzsllsK_US_en_US"),
 ],
},
]
