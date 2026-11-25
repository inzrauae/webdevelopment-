# More blog posts (topic cluster). Executed inside blog.py after POSTS is defined.
POSTS += [
 dict(slug='why-your-business-needs-a-website', img_alt='Business team reviewing plans and reports together', eyebrow='Business Growth',
  title='Why Your Business Needs a Website in Sri Lanka (Not Just a Facebook Page)',
  h1='Why Your Business Needs a <span class="accent">Website</span>',
  desc='Why does a Sri Lankan business need a website when it already has Facebook? 9 reasons a professional website brings more customers, trust and Google visibility.',
  intro='Many Sri Lankan businesses rely only on Facebook, Instagram or WhatsApp. Social media is useful, but a professional website gives you things social platforms cannot. Here is why a website is still the foundation of your online presence.',
  key=['Customers search on Google before they buy, and a website is how you appear there.',
       'You own your website. You do not own your Facebook page or its reach.',
       'A website builds trust with a professional look, reviews and clear information.',
       'Use social media to bring people to your website, not to replace it.'],
  secs=[
   ('search', '1. Customers Search Google Before They Buy', P(
     'When people need a service, such as a builder in Kandy, a jeweller in Colombo or a hotel in Galle, most of them start with a Google search. If you do not have a website, you are mostly invisible in those results, and the enquiry goes to a competitor who does.',
     'A website with the right pages and keywords can appear for searches about your services, location and products every day, without paying for each click. Our guide on <a href="seo-for-small-businesses-sri-lanka.html">SEO for small businesses in Sri Lanka</a> explains how.')),
   ('own', '2. You Own Your Website', P(
     'Your Facebook page belongs to Facebook. Rules change, reach drops, and accounts can be hacked or restricted without warning. Your website and domain belong to you. You control the design, the content and how customers contact you, and nobody can take it away.')),
   ('trust', '3. A Website Builds Trust', P(
     'Customers check whether a business is real and reliable before they pay. A professional website with your address, phone number, real photos, past projects and reviews instantly makes a business look established. Many larger companies and foreign clients will not work with a business that has no website or business email.')),
   ('open', '4. It Works 24 Hours a Day', P(
     'Your website answers questions, shows prices and takes enquiries while you sleep. Customers can read about your services at midnight and send a WhatsApp message or booking request, ready for you in the morning.') + MID_CTA),
   ('compare', 'Website vs Social Media Page', table(
     ['', 'Website', 'Facebook / Instagram page'], [
      ['Appears on Google searches', 'Yes, for many keywords', 'Rarely, mainly for your business name'],
      ['Ownership', 'You own it', 'Owned by the platform'],
      ['Design and branding', 'Fully custom', 'Fixed layout'],
      ['Online payments and bookings', 'Yes', 'Limited'],
      ['Professional email address', 'Yes (you@yourbusiness.lk)', 'No'],
      ['Visitor statistics', 'Full analytics', 'Limited insights']])),
   ('sell', '5. Sell Online and Take Bookings', P(
     'With an online store or booking system, customers can buy or book without calling you. That saves time for your staff and captures sales you would otherwise miss. Read our guide to building an <a href="ecommerce-website-sri-lanka.html">e-commerce website in Sri Lanka</a>, or see how custom systems work in our <a href="web-development-sri-lanka.html">web development guide</a>.')),
   ('more', 'More Reasons a Website Pays for Itself', ul([
     '<strong>Answer common questions</strong> with FAQ pages, so you spend less time on the phone.',
     '<strong>Show your work</strong> with a portfolio or project gallery.',
     '<strong>Advertise better:</strong> Google and Facebook ads perform better when they lead to a focused landing page.',
     '<strong>Reach foreign customers</strong> in tourism, exports and services.',
     '<strong>Measure results</strong> with Google Analytics and Search Console.'])),
   ('start', 'How to Get Started', P(
     'You do not need a big budget. A professional starter website with up to 5 pages costs from LKR 20,000 with us, including hosting, SSL and SEO setup. Read <a href="website-cost-in-sri-lanka.html">how much a website costs in Sri Lanka</a>, then compare your options using our <a href="how-to-choose-a-web-design-company-sri-lanka.html">checklist for choosing a web design company</a>.') +
     tip('Keep your social pages active and link them to your website. Social media brings attention; your website turns that attention into customers.')),
  ],
  faqs=[('Does a small business in Sri Lanka really need a website?', 'Yes. Most customers search on Google before buying, and a website lets you appear in those results, look professional, and take enquiries, bookings or orders at any time.'),
        ('Is a Facebook page enough for my business?', 'A Facebook page is useful, but it rarely ranks on Google for your services, you do not own it, and its design and features are limited. It works best alongside a website.'),
        ('How much does a basic business website cost?', 'With Web Development Sri Lanka, a starter business website with up to 5 pages costs LKR 20,000, including SSL, first-year hosting and SEO setup.')],
  rel=['website-cost-in-sri-lanka', 'seo-for-small-businesses-sri-lanka', 'how-to-choose-a-web-design-company-sri-lanka']),

 dict(slug='wordpress-vs-custom-website', img_alt='Computer and laptop in a website publishing workspace', eyebrow='Comparison',
  title='WordPress vs Custom Website: Which Is Right for Your Business?',
  h1='WordPress vs <span class="accent">Custom Website</span>',
  desc='WordPress vs a custom-coded website: compare cost, speed, security, SEO and ease of updates to choose the right type of website for your Sri Lankan business.',
  intro='One of the first decisions in any website project is whether to build on WordPress or create a custom-coded website. Both are good choices for different needs. This guide compares them honestly so you can choose with confidence.',
  key=['WordPress is ideal when you want to update content and blog often.',
       'Custom code is ideal for top speed, unique features and web applications.',
       'Both can rank well on Google when built properly.',
       'Choose based on your goals, budget and who will update the site.'],
  secs=[
   ('what', 'What Is the Difference?', P(
     '<strong>WordPress</strong> is a content management system (CMS) that powers a large share of the world\'s websites. You get an admin panel where you can edit pages, add blog posts and upload photos without coding. Its look comes from a theme, and extra features come from plugins.',
     'A <strong>custom website</strong> is coded from scratch, usually with HTML, CSS and JavaScript, and a framework or backend when needed. Every part is built only for your project, with no unnecessary code.')),
   ('table', 'Side-by-Side Comparison', table(
     ['Factor', 'WordPress', 'Custom website'], [
      ['Ease of updates', 'Very easy admin panel', 'Simple sites may need a developer, unless a CMS is added'],
      ['Speed', 'Good, if well optimised', 'Excellent, as there is no extra code'],
      ['Security', 'Needs regular plugin and core updates', 'Smaller attack surface'],
      ['Unique features', 'Limited by plugins', 'Anything you need'],
      ['Blogging', 'Excellent', 'Possible, but needs to be built'],
      ['Online store', 'WooCommerce works well', 'Best for complex or high-volume stores'],
      ['Maintenance', 'Regular updates required', 'Low for static sites']])),
   ('choose-wp', 'When to Choose WordPress', ul([
     'You want to add blog posts, news or products regularly yourself.',
     'Several staff members need to edit content.',
     'You need a standard online store, and WooCommerce covers your needs.',
     'You want many proven plugins, such as booking forms or multi-language support.']) + MID_CTA),
   ('choose-custom', 'When to Choose a Custom Website', ul([
     'Speed and Google PageSpeed scores are a top priority.',
     'You need a unique design or features that plugins cannot provide.',
     'You are building a web application, such as a POS, booking system or customer portal.',
     'You want minimal maintenance and fewer security updates.']) + P(
     'Custom systems are covered in more detail in our guide to <a href="web-development-sri-lanka.html">web development in Sri Lanka</a>.')),
   ('seo', 'Which Is Better for SEO?', P(
     'Google does not prefer one platform over the other. What matters is page speed, mobile-friendliness, clean structure, helpful content and links from other websites. A well-built WordPress site and a well-built custom site can both rank at the top. A badly built site of either type will struggle. Learn the basics in our <a href="seo-for-small-businesses-sri-lanka.html">SEO guide for small businesses</a>.')),
   ('cost', 'Cost Comparison', P(
     'For a typical business website, both options fit into our standard packages, starting at LKR 20,000. Complex custom features and web applications are quoted separately. Remember to include yearly costs such as hosting, domain renewal and, for WordPress, plugin licences and updates. See our full <a href="website-cost-in-sri-lanka.html">website cost guide</a>.') +
     tip('Not sure? Tell us how often you will update the site and which features you need. We will recommend the option that fits, not the most expensive one.')),
  ],
  faqs=[('Is WordPress good for business websites?', 'Yes. WordPress is a strong choice for business websites that need regular content updates, blogs or standard online stores, as long as it is kept updated and well optimised.'),
        ('Is a custom website faster than WordPress?', 'Usually, yes. A custom website includes only the code it needs, so it often loads faster. A carefully optimised WordPress site can also be fast.'),
        ('Can I update a custom website myself?', 'Yes, if it is built with a content management system or admin panel. Ask your developer which parts you will be able to edit.')],
  rel=['how-to-create-a-web-design', 'web-development-sri-lanka', 'website-cost-in-sri-lanka']),

 dict(slug='ecommerce-website-sri-lanka', img_alt='Customer making a mobile payment at a shop checkout', eyebrow='E-Commerce',
  title='E-Commerce Website in Sri Lanka: Payments, Delivery &amp; Setup Guide',
  h1='E-Commerce Website <span class="accent">in Sri Lanka</span>',
  desc='How to start an e-commerce website in Sri Lanka: online payment options, cash on delivery, courier delivery, product pages, costs and tips to get more online orders.',
  intro='Selling online in Sri Lanka keeps growing, from fashion and electronics to groceries and gifts. This guide explains what a successful Sri Lankan online store needs: payment options, delivery, product pages, marketing and costs.',
  key=['Offer the payment options Sri Lankans trust: cards, bank transfer and cash on delivery.',
       'Show delivery charges and times clearly, by district.',
       'Great photos and clear prices sell more than fancy design.',
       'Our e-commerce package starts at LKR 39,000.'],
  secs=[
   ('plan', 'Plan Your Online Store', P(
     'Before building, decide what you will sell, how many products you have, who your customers are and how you will deliver. List your categories, prepare product photos and descriptions, and decide your delivery charges. Good planning makes the build faster and the store easier to use.')),
   ('payments', 'Payment Options for Sri Lankan Customers', P(
     'Customers buy more when they can pay the way they prefer. Most Sri Lankan online stores offer a mix of:') + ul([
     '<strong>Card payments</strong> through a local payment gateway or a bank\'s internet payment gateway.',
     '<strong>Bank transfer</strong>, where the customer uploads a payment slip.',
     '<strong>Cash on delivery (COD)</strong>, which many first-time buyers still prefer.',
     '<strong>International payments</strong> if you sell to customers overseas.']) +
     tip('Payment gateways need your business registration and bank details. Start the application early, as approval can take some time.')),
   ('delivery', 'Delivery and Shipping', P(
     'Most stores work with local courier services for island-wide delivery. Set clear delivery charges, for example a lower rate inside Colombo and a different rate for other districts, and show estimated delivery times on product and checkout pages. Unclear delivery costs are one of the main reasons customers abandon their cart.') + MID_CTA),
   ('features', 'Must-Have Features of an Online Store', table(
     ['Feature', 'Why it matters'], [
      ['Fast, mobile-friendly design', 'Most shoppers buy on their phones'],
      ['Product search and filters', 'Customers find products quickly'],
      ['High-quality product photos', 'They replace seeing the product in a shop'],
      ['Clear prices, stock and variants', 'Sizes, colours and availability at a glance'],
      ['Simple checkout', 'Fewer steps mean fewer abandoned carts'],
      ['Order emails and WhatsApp updates', 'Customers know what is happening'],
      ['Admin panel', 'Manage products, orders and stock yourself'],
      ['Reviews', 'Social proof increases sales']])),
   ('product-pages', 'How to Write Product Pages That Sell', ol([
     'Use a clear product name with the main keyword people search for.',
     'Show several photos from different angles, plus a photo in use.',
     'List key details: size, material, warranty and what is in the box.',
     'Show the price, delivery charge and delivery time clearly.',
     'Add an "Order on WhatsApp" button for customers who prefer to chat.'])),
   ('platform', 'Which Platform Should You Use?', P(
     'For most small and medium stores, WooCommerce on WordPress is flexible and affordable. Larger stores with many products, complex stock management or integrations with POS and accounting systems may need a custom build. Compare both in our <a href="wordpress-vs-custom-website.html">WordPress vs custom website guide</a>. If you also sell in a physical shop, a connected <a href="web-development-sri-lanka.html">POS and inventory system</a> keeps online and in-store stock in sync.')),
   ('marketing', 'Getting Your First Orders', ul([
     'Optimise product and category pages for Google searches.',
     'Share products on Facebook, Instagram and TikTok with links to your store.',
     'Run small, targeted ads to your best-selling products.',
     'Encourage reviews and repeat orders with discount codes.',
     'Read our <a href="seo-for-small-businesses-sri-lanka.html">SEO guide</a> to get free traffic from Google.'])),
   ('cost', 'How Much Does an E-Commerce Website Cost?', P(
     'Our e-commerce website package starts at <strong>LKR 39,000</strong>, including product pages, cart and checkout, payment setup, SSL and first-year hosting. Large catalogues and custom integrations are quoted separately. See the <a href="packages.html">web design Sri Lanka price list</a> and our <a href="website-cost-in-sri-lanka.html">website cost guide</a> for details.')),
  ],
  faqs=[('How much does an e-commerce website cost in Sri Lanka?', 'With Web Development Sri Lanka, an e-commerce website starts at LKR 39,000, including cart, checkout, payment setup, SSL and first-year hosting.'),
        ('Can I accept card payments on my website in Sri Lanka?', 'Yes. You can connect a local payment gateway or your bank\'s internet payment gateway to accept Visa and Mastercard. You will need business registration and bank details to apply.'),
        ('Should I offer cash on delivery?', 'In Sri Lanka, cash on delivery is still popular, especially with first-time customers. Offering it alongside card and bank transfer usually increases orders.'),
        ('Can I manage products and orders myself?', 'Yes. Our online stores include an admin panel where you can add products, change prices, manage stock and process orders.')],
  rel=['website-cost-in-sri-lanka', 'wordpress-vs-custom-website', 'seo-for-small-businesses-sri-lanka']),

 dict(slug='seo-for-small-businesses-sri-lanka', img_alt='Analytics dashboard displaying website performance charts', eyebrow='SEO Guide',
  title='SEO for Small Businesses in Sri Lanka: A Practical Guide to Rank on Google',
  h1='SEO for Small Businesses <span class="accent">in Sri Lanka</span>',
  desc='A practical SEO guide for small businesses in Sri Lanka: keyword research, on-page SEO, Google Business Profile, reviews, links, speed and how long it takes to rank.',
  intro='SEO (search engine optimisation) helps your website appear on Google when customers search for what you sell. You do not need a big budget to start. This guide explains the steps that make the biggest difference for small Sri Lankan businesses.',
  key=['Target the exact words customers type, including your town or "Sri Lanka".',
       'Give every page a clear title, one H1 and helpful content.',
       'A Google Business Profile with reviews is essential for local searches.',
       'SEO takes months, not days, but the traffic is free and lasts.'],
  secs=[
   ('what', 'What Is SEO and Why Does It Matter?', P(
     'When someone searches "wedding photographer Kandy" or "web design Sri Lanka", Google shows the pages it thinks are the most relevant and trustworthy. SEO is the work of making your website one of those pages. Unlike ads, you do not pay for each click, so a well-ranked page keeps bringing customers for months or years.')),
   ('keywords', 'Step 1: Find the Right Keywords', P(
     'Keywords are the words your customers type into Google. Write down how customers describe your products and services, then add locations, for example "hotel in Ella", "solar panels Colombo" or "web design company Sri Lanka". Tools such as Google Search Console, Google\'s autocomplete and keyword tools show what people really search for and how often.') +
     tip('Start with specific, lower-competition keywords such as "[service] in [town]". They are easier to rank for and bring customers who are ready to buy.')),
   ('onpage', 'Step 2: On-Page SEO Basics', table(
     ['Element', 'What to do'], [
      ['Page title', 'Include the main keyword near the start; keep it under about 60 characters'],
      ['Meta description', 'Summarise the page and give a reason to click'],
      ['H1 heading', 'One per page, containing the main keyword'],
      ['Subheadings (H2, H3)', 'Break content into clear sections using related keywords'],
      ['Content', 'Answer customer questions in detail, in plain language'],
      ['Images', 'Compress them and add descriptive alt text'],
      ['Internal links', 'Link related pages together with descriptive anchor text'],
      ['URL', 'Short and readable, for example /services or /packages']])),
   ('gbp', 'Step 3: Set Up Your Google Business Profile', P(
     'For local searches, your free <strong>Google Business Profile</strong> is just as important as your website. It puts your business on Google Maps and in the local results. Choose the correct category, add your phone number, website, opening hours, services and photos, and keep the name, address and phone number identical to your website.') + MID_CTA),
   ('reviews', 'Step 4: Collect Reviews', P(
     'Reviews help you rank in local results and convince people to choose you. After every successful job, send happy customers a direct link to leave a Google review. Reply to every review, positive or negative, politely and professionally.')),
   ('speed', 'Step 5: Make Your Website Fast and Mobile-Friendly', P(
     'Google ranks websites based on their mobile version. Check your site with Google PageSpeed Insights, compress large images, avoid heavy sliders and make sure text and buttons are easy to use on a phone. A <a href="how-to-create-a-web-design.html">well-planned web design</a> makes this much easier.')),
   ('links', 'Step 6: Earn Links From Other Websites', P('Links from other trustworthy websites tell Google your business is real and respected. Good sources for small businesses include:') + ul([
     'Business directories and local listings with consistent details.',
     'Suppliers, partners and industry associations.',
     'Local news sites and blogs that feature your business or events.',
     'Guest articles on websites in your industry.',
     'Social profiles such as LinkedIn, Facebook and Instagram.'])),
   ('content', 'Step 7: Publish Helpful Content', P(
     'Blog posts and guides that answer your customers\' questions attract visitors who are researching before they buy. Write about prices, comparisons, how-to topics and common problems in your industry, and link each article to your service pages. This blog is an example: our guides, such as <a href="website-cost-in-sri-lanka.html">how much a website costs in Sri Lanka</a>, link to the pages we want to rank.')),
   ('timeline', 'How Long Does SEO Take?', P(
     'For a new website, low-competition keywords can start ranking within a few weeks to 3 months. Competitive keywords usually take 4 to 12 months of steady content, reviews and links. Track your progress in Google Search Console and keep improving pages that are close to the first page.')),
  ],
  faqs=[('How long does SEO take for a small business?', 'Easier local keywords can rank within a few weeks to 3 months. Competitive keywords usually take 4 to 12 months of consistent work on content, reviews and links.'),
        ('Can I do SEO myself?', 'Yes. Small businesses can handle the basics: keyword-focused page titles, helpful content, a Google Business Profile and collecting reviews. Technical SEO and link building often benefit from expert help.'),
        ('Is SEO included with your websites?', 'Yes. Every website we build includes on-page SEO setup: titles, meta descriptions, headings, alt text, structured data, a sitemap and Google Search Console.'),
        ('What is local SEO?', 'Local SEO helps your business appear in Google Maps and local searches such as "near me" or "in Colombo", mainly through your Google Business Profile, reviews and location-focused pages.')],
  rel=['why-your-business-needs-a-website', 'best-website-design-examples', 'hotel-website-design-sri-lanka']),

 dict(slug='hotel-website-design-sri-lanka', img_alt='Hotel swimming pool and illuminated resort buildings at dusk', eyebrow='Tourism',
  title='Hotel &amp; Villa Website Design in Sri Lanka: Get More Direct Bookings',
  h1='Hotel &amp; Villa Website Design <span class="accent">in Sri Lanka</span>',
  desc='Hotel and villa website design in Sri Lanka: the features, photos, booking options and SEO that help hotels, villas and tour operators win more direct bookings.',
  intro='Booking platforms bring guests, but they also take a commission on every booking. A well-designed hotel or villa website helps you win more direct bookings from local and foreign travellers. Here is what the best tourism websites in Sri Lanka include.',
  key=['Direct bookings through your own website save commission.',
       'Professional photos are the most important part of a hotel website.',
       'Make booking or enquiring possible in a few taps on a phone.',
       'Target searches such as "boutique hotel in Ella" or "villa in Galle".'],
  secs=[
   ('why', 'Why Your Hotel Needs Its Own Website', P(
     'Travellers often find a hotel on a booking platform, then search for its name on Google to see more photos and check for a better deal. If your own website looks professional and makes booking easy, many of those guests will book directly with you, saving you commission and giving you their contact details for future stays.')),
   ('photos', 'Great Photos Sell Rooms', P(
     'Guests book with their eyes. Invest in professional photography of every room type, the view, the pool, the restaurant and the surroundings. Use large, high-quality images that are compressed for fast loading. A short video tour adds even more confidence.') +
     tip('Show real photos of the actual rooms. Guests leave bad reviews when a room does not match the pictures.')),
   ('features', 'Must-Have Features for Hotel Websites', table(
     ['Feature', 'Why it matters'], [
      ['Room pages with photos and prices', 'Guests compare options quickly'],
      ['Booking form or booking engine', 'Turn visitors into direct bookings'],
      ['WhatsApp and click-to-call', 'Foreign and local guests can ask questions instantly'],
      ['Location map and directions', 'Shows how to reach you from the airport, station or highway'],
      ['Reviews and awards', 'Builds trust with first-time guests'],
      ['Things to do nearby', 'Helps guests plan, and helps your SEO'],
      ['Special offers', 'Gives a reason to book direct'],
      ['Fast mobile design', 'Most travellers browse on their phones']]) + MID_CTA),
   ('booking', 'Booking Options: Form, Engine or WhatsApp?', ul([
     '<strong>Enquiry form:</strong> the simplest option. Guests send dates and you confirm by email or WhatsApp.',
     '<strong>Booking engine:</strong> guests see live availability and pay online. Best for hotels with many rooms.',
     '<strong>WhatsApp booking:</strong> very popular in Sri Lanka and with many foreign guests for quick questions.']) + P(
     'Many properties combine an enquiry form with a WhatsApp button. Larger hotels can use a custom booking system, explained in our <a href="web-development-sri-lanka.html">web development guide</a>.')),
   ('seo', 'SEO for Hotels and Villas', P(
     'Create pages that match what travellers search: your town, nearby attractions and type of stay, for example "boutique hotel in Kandy", "beach villa in Mirissa" or "safari lodge near Yala". Add a Google Business Profile, collect reviews and write helpful guides about your area. Our <a href="seo-for-small-businesses-sri-lanka.html">SEO guide for small businesses</a> covers the full process.')),
   ('tours', 'Websites for Tour Operators and Travel Agents', P(
     'Tour operators need clear itinerary pages with day-by-day plans, maps, prices per person and an easy enquiry form. Testimonials from past travellers, photos from real tours and a fast WhatsApp contact button are what convince foreign visitors to book. You can see examples in our <a href="portfolio.html">web design portfolio</a>, including Island Tours Ceylon, Lanka Tour Driver, TukTuk Ceylon Rides and FLY SE.')),
   ('cost', 'Cost of a Hotel Website', P(
     'Most hotel and villa websites fit our business website package from <strong>LKR 30,000</strong>, which includes a CMS so you can update rooms and offers yourself. Websites with online payments or a booking engine are quoted based on your needs. See our <a href="packages.html">website packages</a> and the <a href="best-website-design-examples.html">best website design examples</a> for inspiration.')),
  ],
  faqs=[('How can a website increase direct hotel bookings?', 'A professional website with great photos, clear room information, special offers for booking direct and an easy booking form or WhatsApp button encourages guests to book with you instead of through a booking platform.'),
        ('Do I need a booking engine on my hotel website?', 'Not always. Small villas and guesthouses often do well with an enquiry form and WhatsApp. Hotels with many rooms benefit from a booking engine that shows live availability.'),
        ('How much does a hotel website cost in Sri Lanka?', 'Most hotel and villa websites fit our business website package from LKR 30,000. Online payments and booking engines are quoted based on your requirements.')],
  rel=['best-website-design-examples', 'seo-for-small-businesses-sri-lanka', 'why-your-business-needs-a-website']),

 dict(slug='web-development-sri-lanka', img_alt='Laptop showing source code in a development workspace', eyebrow='Web Development',
  title='Web Development in Sri Lanka: Custom Web Apps, POS &amp; Booking Systems',
  h1='Web Development <span class="accent">in Sri Lanka</span>',
  desc='A guide to web development in Sri Lanka: custom web applications, POS and inventory systems, booking systems, customer portals, how projects work and what they cost.',
  intro='Web development goes beyond a standard website. Custom web applications can automate your sales, bookings, stock and customer service. This guide explains what web development can do for your business and how a project works from idea to launch.',
  key=['Web development builds working systems, not just pages.',
       'Common projects include POS, inventory, booking systems and customer portals.',
       'Web apps run in a browser, so staff can use them on any device.',
       'Start with the most important features, then grow in phases.'],
  secs=[
   ('what', 'What Is Web Development?', P(
     'Web development is the work of building the code behind websites and web applications. <strong>Front-end development</strong> creates what users see and interact with. <strong>Back-end development</strong> handles databases, user accounts, payments and business logic on the server. For the difference from design, read <a href="what-is-web-designing.html">what web designing is</a>.')),
   ('types', 'Types of Web Applications We Build', table(
     ['Application', 'What it does', 'Good for'], [
      ['POS &amp; inventory system', 'Sales, billing, stock and reports', 'Shops, pharmacies, hardware stores'],
      ['Booking system', 'Appointments, rooms or tours with availability', 'Salons, clinics, hotels, tour operators'],
      ['Customer portal', 'Customers log in to see orders, invoices or progress', 'Service companies, B2B suppliers'],
      ['Admin dashboard', 'Manage data, staff and reports in one place', 'Growing businesses of all types'],
      ['E-commerce platform', 'Large stores with custom features and integrations', 'Retail and wholesale'],
      ['SaaS product', 'Software sold as a subscription', 'Startups and tech companies']])),
   ('benefits', 'Why Choose a Web App Over Desktop Software?', ul([
     '<strong>Works anywhere:</strong> use it on a laptop, tablet or phone through a browser.',
     '<strong>No installation:</strong> updates appear for everyone instantly.',
     '<strong>Multiple branches:</strong> see data from every location in real time.',
     '<strong>Secure backups:</strong> data is stored on the server, not on one computer.',
     '<strong>Grows with you:</strong> add features and users as the business grows.']) + MID_CTA),
   ('process', 'How a Web Development Project Works', ol([
     '<strong>Discovery:</strong> we learn how your business works today and what needs to improve.',
     '<strong>Requirements:</strong> a written list of features, users and reports.',
     '<strong>Design:</strong> screens are designed and approved before coding starts.',
     '<strong>Development in phases:</strong> the most important features are built first.',
     '<strong>Testing:</strong> with real data and real staff.',
     '<strong>Launch and training:</strong> your team learns to use the system.',
     '<strong>Support:</strong> fixes, improvements and new features over time.'])),
   ('integrations', 'Integrations That Save Time', P(
     'Web applications become even more useful when they connect to the tools you already use: payment gateways, SMS and WhatsApp notifications, email, accounting software, barcode scanners and receipt printers. Automating these steps removes manual work and reduces mistakes.')),
   ('mvp', 'Start Small, Then Grow', P(
     'You do not need to build everything at once. Start with a <strong>minimum viable product (MVP)</strong> that solves your biggest problem, use it with real customers or staff, then add features based on feedback. This keeps the first cost lower and makes sure every feature is useful.') +
     tip('Write down the three tasks that waste the most time in your business each week. Those are usually the best features to build first.')),
   ('website-or-app', 'Do You Need a Website or a Web App?', P(
     'If you mainly need to present your business and get enquiries, a standard website is enough. Compare the options in our <a href="wordpress-vs-custom-website.html">WordPress vs custom website guide</a>. If you need staff or customers to log in, manage data, make bookings or process sales, you need a web application.')),
   ('cost', 'How Much Does Web Development Cost?', P(
     'Custom web applications are priced based on the features, number of user types, integrations and timeline. After a short discovery call, we provide a fixed quote with a clear scope, often split into phases. Standard websites start from LKR 20,000. See our <a href="packages.html">packages</a> and our <a href="portfolio.html">portfolio</a>, which includes a POS system and booking solutions.')),
  ],
  faqs=[('What is the difference between a website and a web application?', 'A website mainly presents information. A web application lets users log in and do tasks, such as booking appointments, processing sales, managing stock or viewing invoices.'),
        ('How long does it take to build a web application?', 'A focused first version usually takes 4 to 12 weeks, depending on the features. Larger systems are built and released in phases.'),
        ('Can a web-based POS system work on a tablet?', 'Yes. Web-based POS systems run in a browser, so they work on computers, tablets and phones, and can connect to barcode scanners and receipt printers.'),
        ('Who owns the source code?', 'Ownership is agreed in writing before the project starts. For custom projects, the client usually owns the code and data once the project is paid for.')],
  rel=['wordpress-vs-custom-website', 'ecommerce-website-sri-lanka', 'how-to-choose-a-web-design-company-sri-lanka']),
]

# Topic-based "Keep reading" for the original posts
REL = {
  'what-is-web-designing': ['how-to-start-web-designing', 'how-to-create-a-web-design', 'why-your-business-needs-a-website'],
  'how-to-start-web-designing': ['what-is-web-designing', 'how-to-create-a-web-design', 'wordpress-vs-custom-website'],
  'how-to-create-a-web-design': ['best-website-design-examples', 'wordpress-vs-custom-website', 'how-to-start-web-designing'],
  'best-website-design-examples': ['hotel-website-design-sri-lanka', 'how-to-create-a-web-design', 'ecommerce-website-sri-lanka'],
  'how-to-choose-a-web-design-company-sri-lanka': ['website-cost-in-sri-lanka', 'why-your-business-needs-a-website', 'web-development-sri-lanka'],
  'website-cost-in-sri-lanka': ['how-to-choose-a-web-design-company-sri-lanka', 'ecommerce-website-sri-lanka', 'wordpress-vs-custom-website'],
}
for _p in POSTS:
    if _p['slug'] in REL: _p['rel'] = REL[_p['slug']]
