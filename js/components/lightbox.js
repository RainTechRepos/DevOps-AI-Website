/* ========================================
   js/components/lightbox.js — Screenshot Lightbox
   DevOps AI by RainTech
   Version: 2.0.0 (FR-W03)

   Features:
   - Native <dialog> with showModal() for built-in accessibility
   - Blurred backdrop (backdrop-filter: blur(8px))
   - Smooth scale-up entry animation
   - Previous / Next navigation (multiple images)
   - Keyboard: Escape (native dialog), Arrow Left/Right, Tab trap
   - Touch: pinch-to-zoom (CSS touch-action + transform)
   - Caption from data-caption or alt attribute
   - "N of M" counter for galleries
   - Loading spinner while image loads
   - ES Module — exports initLightbox()
   ======================================== */

'use strict';

/* ─────────────────────────────────────────
   STYLES — injected once into <head>
───────────────────────────────────────── */
var LIGHTBOX_STYLES = /* css */`
.lb-dialog {
  border: none;
  padding: 0;
  background: transparent;
  max-width: 100vw;
  max-height: 100vh;
  width: 100vw;
  height: 100dvh;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lb-dialog::backdrop {
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.lb-inner {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: min(92vw, 1200px);
  max-height: 92dvh;
  animation: lb-scale-in 0.22s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

@keyframes lb-scale-in {
  from { opacity: 0; transform: scale(0.88); }
  to   { opacity: 1; transform: scale(1); }
}

.lb-img-wrap {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 120px;
  min-width: 200px;
}

.lb-image {
  display: block;
  max-width: min(88vw, 1100px);
  max-height: 78dvh;
  width: auto;
  height: auto;
  border-radius: 8px;
  object-fit: contain;
  /* Pinch-to-zoom on mobile */
  touch-action: pinch-zoom;
  transform-origin: center center;
  user-select: none;
  -webkit-user-drag: none;
}

/* Spinner */
.lb-spinner {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.lb-spinner::after {
  content: '';
  width: 44px;
  height: 44px;
  border: 3px solid rgba(255,255,255,0.2);
  border-top-color: #fff;
  border-radius: 50%;
  animation: lb-spin 0.7s linear infinite;
}

@keyframes lb-spin {
  to { transform: rotate(360deg); }
}

.lb-spinner[hidden] { display: none; }

/* Caption row */
.lb-caption-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 1rem;
  margin-top: 10px;
  min-height: 28px;
}

.lb-caption {
  color: rgba(255,255,255,0.82);
  font-size: 0.85rem;
  line-height: 1.4;
  flex: 1;
  text-align: center;
}

.lb-counter {
  color: rgba(255,255,255,0.5);
  font-size: 0.78rem;
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}

/* Buttons */
.lb-btn {
  appearance: none;
  -webkit-appearance: none;
  background: rgba(255,255,255,0.1);
  border: 1px solid rgba(255,255,255,0.18);
  color: #fff;
  border-radius: 50%;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: background 0.18s, transform 0.15s;
  font-size: 1.1rem;
  line-height: 1;
  padding: 0;
}

.lb-btn:hover,
.lb-btn:focus-visible {
  background: rgba(255,255,255,0.22);
  outline: 2px solid rgba(255,255,255,0.5);
  outline-offset: 2px;
}

.lb-btn:active { transform: scale(0.93); }

.lb-close {
  position: absolute;
  top: -48px;
  right: 0;
}

.lb-prev,
.lb-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
}

.lb-prev { left: -56px; }
.lb-next { right: -56px; }

/* On narrow screens move controls below image */
@media (max-width: 700px) {
  .lb-prev,
  .lb-next {
    position: static;
    transform: none;
    margin-top: 8px;
  }

  .lb-caption-row {
    flex-wrap: wrap;
    justify-content: center;
  }

  .lb-close { top: -44px; right: 0; }
}

/* Hide nav buttons when only one image */
.lb-dialog[data-single="true"] .lb-prev,
.lb-dialog[data-single="true"] .lb-next {
  display: none;
}
`;

/* ─────────────────────────────────────────
   STATE
───────────────────────────────────────── */
var state = {
  triggers:     [],   // all lightbox trigger elements
  currentIndex: 0,    // index of open image
  dialog:       null, // <dialog> element ref
  imgEl:        null, // <img> inside dialog
  captionEl:    null,
  counterEl:    null,
  spinnerEl:    null,
};

