# Long-form SEO content for each page. Executed inside build.py (uses ic, check_list, faq_list, ARROW).

def seo_section(sid, eyebrow, h2, intro, cards, soft=False):
    body = ''
    for c in cards:
        h3, html = c[0], c[1]
        wide = ' seo-wide' if len(c) > 2 and c[2] else ''
        body += f'      <article class="seo-card{wide}"><h3>{h3}</h3>{html}</article>\n'
    return f'''<section class="section seo-block{' bg-soft' if soft else ''}" id="{sid}">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{h2}</h2>
      <p>{intro}</p>
    </div>
    <div class="seo-grid">
{body}    </div>
  </div>
</section>
'''

def faq_section(sid, h2, intro, items, soft=False):
    return f'''<section class="section{' bg-soft' if soft else ''}" id="{sid}">
  <div class="container narrow">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>{h2}</h2>
      <p>{intro}</p>
    </div>
    {faq_list(items)}
  </div>
</section>
'''

def bullets(items):
    return '<ul class="seo-why">' + ''.join(f'<li><b>{a}</b> {b}</li>' for a, b in items) + '</ul>'

def P(*ps): return ''.join(f'<p>{p}</p>' for p in ps)

# ------------------------------------------------------------------ HOME (extra)
HOME_MORE = seo_section('website-types', 'What We Build',
  'Types of Websites We Build <span class="accent">in Sri Lanka</span>',
  'Every industry has different customers and different goals. We design each website around the way your customers search, compare and buy.',
  [
   ('Business &amp; Corporate Websites', P(
     'A professional company website is the foundation of your online presence. We build corporate websites that clearly explain what you do, show your products and services, highlight past projects and make it easy for customers to call, email or send a WhatsApp message.',
     'Ideal for service providers, manufacturers, import and export companies, construction firms, consultants and B2B suppliers who need to look credible to customers and partners in Sri Lanka and overseas.')),
   ('E-Commerce &amp; Online Stores', P(
     'Online shopping in Sri Lanka keeps growing, and customers expect a store that is quick, simple and trustworthy. We build e-commerce websites with product filters, secure checkout, card payments, bank transfer and cash on delivery, plus delivery charges by district.',
     'You manage products, stock, orders and discounts from an easy dashboard, and we make sure product and category pages are optimised to appear on Google.')),
   ('Hotel, Villa &amp; Tourism Websites', P(
     'Tourism businesses compete with booking platforms that charge high commissions. A well-designed hotel or tour website with great photography, clear room and package details and a direct booking or enquiry form helps you win more direct bookings from local and foreign travellers.',
     'We design for international visitors too: fast loading around the world, clear pricing and easy contact by WhatsApp and email.')),
   ('Restaurant, Café &amp; Salon Websites', P(
     'Hungry customers want your menu, location and opening hours in seconds. We build mobile-first websites for restaurants, cafés, bakeries, salons and spas with online menus, booking or ordering options, Google Maps directions and tap-to-call buttons.',
     'Paired with a properly set-up Google Business Profile, your website helps you appear when people nearby search for what you offer.')),
   ('Real Estate &amp; Construction Websites', P(
     'Property developers, real estate agents and construction companies need to showcase projects with large images, floor plans, locations and specifications. We create project galleries and listing pages that are easy to update and that capture qualified enquiries.')),
   ('Education, Healthcare &amp; NGO Websites', P(
     'Schools, institutes, clinics, pharmacies and non-profit organisations need clear, accessible websites that people of every age can use. We build sites with course or service information, staff profiles, event and news sections, enquiry forms and donation or payment options where needed.')),
   ('How to Choose the Right Web Design Company in Sri Lanka', bullets([
     ('Look at real, live websites.', 'Open the portfolio sites on your own phone. Do they load quickly, look modern and work smoothly? Screenshots alone can hide problems.'),
     ('Ask what is included in the price.', 'Check the number of pages, hosting, SSL, domain, SEO setup, revisions and support period, so you can compare quotes fairly.'),
     ('Make sure you own your website.', 'Your domain, content and design should belong to you once the project is paid for, with full admin access.'),
     ('Check that SEO is built in.', 'Titles, meta descriptions, headings, image alt text, speed and a sitemap should be part of every website, not an expensive extra.'),
     ('Ask about support after launch.', 'Find out who updates the site, how quickly they respond and what ongoing maintenance costs.'),
   ]), True),
   ('Local SEO: Getting Found on Google in Sri Lanka', P(
     'A beautiful website only brings business if people can find it. When someone searches for a product or service "in Colombo", "near me" or "in Sri Lanka", Google looks at how relevant, trustworthy and fast your website is, and at your Google Business Profile and reviews.',
     'That is why every website we build has a clean structure, keyword-focused page titles and descriptions, structured data that tells Google who you are and where you work, fast loading on mobile data, and Google Search Console set up from day one. If you want to go further, our <a class="text-link" href="services.html#seo-marketing">SEO and digital marketing service</a> adds ongoing content, local SEO and monthly reporting.')),
   ('Mobile-First Web Design for Sri Lankan Customers', P(
     'Most Sri Lankan internet users browse on a smartphone, often on mobile data. We design every page for small screens first: readable text, large buttons, compressed images and click-to-call and WhatsApp buttons that are always within reach. Then we scale the design up for tablets and desktops, so it looks great everywhere.')),
  ], soft=True)

