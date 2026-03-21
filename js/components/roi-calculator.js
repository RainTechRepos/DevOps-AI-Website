/* ========================================
   js/components/roi-calculator.js — ROI Calculator
   DevOps AI by RainTech
   Version: 3.0.0 (FR-W23)

   Lazy-loaded by js/app.js when .roi-calculator is present.
   Exports: initROICalculator()

   Features:
   - 6 input fields with real-time calculation
   - Animated number counters
   - CSS/SVG bar chart (no external libs)
   - Share via URL query parameters
   - Pre-fill from query parameters
   - Industry-specific adjustments
   - Fully accessible
   ======================================== */

'use strict';

/* ── Industry Adjustments ───────────────────────────────────────────────── */
var INDUSTRY = {
  'msp':        { autoRate: 0.70, label: 'MSP' },
  'healthcare': { autoRate: 0.55, label: 'Healthcare' },
  'finance':    { autoRate: 0.50, label: 'Finance' },
  'government': { autoRate: 0.45, label: 'Government' },
  'education':  { autoRate: 0.60, label: 'Education' },
  'other':      { autoRate: 0.60, label: 'Other' }
};

/* ── Tier Pricing (monthly per-endpoint) ────────────────────────────────── */
var TIER_COST_PER_ENDPOINT = 3.50; // blended average

/* ── Animation Helpers ──────────────────────────────────────────────────── */
function animateValue(el, start, end, duration, formatter) {
  if (!el) return;
  var startTime = null;
  var diff = end - start;
  if (diff === 0) { el.textContent = formatter(end); return; }

  function step(timestamp) {
    if (!startTime) startTime = timestamp;
    var progress = Math.min((timestamp - startTime) / duration, 1);
    // Ease out cubic
    var eased = 1 - Math.pow(1 - progress, 3);
    var current = Math.round(start + diff * eased);
    el.textContent = formatter(current);
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

function fmtDollars(n) { return '$' + n.toLocaleString(); }
function fmtNumber(n) { return n.toLocaleString(); }
function fmtHours(n) { return n.toLocaleString() + ' hrs'; }
function fmtPercent(n) { return n.toLocaleString() + '%'; }
function fmtMonths(n) { return n <= 0 ? '< 1 month' : n + (n === 1 ? ' month' : ' months'); }

/* ── Previous Values (for animation) ───────────────────────────────────── */
var prevValues = {
  hoursSaved: 0,
  ticketsResolved: 0,
  monthlySavings: 0,
  annualSavings: 0,
  roiPercent: 0,
  timeToRoi: 0
};

/* ── Core Calculator ────────────────────────────────────────────────────── */
function calculate(container) {
  var techs     = getVal(container, 'roi-technicians', 10);
  var tickets   = getVal(container, 'roi-tickets', 1000);
  var resTime   = getVal(container, 'roi-resolution-time', 45);
  var hourlyRate = getVal(container, 'roi-hourly-rate', 35);
  var endpoints = getVal(container, 'roi-endpoints', 500);
  var industry  = getSelect(container, 'roi-industry', 'msp');

  var indData = INDUSTRY[industry] || INDUSTRY['msp'];
  var autoRate = indData.autoRate;

  // Core formulas
  var monthlyTicketHours = (tickets * resTime) / 60;
  var currentMonthlyCost = monthlyTicketHours * hourlyRate;

  var ticketsResolved = Math.round(tickets * autoRate);
  var timeSaved = monthlyTicketHours * autoRate * 0.8;
  var monthlySavings = Math.round(timeSaved * hourlyRate);
  var annualSavings = monthlySavings * 12;

  var tierCost = endpoints * TIER_COST_PER_ENDPOINT;
  var annualCost = tierCost * 12;
  var roiPercent = annualCost > 0 ? Math.round((annualSavings / annualCost) * 100) : 0;
  var timeToRoi = annualSavings > 0 ? Math.max(1, Math.round((annualCost / annualSavings) * 12)) : 0;
  var hoursSaved = Math.round(timeSaved);

  // Animate results
  animateValue(container.querySelector('#roi-result-hours'), prevValues.hoursSaved, hoursSaved, 600, fmtHours);
  animateValue(container.querySelector('#roi-result-tickets'), prevValues.ticketsResolved, ticketsResolved, 600, fmtNumber);
  animateValue(container.querySelector('#roi-result-monthly'), prevValues.monthlySavings, monthlySavings, 600, fmtDollars);
  animateValue(container.querySelector('#roi-result-annual'), prevValues.annualSavings, annualSavings, 600, fmtDollars);
  animateValue(container.querySelector('#roi-result-roi'), prevValues.roiPercent, roiPercent, 600, fmtPercent);
  animateValue(container.querySelector('#roi-result-time'), prevValues.timeToRoi, timeToRoi, 600, fmtMonths);

  // Update chart
  updateChart(container, currentMonthlyCost, monthlySavings, monthlyTicketHours, timeSaved);

  // Store for next animation
  prevValues = { hoursSaved: hoursSaved, ticketsResolved: ticketsResolved, monthlySavings: monthlySavings, annualSavings: annualSavings, roiPercent: roiPercent, timeToRoi: timeToRoi };

  // Update aria-live summary
  var summary = container.querySelector('#roi-summary');
  if (summary) {
    summary.textContent = 'Annual savings: ' + fmtDollars(annualSavings) + ', ROI: ' + roiPercent + '%, ' + ticketsResolved + ' tickets auto-resolved per month.';
  }
}

function getVal(container, id, fallback) {
  var el = container.querySelector('#' + id);
  if (!el) return fallback;
  var v = parseFloat(el.value);
  return isNaN(v) ? fallback : v;
}

function getSelect(container, id, fallback) {
  var el = container.querySelector('#' + id);
  return el ? el.value : fallback;
}

/* ── Bar Chart (pure CSS) ───────────────────────────────────────────────── */
function updateChart(container, currentCost, savings, currentHours, savedHours) {
  var chart = container.querySelector('.roi-chart');
  if (!chart) return;

  var maxVal = Math.max(currentCost, 1);
  var remainingCost = currentCost - savings;
  var savingsPercent = (savings / maxVal) * 100;
  var remainingPercent = (remainingCost / maxVal) * 100;

  var barCurrent = chart.querySelector('.roi-chart__bar--current .roi-chart__fill');
  var barAI = chart.querySelector('.roi-chart__bar--ai .roi-chart__fill-remaining');
  var barSavings = chart.querySelector('.roi-chart__bar--ai .roi-chart__fill-savings');

  if (barCurrent) barCurrent.style.width = '100%';
  if (barAI) barAI.style.width = remainingPercent + '%';
  if (barSavings) barSavings.style.width = savingsPercent + '%';

  // Update labels
  var labelCurrent = chart.querySelector('.roi-chart__val--current');
  var labelAI = chart.querySelector('.roi-chart__val--ai');
  if (labelCurrent) labelCurrent.textContent = fmtDollars(Math.round(currentCost)) + '/mo';
  if (labelAI) labelAI.textContent = fmtDollars(Math.round(remainingCost)) + '/mo';
}

/* ── Slider Sync ────────────────────────────────────────────────────────── */
function syncSlider(container, sliderId, numberId) {
  var slider = container.querySelector('#' + sliderId);
  var number = container.querySelector('#' + numberId);
  if (!slider || !number) return;

  slider.addEventListener('input', function () {
    number.value = slider.value;
    calculate(container);
  });
  number.addEventListener('input', function () {
    var v = parseFloat(number.value);
    if (!isNaN(v)) {
      v = Math.max(parseFloat(slider.min), Math.min(parseFloat(slider.max), v));
      slider.value = v;
    }
    calculate(container);
  });
}

/* ── Share URL ──────────────────────────────────────────────────────────── */
function getShareUrl(container) {
  var params = new URLSearchParams();
  var fields = ['roi-technicians', 'roi-tickets', 'roi-resolution-time', 'roi-hourly-rate', 'roi-endpoints', 'roi-industry'];
  fields.forEach(function (id) {
    var el = container.querySelector('#' + id);
    if (el) params.set(id, el.value);
  });
  return window.location.origin + window.location.pathname + '?' + params.toString();
}

function prefillFromUrl(container) {
  var params = new URLSearchParams(window.location.search);
  var fields = ['roi-technicians', 'roi-tickets', 'roi-resolution-time', 'roi-hourly-rate', 'roi-endpoints', 'roi-industry'];
  fields.forEach(function (id) {
    var val = params.get(id);
    if (val !== null) {
      var el = container.querySelector('#' + id);
      if (el) {
        el.value = val;
        // Sync slider if it exists
        var sliderId = id + '-slider';
        var slider = container.querySelector('#' + sliderId);
        if (slider) slider.value = val;
      }
    }
  });
}

/* ── Methodology Toggle ─────────────────────────────────────────────────── */
function initMethodology(container) {
  var toggle = container.querySelector('.roi-methodology__toggle');
  var body = container.querySelector('.roi-methodology__body');
  if (!toggle || !body) return;

  toggle.addEventListener('click', function () {
    var isOpen = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
    body.style.maxHeight = isOpen ? '0' : body.scrollHeight + 'px';
  });

  toggle.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggle.click();
    }
  });
}

