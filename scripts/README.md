# Build Scripts

## `fetch_genomicsxai_blogs.py`

Fetches your blog posts from the [Genomics × AI](https://genomicsxai.github.io/authors/alan-murphy/) author page and writes `_data/genomicsxai_blogs.yml`. This keeps the right sidebar on your homepage up to date.

**Run locally** (before `jekyll serve`):

```bash
pip install -r scripts/requirements.txt
python scripts/fetch_genomicsxai_blogs.py
```

**Automated:** The [GitHub Actions workflow](../.github/workflows/pages.yml) runs this script before each build. It also runs daily to refresh the list even when you don't push.
