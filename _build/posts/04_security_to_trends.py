# Scheduled posts, batch 4 (10 to 14 December 2026)
POSTS += [
 dict(slug='website-security-guide', date='2026-12-10', cover='esms', img_alt='Website security shield with SSL, backups and login protection', eyebrow='Security',
  title='Website Security for Small Businesses: A Practical Guide',
  h1='Website Security for <span class="accent">Small Businesses</span>',
  desc='Practical website security for small businesses in Sri Lanka: SSL, updates, strong logins, backups, forms, hosting and what to do if your site is hacked.',
  intro='Small business websites are attacked every day, not because attackers chose them personally, but because automated tools scan the internet for weak sites. A hacked website can show spam, redirect visitors, leak customer data or be blocked by Google. The good news is that a few sensible habits stop most attacks. This guide explains them in plain language.',
  key=['Most attacks are automated and target outdated software and weak passwords.',
       'Use HTTPS, keep everything updated and protect logins with strong passwords and 2FA.',
       'Keep regular, tested backups stored away from the website server.',
       'Choose secure hosting and give admin access only to people who need it.'],
  secs=[
   ('why', 'Why Small Business Websites Get Hacked', P(
     'Many owners think “Nobody would want to hack my small website.” In reality, attackers rarely pick targets by hand. Bots scan thousands of sites for known weaknesses: old plugins, default passwords, unprotected forms and outdated server software. When they find one, they use it to send spam, host phishing pages, steal data or infect visitors.',
     'That means every website needs basic protection, whatever its size.')),
   ('risks', 'What Can Happen if Your Website Is Hacked', ul([
     'Visitors see spam, adult content or fake pages on your domain.',
     'Google shows a warning or removes your pages from search results.',
     'Customer information from forms or orders is stolen.',
     'Your hosting account is suspended for sending spam.',
     'Your email addresses are blacklisted, so messages land in spam.',
     'Repair costs, lost sales and damaged reputation.'])),
   ('https', '1. Use HTTPS Everywhere', P(
     'An SSL certificate encrypts data between visitors and your website, protecting forms, logins and payments. Without it, browsers warn visitors that your site is “Not secure”. Free certificates are available with good hosting and should renew automatically. Make sure every page redirects to the https version. Our guide to <a href="domain-and-hosting-sri-lanka.html">domains, hosting and SSL</a> explains the basics.')),
   ('updates', '2. Keep Software Updated', P(
     'Most successful attacks use known weaknesses that already have fixes. Keep your content management system, themes, plugins and server software up to date, and remove anything you do not use. Unused plugins and old test copies of your site are common entry points.',
     'If updating feels risky because things might break, that is a sign you need proper backups and a maintenance routine, as described in our <a href="website-maintenance-sri-lanka.html">website maintenance guide</a>.')),
   ('logins', '3. Protect Every Login', ol([
     'Use long, unique passwords for the website admin, hosting, domain, database and email.',
     'Turn on two-factor authentication (2FA) wherever it is available.',
     'Give each person their own account instead of sharing one admin login.',
     'Give staff only the permissions they need, such as editor instead of administrator.',
     'Remove accounts of former staff and developers immediately.',
     'Limit login attempts to block password-guessing bots.']) + tip('Store passwords in a reputable password manager rather than in a notebook, spreadsheet or WhatsApp chat.')),
   ('backups', '4. Keep Regular, Tested Backups', P(
     'Backups are your safety net. Back up both files and the database automatically, keep several versions, and store at least one copy away from your website server. Test a restore occasionally, because a backup you cannot restore does not protect you.') + MID_CTA),
   ('forms', '5. Secure Forms and Uploads', P(
     'Contact forms, comment boxes and file uploads are common targets for spam and attacks. Use spam protection, validate the information people send, limit file types and sizes for uploads, and never store card details on your own server. Online payments should always go through a secure payment gateway, as explained in our <a href="payment-gateway-sri-lanka.html">payment gateway guide</a>.')),
   ('hosting', '6. Choose Secure Hosting', P(
     'Good hosting providers keep servers updated, isolate accounts from each other, offer firewalls and malware scanning, and respond quickly to problems. Very cheap or free hosting often cuts corners on security. Ask your provider how they protect sites, how backups work and what support they give if something goes wrong.')),
   ('headers', '7. Add Security Headers and Monitoring', P(
     'Security headers tell browsers how to handle your site safely, for example only connecting through HTTPS and refusing to be embedded in other websites. Uptime monitoring and security scanning alert you quickly if something changes. These are technical steps, but a good web developer can set them up once in a few minutes.')),
   ('signs', 'Signs Your Website May Be Compromised', ul([
     'Pages, links or pop-ups you did not create.',
     'Google search results showing strange titles or foreign-language spam.',
     'Warnings in Google Search Console or the browser.',
     'Sudden drops in traffic or unusual traffic spikes.',
     'New admin users you do not recognise.',
     'Hosting company warnings about spam or high resource usage.'])),
   ('hacked', 'What to Do if You Are Hacked', ol([
     'Change all passwords and remove unknown users.',
     'Contact your hosting provider and your web developer.',
     'Restore a clean backup from before the attack, or clean the files carefully.',
     'Update all software and remove unused plugins and files.',
     'Find and fix the weakness that allowed the attack.',
     'Request a review in Google Search Console once the site is clean.'])),
   ('ours', 'Secure Websites by Web Development Sri Lanka', P(
     'Every website we build includes HTTPS, secure hosting, security headers and backups, and our maintenance plans keep sites updated and monitored. If you are worried about your current website, <a href="contact.html">contact us</a> for a security check, or see our <a href="services.html">hosting and maintenance services</a>.')),
  ],
  faqs=[('Why would anyone hack a small business website?', 'Most attacks are automated. Bots look for weak, outdated websites to send spam, host scams or steal data, regardless of the business size.'),
        ('Is SSL enough to make my website secure?', 'No. SSL encrypts data in transit, but you also need updates, strong logins, backups, secure hosting and monitoring.'),
        ('How often should I back up my website?', 'At least weekly for most business websites, and daily for online stores or sites that change often. Keep copies away from the main server.'),
        ('Can you fix a hacked website?', 'Yes. We can clean or restore the site, close the security hole, update the software and help you request a review from Google.')],
  rel=['website-maintenance-sri-lanka', 'domain-and-hosting-sri-lanka', 'wordpress-vs-custom-website']),

 dict(slug='ux-design-tips', date='2026-12-11', cover='mypalmfit', img_alt='User experience design wireframes and a mobile website layout', eyebrow='UX Design',
  title='UX Design Tips: 12 Ways to Turn Visitors Into Customers',
  h1='UX Design Tips: Turn Visitors Into <span class="accent">Customers</span>',
  desc='12 practical UX design tips for business websites: clear navigation, mobile usability, readable text, trust signals, forms and calls to action that convert.',
  intro='User experience (UX) is how easy and pleasant it is to use your website. Good UX is mostly invisible: visitors find what they need, understand your offer and contact you without thinking about it. Poor UX quietly sends them away. These twelve practical tips will help any business website feel easier to use and convert more visitors into customers.',
  key=['UX is about making it easy for visitors to find information and act.',
       'Design for mobile first, with large tap targets and readable text.',
       'Use clear navigation, headings and calls to action on every page.',
       'Test with real people and improve based on what they struggle with.'],
  secs=[
   ('what', 'What Is UX Design?', P(
     'UX design focuses on the whole experience of using a website: how quickly it loads, how easy it is to navigate, how clearly it explains things and how simple it is to complete a task such as booking or buying. UI (user interface) design is part of it, covering the visual elements like buttons, colours and typography.',
     'Our article on <a href="what-is-web-designing.html">what web designing is</a> explains how UX fits into the wider design process.')),
   ('t1', '1. Make the Purpose Clear in Five Seconds', P(
     'Visitors should understand what you offer, who it is for and what to do next within a few seconds of landing. Use a clear headline, a short supporting sentence and one obvious main button. If people have to scroll to find out what you do, many will not bother.')),
   ('t2', '2. Design for Mobile First', P(
     'Most visitors use phones. Start with the mobile layout: one column, large text, buttons big enough to tap with a thumb, and the most important actions within easy reach. Then expand the design for larger screens. Mobile-first design usually improves the desktop experience too, because it forces clarity.')),
   ('t3', '3. Keep Navigation Simple', P(
     'Limit the main menu to the pages people need most, usually five to seven items. Use familiar labels such as Services, Prices, Work, About and Contact rather than creative names. Make the logo link to the home page, and keep navigation in the same place on every page.')),
   ('t4', '4. Use a Clear Visual Hierarchy', P(
     'Size, colour and spacing tell visitors what matters most. Main headings should be largest, buttons should stand out in your accent colour, and less important details should be smaller. When everything is bold and colourful, nothing stands out.')),
   ('t5', '5. Make Text Easy to Read', P(
     'Use a comfortable font size, around 16 pixels or more for body text on mobile, good contrast between text and background, and line lengths that are not too wide. Break text into short paragraphs with descriptive headings. Our guide on <a href="website-content-writing-tips.html">writing website content that sells</a> covers the words themselves.')),
   ('t6', '6. Use Clear Calls to Action', P(
     'Every page should guide visitors to a next step: call, WhatsApp, get a quote, book or buy. Use specific button text such as “Get a free quote” instead of “Click here”, and repeat the main call to action at sensible points on long pages.') + MID_CTA),
   ('t7', '7. Build Trust Early', P(
     'Show reviews, client logos, photos of real work, guarantees and clear contact details near the top of important pages. People need to trust you before they share their details or pay.')),
   ('t8', '8. Make Forms Short and Friendly', ul([
     'Ask only for the information you really need.',
     'Use clear labels above fields, not only placeholder text.',
     'Show helpful error messages next to the field with the problem.',
     'Use the right keyboard on mobile, such as a number pad for phone numbers.',
     'Confirm clearly when the form has been sent.'])),
   ('t9', '9. Be Fast', P(
     'Speed is part of UX. Even a beautiful design feels frustrating when it loads slowly or jumps around. Follow the steps in our <a href="website-speed-optimisation.html">website speed guide</a> to keep pages fast on mobile networks.')),
   ('t10', '10. Be Consistent', P(
     'Use the same colours, button styles, fonts and layouts across the whole website. Consistency helps visitors learn how your site works once and then use it without thinking.')),
   ('t11', '11. Design for Everyone', P(
     'Accessible design helps people with visual, hearing, motor or cognitive difficulties, and it improves usability for everyone. Use sufficient colour contrast, add descriptive alt text to images, make sure the site works with a keyboard, and do not rely on colour alone to show information.')),
   ('t12', '12. Test With Real People', P(
     'The best UX insight comes from watching real people use your website. Ask a few customers or friends to complete simple tasks, such as finding a price or sending an enquiry, and watch where they hesitate. Tools such as Google Analytics and heatmaps show where visitors click and where they leave.') + tip('Ask someone who has never seen your website to find your phone number on their own phone. If it takes more than ten seconds, improve it today.')),
   ('ours', 'UX-Focused Web Design by Web Development Sri Lanka', P(
     'We design websites around how real customers browse and buy, with mobile-first layouts, clear navigation and calls to action that convert. See examples in our <a href="portfolio.html">portfolio</a>, learn about our <a href="services.html">UI/UX design service</a>, or <a href="contact.html">contact us</a> to improve your website.')),
  ],
  faqs=[('What is the difference between UX and UI design?', 'UX is the overall experience of using a website, including how easy it is to complete tasks. UI is the visual layer, such as buttons, colours and typography.'),
        ('How does UX affect sales?', 'Clear navigation, fast pages, trust signals and simple forms make it easier for visitors to contact you or buy, which usually increases enquiries and sales.'),
        ('How can I test my website’s UX?', 'Ask real people to complete simple tasks on their phones and watch where they struggle, then review analytics and heatmaps to see where visitors leave.'),
        ('Is mobile UX more important than desktop?', 'For most Sri Lankan businesses, yes, because most visitors use phones. Design for mobile first, then adapt for larger screens.')],
  rel=['what-is-web-designing', 'how-to-create-a-web-design', 'best-website-design-examples']),

 dict(slug='how-to-get-website-on-google', date='2026-12-12', cover='4u', img_alt='Google Search Console showing a website being indexed', eyebrow='SEO Basics',
  title='How to Get Your Website on Google: A Step-by-Step Guide',
  seo_title='How to Get Your Website on Google: Step-by-Step Guide',
  h1='How to Get Your Website <span class="accent">on Google</span>',
  desc='Why your new website is not on Google yet and how to fix it: Search Console, sitemaps, indexing, on-page SEO, Google Business Profile and backlinks.',
  intro='You launched a new website, searched for it on Google and found nothing. This is normal at first. Google needs to discover, understand and index your pages before they can appear, and then they need reasons to rank. This step-by-step guide explains how to get your website on Google and start appearing for the searches that matter.',
  key=['Google must discover and index a page before it can appear in search results.',
       'Verify your site in Google Search Console and submit your sitemap.',
       'Make sure pages are not blocked and have clear titles and content.',
       'Rankings then grow with useful content, local signals and quality links.'],
  secs=[
   ('how', 'How Google Finds Websites', P(
     'Google uses automated programs called crawlers to discover pages by following links and reading sitemaps. It then analyses each page and stores it in its index, a huge database of web pages. Only indexed pages can appear in search results. Finally, ranking systems decide which indexed pages best answer each search.',
     'So there are three separate questions: is Google able to find your page, has it indexed the page, and does it consider the page the best answer for a search?')),
   ('check', 'Step 1: Check Whether Your Site Is Indexed', P(
     'Search Google for <em>site:yourdomain.lk</em>. The results show pages from your website that Google has indexed. If nothing appears, Google has not indexed your site yet. If only some pages appear, others may be blocked, duplicated or not yet discovered.')),
   ('gsc', 'Step 2: Set Up Google Search Console', P(
     'Google Search Console is a free tool that shows how Google sees your website. Verify ownership of your domain using a DNS record or an HTML tag, then you can see which pages are indexed, which have problems, what searches bring visitors and whether there are security or usability issues.') + ol([
     'Go to Google Search Console and add your website as a property.',
     'Verify ownership using the method offered.',
     'Open the Sitemaps report and submit your sitemap address, usually <em>/sitemap.xml</em>.',
     'Use the URL Inspection tool to request indexing of important new pages.'])),
   ('blocks', 'Step 3: Remove Anything Blocking Google', ul([
     '<strong>Noindex tags</strong> left on from development tell Google not to index pages.',
     '<strong>robots.txt rules</strong> may block crawlers from the whole site.',
     '<strong>Password protection</strong> on a staging site that went live.',
     '<strong>Wrong canonical tags</strong> pointing to other pages or the old domain.',
     '<strong>Duplicate versions</strong> such as http, https, www and non-www without redirects.']) + tip('After launch, check the Pages report in Search Console. It lists every page Google could not index and explains why.')),
   ('onpage', 'Step 4: Make Each Page Easy to Understand', P(
     'Once Google can index your pages, help it understand them. Give each page a unique title tag and meta description, one clear main heading, descriptive subheadings, and enough useful content to answer the searcher’s question. Use the words your customers search for naturally.',
     'Organise your site logically, with a page for each main service and links between related pages. Our guide on <a href="seo-for-small-businesses-sri-lanka.html">SEO for small businesses</a> covers on-page SEO in more detail.') + MID_CTA),
   ('local', 'Step 5: Add Local Signals', P(
     'If you serve customers in a particular area, create and verify a Google Business Profile, link it to your website and keep your name, address and phone number consistent everywhere. Local signals help you appear in the map results for nearby searches. See our <a href="google-business-profile-sri-lanka.html">Google Business Profile guide</a> for each step.')),
   ('links', 'Step 6: Earn Links and Mentions', P(
     'Links from other websites help Google discover your site and act as votes of confidence. Start with easy, legitimate links: your social media profiles, business directories, suppliers, partners, local associations and clients who are happy to credit you.',
     'Avoid buying links or joining link schemes. They can lead to penalties and rarely help for long. Focus on creating content and relationships that people genuinely want to link to.')),
   ('content', 'Step 7: Publish Helpful Content Regularly', P(
     'Websites that publish useful content regularly give Google more pages to index and more searches to appear for. Write articles that answer your customers’ real questions, such as prices, comparisons, how-to guides and local information. Over time, these pages bring steady visitors who are researching before they buy.')),
   ('time', 'How Long Does It Take?', table(
     ['Stage', 'Typical time'], [
      ['Discovery and first indexing', 'A few days to a few weeks'],
      ['Ranking for your business name', 'Days to weeks after indexing'],
      ['Ranking for low-competition local searches', 'A few weeks to a few months'],
      ['Ranking for competitive keywords', 'Several months of consistent work']]) + P(
     'These are only typical ranges. Speed depends on your competition, content quality, technical health and the links and mentions you earn.')),
   ('ours', 'SEO-Ready Websites by Web Development Sri Lanka', P(
     'Every website we build includes on-page SEO, a sitemap, structured data, fast hosting and Google Search Console setup, so Google can find and understand it from day one. Read <a href="how-to-choose-a-web-design-company-sri-lanka.html">how to choose a web design company</a>, see our <a href="packages.html">packages</a>, or <a href="contact.html">contact us</a>.')),
  ],
  faqs=[('Why is my new website not showing on Google?', 'Google may not have discovered or indexed it yet, or something such as a noindex tag or robots.txt rule may be blocking it. Check Search Console and submit your sitemap.'),
        ('How do I submit my website to Google?', 'Verify your site in Google Search Console, submit your sitemap and use URL Inspection to request indexing of important pages.'),
        ('How long does it take for a website to appear on Google?', 'New pages are often indexed within days to a few weeks. Ranking for competitive searches usually takes several months of consistent work.'),
        ('Do I have to pay Google to appear in search results?', 'No. Normal search results are free. You only pay if you choose to run Google Ads, which appear separately as sponsored results.')],
  rel=['seo-for-small-businesses-sri-lanka', 'google-business-profile-sri-lanka', 'website-content-writing-tips']),

 dict(slug='generative-engine-optimisation-guide', date='2026-12-13', cover='seoservice', img_alt='AI search assistant recommending a business website', eyebrow='AI Search',
  title='GEO: How to Get Your Business Recommended by AI Search',
  h1='GEO: Get Recommended by <span class="accent">AI Search</span>',
  desc='What generative engine optimisation (GEO) is and how Sri Lankan businesses can appear in ChatGPT, Google AI Overviews and Perplexity answers.',
  intro='More people now ask AI assistants questions such as “Which web design company in Sri Lanka should I use?” or “What is the best tour operator for a family trip to Sri Lanka?” instead of scrolling through search results. Generative engine optimisation (GEO) is the practice of making your business easy for these AI tools to understand, trust and recommend. Here is what it means and what you can do today.',
  key=['GEO helps AI tools such as ChatGPT, Google AI Overviews and Perplexity cite your business.',
       'Strong SEO is still the foundation: AI tools often draw on search results.',
       'Clear facts, structured data and consistent business details make you easy to understand.',
       'Mentions, reviews and genuinely helpful content build the trust AI systems look for.'],
  secs=[
   ('what', 'What Is Generative Engine Optimisation?', P(
     'Traditional SEO aims to rank your pages in a list of search results. Generative engines, such as ChatGPT search, Google AI Overviews and AI Mode, Microsoft Copilot and Perplexity, write an answer instead, often citing a few sources. GEO aims to make your business one of those sources and one of the names mentioned in the answer.',
     'The field is new and changing quickly, and no one can guarantee AI recommendations. But the principles are clear, and most of them also improve normal SEO.')),
   ('how', 'How AI Search Tools Choose Sources', P(
     'AI search tools typically search the web, read the most relevant pages and summarise them. They tend to favour content that directly answers the question, comes from sources that appear trustworthy, is clearly structured and contains specific facts. They also draw on what many different websites say about a business, such as directories, reviews and articles.') + tip('If your business is never mentioned anywhere except your own website, AI tools have little evidence to recommend you. Mentions on other trusted sites matter.')),
   ('seo', '1. Strong SEO Is the Foundation', P(
     'Many AI answers are built from pages that already rank well in search. Make sure your website is indexed, fast, mobile-friendly and well structured, with a clear page for each service. Our guides on <a href="how-to-get-website-on-google.html">getting your website on Google</a> and <a href="seo-for-small-businesses-sri-lanka.html">SEO for small businesses</a> cover these basics.')),
   ('facts', '2. Publish Clear, Quotable Facts', P(
     'AI tools need facts they can repeat confidently. Put key information in plain sentences on your website: what you do, where you are based, which areas you serve, your prices or price ranges, how long projects take and who leads the business. A short “at a glance” facts section on your About page works well.',
     'Answer common questions directly, starting with the answer and then explaining. FAQ sections are ideal for this.')),
   ('structured', '3. Use Structured Data', P(
     'Structured data (schema markup) labels information on your pages in a format machines understand: your organisation, address, phone, opening hours, services, prices, articles, authors and FAQs. It removes guesswork and helps both search engines and AI systems connect the facts about your business.')),
   ('entity', '4. Be Consistent Everywhere', P(
     'Use the same business name, address, phone number and description on your website, Google Business Profile, social media, directories and partner sites. Consistency helps AI systems recognise that all these mentions refer to the same business, which builds a clearer picture of who you are.') + MID_CTA),
   ('mentions', '5. Earn Mentions, Reviews and Citations', ul([
     'Collect genuine Google reviews from happy customers.',
     'List your business on reputable directories in your industry.',
     'Get featured in local news, industry articles and partner websites.',
     'Publish case studies with clients who are happy to be named.',
     'Answer questions helpfully in communities where your customers ask them.'])),
   ('content', '6. Show Real Expertise', P(
     'AI tools and search engines both look for content that shows real experience. Write with specific examples, real numbers, local knowledge and lessons from your own projects. Name the author and explain their experience. Generic content that repeats what everyone else says gives AI no reason to cite you.',
     'Our guide on <a href="website-content-writing-tips.html">writing website content that sells</a> explains how to make content specific and useful.')),
   ('tech', '7. Let AI Crawlers Read Your Site', P(
     'Check that your robots.txt file does not block the crawlers used by AI search tools if you want to appear in their answers. Some websites also publish an llms.txt file: a plain-text summary of the business and its most important pages, intended to help AI tools. It is a newer, informal convention, but it is quick to add and keeps your key facts in one place.')),
   ('measure', 'How to Measure GEO', P(
     'Measurement is still developing. Ask the main AI tools the questions your customers would ask and note whether your business appears. Check analytics for visits referred by AI tools, ask new customers how they found you, and track branded searches in Search Console, which often grow as AI tools mention you more.')),
   ('ours', 'GEO-Ready Websites by Web Development Sri Lanka', P(
     'We build websites with structured data, clear facts, author information, fast performance and AI-friendly files such as llms.txt as standard. To see how we apply this, look at our own <a href="about.html">About page</a>, or <a href="contact.html">contact us</a> to make your business easier for AI search to recommend.')),
  ],
  faqs=[('What is GEO?', 'Generative engine optimisation is the practice of making your business and content easy for AI search tools, such as ChatGPT, Google AI Overviews and Perplexity, to understand, trust and cite.'),
        ('Is GEO different from SEO?', 'GEO builds on SEO. Strong SEO is the foundation, and GEO adds clear facts, structured data, consistent business details and mentions across the web.'),
        ('Can you guarantee my business will appear in ChatGPT?', 'No one can guarantee AI recommendations. You can greatly improve your chances by being clear, consistent, helpful and well-mentioned online.'),
        ('What is llms.txt?', 'It is a plain-text file on your website that summarises your business and links to your most important pages, intended to help AI tools. It is an informal, emerging convention.')],
  rel=['seo-for-small-businesses-sri-lanka', 'how-to-get-website-on-google', 'google-business-profile-sri-lanka']),

 dict(slug='web-design-trends-2026', date='2026-12-14', cover='rblmarketingagency', img_alt='Modern website design trends for 2026 on laptop and phone', eyebrow='Trends',
  title='Web Design Trends for 2026: What Matters for Business',
  h1='Web Design Trends for <span class="accent">2026</span>',
  desc='The web design trends that matter for businesses in 2026: AI search, speed, mobile-first, bold typography, motion, accessibility, dark mode and trust.',
  intro='Every year brings new web design trends, but not all of them help businesses. Some make websites slower or harder to use, while others genuinely bring more customers. This guide looks at the trends shaping websites in 2026 and explains which ones are worth adopting for a Sri Lankan business, and which to approach with care.',
  key=['The most valuable trends improve speed, clarity and trust, not just looks.',
       'AI search is changing how websites need to present information.',
       'Mobile-first, accessible design is now the baseline, not a bonus.',
       'Use motion and visual effects sparingly so they never slow the site down.'],
  secs=[
   ('ai', '1. Designing for AI Search', P(
     'AI assistants and AI search summaries are changing how people find businesses. Websites now need to present clear facts, direct answers and structured information that AI tools can understand and cite, while still serving human visitors. Expect more FAQ sections, clear “at a glance” summaries and well-structured service pages. Our guide to <a href="generative-engine-optimisation-guide.html">generative engine optimisation</a> explains how.')),
   ('speed', '2. Performance as a Design Feature', P(
     'Fast websites feel more modern and trustworthy. Designers increasingly choose lighter layouts, optimised images, system-friendly fonts and less heavy code from the start. With Core Web Vitals part of Google’s page experience signals, speed is a design decision, not just a technical one. See our <a href="website-speed-optimisation.html">website speed guide</a>.')),
   ('type', '3. Bold, Expressive Typography', P(
     'Large, confident headlines and characterful fonts help brands stand out, especially on mobile where there is little room for images. The trend works best when the main message is short and clear. Body text should remain simple and highly readable.')),
   ('motion', '4. Purposeful Motion and Micro-Interactions', P(
     'Subtle animations, such as buttons that respond when tapped or content that fades in as you scroll, make websites feel polished. The key word is subtle. Heavy animation libraries, autoplay videos and constant movement slow pages down, distract visitors and can cause discomfort for some people. Always respect the “reduce motion” setting on visitors’ devices.') + tip('If an effect does not help visitors understand or act, it probably is not worth its cost in speed.')),
   ('mobile', '5. App-Like Mobile Experiences', P(
     'Mobile websites are increasingly borrowing patterns from apps: bottom navigation bars, swipeable cards, sticky call buttons and bottom-sheet menus. Some websites can also be installed on the home screen as progressive web apps. These patterns make browsing easier with one thumb, which matters when most visitors use phones.')),
   ('access', '6. Accessibility by Default', P(
     'Accessible design, with good contrast, readable text, keyboard support and clear labels, is becoming a basic expectation. It helps people with disabilities, older users and anyone browsing in bright sunlight or on a small screen. It also supports SEO, because many accessibility practices make content easier for machines to understand.') + MID_CTA),
   ('dark', '7. Dark Sections and Dark Mode', P(
     'Dark backgrounds with bright accents remain popular for technology, fashion and premium brands. Many websites mix light and dark sections to create rhythm. Full dark mode that follows the visitor’s device setting is growing, but it must be designed carefully so images, logos and text remain clear in both modes.')),
   ('trust', '8. Authenticity and Trust Signals', P(
     'Visitors and search engines are increasingly sceptical of generic content and stock imagery. Real photos of teams and work, named client reviews, case studies and clear information about who runs the business help websites stand out. Expect fewer stock photos and more genuine stories.')),
   ('personal', '9. Personalisation and Smart Features', P(
     'Websites are starting to adapt content to the visitor, such as showing the nearest branch, relevant products or the right language. AI-powered chat and search tools can help visitors find answers faster. Used well, these features save time; used badly, they become intrusive, so introduce them carefully.')),
   ('sustain', '10. Lighter, More Sustainable Websites', P(
     'Smaller pages use less data and energy. Designers are trimming unnecessary scripts, compressing media and avoiding features that add weight without value. For visitors on mobile data, which includes many Sri Lankan customers, lighter pages are also cheaper and faster to load.')),
   ('choose', 'Which Trends Should Your Business Follow?', table(
     ['Trend', 'Recommended for most businesses?'], [
      ['Designing for AI search', 'Yes, start now'],
      ['Performance and speed', 'Yes, always'],
      ['Mobile app-like patterns', 'Yes, especially for mobile-heavy audiences'],
      ['Accessibility', 'Yes, always'],
      ['Bold typography', 'Yes, with readable body text'],
      ['Heavy motion and 3D effects', 'Only if they do not slow the site'],
      ['Dark mode', 'Optional, depends on your brand']])),
   ('ours', 'Modern Websites by Web Development Sri Lanka', P(
     'We combine modern design with what actually brings customers: speed, clarity, mobile usability and SEO. See current examples in our <a href="portfolio.html">portfolio</a>, read <a href="best-website-design-examples.html">what makes the best websites work</a>, or <a href="contact.html">contact us</a> to plan your new website.')),
  ],
  faqs=[('What are the top web design trends for 2026?', 'Key trends include designing for AI search, performance-first design, bold typography, subtle motion, app-like mobile patterns, accessibility, dark sections and authentic content.'),
        ('Should I redesign my website to follow trends?', 'Only if the changes help visitors and your goals. Prioritise speed, mobile usability, clarity and trust over purely visual trends.'),
        ('Do animations slow down a website?', 'Heavy animations and videos can. Subtle, lightweight effects that respect the reduce-motion setting are usually fine.'),
        ('Is dark mode good for business websites?', 'It can suit some brands, especially in technology and fashion, but it must be designed carefully so content stays readable.')],
  rel=['best-website-design-examples', 'website-redesign-signs', 'ux-design-tips']),
]