/* ─────────────────────────────────────────
   HELPERS
───────────────────────────────────────── */
function getSrc(trigger) {
  return (
    trigger.getAttribute('data-lightbox-src') ||
    trigger.getAttribute('href') ||
    (trigger.tagName === 'IMG' ? trigger.src : null) ||
    trigger.querySelector('img')?.src ||
    null
  );
}

function getCaption(trigger) {
  return (
    trigger.getAttribute('data-caption') ||
    trigger.getAttribute('data-lightbox-caption') ||
    trigger.querySelector('img')?.getAttribute('alt') ||
    (trigger.tagName === 'IMG' ? trigger.getAttribute('alt') : null) ||
    ''
  );
}

/* ─────────────────────────────────────────
   BUILD DIALOG (once)
───────────────────────────────────────── */
function buildDialog() {
  if (state.dialog) return;

  // Inject styles
  var styleEl = document.createElement('style');
  styleEl.textContent = LIGHTBOX_STYLES;
  document.head.appendChild(styleEl);

  // Build DOM
  var dialog = document.createElement('dialog');
  dialog.className = 'lb-dialog';
  dialog.setAttribute('aria-modal', 'true');
  dialog.setAttribute('aria-label', 'Image lightbox');
  dialog.setAttribute('role', 'dialog');

  var inner = document.createElement('div');
  inner.className = 'lb-inner';

  // Close button
  var closeBtn = document.createElement('button');
  closeBtn.className = 'lb-btn lb-close';
  closeBtn.setAttribute('aria-label', 'Close lightbox');
  closeBtn.innerHTML = '&#x2715;'; // ✕
  closeBtn.addEventListener('click', closeLightbox);

  // Prev button
  var prevBtn = document.createElement('button');
  prevBtn.className = 'lb-btn lb-prev';
  prevBtn.setAttribute('aria-label', 'Previous image');
  prevBtn.innerHTML = '&#x2039;'; // ‹
  prevBtn.addEventListener('click', function () { navigate(-1); });

  // Next button
  var nextBtn = document.createElement('button');
  nextBtn.className = 'lb-btn lb-next';
  nextBtn.setAttribute('aria-label', 'Next image');
  nextBtn.innerHTML = '&#x203A;'; // ›
  nextBtn.addEventListener('click', function () { navigate(1); });

  // Image wrapper
  var imgWrap = document.createElement('div');
  imgWrap.className = 'lb-img-wrap';

  var img = document.createElement('img');
  img.className = 'lb-image';
  img.setAttribute('alt', '');
  img.draggable = false;

  // Spinner
  var spinner = document.createElement('div');
  spinner.className = 'lb-spinner';
  spinner.setAttribute('aria-hidden', 'true');

  imgWrap.appendChild(spinner);
  imgWrap.appendChild(img);

  // Caption row
  var captionRow = document.createElement('div');
  captionRow.className = 'lb-caption-row';

  var caption = document.createElement('p');
  caption.className = 'lb-caption';

  var counter = document.createElement('span');
  counter.className = 'lb-counter';
  counter.setAttribute('aria-live', 'polite');

  captionRow.appendChild(caption);
  captionRow.appendChild(counter);

  // Assemble
  inner.appendChild(closeBtn);
  inner.appendChild(prevBtn);
  inner.appendChild(imgWrap);
  inner.appendChild(nextBtn);
  inner.appendChild(captionRow);
  dialog.appendChild(inner);
  document.body.appendChild(dialog);

  // Close on backdrop click (outside inner)
  dialog.addEventListener('click', function (e) {
    if (e.target === dialog) closeLightbox();
  });

  // Store refs
  state.dialog    = dialog;
  state.imgEl     = img;
  state.captionEl = caption;
  state.counterEl = counter;
  state.spinnerEl = spinner;
  state.prevBtn   = prevBtn;
  state.nextBtn   = nextBtn;
}

/* ─────────────────────────────────────────
   OPEN / CLOSE
───────────────────────────────────────── */
function openLightbox(index) {
  buildDialog();

  state.currentIndex = index;
  var single = state.triggers.length <= 1;
  state.dialog.setAttribute('data-single', single ? 'true' : 'false');

  loadImage(index);
  state.dialog.showModal();
}