# ------------------------------------------------------------------ SERVICES
SVC_SEO = seo_section('why-our-services', 'Web Development Sri Lanka',
  'A Complete Web Design &amp; Web Development <span class="accent">Company in Sri Lanka</span>',
  'Design, development, hosting and marketing under one roof, so you have one team responsible for your website from the first idea to long-term growth.',
  [
   ('One Team From Design to Launch', P(
     'Many businesses in Sri Lanka end up juggling a designer, a separate developer, a hosting company and a marketing agency. When something goes wrong, nobody takes responsibility. We bring web design, web development, hosting, maintenance and SEO together, so your website is planned, built and supported by one accountable team.',
     'You get one point of contact, consistent quality and a website that keeps working long after launch day.'), True),
   ('Custom Web Development, Not Just Templates', P(
     'Templates can be a quick start, but they often load slowly, look like hundreds of other sites and are hard to extend. We design every website around your brand and write clean, efficient code. For larger projects we build custom features with modern frameworks such as Laravel and React, so your website can grow with your business.')),
   ('Platforms We Recommend', P(
     '<strong>WordPress</strong> is ideal for business websites and blogs that you want to update yourself. <strong>WooCommerce</strong> and <strong>Shopify</strong> work well for online stores of most sizes. For booking systems, portals, POS and inventory tools, we build <strong>custom web applications</strong> with Laravel, React and Node.js. We will always recommend the platform that fits your budget and goals, not the one that is easiest for us.')),
   ('Built for Speed, Security and SEO', check_list([
     'Optimised images, caching and clean code for fast loading on mobile data',
     'Free SSL, secure logins, regular updates and daily backups',
     'Search-friendly page structure, titles, meta descriptions and structured data',
     'XML sitemap, Google Analytics and Google Search Console setup',
     'Accessibility basics: readable contrast, alt text and keyboard-friendly navigation'])),
   ('Services for Every Stage of Your Business', bullets([
     ('Starting out?', 'A starter business website gets you online quickly with the essentials and a professional look.'),
     ('Growing?', 'A custom business website with a CMS, blog and SEO setup helps you win more enquiries.'),
     ('Selling online?', 'An e-commerce store with online payments, stock and delivery management lets you sell 24/7.'),
     ('Need a custom system?', 'Web applications automate bookings, orders, inventory and reporting to save your team hours every week.'),
   ])),
  ], soft=True)

SVC_FAQ = [
  ('Which web development services do you offer in Sri Lanka?', 'We offer website design, e-commerce website development, custom web applications, UI/UX design, SEO and digital marketing, and managed hosting and maintenance for businesses across Sri Lanka.'),
  ('Do you use WordPress or custom code?', 'Both. We use WordPress, WooCommerce or Shopify when you want a site that is easy to update yourself, and custom development with Laravel, React or Node.js for booking systems, portals and other web applications.'),
  ('Can you redesign my existing website?', 'Yes. We can redesign an old or slow website, keep your existing content and Google rankings where possible, and move it to faster, more secure hosting.'),
  ('Do you provide SEO after the website is launched?', 'Every website includes on-page SEO foundations. For ongoing growth we offer monthly SEO and digital marketing with content, Google Business Profile optimisation, link building and clear ranking and traffic reports.'),
  ('Can you integrate payment gateways and other systems?', 'Yes. We integrate Sri Lankan and international payment gateways, SMS and email notifications, WhatsApp, courier services, accounting tools and other third-party APIs.'),
  ('Do you work with businesses outside Sri Lanka?', 'Yes. Alongside clients across Sri Lanka, we build websites for businesses overseas, including clients in the UAE, and work fully online.'),
]

