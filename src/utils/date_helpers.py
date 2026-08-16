"""Generic date helpers — boilerplate, unrelated to the rest of this PR."""

from datetime import datetime, timezone


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def days_between(a: datetime, b: datetime) -> int:
    return abs((b - a).days)
