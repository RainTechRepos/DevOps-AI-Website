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
