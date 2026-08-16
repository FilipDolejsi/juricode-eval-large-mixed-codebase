"""Generic string/number formatting helpers — boilerplate."""


def truncate(text: str, max_len: int = 80) -> str:
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def humanize_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}"
        n /= 1024
    return f"{n:.0f}TB"