# ------------------------------------------------------------------ PACKAGES
PKG_SEO = seo_section('price-guide', 'Price Guide',
  'Web Design Sri Lanka Price Guide: <span class="accent">What You Pay For</span>',
  'A clear guide to what affects web design prices in Sri Lanka, so you can compare quotes from any web design company with confidence.',
  [
   ('What Affects the Cost of Web Design in Sri Lanka?', bullets([
     ('Number of pages.', 'A 5-page business website takes less time to design, write and build than a 20-page site with many service and location pages.'),
     ('Custom design vs template.', 'A fully custom design built around your brand takes more design time than adapting an existing layout.'),
     ('Features and functionality.', 'Online payments, booking systems, member logins, multiple languages and integrations add development time.'),
     ('Content and images.', 'Copywriting, product uploads, professional photography and video can be included or provided by you.'),
     ('SEO and marketing.', 'Basic on-page SEO is always included. Ongoing SEO, content and ads are separate monthly services.'),
   ])),
   ('Which Package Is Right for You?', P(
     '<strong>Starter (from LKR 20,000)</strong> suits new businesses, freelancers and small shops that need a professional online presence with up to 5 pages, quickly.',
     '<strong>Business (from LKR 30,000)</strong> suits established companies that want a custom design, up to 15 pages, a blog or news section and stronger SEO to win more enquiries from Google.',
     '<strong>E-Commerce (from LKR 39,000)</strong> suits brands that want to sell online with card payments, cash on delivery, stock and order management and delivery options.')),
   ('Watch Out for Hidden Costs', P(
     'Low website prices sometimes leave out essentials that you only discover later: hosting renewals at a much higher price, paid plugins, no SSL certificate, extra charges for every small change, or a website you do not fully own.',
     'With us, every quote lists exactly what is included: pages, design, hosting, SSL, SEO setup, revisions, training and the free support period. If something changes, we agree on it in writing before any work starts.')),
   ('Payment Terms &amp; Ownership', P(
     'Most projects follow a simple 50% advance and 50% on completion, and we can discuss instalments for larger projects. Once the project is paid for, the website design and content are yours, and you get full admin access to your website and domain.')),
   ('Hosting, Domains &amp; Maintenance After Year One', P(
     'Every package includes free SSL and first-year hosting. After that you can renew hosting with us or move to a provider of your choice. We can register a <strong>.lk</strong> or <strong>.com</strong> domain for you, or connect one you already own.',
     'Optional monthly maintenance plans cover backups, security and software updates, uptime monitoring and content changes, so your site stays fast and secure without you having to think about it.'), True),
  ])

PKG_EXTRA_FAQ = [
  ('Why do website prices vary so much in Sri Lanka?', 'Prices depend on how much custom design, development and content work is involved, and on what is included, such as hosting, SSL, SEO setup and support. Always compare what each quote includes, not just the headline price.'),
  ('Can I upgrade my package later?', 'Yes. Many clients start with a Starter website and add pages, a blog, online payments or custom features as the business grows.'),
]

