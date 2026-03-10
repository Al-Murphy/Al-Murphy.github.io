# Build Scripts

## `fetch_genomicsxai_blogs.py`

Fetches your blog posts from the [Genomics × AI](https://genomicsxai.github.io/authors/alan-murphy/) author page and writes `_data/genomicsxai_blogs.yml`. This keeps the right sidebar on your homepage up to date.

## `fetch_featured_tweets.py`

Fetches recent tweets and writes `_data/featured_tweets.yml` for the sidebar embeds.

**Methods (in order of preference):**
1. **Twitter API** – Set `TWITTER_BEARER_TOKEN` (requires paid X developer account). Most reliable.
2. **ntscraper** – Uses Nitter instances. Free but can fail when instances are down. If the fetch fails, the existing YAML is kept.

**Run locally** (before `jekyll serve`):

```bash
pip install -r scripts/requirements.txt
python scripts/fetch_genomicsxai_blogs.py
python scripts/fetch_featured_tweets.py
```

**Automated:** The [GitHub Actions workflow](../.github/workflows/pages.yml) runs both scripts before each build. It also runs daily to refresh the lists even when you don't push.
