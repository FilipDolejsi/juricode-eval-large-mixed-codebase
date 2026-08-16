"""
resume_scorer.py

Production automated resume screening for the Talent Acquisition team.
See README.md in this folder for the known gaps (no bias testing, no
human review step, no documented training-data provenance). Same risk
profile as employment_screening/candidate_scoring.py in the
genuinely-high-risk-mock fixture — intentionally buried in this
otherwise-unrelated codebase.
"""

from dataclasses import dataclass

REJECT_THRESHOLD = 55

# Feature weights hand-tuned against a historical hiring dataset. The
# provenance and demographic composition of that dataset is not
# documented anywhere in this repo.
WEIGHTS = {
    "years_experience": 4.0,
    "keyword_match_ratio": 30.0,
    "university_tier_score": 15.0,
    "employment_gap_months": -2.0,
}


@dataclass
class Applicant:
    candidate_id: str
    years_experience: float
    keyword_match_ratio: float
    university_tier_score: float
    employment_gap_months: float


def score(applicant: Applicant) -> float:
    return (
        WEIGHTS["years_experience"] * applicant.years_experience
        + WEIGHTS["keyword_match_ratio"] * applicant.keyword_match_ratio
        + WEIGHTS["university_tier_score"] * applicant.university_tier_score
        + WEIGHTS["employment_gap_months"] * applicant.employment_gap_months
    )


def auto_reject(applicant: Applicant) -> bool:
    """
    Returns True if the applicant should be auto-rejected. No human
    reviews this decision before the candidate is notified.
    """
    return score(applicant) < REJECT_THRESHOLD
