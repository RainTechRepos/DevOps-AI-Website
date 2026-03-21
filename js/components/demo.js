/* ========================================
   js/components/demo.js — Interactive Product Demo
   DevOps AI by RainTech
   Version: 1.0.0 (FR-W22)

   Lazy-loaded by js/app.js when .demo-container is present.
   Exports: initDemo()

   Features:
   - 7-step guided walkthrough ("Watch AI Resolve a Ticket")
   - Inline compact mode + lightbox full-screen mode
   - Keyboard accessible (arrow keys, Escape)
   - Screen reader support (aria-live)
   - Swipe support on touch devices
   - Smooth crossfade transitions
   ======================================== */

'use strict';

/* ── Demo Step Data ─────────────────────────────────────────────────────── */
var STEPS = [
  {
    id: 'ticket-arrives',
    title: 'Ticket Arrives',
    icon: '📧',
    narration: 'An email arrives from a frustrated client: "Our main printer on the 3rd floor has been offline since this morning — nobody can print." The system ingests the ticket automatically from email, normalizing it into a structured format.',
    platform: {
      label: 'Ticket Inbox',
      status: 'New Ticket',
      statusColor: 'var(--accent)',
      detail: 'From: sarah@acmecorp.com\nSubject: Printer offline — 3rd floor\nPriority: Unassigned\nCategory: Unassigned'
    }
  },
  {
    id: 'ai-classifies',
    title: 'AI Classifies',
    icon: '🤖',
    narration: 'NLP analysis processes the ticket content in under 2 seconds. The AI identifies keywords, sentiment (frustrated), and matches against known categories. Priority set to P3, category assigned to Endpoint — Printer.',
    platform: {
      label: 'AI Classification Engine',
      status: 'Classified',
      statusColor: '#17E4ED',
      detail: 'Priority: P3 (Medium)\nCategory: Endpoint → Printer\nSentiment: Frustrated (0.72)\nConfidence: 94.2%'
    }
  },
  {
    id: 'smart-routing',
    title: 'Smart Routing',
    icon: '🔀',
    narration: 'The routing engine checks the knowledge base and finds a 92% match to a known printer issue pattern. Instead of routing to a technician, it flags the ticket for auto-resolution — saving human time for complex problems.',
    platform: {
      label: 'Routing Decision',
      status: 'Auto-Resolve',
      statusColor: '#8BDB02',
      detail: 'KB Match: 92% — "Printer Spooler Reset"\nRoute: Auto-Resolution Pipeline\nEstimated Fix Time: < 2 minutes\nTechnician Override: Available'
    }
  },
  {
    id: 'auto-resolution',
    title: 'Auto-Resolution',
    icon: '⚡',
    narration: 'The matched KB article triggers an approved remediation script. The system remotely connects to the print server, restarts the spooler service, clears the queue, and verifies the printer is back online — all without human intervention.',
    platform: {
      label: 'Remediation Engine',
      status: 'Executing',
      statusColor: '#17E4ED',
      detail: 'Step 1: Connect to PRINTSVR-03 ✓\nStep 2: Stop Print Spooler ✓\nStep 3: Clear queue (12 jobs) ✓\nStep 4: Start Print Spooler ✓\nStep 5: Verify online ✓'
    }
  },
  {
    id: 'client-notified',
    title: 'Client Notified',
    icon: '✉️',
    narration: 'An AI-generated response is sent to the client with resolution details. The message is personalized, references the specific printer, and includes a verification step. Total resolution time: 97 seconds.',
    platform: {
      label: 'Communication Hub',
      status: 'Sent',
      statusColor: '#8BDB02',
      detail: 'To: sarah@acmecorp.com\nTemplate: Auto-Resolution Confirmation\nPersonalized: Yes (client name, device)\nResolution Time: 1 min 37 sec'
    }
  },
  {
    id: 'metrics-updated',
    title: 'Metrics Updated',
    icon: '📊',
    narration: 'All operational metrics update in real time. SLA timer stopped well within the 4-hour window. The resolution is logged for QBR reporting, and a CSAT survey is automatically triggered to the client.',
    platform: {
      label: 'Analytics Dashboard',
      status: 'Logged',
      statusColor: '#17E4ED',
      detail: 'SLA Status: ✓ Within Target (97s / 4h)\nCSAT Survey: Triggered\nAuto-Resolve Rate: 41.2% → 41.3%\nQBR Data: Updated'
    }
  },
  {
    id: 'learning',
    title: 'AI Learning',
    icon: '🧠',
    narration: 'The successful resolution feeds back into the AI model. Pattern confidence for printer-spooler issues increases, the KB article is strengthened, and similar future tickets will route even faster. The platform gets smarter with every ticket.',
    platform: {
      label: 'Learning Engine',
      status: 'Updated',
      statusColor: '#8BDB02',
      detail: 'Pattern: "printer+offline+spooler"\nConfidence: 92% → 93.1%\nKB Article: Strengthened (+1 success)\nModel Version: v2.847 → v2.848'
    }
  }
];

