# Extra sections for posts 2 to 10
def _add(slug, secs):
    EXTRA[slug] = EXTRA.get(slug, []) + secs

_add('website-maintenance-sri-lanka', [
 ('checklist', 'A Simple Monthly Maintenance Checklist', ol([
   'Confirm the latest backup completed and is stored off the server.',
   'Apply pending updates after taking a fresh backup.',
   'Open the website on a phone and a computer and check the main pages.',
   'Send a test enquiry through the contact form and tap the WhatsApp button.',
   'Check Google Search Console for errors, security issues and indexing problems.',
   'Review prices, offers, opening hours and contact details.',
   'Run a speed test on the home page and one important service page.']) + P(
   'This takes less than an hour a month for most small websites and catches the majority of problems before customers notice them.')),
])
_add('domain-and-hosting-sri-lanka', [
 ('mistakes', 'Common Domain and Hosting Mistakes', ul([
   '<strong>Letting a developer own the domain.</strong> Always register it in your own or your company’s name.',
   '<strong>Choosing hosting only on price.</strong> Slow, unreliable hosting costs more in lost visitors.',
   '<strong>Using free email for business.</strong> It looks less professional and is easier to impersonate.',
   '<strong>Forgetting renewal dates.</strong> An expired domain takes the website and email offline.',
   '<strong>No backups.</strong> Assume something will go wrong one day, and be ready to restore.']) + P(
   'Avoiding these five mistakes puts you ahead of many businesses and protects the investment you make in your website.')),
])
_add('payment-gateway-sri-lanka', [
 ('policies', 'Write Clear Store Policies', P(
   'Clear policies protect both you and your customers, and gateways usually require them. Your refund and returns policy should explain which items can be returned, the time limit, the condition required and how refunds are paid. Your delivery policy should list delivery areas, charges, expected times and what happens if a customer is not available.',
   'Write them in simple language, link them in the footer and at checkout, and follow them consistently. Customers are more willing to pay online when they know exactly what happens if something goes wrong.')),
])
_add('google-business-profile-sri-lanka', [
 ('reviewlink', 'Make Asking for Reviews a Habit', P(
   'The businesses with the most reviews are usually not the biggest, but the ones that ask consistently. Copy your review link from the profile dashboard and save it as a quick reply in WhatsApp Business. Send it after every completed job, delivery or visit with a short personal thank-you message.',
   'Print a QR code that opens the review page and place it at your counter, on receipts or on delivery packaging. Train staff to mention it politely. Within a few months, a steady flow of genuine reviews can transform how your business appears on Google Maps.')),
])
_add('restaurant-website-design-sri-lanka', [
 ('events', 'Promote Events, Offers and Private Dining', P(
   'Restaurants earn a large share of income from special occasions: birthdays, office parties, weddings, Christmas and Avurudu menus. Give these their own pages with menus, prices per person, photos of the space and an enquiry form. Customers planning events search well in advance, and a clear page can win a large booking in a single enquiry.',
   'Use a simple offers page for weekday lunch deals, happy hours or seasonal dishes, and share each offer on social media with a link back to the website, where customers can see the full menu and book.')),
 ('measure', 'Measure What Your Website Brings', P(
   'Track calls, WhatsApp clicks, bookings and online orders from the website. Google Analytics and your Google Business Profile dashboard show how many people viewed your menu, asked for directions or called. Ask guests how they found you. These numbers show which pages and promotions work, so you can invest in what brings people through the door.')),
])
_add('website-redesign-signs', [
 ('data', 'Use Data to Decide', P(
   'Feelings about a website are useful, but numbers are better. Before deciding, look at a few figures from Google Analytics and Search Console over the last year:') + ul([
   '<strong>Mobile share of visitors:</strong> if most visitors use phones, mobile experience is your priority.',
   '<strong>Engagement:</strong> how long visitors stay and how many pages they view.',
   '<strong>Conversion rate:</strong> how many visitors call, message or fill in a form.',
   '<strong>Search performance:</strong> impressions, clicks and average position for your main services.',
   '<strong>Core Web Vitals:</strong> whether your pages pass Google’s experience measures.']) + P(
   'These numbers show where the current site fails and give you a baseline to measure the new website against after launch.')),
 ('brief', 'Write a Simple Redesign Brief', P(
   'A short brief makes any redesign faster and cheaper. Write one page that covers your goals, your main customers, the services you want to promote, websites you like, what must stay from the current site, the features you need and your budget and timeline. Share it with each company you speak to, so their proposals are easy to compare.',
   'Include a list of everything that frustrates you or your customers about the current website. Those frustrations often become the most valuable improvements in the new one.')),
 ('after', 'After the Redesign', P(
   'Launch is the start, not the end. In the first weeks, check Search Console daily for errors, watch analytics for changes in traffic and enquiries, and fix any broken links quickly. Ask a few loyal customers for feedback. Then keep the new website fresh with regular content and maintenance so you do not end up needing another full redesign too soon.')),
])
_add('landing-page-vs-website', [
 ('example', 'Example: One Campaign, Two Approaches', P(
   'Imagine a clinic running Facebook ads for a dental check-up offer. In the first approach, the ad links to the clinic’s home page. Visitors see a general welcome message, a slider and a menu with twelve items. Some find the offer; many do not.',
   'In the second approach, the ad links to a landing page titled “Dental Check-Up and Cleaning Offer in Kandy”. The page shows the price, what is included, photos of the clinic, reviews from patients, the dentist’s qualifications, available times and a large “Book on WhatsApp” button. Every element supports one decision. The second approach usually produces far more bookings from the same ad budget.')),
 ('testing', 'Test and Improve Your Landing Pages', P(
   'A landing page is never finished. Small changes can make a big difference to results, so test one thing at a time: the headline, the main image, the offer, the button text or the length of the form. Run each version long enough to collect meaningful numbers before deciding.',
   'Keep a simple record of what you tested and what happened. Over a few campaigns, you will learn what your customers respond to, and that knowledge improves your ads, your website and even your sales conversations.')),
 ('cost', 'What Does a Landing Page Cost?', P(
   'A landing page usually costs less than a full website because it is a single page, but it still needs careful copywriting, design, speed optimisation and tracking setup. Many businesses add landing pages to an existing website as campaigns come up. If you do not yet have a website, start with a starter or business website and add landing pages for your campaigns. Our guide to <a href="web-design-packages-sri-lanka.html">web design packages in Sri Lanka</a> explains the options.')),
])
_add('website-speed-optimisation', [
 ('fonts', 'Fix 6: Load Fonts Efficiently', P(
   'Custom fonts give a website personality, but each font family and weight is another file to download. Choose one or two families, load only the weights you actually use, and use the font-display setting so text appears immediately in a fallback font while the custom font loads. Avoid icon fonts with hundreds of unused icons when a few small SVG icons would do.')),
 ('third', 'Fix 7: Be Careful With Third-Party Scripts', P(
   'Chat widgets, social media feeds, review widgets, tracking pixels and embedded maps all load code from other companies’ servers. Each one can slow your page, and you cannot control how fast those servers respond. Keep only the scripts that bring real value, load them after the main content, and replace heavy embeds with lighter alternatives where possible, such as a static map image that links to Google Maps.')),
 ('measure', 'Speed Is Ongoing Work', P(
   'Websites tend to get slower over time as new images, plugins and scripts are added. Check your speed every month and after any big change. Make image optimisation part of your routine whenever you upload photos, and review plugins and scripts every few months. Our <a href="website-maintenance-sri-lanka.html">website maintenance guide</a> shows how to build these checks into a simple monthly routine.',
   'For online stores and booking websites, even small speed improvements can produce noticeable increases in completed orders, so speed work often pays for itself quickly.')),
])
_add('web-design-kurunegala', [
 ('examples', 'What Good Local Websites Have in Common', P(
   'Looking at successful local business websites across Sri Lanka, the same patterns appear again and again. They explain clearly what the business does in the first screen. They show real photos of real work. They make contact effortless with phone and WhatsApp buttons. They list prices or price ranges. And they keep information current.',
   'None of this requires a huge budget. It requires a clear plan and a website built for how local customers actually search and decide. You can see examples of these patterns in the websites in our <a href="portfolio.html">portfolio</a>, from construction and retail to tourism and education.')),
 ('language', 'Reaching Customers in Sinhala, Tamil and English', P(
   'Many customers in the Kurunegala District search and read in Sinhala, while professional and overseas audiences often prefer English. Think about who your customers are. A retail shop or tuition class may benefit from Sinhala content, while an exporter needs strong English pages for international buyers.',
   'If you add languages, keep each version complete and accurate, and set up separate pages for each language so search engines show the right one. Even a few key pages in a second language, such as services, prices and contact, can make a real difference.')),
 ('grow', 'Growing Beyond Your Town', P(
   'A website removes geographical limits. A hardware supplier in Kurunegala can take orders from across the province, a manufacturer can reach buyers in Colombo and abroad, and a training institute can offer online courses island-wide. Plan your website with that growth in mind: clear delivery information, online enquiry forms and, when you are ready, online payments. Read our guide on <a href="payment-gateway-sri-lanka.html">accepting online payments</a> to see how.')),
])
