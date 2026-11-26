import sys, io, re, json, html as htmllib
ROOT, S = sys.argv[1], sys.argv[2]
CSSV, JSV = '39', '17'
# Your live domain, e.g. 'https://www.webdesignsrilanka.lk' (no trailing slash).
# When set, canonical URLs, og:url/og:image, breadcrumbs schema and sitemap.xml are generated.
SITE = 'https://webdevelopment.lk'
BUILT = []
PHONE, PHONE_TEL, WA = '+94 77 960 4714', '+94779604714', '94779604714'
EMAIL = 'admin@webdevelopment.lk'
FACEBOOK = 'https://www.facebook.com/webdevelopmentsrilanka'
ADDR_COMPANY, ADDR_STREET, ADDR_CITY = 'Applantics (Pvt) Ltd', 'No. 2, U.B. Wijekoon Mawatha', 'Narammala'
ADDRESS = f'{ADDR_COMPANY}, {ADDR_STREET}, {ADDR_CITY}, Sri Lanka'
MAP_Q = 'No.+2+U.B.+Wijekoon+Mawatha+Narammala+Sri+Lanka'

def part(n): return io.open(f'{S}/parts/{n}.html', encoding='utf-8').read()

def fix_links(x):
    for a, b in [('href="#cta"', 'href="contact.html"'), ('href="#portfolio"', 'href="portfolio.html"'),
                 ('href="#services"', 'href="services.html"'), ('href="#pricing"', 'href="packages.html"'),
                 ('href="#process"', 'href="about.html"')]:
        x = x.replace(a, b)
    return x

def ic(n, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c}><use href="#i-{n}"/></svg>'
ARROW = '<svg class="ic arrow"><use href="#i-arrow"/></svg>'

EXTRA_ICONS = '''    <symbol id="i-wa" viewBox="0 0 24 24"><path d="M12 2.2A9.8 9.8 0 0 0 3.6 17l-1.4 4.9 5-1.3A9.8 9.8 0 1 0 12 2.2zm0 17.9a8.1 8.1 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.1 8.1 0 1 1 12 20.1zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.6 6.6 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.7 11.7 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z" fill="currentColor"/></symbol>
    <symbol id="i-clock" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9.5"/><path d="M12 7v5l3 2"/></g></symbol>
    <symbol id="i-users" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.5-3.5 3.2-5.5 6.5-5.5s6 2 6.5 5.5"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18 14.8c2 .6 3.2 2.3 3.5 5.2"/></g></symbol>
    <symbol id="i-target" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9.5"/><circle cx="12" cy="12" r="5.5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/></g></symbol>
    <symbol id="i-eye" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.7"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></g></symbol>
    <symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 20.5s-8.5-5-8.5-11A4.8 4.8 0 0 1 12 6.6a4.8 4.8 0 0 1 8.5 2.9c0 6-8.5 11-8.5 11z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></symbol>
    <symbol id="i-rocket" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 15c-1.5 1.3-2 5-2 5s3.7-.5 5-2c.7-.8.7-2.1-.1-2.9a2.1 2.1 0 0 0-2.9-.1z"/><path d="M12 15 9 12a22 22 0 0 1 2-4A12.9 12.9 0 0 1 22 2c0 2.7-.8 7.5-6 11a22 22 0 0 1-4 2z"/><path d="M9 12H4s.6-3 2-4c1.6-1.1 5 0 5 0M12 15v5s3-.6 4-2c1.1-1.6 0-5 0-5"/></g></symbol>
    <symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></symbol>
    <symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5.5h16v10H9l-5 4z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></symbol>
    <symbol id="i-award" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="m8.5 13.8-1.5 7.7 5-3 5 3-1.5-7.7"/></g></symbol>
    <symbol id="i-lock" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.7"><rect x="4.5" y="10.5" width="15" height="10.5" rx="2"/><path d="M8 10.5V7a4 4 0 0 1 8 0v3.5"/></g></symbol>
    <symbol id="i-search" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></g></symbol>
    <symbol id="i-home" viewBox="0 0 24 24"><path d="M3.5 10.5 12 3.5l8.5 7V20a1 1 0 0 1-1 1h-5v-6h-5v6h-5a1 1 0 0 1-1-1z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></symbol>
    <symbol id="i-apps" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3.5" y="3.5" width="7" height="7" rx="2"/><rect x="13.5" y="3.5" width="7" height="7" rx="2"/><rect x="3.5" y="13.5" width="7" height="7" rx="2"/><rect x="13.5" y="13.5" width="7" height="7" rx="2"/></g></symbol>
    <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h10" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></symbol>
    <symbol id="i-book" viewBox="0 0 24 24"><path d="M4 5.5A2 2 0 0 1 6 3.5h13v15H6a2 2 0 0 0-2 2zM4 20.5a2 2 0 0 0 2 2h13v-4M8 8h7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
    <symbol id="i-tag" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M3.5 12.6V4.5a1 1 0 0 1 1-1h8.1l8 8a1.5 1.5 0 0 1 0 2.1l-6.9 6.9a1.5 1.5 0 0 1-2.1 0z"/><circle cx="8.5" cy="8.5" r="1.6"/></g></symbol>
    <symbol id="i-info" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9.5"/><path d="M12 11v6M12 7.5v.1"/></g></symbol>
    <symbol id="i-x" viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></symbol>
  </defs>'''
SPRITE = part('sprite').replace('  </defs>', EXTRA_ICONS, 1)

SERVICES = [
  # id, icon, title, short, long, bullets, (desk, phone)
  ('web-design', 'brush', 'Website Design', 'Modern, responsive websites designed around your brand and built to convert visitors.',
   'We design professional business websites that look great on every screen and turn visitors into enquiries. Every site is custom designed around your brand, with clear messaging, fast loading and the calls to action that matter.',
   ['Custom, brand-matched design', 'Mobile-first, fully responsive', 'Contact forms, WhatsApp &amp; Google Maps', 'Easy-to-update CMS'], 'ruvinara'),
  ('ecommerce', 'cart', 'E-Commerce Websites', 'Online stores with local payment gateways, delivery options and easy product management.',
   'Sell online 24/7 with a fast, secure store built for Sri Lankan customers. We set up local payment gateways, cash on delivery, delivery zones and a simple dashboard to manage products, stock and orders.',
   ['Local card payments &amp; cash on delivery', 'Product, stock &amp; order management', 'Delivery zones &amp; SMS / email alerts', 'Conversion-focused product pages'], 'speedtech'),
  ('web-applications', 'code', 'Web Applications', 'Custom booking systems, portals and dashboards built with Laravel and React.',
   'When an off-the-shelf tool will not do, we build custom web applications: booking systems, customer portals, POS and inventory tools, live data dashboards and SaaS products, built to scale with your business.',
   ['Booking, POS &amp; inventory systems', 'Customer &amp; staff portals', 'APIs and third-party integrations', 'Secure logins and role-based access'], 'possystem'),
  ('ui-ux-design', 'layout', 'UI / UX Design', 'Wireframes, prototypes and clean interfaces that make your site a pleasure to use.',
   'Great design is more than looks. We research your customers, map their journeys and design intuitive interfaces with wireframes and clickable prototypes before a single line of code is written.',
   ['User research &amp; journey mapping', 'Wireframes and clickable prototypes', 'Design systems &amp; style guides', 'Usability-tested layouts'], 'officialcodex'),
  ('seo-marketing', 'trend', 'SEO &amp; Digital Marketing', 'Rank higher on Google, run targeted ads and grow your leads month after month.',
   'Get found by customers searching for what you sell. We handle technical SEO, on-page optimisation, Google Business Profile, content and paid ads, with clear monthly reports so you see what is working.',
   ['Technical &amp; on-page SEO', 'Google Business Profile optimisation', 'Google &amp; Meta ad campaigns', 'Monthly ranking &amp; traffic reports'], 'goldpricetoday'),
  ('hosting-maintenance', 'server', 'Hosting &amp; Maintenance', 'Fast, secure hosting with backups, updates and support so your site never sleeps.',
   'Keep your website fast, secure and always online. We provide managed hosting with SSL, daily backups, uptime monitoring, security updates and quick local support whenever you need a change.',
   ['Fast cloud hosting with free SSL', 'Daily backups &amp; uptime monitoring', 'Security &amp; software updates', 'Content edits and local support'], 'dagtech'),
]

