/* ========================================
   app.js — Interactions, Scroll Animations,
   Nav, Dark Mode Toggle
   DevOps AI by RainTech
   ======================================== */

(function () {
  'use strict';

  // ---- Dark Mode Toggle ----
  var currentTheme = 'dark';

  function getPreferredTheme() {
    // Default to dark
    return currentTheme || 'dark';
  }

  function setTheme(theme) {
    currentTheme = theme;
    if (theme === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }

  // Apply theme immediately
  setTheme(getPreferredTheme());

  document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'light' ? 'dark' : 'light';
        setTheme(next);
      });
    }

    // ---- Sticky Header Scroll ----
    const header = document.querySelector('.site-header');
    if (header) {
      let lastScroll = 0;
      const scrollThreshold = 40;

      function handleScroll() {
        const scrollY = window.scrollY;
        if (scrollY > scrollThreshold) {
          header.classList.add('is-scrolled');
        } else {
          header.classList.remove('is-scrolled');
        }
        lastScroll = scrollY;
      }

      window.addEventListener('scroll', handleScroll, { passive: true });
      handleScroll();
    }

    // ---- Mobile Menu ----
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const navOverlay = document.querySelector('.nav-overlay');

    if (menuToggle && navLinks) {
      menuToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.contains('is-open');
        navLinks.classList.toggle('is-open');
        menuToggle.classList.toggle('is-active');
        if (navOverlay) navOverlay.classList.toggle('is-visible');
        menuToggle.setAttribute('aria-expanded', !isOpen);
        document.body.style.overflow = isOpen ? '' : 'hidden';
      });

      if (navOverlay) {
        navOverlay.addEventListener('click', () => {
          navLinks.classList.remove('is-open');
          menuToggle.classList.remove('is-active');
          navOverlay.classList.remove('is-visible');
          menuToggle.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        });
      }

      // Close mobile nav when a link is clicked
      navLinks.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
          if (window.innerWidth <= 1024) {
            navLinks.classList.remove('is-open');
            menuToggle.classList.remove('is-active');
            if (navOverlay) navOverlay.classList.remove('is-visible');
            menuToggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
          }
        });
      });
    }

    // ---- Scroll Fade-Up Animations ----
    const fadeEls = document.querySelectorAll('.fade-up');
    if (fadeEls.length > 0 && 'IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              observer.unobserve(entry.target);
            }
          });
        },
        {
          threshold: 0.1,
          rootMargin: '0px 0px -40px 0px',
        }
      );
      fadeEls.forEach((el) => observer.observe(el));
    }

    // ---- Expandable Cards (Platform page) ----
    document.querySelectorAll('.expandable-header').forEach((header) => {
      header.addEventListener('click', () => {
        const card = header.closest('.expandable-card');
        const body = card.querySelector('.expandable-body');
        const isOpen = card.classList.contains('is-open');

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

      // Keyboard accessibility
      header.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          header.click();
        }
      });
    });

    // ---- Contact Form (basic client-side handling) ----
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
      contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const submitBtn = contactForm.querySelector('[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sending…';
        submitBtn.disabled = true;

        // Simulate form submission
        setTimeout(() => {
          submitBtn.textContent = 'Message Sent!';
          submitBtn.style.background = 'var(--accent)';
          contactForm.reset();
          setTimeout(() => {
            submitBtn.textContent = originalText;
            submitBtn.style.background = '';
            submitBtn.disabled = false;
          }, 3000);
        }, 1000);
      });
    }

    // ---- Smooth Scroll for anchor links ----
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start',
          });
        }
      });
    });

    // ---- Active Nav Highlight ----
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link').forEach((link) => {
      const href = link.getAttribute('href');
      if (href === currentPage || (currentPage === '' && href === 'index.html')) {
        link.classList.add('is-active');
      }
    });
  });
})();

  // ---- Mega-Menu Hover/Click ----
  document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.nav-item');

    navItems.forEach(item => {
      const link = item.querySelector('.nav-link');
      const menu = item.querySelector('.mega-menu');
      if (!link || !menu) return;

      // Desktop: hover
      let hoverTimeout;
      item.addEventListener('mouseenter', () => {
        if (window.innerWidth > 1024) {
          clearTimeout(hoverTimeout);
          navItems.forEach(n => n.classList.remove('is-open'));
          item.classList.add('is-open');
        }
      });

      item.addEventListener('mouseleave', () => {
        if (window.innerWidth > 1024) {
          hoverTimeout = setTimeout(() => {
            item.classList.remove('is-open');
          }, 150);
        }
      });

      // Mobile: click toggle
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 1024 && menu) {
          e.preventDefault();
          const isOpen = item.classList.contains('is-open');
          navItems.forEach(n => n.classList.remove('is-open'));
          if (!isOpen) item.classList.add('is-open');
        }
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-item')) {
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('is-open'));
      }
    });

    // ---- FAQ Accordion ----
    document.querySelectorAll('.faq-question').forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.faq-item');
        const answer = item.querySelector('.faq-answer');
        const isOpen = item.classList.contains('is-open');

        // Close all others in same section
        item.parentElement.querySelectorAll('.faq-item').forEach(i => {
          if (i !== item) {
            i.classList.remove('is-open');
            const a = i.querySelector('.faq-answer');
            if (a) a.style.maxHeight = '0';
          }
        });

        if (isOpen) {
          item.classList.remove('is-open');
          answer.style.maxHeight = '0';
        } else {
          item.classList.add('is-open');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      });
    });

    // ---- ROI Calculator ----
    const roiForm = document.querySelector('.roi-calculator');
    if (roiForm) {
      const inputs = roiForm.querySelectorAll('input[type="number"]');
      inputs.forEach(input => {
        input.addEventListener('input', calculateROI);
      });
      calculateROI();
    }
  });

  function calculateROI() {
    const techs = parseFloat(document.getElementById('roi-technicians')?.value) || 10;
    const tickets = parseFloat(document.getElementById('roi-tickets')?.value) || 1500;
    const rate = parseFloat(document.getElementById('roi-rate')?.value) || 85;
    const clients = parseFloat(document.getElementById('roi-clients')?.value) || 50;

    // Based on market data: 30-40% ticket reduction, $180K-$275K per 50-person MSP
    const ticketReduction = 0.35; // 35% average
    const ticketsReduced = Math.round(tickets * ticketReduction);
    const avgResolutionMinutes = 25;
    const hoursSaved = Math.round((ticketsReduced * avgResolutionMinutes) / 60);
    const monthlySavings = Math.round(hoursSaved * rate);
    const annualSavings = monthlySavings * 12;
    const efficiencyGain = Math.round(ticketReduction * 100);

    const elTickets = document.getElementById('roi-result-tickets');
    const elHours = document.getElementById('roi-result-hours');
    const elSavings = document.getElementById('roi-result-savings');
    const elAnnual = document.getElementById('roi-result-annual');

    if (elTickets) elTickets.textContent = ticketsReduced.toLocaleString();
    if (elHours) elHours.textContent = hoursSaved.toLocaleString() + ' hrs';
    if (elSavings) elSavings.textContent = '$' + monthlySavings.toLocaleString();
    if (elAnnual) elAnnual.textContent = '$' + annualSavings.toLocaleString();
  }

// ---- Cookie Consent (GDPR/CCPA Compliant) ----
(function() {
  'use strict';

  function getCookie(name) {
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
  }

  function setCookie(name, value, days) {
    var d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = name + '=' + value + ';expires=' + d.toUTCString() + ';path=/;SameSite=Lax';
  }

  function showBanner() {
    var banner = document.querySelector('.cookie-banner');
    if (banner) banner.classList.add('is-visible');
  }

  function hideBanner() {
    var banner = document.querySelector('.cookie-banner');
    if (banner) banner.classList.remove('is-visible');
  }

  document.addEventListener('DOMContentLoaded', function() {
    var existingConsent = getCookie('devopsai_consent');
    if (!existingConsent) {
      setTimeout(showBanner, 1500);
    }

    var acceptBtn = document.querySelector('.cookie-btn--accept');
    var rejectBtn = document.querySelector('.cookie-btn--reject');

    if (acceptBtn) {
      acceptBtn.addEventListener('click', function() {
        setCookie('devopsai_consent', 'accepted', 365);
        hideBanner();
      });
    }

    if (rejectBtn) {
      rejectBtn.addEventListener('click', function() {
        setCookie('devopsai_consent', 'rejected', 365);
        hideBanner();
      });
    }
  });
})();
