/* ========================================
   personalization.js — 4-Layer Cookie Personalization
   DevOps AI by RainTech
   
   Layer 1: GDPR-compliant consent manager
   Layer 2: Role identification (post-consent)
   Layer 3: Journey tracking (zone/PA visits)
   Layer 4: Personalized content surfacing

   Feature Flag: DEVOPS_AI_JOURNEY_ENTRY_POINT
   Controlled via BD Zone → Customer Journey / CRM control plane (FR-001)
   ======================================== */

(function() {
  'use strict';

  // ─── Feature Flags ───
  // Follows the DEVOPS_AI_* naming convention for platform-managed feature flags.
  // In production, these values are served from the DevOps AI platform's
  // BD Zone → Customer Journey / CRM control plane (FR-001).
  // HITL approval required before activating on the public website.
  //
  // To toggle: set `enabled` to true/false. When disabled, the original
  // bottom-sheet role picker is used. When enabled, the full-screen neural
  // network Journey Entry Point replaces the role picker experience.
  var DEVOPS_AI_JOURNEY_ENTRY_POINT = {
    enabled: true,           // Master toggle — can be flipped from the BD Zone control plane
    mode: 'auto',            // 'auto' = tier-detect (3D vs card-grid), '3d' = force 3D, 'cards' = force card grid
    showOnPages: ['index'],  // Pages where the full entry point appears (empty = all pages)
    maxShowCount: 1,         // Max times to show per session before falling back to welcome bar
    debug: false             // Show tier indicator and console logging
  };

  // ─── Cookie Helpers ───
  function getCookie(name) {
    var m = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return m ? decodeURIComponent(m[2]) : null;
  }

  function setCookie(name, value, days) {
    var d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = name + '=' + encodeURIComponent(value) +
      ';expires=' + d.toUTCString() + ';path=/;SameSite=Lax';
  }

  function deleteCookie(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;';
  }

  // ─── Constants ───
  var CONSENT_COOKIE = 'devopsai_consent';
  var ROLE_COOKIE = 'devopsai_role';
  var JOURNEY_COOKIE = 'devopsai_journey';
  var STAGE_COOKIE = 'devopsai_stage';
  var VISIT_COOKIE = 'devopsai_visits';
  var ENTRY_SHOWN_COOKIE = 'devopsai_entry_shown';
  var COOKIE_DAYS = 365;

  // ─── Roles (20 roles across 5 categories) ───
  var ROLES = [
    // Executive Suite
    { id: 'msp-owner',            label: 'MSP Owner / CEO',       icon: '🏢', page: 'roles/msp-owner.html',            group: 'executive' },
    { id: 'vcio',                 label: 'vCIO',                  icon: '📊', page: 'roles/vcio.html',                 group: 'executive' },
    { id: 'vciso',                label: 'vCISO',                 icon: '🔒', page: 'roles/vciso.html',                group: 'executive' },
    { id: 'vcco',                 label: 'vCCO',                  icon: '⚖️', page: 'roles/vcco.html',                 group: 'executive' },
    // Operations
    { id: 'it-director',          label: 'IT Director',           icon: '🖥️', page: 'roles/it-director.html',          group: 'operations' },
    { id: 'service-desk-manager', label: 'Service Desk Manager',  icon: '🎫', page: 'roles/service-desk-manager.html', group: 'operations' },
    { id: 'network-engineer',     label: 'Network Engineer',      icon: '🌐', page: 'roles/network-engineer.html',     group: 'operations' },
    { id: 'project-manager',      label: 'Project Manager',       icon: '📁', page: 'roles/project-manager.html',      group: 'operations' },
    { id: 'devops-engineer',      label: 'DevOps Engineer',       icon: '⚙️', page: 'roles/devops-engineer.html',      group: 'operations' },
    // Security & Compliance
    { id: 'security-analyst',     label: 'Security Analyst',      icon: '🛡️', page: 'roles/security-analyst.html',     group: 'security' },
    { id: 'compliance-officer',   label: 'Compliance Officer',    icon: '📋', page: 'roles/compliance-officer.html',   group: 'security' },
    // Business & Relationships
    { id: 'account-manager',      label: 'Account Manager',       icon: '🤝', page: 'roles/account-manager.html',      group: 'business' },
    { id: 'finance-coordinator',  label: 'Finance Coordinator',   icon: '💰', page: 'roles/finance-coordinator.html',  group: 'business' },
    { id: 'sales-director',       label: 'Sales Director',        icon: '📈', page: 'roles/sales-director.html',       group: 'business' },
    { id: 'marketing-director',   label: 'Marketing Director',    icon: '📣', page: 'roles/marketing-director.html',   group: 'business' },
    { id: 'client-success-mgr',   label: 'Client Success Manager',icon: '🌟', page: 'roles/client-success-manager.html', group: 'business' },
    { id: 'data-analyst',         label: 'Data Analyst / BI Lead',icon: '📉', page: 'roles/data-analyst.html',         group: 'business' },
    // People & Culture
    { id: 'hr-director',          label: 'HR Director',           icon: '👥', page: 'roles/hr-director.html',          group: 'people' },
    { id: 'recruiter',            label: 'Recruiter',             icon: '🔍', page: 'roles/recruiter.html',            group: 'people' },
    { id: 'legal-counsel',        label: 'Legal Counsel',         icon: '⚖️', page: 'roles/legal-counsel.html',        group: 'people' }
  ];

  // Lifecycle stages: Awareness → Evaluation → Onboarding → Adoption → Expansion
  var STAGES = ['awareness', 'evaluation', 'onboarding', 'adoption', 'expansion'];

  // Zone recommendations per role (top 3 zones to highlight)
  var ROLE_ZONES = {
    'msp-owner':            ['vc-suite', 'analytics', 'relationships'],
    'it-director':          ['service-desk', 'endpoint-management', 'network-ops'],
    'security-analyst':     ['security-operations', 'grc-compliance', 'endpoint-management'],
    'vcio':                 ['vc-suite', 'projects', 'analytics'],
    'vciso':                ['security-operations', 'grc-compliance', 'vc-suite'],
    'vcco':                 ['grc-compliance', 'vc-suite', 'legal'],
    'compliance-officer':   ['grc-compliance', 'legal', 'security-operations'],
    'service-desk-manager': ['service-desk', 'endpoint-management', 'analytics'],
    'network-engineer':     ['network-ops', 'endpoint-management', 'security-operations'],
    'project-manager':      ['projects', 'service-desk', 'analytics'],
    'account-manager':      ['relationships', 'analytics', 'vc-suite'],
    'finance-coordinator':  ['accounting', 'analytics', 'relationships'],
    'hr-director':          ['people', 'learning', 'organization'],
    'recruiter':            ['people', 'learning', 'organization'],
    // New roles (6 additions)
    'devops-engineer':      ['devops', 'network-ops', 'security-operations'],
    'sales-director':       ['relationships', 'analytics', 'vc-suite'],
    'marketing-director':   ['relationships', 'analytics', 'learning'],
    'client-success-mgr':   ['relationships', 'service-desk', 'analytics'],
    'data-analyst':         ['analytics', 'vc-suite', 'accounting'],
    'legal-counsel':        ['legal', 'grc-compliance', 'vc-suite']
  };

  // Role-specific hero subtext
  var ROLE_HERO_TEXT = {
    'msp-owner':            'See how DevOps AI drives revenue growth and operational excellence across your MSP.',
    'it-director':          'Unify your service desk, endpoint management, and network ops into a single AI-driven platform.',
    'security-analyst':     'Real-time threat detection, automated incident response, and zero-trust governance — built for your SOC.',
    'vcio':                 'Technology roadmaps, budget forecasting, and strategic advisory — powered by AI intelligence.',
    'vciso':                'Security program management, risk scoring, and compliance automation for your CISO practice.',
    'vcco':                 'Framework lifecycle management, audit automation, and compliance governance — streamlined.',
    'compliance-officer':   'CMMC, SOC 2, HIPAA — continuous monitoring with OSCAL-native evidence collection.',
    'service-desk-manager': 'AI-powered triage, predictive SLA management, and intelligent dispatch optimization.',
    'network-engineer':     'Topology visualization, capacity forecasting, and automated patch management.',
    'project-manager':      'Phase-gated execution, migration workflows, and real-time project intelligence.',
    'account-manager':      'Client health scoring, churn prediction, and QBR preparation — all automated.',
    'finance-coordinator':  'Invoice ingestion, three-way reconciliation, and revenue recognition automation.',
    'hr-director':          'Workforce analytics, access lifecycle management, and automated onboarding workflows.',
    'recruiter':            'Skill gap analysis, onboarding automation, and directory synchronization.',
    // New roles (6 additions)
    'devops-engineer':      'CI/CD pipelines, infrastructure automation, and platform operations — engineered for velocity.',
    'sales-director':       'Lead generation, ICP scoring, sales pipeline management, and proposal workflow automation.',
    'marketing-director':   'Campaign orchestration, content management, and brand communications — AI-assisted.',
    'client-success-mgr':   'Client onboarding workflows, health scoring, churn prediction, and QBR delivery automation.',
    'data-analyst':         'Cross-zone analytics, AI-generated report review, and data integrity assurance.',
    'legal-counsel':        'Contract review, regulatory filings, and compliance documentation — managed and tracked.'
  };

  // Role group definitions (used by entry point)
  var ROLE_GROUPS = {
    executive:  { label: 'Executive Suite',           color: '#8BDB02' },
    operations: { label: 'Operations',                color: '#20BAE7' },
    security:   { label: 'Security & Compliance',     color: '#C616EA' },
    business:   { label: 'Business & Relationships',  color: '#17E4ED' },
    people:     { label: 'People & Culture',          color: '#2272E0' }
  };

  // Role descriptions (used by entry point detail panel)
  var ROLE_DESCRIPTIONS = {
    'msp-owner':            'Revenue growth and operational excellence across your MSP',
    'vcio':                 'Technology roadmaps, budget forecasting, and strategic advisory',
    'vciso':                'Security program management, risk scoring, and compliance automation',
    'vcco':                 'Framework lifecycle, audit automation, and compliance governance',
    'it-director':          'Unified service desk, endpoint management, and network operations',
    'service-desk-manager': 'AI-powered triage, predictive SLA management, and intelligent dispatch',
    'network-engineer':     'Topology visualization, capacity forecasting, and automated patching',
    'project-manager':      'Phase-gated execution, migration workflows, and project intelligence',
    'devops-engineer':      'CI/CD pipelines, infrastructure automation, and platform operations',
    'security-analyst':     'Real-time threat detection, automated incident response, zero-trust',
    'compliance-officer':   'CMMC, SOC 2, HIPAA — continuous monitoring with OSCAL-native evidence',
    'account-manager':      'Client health scoring, churn prediction, and QBR preparation',
    'finance-coordinator':  'Invoice ingestion, three-way reconciliation, and revenue recognition',
    'sales-director':       'Lead generation, ICP scoring, sales pipeline, and proposal workflows',
    'marketing-director':   'Campaign orchestration, content management, and brand communications',
    'client-success-mgr':   'Client onboarding, health scoring, churn prediction, QBR delivery',
    'data-analyst':         'Cross-zone analytics, AI report review, and data integrity assurance',
    'hr-director':          'Workforce analytics, access lifecycle management, automated onboarding',
    'recruiter':            'Skill gap analysis, onboarding automation, and directory synchronization',
    'legal-counsel':        'Contract review, regulatory filings, and compliance documentation'
  };

  // ─── State ───
  var state = {
    consent: null,       // { essential: true, analytics: bool, personalization: bool }
    role: null,          // string role ID
    journey: [],         // array of visited zone/PA slugs
    stage: 'awareness',  // lifecycle stage
    visits: 0            // total page visits
  };

  // ─── Initialize from cookies ───
  function loadState() {
    var c = getCookie(CONSENT_COOKIE);
    if (c) {
      try { state.consent = JSON.parse(c); } catch(e) { state.consent = null; }
    }
    state.role = getCookie(ROLE_COOKIE);
    var j = getCookie(JOURNEY_COOKIE);
    if (j) {
      try { state.journey = JSON.parse(j); } catch(e) { state.journey = []; }
    }
    state.stage = getCookie(STAGE_COOKIE) || 'awareness';
    state.visits = parseInt(getCookie(VISIT_COOKIE) || '0', 10);
  }

  function saveConsent() {
    setCookie(CONSENT_COOKIE, JSON.stringify(state.consent), COOKIE_DAYS);
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

  // ─── Utility: resolve relative path ───
  function resolveRoot() {
    var path = window.location.pathname;
    if (path.indexOf('/zones/') >= 0 && path.indexOf('/process-areas/') >= 0) return '../../../';
    if (path.indexOf('/zones/') >= 0 || path.indexOf('/roles/') >= 0 || path.indexOf('/legal/') >= 0) return '../';
    return '';
  }

  // ─── Utility: detect current page slug ───
  function getCurrentPageSlug() {
    var path = window.location.pathname;
    var page = path.split('/').pop() || '';
    page = page.replace(/\.html$/, '');
    return page || 'index';
  }

  // ─── Feature Flag: Should show entry point? ───
  function shouldShowEntryPoint() {
    if (!DEVOPS_AI_JOURNEY_ENTRY_POINT.enabled) return false;
    if (state.role) return false; // Already identified

    // Check page filter
    var pages = DEVOPS_AI_JOURNEY_ENTRY_POINT.showOnPages;
    if (pages && pages.length > 0) {
      var currentPage = getCurrentPageSlug();
      if (pages.indexOf(currentPage) === -1) return false;
    }

    // Check max show count
    var maxCount = DEVOPS_AI_JOURNEY_ENTRY_POINT.maxShowCount || 1;
    var shownCount = parseInt(getCookie(ENTRY_SHOWN_COOKIE) || '0', 10);
    if (shownCount >= maxCount) return false;

    return true;
  }

  // ─── Feature Flag: Track entry point shown ───
  function trackEntryPointShown() {
    var shownCount = parseInt(getCookie(ENTRY_SHOWN_COOKIE) || '0', 10);
    setCookie(ENTRY_SHOWN_COOKIE, String(shownCount + 1), COOKIE_DAYS);
  }

  // ─────────────────────────────────────────
  // LAYER 1: Consent Manager
  // ─────────────────────────────────────────

  function buildConsentBanner() {
    var existing = document.querySelector('.cookie-banner');
    if (existing) existing.remove();

    var banner = document.createElement('div');
    banner.className = 'consent-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie preferences');
    banner.innerHTML =
      '<div class="consent-banner__inner">' +
        '<div class="consent-banner__text">' +
          '<strong>Your Privacy Matters</strong>' +
          '<p>We use cookies to keep the site running, understand how you use it, and personalize your experience. ' +
          'You choose what to allow.</p>' +
        '</div>' +
        '<div class="consent-banner__categories">' +
          '<label class="consent-cat">' +
            '<input type="checkbox" checked disabled> ' +
            '<span class="consent-cat__name">Essential</span>' +
            '<span class="consent-cat__desc">Required for the site to function. Always on.</span>' +
          '</label>' +
          '<label class="consent-cat">' +
            '<input type="checkbox" id="consent-analytics" checked> ' +
            '<span class="consent-cat__name">Analytics</span>' +
            '<span class="consent-cat__desc">Helps us understand site usage to improve the experience.</span>' +
          '</label>' +
          '<label class="consent-cat">' +
            '<input type="checkbox" id="consent-personalization" checked> ' +
            '<span class="consent-cat__name">Personalization</span>' +
            '<span class="consent-cat__desc">Remembers your role and preferences for a tailored experience.</span>' +
          '</label>' +
        '</div>' +
        '<div class="consent-banner__actions">' +
          '<button class="consent-btn consent-btn--reject">Essential Only</button>' +
          '<button class="consent-btn consent-btn--save">Save Preferences</button>' +
          '<button class="consent-btn consent-btn--accept">Accept All</button>' +
        '</div>' +
        '<a href="' + resolveRoot() + 'legal/privacy.html" class="consent-banner__link">Privacy Policy</a>' +
      '</div>';

    document.body.appendChild(banner);

    // Animate in
    requestAnimationFrame(function() {
      banner.classList.add('is-visible');
    });

    // Event handlers
    banner.querySelector('.consent-btn--accept').addEventListener('click', function() {
      state.consent = { essential: true, analytics: true, personalization: true };
      saveConsent();
      hideConsentBanner(banner);
      onConsentGranted();
    });

    banner.querySelector('.consent-btn--reject').addEventListener('click', function() {
      state.consent = { essential: true, analytics: false, personalization: false };
      saveConsent();
      hideConsentBanner(banner);
    });

    banner.querySelector('.consent-btn--save').addEventListener('click', function() {
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
    setTimeout(function() { banner.remove(); }, 350);
  }

  // ─────────────────────────────────────────
  // LAYER 2: Role Identification
  // ─────────────────────────────────────────

  // Original bottom-sheet role picker (used when entry point flag is OFF)
  function showRolePicker() {
    if (state.role) return; // Already identified

    var picker = document.createElement('div');
    picker.className = 'role-picker';
    picker.setAttribute('role', 'dialog');
    picker.setAttribute('aria-label', 'Select your role');

    var pills = ROLES.map(function(r) {
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

    setTimeout(function() {
      picker.classList.add('is-visible');
    }, 400);

    // Events
    picker.querySelector('.role-picker__close').addEventListener('click', function() {
      hideRolePicker(picker);
    });

    picker.querySelectorAll('.role-pill').forEach(function(btn) {
      btn.addEventListener('click', function() {
        state.role = this.getAttribute('data-role');
        saveRole();
        hideRolePicker(picker);
        onRoleSelected();
      });
    });
  }

  function hideRolePicker(picker) {
    picker.classList.remove('is-visible');
    setTimeout(function() { picker.remove(); }, 350);
  }

  // ─────────────────────────────────────────
  // LAYER 2b: Journey Entry Point (Neural Network)
  // Feature-flagged: DEVOPS_AI_JOURNEY_ENTRY_POINT
  // ─────────────────────────────────────────

  function showJourneyEntryPoint() {
    if (state.role) return; // Already identified

    trackEntryPointShown();

    // Build entry point data payload for the module
    var entryPointConfig = {
      roles: ROLES.map(function(r) {
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
      onRoleSelected: function(roleId) {
        state.role = roleId;
        saveRole();
        onRoleSelected();
      },
      resolveRoot: resolveRoot
    };

    // Expose config globally for the entry-point.js module to consume
    window.__DEVOPS_AI_ENTRY_POINT__ = entryPointConfig;

    // Dynamically load entry-point.js if not already loaded
    if (!document.getElementById('devopsai-entry-point-script')) {
      var script = document.createElement('script');
      script.id = 'devopsai-entry-point-script';
      script.type = 'module';
      script.src = resolveRoot() + 'entry-point.js';
      document.body.appendChild(script);
    } else {
      // If script already loaded, re-init
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

    // Identify current page context
    var path = window.location.pathname;
    var slug = null;

    // PA pages (check before zone to avoid false partial match)
    var paMatch = path.match(/\/zones\/[^/]+\/process-areas\/([^/]+?)(?:\.html)?$/);
    if (paMatch) slug = 'pa:' + paMatch[1];

    // Zone pages
    var zoneMatch = !slug && path.match(/\/zones\/([^/]+?)(?:\.html)?$/);
    if (zoneMatch) slug = 'zone:' + zoneMatch[1];

    // Role pages
    var roleMatch = path.match(/\/roles\/([^/]+?)(?:\.html)?$/);
    if (roleMatch && roleMatch[1] !== 'index') slug = 'role:' + roleMatch[1];

    // Root pages
    if (!slug) {
      var page = path.split('/').pop() || 'index';
      slug = 'page:' + page.replace(/\.html$/, '');
      if (!slug || slug === 'page:') slug = 'page:index';
    }

    // Add to journey (dedup, keep last 30)
    if (slug && state.journey.indexOf(slug) === -1) {
      state.journey.push(slug);
      if (state.journey.length > 30) state.journey.shift();
    }

    // Infer lifecycle stage
    inferStage();

    saveJourney();
  }

  function inferStage() {
    var zoneVisits = state.journey.filter(function(s) { return s.indexOf('zone:') === 0; }).length;
    var paVisits = state.journey.filter(function(s) { return s.indexOf('pa:') === 0; }).length;
    var hasVisitedRoi = state.journey.indexOf('page:roi') >= 0;
    var hasVisitedMarketplace = state.journey.indexOf('page:marketplace') >= 0;
    var hasVisitedContact = state.journey.indexOf('page:contact') >= 0;

    if (hasVisitedContact || hasVisitedMarketplace) {
      state.stage = 'onboarding';
    } else if (hasVisitedRoi || paVisits >= 3) {
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
      // Feature-flagged: use entry point or fallback to bottom-sheet picker
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
    // Dismiss the entry point overlay if present
    var entryPoint = document.getElementById('devopsai-entry-point');
    if (entryPoint) {
      entryPoint.classList.add('is-hidden');
      setTimeout(function() { entryPoint.remove(); }, 600);
    }

    applyPersonalization();
  }

  function applyPersonalization() {
    if (!state.role || !state.consent || !state.consent.personalization) return;

    var root = resolveRoot();
    var roleData = ROLES.find(function(r) { return r.id === state.role; });
    if (!roleData) return;

    // 4a. Welcome bar on subsequent visits
    if (state.visits > 1) {
      insertWelcomeBar(roleData, root);
    }

    // 4b. Personalize hero subtext on homepage
    personalizeHero(roleData);

    // 4c. Insert recommended zones sidebar/banner
    insertRecommendedZones(roleData, root);

    // 4d. Update CTAs to be role-aware
    personalizeCtAs(roleData, root);
  }

  function insertWelcomeBar(roleData, root) {
    // Only on pages that have a site-header
    var header = document.querySelector('.site-header');
    if (!header || document.querySelector('.welcome-bar')) return;

    var recentZones = state.journey
      .filter(function(s) { return s.indexOf('zone:') === 0; })
      .slice(-3)
      .map(function(s) { return s.replace('zone:', ''); });

    var continueHtml = '';
    if (recentZones.length > 0) {
      var last = recentZones[recentZones.length - 1];
      var zoneName = last.replace(/-/g, ' ').replace(/\b\w/g, function(c) { return c.toUpperCase(); });
      continueHtml = ' · <a href="' + root + 'zones/' + last + '.html" class="welcome-bar__link">Continue exploring ' + zoneName + ' →</a>';
    }

    var bar = document.createElement('div');
    bar.className = 'welcome-bar';
    bar.innerHTML =
      '<div class="welcome-bar__inner">' +
        '<span class="welcome-bar__greeting">' +
          roleData.icon + ' Welcome back' +
          ' · <a href="' + root + roleData.page + '" class="welcome-bar__link">Your ' + roleData.label + ' Journey</a>' +
          continueHtml +
        '</span>' +
        '<button class="welcome-bar__change" title="Change role">Change Role</button>' +
      '</div>';

    header.insertAdjacentElement('afterend', bar);

    bar.querySelector('.welcome-bar__change').addEventListener('click', function() {
      deleteCookie(ROLE_COOKIE);
      state.role = null;
      bar.remove();
      // Feature-flagged: use entry point or fallback
      if (shouldShowEntryPoint()) {
        showJourneyEntryPoint();
      } else {
        showRolePicker();
      }
    });
  }

  function personalizeHero(roleData) {
    // Only on homepage
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
    // Only on homepage and platform page
    var page = getCurrentPageSlug();
    if (page !== 'index' && page !== '' && page !== 'platform') return;

    var zones = ROLE_ZONES[state.role];
    if (!zones || zones.length === 0) return;

    // Find an appropriate insertion point (must be in main content, not nav menus)
    var target = document.querySelector('main .zone-grid, main .platform-zones, .hero-section, .hero');
    if (!target) target = document.querySelector('main > section:first-of-type, .hero-cta');
    if (!target || document.querySelector('.recommended-zones')) return;

    var zoneCards = zones.map(function(z) {
      var name = z.replace(/-/g, ' ').replace(/\b\w/g, function(c) { return c.toUpperCase(); });
      return '<a href="' + root + 'zones/' + z + '.html" class="rec-zone-card">' +
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

    // Trigger fade-up
    requestAnimationFrame(function() {
      section.classList.add('is-visible');
    });
  }

  function personalizeCtAs(roleData, root) {
    // Find generic "Get Started" CTAs and add role context
    var ctas = document.querySelectorAll('.btn-primary, .cta-primary, [class*="cta"]');
    ctas.forEach(function(cta) {
      if (cta.textContent.trim() === 'Get Started' && !cta.getAttribute('data-personalized')) {
        cta.setAttribute('data-personalized', 'true');
        // Don't change text, but update href to marketplace if in evaluation+ stage
        if (state.stage === 'evaluation' || state.stage === 'onboarding') {
          if (cta.tagName === 'A' && cta.getAttribute('href') === 'contact.html') {
            // Could optionally route to marketplace
          }
        }
      }
    });
  }

  // ─── Footer: Manage Preferences Link ───
  function addManagePreferencesLink() {
    var footer = document.querySelector('footer, .site-footer');
    if (!footer || document.querySelector('.manage-cookies-link')) return;

    var link = document.createElement('a');
    link.href = '#';
    link.className = 'manage-cookies-link';
    link.textContent = 'Manage Cookie Preferences';
    link.style.cssText = 'font-size:12px;color:var(--text-muted,#97999B);text-decoration:underline;cursor:pointer;';
    link.addEventListener('click', function(e) {
      e.preventDefault();
      // Reset consent and show banner again
      deleteCookie(CONSENT_COOKIE);
      state.consent = null;
      buildConsentBanner();
    });

    // Find footer links area or just append
    var footerLinks = footer.querySelector('.footer-links, .footer-bottom, .footer__bottom');
    if (footerLinks) {
      footerLinks.appendChild(link);
    } else {
      footer.appendChild(link);
    }
  }

  // ─── Boot Sequence ───
  document.addEventListener('DOMContentLoaded', function() {
    loadState();

    // Always add manage preferences link in footer
    addManagePreferencesLink();

    if (!state.consent) {
      // No consent yet — show consent banner
      setTimeout(function() {
        buildConsentBanner();
      }, 1200);
    } else {
      // Consent exists — track + personalize
      if (state.consent.personalization) {
        trackPageVisit();
        applyPersonalization();

        // If they consented but never picked a role, prompt after 2 visits
        if (!state.role && state.visits >= 2) {
          // Feature-flagged: use entry point or fallback
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

  // ─── Public API (for DevOps AI platform control plane integration) ───
  // These methods can be called from the BD Zone control plane to manage
  // the journey entry point at runtime.
  window.DevOpsAIPersonalization = {
    // Get current feature flag state
    getEntryPointConfig: function() {
      return JSON.parse(JSON.stringify(DEVOPS_AI_JOURNEY_ENTRY_POINT));
    },
    // Enable/disable the entry point (runtime toggle)
    setEntryPointEnabled: function(enabled) {
      DEVOPS_AI_JOURNEY_ENTRY_POINT.enabled = !!enabled;
      if (DEVOPS_AI_JOURNEY_ENTRY_POINT.debug) {
        console.log('[DevOps AI] Journey Entry Point ' + (enabled ? 'ENABLED' : 'DISABLED'));
      }
    },
    // Update entry point config (partial update)
    updateEntryPointConfig: function(partial) {
      if (partial.enabled !== undefined) DEVOPS_AI_JOURNEY_ENTRY_POINT.enabled = !!partial.enabled;
      if (partial.mode) DEVOPS_AI_JOURNEY_ENTRY_POINT.mode = partial.mode;
      if (partial.showOnPages) DEVOPS_AI_JOURNEY_ENTRY_POINT.showOnPages = partial.showOnPages;
      if (partial.maxShowCount !== undefined) DEVOPS_AI_JOURNEY_ENTRY_POINT.maxShowCount = partial.maxShowCount;
      if (partial.debug !== undefined) DEVOPS_AI_JOURNEY_ENTRY_POINT.debug = !!partial.debug;
    },
    // Reset user's role (trigger re-identification)
    resetRole: function() {
      deleteCookie(ROLE_COOKIE);
      state.role = null;
      var welcomeBar = document.querySelector('.welcome-bar');
      if (welcomeBar) welcomeBar.remove();
    },
    // Get current personalization state
    getState: function() {
      return JSON.parse(JSON.stringify(state));
    },
    // Get all role definitions
    getRoles: function() {
      return JSON.parse(JSON.stringify(ROLES));
    },
    // Get role groups
    getRoleGroups: function() {
      return JSON.parse(JSON.stringify(ROLE_GROUPS));
    }
  };

})();