function closeLightbox() {
  if (state.dialog && state.dialog.open) {
    state.dialog.close();
  }
}

function loadImage(index) {
  var trigger = state.triggers[index];
  if (!trigger) return;

  var src     = getSrc(trigger);
  var caption = getCaption(trigger);
  var total   = state.triggers.length;

  // Show spinner, hide image until loaded
  state.spinnerEl.removeAttribute('hidden');
  state.imgEl.style.opacity = '0';
  state.imgEl.src = '';

  // Set caption
  state.captionEl.textContent = caption;
  state.imgEl.setAttribute('alt', caption || '');

  // Counter
  if (total > 1) {
    state.counterEl.textContent = (index + 1) + ' of ' + total;
  } else {
    state.counterEl.textContent = '';
  }

  // Update nav button states
  if (state.prevBtn) {
    state.prevBtn.disabled = false; // wrap-around always enabled
    state.prevBtn.setAttribute('aria-label', 'Previous image');
  }
  if (state.nextBtn) {
    state.nextBtn.disabled = false;
    state.nextBtn.setAttribute('aria-label', 'Next image');
  }

  if (!src) {
    state.spinnerEl.setAttribute('hidden', '');
    return;
  }

  // Preload
  var tempImg = new Image();
  tempImg.onload = function () {
    state.imgEl.src = src;
    state.imgEl.style.opacity = '1';
    state.spinnerEl.setAttribute('hidden', '');
  };
  tempImg.onerror = function () {
    state.imgEl.src = src; // try anyway
    state.imgEl.style.opacity = '1';
    state.spinnerEl.setAttribute('hidden', '');
  };
  tempImg.src = src;
}

/* ─────────────────────────────────────────
   NAVIGATION
───────────────────────────────────────── */
function navigate(direction) {
  var total = state.triggers.length;
  if (total < 2) return;
  var newIndex = (state.currentIndex + direction + total) % total;
  state.currentIndex = newIndex;
  loadImage(newIndex);
}

/* ─────────────────────────────────────────
   KEYBOARD HANDLING
───────────────────────────────────────── */
function onKeyDown(e) {
  if (!state.dialog || !state.dialog.open) return;

  switch (e.key) {
    case 'ArrowRight':
    case 'ArrowDown':
      e.preventDefault();
      navigate(1);
      break;
    case 'ArrowLeft':
    case 'ArrowUp':
      e.preventDefault();
      navigate(-1);
      break;
    // Escape is handled natively by <dialog>
  }
}

/* ─────────────────────────────────────────
   COLLECT TRIGGERS
   Handles grouped galleries via data-lightbox-group
───────────────────────────────────────── */
function collectTriggers(clickedEl) {
  var group = clickedEl.getAttribute('data-lightbox-group');

  if (group) {
    // Gallery group: collect all triggers with same group
    return Array.from(
      document.querySelectorAll('[data-lightbox-group="' + group + '"]')
    );
  }

  // No group: use all lightbox triggers on the page
  return Array.from(
    document.querySelectorAll('[data-lightbox], .screenshot')
  );
}

/* ─────────────────────────────────────────
   INIT — public export
───────────────────────────────────────── */
export function initLightbox() {
  // Delegate click handling for [data-lightbox] and .screenshot
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-lightbox]') ||
                  e.target.closest('.screenshot');
    if (!trigger) return;

    // Prevent default for <a> tags
    e.preventDefault();

    var triggers = collectTriggers(trigger);
    state.triggers = triggers;

    var index = triggers.indexOf(trigger);
    if (index === -1) index = 0;

    openLightbox(index);
  });

  // Global keyboard listener
  document.addEventListener('keydown', onKeyDown);

  // Handle native dialog cancel (Escape key) — already works natively
  // but we hook to ensure state is correct
  document.addEventListener('cancel', function (e) {
    if (e.target === state.dialog) {
      // dialog.close() is called automatically
    }
  }, true);
}

/* ─────────────────────────────────────────
   AUTO-INIT (when not loaded as module)
───────────────────────────────────────── */
if (typeof module === 'undefined' && typeof exports === 'undefined') {
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLightbox);
  } else {
    initLightbox();
  }
}