/* ── Public Init ────────────────────────────────────────────────────────── */
export function initROICalculator() {
  var containers = document.querySelectorAll('.roi-calculator');
  containers.forEach(function (container) {
    // Prefill from URL
    prefillFromUrl(container);

    // Sync sliders
    syncSlider(container, 'roi-technicians-slider', 'roi-technicians');
    syncSlider(container, 'roi-tickets-slider', 'roi-tickets');
    syncSlider(container, 'roi-resolution-time-slider', 'roi-resolution-time');

    // All inputs trigger recalc
    container.querySelectorAll('input, select').forEach(function (input) {
      input.addEventListener('input', function () { calculate(container); });
      input.addEventListener('change', function () { calculate(container); });
    });

    // Share button
    var shareBtn = container.querySelector('.roi-share-btn');
    if (shareBtn) {
      shareBtn.addEventListener('click', function () {
        var url = getShareUrl(container);
        if (navigator.clipboard) {
          navigator.clipboard.writeText(url).then(function () {
            shareBtn.textContent = 'Link Copied!';
            setTimeout(function () { shareBtn.textContent = 'Share This Report'; }, 2000);
          });
        } else {
          window.prompt('Copy this link:', url);
        }
      });
    }

    // Methodology
    initMethodology(container);

    // Initial calculation
    calculate(container);
  });
}

// Auto-init
if (typeof module === 'undefined' && typeof exports === 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initROICalculator);
  } else {
    initROICalculator();
  }
}
