# Build Scripts

## `fetch_genomicsxai_blogs.py`

Fetches your blog posts from the [Genomics × AI](https://genomicsxai.github.io/authors/alan-murphy/) author page and writes `_data/genomicsxai_blogs.yml`. This keeps the right sidebar on your homepage up to date.

## `fetch_twitter_rss.py`

Fetches tweets from a Twitter RSS feed and writes `_data/twitter_rss.yml` for the sidebar.

**Setup:** Twitter/X no longer offers native RSS. Create a feed at [RSS.app](https://rss.app/rss-feed/create-twitter-rss-feed) (free plan: 5 feeds, 24hr updates). Paste your X profile URL (e.g. `https://x.com/Al_Murphy_`) and generate the feed.

**Configure the feed URL:**
- Add `twitter_rss_url: "https://rss.app/feeds/xxxxx.xml"` to `_config.yml`, or
- Set `TWITTER_RSS_URL` in GitHub Actions secrets (Settings → Secrets → Actions)

**Run locally** (before `jekyll serve`):

```bash
pip install -r scripts/requirements.txt
python scripts/fetch_genomicsxai_blogs.py
python scripts/fetch_twitter_rss.py
```

**Automated:** The [GitHub Actions workflow](../.github/workflows/pages.yml) runs both scripts before each build. It also runs daily to refresh the lists even when you don't push.