PROJECTS = [
  ("speedtech", "SpeedTech IT Solutions", "https://speedtech.lk/", "speedtech.lk", "ecommerce", "E-Commerce", "Online store for computer repairs, upgrades, spare parts and accessories."),
  ("lastsolution", "Last Solution (Pvt) Ltd", "https://lastsolution.lk/", "lastsolution.lk", "corporate", "Corporate Website", "CCTV and security solutions provider in Kandy with product catalogue and enquiries."),
  ("officialcodex", "CODEX Global", "https://officialcodex.com/", "officialcodex.com", "ecommerce", "Fashion E-Commerce", "Premium streetwear brand from Sri Lanka with a bold, editorial online store."),
  ("islandtoursceylon", "Island Tours Ceylon", "https://islandtoursceylon.com/", "islandtoursceylon.com", "tourism", "Car Rental &amp; Tours", "Car rental in Sri Lanka with self-drive cars, airport transfers, chauffeur tours and an online vehicle search."),
  ("ruvinara", "Ruvinara Gems &amp; Jewellery", "http://ruvinara.com/", "ruvinara.com", "corporate", "Luxury Brand", "Elegant showcase for Ceylon gemstones, jewellery collections and import / export."),
  ("lankatourdriver", "Lanka Tour Driver", "https://lankatourdriver.com/", "lankatourdriver.com", "tourism", "Tour Packages", "Private Sri Lanka tours with a driver, tailor-made tour packages, safaris and a trip planner form."),
  ("dagtech", "DAG Tech Solutions", "https://dagtech.lk/", "dagtech.lk", "corporate", "Corporate / B2B", "Telecom and network supplies website for projects of every scale across Sri Lanka."),
  ("dooo", "dooo", "https://dooo.lk/", "dooo.lk", "ecommerce", "Fashion E-Commerce", "Fashionably elegant clothing store with a refined, minimal shopping experience."),
  ("themerchlist", "Merchlist", "https://themerchlist.com/", "themerchlist.com", "ecommerce", "Custom Merch Store", "UAE online store for custom T-shirts, corporate gifts and 1,000+ promotional products with an online design tool."),
  ("mypalmfit", "PALMFIT", "https://mypalmfit.com/", "mypalmfit.com", "ecommerce", "Activewear E-Commerce", "UAE-born gym wear and activewear brand store with men's and women's collections and fast UAE delivery."),
  ("fadeandblade", "Fade &amp; Blade UAE", "https://fadeandblade.ae/", "fadeandblade.ae", "booking", "Booking Website", "Mobile barber and gents salon services at home in the UAE with WhatsApp booking."),
  ("gauraconstruction", "Gaura Construction", "https://gauraconstruction.lk/", "gauraconstruction.lk", "corporate", "Corporate Website", "Construction company website with services, projects and a house budget planner."),
  ("goldpricetoday", "Gold Price Today", "https://goldpricetoday.lk/", "goldpricetoday.lk", "webapp", "Web Application", "Live gold rates in Sri Lanka, updated daily with karat-wise prices and charts."),
  ("possystem", "POS System Sri Lanka", "https://possystem.lk/", "possystem.lk", "webapp", "SaaS / Software", "AI-powered point of sale system website for retail and restaurant businesses."),
  ("flyse", "FLY SE", "https://flyse.se/", "flyse.se", "tourism", "Travel Agency", "Swedish travel agency website for tailor-made Sri Lanka holidays, tours and trip planning."),
  ("tuktukceylonrides", "TukTuk Ceylon Rides", "https://tuktukceylonrides.com/", "tuktukceylonrides.com", "tourism", "Rental Booking", "Self-drive tuk tuk rental in Sri Lanka with online booking and country versions for international travellers."),
  ("esms", "e-SMS", "https://e-sms.lk/", "e-sms.lk", "webapp", "SaaS / SMS Gateway", "SMS gateway in Sri Lanka for bulk SMS and OTPs to all four mobile networks, with clear pricing and a developer API."),
  ("4u", "4U.lk", "https://4u.lk/", "4u.lk", "webapp", "Classifieds Marketplace", "Buy and sell marketplace for vehicles, property, phones, jobs and services across all 25 districts of Sri Lanka."),
  ("rblmarketing", "RBL Marketing Agency", "https://rblmarketing.lk/", "rblmarketing.lk", "corporate", "Marketing Agency", "Sri Lankan marketing agency website for business, tuition class and event campaigns, social media promotion, web and SEO."),
  ("rblmarketingagency", "RBL Marketing Agency Platform", "https://rblmarketingagency.com/", "rblmarketingagency.com", "webapp", "Web Platform", "Social media engagement platform where members complete simple daily tasks and withdraw earnings to local banks."),
  ("seoservice", "seoservice.lk", "https://seoservice.lk/", "seoservice.lk", "corporate", "SEO Services", "SEO specialist website for Sri Lanka with services, case studies, pricing and a free SEO audit request."),
  ("uphonerepair", "&Uuml;Phone Repair", "http://uphonerepair.com/", "uphonerepair.com", "booking", "Repair Booking", "Same-day iPhone, iPad, Samsung and computer repair website with online repair booking and a blog."),
  ("manazelalreyada", "Manazel Al Reyada", "https://manazelalreyada.com/", "manazelalreyada.com", "corporate", "Facility Management", "Bilingual English and Arabic website for a Dubai facility management company offering AC, cleaning, plumbing, carpentry and electrical maintenance."),
]
NAMES = {p[0]: p[1] for p in PROJECTS}

def devices(slug, lazy=True):
    l = ' loading="lazy"' if lazy else ''
    n = NAMES[slug]
    return f'''<div class="pf-desk">
              <div class="pf-desk-screen"><img src="images/portfolio/{slug}-desktop.jpg" alt="{n} website design by Web Development Sri Lanka, desktop view"{l} /></div>
              <div class="pf-desk-chin"></div><div class="pf-desk-neck"></div><div class="pf-desk-base"></div>
            </div>
            <div class="pf-phone"><img src="images/portfolio/{slug}-mobile.jpg" alt="{n} website design by Web Development Sri Lanka, mobile view"{l} /></div>'''

# ---------------------------------------------------------------- client reviews (slug: role, quote)
REVIEWS = {
  'speedtech': ('Business Owner', 'We wanted a professional e-commerce website to showcase our computer accessories, spare parts and repair services. The team understood our business requirements and created a modern, user-friendly website. Really happy with the design and overall functionality.'),
  'lastsolution': ('Managing Director', 'Excellent website development service. They created a professional corporate website that presents our CCTV and security solutions clearly. The product catalogue and enquiry features are particularly useful for our business.'),
  'officialcodex': ('Founder', 'We needed something different from a traditional clothing website. The team understood our streetwear brand identity and delivered a bold, modern online store that matches our vision. Highly recommended for fashion brands.'),
  'islandtoursceylon': ('Business Owner', 'Our car rental and tourism business needed a website that international travellers could navigate easily. They developed a beautiful platform showcasing our vehicles, airport transfers and tour services. Very pleased with the outcome.'),
  'ruvinara': ('Managing Director', 'Presenting premium Ceylon gemstones online requires an elegant and trustworthy design. The team captured our brand identity beautifully. The website looks sophisticated and professionally represents our jewellery business.'),
  'lankatourdriver': ('Owner', 'They created a fantastic tourism website for our private tours and travel packages. The layout makes it easy for international customers to explore destinations and plan their holidays. A professional team that understands the tourism industry.'),
  'dagtech': ('Director', 'We are very satisfied with our new corporate website. It clearly communicates our telecommunications and networking solutions while maintaining a professional business image. Great attention to detail throughout the development.'),
  'dooo': ('Brand Owner', 'Absolutely love the clean and elegant design of our online clothing store. The website reflects our fashion brand perfectly without unnecessary complications. A great choice for anyone looking for modern e-commerce development.'),
  'themerchlist': ('Management Team', 'Our business requires a comprehensive e-commerce platform with a large product catalogue and custom merchandise options. The website development team demonstrated a strong understanding of our requirements and the UAE market. Excellent work.'),
  'mypalmfit': ('Brand Manager', 'We wanted an energetic, premium online shopping experience for our activewear brand. The website design matches our brand personality and makes browsing collections simple. Very happy with the overall presentation.'),
  'fadeandblade': ('Business Owner', 'The website is exactly what our mobile barber business needed. Customers can easily explore our services and contact us through WhatsApp for bookings. Simple, professional and effective.'),
  'gauraconstruction': ('Managing Director', 'Our new website professionally showcases our construction services and project portfolio. The house budget planning feature is a valuable addition for potential clients. Excellent understanding of construction industry requirements.'),
  'goldpricetoday': ('Platform Owner', 'Developing a gold price platform requires more than just good design. The team created a clean and functional web application that presents gold rates and price charts in an easy-to-understand format. Great technical expertise.'),
  'possystem': ('CEO', 'We needed a modern website that clearly communicates our software capabilities to retail and restaurant businesses. The design, structure and presentation reflect our technology-focused brand. A great example of professional software website development.'),
  'flyse': ('Business Owner', 'The team created a beautiful travel website that presents Sri Lanka as an attractive holiday destination for Swedish travellers. The design feels welcoming, professional and suitable for our international audience.'),
  'tuktukceylonrides': ('Founder', 'Our tuk tuk rental website needed to be attractive, informative and easy to use for foreign travellers. The team understood our concept and created a platform that reflects the adventurous experience we offer in Sri Lanka.'),
  'esms': ('Platform Manager', 'We wanted a professional SaaS website that explains our SMS gateway, pricing and developer API without making things complicated. The result is clean, modern and suitable for both businesses and developers.'),
  '4u': ('Founder', 'Building a classifieds marketplace involves many different categories and user requirements. The team created a well-organised platform with a modern interface that makes browsing listings straightforward. Impressive development capabilities.'),
  'rblmarketing': ('Managing Director', 'Our agency needed a website that effectively presents our marketing services and creative capabilities. The team delivered a modern design that reflects our business identity and makes our services easy to understand.'),
  'rblmarketingagency': ('CEO', 'We had a unique business concept that required custom web application development rather than a standard website. The team understood our requirements, including member dashboards, daily tasks and withdrawal functionality. Very pleased with the platform.'),
  'seoservice': ('Business Owner', 'As an SEO-focused business, we needed a website with a strong technical foundation, clear service pages and a professional appearance. The team created a modern website that represents our expertise and supports our digital marketing objectives.'),
  'uphonerepair': ('Business Owner', 'Our repair business needed a professional website where customers could easily find repair services and make online bookings. The new design is clean, mobile-friendly and well suited to our industry. Highly recommended for service-based businesses.'),
}
# Reviews from our own or sister businesses are kept but not shown as client reviews
OWN = {'seoservice', 'esms'}
STARS = '<div class="stars" role="img" aria-label="Rated 5 out of 5">' + ''.join('<svg aria-hidden="true"><use href="#i-star"/></svg>' for _ in range(5)) + '</div>'

