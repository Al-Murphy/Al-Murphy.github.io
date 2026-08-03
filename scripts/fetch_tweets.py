#!/usr/bin/env python3
"""
Hydrate _data/tweets.yml from X's public syndication endpoint.

You curate *which* tweets appear by listing their URLs in _data/tweets.yml;
this script fills in the text and the date for each one. So a new entry only
needs the URL:

    - url: "https://x.com/Al_Murphy_/status/2081701461918957801"

...and the next build turns it into a full entry with title and date.

Why not scrape the timeline? X has no free API for that, and the previous
ntscraper/Nitter approach is dead (public Nitter instances have all shut down
or are blocked), which is why the dates in this file drifted out of sync.
The syndication endpoint below is the same public JSON that powers embedded
tweets: no API key, no auth, but it only serves one tweet at a time by ID.

Add `title_lock: true` to an entry to keep a hand-written title instead of the
tweet's own text.

Fetches are best-effort: anything that fails keeps whatever is already in the
file, and the script always exits 0 so it can never break the site build.
"""
import html
import math
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
import yaml

OUTPUT_FILE = Path(__file__).resolve().parent.parent / "_data" / "tweets.yml"
SYNDICATION_URL = "https://cdn.syndication.twimg.com/tweet-result"
USER_AGENT = "Mozilla/5.0 (compatible; Jekyll-Tweet-Fetcher/1.0)"
MAX_TWEETS = 5
MAX_TITLE_CHARS = 140  # the sidebar column is narrow; longer titles wrap badly

DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"


def tweet_id_from_url(url: str) -> Optional[str]:
    """Pull the numeric status ID out of an x.com/twitter.com URL."""
    m = re.search(r"/status(?:es)?/(\d+)", str(url))
    return m.group(1) if m else None


def _base36(value: float, frac_digits: int = 20) -> str:
    """Base-36 representation of a float, mirroring JS Number.toString(36)."""
    whole = int(value)
    out = ""
    while whole:
        out = DIGITS[whole % 36] + out
        whole //= 36
    out = out or "0"

    frac = value - int(value)
    if frac:
        out += "."
        for _ in range(frac_digits):
            frac *= 36
            digit = int(frac)
            out += DIGITS[digit]
            frac -= digit
    return out


def syndication_token(tweet_id: str) -> str:
    """Token the syndication endpoint expects, as derived by X's own embed code."""
    return re.sub(r"(0+|\.)", "", _base36((int(tweet_id) / 1e15) * math.pi))


def clean_text(text: str) -> str:
    """Flatten tweet text into a single line suitable for a sidebar link."""
    text = html.unescape(text or "").strip()
    # Drop the trailing t.co link X appends for quoted tweets / media.
    text = re.sub(r"\s*https://t\.co/\w+\s*$", "", text)
    text = re.sub(r"\s+", " ", text)
    if len(text) > MAX_TITLE_CHARS:
        cut = text[: MAX_TITLE_CHARS - 1]
        # Prefer a word boundary, unless that would lop off most of the text.
        space = cut.rfind(" ")
        if space > MAX_TITLE_CHARS * 0.6:
            cut = cut[:space]
        text = cut.rstrip(" ,;:-–—") + "…"
    return text


def fetch_tweet(tweet_id: str) -> Optional[Dict[str, str]]:
    """Fetch one tweet's text and date. Returns None if it can't be retrieved."""
    try:
        resp = requests.get(
            SYNDICATION_URL,
            params={"id": tweet_id, "token": syndication_token(tweet_id), "lang": "en"},
            headers={"User-Agent": USER_AGENT},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:  # network error, rate limit, deleted tweet, bad JSON
        print(f"  ! {tweet_id}: fetch failed ({e})", file=sys.stderr)
        return None

    # A protected or deleted tweet comes back as an empty object.
    if not isinstance(data, dict) or not data.get("text"):
        print(f"  ! {tweet_id}: no text in response (deleted or protected?)", file=sys.stderr)
        return None

    title = clean_text(data["text"])
    if not title:
        return None

    result = {"title": title}
    created = str(data.get("created_at") or "")
    if re.match(r"\d{4}-\d{2}-\d{2}", created):
        result["date"] = created[:10]
    return result


def load_entries() -> List[Dict[str, Any]]:
    """Read the curated list, keeping any hand-written values as fallbacks."""
    if not OUTPUT_FILE.exists():
        return []
    try:
        data = yaml.safe_load(OUTPUT_FILE.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as e:
        print(f"Could not parse {OUTPUT_FILE}: {e}", file=sys.stderr)
        return []
    if not isinstance(data, list):
        print(f"{OUTPUT_FILE} is not a YAML list; leaving it alone.", file=sys.stderr)
        return []
    return [e for e in data if isinstance(e, dict) and e.get("url")]


def write_yaml(items: List[Dict[str, Any]]) -> None:
    lines = [
        "# Curated by hand, hydrated by scripts/fetch_tweets.py (GitHub Actions).",
        "# To feature a tweet, add an entry with just its URL — the next build",
        "# fills in the title and date:",
        "#",
        '#   - url: "https://x.com/Al_Murphy_/status/1234567890"',
        "#",
        "# Add `title_lock: true` to keep a hand-written title.",
        "",
    ]
    for item in items:
        title = str(item.get("title", "")).replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'- title: "{title}"')
        lines.append(f'  url: "{item["url"]}"')
        lines.append(f'  date: "{item.get("date", "")}"')
        if item.get("title_lock"):
            lines.append("  title_lock: true")
        lines.append("")
    OUTPUT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    entries = load_entries()
    if not entries:
        print(f"No tweet URLs listed in {OUTPUT_FILE}; nothing to do.", file=sys.stderr)
        return 0

    resolved: List[Dict[str, Any]] = []
    fetched = 0
    for entry in entries:
        url = str(entry["url"])
        tweet_id = tweet_id_from_url(url)
        if not tweet_id:
            # Probably a typo — pass it through untouched rather than deleting it.
            print(f"  ! no tweet ID in URL, leaving as-is: {url}", file=sys.stderr)
            if entry.get("title"):
                resolved.append(entry)
            continue

        item: Dict[str, Any] = {"url": url}
        if entry.get("title_lock"):
            item["title_lock"] = True

        live = fetch_tweet(tweet_id)
        if live:
            fetched += 1
            item["date"] = live.get("date") or entry.get("date", "")
            item["title"] = entry.get("title", "") if entry.get("title_lock") else live["title"]
        else:
            # Keep whatever was already there rather than dropping the entry.
            item["date"] = entry.get("date", "")
            item["title"] = entry.get("title", "")

        if not item["title"]:
            print(f"  ! skipping {url}: no title available", file=sys.stderr)
            continue
        resolved.append(item)

    if not resolved:
        print("Nothing resolved; leaving tweets.yml unchanged.", file=sys.stderr)
        return 0

    # Newest first; undated entries sink to the bottom rather than the top.
    resolved.sort(key=lambda i: i.get("date") or "", reverse=True)
    dropped = len(resolved) - MAX_TWEETS
    if dropped > 0:
        print(f"Showing newest {MAX_TWEETS} of {len(resolved)} tweets.", file=sys.stderr)
    resolved = resolved[:MAX_TWEETS]

    write_yaml(resolved)
    print(f"Wrote {len(resolved)} tweets to {OUTPUT_FILE} ({fetched} refreshed from X).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
