# Prediction — large-mixed-codebase

**Expected severity:** `block` (at minimum `warn`), driven specifically by
`src/internal_tools/hr_screening/resume_scorer.py`.

**Expected article/annex citations:** Annex III(4)(a) (employment
screening) tied to `resume_scorer.py`, same reasoning as
`genuinely-high-risk-mock`. No citation should attach to
`src/utils/date_helpers.py` or `src/routes/status.py` — those are generic
boilerplate added in the same PR with no compliance relevance.

**Reasoning:** This PR's diff intentionally mixes two unrelated boilerplate
additions (`date_helpers.py`, `status.py` — plain utility/routing code)
with one genuinely high-risk component buried in a subfolder
(`resume_scorer.py` — auto-reject candidate scoring, no human review, no
bias assessment, same profile as fixture #3). A correct audit should find
and cite the buried component specifically — ideally with an `evidence`
file_path pointing at `resume_scorer.py` — and should NOT produce findings
whose evidence points at the boilerplate files. This tests whether the
tool's severity/citations track the actual risky file and not just "some
file changed in a PR with a risky file in it."
