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

ANSWERS = []
