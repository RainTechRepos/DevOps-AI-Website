/* ========================================
   enhancements.js — Interactive Visual Enhancements
   DevOps AI by RainTech
   
   - Animated stat counters
   - Staggered scroll reveals for grids
   - Card hover micro-interactions (via CSS)
   - Smooth header transitions
   - Lightbox gallery navigation (keyboard)
   ======================================== */

(function() {
  'use strict';

  // ─── Animated Stat Counters ───
  // Counts up from 0 to the displayed number when the stat scrolls into view
  function initStatCounters() {
    var statEls = document.querySelectorAll('.stat-number, .stat-value, .stats-grid .stat h3');
    if (!statEls.length || !('IntersectionObserver' in window)) return;

    statEls.forEach(function(el) {
      el.setAttribute('data-target', el.textContent.trim());
      // Don't reset text yet — only animate when visible
    });

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        if (el.getAttribute('data-counted')) return;
        el.setAttribute('data-counted', 'true');
        observer.unobserve(el);
        animateCounter(el);
      });
    }, { threshold: 0.3 });

    statEls.forEach(function(el) { observer.observe(el); });
  }

  function animateCounter(el) {
    var raw = el.getAttribute('data-target') || '';
    // Extract numeric part: "720K+" → 720, "<35" → 35, "113" → 113
    var prefix = '';
    var suffix = '';
    var numStr = raw;
    
    // Handle prefixes like < > ~
    var prefixMatch = numStr.match(/^([<>~≈])/);
    if (prefixMatch) {
      prefix = prefixMatch[1];
      numStr = numStr.substring(1);
    }

    // Handle suffixes like K+, +, %, etc.
    var suffixMatch = numStr.match(/([KkMm%+]+.*)$/);
    if (suffixMatch) {
      suffix = suffixMatch[1];
      numStr = numStr.replace(suffixMatch[0], '');
    }

    var target = parseFloat(numStr.replace(/,/g, ''));
    if (isNaN(target)) return;

    var duration = 1500; // ms
    var start = performance.now();
    var isInteger = target === Math.floor(target);

    function step(now) {
      var elapsed = now - start;
      var progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = eased * target;
      
      if (isInteger) {
        el.textContent = prefix + Math.floor(current).toLocaleString() + suffix;
      } else {
        el.textContent = prefix + current.toFixed(1) + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = raw; // Restore exact original
      }
    }

    el.textContent = prefix + '0' + suffix;
    requestAnimationFrame(step);
  }

  // ─── Staggered Grid Reveals ───
  // Grid children animate in one by one instead of all at once
  function initStaggeredReveals() {
    var grids = document.querySelectorAll(
      '.zone-grid, .role-grid, .stats-grid, .features-grid, ' +
      '.solutions-grid, .zone-card-grid, .rzc-grid, .tile-grid, ' +
      '.industry-grid, .platform-zones-grid'
    );
    if (!grids.length || !('IntersectionObserver' in window)) return;

    grids.forEach(function(grid) {
      var children = grid.children;
      for (var i = 0; i < children.length; i++) {
        children[i].style.opacity = '0';
        children[i].style.transform = 'translateY(20px)';
        children[i].style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        children[i].style.transitionDelay = (i * 80) + 'ms';
      }
    });

    var gridObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (!entry.isIntersecting) return;
        var grid = entry.target;
        if (grid.getAttribute('data-revealed')) return;
        grid.setAttribute('data-revealed', 'true');
        gridObserver.unobserve(grid);

        var children = grid.children;
        for (var i = 0; i < children.length; i++) {
          children[i].style.opacity = '1';
          children[i].style.transform = 'translateY(0)';
        }
      });
    }, { threshold: 0.1 });

    grids.forEach(function(grid) { gridObserver.observe(grid); });
  }

  // ─── Enhanced Scroll Header ───
  // Adds smooth glass effect as user scrolls
  function initScrollHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;

    var lastScroll = 0;
    var ticking = false;

    window.addEventListener('scroll', function() {
      lastScroll = window.scrollY;
      if (!ticking) {
        requestAnimationFrame(function() {
          if (lastScroll > 60) {
            header.classList.add('is-scrolled');
          } else {
            header.classList.remove('is-scrolled');
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  // ─── Lightbox Keyboard Navigation ───
  // Arrow keys navigate between lightbox images
  function initLightboxKeyboard() {
    document.addEventListener('keydown', function(e) {
      var overlay = document.querySelector('.lightbox-overlay.is-active, .lightbox-overlay.active');
      if (!overlay) return;

      if (e.key === 'Escape') {
        var closeBtn = overlay.querySelector('.lightbox-close, [class*="close"]');
        if (closeBtn) closeBtn.click();
        return;
      }

      // Find all lightbox triggers to enable prev/next
      var triggers = document.querySelectorAll('[data-lightbox], .lightbox-trigger, .pa-screenshot');
      if (triggers.length < 2) return;

      var currentSrc = overlay.querySelector('img')?.src;
      if (!currentSrc) return;

      var currentIndex = -1;
      triggers.forEach(function(t, i) {
        var src = t.getAttribute('data-lightbox-src') || t.getAttribute('href') || t.querySelector('img')?.src;
        if (src && currentSrc.includes(src.split('/').pop())) currentIndex = i;
      });

      if (currentIndex === -1) return;

      var newIndex;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        newIndex = (currentIndex + 1) % triggers.length;
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        newIndex = (currentIndex - 1 + triggers.length) % triggers.length;
      } else {
        return;
      }

      e.preventDefault();
      triggers[newIndex].click();
    });
  }

  // ─── Smooth Anchor Scrolling ───
  function initSmoothAnchors() {
    document.addEventListener('click', function(e) {
      var link = e.target.closest('a[href^="#"]');
      if (!link) return;
      
      var hash = link.getAttribute('href');
      if (hash === '#' || hash.length < 2) return;
      
      var target = document.querySelector(hash);
      if (!target) return;

      e.preventDefault();
      var headerHeight = document.querySelector('.site-header')?.offsetHeight || 80;
      var welcomeBar = document.querySelector('.welcome-bar');
      var welcomeHeight = welcomeBar ? welcomeBar.offsetHeight : 0;
      
      var top = target.getBoundingClientRect().top + window.scrollY - headerHeight - welcomeHeight - 16;
      window.scrollTo({ top: top, behavior: 'smooth' });
      
      // Update URL hash without scrolling
      if (history.replaceState) {
        history.replaceState(null, null, hash);
      }
    });
  }

  // ─── Progress indicator for long pages ───
  function initReadingProgress() {
    // Only on deep-dive pages (zone pages, PA pages)
    var path = window.location.pathname;
    if (path.indexOf('/zones/') === -1 && path.indexOf('/roles/') === -1) return;

    var bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.setAttribute('role', 'progressbar');
    bar.setAttribute('aria-label', 'Reading progress');
    document.body.appendChild(bar);

    var ticking = false;
    window.addEventListener('scroll', function() {
      if (!ticking) {
        requestAnimationFrame(function() {
          var scrollTop = window.scrollY;
          var docHeight = document.documentElement.scrollHeight - window.innerHeight;
          var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
          bar.style.width = progress + '%';
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  // ─── Boot ───
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    initStatCounters();
    initStaggeredReveals();
    initScrollHeader();
    initLightboxKeyboard();
    initSmoothAnchors();
    initReadingProgress();
  }

})();
