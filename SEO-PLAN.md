# SEO Ranking Plan: Web Design Sri Lanka

## 1. Keyword map (done on the website)

| Keyword | Volume | KD | Page | Status |
|---|---|---|---|---|
| web design sri lanka | 3.6K | 56 | `index.html` | Title, H1, intro, 8 mentions, FAQ |
| web design / website design | 1.0K | 58 | `index.html`, `services.html` | Done |
| web design company sri lanka | 480 | 28 | `about.html` | Title + H1 + footer and home anchor links |
| web design company | 260 | 45 | `about.html` | Done |
| web design sri lanka price | 210 | 5 | `packages.html` | Title + H1 "Web Design Sri Lanka Price List" |
| what is web designing | 30 | – | `what-is-web-designing.html` | Article |
| how to start / how to do web designing | 30 / 20 | – | `how-to-start-web-designing.html` | Article |
| how to create web design, web page design, design in Photoshop | 20 | – | `how-to-create-a-web-design.html` | Article |
| best websites (cluster) | – | – | `best-website-design-examples.html` | Article |
| how to choose a web design company sri lanka | – | – | `how-to-choose-a-web-design-company-sri-lanka.html` | Article (supports About) |
| website cost / how much does a website cost in sri lanka | – | – | `website-cost-in-sri-lanka.html` | Article (supports Packages) |
| why business needs a website sri lanka | – | – | `why-your-business-needs-a-website.html` | Article (supports Home) |
| wordpress vs custom website | – | – | `wordpress-vs-custom-website.html` | Article (supports Services) |
| e-commerce website sri lanka | – | – | `ecommerce-website-sri-lanka.html` | Article (supports Packages) |
| seo for small business sri lanka | – | – | `seo-for-small-businesses-sri-lanka.html` | Article (supports Services) |
| hotel / villa website design sri lanka | – | – | `hotel-website-design-sri-lanka.html` | Article |
| web development sri lanka | – | – | `web-development-sri-lanka.html` | Article (supports Services / Home) |

**Rule:** do not create another page targeting "web design sri lanka". All other pages link to the home page with that phrase.

**How to rebuild the site after editing:** the build files live in `_build/`. Open a terminal in `_build/` and run:
`python build.py .. .`

## 2. Before going live (one-off)

1. Done: the domain is set (`SITE = 'https://webdevelopment.lk'` in `build.py`). Canonical URLs, Open Graph tags, breadcrumbs, `sitemap.xml` and `robots.txt` are generated on every build.
2. Done: email is admin@webdevelopment.lk and phone / WhatsApp is +94 77 960 4714 (set in `build.py` and `js/main.js`).
3. Add your real business address in the `ORG` schema (`address`) if you have one.
4. Use HTTPS, and redirect `http://` and `www.webdevelopment.lk` to `https://webdevelopment.lk` (the version used in the canonical URLs).

## 3. Google setup (week 1)

- **Google Search Console:** verify the domain, submit `sitemap.xml`, and request indexing for Home, Packages, About and the blog posts.
- **Google Business Profile:** category "Website designer". Use the same name, phone and website as the site. Add your services, the prices from LKR 20,000, photos of your work and a weekly post.
- **Google Analytics 4:** add the tag to `build.py` (`page()` head).

## 4. Backlinks: the ~75 referring domains you need

**a) Client websites (fastest and strongest).** Ask all 22 portfolio clients to add a footer credit:
`Website by <a href="https://webdevelopment.lk/">Web Design Sri Lanka</a>`
Vary the anchor text: "Web Design Sri Lanka", "web design company Sri Lanka", "Applantics".

**b) Business directories (target 25+).** Use the same name, phone and address (NAP) everywhere:
Clutch, DesignRush, GoodFirms, TechBehemoths, Sortlist, Upcity, The Manifest, LankaYP / Yellow Pages Sri Lanka, Hitad, ikman services, LinkedIn Company Page, Facebook Page, Behance, Dribbble, Crunchbase, Bing Places, Apple Business Connect.

**c) Reviews.** Ask every happy client for a Google review, and a Clutch review if they will. Aim for 20+ Google reviews.

**d) Content and PR (ongoing).**
- Guest posts on Sri Lankan business and tech blogs.
- Answer questions on Quora and Reddit, and in Facebook groups, linking to your blog guides.
- Publish case studies of client projects and share them on LinkedIn.

## 5. Content calendar (2 posts per month)

Ideas that target more keywords from your keyword research:

- Case study posts for each portfolio client
- Restaurant and café website design in Sri Lanka
- Website maintenance: what it includes and why it matters
- Website design for schools and institutes in Sri Lanka
- Landing pages vs websites for Facebook and Google ads

Add new posts to the `POSTS` list in `blog_more.py` (set `rel` to 3 related post slugs, and link to them from inside the text) and rebuild. They appear automatically on the blog, the home page strip and the sitemap.

## 6. Track monthly

- Rankings for the 5 main keywords, in Semrush or Search Console.
- Number of referring domains: aim for +10 per month.
- Search Console clicks, impressions and Core Web Vitals.
- Calls and WhatsApp enquiries from the website.

**Realistic timeline:**
- "web design sri lanka price" and "web design company sri lanka" can reach page 1 in about 1–3 months after launch.
- "web design sri lanka" (KD 56) typically takes about 4–8 months of consistent link building and content.
