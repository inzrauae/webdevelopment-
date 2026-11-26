// Header style on scroll
const header = document.getElementById('header');
const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 20);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const toggle = document.getElementById('menuToggle');
const nav = document.getElementById('nav');
toggle.addEventListener('click', () => {
  nav.classList.toggle('open');
  toggle.classList.toggle('open');
});
nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  nav.classList.remove('open');
  toggle.classList.remove('open');
}));

// Count-up numbers
const runCounter = el => {
  const target = +el.dataset.target;
  const start = performance.now();
  const step = now => {
    const p = Math.min((now - start) / 1400, 1);
    el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
};

// Reveal on scroll
document.querySelectorAll('.section-head, .feature, .pf-card, .steps li, .how-visual, .price, .t-card, .cta, .stats > div, .svc-row, .proc, .ind-grid li, .cmp-wrap, .faq details, .info-card, .form-card, .about-text')
  .forEach((el, i) => {
    el.classList.add('reveal');
    el.style.transitionDelay = `${(i % 3) * 80}ms`;
  });

const io = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('visible');
    entry.target.querySelectorAll('.count').forEach(runCounter);
    io.unobserve(entry.target);
  });
}, { threshold: 0, rootMargin: '0px 0px -60px 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// Portfolio: filters + view all
const pfGrid = document.getElementById('pfGrid');
const pfMore = document.getElementById('pfMore');
if (pfGrid) {
  const cards = [...pfGrid.querySelectorAll('.pf-card')];
  document.querySelectorAll('.pf-filters button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.pf-filters button').forEach(b => b.classList.toggle('on', b === btn));
      const f = btn.dataset.filter;
      cards.forEach(c => {
        const match = f === 'all' || c.dataset.cat === f;
        c.classList.toggle('hide', !match);
        if (f !== 'all') c.classList.add('show');
        c.classList.add('visible');
      });
      if (pfMore) pfMore.classList.toggle('hidden', f !== 'all' || cards.every(c => !c.classList.contains('more') || c.classList.contains('show')));
    });
  });
  if (pfMore) pfMore.addEventListener('click', () => {
    cards.forEach(c => c.classList.add('show', 'visible'));
    pfMore.classList.add('hidden');
  });
}

