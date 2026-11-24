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
{
 "slug": "is-my-agency-profitable",
 "published": "2026-11-24", "updated": "2026-11-24",
 "question": "How do I know if my agency is actually profitable?",
 "title": "How to Know if Your Agency Is Actually Profitable | Computatio",
 "desc": "Read a reconciled profit and loss report: subtract direct delivery costs for gross profit, then all other expenses and a fair owner pay for true net profit.",
 "answer": "Your agency is actually profitable when a reconciled profit and loss report shows money left over after you subtract the direct cost of delivering client work, every overhead expense and a fair wage for the time you put in. If profit only appears because you paid yourself nothing, or because the books are missing transactions, the agency is not yet profitable in a way you can rely on.",
 "sections": [
  ("Why can revenue look fine while cash is tight?",
   "<p>Revenue, profit and cash measure different things. The U.S. Small Business Administration (SBA) describes a profit and loss statement as a report that measures net income or loss over a defined period of time. Cash is simply what is in the bank today.</p>"
   "<p>The gap usually comes from timing. The IRS explains that under the accrual method you generally report income in the tax year you earn it, regardless of when payment is received. So an agency that invoiced $40,000 in October can show a strong October profit while the money arrives in December. Contractors, payroll and software subscriptions still leave the bank on schedule.</p>"
   "<p>QuickBooks Online lets you see both views. Intuit says a cash-basis report counts income or expenses only once you get a payment or pay a bill, while an accrual-basis report counts them whether or not the invoice or bill was paid. Run the same month both ways and compare.</p>"),
  ("What's the difference between gross profit and net profit?",
   "<p>Gross profit tells you whether client work pays for itself. Net profit tells you whether the whole business does. The SBA defines gross profit as income less cost of goods sold, and cost of goods sold as the direct cost of producing your product or service. For an agency, that usually means contractor and freelancer costs, wages for the people doing billable work, and any costs you pass through on a client's behalf.</p>"
   "<p>Net income is what is left after all expenses: rent, software, insurance, sales and admin time, and taxes. Use the SBA's two ratios to compare months of different sizes:</p>"
   "<table><thead><tr><th>Measure</th><th>Formula</th><th>What it answers</th></tr></thead><tbody>"
   "<tr><td>Gross profit</td><td>Revenue &minus; direct delivery costs</td><td>Does client work cover the people and tools that deliver it?</td></tr>"
   "<tr><td>Gross profit margin</td><td>(Revenue &minus; direct costs) &divide; revenue</td><td>How much of each dollar of fees is left after delivery?</td></tr>"
   "<tr><td>Net profit</td><td>Revenue &minus; all expenses</td><td>Does the business make money after overhead?</td></tr>"
   "<tr><td>Profit margin</td><td>(Revenue &minus; all expenses) &divide; revenue</td><td>How much of each dollar of fees the business keeps</td></tr>"
   "<tr><td>Profit after owner pay</td><td>Net profit &minus; a fair wage for your hours</td><td>Would the agency still make money if you hired someone to do your job?</td></tr>"
   "</tbody></table>"
   "<p>These only work if direct costs are in their own section of the chart of accounts. If contractors sit in the same bucket as office supplies, gross profit can't be measured.</p>"),
  ("How should I count my own pay?",
   "<p>Owner pay is where agency profit is most often overstated. If you are a sole proprietor or single-member LLC, the money you take out is usually recorded as an owner draw, which does not appear on the profit and loss report. A report that shows $8,000 of monthly profit may be the only thing paying you.</p>"
   "<p>To test real profitability, subtract what it would cost to pay someone else for the work you do. If that leaves nothing, the agency is a job that pays you, not yet a business that earns a profit on top of your wage.</p>"
   "<p>If your agency is an S corporation, the IRS says it must pay reasonable compensation to a shareholder-employee for services before non-wage distributions may be made. The IRS lists factors such as duties and responsibilities, time and effort devoted to the business, and what comparable businesses pay for similar services. Ask your tax preparer what fits your situation.</p>"),
  ("How do I read my profit and loss report?",
   "<p>Read the report in the same order every month. In QuickBooks Online, go to Reports, then Standard reports, and choose Profit and Loss Comparison. Intuit's help page says you can set the accounting method to Cash or Accrual and compare to the previous period or the previous year, with a dollar or percent change.</p>"
   "<ul><li><b>Revenue:</b> is it from a few large clients or many? Is any of it a pass-through cost you'll pay out again?</li>"
   "<li><b>Direct costs:</b> did they rise faster than revenue?</li>"
   "<li><b>Gross profit margin:</b> is it steady month to month?</li>"
   "<li><b>Overhead:</b> which subscriptions or fees grew without anyone deciding they should?</li>"
   "<li><b>Net profit:</b> does it hold up after a fair owner wage?</li></ul>"
   "<p>None of this is reliable until every account is reconciled. If you're months behind, start with <a href=\"/answers/how-to-catch-up-on-bookkeeping/\">how to catch up on months of bookkeeping</a>.</p>"),
  ("Example: a 6-person design studio",
   "<p>All of these are made-up numbers to show the math, not results from a real client.</p>"
   "<ul><li>October revenue: $60,000 invoiced, of which $5,000 is printing passed through to a client (made-up numbers).</li>"
   "<li>Direct costs: $22,000 for the designers and freelancers on client work, plus the $5,000 printing (made-up numbers). Gross profit: $60,000 &minus; $27,000 = $33,000, a 55% gross margin. Without the pass-through, fee revenue is $55,000 and fee gross margin is $33,000 &divide; $55,000 = 60% (made-up numbers).</li>"
   "<li>Overhead: $21,000 for rent, software, insurance, an office manager and marketing (made-up numbers). Net profit: $33,000 &minus; $21,000 = $12,000 (made-up numbers).</li>"
   "<li>The owner takes no salary and draws $10,000 a month. Paying someone else to run the studio and lead creative would cost about $11,000 a month (made-up numbers). Profit after owner pay: $12,000 &minus; $11,000 = $1,000 (made-up numbers).</li>"
   "<li>Cash: $35,000 of October invoices won't be paid until December, so the bank balance falls even though October was profitable (made-up numbers).</li></ul>"
   "<p>The studio is profitable, but barely, once the owner's work is counted. Its cash problem is collections timing, not a lack of profit.</p>"),
  ("What should I compare my numbers against?",
   "<p>Compare your agency with itself first. The SBA suggests comparing ratios over three years to find trends and says industry standards are a reference, not a recipe, because what's healthy depends on your company and industry. We don't quote agency benchmark ranges here because we haven't found an official source for them.</p>"
   "<p>Track gross margin and profit after owner pay monthly, and by client if you can. A falling gross margin often means scope creep or underpriced retainers. Flat revenue with rising overhead points to costs that grew without a decision.</p>"),
 ],
 "help": "<p>It's time to get help when you can't answer &ldquo;did we make money last month?&rdquo; within a few days of month-end, when contractors and overhead are mixed in the same accounts, or when the books are more than a month behind. At that point the report you're reading may be wrong in ways you can't see. <a href=\"/monthly-bookkeeping/\">Computatio's Monthly Books</a> closes and reconciles your books each month and sets up your accounts so gross profit is visible; a person reviews and signs off on every account.</p>",
 "service": "monthly",
 "faq": [
  ("Is profit the same as cash in the bank?", "No. Profit measures income minus expenses for a period, while cash depends on when clients pay and when you pay bills. Run your profit and loss report on both a cash and an accrual basis to see the gap."),
  ("Do owner draws show up on the profit and loss report?", "Usually not. For sole proprietors and single-member LLCs, draws are typically recorded in equity, so the report can show a profit that is really your pay."),
  ("What counts as a direct cost for an agency?", "The costs of delivering client work: contractors, freelancers, wages for billable staff and anything you buy on a client's behalf. Keep them in their own section of the chart of accounts so gross profit is visible."),
  ("Should I use cash or accrual reports?", "Look at both. Accrual shows what you earned in a month; cash shows what actually came in and went out. The method on your tax return is a separate choice; ask your tax preparer which one your business uses."),
  ("How often should I check profitability?", "Every month, after all accounts are reconciled. Compare each month with the previous month and the same month last year."),
 ],
 "sources": [
  ("SBA: How to Understand a Profit and Loss Statement", "https://ascent.sba.gov/2a/a6/83cfbd2149a882a791f18f5cd2e6/your-business-financial-strategy-2-1-financial-statements-business-growth-decisions-tool.pdf"),
  ("SBA: Calculate & Analyze Your Financial Ratios", "https://ascent.sba.gov/4b/e9/d831e3d546ab9083d79b1f04f816/your-business-financial-strategy-2-4-financial-statements-business-growth-decisions-tool.pdf"),
  ("IRS Publication 538, Accounting Periods and Methods", "https://www.irs.gov/publications/p538"),
  ("IRS: S corporation compensation and medical insurance issues", "https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues"),
  ("Intuit: Choose between cash and accrual accounting methods in QuickBooks Online", "https://quickbooks.intuit.com/learn-support/en-us/help-article/product-preferences/choose-cash-accrual-accounting-methods-reports/L64yocn6B_US_en_US"),
 ],
},
]
