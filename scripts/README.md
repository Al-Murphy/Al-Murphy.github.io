# Build Scripts

## `fetch_genomicsxai_blogs.py`

Fetches your blog posts from the [Genomics × AI](https://genomicsxai.github.io/authors/alan-murphy/) author page and writes `_data/genomicsxai_blogs.yml`. This keeps the right sidebar on your homepage up to date.

## `fetch_tweets.py`

Fetches your last few tweets via ntscraper (Nitter) and writes `_data/tweets.yml` for the sidebar. Free, no API keys needed. Nitter instances can be unreliable—if the fetch fails, the existing file is kept.

**Run locally** (before `jekyll serve`):

```bash
pip install -r scripts/requirements.txt
python scripts/fetch_genomicsxai_blogs.py
python scripts/fetch_tweets.py
```

**Automated:** The [GitHub Actions workflow](../.github/workflows/pages.yml) runs both scripts before each build and daily to refresh the lists.
