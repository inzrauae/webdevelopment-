# Web Development Sri Lanka (webdevelopment.lk)

Static website for https://webdevelopment.lk.

## How to update the site

1. Edit the source files in `_build/` (pages and data in `build.py`, blog posts in `blog.py` and `blog_more.py`, page sections in `_build/parts/`), or the styles in `css/style.css` and the scripts in `js/main.js`.
2. Rebuild the HTML. Open a terminal in `_build/` and run:
   `python build.py .. .`
3. Commit and push to GitHub:
   `git add -A`, `git commit -m "Describe the change"`, `git push`
4. In cPanel, go to **Git Version Control → Manage → Pull or Deploy**, click **Update from Remote**, then **Deploy HEAD Commit**.

`.cpanel.yml` copies only the live website files into `public_html`.

When you change `css/style.css` or `js/main.js`, raise `CSSV` or `JSV` at the top of `_build/build.py` before rebuilding, so visitors' browsers load the new version.

## Scheduled blog posts (one per day)

- Scheduled posts live in `_build/posts/*.py`. Each post has `date='YYYY-MM-DD'` and only goes live on that day (Sri Lanka time).
- Until then the post is left out of the blog, home page, sitemap and llms.txt, and links to it from other posts stay as plain text.
- `.github/workflows/daily-publish.yml` rebuilds the site on GitHub every night at 00:05 Sri Lanka time and commits the result.
- A cPanel cron job pulls the repo and copies the files into `public_html` (see below).
- Cover images: `cd _build && python make_covers.py` creates `images/blog/<slug>.webp` for new posts (needs Pillow).
- To preview a future date locally: `PUBLISH_DATE=2026-12-14 python build.py .. .` (then rebuild without it before committing).

### cPanel cron job (hourly auto-deploy)

```
15 * * * * cd /home/webseodevlop/repositories/webdevelopment- && /usr/local/cpanel/3rdparty/bin/git pull -q origin main && /bin/cp -f *.html .htaccess robots.txt sitemap.xml llms.txt manifest.webmanifest sw.js /home/webseodevlop/public_html/ && /bin/cp -R css js images /home/webseodevlop/public_html/
```
