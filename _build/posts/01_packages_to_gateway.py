# Scheduled posts, batch 1 (25 to 29 November 2026). Executed inside blog.py.
POSTS += [
 dict(slug='web-design-packages-sri-lanka', date='2026-11-25', cover='speedtech', img_alt='Web design packages in Sri Lanka compared on desktop and mobile', eyebrow='Pricing Guide',
  title='Web Design Packages in Sri Lanka: What You Get at Each Price',
  h1='Web Design Packages in Sri Lanka: <span class="accent">What You Get</span>',
  desc='Compare web design packages in Sri Lanka: what a starter, business and e-commerce package includes, what costs extra, and how to choose the right one.',
  intro='Web design packages in Sri Lanka range from cheap template sites to large custom projects, and the names rarely tell you what is actually included. This guide explains what you should expect at each level, what is often left out, and how to pick a package that fits your business today and can grow with it.',
  key=['A package should list pages, features, hosting, SSL, SEO setup and support in writing.',
       'Starter packages suit new businesses that need a professional presence fast.',
       'Business packages add a CMS, blog and more pages so you can grow on Google.',
       'E-commerce packages add products, payments, delivery and order management.'],
  secs=[
   ('why', 'Why Packages Make Website Pricing Easier', P(
     'A custom quote for every website takes time and makes it hard to compare offers. Packages solve that by grouping the most common needs into fixed prices. You know the cost before you start, the designer knows the scope, and both sides avoid surprises at the end of the project.',
     'The catch is that two packages with the same name can be very different. One company’s “business website” might be five template pages with no SEO, while another includes a content management system, a blog, analytics and on-page SEO for every page. Always compare what is inside the package, not the label on it.',
     'If you are still working out your budget, start with our detailed guide to <a href="website-cost-in-sri-lanka.html">how much a website costs in Sri Lanka</a>, then come back here to match a package to your goals.')),
   ('starter', 'Starter Package: A Professional Online Presence', P(
     'A starter package is for businesses that need to look credible online quickly: a new shop, a consultant, a tuition class, a small service company or a business that only has a Facebook page today. It usually covers up to five pages, such as Home, About, Services, Gallery and Contact.',
     'Even at this level, the website should be mobile-friendly, load fast, use your own domain name and include a free SSL certificate so browsers show it as secure. Basic on-page SEO, a contact form, a WhatsApp button and Google Maps on the contact page should be standard.') + ul([
     '<strong>Best for:</strong> new and small businesses, freelancers, local services.',
     '<strong>Typical timeline:</strong> one to two weeks once your content is ready.',
     '<strong>Our price:</strong> from LKR 20,000, including SSL, first-year hosting and SEO setup.'])),
   ('business', 'Business Package: Built to Grow on Google', P(
     'A business package is the right choice when your website needs to win customers through search, not just exist. It usually allows more pages, so each service gets its own page that can rank for its own keywords, and it adds a content management system (CMS) so you can update text, photos and blog posts yourself.',
     'This is where a website starts working as a sales tool. Separate service pages, a blog, customer reviews, a portfolio and clear calls to action give Google more reasons to show your site and give visitors more reasons to contact you. Our guide on <a href="seo-for-small-businesses-sri-lanka.html">SEO for small businesses in Sri Lanka</a> explains why this structure matters.') + ul([
     '<strong>Best for:</strong> established companies, professional services, hotels, schools, builders.',
     '<strong>Typical timeline:</strong> three to four weeks.',
     '<strong>Our price:</strong> from LKR 30,000 with a CMS, blog and up to 15 pages.'])),
   ('ecommerce', 'E-Commerce Package: Sell Online', P(
     'An e-commerce package turns your website into a shop. It adds product pages with photos and variations such as size and colour, a cart and checkout, online card payments, cash on delivery, delivery charges by area, stock control and order emails.',
     'The details matter more here than anywhere else. Ask which payment gateway is included, whether you can add products yourself, how delivery fees are calculated and whether customers can track orders. Our full guide to building an <a href="ecommerce-website-sri-lanka.html">e-commerce website in Sri Lanka</a> covers each of these decisions.') + ul([
     '<strong>Best for:</strong> retail shops, fashion brands, electronics, gifts, food producers.',
     '<strong>Typical timeline:</strong> four to six weeks.',
     '<strong>Our price:</strong> from LKR 39,000, with payment gateway and delivery setup.']) + fig('speedtech', 'An online store we built for SpeedTech IT Solutions, with products, categories and enquiries')),
   ('compare', 'Package Comparison at a Glance', table(
     ['Feature', 'Starter', 'Business', 'E-commerce'], [
      ['Pages', 'Up to 5', 'Up to 15', 'Unlimited products'],
      ['Mobile-friendly design', 'Yes', 'Yes', 'Yes'],
      ['Content management system', 'Optional', 'Yes', 'Yes'],
      ['Blog', 'No', 'Yes', 'Yes'],
      ['On-page SEO', 'Basic', 'Every page', 'Every page and product'],
      ['Online payments', 'No', 'No', 'Yes'],
      ['Free SSL and first-year hosting', 'Yes', 'Yes', 'Yes'],
      ['Starting price', 'LKR 20,000', 'LKR 30,000', 'LKR 39,000']]) + MID_CTA),
   ('extras', 'What Is Usually Not Included', P(
     'Most disagreements about website prices come from things that were never written down. Before you sign, check how each of these is handled:') + ul([
     '<strong>Domain renewal and hosting after the first year.</strong> These are yearly costs you will pay for as long as the site is live.',
     '<strong>Content writing and photography.</strong> Many packages assume you supply the text and images.',
     '<strong>Logo and brand design.</strong> Often a separate service.',
     '<strong>Extra revisions</strong> beyond the agreed rounds of changes.',
     '<strong>Ongoing SEO and ads.</strong> Setup is not the same as monthly optimisation.',
     '<strong>Maintenance</strong> such as updates, backups and content changes after launch.']) + tip('Ask for a one-page summary of what is included and what costs extra. A good web design company will give you this without hesitation.')),
   ('choose', 'How to Choose the Right Package', P(
     'Start with the goal, not the price. If you simply need customers to find your phone number and see that you are real, a starter package is enough. If you want enquiries from Google every week, choose a business package and plan to publish content. If you want people to pay online, you need an e-commerce package.',
     'Next, think about the next 12 months. Will you add services, open a branch or start selling online? A package that allows upgrades without rebuilding the site will save money later. Finally, compare the companies themselves using our checklist on <a href="how-to-choose-a-web-design-company-sri-lanka.html">how to choose a web design company in Sri Lanka</a>.')),
   ('mistakes', 'Common Mistakes When Buying a Package', ol([
     '<strong>Choosing only on price.</strong> A cheap site that is slow, insecure or invisible on Google costs more in lost customers.',
     '<strong>Not owning your domain.</strong> Make sure the domain is registered in your name or your company’s name.',
     '<strong>Ignoring mobile.</strong> Most visitors in Sri Lanka browse on phones, so check the mobile version of past work.',
     '<strong>No access to your own website.</strong> You should receive the admin login and be able to move the site if you ever need to.',
     '<strong>Skipping the portfolio.</strong> Look at live websites the company has built, not only screenshots.'])),
   ('ours', 'Our Packages', P(
     'At Web Development Sri Lanka, every package includes a responsive design, on-page SEO, free SSL, first-year hosting and support after launch. You can see the full list of features side by side on our <a href="packages.html">web design Sri Lanka price list</a>, and you can view live client websites in our <a href="portfolio.html">portfolio</a>.',
     'Not sure which one fits? Send us a short message about your business and we will recommend a package honestly, even if that means the smaller one.')),
  ],
  faqs=[('What is the cheapest web design package in Sri Lanka?', 'Prices vary widely. With Web Development Sri Lanka, a professional starter website with up to 5 pages starts from LKR 20,000, including SSL, first-year hosting and SEO setup.'),
        ('Can I upgrade my package later?', 'Yes. A starter website can be upgraded to a business or e-commerce website later, so you only pay for what you need today.'),
        ('Are hosting and the domain included in web design packages?', 'Our packages include first-year hosting and SSL. Domain registration and renewals, and hosting from the second year, are yearly costs.'),
        ('How long does a package website take to build?', 'Usually one to two weeks for a starter website, three to four weeks for a business website and four to six weeks for an e-commerce website.')],
  rel=['website-cost-in-sri-lanka', 'how-to-choose-a-web-design-company-sri-lanka', 'ecommerce-website-sri-lanka']),

 dict(slug='website-maintenance-sri-lanka', date='2026-11-26', cover='gauraconstruction', img_alt='Website maintenance dashboard with updates, backups and security checks', eyebrow='Website Care',
  title='Website Maintenance in Sri Lanka: What It Includes and Why',
  h1='Website Maintenance: <span class="accent">What It Includes</span>',
  desc='What website maintenance includes, why it matters for security, speed and SEO, and how to choose a maintenance plan for your Sri Lankan business website.',
  intro='A website is not finished on launch day. Software needs updates, content goes out of date, and security threats change every month. Website maintenance keeps your site safe, fast and accurate so it keeps bringing in customers. Here is what a good maintenance plan covers and how to decide what you need.',
  key=['Maintenance protects your website from hacking, downtime and data loss.',
       'Regular updates keep the site fast and compatible with new browsers.',
       'Fresh, accurate content helps both customers and Google rankings.',
       'Choose a plan based on how often your site changes and how critical it is.'],
  secs=[
   ('what', 'What Is Website Maintenance?', P(
     'Website maintenance is the regular work needed to keep a website secure, working and up to date after it goes live. It includes technical tasks such as software updates, backups and security monitoring, and business tasks such as updating prices, adding new products and publishing news.',
     'Think of it like servicing a vehicle. A new car runs well, but without regular servicing small problems turn into expensive repairs. Websites are the same: a missed update or an expired certificate can take a site offline or put customer data at risk.')),
   ('why', 'Why Maintenance Matters', P(
     'For most businesses the website is the first place customers check. If it is slow, shows a security warning or lists last year’s prices, people quietly go to a competitor. Maintenance prevents that.') + ul([
     '<strong>Security:</strong> most hacked websites run outdated software. Updates close the holes attackers use.',
     '<strong>Uptime:</strong> monitoring catches problems quickly, so your site is not down for days without you knowing.',
     '<strong>Speed:</strong> clean databases, optimised images and current software keep pages fast.',
     '<strong>SEO:</strong> Google prefers secure, fast, regularly updated websites.',
     '<strong>Trust:</strong> accurate contact details, prices and opening hours stop lost enquiries.'])),
   ('tasks', 'What a Maintenance Plan Should Include', table(
     ['Task', 'How often', 'Why it matters'], [
      ['Software, theme and plugin updates', 'Weekly or monthly', 'Fixes security holes and bugs'],
      ['Full backups (files and database)', 'Daily or weekly', 'Restores the site after any problem'],
      ['Uptime monitoring', 'Every few minutes', 'Alerts when the site goes down'],
      ['Security scans', 'Weekly', 'Finds malware and suspicious changes'],
      ['SSL certificate check', 'Monthly', 'Prevents “Not secure” warnings'],
      ['Speed check', 'Monthly', 'Keeps pages loading quickly'],
      ['Broken link and form tests', 'Monthly', 'Makes sure enquiries reach you'],
      ['Content updates', 'As needed', 'Keeps prices, products and news accurate']]) + tip('Ask your provider to test the contact form and WhatsApp button every month. A broken form can cost you enquiries for weeks before anyone notices.')),
   ('wordpress', 'Maintenance for WordPress vs Custom Websites', P(
     'WordPress websites rely on a core system, a theme and plugins written by different developers. Each part gets regular updates, and they must stay compatible with each other. That makes regular updates essential, and it is why unmaintained WordPress sites are a common target for attackers.',
     'Custom-coded websites have fewer moving parts and no third-party plugins, so they need fewer updates, but they still need backups, monitoring, SSL renewal and content changes. Our comparison of <a href="wordpress-vs-custom-website.html">WordPress vs a custom website</a> explains the trade-offs in more detail.')),
   ('content', 'Content Maintenance Is Just as Important', P(
     'Technical health is only half the job. Customers notice outdated content immediately: an old phone number, a product you no longer sell, a “2023 offer” banner or a blog that stopped years ago. Each one makes the business look inactive.',
     'Set a simple routine. Review prices and contact details every quarter, remove expired offers, add new projects to your portfolio and publish at least one useful article a month. Regular content also gives Google a reason to visit and rank your website more often.') + MID_CTA),
   ('diy', 'Can You Maintain a Website Yourself?', P(
     'If your website has a CMS, you can handle content changes yourself after a short training session. Many business owners update products, photos and blog posts without any help.',
     'Technical maintenance is different. Updates sometimes conflict, backups must be tested, and security problems need quick, careful fixes. Unless someone on your team has the skills and time, a maintenance plan is usually cheaper than fixing a hacked or broken website.')),
   ('signs', 'Signs Your Website Needs Attention Now', ul([
     'Browsers show “Not secure” next to your address.',
     'Pages take more than three seconds to load on a phone.',
     'The contact form or WhatsApp button does not work.',
     'Strange pages, links or pop-ups appear that you did not add.',
     'Your admin panel shows many pending updates.',
     'Your Google ranking or traffic has dropped suddenly.']) + P('If you see any of these, act quickly. Our article on <a href="website-redesign-signs.html">signs your website needs a redesign</a> helps you decide whether a fix or a fresh website is the better option.')),
   ('choose', 'How to Choose a Maintenance Plan', P(
     'Match the plan to how important the website is to your income. A brochure website that changes a few times a year needs updates, backups and monitoring. An online store or booking site that takes payments every day needs faster response times, more frequent backups and regular checks of the checkout.',
     'Ask each provider exactly what is included, how quickly they respond to a problem, where backups are stored and whether content changes are included or charged separately.')),
   ('ours', 'Maintenance With Web Development Sri Lanka', P(
     'We offer affordable monthly maintenance for websites we build and for existing websites, covering updates, backups, uptime and security monitoring, and content changes. Every website we build also includes support after launch. See our <a href="services.html">hosting and maintenance services</a> or <a href="contact.html">contact us</a> for a quote based on your website.')),
  ],
  faqs=[('What does website maintenance include?', 'Software and plugin updates, regular backups, uptime and security monitoring, SSL checks, speed checks, form testing and content updates such as prices, products and news.'),
        ('How often should a website be maintained?', 'Security updates and backups should happen at least weekly for most business websites, with monthly checks of speed, forms and content. Online stores need more frequent checks.'),
        ('Is website maintenance necessary for a small business?', 'Yes. Even a small website can be hacked, go offline or show outdated information. Basic maintenance is far cheaper than fixing a broken or hacked site.'),
        ('Do you maintain websites built by other companies?', 'Yes. We can review an existing website, fix urgent issues and then maintain it on a monthly plan.')],
  rel=['wordpress-vs-custom-website', 'website-cost-in-sri-lanka', 'web-design-packages-sri-lanka']),

 dict(slug='domain-and-hosting-sri-lanka', date='2026-11-27', cover='dagtech', img_alt='Domain name and web hosting setup for a Sri Lankan business website', eyebrow='Beginner Guide',
  title='Domain and Web Hosting in Sri Lanka: A Beginner’s Guide',
  h1='Domain &amp; Web Hosting in Sri Lanka: <span class="accent">Explained</span>',
  desc='A simple guide to domains and web hosting in Sri Lanka: .lk vs .com, how to register a domain, types of hosting, SSL and what to check before you buy.',
  intro='Every website needs two things before it can go live: a domain name, which is your address on the internet, and web hosting, which is where your website files live. The terms sound technical, but the decisions are simple once you understand them. This guide explains both in plain language for Sri Lankan businesses.',
  key=['A domain is your website address; hosting is the server that stores your site.',
       'Choose .lk for a local identity or .com for an international audience, or both.',
       'Register the domain in your own name so you always control it.',
       'Good hosting is fast, secure, backed up and supported locally.'],
  secs=[
   ('domain', 'What Is a Domain Name?', P(
     'A domain name is the address people type to visit your website, such as <em>yourbusiness.lk</em> or <em>yourbusiness.com</em>. It is also used for professional email addresses like <em>info@yourbusiness.lk</em>, which look far more trustworthy than a free email account.',
     'You do not buy a domain forever. You register it for a period, usually one year or more, and renew it before it expires. If a domain expires and is not renewed, someone else can register it, so renewals are important.')),
   ('lk', '.lk or .com: Which Should You Choose?', P(
     'The <strong>.lk</strong> extension is Sri Lanka’s country domain, managed by the LK Domain Registry. It tells visitors and Google that you are a Sri Lankan business, which can help with local trust. Variations such as .com.lk are also available.',
     'A <strong>.com</strong> domain is international and familiar everywhere, which suits exporters, tourism businesses and companies with overseas customers. .com domains are usually cheaper to register than .lk domains.') + table(
     ['', '.lk', '.com'], [
      ['Best for', 'Local businesses and Sri Lankan brands', 'International audience, tourism, exports'],
      ['Local trust', 'Strong', 'Neutral'],
      ['Typical cost', 'Higher', 'Lower'],
      ['Registration', 'Through the LK Domain Registry or its partners', 'Through any international registrar']]) + tip('If your budget allows, register both the .lk and the .com version of your name and point one to the other. It protects your brand and catches customers who type the wrong ending.')),
   ('pick', 'How to Pick a Good Domain Name', ol([
     '<strong>Keep it short</strong> and easy to spell when you say it over the phone.',
     '<strong>Use your business name</strong> where possible, or a clear description such as your service and city.',
     '<strong>Avoid hyphens and numbers</strong>, which people forget or mistype.',
     '<strong>Check social media handles</strong> so your brand matches everywhere.',
     '<strong>Make sure it is not a trademark</strong> belonging to someone else.'])),
   ('hosting', 'What Is Web Hosting?', P(
     'Web hosting is the service that stores your website on a server connected to the internet all day. When someone visits your domain, the server sends them your pages, images and files. The quality of your hosting affects how fast your site loads, how often it is available and how safe it is.',
     'There are several types of hosting. Most small and medium business websites run perfectly on good shared hosting or managed hosting. Larger online stores and web applications may need a virtual private server (VPS) or cloud hosting with dedicated resources.') + table(
     ['Type', 'Best for', 'Notes'], [
      ['Shared hosting', 'Small business websites', 'Affordable; quality varies a lot between providers'],
      ['Managed hosting', 'Busy business sites and WordPress', 'Updates, backups and security handled for you'],
      ['VPS / cloud', 'Online stores, web apps', 'More power and control; needs technical management'],
      ['Free hosting', 'Not recommended for business', 'Slow, limited and often shows ads']])),
   ('check', 'What to Check Before Buying Hosting', ul([
     '<strong>Speed:</strong> modern SSD or NVMe storage and servers close to your visitors.',
     '<strong>Free SSL:</strong> the padlock and https are essential for trust and SEO.',
     '<strong>Backups:</strong> automatic daily or weekly backups you can restore easily.',
     '<strong>Uptime:</strong> a reliable provider with monitoring and quick support.',
     '<strong>Email:</strong> whether business email accounts are included.',
     '<strong>Support:</strong> someone who answers quickly when there is a problem.']) + MID_CTA),
   ('ssl', 'SSL Certificates: The Padlock in the Browser', P(
     'An SSL certificate encrypts the connection between your website and its visitors. Without it, browsers such as Chrome show a “Not secure” warning, which scares customers away and can hurt your Google rankings. With it, your address starts with https and shows a padlock.',
     'Free SSL certificates are now standard with good hosting and renew automatically. There is no reason for any business website to run without one. Our <a href="website-maintenance-sri-lanka.html">website maintenance guide</a> explains why SSL renewals should be monitored.')),
   ('own', 'Always Keep Control of Your Domain and Hosting', P(
     'One of the most common problems we see is a business that cannot change its website because a previous developer registered the domain in their own name or holds the only hosting login. Avoid this by making sure the domain is registered in your name or your company’s name, and that you have the login details for both the domain and hosting accounts.',
     'Keep a simple record of where your domain is registered, when it renews, where the website is hosted and who has access. It takes ten minutes and can save your business from a lot of stress.')),
   ('connect', 'How Domain, Hosting and Email Work Together', P(
     'Your domain points to your hosting using DNS records. One record sends website visitors to your server, and others send your emails to your mailbox provider. This is why changing hosting or email providers involves updating DNS, and why it should be done carefully so emails and the website are not interrupted.',
     'If this sounds complicated, a good web design company handles it for you during setup, and explains what each record does.')),
   ('ours', 'Domain and Hosting With Web Development Sri Lanka', P(
     'Every website package we build includes free SSL and first-year hosting, and we can register a .lk or .com domain for you or connect one you already own. You keep ownership of your domain and receive all access details. See what each package includes on our <a href="packages.html">price list</a>, or read <a href="web-design-packages-sri-lanka.html">what you get with each web design package</a>.')),
  ],
  faqs=[('Should I choose a .lk or .com domain?', 'Choose .lk for a strong local identity and .com for an international audience. Many businesses register both and point one to the other.'),
        ('Who should own my domain name?', 'You or your company. Make sure the domain is registered in your name and that you have the login details, even if a developer manages it for you.'),
        ('Is web hosting included in your website price?', 'Yes. All our packages include first-year hosting and free SSL. Hosting renews yearly from the second year.'),
        ('Can I move my existing website to new hosting?', 'Yes. A website can be moved to new hosting without losing content, as long as the move and the DNS changes are planned carefully.')],
  rel=['web-design-packages-sri-lanka', 'website-maintenance-sri-lanka', 'website-cost-in-sri-lanka']),

 dict(slug='payment-gateway-sri-lanka', date='2026-11-28', cover='themerchlist', img_alt='Online checkout page with card payment and cash on delivery options', eyebrow='E-Commerce',
  title='Payment Gateways in Sri Lanka: How to Accept Online Payments',
  h1='Payment Gateways in Sri Lanka: <span class="accent">Accept Payments Online</span>',
  desc='How to accept online payments on your website in Sri Lanka: types of payment gateways, what to compare, documents you need, and how checkout affects sales.',
  intro='An online store only works if customers can pay easily and safely. In Sri Lanka you can accept card payments, bank transfers, mobile wallets, cash on delivery and instalment plans, but each option works differently. This guide explains how payment gateways work, what to compare and how to set up a checkout that customers trust.',
  key=['A payment gateway securely connects your website checkout to card networks and banks.',
       'Compare fees, settlement time, supported cards and ease of integration.',
       'Offer more than one method, including cash on delivery, to reduce lost sales.',
       'A simple, secure, mobile-friendly checkout matters as much as the gateway itself.'],
  secs=[
   ('what', 'What Is a Payment Gateway?', P(
     'A payment gateway is the service that takes a customer’s card or wallet details on your website, checks them with the bank and card network, and confirms whether the payment succeeded. The money is then settled into your bank account, usually after a short delay.',
     'You never store card numbers on your own website. The gateway handles the sensitive data on its secure systems, which is why using a recognised gateway is essential for both security and customer trust.')),
   ('options', 'Payment Options for Sri Lankan Websites', P(
     'Sri Lankan businesses have several ways to get paid online. Most successful stores offer two or three of them so every customer can pay in the way they prefer.') + table(
     ['Method', 'How it works', 'Good for'], [
      ['Local payment gateways', 'Card and wallet payments through a Sri Lankan provider such as PayHere or WebXPay', 'Most local online stores'],
      ['Bank payment gateways', 'Card payments through a bank’s own internet payment gateway', 'Larger businesses with bank relationships'],
      ['Buy now, pay later', 'Customers pay in instalments through services such as Koko or Mintpay', 'Higher-priced items'],
      ['Bank transfer', 'Customer transfers money and sends a receipt', 'B2B orders, small shops'],
      ['Cash on delivery', 'Customer pays the courier on delivery', 'Building trust with new customers']]) + tip('Providers, fees and features change often, so always check the latest terms directly with each provider before you choose.')),
   ('compare', 'What to Compare Between Gateways', ul([
     '<strong>Transaction fees:</strong> usually a percentage of each payment; check for setup or monthly fees too.',
     '<strong>Settlement time:</strong> how many days until money reaches your bank account.',
     '<strong>Supported payments:</strong> Visa, Mastercard, Amex, local wallets and foreign cards.',
     '<strong>Currencies:</strong> important if you sell to tourists or overseas customers.',
     '<strong>Integration:</strong> ready plugins for your platform, or an API for custom websites.',
     '<strong>Refunds and disputes:</strong> how easily you can refund an order.',
     '<strong>Dashboard:</strong> clear reports of payments and payouts.'])),
   ('documents', 'What You Usually Need to Apply', P(
     'Gateways need to verify your business before they let you accept payments. Requirements differ, but you should be ready with:') + ul([
     'Business registration documents, or identity documents for sole proprietors.',
     'A business bank account in the same name.',
     'A working website with clear product details and prices.',
     'Published policies: terms and conditions, privacy policy, refund and delivery policies.',
     'Contact details: phone number, email and physical address.']) + P('Many applications are delayed because the website is incomplete. Building the policies and product pages first speeds up approval.')),
   ('checkout', 'Design a Checkout That Customers Trust', P(
     'Even with the best gateway, a confusing checkout loses sales. Customers abandon carts when they see unexpected delivery charges, long forms, or a page that looks unsafe.') + ol([
     'Show delivery charges early, ideally on the product or cart page.',
     'Ask only for the details you need to deliver the order.',
     'Allow guest checkout without forcing account creation.',
     'Display the payment logos and the padlock clearly.',
     'Make the checkout fast and easy to use on phones.',
     'Send an immediate order confirmation by email and, ideally, SMS or WhatsApp.']) + MID_CTA),
   ('cod', 'Cash on Delivery Still Matters', P(
     'Many Sri Lankan customers still prefer to pay on delivery, especially for their first order with a new shop. Offering cash on delivery alongside card payments often increases total sales, even if more customers eventually switch to paying online.',
     'To reduce failed deliveries, confirm cash on delivery orders by phone or WhatsApp before dispatch, and consider limits for very high-value orders.')),
   ('security', 'Security and Compliance', P(
     'Your website must use SSL so all data is encrypted. Card data should be entered on the gateway’s secure page or secure fields, not stored in your database. Keep your website software updated and restrict admin access to the people who really need it.',
     'Our guide to <a href="domain-and-hosting-sri-lanka.html">domains, hosting and SSL</a> explains the basics, and regular <a href="website-maintenance-sri-lanka.html">website maintenance</a> keeps your store secure over time.')),
   ('international', 'Selling to Overseas Customers', P(
     'If you sell to tourists or customers abroad, check whether your gateway accepts foreign cards and which currencies it can display. Tourism businesses such as tour operators and car rental companies often take a deposit online and the balance on arrival, which keeps fees lower and reduces cancellations.',
     'Clear pricing, cancellation terms and quick confirmation emails matter even more when the customer is in another country.')),
   ('ours', 'Payment Integration With Web Development Sri Lanka', P(
     'Our e-commerce package includes payment gateway integration, cash on delivery, delivery charges and order notifications. We help you choose the right provider and prepare the pages gateways require. Read our complete guide to building an <a href="ecommerce-website-sri-lanka.html">e-commerce website in Sri Lanka</a> or see our <a href="packages.html">e-commerce package from LKR 39,000</a>.')),
  ],
  faqs=[('How can I accept card payments on my website in Sri Lanka?', 'Sign up with a payment gateway provider, connect it to your website checkout and complete their business verification. Your customers can then pay by card or wallet online.'),
        ('Which payment gateway is best in Sri Lanka?', 'It depends on your fees, settlement time, cards and currencies you need, and how your website is built. Compare current terms from several providers before choosing.'),
        ('Should I offer cash on delivery?', 'For most Sri Lankan online stores, yes. Many customers prefer cash on delivery for a first order, and offering it alongside card payments usually increases sales.'),
        ('Do I need a registered business to accept online payments?', 'Most gateways require business registration or identity documents, a bank account and a complete website with policies. Check each provider’s requirements.')],
  rel=['ecommerce-website-sri-lanka', 'web-design-packages-sri-lanka', 'domain-and-hosting-sri-lanka']),

 dict(slug='google-business-profile-sri-lanka', date='2026-11-29', cover='lastsolution', img_alt='Google Maps listing of a local business with reviews and directions', eyebrow='Local SEO',
  title='Google Business Profile in Sri Lanka: A Complete Guide',
  h1='Google Business Profile: <span class="accent">Get Found Locally</span>',
  desc='Set up and optimise your Google Business Profile in Sri Lanka to appear on Google Maps and local searches, get more calls and connect it to your website.',
  intro='When someone searches for a service near them, Google often shows a map with three local businesses before any normal website results. Those listings come from Google Business Profile. Setting it up is free, and a well-optimised profile can bring calls, directions and website visits every week. Here is how to do it properly.',
  key=['Google Business Profile is free and powers your listing on Google Search and Maps.',
       'Choose the right category, add accurate details and verify your business.',
       'Reviews, photos and regular posts help you rank higher in the local map results.',
       'Link the profile to a fast website for the best results.'],
  secs=[
   ('what', 'What Is Google Business Profile?', P(
     'Google Business Profile, previously called Google My Business, is the free listing that shows your business name, address, phone number, opening hours, photos and reviews on Google Search and Google Maps. It is often the first thing a customer sees about you, even before they visit your website.',
     'For local businesses such as shops, restaurants, clinics, builders, schools and service providers, it is one of the most valuable free marketing tools available.')),
   ('why', 'Why It Matters for Sri Lankan Businesses', ul([
     '<strong>Appear in the local map results</strong> for searches like “web design Kurunegala” or “restaurant near me”.',
     '<strong>Get calls and directions</strong> directly from the listing.',
     '<strong>Build trust</strong> with reviews and real photos.',
     '<strong>Show up for your brand name</strong> with a full information panel.',
     '<strong>Send visitors to your website</strong> to learn more and make an enquiry.'])),
   ('setup', 'How to Set Up Your Profile', ol([
     'Go to Google Business Profile and sign in with a Google account you control long term.',
     'Enter your exact business name, as it appears on your signboard and documents.',
     'Choose the most accurate primary category, for example “Website designer” or “Hardware store”.',
     'Add your address if customers visit you, or set a service area if you travel to customers.',
     'Add your phone number and your website address.',
     'Verify the business using the method Google offers, such as a phone call, video or postcard.']) + tip('Do not add keywords to your business name, such as “Best Web Design Sri Lanka”. Google can suspend profiles for this. Use your real business name.')),
   ('optimise', 'How to Optimise Your Profile', P(
     'Once verified, complete every section. Google tends to favour complete, active profiles.') + table(
     ['Section', 'What to do'], [
      ['Categories', 'One accurate primary category and a few relevant secondary ones'],
      ['Description', 'Explain what you do, where and for whom, in natural language'],
      ['Hours', 'Keep them accurate, including holidays such as Poya days'],
      ['Services / products', 'List each service with a short description and price if possible'],
      ['Photos', 'Add your logo, cover, premises, team and real work regularly'],
      ['Posts', 'Share offers, news and new projects weekly or monthly'],
      ['Questions and answers', 'Add common questions and clear answers']]) + MID_CTA),
   ('reviews', 'Reviews: The Biggest Local Ranking Factor You Control', P(
     'Reviews influence both rankings and decisions. A business with many recent, detailed reviews looks more trustworthy and often ranks higher in the map results.',
     'Ask every happy customer for a review, ideally right after you finish the job. Send them a direct review link by WhatsApp or email to make it easy. Reply to every review, thank people for positive feedback and respond calmly and helpfully to negative feedback. Never buy fake reviews or offer rewards for reviews, which breaks Google’s rules.')),
   ('nap', 'Keep Your Name, Address and Phone Consistent', P(
     'Google compares your business details across the web. Use exactly the same business name, address and phone number on your profile, your website, Facebook, directories and any other listings. Inconsistent details confuse Google and customers.',
     'Your website should also show the same details in the footer and contact page, and ideally in structured data. Our guide to <a href="seo-for-small-businesses-sri-lanka.html">SEO for small businesses in Sri Lanka</a> explains how the website and profile work together.')),
   ('website', 'Connect Your Profile to a Strong Website', P(
     'Many people check the website before they call. A profile that links to a slow, outdated or missing website loses those customers. A fast, mobile-friendly website with clear service pages, prices and contact options turns profile views into enquiries.',
     'Use a separate page for each main service and location you serve. If you have one office, link the profile to your home page or contact page.')),
   ('mistakes', 'Common Mistakes to Avoid', ul([
     'Creating duplicate profiles for the same business.',
     'Using a P.O. box or virtual office that customers cannot visit.',
     'Leaving old phone numbers or wrong opening hours.',
     'Ignoring reviews and questions from customers.',
     'Choosing a broad category such as “Company” instead of a specific one.'])),
   ('track', 'Track Your Results', P(
     'Your profile dashboard shows how many people found you, how they searched, and how many called, asked for directions or clicked to your website. Check these numbers monthly, and combine them with Google Search Console and Analytics on your website to see the full picture.',
     'Need help? We set up and optimise Google Business Profiles as part of our <a href="services.html">SEO services</a>, and our websites are built to support local rankings. <a href="contact.html">Contact us</a> to get started.')),
  ],
  faqs=[('Is Google Business Profile free?', 'Yes. Creating and managing a Google Business Profile is free. You only need a Google account and a real business that serves customers.'),
        ('Can I create a profile without a shop or office?', 'Yes. Service businesses that visit customers can hide their address and set a service area instead.'),
        ('How do I rank higher on Google Maps in Sri Lanka?', 'Choose the right category, complete every section, keep your details consistent, collect genuine reviews regularly, add photos and posts, and link to a fast, relevant website.'),
        ('How long does verification take?', 'It depends on the method Google offers. Phone, email or video verification can be quick, while postcard verification can take longer.')],
  rel=['seo-for-small-businesses-sri-lanka', 'why-your-business-needs-a-website', 'web-design-packages-sri-lanka']),
]