// Contact form: send the enquiry via WhatsApp or email (no server needed)
const form = document.getElementById('quoteForm');
if (form) {
  const WA = '94779604714', EMAIL = 'admin@webdevelopment.lk';
  const err = document.getElementById('formError');
  const svc = new URLSearchParams(location.search).get('service');
  if (svc && form.service.querySelector(`option[value="${svc}"]`)) form.service.value = svc;

  const build = () => {
    let ok = true;
    form.querySelectorAll('[required]').forEach(f => {
      const bad = !f.value.trim();
      f.classList.toggle('invalid', bad);
      if (bad) ok = false;
    });
    if (form.email.value && !form.email.checkValidity()) { form.email.classList.add('invalid'); ok = false; }
    if (!ok) { err.textContent = 'Please fill in the required fields marked with *.'; return null; }
    err.textContent = '';
    const v = n => form[n].value.trim();
    const svcText = form.service.value ? form.service.selectedOptions[0].text : '';
    const opt = (label, val) => (val ? `${label}: ${val}` : null);
    return [
      'Hi Web Development Sri Lanka, I would like a website quote.', '',
      `Name: ${v('name')}`, `Phone: ${v('phone')}`,
      opt('Email', v('email')), opt('Business', v('company')),
      opt('Service', svcText), opt('Budget', v('budget')), '',
      v('message')
    ].filter(l => l !== null).join('\n');
  };
  form.addEventListener('submit', e => {
    e.preventDefault();
    const msg = build();
    if (msg) window.open(`https://wa.me/${WA}?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
  });
  document.getElementById('sendEmail').addEventListener('click', () => {
    const msg = build();
    if (msg) location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Website quote request')}&body=${encodeURIComponent(msg)}`;
  });
  form.addEventListener('input', e => { if (e.target.value.trim()) e.target.classList.remove('invalid'); });
}

// Hero: rotate real portfolio screenshots on the desktop, tablet and phone
const heroStage = document.querySelector('.stage');
if (heroStage) {
  const SLIDES = [ // [desktop, tablet, phone]
    ['ruvinara', 'lastsolution', 'gauraconstruction'],
    ['speedtech', 'officialcodex', 'dooo'],
    ['officialcodex', 'speedtech', 'goldpricetoday'],
    ['dagtech', 'gauraconstruction', 'speedtech'],
    ['possystem', 'ruvinara', 'officialcodex'],
    ['dooo', 'fadeandblade', 'ruvinara'],
    ['fadeandblade', 'dagtech', 'possystem'],
    ['gauraconstruction', 'possystem', 'fadeandblade'],
    ['goldpricetoday', 'lastsolution', 'dagtech'],
    ['lastsolution', 'gauraconstruction', 'possystem'],
    ['islandtoursceylon', 'lankatourdriver', 'tuktukceylonrides'],
    ['lankatourdriver', 'flyse', 'islandtoursceylon'],
    ['flyse', 'tuktukceylonrides', 'lankatourdriver'],
    ['tuktukceylonrides', 'islandtoursceylon', 'flyse'],
    ['themerchlist', 'mypalmfit', 'officialcodex'],
    ['mypalmfit', 'themerchlist', 'dooo'],
    ['esms', '4u', 'seoservice'],
    ['4u', 'rblmarketing', 'esms'],
    ['rblmarketing', 'rblmarketingagency', 'uphonerepair'],
    ['seoservice', 'esms', 'rblmarketing'],
    ['uphonerepair', '4u', 'rblmarketingagency']
  ];
  const screens = [
    { el: heroStage.querySelector('.mon-screen'), view: 'desktop', label: 'desktop' },
    { el: heroStage.querySelector('.tab-screen'), view: 'tablet', label: 'tablet' },
    { el: heroStage.querySelector('.mob-screen'), view: 'mobile', label: 'mobile' }
  ].filter(s => s.el);
  const src = (slug, view) => `images/portfolio/${slug}-${view}.jpg`;

  const swap = async (screen, slug) => {
    const old = screen.el.querySelector('img:last-of-type');
    if (!old || old.getAttribute('src') === src(slug, screen.view)) return;
    const img = new Image();
    img.src = src(slug, screen.view);
    img.alt = `${slug} website on ${screen.label}`;
    try { await img.decode(); } catch (e) { return; } // skip if the image fails to load
    Object.assign(img.style, {
      position: 'absolute', top: old.offsetTop + 'px', left: old.offsetLeft + 'px',
      width: old.offsetWidth + 'px', height: old.offsetHeight + 'px'
    });
    img.className = 'swap-in';
    screen.el.appendChild(img);
    requestAnimationFrame(() => requestAnimationFrame(() => img.classList.add('on')));
    setTimeout(() => { old.remove(); img.removeAttribute('style'); img.className = ''; }, 900);
  };

  // Preload upcoming slides so the fade never shows an empty screen
  const preload = i => SLIDES[i % SLIDES.length].forEach((slug, d) => { if (screens[d]) new Image().src = src(slug, screens[d].view); });

  let idx = 0, paused = false;
  heroStage.addEventListener('mouseenter', () => { paused = true; });
  heroStage.addEventListener('mouseleave', () => { paused = false; });
  preload(1);
  setInterval(() => {
    if (paused || document.hidden) return;
    idx = (idx + 1) % SLIDES.length;
    screens.forEach((s, d) => setTimeout(() => swap(s, SLIDES[idx][d]), d * 350));
    preload(idx + 1);
  }, 4000);
}

// =========================================================
// Mobile app experience
// =========================================================
const mq = window.matchMedia('(max-width: 768px)');

// Header hides while scrolling down, returns when scrolling up
let lastY = window.scrollY;
window.addEventListener('scroll', () => {
  const y = window.scrollY;
  if (mq.matches && !document.body.classList.contains('sheet-open')) {
    header.classList.toggle('hide', y > lastY && y > 140);
  } else header.classList.remove('hide');
  lastY = y;
}, { passive: true });

// Bottom-sheet menu
const sheet = document.getElementById('sheet');
const sheetBtn = document.getElementById('sheetOpen');
if (sheet && sheetBtn) {
  const panel = sheet.querySelector('.sheet-panel');
  const openSheet = () => {
    sheet.classList.add('open'); sheet.setAttribute('aria-hidden', 'false');
    sheetBtn.setAttribute('aria-expanded', 'true'); document.body.classList.add('sheet-open');
  };
  const closeSheet = () => {
    sheet.classList.remove('open'); sheet.setAttribute('aria-hidden', 'true');
    sheetBtn.setAttribute('aria-expanded', 'false'); document.body.classList.remove('sheet-open');
    panel.style.transform = '';
  };
  sheetBtn.addEventListener('click', openSheet);
  if (toggle) toggle.addEventListener('click', e => { if (mq.matches) { e.stopImmediatePropagation(); nav.classList.remove('open'); toggle.classList.remove('open'); openSheet(); } }, true);
  sheet.querySelectorAll('[data-close]').forEach(el => el.addEventListener('click', closeSheet));
  sheet.querySelectorAll('a').forEach(a => a.addEventListener('click', closeSheet));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSheet(); });
  // Swipe down to close
  let startY = null, dy = 0;
  panel.addEventListener('touchstart', e => {
    if (sheet.querySelector('.sheet-body').scrollTop > 0 && !e.target.closest('.sheet-grab, .sheet-head')) return;
    startY = e.touches[0].clientY; dy = 0; panel.style.transition = 'none';
  }, { passive: true });
  panel.addEventListener('touchmove', e => {
    if (startY === null) return;
    dy = Math.max(0, e.touches[0].clientY - startY);
    panel.style.transform = `translateY(${dy}px)`;
  }, { passive: true });
  panel.addEventListener('touchend', () => {
    if (startY === null) return;
    panel.style.transition = ''; startY = null;
    if (dy > 90) closeSheet(); else panel.style.transform = '';
  });
}

