/* ========================================
   js/personalization.js — Personalization System (FR-W24)
   DevOps AI by RainTech

   Layer 1: GDPR-compliant consent manager
   Layer 2: Role identification (post-consent)
   Layer 3: Journey tracking (zone/PA visits)
   Layer 4: Personalized content surfacing

   Feature Flag: DEVOPS_AI_JOURNEY_ENTRY_POINT
   ======================================== */

(function () {
  'use strict';

  // ─── Feature Flags ───
  var DEVOPS_AI_JOURNEY_ENTRY_POINT = {
    enabled: true,
    mode: 'auto',
    showOnPages: ['index'],
    maxShowCount: 1,
    debug: false
  };

  // ─── Cookie Helpers ───
  function getCookie(name) {
    var m = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return m ? decodeURIComponent(m[2]) : null;
  }

  function setCookie(name, value, days) {
    var d = new Date();
    d.setTime(d.getTime() + (days * 86400000));
    document.cookie = name + '=' + encodeURIComponent(value) +
      ';expires=' + d.toUTCString() + ';path=/;SameSite=Lax';
  }

  function deleteCookie(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;';
  }

  // ─── Constants ───
  var CONSENT_COOKIE = 'devopsai_consent';
  var CONSENT_VERSION_COOKIE = 'devopsai_consent_v';
  var ROLE_COOKIE = 'devopsai_role';
  var JOURNEY_COOKIE = 'devopsai_journey';
  var STAGE_COOKIE = 'devopsai_stage';
  var VISIT_COOKIE = 'devopsai_visits';
  var ENTRY_SHOWN_COOKIE = 'devopsai_entry_shown';
  var COOKIE_DAYS = 365;
  var CONSENT_VERSION = 2; // Bump to re-trigger consent

  // ─── 21 Roles across 5 categories ───
  var ROLES = [
    // Executive Suite (5)
    { id: 'msp-owner',             label: 'MSP Owner / CEO',           icon: '🏢', page: 'roles/msp-owner.html',             group: 'executive' },
    { id: 'vcio',                  label: 'vCIO',                      icon: '📊', page: 'roles/vcio.html',                  group: 'executive' },
    { id: 'vciso',                 label: 'vCISO',                     icon: '🔒', page: 'roles/vciso.html',                 group: 'executive' },
    { id: 'vcco',                  label: 'vCCO',                      icon: '⚖️', page: 'roles/vcco.html',                  group: 'executive' },
    { id: 'vcto',                  label: 'vCTO',                      icon: '🔬', page: 'roles/vcto.html',                  group: 'executive' },
    // Operations (6)
    { id: 'it-director',           label: 'IT Director',               icon: '🖥️', page: 'roles/it-director.html',           group: 'operations' },
    { id: 'service-delivery-mgr',  label: 'Service Delivery Manager',  icon: '📋', page: 'roles/service-delivery-manager.html', group: 'operations' },
    { id: 'project-manager',       label: 'Project Manager',           icon: '📁', page: 'roles/project-manager.html',       group: 'operations' },
    { id: 'service-desk-manager',  label: 'Service Desk Manager',      icon: '🎫', page: 'roles/service-desk-manager.html',  group: 'operations' },
    { id: 'network-engineer',      label: 'Network Engineer',          icon: '🌐', page: 'roles/network-engineer.html',      group: 'operations' },
    { id: 'devops-engineer',       label: 'DevOps Engineer',           icon: '⚙️', page: 'roles/devops-engineer.html',       group: 'operations' },
    // Security & Compliance (2)
    { id: 'security-analyst',      label: 'Security Analyst',          icon: '🛡️', page: 'roles/security-analyst.html',      group: 'security' },
    { id: 'compliance-officer',    label: 'Compliance Officer',        icon: '📋', page: 'roles/compliance-officer.html',    group: 'security' },
    // Business & Relationships (5)
    { id: 'client-success-mgr',    label: 'Client Success Manager',    icon: '🌟', page: 'roles/client-success-manager.html', group: 'business' },
    { id: 'finance-coordinator',   label: 'Finance Coordinator',       icon: '💰', page: 'roles/finance-coordinator.html',   group: 'business' },
    { id: 'sales-director',        label: 'Sales Director',            icon: '📈', page: 'roles/sales-director.html',        group: 'business' },
    { id: 'marketing-director',    label: 'Marketing Director',        icon: '📣', page: 'roles/marketing-director.html',    group: 'business' },
    { id: 'data-analyst',          label: 'Data Analyst',              icon: '📉', page: 'roles/data-analyst.html',          group: 'business' },
    // People & Culture (3)
    { id: 'hr-director',           label: 'HR Director',               icon: '👥', page: 'roles/hr-director.html',           group: 'people' },
    { id: 'recruiter',             label: 'Recruiter',                 icon: '🔍', page: 'roles/recruiter.html',             group: 'people' },
    { id: 'legal-counsel',         label: 'Legal Counsel',             icon: '⚖️', page: 'roles/legal-counsel.html',         group: 'people' }
  ];

  // Lifecycle stages
  var STAGES = ['awareness', 'evaluation', 'onboarding', 'adoption', 'expansion'];

  // Zone recommendations per role (top 3 zones)
  var ROLE_ZONES = {
    'msp-owner':            ['vc-suite', 'analytics', 'relationships'],
    'vcio':                 ['vc-suite', 'projects', 'analytics'],
    'vciso':                ['security-operations', 'grc-compliance', 'vc-suite'],
    'vcco':                 ['grc-compliance', 'vc-suite', 'legal'],
    'vcto':                 ['devops', 'network-ops', 'vc-suite'],
    'it-director':          ['service-desk', 'endpoint-management', 'network-ops'],
    'service-delivery-mgr': ['service-desk', 'relationships', 'analytics'],
    'project-manager':      ['projects', 'service-desk', 'analytics'],
    'service-desk-manager': ['service-desk', 'endpoint-management', 'analytics'],
    'network-engineer':     ['network-ops', 'endpoint-management', 'security-operations'],
    'devops-engineer':      ['devops', 'network-ops', 'security-operations'],
    'security-analyst':     ['security-operations', 'grc-compliance', 'endpoint-management'],
    'compliance-officer':   ['grc-compliance', 'legal', 'security-operations'],
    'client-success-mgr':   ['relationships', 'service-desk', 'analytics'],
    'finance-coordinator':  ['accounting', 'analytics', 'relationships'],
    'sales-director':       ['relationships', 'analytics', 'vc-suite'],
    'marketing-director':   ['relationships', 'analytics', 'learning'],
    'data-analyst':         ['analytics', 'vc-suite', 'accounting'],
    'hr-director':          ['people', 'learning', 'organization'],
    'recruiter':            ['people', 'learning', 'organization'],
    'legal-counsel':        ['legal', 'grc-compliance', 'vc-suite']
  };

  // Role-specific hero subtext
  var ROLE_HERO_TEXT = {
    'msp-owner':            'See how DevOps AI drives revenue growth and operational excellence across your MSP.',
    'vcio':                 'Technology roadmaps, budget forecasting, and strategic advisory — powered by AI intelligence.',
    'vciso':                'Security program management, risk scoring, and compliance automation for your CISO practice.',
    'vcco':                 'Framework lifecycle management, audit automation, and compliance governance — streamlined.',
    'vcto':                 'Architecture reviews, technology evaluation, and engineering excellence — driven by data.',
    'it-director':          'Unify your service desk, endpoint management, and network ops into a single AI-driven platform.',
    'service-delivery-mgr': 'SLA tracking, QBR preparation, and client satisfaction analytics — orchestrated by AI.',
    'project-manager':      'Phase-gated execution, migration workflows, and real-time project intelligence.',
    'service-desk-manager': 'AI-powered triage, predictive SLA management, and intelligent dispatch optimization.',
    'network-engineer':     'Topology visualization, capacity forecasting, and automated patch management.',
    'devops-engineer':      'CI/CD pipelines, infrastructure automation, and platform operations — engineered for velocity.',
    'security-analyst':     'Real-time threat detection, automated incident response, and zero-trust governance — built for your SOC.',
    'compliance-officer':   'CMMC, SOC 2, HIPAA — continuous monitoring with OSCAL-native evidence collection.',
    'client-success-mgr':   'Client onboarding workflows, health scoring, churn prediction, and QBR delivery automation.',
    'finance-coordinator':  'Invoice ingestion, three-way reconciliation, and revenue recognition automation.',
    'sales-director':       'Lead generation, ICP scoring, sales pipeline management, and proposal workflow automation.',
    'marketing-director':   'Campaign orchestration, content management, and brand communications — AI-assisted.',
    'data-analyst':         'Cross-zone analytics, AI-generated report review, and data integrity assurance.',
    'hr-director':          'Workforce analytics, access lifecycle management, and automated onboarding workflows.',
    'recruiter':            'Skill gap analysis, onboarding automation, and directory synchronization.',
    'legal-counsel':        'Contract review, regulatory filings, and compliance documentation — managed and tracked.'
  };

  // Role group definitions
  var ROLE_GROUPS = {
    executive:  { label: 'Executive Suite',          color: '#8BDB02' },
    operations: { label: 'Operations',               color: '#20BAE7' },
    security:   { label: 'Security & Compliance',    color: '#C616EA' },
    business:   { label: 'Business & Relationships', color: '#17E4ED' },
    people:     { label: 'People & Culture',         color: '#2272E0' }
  };

  // Role descriptions (brief)
  var ROLE_DESCRIPTIONS = {
    'msp-owner':            'Revenue growth and operational excellence across your MSP',
    'vcio':                 'Technology roadmaps, budget forecasting, and strategic advisory',
    'vciso':                'Security program management, risk scoring, and compliance automation',
    'vcco':                 'Framework lifecycle, audit automation, and compliance governance',
    'vcto':                 'Architecture reviews, technology evaluation, and engineering excellence',
    'it-director':          'Unified service desk, endpoint management, and network operations',
    'service-delivery-mgr': 'SLA management, QBR preparation, and client satisfaction analytics',
    'project-manager':      'Phase-gated execution, migration workflows, and project intelligence',
    'service-desk-manager': 'AI-powered triage, predictive SLA management, and intelligent dispatch',
    'network-engineer':     'Topology visualization, capacity forecasting, and automated patching',
    'devops-engineer':      'CI/CD pipelines, infrastructure automation, and platform operations',
    'security-analyst':     'Real-time threat detection, automated incident response, zero-trust',
    'compliance-officer':   'CMMC, SOC 2, HIPAA — continuous monitoring with OSCAL-native evidence',
    'client-success-mgr':   'Client onboarding, health scoring, churn prediction, QBR delivery',
    'finance-coordinator':  'Invoice ingestion, three-way reconciliation, and revenue recognition',
    'sales-director':       'Lead generation, ICP scoring, sales pipeline, and proposal workflows',
    'marketing-director':   'Campaign orchestration, content management, and brand communications',
    'data-analyst':         'Cross-zone analytics, AI report review, and data integrity assurance',
    'hr-director':          'Workforce analytics, access lifecycle management, automated onboarding',
    'recruiter':            'Skill gap analysis, onboarding automation, and directory synchronization',
    'legal-counsel':        'Contract review, regulatory filings, and compliance documentation'
  };

  // Lifecycle-aware CTA text
  var LIFECYCLE_CTAS = {
    awareness:  { primary: 'Learn More', secondary: 'Explore the Platform' },
    evaluation: { primary: 'See It In Action', secondary: 'Compare Plans' },
    onboarding: { primary: 'Start Your Journey', secondary: 'Continue Setup' }
  };

  // ─── State ───
  var state = {
    consent: null,
    role: null,
    journey: [],
    stage: 'awareness',
    visits: 0
  };

  // ─── Initialize from cookies ───
  function loadState() {
    var c = getCookie(CONSENT_COOKIE);
    if (c) {
      try { state.consent = JSON.parse(c); } catch (e) { state.consent = null; }
    }

    // Check consent version — re-trigger if outdated
    var storedVersion = parseInt(getCookie(CONSENT_VERSION_COOKIE) || '0', 10);
    if (state.consent && storedVersion < CONSENT_VERSION) {
      state.consent = null;
      deleteCookie(CONSENT_COOKIE);
    }

    state.role = getCookie(ROLE_COOKIE);
    var j = getCookie(JOURNEY_COOKIE);
    if (j) {
      try { state.journey = JSON.parse(j); } catch (e) { state.journey = []; }
    }
    state.stage = getCookie(STAGE_COOKIE) || 'awareness';
    state.visits = parseInt(getCookie(VISIT_COOKIE) || '0', 10);
  }

  function saveConsent() {
    setCookie(CONSENT_COOKIE, JSON.stringify(state.consent), COOKIE_DAYS);
    setCookie(CONSENT_VERSION_COOKIE, String(CONSENT_VERSION), COOKIE_DAYS);
  }

  function saveRole() {
    if (state.role) setCookie(ROLE_COOKIE, state.role, COOKIE_DAYS);
  }

  function saveJourney() {
    if (state.consent && state.consent.personalization) {
      setCookie(JOURNEY_COOKIE, JSON.stringify(state.journey), COOKIE_DAYS);
      setCookie(STAGE_COOKIE, state.stage, COOKIE_DAYS);
      setCookie(VISIT_COOKIE, String(state.visits), COOKIE_DAYS);
    }
  }

  // ─── Path resolver ───
  function resolveRoot() {
    var path = window.location.pathname;
    if (path.indexOf('/zones/') >= 0 && path.indexOf('/process-areas/') >= 0) return '../../../';
    if (path.indexOf('/zones/') >= 0 || path.indexOf('/roles/') >= 0) return '../';
    return '';
  }

  function getCurrentPageSlug() {
    var path = window.location.pathname;
    var page = path.split('/').pop() || '';
    page = page.replace(/\.html$/, '');
    return page || 'index';
  }

  // ─── Feature flag checks ───
  function shouldShowEntryPoint() {
    if (!DEVOPS_AI_JOURNEY_ENTRY_POINT.enabled) return false;
    if (state.role) return false;

    var pages = DEVOPS_AI_JOURNEY_ENTRY_POINT.showOnPages;
    if (pages && pages.length > 0) {
      var currentPage = getCurrentPageSlug();
      if (pages.indexOf(currentPage) === -1) return false;
    }

    var maxCount = DEVOPS_AI_JOURNEY_ENTRY_POINT.maxShowCount || 1;
    var shownCount = parseInt(getCookie(ENTRY_SHOWN_COOKIE) || '0', 10);
    if (shownCount >= maxCount) return false;

    return true;
  }

  function trackEntryPointShown() {
    var shownCount = parseInt(getCookie(ENTRY_SHOWN_COOKIE) || '0', 10);
    setCookie(ENTRY_SHOWN_COOKIE, String(shownCount + 1), COOKIE_DAYS);
  }

  // ─────────────────────────────────────────
  // LAYER 1: Consent Manager
  // ─────────────────────────────────────────

  function buildConsentBanner() {
    var existing = document.querySelector('.consent-banner');
    if (existing) existing.remove();

    var banner = document.createElement('div');
    banner.className = 'consent-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie preferences');
    banner.innerHTML =
      '<div class="consent-banner__inner">' +
        '<div class="consent-banner__text">' +
          '<strong>Your Privacy Matters</strong>' +
          '<p>We use cookies to keep the site running, understand how you use it, and personalize your experience. You choose what to allow.</p>' +
        '</div>' +
        '<div class="consent-banner__categories">' +
          '<label class="consent-cat">' +
            '<input type="checkbox" checked disabled> ' +
            '<div><span class="consent-cat__name">Essential</span>' +
            '<span class="consent-cat__desc">Required for the site to function. Always on.</span></div>' +
          '</label>' +
          '<label class="consent-cat">' +
            '<input type="checkbox" id="consent-analytics" checked> ' +
            '<div><span class="consent-cat__name">Analytics</span>' +
            '<span class="consent-cat__desc">Helps us understand site usage to improve the experience.</span></div>' +
          '</label>' +
          '<label class="consent-cat">' +
            '<input type="checkbox" id="consent-personalization" checked> ' +
            '<div><span class="consent-cat__name">Personalization</span>' +
            '<span class="consent-cat__desc">Remembers your role and preferences for a tailored experience.</span></div>' +
          '</label>' +
        '</div>' +
        '<details class="consent-details">' +
          '<summary class="consent-details__toggle">What do we track?</summary>' +
          '<div class="consent-details__body">' +
            '<p><strong>Essential:</strong> Theme preference, session state. No personal data.</p>' +
            '<p><strong>Analytics:</strong> Page views, time on site, navigation paths. Aggregated, never sold.</p>' +
            '<p><strong>Personalization:</strong> Selected role, visited zones/PAs, lifecycle stage. Stored locally in cookies.</p>' +
          '</div>' +
        '</details>' +
        '<div class="consent-banner__actions">' +
          '<button class="consent-btn consent-btn--reject">Essential Only</button>' +
          '<button class="consent-btn consent-btn--save">Save Preferences</button>' +
          '<button class="consent-btn consent-btn--accept">Accept All</button>' +
        '</div>' +
        '<a href="' + resolveRoot() + 'privacy.html" class="consent-banner__link">Privacy Policy</a>' +
      '</div>';

    document.body.appendChild(banner);

    requestAnimationFrame(function () {
      banner.classList.add('is-visible');
    });

    banner.querySelector('.consent-btn--accept').addEventListener('click', function () {
      state.consent = { essential: true, analytics: true, personalization: true };
      saveConsent();
      hideConsentBanner(banner);
      onConsentGranted();
    });

    banner.querySelector('.consent-btn--reject').addEventListener('click', function () {
      state.consent = { essential: true, analytics: false, personalization: false };
      saveConsent();
      hideConsentBanner(banner);
    });

    banner.querySelector('.consent-btn--save').addEventListener('click', function () {
      state.consent = {
        essential: true,
        analytics: !!document.getElementById('consent-analytics').checked,
        personalization: !!document.getElementById('consent-personalization').checked
      };
      saveConsent();
      hideConsentBanner(banner);
      if (state.consent.personalization) onConsentGranted();
    });
  }

  function hideConsentBanner(banner) {
    banner.classList.remove('is-visible');
    setTimeout(function () { banner.remove(); }, 350);
  }

  // ─────────────────────────────────────────
  // LAYER 2: Role Identification
  // ─────────────────────────────────────────

  // Fallback bottom-sheet role picker
  function showRolePicker() {
    if (state.role) return;

    var picker = document.createElement('div');
    picker.className = 'role-picker';
    picker.setAttribute('role', 'dialog');
    picker.setAttribute('aria-label', 'Select your role');

    var pills = ROLES.map(function (r) {
      return '<button class="role-pill" data-role="' + r.id + '">' +
        '<span class="role-pill__icon">' + r.icon + '</span>' +
        '<span class="role-pill__label">' + r.label + '</span>' +
      '</button>';
    }).join('');

    picker.innerHTML =
      '<div class="role-picker__inner">' +
        '<div class="role-picker__header">' +
          '<span class="role-picker__title">What best describes your role?</span>' +
          '<button class="role-picker__close" aria-label="Dismiss">&times;</button>' +
        '</div>' +
        '<p class="role-picker__subtitle">We\'ll tailor your experience to show the most relevant capabilities.</p>' +
        '<div class="role-picker__grid">' + pills + '</div>' +
      '</div>';

    document.body.appendChild(picker);

    setTimeout(function () { picker.classList.add('is-visible'); }, 400);

    picker.querySelector('.role-picker__close').addEventListener('click', function () {
      hideRolePicker(picker);
    });

    picker.querySelectorAll('.role-pill').forEach(function (btn) {
      btn.addEventListener('click', function () {
        state.role = this.getAttribute('data-role');
        saveRole();
        hideRolePicker(picker);
        onRoleSelected();
      });
    });
  }

  function hideRolePicker(picker) {
    picker.classList.remove('is-visible');
    setTimeout(function () { picker.remove(); }, 350);
  }

  // ─────────────────────────────────────────
  // LAYER 2b: Journey Entry Point
  // ─────────────────────────────────────────

  function showJourneyEntryPoint() {
    if (state.role) return;

    trackEntryPointShown();

    var entryPointConfig = {
      roles: ROLES.map(function (r) {
        return {
          id: r.id,
          label: r.label,
          desc: ROLE_DESCRIPTIONS[r.id] || '',
          zones: (ROLE_ZONES[r.id] || []).slice(0, 3),
          group: r.group
        };
      }),
      groups: ROLE_GROUPS,
      mode: DEVOPS_AI_JOURNEY_ENTRY_POINT.mode || 'auto',
      debug: DEVOPS_AI_JOURNEY_ENTRY_POINT.debug || false,
      onRoleSelected: function (roleId) {
        state.role = roleId;
        saveRole();
        onRoleSelected();
      },
      resolveRoot: resolveRoot
    };

    window.__DEVOPS_AI_ENTRY_POINT__ = entryPointConfig;

    if (!document.getElementById('devopsai-entry-point-script')) {
      var script = document.createElement('script');
      script.id = 'devopsai-entry-point-script';
      script.src = resolveRoot() + 'js/entry-point.js';
      document.body.appendChild(script);
    } else {
      if (window.__devopsAIEntryPointInit) {
        window.__devopsAIEntryPointInit(entryPointConfig);
      }
    }
  }

  // ─────────────────────────────────────────
  // LAYER 3: Journey Tracking
  // ─────────────────────────────────────────

  function trackPageVisit() {
    if (!state.consent || !state.consent.personalization) return;

    state.visits++;

    var path = window.location.pathname;
    var slug = null;

    var paMatch = path.match(/\/zones\/[^/]+\/process-areas\/([^/]+?)(?:\.html)?$/);
    if (paMatch) slug = 'pa:' + paMatch[1];

    var zoneMatch = !slug && path.match(/\/zones\/([^/]+?)(?:\/index)?(?:\.html)?$/);
    if (zoneMatch) slug = 'zone:' + zoneMatch[1];

    var roleMatch = path.match(/\/roles\/([^/]+?)(?:\.html)?$/);
    if (roleMatch && roleMatch[1] !== 'index') slug = 'role:' + roleMatch[1];

    if (!slug) {
      var page = path.split('/').pop() || 'index';
      slug = 'page:' + page.replace(/\.html$/, '');
      if (!slug || slug === 'page:') slug = 'page:index';
    }

    if (slug && state.journey.indexOf(slug) === -1) {
      state.journey.push(slug);
      if (state.journey.length > 30) state.journey.shift();
    }

    inferStage();
    saveJourney();
  }

  function inferStage() {
    var zoneVisits = state.journey.filter(function (s) { return s.indexOf('zone:') === 0; }).length;
    var paVisits = state.journey.filter(function (s) { return s.indexOf('pa:') === 0; }).length;
    var hasVisitedPricing = state.journey.indexOf('page:pricing') >= 0;
    var hasVisitedContact = state.journey.indexOf('page:contact') >= 0;
    var hasVisitedGetStarted = state.journey.indexOf('page:get-started') >= 0;

    if (hasVisitedGetStarted || hasVisitedContact) {
      state.stage = 'onboarding';
    } else if (hasVisitedPricing || paVisits >= 3) {
      state.stage = 'evaluation';
    } else if (zoneVisits >= 2 || state.visits >= 5) {
      state.stage = 'evaluation';
    } else {
      state.stage = 'awareness';
    }
  }

  // ─────────────────────────────────────────
  // LAYER 4: Personalized Content Surfacing
  // ─────────────────────────────────────────

  function onConsentGranted() {
    if (state.consent.personalization && !state.role) {
      if (shouldShowEntryPoint()) {
        setTimeout(showJourneyEntryPoint, 800);
      } else {
        setTimeout(showRolePicker, 800);
      }
    }
    if (state.consent.personalization) {
      trackPageVisit();
    }
  }

  function onRoleSelected() {
    var entryPoint = document.getElementById('devopsai-entry-point');
    if (entryPoint) {
      entryPoint.classList.add('is-hidden');
      setTimeout(function () { entryPoint.remove(); }, 600);
    }
    applyPersonalization();
  }

  function applyPersonalization() {
    if (!state.role || !state.consent || !state.consent.personalization) return;

    var root = resolveRoot();
    var roleData = ROLES.find(function (r) { return r.id === state.role; });
    if (!roleData) return;

    if (state.visits > 1) insertWelcomeBar(roleData, root);
    personalizeHero(roleData);
    insertRecommendedZones(roleData, root);
    personalizeCtAs(roleData, root);
  }

  function insertWelcomeBar(roleData, root) {
    var header = document.querySelector('.site-header');
    if (!header || document.querySelector('.welcome-bar')) return;

    var recentZones = state.journey
      .filter(function (s) { return s.indexOf('zone:') === 0; })
      .slice(-3)
      .map(function (s) { return s.replace('zone:', ''); });

    var continueHtml = '';
    if (recentZones.length > 0) {
      var last = recentZones[recentZones.length - 1];
      var zoneName = last.replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
      continueHtml = ' · <a href="' + root + 'zones/' + last + '/index.html" class="welcome-bar__link">Continue exploring ' + zoneName + ' →</a>';
    }

    // Recent PA link
    var recentPAs = state.journey
      .filter(function (s) { return s.indexOf('pa:') === 0; })
      .slice(-1)
      .map(function (s) { return s.replace('pa:', ''); });

    var lastPaHtml = '';
    if (recentPAs.length > 0) {
      var lastPa = recentPAs[0];
      var paName = lastPa.replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
      lastPaHtml = ' · <span class="welcome-bar__breadcrumb">Last viewed: ' + paName + '</span>';
    }

    var bar = document.createElement('div');
    bar.className = 'welcome-bar';
    bar.innerHTML =
      '<div class="welcome-bar__inner">' +
        '<span class="welcome-bar__greeting">' +
          roleData.icon + ' Welcome back, ' + roleData.label +
          ' · <a href="' + root + roleData.page + '" class="welcome-bar__link">Your Journey</a>' +
          continueHtml + lastPaHtml +
        '</span>' +
        '<button class="welcome-bar__change" title="Change role">Change Role</button>' +
      '</div>';

    header.insertAdjacentElement('afterend', bar);

    bar.querySelector('.welcome-bar__change').addEventListener('click', function () {
      deleteCookie(ROLE_COOKIE);
      state.role = null;
      bar.remove();
      if (shouldShowEntryPoint()) {
        showJourneyEntryPoint();
      } else {
        showRolePicker();
      }
    });
  }

  function personalizeHero(roleData) {
    var page = getCurrentPageSlug();
    if (page !== 'index' && page !== '') return;

    var heroText = ROLE_HERO_TEXT[state.role];
    if (!heroText) return;

    var heroSubtitle = document.querySelector('.hero-subtitle, .hero p, .hero__subtitle');
    if (heroSubtitle) {
      heroSubtitle.setAttribute('data-original', heroSubtitle.textContent);
      heroSubtitle.textContent = heroText;
      heroSubtitle.style.transition = 'opacity 0.3s ease';
    }
  }

  function insertRecommendedZones(roleData, root) {
    var page = getCurrentPageSlug();
    if (page !== 'index' && page !== '' && page !== 'platform') return;

    var zones = ROLE_ZONES[state.role];
    if (!zones || zones.length === 0) return;

    var target = document.querySelector('main .zone-grid, main .platform-zones, .hero-section, .hero');
    if (!target) target = document.querySelector('main > section:first-of-type');
    if (!target || document.querySelector('.recommended-zones')) return;

    var zoneCards = zones.map(function (z) {
      var name = z.replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
      return '<a href="' + root + 'zones/' + z + '/index.html" class="rec-zone-card">' +
        '<span class="rec-zone-card__name">' + name + '</span>' +
        '<span class="rec-zone-card__arrow">→</span>' +
      '</a>';
    }).join('');

    var section = document.createElement('div');
    section.className = 'recommended-zones fade-up';
    section.innerHTML =
      '<div class="recommended-zones__header">' +
        '<span class="recommended-zones__badge">' + roleData.icon + ' For ' + roleData.label + 's</span>' +
        '<span class="recommended-zones__label">Recommended starting points</span>' +
      '</div>' +
      '<div class="recommended-zones__grid">' + zoneCards + '</div>';

    target.parentNode.insertBefore(section, target.nextSibling);

    requestAnimationFrame(function () {
      section.classList.add('is-visible');
    });
  }

  function personalizeCtAs(roleData, root) {
    var ctaConfig = LIFECYCLE_CTAS[state.stage] || LIFECYCLE_CTAS.awareness;

    // Update primary CTAs based on lifecycle stage
    var ctas = document.querySelectorAll('.nav-cta, [class*="cta"]');
    ctas.forEach(function (cta) {
      if (cta.getAttribute('data-personalized')) return;

      var text = (cta.textContent || '').trim();
      if (text === 'Get Started →' || text === 'Get Started') {
        cta.setAttribute('data-personalized', 'true');
        if (state.stage === 'evaluation') {
          cta.textContent = ctaConfig.primary + ' →';
        } else if (state.stage === 'onboarding') {
          cta.textContent = ctaConfig.primary + ' →';
        }
      }
    });
  }

  // ─── Footer: Manage Preferences Link ───
  function addManagePreferencesLink() {
    var footer = document.querySelector('.site-footer');
    if (!footer || document.querySelector('.manage-cookies-link')) return;

    var link = document.createElement('a');
    link.href = '#';
    link.className = 'manage-cookies-link';
    link.textContent = 'Manage Cookie Preferences';
    link.addEventListener('click', function (e) {
      e.preventDefault();
      deleteCookie(CONSENT_COOKIE);
      state.consent = null;
      buildConsentBanner();
    });

    var footerLinks = footer.querySelector('.footer-bottom');
    if (footerLinks) {
      footerLinks.appendChild(link);
    } else {
      footer.appendChild(link);
    }
  }

  // ─── Boot Sequence ───
  document.addEventListener('DOMContentLoaded', function () {
    loadState();
    addManagePreferencesLink();

    if (!state.consent) {
      setTimeout(function () { buildConsentBanner(); }, 1200);
    } else {
      if (state.consent.personalization) {
        trackPageVisit();
        applyPersonalization();

        if (!state.role && state.visits >= 2) {
          if (shouldShowEntryPoint()) {
            setTimeout(showJourneyEntryPoint, 2000);
          } else {
            setTimeout(showRolePicker, 2000);
          }
        }
      } else if (state.consent.analytics) {
        trackPageVisit();
      }
    }
  });

  // ─── Public API ───
  window.DevOpsAIPersonalization = {
    getEntryPointConfig: function () {
      return JSON.parse(JSON.stringify(DEVOPS_AI_JOURNEY_ENTRY_POINT));
    },
    setEntryPointEnabled: function (enabled) {
      DEVOPS_AI_JOURNEY_ENTRY_POINT.enabled = !!enabled;
    },
    updateEntryPointConfig: function (partial) {
      if (partial.enabled !== undefined) DEVOPS_AI_JOURNEY_ENTRY_POINT.enabled = !!partial.enabled;
      if (partial.mode) DEVOPS_AI_JOURNEY_ENTRY_POINT.mode = partial.mode;
      if (partial.showOnPages) DEVOPS_AI_JOURNEY_ENTRY_POINT.showOnPages = partial.showOnPages;
      if (partial.maxShowCount !== undefined) DEVOPS_AI_JOURNEY_ENTRY_POINT.maxShowCount = partial.maxShowCount;
      if (partial.debug !== undefined) DEVOPS_AI_JOURNEY_ENTRY_POINT.debug = !!partial.debug;
    },
    resetRole: function () {
      deleteCookie(ROLE_COOKIE);
      state.role = null;
      var welcomeBar = document.querySelector('.welcome-bar');
      if (welcomeBar) welcomeBar.remove();
    },
    getState: function () { return JSON.parse(JSON.stringify(state)); },
    getRoles: function () { return JSON.parse(JSON.stringify(ROLES)); },
    getRoleGroups: function () { return JSON.parse(JSON.stringify(ROLE_GROUPS)); }
  };

})();
