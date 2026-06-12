/* ─────────────────────────────────────────
   DE CARLI – Main JavaScript
   ───────────────────────────────────────── */

// ─── Nav scroll ───
const nav = document.querySelector('.nav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  });
}

// ─── Mobile menu ───
const hamburger = document.querySelector('.nav-hamburger');
const mobileMenu = document.querySelector('.nav-mobile');
const mobileClose = document.querySelector('.nav-mobile-close');
if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => mobileMenu.classList.add('open'));
  mobileClose?.addEventListener('click', () => mobileMenu.classList.remove('open'));
  mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobileMenu.classList.remove('open')));
}

// ─── Hero slider ───
function initHeroSlider() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots   = document.querySelectorAll('.hero-dot');
  if (!slides.length) return;

  let current = 0;
  let timer;

  function goTo(index) {
    slides[current].classList.remove('active');
    dots[current]?.classList.remove('active');
    current = (index + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current]?.classList.add('active');
  }

  function next() { goTo(current + 1); }

  timer = setInterval(next, 6000);

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      clearInterval(timer);
      goTo(i);
      timer = setInterval(next, 6000);
    });
  });
}
initHeroSlider();

// ─── Reveal on scroll ───
function initReveal() {
  const els = document.querySelectorAll('.reveal');
  if (!els.length) return;
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(el => obs.observe(el));
}
initReveal();

// ─── Tabs ───
function initTabs() {
  const tabBtns   = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');
  if (!tabBtns.length) return;
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanels.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(target)?.classList.add('active');
    });
  });
}
initTabs();

// ─── Lightbox ───
function initLightbox() {
  const lb    = document.getElementById('lightbox');
  const lbImg = document.getElementById('lightbox-img');
  if (!lb) return;

  document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.addEventListener('click', () => {
      const src = el.dataset.lightbox || el.src || el.style.backgroundImage.slice(5, -2);
      lbImg.src = src;
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  lb.querySelector('.lightbox-close')?.addEventListener('click', closeLB);
  lb.addEventListener('click', e => { if (e.target === lb) closeLB(); });

  function closeLB() {
    lb.classList.remove('open');
    document.body.style.overflow = '';
  }

  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeLB(); });
}
initLightbox();

// ─── Vídeo inline (manifesto: play customizado) ───
function initLocalVideo() {
  document.querySelectorAll('.video-inline').forEach(wrap => {
    const video = wrap.querySelector('video');
    const btn = wrap.querySelector('.video-play-overlay');
    if (!video || !btn) return;

    btn.addEventListener('click', () => {
      video.setAttribute('controls', '');
      video.play();
      wrap.classList.add('is-playing');
    });

    video.addEventListener('pause', () => {
      if (video.currentTime === 0 || video.ended) {
        wrap.classList.remove('is-playing');
        video.removeAttribute('controls');
      }
    });
  });
}
initLocalVideo();

// ─── Parallax band ───
function initParallax() {
  const bands = document.querySelectorAll('.band-bg[data-parallax]');
  if (!bands.length) return;
  window.addEventListener('scroll', () => {
    const sy = window.scrollY;
    bands.forEach(b => {
      const rect   = b.parentElement.getBoundingClientRect();
      const offset = (rect.top + rect.height / 2) * 0.15;
      b.style.transform = `translateY(${offset}px)`;
    });
  }, { passive: true });
}
initParallax();

// ─── Smooth anchor ───
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ─── Active nav link ───
(function setActiveLink() {
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });
})();