// Swipeable card rows with dot indicators (mobile)
document.querySelectorAll('.feature-grid, .t-grid:not(.pg-reviews .t-grid), .price-grid, .wt-grid, .wt-steps, .seo-grid, .value-grid, .proc-grid, .pg-index .pf-grid, .blog-grid:not(.pg-blog .blog-grid)').forEach(row => {
  const items = [...row.children];
  if (items.length < 2) return;
  row.classList.add('swipe');
  const dots = document.createElement('div');
  dots.className = 'swipe-dots';
  dots.setAttribute('aria-hidden', 'true');
  items.forEach((item, i) => {
    const d = document.createElement('button');
    d.tabIndex = -1;
    d.addEventListener('click', () => row.scrollTo({ left: item.offsetLeft - row.offsetLeft - 16, behavior: 'smooth' }));
    dots.appendChild(d);
  });
  row.after(dots);
  const mark = () => {
    const mid = row.scrollLeft + row.clientWidth / 2;
    let best = 0, dist = Infinity;
    items.forEach((it, i) => {
      const c = it.offsetLeft - row.offsetLeft + it.offsetWidth / 2;
      if (Math.abs(c - mid) < dist) { dist = Math.abs(c - mid); best = i; }
    });
    [...dots.children].forEach((d, i) => d.classList.toggle('on', i === best));
  };
  row.addEventListener('scroll', () => requestAnimationFrame(mark), { passive: true });
  mark();
  // Start the pricing row on the most popular package
  const pop = row.querySelector('.popular');
  if (pop && mq.matches) requestAnimationFrame(() => { row.scrollLeft = pop.offsetLeft - row.offsetLeft - (row.clientWidth - pop.offsetWidth) / 2; mark(); });
});

// Article table of contents: collapsed on phones
document.querySelectorAll('details.art-toc').forEach(d => {
  if (mq.matches) d.removeAttribute('open');
  d.querySelector('summary').addEventListener('click', e => { if (!mq.matches) e.preventDefault(); });
  d.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { if (mq.matches) d.removeAttribute('open'); }));
});

// Installable app + offline support (only works when served over http/https)
if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
}