# ------------------------------------------------------------------ PORTFOLIO
PF_SEO = seo_section('our-work', 'Our Work',
  'Web Design Projects From Sri Lanka <span class="accent">and Beyond</span>',
  'Every web design and web development project in our portfolio is a live website, built around a real business goal.',
  [
   ('Real Web Design Projects for Real Businesses', P(
     'Our portfolio covers jewellery and gem companies, fashion brands, IT and telecom suppliers, CCTV and security providers, construction companies, salons and barbers, and live market-data websites. Each one was designed from scratch around the client\'s brand, customers and goals.',
     'Open any project on your own phone. Our websites are built mobile first, so they are fast, easy to read and simple to use on small screens.'), True),
   ('E-Commerce Projects', P(
     'Online stores such as <strong>SpeedTech</strong>, <strong>CODEX Global</strong> and <strong>dooo</strong> combine strong product photography, clear categories and a smooth checkout. They are built to turn browsers into buyers and make day-to-day product and order management easy for the store owner.')),
   ('Corporate &amp; Brand Websites', P(
     'Projects like <strong>Ruvinara Gems &amp; Jewellery</strong>, <strong>Last Solution</strong>, <strong>DAG Tech Solutions</strong> and <strong>Gaura Construction</strong> present products, services and past work with a premium, trustworthy look that helps win larger clients and partners.')),
   ('Web Applications &amp; Booking Websites', P(
     'From a <strong>POS system</strong> for retail businesses to <strong>Fade &amp; Blade</strong>\'s WhatsApp booking flow and the live <strong>Gold Price Today</strong> website, we build functional web apps that automate everyday work and keep information up to date in real time.')),
   ('What Every Project Has in Common', check_list([
     'Custom design matched to the brand',
     'Mobile-first, responsive layouts',
     'Fast loading and clean, SEO-friendly code',
     'Clear calls to action: call, WhatsApp, enquire or buy',
     'Easy content management and local support'])),
  ], soft=True)

# ------------------------------------------------------------------ ABOUT
ABOUT_SEO = seo_section('our-approach', 'Our Approach',
  'How We Work With <span class="accent">Sri Lankan Businesses</span>',
  'Honest advice, clear communication and websites built to deliver results, not just to look nice.',
  [
   ('A Trusted Web Design Company in Sri Lanka', P(
     'Web Development Sri Lanka is the website design and web development studio of <strong>Applantics</strong>. We started with a simple goal: to give Sri Lankan businesses of every size access to the kind of fast, modern, professional websites usually reserved for big brands, at a fair, transparent price.',
     'Today we design and build business websites, online stores and custom web applications for clients across Sri Lanka and overseas, from small family businesses to established companies.'), True),
   ('We Start With Your Business, Not the Design', P(
     'Before we design anything, we learn how your business works: who your customers are, what they search for on Google, what makes them trust you and what you want them to do on your website. That understanding shapes every page, headline and button, so your website brings in enquiries and sales, not just compliments.')),
   ('Clear Communication at Every Step', P(
     'You always know what is happening with your project. We agree on the scope, price and timeline in writing, share designs for your feedback before development, and keep in touch by WhatsApp, phone or email. No jargon and no surprises, just regular updates and a website delivered when we said it would be.')),
   ('Long-Term Partners, Not One-Off Projects', P(
     'Launching your website is the beginning, not the end. We stay on hand for updates, new features, hosting, security and SEO, and many of our clients come back to us for their next project or recommend us to friends. Our aim is to be the web partner you can rely on for years.')),
  ])

# ------------------------------------------------------------------ CONTACT
CONTACT_SEO = seo_section('next-steps', 'What Happens Next',
  'From Enquiry to <span class="accent">Live Website</span>',
  'Getting a new website is simple. Here is what to expect after you contact us.',
  [
   ('1. Free Consultation', P(
     'We reply within 24 hours to learn about your business, your customers and your goals, by phone, WhatsApp or a short online meeting, whichever suits you.')),
   ('2. Clear, Written Quote', P(
     'You receive a written proposal with the pages, features, timeline and total price in LKR. There are no hidden fees, and nothing starts until you are happy with it.')),
   ('3. Design &amp; Development', P(
     'We design your website, share it for feedback, make revisions and then build it with fast, secure, SEO-friendly code. You can follow progress at every stage.')),
   ('4. Launch &amp; Support', P(
     'We launch your website, connect your domain, set up Google tools and show you how to update it. Free support continues after launch, with optional maintenance plans.')),
   ('Tips for a Faster Quote', bullets([
     ('Tell us about your business.', 'What you sell, who your customers are and where you operate.'),
     ('Share websites you like.', 'Links to two or three sites, even from other industries, help us understand your style.'),
     ('List the features you need.', 'For example online payments, bookings, a blog or multiple languages.'),
     ('Mention your timeline and budget.', 'This lets us recommend the right package straight away.'),
   ]), True),
  ], soft=True)