def initials(name):
    w = [x for x in re.sub(r'&[a-z]+;|[^A-Za-z0-9 ]', ' ', plain(name)).split() if x]
    return (w[0][0] + (w[1][0] if len(w) > 1 else w[0][1:2])).upper() if w else '?'

def review_card(slug):
    role, quote = REVIEWS[slug]
    prj = next(p for p in PROJECTS if p[0] == slug)
    name, url, disp = prj[1], prj[2], prj[3]
    return f'''      <figure class="t-card">
        <svg class="q" aria-hidden="true"><use href="#i-quote"/></svg>
        {STARS}
        <blockquote>{quote}</blockquote>
        <figcaption><span class="t-av" aria-hidden="true">{initials(name)}</span><div><b>{name}</b><span>{role} · <a href="{url}" target="_blank" rel="noopener">{disp}</a></span></div></figcaption>
      </figure>'''

def testimonials(slugs, sub='Reviews from Sri Lankan and international businesses we have designed and built websites for.'):
    return f'''<!-- ================= TESTIMONIALS ================= -->
<section class="section testimonials">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Client Reviews</span>
      <h2>What Our <span class="accent">Clients Say</span></h2>
      <p>{sub}</p>
    </div>
    <div class="t-grid">
{chr(10).join(review_card(s) for s in slugs)}
    </div>
    <div class="center-btn"><a href="portfolio.html" class="btn btn-light btn-lg">See All Client Projects {ARROW}</a></div>
  </div>
</section>
'''
HOME_REVIEWS = ['speedtech', 'ruvinara', 'islandtoursceylon', 'themerchlist', 'goldpricetoday', 'uphonerepair']
ABOUT_REVIEWS = ['lastsolution', 'officialcodex', 'lankatourdriver', 'mypalmfit', 'possystem', 'gauraconstruction']

def card(p, review=False):
    slug, name, url, disp, cat, tag, desc = p
    return f'''        <article class="pf-card" data-cat="{cat}">
          <div class="pf-media">
            {devices(slug)}
          </div>
          <div class="pf-body">
            <span class="tag">{tag}</span>
            <h3>{name}</h3>
            <p>{desc}</p>
            {(f'<blockquote class="pf-review">{STARS}<p>&ldquo;{REVIEWS[slug][1]}&rdquo;</p><cite>{REVIEWS[slug][0]}, {name}</cite></blockquote>') if review and slug in REVIEWS and slug not in OWN else ''}
            <a class="pf-link" href="{url}" target="_blank" rel="noopener">{disp} {ic('arrow')}</a>
          </div>
        </article>'''

# ---------------------------------------------------------------- shell
NAV = [('index.html', 'Home'), ('services.html', 'Services'), ('portfolio.html', 'Portfolio'),
       ('packages.html', 'Packages'), ('about.html', 'About'), ('blog.html', 'Blog'), ('contact.html', 'Contact')]

def header(active):
    links = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ''
        if href == 'services.html':
            items = ''.join(f'\n          <a href="services.html#{s[0]}">{ic(s[1])}{s[2]}</a>' for s in SERVICES)
            links.append(f'''      <div class="dropdown">
        <a href="services.html"{cls}>Services {ic('chev', 'chev')}</a>
        <div class="dropdown-menu">{items}
        </div>
      </div>''')
        else:
            links.append(f'      <a href="{href}"{cls}>{label}</a>')
    return f'''<!-- ================= HEADER ================= -->
<header class="header on-dark" id="header">
  <div class="container nav-wrap">
    <a href="index.html" class="logo" aria-label="Web Development Sri Lanka home">
      <span class="logo-word">Web<b>Development</b></span>
      <span class="logo-tag">Sri Lanka · by Buddhika S Weerasekara</span>
    </a>
    <nav class="nav" id="nav">
{chr(10).join(links)}
    </nav>
    <div class="nav-actions">
      <a href="tel:{PHONE_TEL}" class="btn btn-light">{ic('phone', 'ic')}{PHONE}</a>
      <a href="contact.html" class="btn btn-primary">Get a Quote {ARROW}</a>
    </div>
    <button class="menu-toggle" id="menuToggle" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
'''

CTA = f'''<!-- ================= CTA ================= -->
<section class="cta-wrap" id="cta">
  <div class="container">
    <div class="cta">
      <div>
        <h2>Ready to Build Your New Website?</h2>
        <p>Tell us about your project and get a free, no-obligation quote within 24 hours.</p>
      </div>
      <div class="cta-actions">
        <a href="contact.html" class="btn btn-white btn-lg">Get a Free Quote {ARROW}</a>
        <a href="tel:{PHONE_TEL}" class="btn btn-outline-white btn-lg">{ic('phone', 'ic')}{PHONE}</a>
      </div>
    </div>
  </div>
</section>
'''

FOOTER = f'''<!-- ================= FOOTER ================= -->
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <a href="index.html" class="logo light"><span class="logo-word">Web<b>Development</b></span><span class="logo-tag">Sri Lanka · by Buddhika S Weerasekara</span></a>
      <p>Web Development Sri Lanka by Applantics is a web design company in Sri Lanka building websites, online stores and web apps for results.</p>
      <div class="socials">
        <a href="{FACEBOOK}" target="_blank" rel="noopener me" aria-label="Facebook page">{ic('fb')}</a>
        <a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic('wa')}</a>
        <a href="mailto:{EMAIL}" aria-label="Email">{ic('mail')}</a>
        <a href="tel:{PHONE_TEL}" aria-label="Call">{ic('phone')}</a>
      </div>
    </div>
    <div><h5>Services</h5>{''.join(f'<a href="services.html#{s[0]}">{s[2]}</a>' for s in SERVICES[:5])}</div>
    <div><h5>Company</h5><a href="about.html">Web Design Company Sri Lanka</a><a href="packages.html">Web Design Sri Lanka Price</a><a href="portfolio.html">Web Design Portfolio</a><a href="blog.html">Web Design Blog</a><a href="contact.html">Contact</a></div>
    <div><h5>Get in Touch</h5><a href="tel:{PHONE_TEL}" class="fc">{ic('phone')}{PHONE}</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener" class="fc">{ic('wa')}WhatsApp Us</a><a href="mailto:{EMAIL}" class="fc">{ic('mail')}{EMAIL}</a><a href="https://www.google.com/maps/search/?api=1&amp;query={MAP_Q}" target="_blank" rel="noopener" class="fc fc-addr">{ic('pin')}<span>{ADDR_COMPANY}<br />{ADDR_STREET}, {ADDR_CITY}, Sri Lanka</span></a></div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; <span id="year"></span> Web Development Sri Lanka by Applantics. All rights reserved.</span>
    <span><a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms of Service</a></span>
  </div>
</footer>

<a href="https://wa.me/{WA}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ic('wa')}</a>
'''

TABS = [('index.html', 'home', 'Home'), ('services.html', 'apps', 'Services'), None, ('portfolio.html', 'layout', 'Work')]
SHEET = [('index.html', 'home', 'Home'), ('services.html', 'apps', 'Services'), ('portfolio.html', 'layout', 'Portfolio'), ('packages.html', 'tag', 'Packages'),
         ('about.html', 'info', 'About'), ('blog.html', 'book', 'Blog'), ('contact.html', 'chat', 'Contact'), ('tel:' + PHONE_TEL, 'phone', 'Call Us')]
def appbar(active):
    tabs = []
    for t in TABS:
        if t is None:
            tabs.append(f'<a href="https://wa.me/{WA}" class="tbi tbi-wa" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><span>{ic("wa")}</span><em>WhatsApp</em></a>')
        else:
            h, i, l = t
            on, cur = (' on', ' aria-current="page"') if h == active else ('', '')
            tabs.append(f'<a href="{h}" class="tbi{on}"{cur}>{ic(i)}<em>{l}</em></a>')
    tabs.append(f'<button class="tbi" id="sheetOpen" aria-label="Open menu" aria-controls="sheet" aria-expanded="false">{ic("menu")}<em>Menu</em></button>')
    tiles = ''.join(f'<a href="{h}" class="sh-tile{" on" if h == active else ""}"><span>{ic(i)}</span>{l}</a>' for h, i, l in SHEET)
    svcs = ''.join(f'<a href="services.html#{s[0]}">{ic(s[1])}{s[2]}{ic("chev-r", "go")}</a>' for s in SERVICES)
    return f'''<!-- ================= MOBILE APP BAR ================= -->
<nav class="tabbar" aria-label="Quick navigation">{"".join(tabs)}</nav>
<div class="sheet" id="sheet" aria-hidden="true">
  <div class="sheet-bg" data-close></div>
  <div class="sheet-panel" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="sheet-grab" data-close><i></i></div>
    <div class="sheet-head"><a href="index.html" class="logo"><span class="logo-word">Web<b>Development</b></span><span class="logo-tag">Sri Lanka · by Buddhika S Weerasekara</span></a><button class="sheet-x" data-close aria-label="Close menu">{ic('x')}</button></div>
    <div class="sheet-body">
      <div class="sh-grid">{tiles}</div>
      <b class="sh-label">Our services</b>
      <div class="sh-list">{svcs}</div>
    </div>
    <div class="sheet-foot">
      <a href="https://wa.me/{WA}" class="btn btn-wa" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
      <a href="contact.html" class="btn btn-primary">Free Quote {ARROW}</a>
    </div>
  </div>
</div>
'''

