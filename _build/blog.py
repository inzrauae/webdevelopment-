# Blog: index + guide articles targeting question / cluster keywords. Executed inside build.py.
BLOG_DATE, BLOG_DATE_TXT = '2026-11-24', '24 November 2026'

def tip(t): return f'<div class="art-tip">{ic("bolt")}<p>{t}</p></div>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def table(head, rows):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="art-table"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'
def fig(slug, cap, view='desktop'):
    return (f'<figure class="art-fig"><img src="images/portfolio/{slug}-{view}.jpg" alt="{cap}" loading="lazy" />'
            f'<figcaption>{cap}</figcaption></figure>')

def keybox(items):
    return (f'<div class="art-key"><b>{ic("check")}Key takeaways</b><ul>' +
            ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>')
MID_CTA = f'''<aside class="art-cta"><div><b>Need a professional website instead?</b><p>Our team builds fast, SEO-ready business websites from LKR 20,000. See our <a href="packages.html">web design Sri Lanka price list</a>.</p></div><a href="contact.html" class="btn btn-primary">Get a Free Quote {ARROW}</a></aside>'''

POSTS = [
 dict(slug='what-is-web-designing', img_alt='Laptop displaying website analytics on a desk', eyebrow='Web Design Basics',
  title='What Is Web Designing? A Simple Guide for Beginners &amp; Businesses',
  h1='What Is <span class="accent">Web Designing?</span>',
  desc='What is web designing? Learn what web design means, its main elements, types of web design, the tools designers use and why good web design matters for businesses in Sri Lanka.',
  intro='Web designing is the process of planning and creating how a website looks, feels and works for the people who use it. Here is a clear, jargon-free explanation of what web design includes, the skills involved and why it matters for every business.',
  key=['Web designing is planning the layout, colours, fonts, images and navigation of a website.',
       'Good web design combines how a site looks (UI) with how easy it is to use (UX).',
       'Web design and web development are different jobs, and most businesses need both.',
       'In Sri Lanka, design for mobile first: most visitors browse on smartphones.'],
  secs=[
   ('meaning', 'What Does Web Designing Mean?', P(
     '<strong>Web designing</strong> is the work of planning the layout, colours, typography, images and navigation of a website so that visitors can find what they need quickly and enjoy using it. A web designer decides where everything goes on each page, how the website adapts to phones and tablets, and how visitors move from one page to the next.',
     'Good web design is not only about looks. It combines visual design with <strong>user experience (UX)</strong>, which focuses on making the site easy to use, and with an understanding of the business goals behind the website, such as getting more calls, enquiries or online sales.',
     'Think of a website like a shop. The web designer is the person who plans the shop floor: where the entrance is, how the shelves are arranged, where the signs go and where the counter sits. A well-planned shop makes buying easy. A well-designed website does exactly the same online.')),
   ('elements', 'The Main Elements of Web Design', P('Every well-designed website is built from the same core elements:') + ul([
     '<strong>Layout:</strong> how content is arranged on the page, usually on a grid, so it looks organised and balanced.',
     '<strong>Colour:</strong> a colour palette that matches the brand and guides attention to important buttons.',
     '<strong>Typography:</strong> fonts and text sizes that are easy to read on every screen.',
     '<strong>Images and graphics:</strong> photos, icons and illustrations that explain and sell.',
     '<strong>Navigation:</strong> menus and links that help visitors find pages in one or two clicks.',
     '<strong>Responsiveness:</strong> a layout that adapts automatically to phones, tablets and desktops.',
     '<strong>Speed:</strong> optimised images and code so pages load quickly, even on mobile data.',
     '<strong>Content:</strong> clear headings and short, helpful text that answers what visitors want to know.'])),
   ('principles', 'Core Principles of Good Web Design', P(
     'Designers follow a few simple principles that make any website feel professional and easy to use:') + table(
     ['Principle', 'What it means', 'Example'], [
      ['Visual hierarchy', 'The most important things stand out first', 'A large headline and one bright "Get a Quote" button'],
      ['Consistency', 'The same styles are used on every page', 'Buttons, fonts and colours never change randomly'],
      ['White space', 'Empty space around content makes it easier to read', 'Short paragraphs with room between sections'],
      ['Contrast', 'Text and buttons are easy to see', 'Dark text on a light background'],
      ['Simplicity', 'Every element has a purpose', 'Five clear menu items instead of fifteen'],
      ['Accessibility', 'Everyone can use the site', 'Readable font sizes and image alt text']])),
   ('ui-ux', 'UI Design vs UX Design', P(
     'You will often hear the terms <strong>UI</strong> and <strong>UX</strong> in web design. <strong>UI (user interface) design</strong> is about the visual side: buttons, colours, icons, fonts and how each screen looks. <strong>UX (user experience) design</strong> is about how the website works for the visitor: whether they can find information quickly, understand what to do next and complete a task such as booking or buying without frustration.',
     'A beautiful website with poor UX still loses customers, and an easy-to-use website with poor UI looks untrustworthy. Great web design balances both.')),
   ('design-vs-development', 'Web Design vs Web Development', P(
     'People often use the two terms together, but they are different jobs. <strong>Web design</strong> is about what users see and experience: the look, layout and flow. <strong>Web development</strong> is about building it: writing the HTML, CSS, JavaScript and server code that turn a design into a working website, with features like contact forms, online payments and admin panels.') + table(
     ['', 'Web design', 'Web development'], [
      ['Focus', 'Look, layout and user experience', 'Code, features and performance'],
      ['Main tools', 'Figma, Adobe XD, Photoshop', 'HTML, CSS, JavaScript, PHP, databases'],
      ['Output', 'Page designs and prototypes', 'A working, live website'],
      ['Skills', 'Colour, typography, layout, UX', 'Programming, hosting, security']]) + P(
     'Most businesses need both. That is why a full-service <a href="about.html">web design company in Sri Lanka</a> usually offers design, development, hosting and SEO under one roof, so one team is responsible for the whole project.')),
   ('types', 'Types of Web Design', ul([
     '<strong>Responsive web design:</strong> one website that adjusts its layout to any screen size. This is the modern standard.',
     '<strong>Adaptive web design:</strong> several fixed layouts for specific screen sizes.',
     '<strong>Static websites:</strong> simple pages with fixed content, ideal for small business sites.',
     '<strong>Dynamic websites:</strong> content managed through a CMS such as WordPress, or loaded from a database.',
     '<strong>E-commerce design:</strong> online stores focused on products, checkout and payments. See our <a href="ecommerce-website-sri-lanka.html">e-commerce website guide</a>.',
     '<strong>Landing pages:</strong> single pages built for one goal, such as an advertising campaign or event.']) + MID_CTA),
   ('designer-job', 'What Does a Web Designer Do Day to Day?', P('A typical web design project includes these tasks:') + ol([
     'Meeting the client to understand the business, customers and goals.',
     'Researching competitors and collecting design inspiration.',
     'Planning the sitemap and the content for each page.',
     'Sketching wireframes, then creating full-colour designs for desktop and mobile.',
     'Presenting designs, collecting feedback and making revisions.',
     'Working with developers (or building the site themselves) and testing it before launch.'])),
   ('tools', 'Tools Web Designers Use', P(
     'Professional web designers usually create designs in <strong>Figma</strong>, <strong>Adobe XD</strong> or <strong>Photoshop</strong>, then build them with HTML, CSS and JavaScript or with a platform such as WordPress, WooCommerce or Shopify. Supporting tools include Google Fonts, icon libraries, image compressors and testing tools such as Google PageSpeed Insights.',
     'If you want to try it yourself, read our step-by-step guide on <a href="how-to-start-web-designing.html">how to start web designing</a>.')),
   ('why-it-matters', 'Why Good Web Design Matters for Businesses', P(
     'Visitors decide within seconds whether a website looks trustworthy. A slow, outdated or confusing site sends customers straight to a competitor, while a clean, fast and mobile-friendly site builds confidence and turns visitors into enquiries.',
     'Good web design also supports SEO. Clear page structure, fast loading and mobile-friendliness all help a website appear higher in Google results, which is why <a href="index.html">web design Sri Lanka</a> projects should always be planned with search in mind. Learn more in our <a href="seo-for-small-businesses-sri-lanka.html">SEO guide for small businesses</a>.',
     'Still unsure whether you need one? Read <a href="why-your-business-needs-a-website.html">why your business needs a website</a>.') +
     tip('In Sri Lanka, most people browse on smartphones. Always check how a website design looks and works on a phone before anything else.')),
   ('redesign', 'Signs Your Website Needs a New Design', ul([
     'It looks broken or hard to read on a mobile phone.',
     'Pages take more than a few seconds to load.',
     'You get visitors but very few calls, WhatsApp messages or enquiries.',
     'The design, photos or prices are several years out of date.',
     'You cannot update the content yourself.',
     'It does not appear on Google for your business name or services.']) + P(
     'If several of these sound familiar, a redesign is usually a better investment than more advertising. See our <a href="packages.html">website packages</a> to find out what a professional website costs.')),
  ],
  faqs=[('What is web designing in simple words?', 'Web designing is planning and creating how a website looks and works, including its layout, colours, fonts, images and navigation, so visitors can easily find information and take action.'),
        ('Is web designing a good career in Sri Lanka?', 'Yes. Demand for websites, online stores and digital marketing keeps growing in Sri Lanka and overseas, and web designers can work for agencies, companies or as freelancers for local and international clients.'),
        ('What is the difference between web design and web development?', 'Web design covers how a website looks and feels. Web development is writing the code that makes the design work as a real website, including features such as forms, payments and databases.'),
        ('Does web design need coding?', 'Not always. Many web designers work only in design tools such as Figma. However, knowing HTML and CSS helps designers create layouts that are realistic to build and lets them build simple websites themselves.'),
        ('What is responsive web design?', 'Responsive web design means one website automatically adjusts its layout to fit any screen, from a large desktop monitor to a small phone, so it is always easy to read and use.')]),

 dict(slug='how-to-start-web-designing', img_alt='Two people reviewing a website together on a laptop', eyebrow='Beginner Guide',
  title='How to Start Web Designing in 2026: A Step-by-Step Beginner Roadmap',
  h1='How to Start <span class="accent">Web Designing</span>',
  desc='How to start web designing from zero: the skills to learn, free tools, how to practise, build a portfolio and find your first clients in Sri Lanka. A complete beginner roadmap.',
  intro='Want to learn web designing but not sure where to begin? This step-by-step roadmap shows you how to start web designing from zero, what to learn first, which tools to use and how to build a portfolio that wins clients.',
  key=['Start with design basics, then HTML and CSS. They are the foundation of every website.',
       'Figma is free and is the most widely used web design tool today.',
       'Build real projects early. A portfolio matters more than certificates.',
       'Regular practice for 6 to 12 months is enough to become job-ready.'],
  secs=[
   ('basics', 'Step 1: Learn the Basics of Design', P(
     'Before touching code, learn the fundamentals that make any design look professional: <strong>layout and spacing</strong>, <strong>colour theory</strong>, <strong>typography</strong> and <strong>visual hierarchy</strong> (making the most important things stand out). Study websites you like and ask yourself why they work: where your eye goes first, how much white space they use and how buttons are styled.',
     'If you are completely new, start with our guide on <a href="what-is-web-designing.html">what web designing is</a>, then come back to this roadmap.')),
   ('html-css', 'Step 2: Learn HTML and CSS', P(
     'HTML gives a web page its structure (headings, paragraphs, images, links) and CSS controls how it looks (colours, fonts, spacing and layout). These two languages are the foundation of every website. Focus on modern CSS layout with <strong>Flexbox</strong> and <strong>Grid</strong>, and on <strong>responsive design</strong> with media queries so your pages work on phones.') +
     tip('Free resources such as MDN Web Docs, freeCodeCamp and W3Schools are enough to learn HTML and CSS properly. Practise every day, even for 30 minutes.')),
   ('tools', 'Step 3: Learn a Design Tool', P(
     '<strong>Figma</strong> is the most popular tool for designing websites and it is free to start. Learn frames, auto layout, components and prototyping. Many designers in Sri Lanka also use <strong>Adobe Photoshop</strong> and <strong>Adobe XD</strong>, but Figma is the industry standard for web and app design today.')),
   ('javascript', 'Step 4: Add JavaScript and a CMS', P(
     'Once you are comfortable with HTML and CSS, learn basic <strong>JavaScript</strong> to add interactivity such as menus, sliders and form validation. Then learn <strong>WordPress</strong>, which powers a large share of business websites. Knowing how to build and customise WordPress sites makes you far more employable as a beginner. Our <a href="wordpress-vs-custom-website.html">WordPress vs custom website comparison</a> explains when each is used.') + MID_CTA),
   ('seo-a11y', 'Step 5: Learn SEO and Accessibility Basics', P(
     'A website is only useful if people can find it and use it. Learn the basics of <strong>SEO</strong>: page titles, meta descriptions, one H1 per page, logical headings, descriptive image alt text, fast loading and internal links. Then learn <strong>accessibility</strong>: good colour contrast, readable font sizes, keyboard-friendly menus and labelled form fields.',
     'Designers who understand SEO and accessibility are more valuable to clients, because their websites bring in more visitors and work for everyone.')),
   ('practise', 'Step 6: Practise With Real Projects', P('The fastest way to improve is to build. Try these practice projects:') + ol([
     'Redesign the website of a local shop, restaurant or school.',
     'Build a personal portfolio website to show your work.',
     'Create a landing page for a product or event.',
     'Recreate the layout of a website you admire, then add your own improvements.',
     'Build a small online store with WooCommerce.'])),
   ('portfolio', 'Step 7: Build Your Portfolio', P(
     'Clients and employers want to see what you can do. Put your best 4 to 6 projects on a simple portfolio website. For each project explain the goal, your process and the result. Live, working websites are always more convincing than screenshots.')),
   ('clients', 'Step 8: Find Your First Clients or Job', P(
     'Start with people you know: friends, family businesses and local shops that need a website. Freelance platforms such as Fiverr and Upwork, Facebook groups and LinkedIn are also good places to find work. You can also apply for internships at a <a href="about.html">web design company in Sri Lanka</a> to learn from experienced designers and developers on real client projects.') +
     tip('Keep learning SEO basics. Clients value designers who understand how to help a website rank on Google.')),
   ('plan', 'A 6-Month Learning Plan', P('Here is a realistic plan if you can practise for about an hour a day:') + table(
     ['Month', 'Focus', 'Goal by the end of the month'], [
      ['1', 'Design basics and HTML', 'Build a simple one-page personal website'],
      ['2', 'CSS, Flexbox and Grid', 'Make your page fully responsive on phones'],
      ['3', 'Figma', 'Design a 3-page business website in Figma'],
      ['4', 'JavaScript basics', 'Add a mobile menu, slider and form validation'],
      ['5', 'WordPress and SEO basics', 'Build a WordPress site with good titles and alt text'],
      ['6', 'Portfolio and real projects', 'Publish your portfolio with 4 or more projects']])),
   ('free-tools', 'Free Tools Every Beginner Needs', ul([
     '<strong>Visual Studio Code:</strong> a free code editor for HTML, CSS and JavaScript.',
     '<strong>Figma (free plan):</strong> for designing pages and prototypes.',
     '<strong>Google Fonts:</strong> free, web-friendly fonts.',
     '<strong>Chrome DevTools:</strong> built into the browser for testing layouts and mobile views.',
     '<strong>GitHub Pages or Netlify:</strong> free hosting for practice projects and your portfolio.',
     '<strong>Google PageSpeed Insights:</strong> to check how fast your pages load.'])),
   ('mistakes', 'Common Beginner Mistakes to Avoid', ul([
     '<strong>Only watching tutorials:</strong> build something after every lesson, or you will not remember it.',
     '<strong>Ignoring mobile:</strong> always design and test the phone version.',
     '<strong>Using too many fonts and colours:</strong> stick to two fonts and a small palette.',
     '<strong>Copying designs without understanding them:</strong> learn why a layout works.',
     '<strong>Waiting until you feel "ready":</strong> start freelancing small projects early and learn as you go.'])),
   ('career-paths', 'Freelancer, Agency or In-House?', table(
     ['Path', 'Good for', 'Things to know'], [
      ['Freelancer', 'Flexible hours, choosing your own clients', 'You must find clients and manage payments yourself'],
      ['Agency job', 'Learning fast from a team on many projects', 'Deadlines and variety; great for beginners'],
      ['In-house designer', 'Working on one brand in depth', 'Stable work, but fewer types of projects']]) + P(
     'Many designers start at an agency to gain experience, then move to freelancing or senior roles.')),
  ],
  faqs=[('How long does it take to learn web designing?', 'Most beginners can learn HTML, CSS and a design tool well enough to build simple websites in 3 to 6 months of regular practice. Becoming job-ready with JavaScript and WordPress usually takes 6 to 12 months.'),
        ('Can I learn web designing for free?', 'Yes. Free resources such as MDN Web Docs, freeCodeCamp, YouTube tutorials and the free plan of Figma are enough to learn web design from scratch.'),
        ('Do I need a degree to become a web designer?', 'No. Many successful web designers are self-taught. A strong portfolio of real projects matters more to clients and employers than a degree.'),
        ('What should I learn first for web designing?', 'Learn design basics such as layout, colour and typography, together with HTML and CSS. Then learn Figma, followed by JavaScript and WordPress.'),
        ('Can I learn web designing on a phone?', 'You can read tutorials and watch lessons on a phone, but you need a laptop or desktop computer to practise coding and use design tools properly.'),
        ('How do I do web designing as a freelancer?', 'Build a portfolio with 4 to 6 projects, set clear prices, start with local businesses you know, and create profiles on platforms such as Fiverr, Upwork and LinkedIn.')]),

 dict(slug='how-to-create-a-web-design', img_alt='Designer planning interface layouts with wireframe sketches', eyebrow='Step-by-Step',
  title='How to Create a Web Design: 8 Steps From Idea to Web Page Design',
  h1='How to Create a <span class="accent">Web Design</span>',
  desc='How to create a web design step by step: planning, sitemap, wireframes, web page design in Figma or Photoshop, responsive layouts, testing and launch. Practical guide with tips.',
  intro='Creating a website design is easier when you follow a clear process. These 8 steps are the same process professional designers use to go from a blank page to a finished, responsive web page design.',
  key=['Define the goal and audience before designing anything.',
       'Go from sitemap, to wireframe, to full design. Fix the structure first.',
       'Design desktop (1440px) and mobile (390px) versions of every page.',
       'Test speed, links, forms and real phones before launch.'],
  secs=[
   ('goals', '1. Define the Goal and Audience', P(
     'Every good web design starts with two questions: <strong>who is this website for</strong>, and <strong>what should visitors do</strong>? A restaurant wants table bookings, a shop wants online orders and a service company wants enquiries. Write down the main goal, the target customers and the key messages before you design anything.',
     'It also helps to look at 3 to 5 competitor websites. Note what they do well, what is missing and how your website can be clearer, faster or more helpful.')),
   ('sitemap', '2. Plan the Sitemap and Content', P(
     'List all the pages the website needs, for example Home, Services, Portfolio, Packages, About and Contact, and how they connect. Then plan the content for each page: headings, text, images and calls to action. Designing with real content gives far better results than using placeholder text.')),
   ('wireframe', '3. Sketch Wireframes', P(
     'A wireframe is a simple black-and-white layout that shows where each element goes on the page, without colours or images. Sketch on paper or use Figma to quickly try different layouts for the header, hero section, content blocks and footer. Fix the structure first, then make it beautiful.')),
   ('anatomy', 'The Anatomy of a Good Home Page', P('Most effective home pages follow a similar structure from top to bottom:') + ol([
     '<strong>Header:</strong> logo, a short menu and a clear contact button.',
     '<strong>Hero section:</strong> a headline that says what you do, a short sub-heading and one main call to action.',
     '<strong>Trust bar:</strong> client logos, review stars or key numbers.',
     '<strong>Services or products:</strong> short cards that link to detailed pages.',
     '<strong>Proof:</strong> portfolio examples, case studies and testimonials.',
     '<strong>How it works:</strong> 3 or 4 simple steps that remove uncertainty.',
     '<strong>FAQ:</strong> answers to the questions customers ask most.',
     '<strong>Final call to action and footer:</strong> contact details, map, social links and important pages.'])),
   ('style', '4. Choose Colours, Fonts and Style', P(
     'Pick a colour palette of one main brand colour, one accent colour and neutral greys. Choose one or two readable fonts from Google Fonts, for example one for headings and one for body text. Collect a mood board of websites and images you like to keep the style consistent across every page.')),
   ('mockup', '5. Design the Web Page in Figma or Photoshop', P(
     'Now turn your wireframe into a full-colour <strong>web page design</strong>. In <strong>Figma</strong>, create a desktop frame (1440px wide) and a mobile frame (390px wide), use a 12-column grid and build reusable components for buttons and cards.',
     'If you prefer <strong>Photoshop</strong>, start a new document 1440px wide, add guides for a 12-column grid, use separate layer groups for each section and save colours and text styles in libraries. Photoshop is great for image-heavy designs, while Figma is better for collaboration and prototypes.') + MID_CTA),
   ('tool-compare', 'Figma vs Photoshop vs Adobe XD', table(
     ['Tool', 'Best for', 'Price', 'Notes'], [
      ['Figma', 'Websites, apps and teamwork', 'Free plan available', 'Runs in the browser, easy sharing and prototypes'],
      ['Photoshop', 'Photo editing and image-heavy layouts', 'Paid subscription', 'Powerful for images; slower for full page layouts'],
      ['Adobe XD', 'Simple web and app prototypes', 'Paid / legacy', 'No longer actively developed by Adobe; most designers have moved to Figma']]) +
     tip('Whatever tool you use, name your layers and sections clearly. It saves hours when the design is handed to a developer.')),
   ('photoshop-steps', 'How to Design a Web Page in Photoshop (Quick Method)', ol([
     'Create a new document 1440px wide (the height can grow), RGB colour, 72 PPI.',
     'Add a 12-column grid with View &gt; Guides &gt; New Guide Layout (for example 1200px content width and 24px gutters).',
     'Create a layer group for each section: header, hero, services, testimonials, footer.',
     'Use shapes for buttons and cards, and keep text as live type layers.',
     'Save your brand colours as swatches and your text styles as character styles.',
     'Create a separate 390px-wide document for the mobile version.',
     'Export images with File &gt; Export &gt; Export As in WebP or JPG, and share the PSD with your developer.'])),
   ('responsive', '6. Make It Responsive', P(
     'Design how each section rearranges on tablets and phones: columns stack, images resize, text sizes adjust and the menu becomes a tap-friendly button. With most visitors on mobile, the phone version is often the most important design of all.') + table(
     ['Item', 'Recommended size'], [
      ['Desktop design width', '1440px (content area about 1200px)'],
      ['Tablet design width', '768px'],
      ['Mobile design width', '390px'],
      ['Body text', '16px to 18px'],
      ['Buttons and tap targets', 'At least 44px tall'],
      ['Line length', 'About 60 to 80 characters']])),
   ('build', '7. Build and Test the Website', P(
     'Turn the design into a working website with HTML, CSS and JavaScript or a CMS such as WordPress (see <a href="wordpress-vs-custom-website.html">WordPress vs custom website</a>). Then test everything: page speed on mobile, every link and form, different browsers, and real Android and iPhone devices. Check SEO basics such as page titles, meta descriptions, headings and image alt text.')),
   ('launch', '8. Launch and Improve', P(
     'Connect your domain, install an SSL certificate, submit the sitemap to Google Search Console and set up Google Analytics. After launch, watch how visitors use the site and keep improving the design and content based on real data.') +
     tip('Short on time? A professional <a href="index.html">web design Sri Lanka</a> team can take your idea through all 8 steps in a few weeks.')),
   ('mistakes', 'Common Web Design Mistakes to Avoid', ul([
     '<strong>Too much text and no headings:</strong> visitors scan pages, so break text into short sections.',
     '<strong>Huge, uncompressed images:</strong> they make pages slow, especially on mobile data.',
     '<strong>Many competing buttons:</strong> give each section one clear call to action.',
     '<strong>Low contrast text:</strong> light grey on white is hard to read outdoors on a phone.',
     '<strong>Hidden contact details:</strong> phone, WhatsApp and location should be easy to find.',
     '<strong>Designing only for desktop:</strong> always design the mobile version too.']) + P(
     'For real examples of these ideas in action, see our list of the <a href="best-website-design-examples.html">best website design examples</a>.')),
  ],
  faqs=[('What is the best software to create a web design?', 'Figma is the most popular tool for creating web designs today because it is free to start, works in the browser and makes prototyping and teamwork easy. Adobe Photoshop and Adobe XD are also widely used.'),
        ('How do I design a web page in Photoshop?', 'Create a 1440px-wide document, add guides for a 12-column grid, design each section in its own layer group, use consistent text and colour styles, then export images and hand the design over for development.'),
        ('Can I create a website design without coding?', 'Yes. You can design in Figma without code and build with no-code platforms or WordPress page builders, although coding skills give you more control over speed and SEO.'),
        ('What size should a web page design be?', 'Design desktop pages at 1440px wide with a content area of about 1200px, and design mobile pages at about 390px wide. The height depends on your content.'),
        ('How long does it take to create a web design?', 'A simple 5-page website design usually takes 1 to 2 weeks. Larger business websites and online stores can take 3 to 6 weeks, including revisions and development.')]),

 dict(slug='best-website-design-examples', img_alt='Website layouts displayed across a desktop monitor, tablet and phone', eyebrow='Inspiration',
  title='Best Website Design Examples: What Makes the Best Websites Work',
  h1='Best Website <span class="accent">Design Examples</span>',
  desc='What do the best websites have in common? Real website design examples from Sri Lanka and beyond, plus the 8 design principles behind great websites that win customers.',
  intro='The best websites are not just beautiful. They are fast, clear and built around what customers need. Here are the principles behind great website design, with real examples from projects we have designed and built.',
  key=['The best websites explain what they offer within five seconds.',
       'Speed, mobile design and clear calls to action matter more than decoration.',
       'Every industry needs different features. A hotel site and a shop site should not look the same.',
       'Use the checklist below to score your own website.'],
  secs=[
   ('principles', 'What Makes a Website One of the Best?', ol([
     '<strong>A clear message in seconds:</strong> visitors instantly understand what you offer and who it is for.',
     '<strong>Strong visual hierarchy:</strong> important content and buttons stand out.',
     '<strong>Fast loading:</strong> pages open quickly, even on mobile data.',
     '<strong>Mobile-first design:</strong> it works beautifully on phones.',
     '<strong>Easy navigation:</strong> every important page is one or two clicks away.',
     '<strong>Trust signals:</strong> real photos, reviews, contact details and a secure SSL padlock.',
     '<strong>Clear calls to action:</strong> call, WhatsApp, enquire or buy buttons are always easy to find.',
     '<strong>Search-friendly structure:</strong> proper headings, titles and content that help it rank on Google.'])),
   ('luxury', 'Example: Luxury Brand Website', P(
     '<strong>Ruvinara Gems &amp; Jewellery</strong> shows how a premium brand should look online: rich photography of Ceylon gemstones, elegant typography and generous white space that feels exclusive. Every section leads the visitor towards exploring collections and making an enquiry.',
     '<strong>Lesson:</strong> for luxury products, photography and spacing do most of the selling. Fewer words, larger images.')),
   ('ecommerce', 'Example: E-Commerce Website', P(
     '<strong>CODEX Global</strong> and <strong>dooo</strong> use bold product imagery, simple category navigation and a smooth path from product to checkout. <strong>SpeedTech</strong> shows how a technical store can stay clear and easy to browse even with many products and services.',
     '<strong>Lesson:</strong> online stores win on clarity. Clear prices, delivery details and a short checkout reduce abandoned carts.') + MID_CTA),
   ('corporate', 'Example: Corporate &amp; B2B Website', P(
     '<strong>Gaura Construction</strong>, <strong>DAG Tech Solutions</strong> and <strong>Last Solution</strong> present services, projects and products in a structured, trustworthy way, helping them win larger clients and partners.',
     '<strong>Lesson:</strong> business buyers want proof. Project galleries, certifications, client lists and detailed service pages build that confidence.')),
   ('apps', 'Example: Booking and Web App Websites', P(
     '<strong>Fade &amp; Blade</strong> makes booking a mobile barber as easy as tapping a WhatsApp button, while <strong>Gold Price Today</strong> delivers live gold prices in a clean, fast layout that people check every day. Our <strong>POS system</strong> project shows how a web app can manage sales and stock from any browser.',
     '<strong>Lesson:</strong> for tools and booking sites, speed and simplicity are the design. Remove every unnecessary step. Learn more about <a href="web-development-sri-lanka.html">custom web development in Sri Lanka</a>.')),
   ('by-industry', 'What the Best Websites Include, by Industry', table(
     ['Industry', 'Must-have features'], [
      ['<a href="hotel-website-design-sri-lanka.html">Hotels &amp; villas</a>', 'Large photo galleries, room details, direct booking form, map, reviews'],
      ['Restaurants &amp; cafés', 'Mobile menu, opening hours, location, call and order buttons'],
      ['<a href="ecommerce-website-sri-lanka.html">Online stores</a>', 'Product filters, clear prices, delivery charges, secure checkout'],
      ['Construction &amp; real estate', 'Project galleries, floor plans, locations, enquiry forms'],
      ['Schools &amp; institutes', 'Courses, fees, staff, news and an easy application form'],
      ['Clinics &amp; salons', 'Services, prices, online booking, WhatsApp and directions'],
      ['Service companies', 'Service pages, portfolio, testimonials, free-quote form']])),
   ('trends', 'Website Design Trends Worth Following in 2026', ul([
     '<strong>Bold, large typography</strong> that makes the main message impossible to miss.',
     '<strong>Bento-style grids</strong> that show many features in neat, card-based layouts.',
     '<strong>Subtle motion</strong>, such as gentle fade-ins and hover effects, used without slowing the page.',
     '<strong>Dark sections</strong> that add contrast and highlight important content.',
     '<strong>Real photography</strong> of the team, products and work, instead of generic stock photos.',
     '<strong>WhatsApp-first contact</strong>, which is especially effective for Sri Lankan customers.']) +
     tip('Follow trends only when they help your customers. A fast, clear website always beats a trendy but slow one.')),
   ('checklist', 'Score Your Website: A Quick Checklist', P('Give your website one point for each "yes":') + table(
     ['Question', 'Yes / No'], [
      ['Can a new visitor tell what you offer within 5 seconds?', '&#9744;'],
      ['Does the site load quickly on a phone using mobile data?', '&#9744;'],
      ['Is the phone or WhatsApp button visible on every page?', '&#9744;'],
      ['Are there real photos, reviews or portfolio examples?', '&#9744;'],
      ['Does every page have one clear call to action?', '&#9744;'],
      ['Does the site show a secure padlock (HTTPS)?', '&#9744;'],
      ['Does it appear on Google when you search your business name?', '&#9744;'],
      ['Can you update the content yourself?', '&#9744;']]) + P(
     '<strong>7 to 8 points:</strong> great work. <strong>4 to 6:</strong> a few improvements will bring more enquiries. <strong>0 to 3:</strong> it is time for a redesign.')),
   ('apply', 'How to Apply These Ideas to Your Website', P(
     'Start by looking at your own website on a phone. Is your offer clear within five seconds? Is it fast? Is the contact button easy to find? Small improvements in clarity, speed and trust often make a bigger difference than a complete redesign.',
     'You can see all these projects, on desktop and mobile, in our <a href="portfolio.html">web design portfolio</a>. If you want to design your own, follow our guide on <a href="how-to-create-a-web-design.html">how to create a web design</a>.') +
     tip('Collect 3 to 5 websites you love before starting your own project. They make it much easier to explain the style you want to your designer.')),
  ],
  faqs=[('What makes a website design good?', 'A good website design is clear, fast, mobile-friendly, easy to navigate and built around the customer, with strong calls to action and trust signals that turn visitors into customers.'),
        ('Where can I find website design inspiration?', 'Great sources include Awwwards, Dribbble, Behance, competitor websites and web design agency portfolios. Save examples you like and note what makes each one work.'),
        ('What are the best websites for small businesses?', 'The best small business websites are simple: a clear home page, service pages, real photos, reviews, prices or packages, and an easy way to call or WhatsApp. They load fast and work perfectly on phones.'),
        ('How often should a website be redesigned?', 'Most businesses refresh their website design every 3 to 5 years, and update content, photos and prices much more often. Redesign sooner if your site is slow or hard to use on phones.')]),

 dict(slug='how-to-choose-a-web-design-company-sri-lanka', img_alt='Creative team collaborating in a design studio', eyebrow='Buyer\'s Guide',
  title='How to Choose a Web Design Company in Sri Lanka: 12-Point Checklist',
  h1='How to Choose a <span class="accent">Web Design Company in Sri Lanka</span>',
  desc='How to choose the right web design company in Sri Lanka: 12 checks for portfolio, pricing, ownership, SEO, hosting and support, plus questions to ask and red flags to avoid.',
  intro='There are hundreds of web designers and agencies in Sri Lanka, and quotes can vary a lot. This checklist helps you compare companies fairly and choose one that delivers a website that actually brings in business.',
  key=['Judge a company by live websites, not screenshots or promises.',
       'Compare quotes line by line: pages, hosting, SSL, SEO, revisions and support.',
       'Make sure you own your domain, content and website after payment.',
       'A clear written scope and timeline prevents most problems.'],
  secs=[
   ('why', 'Why Choosing the Right Company Matters', P(
     'Your website often makes the first impression of your business. The right web design company will understand your customers, build a fast and trustworthy website, and help it appear on Google. The wrong one can leave you with a slow, outdated site, hidden costs or a website you cannot update or even access.',
     'Spending a little time comparing companies before you pay saves a lot of money and stress later. If you are still deciding whether you need a website at all, read <a href="why-your-business-needs-a-website.html">why your business needs a website</a>.')),
   ('checklist', 'The 12-Point Checklist', ol([
     '<strong>Portfolio of live websites:</strong> open their recent projects on your phone. Are they fast, modern and easy to use?',
     '<strong>Experience in your industry:</strong> or at least with similar types of websites.',
     '<strong>Clear, written pricing:</strong> a fixed quote in LKR that lists exactly what is included.',
     '<strong>Custom design:</strong> ask whether the design is custom or a ready-made template.',
     '<strong>Mobile-first approach:</strong> they should show you the phone version of every page.',
     '<strong>SEO included:</strong> titles, meta descriptions, headings, alt text, sitemap and speed.',
     '<strong>Ownership:</strong> you should own the domain, content and website after payment.',
     '<strong>Hosting and SSL:</strong> who provides them, and what renewal costs are after the first year.',
     '<strong>Content management:</strong> can you update text, photos and prices yourself?',
     '<strong>Timeline:</strong> a realistic schedule with clear milestones.',
     '<strong>Support after launch:</strong> who fixes problems, how fast, and at what cost.',
     '<strong>Reviews and references:</strong> Google reviews and past clients you can speak to.'])),
   ('questions', 'Questions to Ask Before You Hire', ul([
     'Can I see 3 live websites you built in the last year?',
     'How many pages, revisions and email accounts are included?',
     'Will the design be custom, or based on a template?',
     'Who owns the domain, hosting account and website files?',
     'What are the yearly renewal costs for hosting and the domain?',
     'What SEO work is included at launch?',
     'How long will the project take, and what do you need from me?',
     'What support is included after launch, and for how long?']) + MID_CTA),
   ('compare', 'Freelancer vs Web Design Company', table(
     ['', 'Freelancer', 'Web design company'], [
      ['Price', 'Often lower', 'Usually higher, but more included'],
      ['Skills', 'One person, may not cover design, code and SEO', 'A team covering design, development, SEO and hosting'],
      ['Speed', 'Depends on one person\'s workload', 'Can work on several parts at once'],
      ['Support', 'Can be hard to reach later', 'Ongoing support and a business you can contact'],
      ['Best for', 'Very small, simple projects', 'Business websites, online stores and web apps']])),
   ('red-flags', 'Red Flags to Watch Out For', ul([
     '<strong>Very low prices with no clear scope:</strong> extra costs often appear later.',
     '<strong>No live portfolio:</strong> only screenshots or "confidential" projects.',
     '<strong>The domain registered in their name:</strong> you may lose it if you change companies.',
     '<strong>No written quote or agreement.</strong>',
     '<strong>Promises of "number 1 on Google" in days:</strong> no honest company can guarantee rankings.',
     '<strong>Slow replies before you have paid:</strong> it rarely gets better afterwards.'])),
   ('price', 'How Much Should You Pay?', P(
     'Prices depend on the number of pages, custom design work and features such as online payments or booking systems. As a guide, our packages start at <strong>LKR 20,000</strong> for a starter business website, <strong>LKR 30,000</strong> for a business website with a CMS and blog, and <strong>LKR 39,000</strong> for an e-commerce website. See the full <a href="packages.html">web design Sri Lanka price list</a> for what each package includes.',
     'Whatever company you choose, compare what is included, not only the price. A cheap website that brings no enquiries is the most expensive option of all.')),
   ('process', 'What a Good Web Design Process Looks Like', ol([
     '<strong>Discovery call:</strong> they ask about your business, customers and goals.',
     '<strong>Written proposal:</strong> scope, timeline and fixed price.',
     '<strong>Design:</strong> you review the home page design, on desktop and mobile, before development.',
     '<strong>Development:</strong> the website is built and tested on a private link.',
     '<strong>Launch:</strong> domain, SSL, Google Search Console and analytics are set up.',
     '<strong>Support:</strong> training, backups and help with changes after launch.']) + P(
     'This is exactly how we work. Learn more <a href="about.html">about our web design company in Sri Lanka</a>, or see our <a href="portfolio.html">portfolio</a>.') +
     tip('Ask for everything in writing: pages, features, price, timeline and who owns what. It protects both you and the company.')),
  ],
  faqs=[('How do I choose a good web design company in Sri Lanka?', 'Check their live portfolio on your phone, compare written quotes line by line, confirm you will own your domain and website, make sure SEO and mobile design are included, and read their Google reviews.'),
        ('Is it better to hire a freelancer or a web design company?', 'A freelancer can be fine for very small, simple projects. For business websites, online stores and web apps, a company usually offers a wider range of skills, faster delivery and more reliable support.'),
        ('Should I own my website and domain?', 'Yes. Once the project is paid for, the domain, content and website files should belong to you, with full admin access, so you can change companies in the future if you need to.'),
        ('Can a web design company guarantee first place on Google?', 'No. Nobody controls Google rankings. A good company builds a fast, well-structured, SEO-ready website and gives honest advice on content, reviews and links that help it rank over time.')]),

 dict(slug='website-cost-in-sri-lanka', img_alt='Financial documents and a phone calculator for planning a budget', eyebrow='Pricing Guide',
  title='How Much Does a Website Cost in Sri Lanka? 2026 Price Guide',
  h1='How Much Does a <span class="accent">Website Cost in Sri Lanka?</span>',
  desc='How much does a website cost in Sri Lanka in 2026? Prices for business websites, e-commerce stores and web apps, what affects cost, yearly running costs and how to save money.',
  intro='Website prices in Sri Lanka vary widely, and it can be hard to know what is fair. This guide explains what you get at each price level, what affects the cost, which yearly costs to expect and how to get the best value.',
  key=['A professional business website starts from LKR 20,000 with us.',
       'Pages, custom design and features such as payments affect the price most.',
       'Remember yearly costs: domain renewal, hosting and maintenance.',
       'Compare what is included, not only the headline price.'],
  secs=[
   ('overview', 'Website Prices at a Glance', P(
     'Here is what our packages cost and what each one is best for. Every package includes a responsive design, on-page SEO, free SSL and first-year hosting.') + table(
     ['Website type', 'Best for', 'Typical timeline', 'Price'], [
      ['Starter business website', 'Small businesses and startups (up to 5 pages)', '1 to 2 weeks', 'LKR 20,000'],
      ['Business website', 'Growing companies that need a CMS and blog', '3 to 4 weeks', 'LKR 30,000'],
      ['E-commerce website', 'Selling products online with payments', '4 to 6 weeks', 'LKR 39,000'],
      ['Custom web application', 'Booking systems, POS, portals and SaaS', 'Depends on scope', 'Custom quote']]) + P(
     'Full details are on our <a href="packages.html">web design Sri Lanka price list</a>.')),
   ('factors', 'What Affects the Cost of a Website?', ul([
     '<strong>Number of pages:</strong> more pages mean more design, content and testing time.',
     '<strong>Custom design vs template:</strong> a design made for your brand takes more work than a ready-made theme.',
     '<strong>Features:</strong> online payments, booking systems, multi-language content, member logins and integrations add cost (see our <a href="ecommerce-website-sri-lanka.html">e-commerce</a> and <a href="web-development-sri-lanka.html">web development</a> guides).',
     '<strong>Content:</strong> whether you supply text and photos, or need copywriting and photography.',
     '<strong>E-commerce size:</strong> the number of products, categories and delivery options.',
     '<strong>SEO and marketing:</strong> basic on-page SEO is included; ongoing SEO campaigns are extra.',
     '<strong>Deadline:</strong> urgent projects may need extra resources.'])),
   ('yearly', 'Yearly Running Costs to Plan For', P(
     'A website is not only a one-time cost. Plan for these ongoing costs each year:') + table(
     ['Cost', 'What it is', 'Notes'], [
      ['Domain name', 'Your web address (.lk or .com)', 'Renewed every year; .lk domains usually cost more than .com'],
      ['Hosting', 'The server that stores your website', 'First year included with our packages'],
      ['SSL certificate', 'The secure padlock (HTTPS)', 'Free SSL included'],
      ['Maintenance', 'Updates, backups and small changes', 'Optional monthly or yearly plan'],
      ['Payment gateway fees', 'For online stores taking card payments', 'A small percentage per transaction, charged by the payment provider']]) + MID_CTA),
   ('cheap', 'Is a Cheap Website Worth It?', P(
     'Very cheap websites are often built from a basic template with little care for speed, SEO or mobile design. They may look acceptable at first, but they rarely bring in enquiries, and you may need to pay again for a proper website later.',
     'On the other hand, a higher price does not always mean better quality. The best value comes from a company that shows live work, explains exactly what is included and builds the website around your customers. Read our guide on <a href="how-to-choose-a-web-design-company-sri-lanka.html">how to choose a web design company in Sri Lanka</a> before you decide.')),
   ('save', 'How to Save Money on Your Website', ol([
     'Prepare your text, logo and photos before the project starts.',
     'Start with the pages you really need, and add more later.',
     'Choose the right platform for your needs (read <a href="wordpress-vs-custom-website.html">WordPress vs custom website</a>).',
     'Choose a package with a CMS so you can update content yourself.',
     'Collect 3 to 5 example websites you like to speed up design decisions.',
     'Give clear, combined feedback in one message instead of many small changes.',
     'Ask what is included up front to avoid paying for extras later.'])),
   ('roi', 'Think of It as an Investment', P(
     'A good website works for your business 24 hours a day. If it brings in even a few extra customers each month, it usually pays for itself quickly. That is why it is worth choosing a website that is fast, mobile-friendly and built to appear on Google, rather than simply the cheapest option.') +
     tip('Ask for a free quote. You will get a fixed price in LKR with the exact scope, timeline and what is included, before you commit to anything.')),
  ],
  faqs=[('How much does a website cost in Sri Lanka?', 'With Web Development Sri Lanka, a starter business website costs LKR 20,000, a business website with a CMS and blog costs LKR 30,000, and an e-commerce website costs LKR 39,000. Custom web applications are quoted based on the features you need.'),
        ('What is included in the website price?', 'All our packages include a responsive design, on-page SEO setup, free SSL, first-year hosting and support after launch. The number of pages and features depends on the package.'),
        ('Are there yearly costs after the website is built?', 'Yes. Expect yearly domain renewal and hosting from the second year, plus optional maintenance. Online stores may also pay transaction fees to their payment provider.'),
        ('How long does it take to build a website?', 'A starter website usually takes 1 to 2 weeks, a business website 3 to 4 weeks and an e-commerce website 4 to 6 weeks, depending on how quickly content and feedback are provided.')]),
]
exec(io.open(f'{S}/blog_more.py', encoding='utf-8').read())

# ---- Scheduled posts: _build/posts/*.py, each post has date='YYYY-MM-DD' and goes live on that day
import glob as _glob, os as _os
from datetime import datetime as _dt, timezone as _tz, timedelta as _td
EXTRA = {}  # slug -> extra sections, inserted before the closing section
for _f in sorted(_glob.glob(f'{S}/posts/*.py')):
    exec(io.open(_f, encoding='utf-8').read())
for _p in POSTS:
    if _p['slug'] in EXTRA: _p['secs'] = _p['secs'][:-1] + EXTRA[_p['slug']] + _p['secs'][-1:]
TODAY = _os.environ.get('PUBLISH_DATE') or _dt.now(_tz(_td(hours=5, minutes=30))).date().isoformat()
ALL_SLUGS = {p['slug'] for p in POSTS}
POSTS = [p for p in POSTS if p.get('date', BLOG_DATE) <= TODAY]
LIVE = {p['slug'] for p in POSTS}
_HIDDEN = ALL_SLUGS - LIVE
for _s in _HIDDEN:  # never leave a not-yet-published post online from an earlier build
    if _os.path.exists(f'{ROOT}/{_s}.html'): _os.remove(f'{ROOT}/{_s}.html')

def _unlink_future(h):
    # A link to a post that is not published yet becomes plain text until that post goes live
    for s in _HIDDEN:
        h = re.sub(r'<a href="' + re.escape(s) + r'\.html(?:#[^"]*)?"[^>]*>(.*?)</a>', r'\1', h)
    return h

def _date_txt(d):
    y, m, dd = d.split('-')
    return f"{int(dd)} {['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {y}"

for p in POSTS:
    p['secs'] = [(a, h, _unlink_future(x)) for a, h, x in p['secs']]
    p['rel'] = [s for s in p.get('rel', []) if s in LIVE]
    p.setdefault('date', BLOG_DATE)
LATEST = sorted(POSTS, key=lambda p: p['date'], reverse=True)
PAGE_DATE = {f"{p['slug']}.html": p['date'] for p in POSTS}
if LATEST: PAGE_DATE['blog.html'] = LATEST[0]['date']

for p in POSTS:
    words = len(re.sub(r'<[^>]+>', ' ', ''.join(h for _, _, h in p['secs'])).split())
    p['mins'] = max(4, round(words / 200))

def post_card(p):
    return f'''      <article class="blog-card">
        <a href="{p['slug']}.html" class="blog-thumb"><img src="images/blog/{p['slug']}.webp" alt="{p['img_alt']}" width="1200" height="675" loading="lazy" decoding="async" /><span>{p['eyebrow']}</span></a>
        <div class="blog-body">
          <small>{ic('clock')}{p['mins']} min read</small>
          <h3><a href="{p['slug']}.html">{p['title']}</a></h3>
          <p>{p['desc']}</p>
          <a href="{p['slug']}.html" class="text-link">Read article {ARROW}</a>
        </div>
      </article>'''

SEO_TITLES = {
    'seo-for-small-businesses-sri-lanka': 'SEO for Small Businesses in Sri Lanka: Practical Guide',
    'why-your-business-needs-a-website': 'Why Your Business Needs a Website in Sri Lanka',
    'web-development-sri-lanka': 'Web Development in Sri Lanka: Web Apps, POS &amp; Booking',
    'hotel-website-design-sri-lanka': 'Hotel &amp; Villa Website Design Sri Lanka | Direct Bookings',
    'ecommerce-website-sri-lanka': 'E-Commerce Website in Sri Lanka: Payments &amp; Setup Guide',
    'what-is-web-designing': 'What Is Web Designing? A Simple Guide for Beginners',
    'how-to-start-web-designing': 'How to Start Web Designing in 2026: Beginner Roadmap',
    'how-to-choose-a-web-design-company-sri-lanka': 'How to Choose a Web Design Company in Sri Lanka',
    'how-to-create-a-web-design': 'How to Create a Web Design: 8 Steps From Idea to Page',
    'best-website-design-examples': 'Best Website Design Examples &amp; What Makes Them Work',
    'wordpress-vs-custom-website': 'WordPress vs Custom Website: Which Is Right for You?',
}
AUTHOR = {'@type': 'Person', 'name': 'Buddhika S Weerasekara'}
if SITE: AUTHOR.update({'@id': f'{SITE}/#founder', 'url': f'{SITE}/about.html'})
PUBLISHER = {'@type': 'Organization', 'name': 'Web Development Sri Lanka'}
if SITE: PUBLISHER.update({'@id': f'{SITE}/#business', 'logo': {'@type': 'ImageObject', 'url': f'{SITE}/images/icon-512.png'}})

for i, p in enumerate(POSTS):
    toc = ''.join(f'<li><a href="#{sid}">{h}</a></li>' for sid, h, _ in p['secs'])
    body = ''.join(f'<h2 id="{sid}">{h}</h2>{html}' for sid, h, html in p['secs'])
    BY = {q['slug']: q for q in POSTS}
    related = [BY[s] for s in p.get('rel', [])][:3]
    for q in LATEST:
        if len(related) >= 3: break
        if q is not p and q not in related: related.append(q)
    art_ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': plain(p['title']), 'description': plain(p['desc']),
              'datePublished': p['date'], 'dateModified': p['date'], 'author': AUTHOR, 'publisher': PUBLISHER, 'inLanguage': 'en-LK',
              'about': plain(p['eyebrow']), 'wordCount': len(re.sub(r'<[^>]+>', ' ', ''.join(h for _, _, h in p['secs'])).split())}
    if SITE: art_ld.update({'image': f"{SITE}/images/blog/{p['slug']}.webp", 'mainEntityOfPage': f"{SITE}/{p['slug']}.html"})
    page(f"{p['slug']}.html", SEO_TITLES.get(p['slug'], p.get('seo_title', p['title'])), p['desc'],
         page_hero(p['eyebrow'], p['h1'], p['intro'], 'Blog', [('clock', f"{p['mins']} min read", 'Guide'), ('award', 'Expert tips', 'By our team')]) +
         f'''<section class="section article-wrap">
  <div class="container article-grid">
    <article class="article">
      <div class="art-meta"><span>{ic('users')}By <a href="about.html" rel="author">Buddhika S Weerasekara</a></span><span>{ic('clock')}{p['mins']} min read</span><span>{'Published' if p['date'] != BLOG_DATE else 'Updated'} {_date_txt(p['date'])}</span></div>
      <figure class="art-cover"><img src="images/blog/{p['slug']}.webp" alt="{p['img_alt']}" width="1200" height="675" decoding="async" /></figure>
      {keybox(p['key'])}
      {body}
      <h2 id="faq">Frequently Asked Questions</h2>
      {faq_list(p['faqs'])}
    </article>
    <aside class="art-side">
      <details class="art-toc" open><summary><b>In this article</b>{ic("chev", "chev")}</summary><ol>{toc}<li><a href="#faq">FAQs</a></li></ol></details>
      <div class="art-promo">
        <span class="wd-kicker light">{ic('rocket')}Web Development Sri Lanka</span>
        <b>Get a professional website from LKR 20,000</b>
        <p>Mobile-friendly, SEO-ready and built by a local team.</p>
        <a href="contact.html" class="btn btn-primary btn-sm">Get a Free Quote {ARROW}</a>
      </div>
    </aside>
  </div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Keep Reading</span><h2>More Web Design <span class="accent">Guides</span></h2></div>
    <div class="blog-grid">
{chr(10).join(post_card(q) for q in related)}
    </div>
  </div>
</section>
''' + CTA, 'blog.html', faqs=p['faqs'], crumb='Blog', ld_extra=[art_ld], og_type='article', og_img=f"images/blog/{p['slug']}.webp")

page('blog.html', 'Web Design Blog: Guides &amp; Tips | Web Development Sri Lanka',
     'Web design blog from a web design company in Sri Lanka: guides on web designing, website costs, e-commerce, SEO, hotel websites, WordPress and web development.',
     page_hero('Blog', 'Web Design <span class="accent">Guides &amp; Tips</span>',
               'Practical articles on web designing, website planning, pricing, SEO and growing your business online, written by the Web Development Sri Lanka team.',
               'Blog', [('edu', 'Free Guides', 'Beginner friendly'), ('trend', 'SEO Tips', 'Rank higher')]) +
     f'''<section class="section">
  <div class="container">
    <div class="blog-grid">
{chr(10).join(post_card(q) for q in LATEST)}
    </div>
  </div>
</section>
''' + CTA, crumb='Blog')
