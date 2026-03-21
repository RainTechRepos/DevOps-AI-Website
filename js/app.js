/* ========================================
   js/app.js — Core Application JavaScript
   DevOps AI by RainTech
   Version: 2.0.0 (FR-W03)

   Handles:
   - Theme toggle (localStorage + prefers-color-scheme)
   - Mobile nav with focus trap
   - Mega-menu (hover desktop / click mobile)
   - Sticky header
   - Scroll animations (CSS view() or IntersectionObserver)
   - Staggered grid reveals
   - Smooth anchor scrolling
   - Active nav highlight
   - Lazy component loading
   - Reading progress bar
   - FAQ accordion
   ======================================== */

(function () {
  'use strict';

  /* ─────────────────────────────────────────
     THEME MANAGEMENT
     Priority: explicit localStorage > prefers-color-scheme > dark
  ───────────────────────────────────────── */
  var ThemeManager = (function () {
    var STORAGE_KEY = 'devops-ai-theme';

    function getSystemPreference() {
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
        return 'light';
      }
      return 'dark';
    }

    function getStoredTheme() {
      try {
        return localStorage.getItem(STORAGE_KEY);
      } catch (e) {
        return null;
      }
    }

    function storeTheme(theme) {
      try {
        localStorage.setItem(STORAGE_KEY, theme);
      } catch (e) { /* storage unavailable */ }
    }

    function applyTheme(theme) {
      if (theme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
      } else {
        document.documentElement.removeAttribute('data-theme');
      }
      // Update toggle button state if present
      var toggleBtn = document.querySelector('.theme-toggle');
      if (toggleBtn) {
        toggleBtn.setAttribute('aria-pressed', theme === 'light' ? 'true' : 'false');
        toggleBtn.setAttribute('aria-label', theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
      }
    }

    function resolveTheme() {
      var stored = getStoredTheme();
      if (stored === 'light' || stored === 'dark') return stored;
      return getSystemPreference();
    }

    function init() {
      // Apply immediately (before DOMContentLoaded) to prevent flash
      applyTheme(resolveTheme());

      // Listen for system preference changes
      if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', function (e) {
          // Only follow system if user hasn't made an explicit choice
          if (!getStoredTheme()) {
            applyTheme(e.matches ? 'light' : 'dark');
          }
        });
      }
    }

    function toggle() {
      var current = document.documentElement.getAttribute('data-theme');
      var next = current === 'light' ? 'dark' : 'light';
      storeTheme(next);
      applyTheme(next);
    }

    return { init: init, toggle: toggle, applyTheme: applyTheme };
  })();

  // Apply theme immediately on parse
  ThemeManager.init();

  /* ─────────────────────────────────────────
     DOM READY
  ───────────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', onReady);
  } else {
    onReady();
  }

  function onReady() {
    initThemeToggle();
    initStickyHeader();
    initMobileNav();
    initMegaMenu();
    initScrollAnimations();
    initStaggeredGrids();
    initSmoothScrolling();
    initActiveNav();
    initFaqAccordion();
    initReadingProgress();
    lazyLoadComponents();
  }

  /* ─────────────────────────────────────────
     THEME TOGGLE BUTTON
  ───────────────────────────────────────── */
  function initThemeToggle() {
    var toggleBtn = document.querySelector('.theme-toggle');
    if (!toggleBtn) return;

    // Set initial aria state
    var currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    toggleBtn.setAttribute('aria-pressed', currentTheme === 'light' ? 'true' : 'false');
    toggleBtn.setAttribute('aria-label', currentTheme === 'light' ? 'Switch to dark mode' : 'Switch to light mode');

    toggleBtn.addEventListener('click', function () {
      ThemeManager.toggle();
    });
  }

  /* ─────────────────────────────────────────
     STICKY HEADER
  ───────────────────────────────────────── */
  function initStickyHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;

    var lastScrollY = 0;
    var ticking = false;
    var SCROLL_THRESHOLD = 50;

    function updateHeader() {
      if (lastScrollY > SCROLL_THRESHOLD) {
        header.classList.add('is-scrolled');
      } else {
        header.classList.remove('is-scrolled');
      }
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      lastScrollY = window.scrollY;
      if (!ticking) {
        requestAnimationFrame(updateHeader);
        ticking = true;
      }
    }, { passive: true });

    // Initial check
    lastScrollY = window.scrollY;
    updateHeader();
  }

  /* ─────────────────────────────────────────
     MOBILE NAV — with focus trap
  ───────────────────────────────────────── */
  function initMobileNav() {
    var menuToggle = document.querySelector('.mobile-menu-toggle');
    var navLinks   = document.querySelector('.nav-links');
    var navOverlay = document.querySelector('.nav-overlay');
    if (!menuToggle || !navLinks) return;

    var isOpen = false;

    // Focusable elements selector
    var FOCUSABLE = 'a[href], button:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"])';

    function openNav() {
      isOpen = true;
      navLinks.classList.add('is-open');
      menuToggle.classList.add('is-active');
      menuToggle.setAttribute('aria-expanded', 'true');
      if (navOverlay) navOverlay.classList.add('is-visible');
      document.body.style.overflow = 'hidden';
      // Move focus into nav
      var firstFocusable = navLinks.querySelector(FOCUSABLE);
      if (firstFocusable) firstFocusable.focus();
    }

    function closeNav() {
      isOpen = false;
      navLinks.classList.remove('is-open');
      menuToggle.classList.remove('is-active');
      menuToggle.setAttribute('aria-expanded', 'false');
      if (navOverlay) navOverlay.classList.remove('is-visible');
      document.body.style.overflow = '';
      menuToggle.focus();
    }

    menuToggle.addEventListener('click', function () {
      if (isOpen) { closeNav(); } else { openNav(); }
    });

    // Close on overlay click
    if (navOverlay) {
      navOverlay.addEventListener('click', closeNav);
    }

    // Close on nav link click (mobile only)
    navLinks.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 1024 && isOpen) {
          closeNav();
        }
      });
    });

    // Escape key closes nav
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen) {
        closeNav();
      }
    });

    // Focus trap inside mobile nav
    navLinks.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || !isOpen) return;
      var focusable = Array.from(navLinks.querySelectorAll(FOCUSABLE));
      if (!focusable.length) return;
      var first = focusable[0];
      var last  = focusable[focusable.length - 1];

      if (e.shiftKey) {
        if (document.activeElement === first) {
          e.preventDefault();
          last.focus();
        }
      } else {
        if (document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    });
  }

  /* ─────────────────────────────────────────
     MEGA MENU
     - Desktop: hover with 150ms leave delay
     - Mobile: click accordion toggle
     - Outside click closes all
  ───────────────────────────────────────── */
  function initMegaMenu() {
    var navItems = document.querySelectorAll('.nav-item');
    if (!navItems.length) return;

    function closeAll() {
      navItems.forEach(function (n) { n.classList.remove('is-open'); });
    }

    navItems.forEach(function (item) {
      var link = item.querySelector('.nav-link');
      var menu = item.querySelector('.mega-menu');
      if (!link || !menu) return;

      var hoverTimeout;

      // Desktop: hover
      item.addEventListener('mouseenter', function () {
        if (window.innerWidth > 1024) {
          clearTimeout(hoverTimeout);
          closeAll();
          item.classList.add('is-open');
        }
      });

      item.addEventListener('mouseleave', function () {
        if (window.innerWidth > 1024) {
          hoverTimeout = setTimeout(function () {
            item.classList.remove('is-open');
          }, 150);
        }
      });

      // Mobile: click toggle
      link.addEventListener('click', function (e) {
        if (window.innerWidth <= 1024) {
          e.preventDefault();
          var wasOpen = item.classList.contains('is-open');
          closeAll();
          if (!wasOpen) item.classList.add('is-open');
        }
      });
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-item')) {
        closeAll();
      }
    });
  }

  /* ─────────────────────────────────────────
     SCROLL ANIMATIONS
     Detects [data-animate] elements.
     Uses CSS animation-timeline: view() where supported,
     falls back to IntersectionObserver.
  ───────────────────────────────────────── */
  function initScrollAnimations() {
    var animEls = document.querySelectorAll('[data-animate], .fade-up');
    if (!animEls.length) return;

    // Feature detect CSS scroll-driven animations
    var hasScrollTimeline = (function () {
      try {
        return typeof CSS !== 'undefined' &&
               CSS.supports('animation-timeline', 'view()');
      } catch (e) {
        return false;
      }
    })();

    if (hasScrollTimeline) {
      // CSS handles it natively — just mark elements as scroll-driven
      animEls.forEach(function (el) {
        el.classList.add('scroll-driven');
      });
      return;
    }

    // Fallback: IntersectionObserver
    if (!('IntersectionObserver' in window)) {
      // No IO support: just show everything
      animEls.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '-40px 0px -40px 0px'
    });

    animEls.forEach(function (el) { observer.observe(el); });
  }

  /* ─────────────────────────────────────────
     STAGGERED GRID REVEALS
     Grid children animate in with 80ms stagger
  ───────────────────────────────────────── */
  function initStaggeredGrids() {
    var GRID_SELECTORS = [
      '.grid--cards > *',
      '.grid--zones > *',
      '.zone-grid > *',
      '.role-grid > *',
      '.stats-grid > *',
      '.features-grid > *',
      '.solutions-grid > *',
      '.industry-grid > *',
      '.platform-zones-grid > *'
    ].join(', ');

    var grids = document.querySelectorAll(
      '.grid--cards, .grid--zones, .zone-grid, .role-grid, ' +
      '.stats-grid, .features-grid, .solutions-grid, ' +
      '.industry-grid, .platform-zones-grid'
    );

    if (!grids.length || !('IntersectionObserver' in window)) return;

    grids.forEach(function (grid) {
      var children = Array.from(grid.children);
      children.forEach(function (child, i) {
        child.style.opacity = '0';
        child.style.transform = 'translateY(20px)';
        child.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        child.style.transitionDelay = (i * 80) + 'ms';
      });
    });

    var gridObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var grid = entry.target;
        if (grid.getAttribute('data-stagger-revealed')) return;
        grid.setAttribute('data-stagger-revealed', 'true');
        gridObserver.unobserve(grid);

        Array.from(grid.children).forEach(function (child) {
          child.style.opacity = '1';
          child.style.transform = 'translateY(0)';
        });
      });
    }, { threshold: 0.1 });

    grids.forEach(function (grid) { gridObserver.observe(grid); });
  }

  /* ─────────────────────────────────────────
     SMOOTH SCROLLING
     Anchor links with offset for sticky header
  ───────────────────────────────────────── */
  function initSmoothScrolling() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;

      var hash = link.getAttribute('href');
      if (!hash || hash === '#' || hash.length < 2) return;

      var target = document.querySelector(hash);
      if (!target) return;

      e.preventDefault();

      var header = document.querySelector('.site-header');
      var headerHeight = header ? header.offsetHeight : 80;
      var welcomeBar = document.querySelector('.welcome-bar');
      var welcomeHeight = welcomeBar ? welcomeBar.offsetHeight : 0;
      var offset = headerHeight + welcomeHeight + 16;

      var top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });

      if (history.replaceState) {
        history.replaceState(null, null, hash);
      }
    });
  }

  /* ─────────────────────────────────────────
     ACTIVE NAV HIGHLIGHT
  ───────────────────────────────────────── */
  function initActiveNav() {
    var currentPage = window.location.pathname.split('/').pop() || 'index.html';
    if (currentPage === '') currentPage = 'index.html';

    document.querySelectorAll('.nav-link').forEach(function (link) {
      var href = link.getAttribute('href');
      if (!href) return;
      var hrefPage = href.split('/').pop();
      if (hrefPage === currentPage) {
        link.classList.add('is-active');
        link.setAttribute('aria-current', 'page');
      }
    });
  }

  /* ─────────────────────────────────────────
     FAQ ACCORDION
     Click to expand/collapse, close siblings
  ───────────────────────────────────────── */
  function initFaqAccordion() {
    document.querySelectorAll('.faq-question').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var item   = btn.closest('.faq-item');
        var answer = item.querySelector('.faq-answer');
        if (!item || !answer) return;

        var isOpen = item.classList.contains('is-open');

        // Close siblings in the same container
        var siblings = item.parentElement
          ? item.parentElement.querySelectorAll('.faq-item')
          : [];
        siblings.forEach(function (sibling) {
          if (sibling !== item && sibling.classList.contains('is-open')) {
            sibling.classList.remove('is-open');
            var sibAnswer = sibling.querySelector('.faq-answer');
            if (sibAnswer) sibAnswer.style.maxHeight = '0';
            var sibBtn = sibling.querySelector('.faq-question');
            if (sibBtn) sibBtn.setAttribute('aria-expanded', 'false');
          }
        });

        if (isOpen) {
          item.classList.remove('is-open');
          answer.style.maxHeight = '0';
          btn.setAttribute('aria-expanded', 'false');
        } else {
          item.classList.add('is-open');
          answer.style.maxHeight = answer.scrollHeight + 'px';
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });

    // Also support expandable cards (platform page)
    document.querySelectorAll('.expandable-header').forEach(function (header) {
      header.addEventListener('click', function () {
        var card = header.closest('.expandable-card');
        if (!card) return;
        var body   = card.querySelector('.expandable-body');
        var isOpen = card.classList.contains('is-open');

        if (isOpen) {
          body.style.maxHeight = '0';
          card.classList.remove('is-open');
          header.setAttribute('aria-expanded', 'false');
        } else {
          body.style.maxHeight = body.scrollHeight + 'px';
          card.classList.add('is-open');
          header.setAttribute('aria-expanded', 'true');
        }
      });

      header.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          header.click();
        }
      });
    });
  }

  /* ─────────────────────────────────────────
     READING PROGRESS BAR
     Only on zone/role pages
  ───────────────────────────────────────── */
  function initReadingProgress() {
    var path = window.location.pathname;
    var isDeepPage = path.indexOf('/zones/') !== -1 || path.indexOf('/roles/') !== -1;
    if (!isDeepPage) return;

    var bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-label', 'Reading progress');
    bar.setAttribute('aria-valuemin', '0');
    bar.setAttribute('aria-valuemax', '100');
    bar.setAttribute('aria-valuenow', '0');
    document.body.appendChild(bar);

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          var scrollTop  = window.scrollY;
          var docHeight  = document.documentElement.scrollHeight - window.innerHeight;
          var progress   = docHeight > 0 ? Math.round((scrollTop / docHeight) * 100) : 0;
          bar.style.width = progress + '%';
          bar.setAttribute('aria-valuenow', progress);
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  /* ─────────────────────────────────────────
     LAZY COMPONENT LOADING
     Dynamic import() based on DOM presence
  ───────────────────────────────────────── */
  function lazyLoadComponents() {
    // Counter animations — load when stat elements present
    var statEls = document.querySelectorAll('.stat-number, .stat-value, .stats-grid .stat h3');
    if (statEls.length) {
      import('./components/counter.js')
        .then(function (mod) {
          if (mod && typeof mod.initCounters === 'function') {
            mod.initCounters();
          }
        })
        .catch(function (err) {
          console.warn('[app.js] Failed to load counter.js:', err);
        });
    }

    // Lightbox — load when lightbox triggers present
    var lightboxEls = document.querySelectorAll('[data-lightbox], .screenshot');
    if (lightboxEls.length) {
      import('./components/lightbox.js')
        .then(function (mod) {
          if (mod && typeof mod.initLightbox === 'function') {
            mod.initLightbox();
          }
        })
        .catch(function (err) {
          console.warn('[app.js] Failed to load lightbox.js:', err);
        });
    }

    // Chatbot
    if (document.querySelector('#chatbot-container')) {
      import('./components/chatbot.js').catch(function () {});
    }

    // Demo
    if (document.querySelector('.demo-container')) {
      import('./components/demo.js').catch(function () {});
    }

    // ROI Calculator
    if (document.querySelector('.roi-calculator')) {
      import('./components/roi-calculator.js')
        .then(function (mod) {
          if (mod && typeof mod.initROICalculator === 'function') {
            mod.initROICalculator();
          }
        })
        .catch(function (err) {
          console.warn('[app.js] Failed to load roi-calculator.js:', err);
        });
    }
  }

})();