def plain(s): return htmllib.unescape(re.sub(r'<[^>]+>', '', s)).strip()

ORG = {
  '@context': 'https://schema.org', '@type': 'ProfessionalService', '@id': '#business',
  'name': 'Web Development Sri Lanka', 'alternateName': ['Web Design Sri Lanka', 'Web Development Sri Lanka by Buddhika S Weerasekara', 'Web Development Sri Lanka by Applantics'],
  'description': 'Web design and web development company in Sri Lanka building mobile-friendly, SEO-ready business websites, e-commerce stores and web applications.',
  'telephone': PHONE_TEL, 'email': EMAIL, 'priceRange': 'LKR 20,000 - LKR 39,000+', 'currenciesAccepted': 'LKR',
  'address': {'@type': 'PostalAddress', 'streetAddress': 'No. 2, U.B. Wijekoon Mawatha', 'addressLocality': 'Narammala', 'addressRegion': 'North Western Province', 'addressCountry': 'LK'},
  'areaServed': {'@type': 'Country', 'name': 'Sri Lanka'},
  'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 'opens': '09:00', 'closes': '18:00'}],
  'knowsAbout': ['Web design', 'Web development', 'E-commerce development', 'UI/UX design', 'Search engine optimisation', 'Web hosting'],
  'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Website packages', 'itemListElement': [
    {'@type': 'Offer', 'name': n, 'price': p, 'priceCurrency': 'LKR', 'itemOffered': {'@type': 'Service', 'name': n}}
    for n, p in [('Starter business website', '20000'), ('Business website', '30000'), ('E-commerce website', '39000')]]}
}

PERSON = {
  '@context': 'https://schema.org', '@type': 'Person', 'name': 'Buddhika S Weerasekara',
  'jobTitle': 'Web Developer &amp; SEO Specialist', 'worksFor': {'@id': '#business'},
  'knowsAbout': ['Web design', 'Web development', 'Search engine optimisation', 'Generative engine optimisation', 'E-commerce development'],
  'sameAs': ['https://seoservice.lk/'], 'nationality': {'@type': 'Country', 'name': 'Sri Lanka'}
}
if 'example.com' in EMAIL: ORG.pop('email', None)

def person_ld():
    d = dict(PERSON); d['jobTitle'] = plain(d['jobTitle'])
    if SITE: d.update({'@id': f'{SITE}/#founder', 'url': f'{SITE}/about.html', 'worksFor': {'@id': f'{SITE}/#business'}})
    return d

def faq_schema(items):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': plain(q), 'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in items]}

IMG_SIZES = {'-desktop.jpg': (1440, 900), '-tablet.jpg': (768, 1050), '-mobile.jpg': (390, 844)}
def nofollow_clients(html):
    """Client website links get rel="nofollow noopener" (rel="me" links to our own profiles are left alone)."""
    hosts = {re.sub(r'^https?://(www\.)?', '', p[2]).strip('/').lower() for p in PROJECTS}
    def fix(m):
        tag, url = m.group(0), m.group(1)
        host = re.sub(r'^https?://(www\.)?', '', url).split('/')[0].lower()
        if host not in hosts or re.search(r'rel="[^"]*\bme\b', tag): return tag
        if 'rel="' in tag: return re.sub(r'rel="[^"]*"', 'rel="nofollow noopener"', tag)
        return tag[:-1] + ' rel="nofollow noopener">'
    return re.sub(r'<a\b[^>]*href="(https?://[^"]+)"[^>]*>', fix, html)

def img_dims(html):
    """Give every <img> a width/height so the page does not jump while loading (CLS)."""
    def fix(m):
        tag = m.group(0)
        if 'width=' in tag: return tag
        src = re.search(r'src="([^"]+)"', tag).group(1)
        wh = next((v for k, v in IMG_SIZES.items() if src.endswith(k)), None)
        if not wh:
            q = re.search(r'[?&]w=(\d+)&(?:amp;)?h=(\d+)', src)
            wh = (int(q.group(1)), int(q.group(2))) if q else None
        if not wh: return tag
        extra = '' if 'decoding=' in tag else ' decoding="async"'
        return tag[:4] + f' width="{wh[0]}" height="{wh[1]}"{extra}' + tag[4:]
    return re.sub(r'<img\b[^>]*>', fix, html)

