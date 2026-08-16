# HR Screening (internal tool)

**Status:** production-intended, used by Talent Acquisition to pre-filter
inbound job applications. Same profile as the `genuinely-high-risk-mock`
fixture, buried here in a subfolder of an otherwise-unrelated codebase to
test whether the compliance gate can find it without also flagging the
surrounding boilerplate.

`resume_scorer.py` computes a score per applicant from resume features
and auto-rejects anyone below `REJECT_THRESHOLD` — no recruiter reviews a
rejection before the candidate is notified, no bias/fairness testing has
been done, and the training data's provenance/demographics are
undocumented.
