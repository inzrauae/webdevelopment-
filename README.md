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
