# Build Scripts

## `fetch_genomicsxai_blogs.py`

Fetches your blog posts from the [Genomics × AI](https://genomicsxai.github.io/authors/alan-murphy/) author page and writes `_data/genomicsxai_blogs.yml`. This keeps the right sidebar on your homepage up to date.

## `fetch_tweets.py`

Keeps the "Recent Tweets" sidebar list in `_data/tweets.yml` up to date. You choose *which* tweets appear; the script fills in the text and date for each one, so adding a tweet means adding its URL and nothing else:

```yaml
- url: "https://x.com/Al_Murphy_/status/2081701461918957801"
```

The next build turns that into a full entry with `title` and `date`. Entries are sorted newest first and the list is capped at the 5 most recent. Add `title_lock: true` to an entry to keep a hand-written title instead of the tweet's own text.

Free, no API keys: it reads the public syndication endpoint (`cdn.syndication.twimg.com`) that powers embedded tweets. If a fetch fails, that entry keeps whatever is already in the file, and the script always exits 0 so it can't break the build.

> **Why not fetch the timeline automatically?** It used to, via ntscraper/Nitter, but every public Nitter instance has since shut down or started blocking, so the fetch silently failed on every build and the file went stale (its dates drifted two years out). X has no free timeline API, and the syndication endpoint only serves one tweet at a time by ID — hence the curated list.

**Run locally** (before `jekyll serve`):

```bash
pip install -r scripts/requirements.txt
python scripts/fetch_genomicsxai_blogs.py
python scripts/fetch_tweets.py
```

**Automated:** The [GitHub Actions workflow](../.github/workflows/pages.yml) runs both scripts before each build and daily to refresh the lists.
