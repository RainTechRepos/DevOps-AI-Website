/* ========================================
   js/components/roi-calculator.js — ROI Calculator
   DevOps AI by RainTech
   Version: 2.0.0 (FR-W03)

   Lazy-loaded by js/app.js when .roi-calculator is present.
   Exports: initROICalculator()
   ======================================== */

'use strict';

/**
 * Calculate and render ROI metrics based on input values.
 */
function calculateROI() {
  var techs   = parseFloat(document.getElementById('roi-technicians')?.value) || 10;
  var tickets = parseFloat(document.getElementById('roi-tickets')?.value)     || 1500;
  var rate    = parseFloat(document.getElementById('roi-rate')?.value)        || 85;
  var clients = parseFloat(document.getElementById('roi-clients')?.value)     || 50;

  // Market-data-backed model:
  // 35% average ticket reduction, 25 min avg resolution time
  var TICKET_REDUCTION_RATE = 0.35;
  var AVG_RESOLUTION_MINS   = 25;

  var ticketsReduced  = Math.round(tickets * TICKET_REDUCTION_RATE);
  var hoursSaved      = Math.round((ticketsReduced * AVG_RESOLUTION_MINS) / 60);
  var monthlySavings  = Math.round(hoursSaved * rate);
  var annualSavings   = monthlySavings * 12;

  // Render
  var elTickets = document.getElementById('roi-result-tickets');
  var elHours   = document.getElementById('roi-result-hours');
  var elSavings = document.getElementById('roi-result-savings');
  var elAnnual  = document.getElementById('roi-result-annual');

  if (elTickets) elTickets.textContent = ticketsReduced.toLocaleString();
  if (elHours)   elHours.textContent   = hoursSaved.toLocaleString() + ' hrs';
  if (elSavings) elSavings.textContent = '$' + monthlySavings.toLocaleString();
  if (elAnnual)  elAnnual.textContent  = '$' + annualSavings.toLocaleString();
}

/**
 * Attach input listeners and run initial calculation.
 * @param {Element} form - .roi-calculator element
 */
function attachCalculator(form) {
  var inputs = form.querySelectorAll('input[type="number"], input[type="range"]');
  inputs.forEach(function (input) {
    input.addEventListener('input', calculateROI);
  });
  // Run once with defaults
  calculateROI();
}

/**
 * Public init — called by app.js lazy loader.
 */
export function initROICalculator() {
  var forms = document.querySelectorAll('.roi-calculator');
  forms.forEach(attachCalculator);
}

// Auto-init when loaded directly
if (typeof module === 'undefined' && typeof exports === 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initROICalculator);
  } else {
    initROICalculator();
  }
}
