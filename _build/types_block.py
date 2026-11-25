TYPES = [
  ('corp', 'Business &amp; Corporate Websites',
   'A professional company website is the foundation of your online presence. We build corporate websites that clearly explain what you do, show your products and services, highlight past projects and make it easy for customers to call, email or send a WhatsApp message.',
   ['Service providers', 'Manufacturers', 'Import &amp; export', 'B2B suppliers']),
  ('cart', 'E-Commerce &amp; Online Stores',
   'Online shopping in Sri Lanka keeps growing, and customers expect a store that is quick, simple and trustworthy. We build e-commerce websites with product filters, secure checkout, card payments, bank transfer and cash on delivery, plus delivery charges by district.',
   ['Fashion', 'Electronics', 'Beauty', 'Groceries']),
  ('palm', 'Hotel, Villa &amp; Tourism Websites',
   'Tourism businesses compete with booking platforms that charge high commissions. A well-designed hotel or tour website with great photography, clear room and package details and a direct booking form helps you win more direct bookings from local and foreign travellers.',
   ['Hotels', 'Villas', 'Tour operators', 'Safari &amp; travel']),
  ('fork', 'Restaurant, Café &amp; Salon Websites',
   'Hungry customers want your menu, location and opening hours in seconds. We build mobile-first websites for restaurants, cafés, bakeries, salons and spas with online menus, booking or ordering options, Google Maps directions and tap-to-call buttons.',
   ['Restaurants', 'Cafés', 'Salons', 'Spas']),
  ('hotel', 'Real Estate &amp; Construction Websites',
   'Property developers, real estate agents and construction companies need to showcase projects with large images, floor plans, locations and specifications. We create project galleries and listing pages that are easy to update and that capture qualified enquiries.',
   ['Developers', 'Real estate agents', 'Contractors', 'Architects']),
  ('edu', 'Education, Healthcare &amp; NGO Websites',
   'Schools, institutes, clinics, pharmacies and non-profit organisations need clear, accessible websites that people of every age can use. We build sites with course or service information, staff profiles, news sections, enquiry forms and donation or payment options.',
   ['Schools', 'Institutes', 'Clinics', 'NGOs']),
]
CHOOSE = [
  ('eye', 'Look at real, live websites', 'Open the portfolio sites on your own phone. Do they load quickly, look modern and work smoothly? Screenshots alone can hide problems.'),
  ('search', 'Ask what is included', 'Check pages, hosting, SSL, domain, SEO setup, revisions and support period, so you can compare quotes fairly.'),
  ('lock', 'Make sure you own it', 'Your domain, content and design should belong to you once the project is paid for, with full admin access.'),
  ('trend', 'Check SEO is built in', 'Titles, meta descriptions, headings, alt text, speed and a sitemap should be standard, not an expensive extra.'),
  ('chat', 'Ask about support', 'Find out who updates the site, how quickly they respond and what ongoing maintenance costs.'),
]

HOME_MORE = f'''<!-- ================= WEBSITE TYPES ================= -->
<section class="section wt" id="website-types">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What We Build</span>
      <h2>Types of Websites We Build <span class="accent">in Sri Lanka</span></h2>
      <p>Every industry has different customers and different goals. We design each website around the way your customers search, compare and buy.</p>
    </div>

    <div class="wt-grid">
''' + '\n'.join(f'''      <article class="wt-card">
        <div class="wt-top"><span class="wt-ic">{ic(i)}</span><span class="wt-num">0{n + 1}</span></div>
        <h3>{t}</h3>
        <p>{d}</p>
        <ul class="wt-tags">{''.join(f'<li>{x}</li>' for x in tags)}</ul>
      </article>''' for n, (i, t, d, tags) in enumerate(TYPES)) + f'''
    </div>

    <div class="wt-choose">
      <div class="wt-choose-head">
        <span class="wd-kicker light">{ic('target')}Buyer's guide</span>
        <h3>How to Choose the Right <span class="accent">Web Design Company in Sri Lanka</span></h3>
        <p>Five quick checks that help you compare web design quotes and avoid costly surprises later.</p>
      </div>
      <ol class="wt-steps">
''' + '\n'.join(f'        <li><span class="wt-step-ic">{ic(i)}</span><b>{t}</b><small>{d}</small></li>' for i, t, d in CHOOSE) + f'''
      </ol>
    </div>

    <div class="wt-duo">
      <article class="wt-feature">
        <span class="wd-kicker">{ic('search')}Local SEO</span>
        <h3>Getting Found on Google in Sri Lanka</h3>
        <p>A beautiful website only brings business if people can find it. When someone searches for a product or service "in Colombo", "near me" or "in Sri Lanka", Google looks at how relevant, trustworthy and fast your website is, and at your Google Business Profile and reviews.</p>
        <div class="wt-serp" aria-hidden="true">
          <div class="wt-serp-bar">{ic('search')}<span>web design sri lanka</span></div>
          <div class="wt-serp-res"><small>yourbusiness.lk</small><b>Your Business | Best in Sri Lanka</b><i></i><i class="s"></i></div>
        </div>
        <p>That is why every website we build has a clean structure, keyword-focused titles and descriptions, structured data that tells Google who you are and where you work, fast loading on mobile data, and Google Search Console set up from day one.</p>
        <a class="text-link" href="services.html#seo-marketing">Explore our SEO service {ARROW}</a>
      </article>
      <article class="wt-feature dark">
        <span class="wd-kicker light">{ic('mobile')}Mobile first</span>
        <h3>Mobile-First Web Design for Sri Lankan Customers</h3>
        <p>Most Sri Lankan internet users browse on a smartphone, often on mobile data. We design every page for small screens first, then scale the design up for tablets and desktops, so it looks great everywhere.</p>
        <ul class="wt-mob">
          <li>{ic('bolt')}<div><b>Compressed images</b><small>Quick to load on 4G</small></div></li>
          <li>{ic('layout')}<div><b>Readable text</b><small>No pinching or zooming</small></div></li>
          <li>{ic('phone')}<div><b>Click-to-call</b><small>One tap to reach you</small></div></li>
          <li>{ic('wa')}<div><b>WhatsApp button</b><small>Always within reach</small></div></li>
        </ul>
        <div class="wt-test">
          <b>Tested before every launch</b>
          <ul>
            <li>{ic('check')}Real Android &amp; iPhone devices</li>
            <li>{ic('check')}Google PageSpeed on mobile</li>
            <li>{ic('check')}Mobile-friendly layouts at every size</li>
            <li>{ic('check')}Forms, calls &amp; WhatsApp links</li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>
'''