def page(file, title, desc, body, active=None, faqs=None, crumb=None, ld_extra=None, og_type='website', og_img=None):
    BUILT.append(file)
    url = f'{SITE}/' + ('' if file == 'index.html' else file) if SITE else ''
    org = dict(ORG)
    if SITE: org.update({'@id': f'{SITE}/#business', 'url': f'{SITE}/', 'image': f'{SITE}/images/og-image.jpg',
                         'logo': {'@type': 'ImageObject', 'url': f'{SITE}/images/icon-512.png', 'width': 512, 'height': 512},
                         'founder': {'@id': f'{SITE}/#founder'}, 'sameAs': [FACEBOOK, 'https://seoservice.lk/']})
    data = [org]
    if file == 'index.html':
        data.append({'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Web Development Sri Lanka', 'alternateName': ['WebDevelopment.lk', 'Web Development LK'], 'inLanguage': 'en-LK',
                     **({'@id': f'{SITE}/#website', 'url': f'{SITE}/', 'publisher': {'@id': f'{SITE}/#business'}} if SITE else {})})
    if file in ('index.html', 'about.html'): data.append(person_ld())
    if crumb and SITE:
        data.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': f'{SITE}/'},
            {'@type': 'ListItem', 'position': 2, 'name': plain(crumb), 'item': url}]})
    if faqs: data.append(faq_schema(faqs))
    if ld_extra: data += ld_extra
    ld = '\n'.join(f'  <script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in data)
    abs_tags = (f'''  <link rel="canonical" href="{url}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/{og_img or 'images/og-image.jpg'}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="{675 if og_img else 630}" />
  <meta name="twitter:image" content="{SITE}/{og_img or 'images/og-image.jpg'}" />
''' if SITE else '')
    html = f'''<!DOCTYPE html>
<html lang="en-LK">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="google-site-verification" content="SpKqGz24boeyDIz5oEE-En4Ni3BAmk8EDuyBMyTMWDc" />
  <meta name="theme-color" content="#0b1533" />
  <meta name="mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-title" content="Web Development SL" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="format-detection" content="telephone=no" />
  <link rel="manifest" href="manifest.webmanifest" />
  <link rel="icon" href="/favicon.ico" sizes="48x48" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="icon" type="image/png" sizes="96x96" href="images/favicon-96.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="images/icon-192.png" />
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png" />
  <meta name="geo.region" content="LK" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:locale" content="en_LK" />
  <meta property="og:site_name" content="Web Development Sri Lanka" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
{abs_tags}{ld}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css?v={CSSV}" />
</head>
<body class="pg-{file[:-5]}">

{SPRITE.strip()}

{header(active or file)}
{body.strip()}

{FOOTER}
{appbar(active or file)}
<script src="js/main.js?v={JSV}"></script>
</body>
</html>
'''
    html = nofollow_clients(img_dims(html))
    io.open(f'{ROOT}/{file}', 'w', encoding='utf-8', newline='\n').write(html)

def page_hero(eyebrow, h1, sub, crumb, chips=()):
    chip_html = ''.join(f'<div class="ph-chip ph-chip-{i+1}"><span>{ic(c[0])}</span><div><b>{c[1]}</b><small>{c[2]}</small></div></div>' for i, c in enumerate(chips))
    return f'''<!-- ================= PAGE HERO ================= -->
<section class="page-hero">
  <svg class="ph-bg" viewBox="0 0 1600 520" preserveAspectRatio="none" aria-hidden="true">
    <defs><linearGradient id="phNavy" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22357a"/><stop offset="1" stop-color="#16245a"/></linearGradient><linearGradient id="phEdge" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff7a1a" stop-opacity="0"/><stop offset=".22" stop-color="#ff7a1a" stop-opacity="0"/><stop offset=".42" stop-color="#ff7a1a"/><stop offset="1" stop-color="#ff7a1a"/></linearGradient></defs>
    <path d="M1180 0 C 1110 120, 1010 230, 990 340 C 975 430, 1030 490, 1120 520 H 1600 V 0 Z" fill="url(#phNavy)"/>
    <path d="M1180 0 C 1110 120, 1010 230, 990 340 C 975 430, 1030 490, 1120 520" fill="none" stroke="url(#phEdge)" stroke-width="10"/>
    <path d="M0 440 C 120 455, 230 490, 330 520 H 0 Z" fill="#ff6a00" opacity=".9"/>
  </svg>
  <div class="ph-glow"></div>
  <div class="container ph-grid">
    <div class="ph-inner">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a>{ic('chev-r')}<span>{crumb}</span></nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{sub}</p>
    </div>
    <div class="ph-chips">{chip_html}</div>
  </div>
</section>
'''

def check_list(items):
    return '<ul class="check-list">' + ''.join(f'<li>{ic("check")}{x}</li>' for x in items) + '</ul>'
def faq_list(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}<span>{ic("plus")}</span></summary><p>{a}</p></details>' for q, a in items) + '</div>'
exec(io.open(f'{S}/content.py', encoding='utf-8').read())

# ---------------------------------------------------------------- HOME
hero = fix_links(part('hero'))
services_home = f'''<!-- ================= SERVICES ================= -->
<section class="section" id="services">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our Services</span>
      <h2>Complete Web Solutions for <span class="accent">Your Business</span></h2>
      <p>Everything you need to launch, run and grow a successful website, all under one roof.</p>
    </div>
    <div class="feature-grid">
''' + '\n'.join(f'      <a class="feature" href="services.html#{s[0]}"><span class="f-ic">{ic(s[1])}</span><h3>{s[2]}</h3><p>{s[3]}</p><span class="f-more">Learn more {ic("arrow")}</span></a>' for s in SERVICES) + f'''
    </div>
    <div class="center-btn"><a href="services.html" class="btn btn-light btn-lg">View All Services {ARROW}</a></div>
  </div>
</section>
'''
portfolio_home = f'''<!-- ================= PORTFOLIO ================= -->
<section class="section portfolio" id="portfolio">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Portfolio</span>
      <h2>Websites We've <span class="accent">Designed &amp; Built</span></h2>
      <p>Real projects for real businesses, crafted to look great and work perfectly on desktop and mobile.</p>
    </div>
    <div class="pf-grid">
{chr(10).join(card(p) for p in PROJECTS[:6])}
    </div>
    <div class="center-btn"><a href="portfolio.html" class="btn btn-light btn-lg">View All Projects {ARROW}</a></div>
  </div>
</section>
'''
# (home page is written at the end of the file, after the FAQ helpers)

# ---------------------------------------------------------------- SERVICES
rows = []
for i, (sid, icon, title, short, long, bullets, slug) in enumerate(SERVICES):
    media = part('hosting-media').strip() if sid == 'hosting-maintenance' else f'''<div class="svc-media pf-media">
            {devices(slug, lazy=i > 0)}
      </div>'''
    rows.append(f'''    <div class="svc-row" id="{sid}">
      {media}
      <div class="svc-text">
        <span class="f-ic">{ic(icon)}</span>
        <span class="svc-num">0{i+1}</span>
        <h2>{title}</h2>
        <p>{long}</p>
        {check_list(bullets)}
        <div class="svc-actions">
          <a href="contact.html?service={sid}" class="btn btn-primary">Get a Quote {ARROW}</a>
          <a href="packages.html" class="btn btn-light">See Packages</a>
        </div>
      </div>
    </div>''')
STEPS5 = [('search', 'Discover', 'We learn about your business, customers and goals.'),
          ('layout', 'Plan &amp; Wireframe', 'We map the pages, content and user journeys.'),
          ('brush', 'Design', 'You review and approve a custom visual design.'),
          ('code', 'Develop &amp; Test', 'We build it with clean, fast and secure code.'),
          ('rocket', 'Launch &amp; Support', 'We go live, set up SEO and keep it running.')]
proc = f'''<section class="section bg-soft">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Our Process</span>
      <h2>How We Deliver <span class="accent">Every Project</span></h2>
      <p>A proven, transparent five-step process, with regular updates at every stage.</p>
    </div>
    <ol class="proc-grid">
''' + '\n'.join(f'      <li class="proc"><span class="proc-n">{i+1:02d}</span><span class="f-ic">{ic(s[0])}</span><h3>{s[1]}</h3><p>{s[2]}</p></li>' for i, s in enumerate(STEPS5)) + '''
    </ol>
  </div>
</section>
'''
TECH = ['HTML5 &amp; CSS3', 'JavaScript', 'React', 'Laravel', 'PHP', 'WordPress', 'WooCommerce', 'Shopify', 'Node.js', 'MySQL', 'Figma', 'Google Analytics']
tech = '''<section class="section tech">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Technology</span>
      <h2>Tools &amp; Platforms <span class="accent">We Work With</span></h2>
    </div>
    <ul class="tech-list">''' + ''.join(f'<li>{t}</li>' for t in TECH) + '''</ul>
  </div>
</section>
'''
page('services.html', 'Website Design &amp; Web Development Services in Sri Lanka',
     'Professional web design and web development services in Sri Lanka: business websites, e-commerce stores, web applications, UI/UX, SEO and hosting.',
     page_hero('Our Services', 'Web Design &amp; Development <span class="accent">Services</span>',
               'As a web design and web development company in Sri Lanka, we take you from a simple business website to a full online store or custom web app, and help it grow.',
               'Services', [('mobile', 'Mobile First', 'Every screen size'), ('trend', 'SEO Ready', 'Built to rank')]) +
     '''<section class="section svc-overview">
  <div class="container">
    <div class="feature-grid">
''' + '\n'.join(f'      <a class="feature" href="#{s[0]}"><span class="f-ic">{ic(s[1])}</span><h3>{s[2]}</h3><p>{s[3]}</p><span class="f-more">Learn more {ic("arrow")}</span></a>' for s in SERVICES) + '''
    </div>
  </div>
</section>
<section class="section svc-details">
  <div class="container">
''' + '\n'.join(rows) + '''
  </div>
</section>
''' + proc + tech + SVC_SEO + faq_section('services-faq', 'Web Development Services <span class="accent">FAQs</span>', 'Common questions about our web design and web development services in Sri Lanka.', SVC_FAQ) + CTA, 'services.html', crumb='Services', faqs=SVC_FAQ)

# ---------------------------------------------------------------- PORTFOLIO
INDUSTRIES = [('cart', 'Retail'), ('fork', 'Restaurants'), ('hotel', 'Hotels'), ('palm', 'Tourism'), ('corp', 'Corporate'), ('health', 'Healthcare'), ('edu', 'Education'), ('code', 'Software &amp; SaaS')]
page('portfolio.html', 'Web Design Portfolio Sri Lanka | Websites We Have Built',
     'See real websites, online stores and web applications designed and developed in Sri Lanka by Web Development Sri Lanka, shown on desktop, tablet and mobile.',
     page_hero('Portfolio', 'Websites We\'ve <span class="accent">Designed &amp; Built</span>',
               'Real projects for real businesses across Sri Lanka and beyond, shown on desktop and mobile exactly as their customers see them.',
               'Portfolio', [('award', '100+ Projects', 'Delivered'), ('heart', '4.9/5 Rating', 'Happy clients')]) +
     f'''<section class="section portfolio">
  <div class="container">
    <div class="pf-filters" role="tablist">
      <button class="on" data-filter="all">All Projects</button>
      <button data-filter="ecommerce">E-Commerce</button>
      <button data-filter="corporate">Corporate</button>
      <button data-filter="webapp">Web Apps</button>
      <button data-filter="booking">Booking</button>
      <button data-filter="tourism">Tourism</button>
    </div>
    <div class="pf-grid" id="pfGrid">
{chr(10).join(card(p, review=True) for p in PROJECTS)}
    </div>
  </div>
</section>
''' + part('stats') + PF_SEO + f'''
<section class="section" id="industries">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Industries</span>
      <h2>Built for <span class="accent">Every Industry</span></h2>
      <p>Whatever your business, we understand what your customers need to see online.</p>
    </div>
    <ul class="ind-grid">''' + ''.join(f'<li><span class="f-ic">{ic(a)}</span>{b}</li>' for a, b in INDUSTRIES) + '''</ul>
  </div>
</section>
''' + CTA, crumb='Portfolio')

# ---------------------------------------------------------------- PACKAGES
CMP = [('Number of pages', 'Up to 5', 'Up to 15', 'Unlimited'),
       ('Mobile-responsive design', 1, 1, 1),
       ('Custom UI design', 0, 1, 1),
       ('Contact form &amp; WhatsApp chat', 1, 1, 1),
       ('Basic SEO setup', 1, 1, 1),
       ('Advanced SEO &amp; Google Analytics', 0, 1, 1),
       ('Blog / CMS', 0, 1, 1),
       ('Online payments', 0, 0, 1),
       ('Orders, stock &amp; delivery management', 0, 0, 1),
       ('Free SSL &amp; first-year hosting', 1, 1, 1),
       ('Free support', '1 month', '3 months', '6 months'),
       ('Delivery time', '1–2 weeks', '3–4 weeks', '4–6 weeks')]
def cell(v):
    if v == 1: return f'<td><span class="yes">{ic("check")}</span></td>'
    if v == 0: return f'<td><span class="no">{ic("x")}</span></td>'
    return f'<td>{v}</td>'
cmp_rows = ''.join(f'<tr><th scope="row">{r[0]}</th>{cell(r[1])}{cell(r[2])}{cell(r[3])}</tr>' for r in CMP)
FAQ = [('What is the web design price in Sri Lanka?', 'Our web design Sri Lanka price list starts from LKR 20,000 for a starter business website, LKR 30,000 for a custom business website and LKR 39,000 for an e-commerce store. Every package can be tailored, and you get a written quote with no hidden fees.'),
       ('How long does it take to build a website?', 'Most business websites are ready in 1–4 weeks and online stores in 4–6 weeks, depending on the number of pages, features and how quickly content is provided.'),
       ('Do I need to provide the content and photos?', 'You know your business best, so we ask for your key information. We can also help write content, source quality stock images and arrange professional photography.'),
       ('Can I update the website myself?', 'Yes. We build on an easy-to-use CMS and show you how to edit text, images, products and blog posts. We are always available if you would rather we do it.'),
       ('Is hosting and a domain included?', 'Every package includes free SSL and first-year hosting. We can register a .lk or .com domain for you, or connect one you already own.'),
       ('Do you offer payment plans?', 'Yes. We usually work with a 50% advance and 50% on completion, and we can discuss instalments for larger projects.'),
       ('What happens after the free support period?', 'You can choose an affordable monthly maintenance plan covering hosting, backups, security updates and content changes, or contact us only when you need help.')]
INCLUDED = [('mobile', 'Responsive Design', 'Looks perfect on phones, tablets and desktops.'),
            ('lock', 'Free SSL Security', 'The padlock that builds trust and helps SEO.'),
            ('bolt', 'Fast Loading', 'Optimised images and code for top speed.'),
            ('trend', 'SEO Foundations', 'Clean structure, meta tags and sitemap.'),
            ('wa', 'WhatsApp Integration', 'Customers can chat with you in one tap.'),
            ('chat', 'Local Support', 'Real people in Sri Lanka, ready to help.')]
page('packages.html', 'Web Design Sri Lanka Price List 2026 | From LKR 20,000',
     'Web design Sri Lanka price list for 2026. Starter websites from LKR 20,000, business websites from LKR 30,000 and e-commerce stores from LKR 39,000. No hidden fees.',
     page_hero('Web Design Sri Lanka Price', 'Web Design Sri Lanka <span class="accent">Price List</span>',
               'Choose a starting point that fits your business. Every package can be tailored, and there are no hidden costs.',
               'Packages', [('shield', 'No Hidden Fees', 'Clear quotes'), ('clock', 'Fast Delivery', 'From 1 week')]) +
     re.sub(r'\s*<div class="section-head">.*?</div>', '', fix_links(part('pricing')), count=1, flags=re.S) +
     '''<section class="section bg-soft">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Every Package Includes</span>
      <h2>The Essentials, <span class="accent">Always Included</span></h2>
    </div>
    <div class="feature-grid">
''' + '\n'.join(f'      <article class="feature"><span class="f-ic">{ic(a)}</span><h3>{b}</h3><p>{c}</p></article>' for a, b, c in INCLUDED) + f'''
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Compare</span>
      <h2>Compare <span class="accent">Packages</span></h2>
    </div>
    <div class="cmp-wrap">
      <table class="cmp-table">
        <thead><tr><th>Features</th><th>Starter<small>LKR 20,000</small></th><th class="hl">Business<small>LKR 30,000</small></th><th>E-Commerce<small>LKR 39,000</small></th></tr></thead>
        <tbody>{cmp_rows}</tbody>
      </table>
    </div>
    <p class="note">Need something custom, like a web application or booking system? <a href="contact.html">Ask for a tailored quote</a>.</p>
  </div>
</section>
''' + PKG_SEO + f'''<section class="section bg-soft">
  <div class="container narrow">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>Frequently Asked <span class="accent">Questions</span></h2>
    </div>
    {faq_list(FAQ + PKG_EXTRA_FAQ)}
  </div>
</section>
''' + CTA, faqs=FAQ + PKG_EXTRA_FAQ, crumb='Packages')

# ---------------------------------------------------------------- ABOUT
VALUES = [('target', 'Our Mission', 'To give every Sri Lankan business, big or small, a professional website that wins customers and grows with them.'),
          ('eye', 'Our Vision', 'To be the most trusted web design partner in Sri Lanka, known for quality, honesty and real results.'),
          ('heart', 'Our Values', 'Clear communication, fair pricing, on-time delivery and support you can count on long after launch.')]
WHY = [('users', 'Local Expert Team', 'Designers and developers based in Sri Lanka who understand your market.'),
       ('brush', '100% Custom Design', 'No cookie-cutter templates: every site is designed around your brand.'),
       ('bolt', 'Fast Turnaround', 'Most websites go live in weeks, not months.'),
       ('trend', 'Built to Rank', 'SEO-friendly structure and speed from day one.'),
       ('shield', 'Secure &amp; Reliable', 'SSL, backups and updates keep your site safe.'),
       ('chat', 'Ongoing Support', 'Call or WhatsApp us any time you need a hand.')]
page('about.html', 'Web Design Company Sri Lanka | About Our Team',
     'Web Development Sri Lanka by Applantics is a web design company in Sri Lanka building fast, SEO-ready websites, online stores and web apps from LKR 20,000.',
     page_hero('Web Design Company Sri Lanka', 'A Web Design Company in Sri Lanka <span class="accent">That Delivers</span>',
               'Web Development Sri Lanka is the web design company of Applantics, helping businesses across Sri Lanka look professional online and win more customers.',
               'About', [('award', '9+ Years', 'Experience'), ('users', '100+ Clients', 'Served')]) +
     f'''<section class="section facts-sec" id="at-a-glance">
  <div class="container narrow">
    <div class="section-head">
      <span class="eyebrow">Quick Facts</span>
      <h2>Web Development Sri Lanka <span class="accent">at a Glance</span></h2>
    </div>
    <dl class="facts">
      <div><dt>Who we are</dt><dd>A web design and web development company in Sri Lanka, part of Applantics</dd></div>
      <div><dt>Led by</dt><dd>Buddhika S Weerasekara, web developer and SEO specialist (<a href="https://seoservice.lk/" target="_blank" rel="me noopener">seoservice.lk</a>)</dd></div>
      <div><dt>What we build</dt><dd>Business websites, e-commerce stores, web applications, UI/UX design, SEO and hosting</dd></div>
      <div><dt>Prices</dt><dd>From LKR 20,000 (starter), LKR 30,000 (business with CMS) and LKR 39,000 (e-commerce). <a href="packages.html">See the price list</a></dd></div>
      <div><dt>Included</dt><dd>Mobile-friendly design, on-page SEO, free SSL and first-year hosting</dd></div>
      <div><dt>Our work</dt><dd>{len(PROJECTS)} live client websites in Sri Lanka, the UAE and Sweden. <a href="portfolio.html">View the portfolio</a></dd></div>
      <div><dt>Office &amp; service area</dt><dd>{ADDRESS}. Working with clients across Sri Lanka and overseas, online, by phone and on WhatsApp</dd></div>
      <div><dt>Contact</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a> (call or WhatsApp), <a href="mailto:{EMAIL}">{EMAIL}</a>. Monday to Saturday, 9:00 to 18:00</dd></div>
    </dl>
  </div>
</section>
<section class="section">
  <div class="container how-grid">
    <div class="how-visual">
      <div class="team-img"><img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1100&h=800&fit=crop" alt="Our web design team at work" /></div>
      <div class="how-card hc-1"><span class="dot-live"></span><div><b>100+ websites</b><small>Delivered and live</small></div></div>
      <div class="how-card hc-2">{ic('check')}<div><b>4.9/5 rating</b><small>From happy clients</small></div></div>
    </div>
    <div class="about-text">
      <span class="eyebrow">Who We Are</span>
      <h2>Helping Sri Lankan Businesses <span class="accent">Grow Online</span></h2>
      <p class="lead">For more than nine years we have designed and built websites, online stores and web applications for retailers, restaurants, hotels, construction firms, jewellers, tech companies and more.</p>
      <p>We believe a website should do more than look good. It should load fast, be easy to use on a phone, show up on Google and turn visitors into customers. That is why every project starts with understanding your business and ends with a site you are proud to share.</p>
      {check_list(['Custom design for every client', 'Transparent pricing with no hidden fees', 'Support from a real local team'])}
      <a href="contact.html" class="btn btn-primary btn-lg">Work With Us {ARROW}</a>
    </div>
  </div>
</section>
''' + ABOUT_SEO + f'''<section class="section bg-soft">
  <div class="container">
    <div class="value-grid">
''' + '\n'.join(f'      <article class="feature value"><span class="f-ic">{ic(a)}</span><h3>{b}</h3><p>{c}</p></article>' for a, b, c in VALUES) + '''
    </div>
  </div>
</section>
''' + part('stats') + '''
<section class="section">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why Choose Us</span>
      <h2>Why Businesses <span class="accent">Choose Us</span></h2>
      <p>We combine great design, solid development and honest service.</p>
    </div>
    <div class="feature-grid">
''' + '\n'.join(f'      <article class="feature"><span class="f-ic">{ic(a)}</span><h3>{b}</h3><p>{c}</p></article>' for a, b, c in WHY) + '''
    </div>
  </div>
</section>
''' + fix_links(testimonials(ABOUT_REVIEWS)) + CTA, crumb='About')

# ---------------------------------------------------------------- CONTACT
svc_opts = ''.join(f'<option value="{s[0]}">{s[2]}</option>' for s in SERVICES)
CFAQ = FAQ[:3]
page('contact.html', 'Contact Web Development Sri Lanka | Free Quote in 24 Hours',
     'Get a free, no-obligation web design quote in Sri Lanka. Call or WhatsApp +94 77 960 4714 or send your project details and we will reply within 24 hours.',
     page_hero('Contact Us', 'Let\'s Build Your <span class="accent">New Website</span>',
               'Tell us about your project and get a free, no-obligation quote within 24 hours. Prefer to talk? Call or WhatsApp us any time.',
               'Contact', [('clock', 'Reply in 24h', 'Free quote'), ('wa', 'WhatsApp', 'Quick chat')]) +
     f'''<section class="section contact">
  <div class="container contact-grid">
    <div class="contact-info">
      <h2>Get in <span class="accent">Touch</span></h2>
      <p class="lead">We would love to hear about your business. Reach us the way that suits you best.</p>
      <a class="info-card" href="tel:{PHONE_TEL}"><span class="f-ic">{ic('phone')}</span><div><small>Call Us</small><b>{PHONE}</b></div></a>
      <a class="info-card" href="https://wa.me/{WA}" target="_blank" rel="noopener"><span class="f-ic">{ic('wa')}</span><div><small>WhatsApp</small><b>Chat with us now</b></div></a>
      <a class="info-card" href="mailto:{EMAIL}"><span class="f-ic">{ic('mail')}</span><div><small>Email Us</small><b>{EMAIL}</b></div></a>
      <div class="info-card"><span class="f-ic">{ic('clock')}</span><div><small>Working Hours</small><b>Mon – Sat, 9.00 am – 6.00 pm</b></div></div>
      <div class="info-card"><span class="f-ic">{ic('pin')}</span><div><small>Office</small><b>{ADDR_COMPANY}, {ADDR_STREET}, {ADDR_CITY}, Sri Lanka</b></div></div>
    </div>
    <form class="form-card" id="quoteForm" novalidate>
      <h3>Request a Free Quote</h3>
      <p>Fill in the form and we will send your details to us on WhatsApp.</p>
      <div class="f-row">
        <label>Your Name *<input name="name" required autocomplete="name" placeholder="John Perera" /></label>
        <label>Phone / WhatsApp *<input name="phone" type="tel" required autocomplete="tel" placeholder="07X XXX XXXX" /></label>
      </div>
      <div class="f-row">
        <label>Email<input name="email" type="email" autocomplete="email" placeholder="you@company.lk" /></label>
        <label>Company / Business<input name="company" autocomplete="organization" placeholder="Your business name" /></label>
      </div>
      <div class="f-row">
        <label>Service Needed<select name="service"><option value="">Select a service</option>{svc_opts}</select></label>
        <label>Budget<select name="budget"><option value="">Select a budget</option><option>Under LKR 20,000</option><option>LKR 20,000 – 30,000</option><option>LKR 30,000 – 40,000</option><option>LKR 40,000 – 100,000</option><option>Above LKR 100,000</option><option>Not sure yet</option></select></label>
      </div>
      <label>Project Details *<textarea name="message" rows="5" required placeholder="Tell us about your business and what you need..."></textarea></label>
      <p class="f-error" id="formError" role="alert"></p>
      <div class="f-actions">
        <button type="submit" class="btn btn-primary btn-lg">{ic('wa', 'ic')}Send via WhatsApp</button>
        <button type="button" class="btn btn-light btn-lg" id="sendEmail">{ic('mail', 'ic')}Send via Email</button>
      </div>
    </form>
  </div>
</section>
''' + CONTACT_SEO + f'''<section class="map-wrap">
  <div class="container">
    <iframe class="map" title="Map of our office in Narammala, Sri Lanka" src="https://maps.google.com/maps?q={MAP_Q}&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
<section class="section">
  <div class="container narrow">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>Before You <span class="accent">Get in Touch</span></h2>
    </div>
    {faq_list(CFAQ)}
    <div class="center-btn"><a href="packages.html" class="btn btn-light btn-lg">View Packages {ARROW}</a></div>
  </div>
</section>
''', faqs=CFAQ, crumb='Contact')

# ---------------------------------------------------------------- LEGAL
def legal(file, title, crumb, sections):
    body = ''.join(f'<h2>{h}</h2>' + ''.join(f'<p>{p}</p>' for p in ps) for h, ps in sections)
    page(file, f'{title} | Web Development Sri Lanka', f'{title} for Web Development Sri Lanka by Applantics.',
         page_hero('Legal', title, 'Last updated: November 2026', crumb) +
         f'<section class="section"><div class="container narrow prose">{body}</div></section>', file, crumb=crumb)
legal('privacy.html', 'Privacy Policy', 'Privacy Policy', [
  ('Information We Collect', ['When you contact us or request a quote, we collect the details you provide, such as your name, phone number, email address, business name and project details.']),
  ('How We Use Your Information', ['We use your information only to respond to your enquiry, prepare quotes, deliver our services and communicate with you about your project. We do not sell or rent your personal information.']),
  ('Cookies &amp; Analytics', ['Our website may use cookies and analytics tools to understand how visitors use the site so we can improve it. You can disable cookies in your browser settings.']),
  ('Third-Party Services', ['Links and services such as WhatsApp, Google Maps and Google Fonts are provided by third parties with their own privacy policies.']),
  ('Contact', [f'If you have any questions about this policy, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.'])])
legal('terms.html', 'Terms of Service', 'Terms of Service', [
  ('Quotes &amp; Payments', ['All quotes are valid for 30 days. Unless agreed otherwise, projects begin after a 50% advance payment, with the balance due on completion before the website goes live.']),
  ('Project Timelines', ['Timelines depend on receiving content, feedback and approvals from the client on time. Delays in providing these may extend the delivery date.']),
  ('Revisions', ['Each package includes reasonable design revisions during the design stage. Major changes in scope after approval may be quoted separately.']),
  ('Ownership', ['Once full payment is received, you own your website design and content. Third-party themes, plugins and stock images remain subject to their own licences.']),
  ('Hosting &amp; Support', ['Hosting, domains and support are provided for the periods stated in your package. Renewals are billed annually unless cancelled.']),
  ('Contact', [f'Questions about these terms? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.'])])

exec(io.open(f'{S}/blog.py', encoding='utf-8').read())

# ---------------------------------------------------------------- HOME (SEO content + FAQ)
DISTRICTS = ['Colombo', 'Gampaha', 'Negombo', 'Kalutara', 'Kandy', 'Galle', 'Matara', 'Hambantota', 'Kurunegala', 'Puttalam',
             'Anuradhapura', 'Polonnaruwa', 'Jaffna', 'Trincomalee', 'Batticaloa', 'Ampara', 'Ratnapura', 'Kegalle', 'Badulla', 'Nuwara Eliya']
exec(io.open(f'{S}/seo_block.py', encoding='utf-8').read())
exec(io.open(f'{S}/types_block.py', encoding='utf-8').read())
HFAQ = [('How much does a website cost in Sri Lanka?', 'With Web Development Sri Lanka, a starter business website starts from LKR 20,000, a custom business website with a CMS from LKR 30,000 and an e-commerce website with online payments from LKR 39,000. Custom web applications are quoted per project after a free consultation.'),
        ('How long does it take to design and develop a website?', 'A starter website is usually ready in 1–2 weeks, a business website in 3–4 weeks and an online store in 4–6 weeks. Timelines depend on the number of pages, features and how quickly content is provided.'),
        ('What is the difference between web design and web development?', 'Web design is how your website looks and feels: layout, colours, typography and user experience. Web development is the code that makes it work: pages, forms, online payments, databases and admin panels. We handle both, so you deal with one team from start to finish.'),
        ('Do you build e-commerce websites with online payments in Sri Lanka?', 'Yes. We build online stores that accept card payments through Sri Lankan payment gateways, along with bank transfer and cash on delivery. They include product, stock, order and delivery management.'),
        ('Will my website be mobile-friendly and SEO-ready?', 'Every website we build is fully responsive and includes on-page SEO: keyword-focused titles and meta descriptions, a proper heading structure, structured data, an XML sitemap, fast loading and Google Search Console setup.'),
        ('Do you provide web design services outside Colombo?', 'Yes. We work with businesses across Sri Lanka, including Gampaha, Kandy, Galle, Matara, Kurunegala, Jaffna, Batticaloa and Trincomalee. Everything can be done online, by phone or over WhatsApp.'),
        ('Can I update my website myself after it is launched?', 'Yes. We build on an easy-to-use content management system and show you how to edit text, images, products and blog posts. If you prefer, we can make updates for you under a maintenance plan.'),
        ('Do you provide hosting, a .lk domain and maintenance?', 'Every package includes free SSL and first-year hosting. We can register a .lk or .com domain for you or connect one you already own, and we offer affordable monthly maintenance covering backups, security updates and content changes.')]
home_faq = f'''<section class="section" id="faq">
  <div class="container narrow">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>Web Design Sri Lanka <span class="accent">FAQs</span></h2>
      <p>Answers to the questions Sri Lankan businesses ask us most about getting a new website.</p>
    </div>
    {faq_list(HFAQ)}
  </div>
</section>
'''

page('index.html', 'Web Development Sri Lanka | Web Design Company',
     'Web design &amp; web development in Sri Lanka by Applantics. Mobile-friendly, SEO-ready business websites, online stores &amp; web apps from LKR 20,000. Get a free quote.',
     hero + services_home + portfolio_home + fix_links(part('process')) + part('stats') + fix_links(part('pricing')) + fix_links(testimonials(HOME_REVIEWS)) + seo_block + HOME_MORE + home_faq + f'''<section class="section bg-soft" id="guides">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Web Design Blog</span>
      <h2>Free Web Design <span class="accent">Guides</span></h2>
      <p>Learn what web designing is, how to start, and how to plan a website that wins customers.</p>
    </div>
    <div class="blog-grid blog-grid-4">
{chr(10).join(post_card(q) for q in LATEST[:4])}
    </div>
    <div class="center-btn"><a href="blog.html" class="btn btn-light btn-lg">Read All Guides {ARROW}</a></div>
  </div>
</section>
''' + CTA,
     faqs=HFAQ)

# ---------------------------------------------------------------- 404 page (not indexed, not in the sitemap)
page('404.html', 'Page Not Found | Web Development Sri Lanka',
     'The page you are looking for could not be found. Browse our web design services, packages and portfolio.',
     page_hero('Error 404', 'Sorry, This Page Could Not Be Found',
               'The link may be old or mistyped. These pages will help you find what you need.', 'Page Not Found') +
     f'''<section class="section"><div class="container narrow center-btn" style="display:flex;flex-wrap:wrap;gap:.8rem;justify-content:center">
  <a href="index.html" class="btn btn-primary btn-lg">Go to Home {ARROW}</a>
  <a href="services.html" class="btn btn-light btn-lg">Services</a>
  <a href="packages.html" class="btn btn-light btn-lg">Packages &amp; Prices</a>
  <a href="portfolio.html" class="btn btn-light btn-lg">Portfolio</a>
  <a href="blog.html" class="btn btn-light btn-lg">Blog</a>
</div></section>
''' + CTA)
BUILT.remove('404.html')
_f = f'{ROOT}/404.html'
_s = io.open(_f, encoding='utf-8').read()
_s = _s.replace('content="index, follow, max-image-preview:large"', 'content="noindex, follow"')
_s = re.sub(r'  <link rel="canonical"[^>]*>\n', '', _s)
_s = _s.replace('<meta charset="UTF-8" />', '<meta charset="UTF-8" />\n  <base href="/" />', 1)
io.open(_f, 'w', encoding='utf-8', newline='\n').write(_s)

# ---------------------------------------------------------------- llms.txt (summary for AI search engines)
if SITE:
    def _t(f):
        m = re.search(r'<title>(.*?)</title>', io.open(f'{ROOT}/{f}', encoding='utf-8').read())
        return plain(m.group(1)) if m else f
    def _d(f):
        m = re.search(r'<meta name="description" content="(.*?)"', io.open(f'{ROOT}/{f}', encoding='utf-8').read())
        return plain(m.group(1)) if m else ''
    main_pages = ['index.html', 'services.html', 'packages.html', 'portfolio.html', 'about.html', 'contact.html', 'blog.html']
    guides = [f for f in BUILT if f not in main_pages and f not in ('privacy.html', 'terms.html')]
    L = [f'# Web Development Sri Lanka', '',
         f'> Web Development Sri Lanka ({SITE}/) is a web design and web development company in Sri Lanka, led by Buddhika S Weerasekara. '
         'It builds mobile-friendly, SEO-ready business websites, e-commerce stores and custom web applications for businesses across Sri Lanka and abroad.', '',
         '## Key facts', '',
         '- Business name: Web Development Sri Lanka',
         '- Led by: Buddhika S Weerasekara, web developer and SEO specialist (https://seoservice.lk/)',
         '- Company: part of Applantics',
         '- Location: Sri Lanka; works with clients across Sri Lanka and overseas, online, by phone and WhatsApp',
         f'- Phone and WhatsApp: {PHONE}',
         f'- Email: {EMAIL}',
         f'- Facebook: {FACEBOOK}',
         f'- Address: {ADDRESS}',
         '- Opening hours: Monday to Saturday, 9:00 to 18:00 (Sri Lanka time)',
         '- Prices: starter business website from LKR 20,000; business website with CMS from LKR 30,000; e-commerce website from LKR 39,000; custom web applications quoted per project',
         '- Every package includes a mobile-friendly design, on-page SEO, free SSL and first-year hosting',
         '- Services: ' + '; '.join(plain(s[2]) for s in SERVICES),
         f'- Portfolio: {len(PROJECTS)} live client websites, including ' + ', '.join(f'{plain(p[1])} ({p[3]})' for p in PROJECTS[:10]),
         '', '## Main pages', '']
    L += [f'- [{_t(f)}]({SITE}/{"" if f == "index.html" else f}): {_d(f)}' for f in main_pages]
    L += ['', '## Guides', '']
    L += [f'- [{_t(f)}]({SITE}/{f}): {_d(f)}' for f in guides]
    L += ['', '## Frequently asked questions', '']
    L += [f'**{plain(q)}**\n{plain(a)}\n' for q, a in HFAQ]
    L += ['## Optional', '', f'- [Privacy Policy]({SITE}/privacy.html)', f'- [Terms of Service]({SITE}/terms.html)', '']
    io.open(f'{ROOT}/llms.txt', 'w', encoding='utf-8', newline='\n').write('\n'.join(L))

# ---------------------------------------------------------------- .htaccess (Apache / cPanel hosting)
io.open(f'{ROOT}/.htaccess', 'w', encoding='utf-8', newline='\n').write('''# Web Development Sri Lanka: server rules for Apache / cPanel hosting
Options -Indexes
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
  RewriteEngine On
  # Force HTTPS and the non-www domain (matches the canonical URLs)
  RewriteCond %{HTTPS} off [OR]
  RewriteCond %{HTTP_HOST} ^www\\. [NC]
  RewriteRule ^(.*)$ https://webdevelopment.lk/$1 [L,R=301]
  # /index.html and /index -> /
  RewriteCond %{THE_REQUEST} \\s/index(\\.html)?[\\s?] [NC]
  RewriteRule ^index(\\.html)?$ / [L,R=301]
  # /about.html -> /about (301, keeps one clean URL per page)
  RewriteCond %{THE_REQUEST} \\s/([^.\\s?]+)\\.html[\\s?] [NC]
  RewriteRule ^ /%1 [L,R=301]
  # /about/ -> /about
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule ^([^/.]+)/$ /$1 [L,R=301]
  # Serve /about from about.html
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{DOCUMENT_ROOT}/$1.html -f
  RewriteRule ^([^/.]+)$ /$1.html [L]
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/javascript application/json application/xml image/svg+xml application/manifest+json
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 month"
  ExpiresByType image/png "access plus 1 month"
  ExpiresByType image/webp "access plus 1 month"
  ExpiresByType image/svg+xml "access plus 1 year"
</IfModule>

<IfModule mod_headers.c>
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
  <FilesMatch "sw\\.js$">
    Header set Cache-Control "no-cache"
  </FilesMatch>
</IfModule>

AddType application/manifest+json .webmanifest
AddType text/plain .txt
AddDefaultCharset utf-8
''')

# ---------------------------------------------------------------- robots.txt + sitemap.xml
robots = ('User-agent: *\nAllow: /\nDisallow: /_build/\n\n'
          '# AI search and answer engines are welcome to read and cite this site\n'
          + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'PerplexityBot', 'Google-Extended', 'Applebot-Extended', 'Bingbot']))
