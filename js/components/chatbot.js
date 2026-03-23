/* ========================================
   js/components/chatbot.js — AI Chatbot Widget
   DevOps AI by RainTech
   FR-W20

   Lazy-loaded when #chatbot-container exists.
   Renders FAB, chat panel, message history.
   ======================================== */

(function () {
  'use strict';

  // ── Config ──────────────────────────────────────────────────────────────
  var RATE_LIMIT = 30;
  var RATE_WINDOW_MS = 60000;
  var API_TIMEOUT_MS = 5000;
  var TYPING_DELAY_MIN = 600;
  var TYPING_DELAY_MAX = 1500;
  var SESSION_KEY = 'devops-ai-chat-history';
  var FIRST_VISIT_KEY = 'devops-ai-chat-seen';

  // ── Mock responses ──────────────────────────────────────────────────────
  var MOCK_RESPONSES = {
    ticket: 'DevOps AI uses NLP-powered ticket classification to automatically triage, prioritize, and route incoming tickets. Our Service Desk zone covers 12 process areas — from AI auto-resolution to SLA prediction — reducing average triage time to under 30 seconds.',
    triage: 'Our AI Triage engine classifies tickets using natural language processing, assigns priority scores based on client SLA tiers, and routes to the optimal technician based on skills and workload. It handles 80%+ of routine classification automatically.',
    security: 'We maintain **SOC 2 Type II** certification and support **CMMC**, **HIPAA**, and **GDPR** compliance frameworks. Our Security Operations zone includes 13 process areas covering threat intelligence, incident response, EDR/XDR integration, and zero-knowledge vault encryption.',
    certification: 'DevOps AI supports multiple compliance frameworks including **SOC 2 Type II**, **CMMC 2.0** (with SSP builder), **HIPAA**, **GDPR**, and **NIST 800-171**. Our GRC zone automates evidence collection, gap analysis, and continuous monitoring.',
    pricing: 'DevOps AI offers three tiers:\n\n- **Starter** (1–3 techs): Core service desk + endpoint management\n- **Professional** (4–15 techs): All 15 zones + analytics\n- **Enterprise** (15+): Custom deployment, dedicated support, GCC High\n\nVisit our [pricing page](pricing.html) for details.',
    zone: 'DevOps AI covers **15 operational zones**: Service Desk, Security Operations, GRC & Compliance, Endpoint Management, Network Ops, vC-Suite, Analytics, Relationships, People, Learning, Organization, Legal, DevOps, Accounting, and Projects — with **157 process areas** total.',
    process: 'Each process area is a self-contained operational capability with AI automation, role-based access, and human-in-the-loop controls. Examples include Ticket Ingestion & AI Triage, Incident Response Orchestration, and CMMC SSP Builder.',
    connectwise: 'Unlike ConnectWise or Datto, DevOps AI is built **AI-first** — not bolted onto legacy PSA/RMM. Key differences:\n\n- **15 unified zones** vs. siloed tools\n- **AI-native automation** in every process area\n- **Full data sovereignty** — your data stays in your Azure tenant\n- **CMMC/GCC High** ready out of the box',
    different: 'DevOps AI is the first **AI-orchestrated MSP control plane**. Instead of stitching together PSA, RMM, security, and billing tools, we provide a single platform with 15 operational zones and 157 process areas — all powered by AI with human-in-the-loop controls.',
    ai: 'AI is embedded in every process area — from NLP ticket classification and predictive SLA management to automated compliance evidence collection and executive KPI dashboards. Our AI operates with transparent human-in-the-loop checkpoints so you stay in control.',
    demo: 'Great question! You can [request a demo](get-started.html) to see DevOps AI in action. Our team will walk you through the zones most relevant to your MSP operations.',
    endpoint: 'The Endpoint Management zone covers 10 process areas including automated patching, fleet intelligence, vulnerability management, and Intune integration. AI monitors device health in real-time and triggers remediation workflows automatically.',
    compliance: 'Our GRC & Compliance zone includes 11 process areas: Policy Management, Risk Management, Gap Analysis, CMMC SSP Builder, OSCAL Evidence, Audit Management, C3PAO Readiness, and more. AI automates evidence collection and maintains continuous compliance posture.',
    forge: 'DevOps AI is built on **FORGE** (Fixpoint Output Repair for Generative Engines) — a deterministic normalization engine that repairs structural defects in AI-generated content. FORGE makes no LLM calls, uses no randomness, and fails closed on ambiguity. Every AI output in DevOps AI passes through FORGE before reaching production. Learn more at [The FORGE Principle](/forge).',
    trust: 'DevOps AI provides **structural guarantees** that no other AI platform offers. FORGE normalizes every AI output across 23 content types — code, YAML, SQL, documents, and more — ensuring structural correctness is verified, not hoped for. Our convergence loop scans 6 dimensions in under 9 seconds on every change. Details: [fixpointforge.ai](https://fixpointforge.ai)',
    deterministic: 'FORGE is fully deterministic — same input always produces same output. It makes zero LLM calls, accesses no internet, and uses no randomness. Every repair is logged in an immutable audit trail. This is what makes DevOps AI the first platform that can **guarantee** the structural integrity of its AI outputs. Technical docs: [fixpointforge.dev](https://fixpointforge.dev)',
    convergence: 'DevOps AI uses a **fixpoint convergence loop** that scans 6 dimensions — code structure, AI governance, documentation, frontend/UI, conventions, and the public website — in a single pass under 9 seconds. Every PR is gated by this loop. The platform literally improves itself. [Learn more](/forge)',
    safe: 'Safety is built into every layer. **FORGE** guarantees structural correctness of AI output. **G1-G10 governance primitives** enforce action classification, confidence scoring, HITL approval, DLP scanning, audit trails, and tenant isolation on every AI action. Every consequential operation requires human approval. [Security details](/security)'
  };

  var DEFAULT_RESPONSE = "I can help you learn about DevOps AI — the world's first AI-first business automation platform, built on **FORGE** for deterministic trust. Ask me about:\n\n- What is FORGE and how does it work?\n- How AI ticket triage works\n- Security and trust guarantees\n- Pricing tiers\n- What makes us different\n\nOr [request a demo](get-started.html) to see the platform in action!";

  var SUGGESTED_PROMPTS = [
    'What is FORGE?',
    'How does DevOps AI use AI safely?',
    'What security certifications do you have?',
    'How is DevOps AI different?'
  ];

  var FAQ_ITEMS = [
    { q: 'What is DevOps AI?', a: 'DevOps AI is an AI-orchestrated MSP control plane with 15 operational zones and 157 process areas covering service desk, security, compliance, and more.' },
    { q: 'How many zones are there?', a: '15 zones: Service Desk, Security Operations, GRC & Compliance, Endpoint Management, Network Ops, vC-Suite, Analytics, Relationships, People, Learning, Organization, Legal, DevOps, Accounting, and Projects.' },
    { q: 'What compliance frameworks?', a: 'SOC 2 Type II, CMMC 2.0, HIPAA, GDPR, NIST 800-171, and more — with automated evidence collection and continuous monitoring.' },
    { q: 'Is there a free trial?', a: 'Contact our team to request a demo and discuss trial options tailored to your MSP size and needs.' },
    { q: 'What about data sovereignty?', a: 'Your data stays in your own Azure tenant. DevOps AI supports GCC High deployment for government contractors requiring ITAR/EAR compliance.' },
    { q: 'What is FORGE?', a: 'FORGE (Fixpoint Output Repair for Generative Engines) is the deterministic trust layer that DevOps AI is built on. It normalizes every AI output to guarantee structural correctness — no LLM calls, no randomness, fail-closed on ambiguity.' },
    { q: 'How does AI safety work?', a: 'Every AI action passes through 10 governance primitives (G1-G10): action classification, confidence scoring, chain-of-thought logging, HITL approval, DLP scanning, routing enforcement, rollback planning, audit trails, blast radius estimation, and tenant isolation.' }
  ];

  // ── State ───────────────────────────────────────────────────────────────
  var isOpen = false;
  var messages = [];
  var requestTimestamps = [];
  var isFallbackMode = false;

  // ── DOM refs ────────────────────────────────────────────────────────────
  var container, fab, tooltip, panel, panelHeader, panelClose, messagesEl,
      inputArea, inputField, sendBtn, typingIndicator;

  // ── Init ────────────────────────────────────────────────────────────────
  function init() {
    container = document.getElementById('chatbot-container');
    if (!container) return;

    loadHistory();
    buildDOM();
    bindEvents();

    // Show tooltip on first visit
    if (!sessionStorage.getItem(FIRST_VISIT_KEY)) {
      setTimeout(function () {
        if (tooltip) tooltip.classList.add('is-visible');
      }, 2000);
    }
  }

  // ── Build DOM ───────────────────────────────────────────────────────────
  function buildDOM() {
    container.innerHTML = '';
    container.setAttribute('role', 'complementary');
    container.setAttribute('aria-label', 'AI Chat Assistant');

    // FAB
    fab = el('button', {
      className: 'chatbot-fab',
      'aria-label': 'Open AI chat assistant',
      'aria-expanded': 'false',
      'aria-controls': 'chatbot-panel'
    });
    fab.innerHTML =
      '<svg class="chatbot-fab__icon chatbot-fab__icon--chat" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>' +
      '<svg class="chatbot-fab__icon chatbot-fab__icon--close" viewBox="0 0 24 24" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';

    // Tooltip
    tooltip = el('span', { className: 'chatbot-tooltip', 'aria-hidden': 'true' });
    tooltip.textContent = 'Ask AI';

    // Panel
    panel = el('div', {
      className: 'chatbot-panel',
      id: 'chatbot-panel',
      role: 'dialog',
      'aria-label': 'DevOps AI Assistant',
      'aria-hidden': 'true'
    });

    // Panel header
    panelHeader = el('div', { className: 'chatbot-panel__header' });
    var headerTitle = el('div', { className: 'chatbot-panel__title' });
    headerTitle.innerHTML = '<span class="chatbot-panel__indicator"></span>DevOps AI Assistant';
    panelClose = el('button', {
      className: 'chatbot-panel__close',
      'aria-label': 'Close chat'
    });
    panelClose.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>';
    panelHeader.appendChild(headerTitle);
    panelHeader.appendChild(panelClose);

    // Messages area
    messagesEl = el('div', {
      className: 'chatbot-messages',
      role: 'log',
      'aria-live': 'polite',
      'aria-label': 'Chat messages'
    });

    // Typing indicator (hidden by default)
    typingIndicator = el('div', { className: 'chatbot-typing', 'aria-hidden': 'true' });
    typingIndicator.innerHTML =
      '<span class="chatbot-typing__dot"></span>' +
      '<span class="chatbot-typing__dot"></span>' +
      '<span class="chatbot-typing__dot"></span>';

    // Input area
    inputArea = el('div', { className: 'chatbot-input' });
    inputField = el('textarea', {
      className: 'chatbot-input__field',
      placeholder: 'Ask about DevOps AI...',
      rows: '1',
      'aria-label': 'Type your message'
    });
    sendBtn = el('button', {
      className: 'chatbot-input__send',
      'aria-label': 'Send message',
      disabled: true
    });
    sendBtn.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>';
    inputArea.appendChild(inputField);
    inputArea.appendChild(sendBtn);

    // Assemble panel
    panel.appendChild(panelHeader);
    panel.appendChild(messagesEl);
    panel.appendChild(typingIndicator);
    panel.appendChild(inputArea);

    // Assemble container
    container.appendChild(fab);
    container.appendChild(tooltip);
    container.appendChild(panel);

    // Render messages or welcome
    if (messages.length > 0) {
      renderAllMessages();
    } else {
      renderWelcome();
    }
  }

  // ── Event binding ───────────────────────────────────────────────────────
  function bindEvents() {
    fab.addEventListener('click', togglePanel);
    panelClose.addEventListener('click', closePanel);

    inputField.addEventListener('input', function () {
      sendBtn.disabled = !inputField.value.trim();
      autoResize(inputField);
    });

    inputField.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSend();
      }
    });

    sendBtn.addEventListener('click', handleSend);

    // Escape closes panel
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen) {
        closePanel();
      }
    });

    // Tab trap inside panel
    panel.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || !isOpen) return;
      var focusable = getFocusable(panel);
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  // ── Toggle / Open / Close ───────────────────────────────────────────────
  function togglePanel() {
    if (isOpen) { closePanel(); } else { openPanel(); }
  }

  function openPanel() {
    isOpen = true;
    panel.classList.add('is-open');
    panel.setAttribute('aria-hidden', 'false');
    fab.classList.add('is-open');
    fab.setAttribute('aria-expanded', 'true');
    if (tooltip) tooltip.classList.remove('is-visible');
    sessionStorage.setItem(FIRST_VISIT_KEY, '1');

    // Prevent body scroll on mobile
    if (window.innerWidth < 768) {
      document.body.style.overflow = 'hidden';
    }

    // Focus input
    setTimeout(function () { inputField.focus(); }, 300);
    scrollMessages();
  }

  function closePanel() {
    isOpen = false;
    panel.classList.remove('is-open');
    panel.setAttribute('aria-hidden', 'true');
    fab.classList.remove('is-open');
    fab.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    fab.focus();
  }

  // ── Send message ────────────────────────────────────────────────────────
  function handleSend() {
    var text = inputField.value.trim();
    if (!text) return;

    // Rate limit check
    var now = Date.now();
    requestTimestamps = requestTimestamps.filter(function (t) { return now - t < RATE_WINDOW_MS; });
    if (requestTimestamps.length >= RATE_LIMIT) {
      addMessage('assistant', 'Please wait a moment before sending more messages. Rate limit reached.');
      return;
    }
    requestTimestamps.push(now);

    // Add user message
    addMessage('user', text);
    inputField.value = '';
    sendBtn.disabled = true;
    autoResize(inputField);

    // Show typing
    showTyping();

    // Try API, fall back to mock
    var endpoint = container.getAttribute('data-chatbot-endpoint');
    // API key removed from client-side (W4 chatbot isolation).
    // If a live endpoint is configured, it must handle auth server-side.

    if (endpoint && !isFallbackMode) {
      callAPI(endpoint, null, text)
        .then(function (response) {
          hideTyping();
          addMessage('assistant', response);
        })
        .catch(function () {
          isFallbackMode = true;
          hideTyping();
          respondMock(text);
        });
    } else if (isFallbackMode) {
      respondFallbackFAQ();
    } else {
      var delay = TYPING_DELAY_MIN + Math.random() * (TYPING_DELAY_MAX - TYPING_DELAY_MIN);
      setTimeout(function () {
        hideTyping();
        respondMock(text);
      }, delay);
    }
  }

  // ── API call ────────────────────────────────────────────────────────────
  function callAPI(endpoint, apiKey, text) {
    var history = messages.map(function (m) {
      return { role: m.role, content: m.content };
    });

    var headers = { 'Content-Type': 'application/json' };
    // NOTE: API key is never sent from the client. Authentication is handled
    // server-side by the proxy endpoint. This prevents key exposure in
    // client-side JavaScript. See WEBSITE_CONVERGENCE_PLAN.md W4.

    var controller = typeof AbortController !== 'undefined' ? new AbortController() : null;
    var timeoutId = setTimeout(function () {
      if (controller) controller.abort();
    }, API_TIMEOUT_MS);

    return fetch(endpoint, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify({ message: text, history: history }),
      signal: controller ? controller.signal : undefined
    })
    .then(function (res) {
      clearTimeout(timeoutId);
      if (!res.ok) throw new Error('API error: ' + res.status);
      return res.json();
    })
    .then(function (data) {
      return data.response || data.message || DEFAULT_RESPONSE;
    });
  }

  // ── Mock response ───────────────────────────────────────────────────────
  function respondMock(text) {
    var lower = text.toLowerCase();
    var response = DEFAULT_RESPONSE;

    var keywords = Object.keys(MOCK_RESPONSES);
    for (var i = 0; i < keywords.length; i++) {
      if (lower.indexOf(keywords[i]) !== -1) {
        response = MOCK_RESPONSES[keywords[i]];
        break;
      }
    }

    addMessage('assistant', response);
  }

  // ── Fallback FAQ ────────────────────────────────────────────────────────
  function respondFallbackFAQ() {
    hideTyping();
    var faqHtml = 'The AI service is temporarily unavailable. Here are some common questions:\n\n';
    FAQ_ITEMS.forEach(function (item) {
      faqHtml += '**' + item.q + '**\n' + item.a + '\n\n';
    });
    addMessage('assistant', faqHtml.trim());
  }

  // ── Messages ────────────────────────────────────────────────────────────
  function addMessage(role, content) {
    messages.push({ role: role, content: content, ts: Date.now() });
    renderMessage(role, content);
    saveHistory();
    scrollMessages();
  }

  function renderMessage(role, content) {
    var bubble = el('div', {
      className: 'chatbot-msg chatbot-msg--' + role
    });

    if (role === 'assistant') {
      bubble.innerHTML = renderMarkdown(content);
    } else {
      bubble.textContent = content;
    }

    messagesEl.appendChild(bubble);
  }

  function renderAllMessages() {
    messagesEl.innerHTML = '';
    messages.forEach(function (m) {
      renderMessage(m.role, m.content);
    });
  }

  function renderWelcome() {
    var welcome = el('div', { className: 'chatbot-welcome' });
    welcome.innerHTML =
      '<div class="chatbot-welcome__icon">🤖</div>' +
      '<p class="chatbot-welcome__title">Hi! I\'m the DevOps AI Assistant.</p>' +
      '<p class="chatbot-welcome__subtitle">Ask me anything about the platform.</p>';

    var prompts = el('div', { className: 'chatbot-prompts' });
    SUGGESTED_PROMPTS.forEach(function (text) {
      var btn = el('button', { className: 'chatbot-prompt-btn' });
      btn.textContent = text;
      btn.addEventListener('click', function () {
        inputField.value = text;
        sendBtn.disabled = false;
        handleSend();
      });
      prompts.appendChild(btn);
    });

    messagesEl.appendChild(welcome);
    messagesEl.appendChild(prompts);
  }

  // ── Typing indicator ────────────────────────────────────────────────────
  function showTyping() {
    typingIndicator.classList.add('is-visible');
    typingIndicator.setAttribute('aria-hidden', 'false');
  }

  function hideTyping() {
    typingIndicator.classList.remove('is-visible');
    typingIndicator.setAttribute('aria-hidden', 'true');
  }

  // ── Basic Markdown renderer ─────────────────────────────────────────────
  function renderMarkdown(text) {
    var html = escapeHtml(text);
    // Bold
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    // Italic
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
    // Inline code
    html = html.replace(/`(.+?)`/g, '<code>$1</code>');
    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    // Unordered lists
    html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>');
    // Paragraphs (double newline)
    html = html.replace(/\n\n/g, '</p><p>');
    // Single newlines within paragraphs
    html = html.replace(/\n/g, '<br>');
    html = '<p>' + html + '</p>';
    // Clean empty paragraphs
    html = html.replace(/<p><\/p>/g, '');
    html = html.replace(/<p>(<ul>)/g, '$1');
    html = html.replace(/(<\/ul>)<\/p>/g, '$1');
    return html;
  }

  // ── Session storage ─────────────────────────────────────────────────────
  function saveHistory() {
    try {
      sessionStorage.setItem(SESSION_KEY, JSON.stringify(messages));
    } catch (e) { /* quota exceeded or unavailable */ }
  }

  function loadHistory() {
    try {
      var stored = sessionStorage.getItem(SESSION_KEY);
      if (stored) messages = JSON.parse(stored);
    } catch (e) {
      messages = [];
    }
  }

  // ── Utilities ───────────────────────────────────────────────────────────
  function el(tag, attrs) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (key) {
        if (key === 'className') {
          node.className = attrs[key];
        } else {
          node.setAttribute(key, attrs[key]);
        }
      });
    }
    return node;
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  function scrollMessages() {
    requestAnimationFrame(function () {
      messagesEl.scrollTop = messagesEl.scrollHeight;
    });
  }

  function autoResize(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = Math.min(textarea.scrollHeight, 120) + 'px';
  }

  function getFocusable(root) {
    return Array.from(root.querySelectorAll(
      'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"])'
    )).filter(function (el) {
      return getComputedStyle(el).display !== 'none';
    });
  }

  // ── Start ───────────────────────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
