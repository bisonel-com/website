# Bisonel Limited website

Static marketing site for [Bisonel Limited](https://bisonel.com).

Public preview (GitHub Pages project site):

**https://bisonel-com.github.io/website/**

## Stack

Plain multipage HTML, CSS, and a small amount of JavaScript. No runtime build step on Pages.

Pages:

- `/` Home
- `/services/`
- `/clients/`
- `/incubation/`
- `/about/`
- `/contact/`

Relative asset and nav paths work from the project Pages base path `/website/`.

Shared header, nav, and footer are assembled by `scripts/build_pages.py`. Re-run after copy or chrome changes:

```bash
python3 scripts/build_pages.py
```

## Brand assets

- `assets/logo.png`: BISONEL wordmark (header)
- `assets/favicon.png`: bison mark (favicon)

## Local preview

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Enable GitHub Pages

1. Open **Settings → Pages** on [bisonel-com/website](https://github.com/bisonel-com/website).
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Set **Branch** to `main` and **Folder** to `/ (root)`.
4. Save. After deploy, the site is at `https://bisonel-com.github.io/website/`.

No `CNAME` is included yet. When ready for the custom domain `bisonel.net`, add a `CNAME` file and DNS per GitHub Pages docs.
