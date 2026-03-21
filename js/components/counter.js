/* ========================================
   js/components/counter.js — Animated Number Counter
   DevOps AI by RainTech
   Version: 2.0.0 (FR-W03)

   - Counts up from 0 to target over 1500ms
   - Triggered by IntersectionObserver (threshold 0.3)
   - Handles prefixes (< > ~ ≈), suffixes (K+, %, M+), decimals
   - Ease-out cubic timing
   - Tabular nums via data attribute
   - ES Module — exports initCounters()
   ======================================== */

'use strict';

/**
 * Parse a raw stat string into its component parts.
 * e.g. "<35ms"  → { prefix: "<", number: 35, suffix: "ms", isInteger: true }
 *      "720K+"  → { prefix: "",  number: 720, suffix: "K+", isInteger: true }
 *      "4.8"    → { prefix: "",  number: 4.8, suffix: "",   isInteger: false }
 *
 * @param {string} raw
 * @returns {{ prefix: string, number: number, suffix: string, isInteger: boolean, original: string } | null}
 */
function parseStatValue(raw) {
  if (!raw) return null;
  var str = raw.trim();
  var original = str;

  // Extract leading prefix symbol
  var prefix = '';
  var prefixMatch = str.match(/^([<>~≈]+)/);
  if (prefixMatch) {
    prefix = prefixMatch[1];
    str = str.slice(prefix.length);
  }

  // Extract trailing suffix (letters, symbols after the number)
  // Matches things like: K+, M+, %, ms, +, hrs, s
  var suffix = '';
  var suffixMatch = str.match(/([A-Za-z%+]+[\w%+]*)$/);
  if (suffixMatch) {
    suffix = suffixMatch[0];
    str = str.slice(0, str.length - suffix.length);
  }

  // Remove commas for parsing
  var numStr = str.replace(/,/g, '');
  var number = parseFloat(numStr);

  if (isNaN(number)) return null;

  return {
    prefix:    prefix,
    number:    number,
    suffix:    suffix,
    isInteger: number === Math.floor(number),
    original:  original
  };
}

/**
 * Ease-out cubic: starts fast, decelerates to target.
 * @param {number} t - progress 0..1
 * @returns {number}
 */
function easeOutCubic(t) {
  return 1 - Math.pow(1 - t, 3);
}

/**
 * Animate a single counter element from 0 to its target.
 * @param {Element} el
 * @param {object} parsed - result of parseStatValue()
 * @param {number} duration - ms
 */
function animateCounter(el, parsed, duration) {
  var start = null;
  var prefix    = parsed.prefix;
  var suffix    = parsed.suffix;
  var target    = parsed.number;
  var isInteger = parsed.isInteger;
  var original  = parsed.original;

  // Set tabular-nums for stable layout during counting
  el.style.fontVariantNumeric = 'tabular-nums';

  function step(timestamp) {
    if (start === null) start = timestamp;
    var elapsed  = timestamp - start;
    var progress = Math.min(elapsed / duration, 1);
    var eased    = easeOutCubic(progress);
    var current  = eased * target;

    if (isInteger) {
      el.textContent = prefix + Math.floor(current).toLocaleString() + suffix;
    } else {
      el.textContent = prefix + current.toFixed(1) + suffix;
    }

    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      // Restore exact original text
      el.textContent = original;
    }
  }

  // Start from zero
  el.textContent = prefix + '0' + suffix;
  requestAnimationFrame(step);
}

/**
 * Initialize animated stat counters.
 * Observes all matching elements and triggers animation on intersection.
 *
 * Selectors targeted:
 *   .stat-number, .stat-value, .stats-grid .stat h3
 */
export function initCounters() {
  var SELECTORS = '.stat-number, .stat-value, .stats-grid .stat h3';
  var DURATION  = 1500; // ms
  var THRESHOLD = 0.3;

  var statEls = document.querySelectorAll(SELECTORS);
  if (!statEls.length) return;

  // IntersectionObserver required — skip gracefully if unavailable
  if (!('IntersectionObserver' in window)) {
    return;
  }

  // Store original text as data-target before any mutation
  statEls.forEach(function (el) {
    if (!el.hasAttribute('data-target')) {
      el.setAttribute('data-target', el.textContent.trim());
    }
  });

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;

      var el = entry.target;

      // Guard: only animate once
      if (el.getAttribute('data-counted') === 'true') return;
      el.setAttribute('data-counted', 'true');
      observer.unobserve(el);

      var raw    = el.getAttribute('data-target') || el.textContent.trim();
      var parsed = parseStatValue(raw);

      if (!parsed) {
        // Not a number — leave as-is
        return;
      }

      animateCounter(el, parsed, DURATION);
    });
  }, {
    threshold: THRESHOLD
  });

  statEls.forEach(function (el) {
    observer.observe(el);
  });
}

// Auto-init if loaded directly as a non-module script (defensive)
if (typeof module === 'undefined' && typeof exports === 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCounters);
  } else {
    initCounters();
  }
}
