# Bisonel Limited website

Static marketing site for [Bisonel Limited](https://bisonel.com) (company number 14557664).

Public preview (GitHub Pages project site):

**https://bisonel-com.github.io/website/**

## Stack

Plain HTML, CSS, and a small amount of JavaScript. No build step. Relative asset paths so the site works from the project Pages base path `/website/`.

## Local preview

Open `index.html` in a browser, or serve the repo root:

```bash
python3 -m http.server 8080
```

Then visit `http://localhost:8080`.

## Enable GitHub Pages

Pages is not enabled until this is configured once in the repo settings:

1. Open **Settings → Pages** on [bisonel-com/website](https://github.com/bisonel-com/website).
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Set **Branch** to `main` and **Folder** to `/ (root)`.
4. Save. After the Pages deploy finishes, the site is at `https://bisonel-com.github.io/website/`.

No `CNAME` is included yet. When ready for the custom domain `bisonel.net`, add a `CNAME` file and DNS per GitHub Pages docs.