if SITE:
    robots += f'\nSitemap: {SITE}/sitemap.xml\n'
    pri = {'index.html': '1.0', 'services.html': '0.9', 'packages.html': '0.9', 'portfolio.html': '0.8', 'contact.html': '0.8', 'about.html': '0.7'}
    urls = ''.join(f'  <url><loc>{SITE}/{"" if f == "index.html" else f}</loc><lastmod>{PAGE_DATE.get(f, "2026-11-25")}</lastmod><priority>{pri.get(f, "0.3" if f in ("privacy.html", "terms.html") else "0.6")}</priority></url>\n' for f in sorted(BUILT, key=lambda f: -float(pri.get(f, "0.3" if f in ("privacy.html", "terms.html") else "0.6"))))
    io.open(f'{ROOT}/sitemap.xml', 'w', encoding='utf-8', newline='\n').write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
io.open(f'{ROOT}/robots.txt', 'w', encoding='utf-8', newline='\n').write(robots)

# ---------------------------------------------------------------- clean URLs (/about instead of /about.html)
_stems = sorted({f[:-5] for f in BUILT} | {'404'}, key=len, reverse=True)
_alt = '|'.join(re.escape(s) for s in _stems)
def _clean(s):
    s = re.sub(r'href="(' + _alt + r')\.html(#[^"]*)?"', lambda m: f'href="/{"" if m.group(1) == "index" else m.group(1)}{m.group(2) or ""}"', s)
    if SITE:
        s = re.sub(re.escape(SITE) + r'/(' + _alt + r')\.html', lambda m: f'{SITE}/{"" if m.group(1) == "index" else m.group(1)}', s)
    return s
for _f in [f'{x}.html' for x in _stems] + ['sitemap.xml', 'llms.txt']:
    _p = f'{ROOT}/{_f}'
    try: _s = io.open(_p, encoding='utf-8').read()
    except FileNotFoundError: continue
    io.open(_p, 'w', encoding='utf-8', newline='\n').write(_clean(_s))

print('built')