/* ── Platform UI Renderer ───────────────────────────────────────────────── */
function renderPlatformUI(step) {
  var lines = step.platform.detail.split('\n');
  var linesHtml = lines.map(function (line) {
    return '<div class="demo-platform__line">' + escapeHtml(line) + '</div>';
  }).join('');

  return '<div class="demo-platform">' +
    '<div class="demo-platform__header">' +
      '<span class="demo-platform__label">' + escapeHtml(step.platform.label) + '</span>' +
      '<span class="demo-platform__status" style="color:' + step.platform.statusColor + '">' +
        escapeHtml(step.platform.status) +
      '</span>' +
    '</div>' +
    '<div class="demo-platform__body">' + linesHtml + '</div>' +
  '</div>';
}

function escapeHtml(str) {
  var div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

/* ── Demo Component ─────────────────────────────────────────────────────── */
function createDemo(container) {
  var currentStep = 0;
  var isLightbox = false;
  var lightboxEl = null;

  // Build the demo HTML
  function render(target, mode) {
    var isCompact = mode === 'inline';
    var prefix = isCompact ? 'demo-inline' : 'demo-lightbox';

    var stepsHtml = STEPS.map(function (step, i) {
      var active = i === currentStep ? ' is-active' : '';
      return '<div class="demo-step' + active + '" data-step="' + i + '" id="' + prefix + '-step-' + i + '">' +
        '<div class="demo-step__icon">' + step.icon + '</div>' +
        '<div class="demo-step__content">' +
          '<h3 class="demo-step__title">' + escapeHtml(step.title) + '</h3>' +
          '<p class="demo-step__narration">' + escapeHtml(step.narration) + '</p>' +
        '</div>' +
        '<div class="demo-step__platform">' + renderPlatformUI(step) + '</div>' +
      '</div>';
    }).join('');

    // Progress indicators
    var dotsHtml = STEPS.map(function (step, i) {
      var active = i === currentStep ? ' is-active' : '';
      var completed = i < currentStep ? ' is-completed' : '';
      return '<button class="demo-dot' + active + completed + '" data-goto="' + i + '" ' +
        'aria-label="Go to step ' + (i + 1) + ': ' + escapeHtml(step.title) + '">' +
        '<span class="demo-dot__label">' + escapeHtml(step.title) + '</span>' +
      '</button>';
    }).join('');

    var html = '<div class="demo-progress">' +
      '<div class="demo-progress__bar"><div class="demo-progress__fill" style="width:' + ((currentStep / (STEPS.length - 1)) * 100) + '%"></div></div>' +
      '<span class="demo-progress__text">Step ' + (currentStep + 1) + ' of ' + STEPS.length + '</span>' +
    '</div>' +
    '<div class="demo-dots">' + dotsHtml + '</div>' +
    '<div class="demo-viewport" aria-live="polite" aria-atomic="true">' + stepsHtml + '</div>' +
    '<div class="demo-controls">' +
      '<button class="demo-btn demo-btn--prev"' + (currentStep === 0 ? ' disabled' : '') + ' aria-label="Previous step">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="15,18 9,12 15,6"/></svg> Back' +
      '</button>' +
      (currentStep < STEPS.length - 1
        ? '<button class="demo-btn demo-btn--next" aria-label="Next step">Next <svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="9,6 15,12 9,18"/></svg></button>'
        : '') +
      (currentStep === STEPS.length - 1
        ? '<div class="demo-completion">' +
            '<p class="demo-completion__text">Ticket resolved in 97 seconds — zero human intervention.</p>' +
            '<div class="demo-completion__actions">' +
              '<a href="get-started.html" class="btn btn--primary">Book a Demo</a>' +
              '<a href="zones/service-desk/" class="btn btn--secondary">Explore Service Desk →</a>' +
            '</div>' +
          '</div>'
        : '') +
    '</div>';

    if (!isCompact) {
      html += '<button class="demo-lightbox__close" aria-label="Close demo">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>' +
      '</button>';
    } else {
      html += '<button class="demo-expand-btn" aria-label="View full demo">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="15,3 21,3 21,9"/><polyline points="9,21 3,21 3,15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>' +
        ' View Full Demo' +
      '</button>';
    }

    target.innerHTML = html;
    attachEvents(target, mode);
  }

  function goToStep(step) {
    if (step < 0 || step >= STEPS.length) return;
    currentStep = step;
    // Re-render both views if lightbox is open
    render(container, 'inline');
    if (lightboxEl) render(lightboxEl.querySelector('.demo-lightbox__content'), 'lightbox');
  }

  function attachEvents(target, mode) {
    // Prev/Next
    var prevBtn = target.querySelector('.demo-btn--prev');
    var nextBtn = target.querySelector('.demo-btn--next');
    if (prevBtn) prevBtn.addEventListener('click', function () { goToStep(currentStep - 1); });
    if (nextBtn) nextBtn.addEventListener('click', function () { goToStep(currentStep + 1); });

    // Dots
    target.querySelectorAll('.demo-dot').forEach(function (dot) {
      dot.addEventListener('click', function () {
        goToStep(parseInt(dot.getAttribute('data-goto'), 10));
      });
    });

    // Expand to lightbox
    var expandBtn = target.querySelector('.demo-expand-btn');
    if (expandBtn) expandBtn.addEventListener('click', openLightbox);

    // Close lightbox
    var closeBtn = target.querySelector('.demo-lightbox__close');
    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  }

  function openLightbox() {
    if (lightboxEl) return;
    isLightbox = true;

    lightboxEl = document.createElement('div');
    lightboxEl.className = 'demo-lightbox';
    lightboxEl.setAttribute('role', 'dialog');
    lightboxEl.setAttribute('aria-modal', 'true');
    lightboxEl.setAttribute('aria-label', 'Interactive product demo');

    var overlay = document.createElement('div');
    overlay.className = 'demo-lightbox__overlay';
    overlay.addEventListener('click', closeLightbox);

    var content = document.createElement('div');
    content.className = 'demo-lightbox__content';

    lightboxEl.appendChild(overlay);
    lightboxEl.appendChild(content);
    document.body.appendChild(lightboxEl);
    document.body.style.overflow = 'hidden';

    // Small delay for CSS transition
    requestAnimationFrame(function () {
      lightboxEl.classList.add('is-open');
      render(content, 'lightbox');
      content.focus();
    });
  }

  function closeLightbox() {
    if (!lightboxEl) return;
    isLightbox = false;
    lightboxEl.classList.remove('is-open');
    document.body.style.overflow = '';

    setTimeout(function () {
      if (lightboxEl && lightboxEl.parentNode) {
        lightboxEl.parentNode.removeChild(lightboxEl);
      }
      lightboxEl = null;
    }, 300);
  }

  // Keyboard navigation
  document.addEventListener('keydown', function (e) {
    // Only handle if demo is in viewport or lightbox is open
    if (!isLightbox && !isElementInViewport(container)) return;

    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      e.preventDefault();
      goToStep(currentStep + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault();
      goToStep(currentStep - 1);
    } else if (e.key === 'Escape' && isLightbox) {
      closeLightbox();
    }
  });

  // Touch/swipe support
  var touchStartX = 0;
  container.addEventListener('touchstart', function (e) {
    touchStartX = e.touches[0].clientX;
  }, { passive: true });

  container.addEventListener('touchend', function (e) {
    var diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {
      if (diff > 0) goToStep(currentStep + 1);
      else goToStep(currentStep - 1);
    }
  }, { passive: true });

  // Initial render
  render(container, 'inline');
}

function isElementInViewport(el) {
  var rect = el.getBoundingClientRect();
  return rect.top < window.innerHeight && rect.bottom > 0;
}

/* ── Public Init ────────────────────────────────────────────────────────── */
export function initDemo() {
  var containers = document.querySelectorAll('.demo-container');
  containers.forEach(function (container) {
    createDemo(container);
  });
}

// Auto-init
if (typeof module === 'undefined' && typeof exports === 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDemo);
  } else {
    initDemo();
  }
}
