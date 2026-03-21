#!/usr/bin/env python3
"""
FR-W25: Generate Secondary Pages for DevOps AI Website
Creates: about.html, contact.html, marketplace.html, blog.html, login.html,
         why-devops-ai.html, solutions.html, legal/privacy.html, legal/terms.html,
         legal/acceptable-use.html
"""
import os
import html as html_mod

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def e(text):
    """HTML-escape"""
    return html_mod.escape(text)


# ─── Shared HTML fragments ───────────────────────────────────────────────────

def head_block(title, description, canonical_slug, og_description, breadcrumbs, prefix, extra_head=""):
    """Generate <head> block. prefix is '' for root pages, '../' for legal/ pages."""
    bc_json = ",\n          ".join(
        '{{ "@type": "ListItem", "position": {pos}, "name": "{name}", "item": "https://devops.ai.rain.tech/{item}" }}'.format(
            pos=i + 1, name=e(bc["name"]), item=bc["item"]
        )
        for i, bc in enumerate(breadcrumbs)
    )

    return f'''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{e(title)} — DevOps AI | RainTech</title>

<meta name="description" content="{e(description)}">
<link rel="canonical" href="https://devops.ai.rain.tech/{canonical_slug}">

<!-- Open Graph -->
<meta property="og:type"        content="website">
<meta property="og:title"       content="{e(title)} — DevOps AI">
<meta property="og:description" content="{e(og_description)}">
<meta property="og:url"         content="https://devops.ai.rain.tech/{canonical_slug}">
<meta property="og:site_name"   content="DevOps AI by RainTech">
<meta property="og:image"       content="https://devops.ai.rain.tech/assets/og-image.png">
<meta property="og:image:width"  content="1200">
<meta property="og:image:height" content="630">

<!-- Twitter / X Card -->
<meta name="twitter:card"        content="summary_large_image">
<meta name="twitter:title"       content="{e(title)} — DevOps AI">
<meta name="twitter:description" content="{e(og_description)}">
<meta name="twitter:image"       content="https://devops.ai.rain.tech/assets/og-image.png">

<!-- Favicon -->
<link rel="icon"             type="image/svg+xml" href="{prefix}favicon.svg">
<link rel="alternate icon"   type="image/png"     href="{prefix}assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon"                      href="{prefix}assets/apple-touch-icon.png">

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Rock+Salt&display=swap" rel="stylesheet">

<!-- CSS -->
<link rel="stylesheet" href="{prefix}css/base.css">
<link rel="stylesheet" href="{prefix}css/layout.css">
<link rel="stylesheet" href="{prefix}css/components.css">
<link rel="stylesheet" href="{prefix}css/animations.css">
<link rel="stylesheet" href="{prefix}css/pages.css">
{extra_head}
<!-- Structured Data -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "name": "RainTech",
      "url": "https://devops.ai.rain.tech",
      "logo": "https://devops.ai.rain.tech/assets/logo-powered-by.png",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "3 S Tejon St., Suite 400",
        "addressLocality": "Colorado Springs",
        "addressRegion": "CO",
        "postalCode": "80903",
        "addressCountry": "US"
      }},
      "telephone": "+1-844-835-7246"
    }},
    {{
      "@type": "WebPage",
      "name": "{e(title)} — DevOps AI",
      "url": "https://devops.ai.rain.tech/{canonical_slug}",
      "description": "{e(description)}",
      "breadcrumb": {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {bc_json}
        ]
      }}
    }}
  ]
}}
</script>'''


def header_block(prefix, current_page=""):
    """Site header with nav. prefix is '' or '../'"""
    current_about = ' aria-current="page"' if current_page == "about" else ""
    current_contact = ' aria-current="page"' if current_page == "contact" else ""
    current_security = ' aria-current="page"' if current_page == "security" else ""

    return f'''  <!-- ===== SITE HEADER ===== -->
  <header class="site-header" role="banner" id="site-header">
    <div class="container">
      <div class="header-inner">

        <a href="{prefix}index.html" class="header-logo" aria-label="DevOps AI — Home">
          <svg class="header-logo__img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" aria-hidden="true" focusable="false">
            <circle cx="20" cy="20" r="18" fill="none" stroke="#8BDB02" stroke-width="2.5"/>
            <path d="M12 20 L20 12 L28 20 L20 28 Z" fill="#8BDB02" opacity="0.9"/>
            <circle cx="20" cy="20" r="4" fill="#17E4ED"/>
          </svg>
          <span class="header-logo__wordmark" aria-hidden="true">
            DevOps <span>AI</span>
          </span>
        </a>

        <nav class="nav-primary" aria-label="Primary navigation" id="primary-nav">

          <!-- Platform -->
          <div class="nav-item" id="nav-platform">
            <button class="nav-link--dropdown" aria-expanded="false" aria-haspopup="true" aria-controls="mega-platform" id="nav-btn-platform">
              Platform
              <svg class="nav-chevron" aria-hidden="true" viewBox="0 0 16 16"><polyline points="3,6 8,11 13,6"/></svg>
            </button>
            <div class="mega-menu mega-menu--platform" id="mega-platform" role="region" aria-label="Platform menu">
              <div class="mega-menu__inner">
                <div class="mega-menu__col">
                  <div class="mega-menu__group">
                    <p class="mega-menu__heading">Platform Overview</p>
                    <p class="mega-menu__description">The AI-orchestrated MSP control plane with 15 operational zones, 157 process areas, and full data sovereignty.</p>
                    <a class="mega-menu__link mega-menu__link--more" href="{prefix}platform.html">Explore the Platform →</a>
                  </div>
                  <div class="mega-menu__divider" role="separator"></div>
                  <div class="mega-menu__group">
                    <p class="mega-menu__section-label">By Zone</p>
                    <ul class="mega-menu__list" role="list">
                      <li><a class="mega-menu__link" href="{prefix}zones/service-desk.html">Service Desk &amp; ITSM</a></li>
                      <li><a class="mega-menu__link" href="{prefix}zones/security-operations.html">Security Operations</a></li>
                      <li><a class="mega-menu__link" href="{prefix}zones/endpoint-management.html">Endpoint Management</a></li>
                      <li><a class="mega-menu__link" href="{prefix}zones/network-operations.html">Network Operations</a></li>
                    </ul>
                  </div>
                </div>
                <div class="mega-menu__col">
                  <div class="mega-menu__group">
                    <p class="mega-menu__section-label">Technical</p>
                    <ul class="mega-menu__list" role="list">
                      <li><a class="mega-menu__link" href="{prefix}architecture.html">Architecture &amp; Design</a></li>
                      <li><a class="mega-menu__link" href="{prefix}security.html">Security Center</a></li>
                      <li><a class="mega-menu__link" href="https://azuremarketplace.microsoft.com/" rel="noopener" target="_blank">Azure Marketplace ↗</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Solutions -->
          <div class="nav-item" id="nav-solutions">
            <button class="nav-link--dropdown" aria-expanded="false" aria-haspopup="true" aria-controls="mega-solutions" id="nav-btn-solutions">
              Solutions
              <svg class="nav-chevron" aria-hidden="true" viewBox="0 0 16 16"><polyline points="3,6 8,11 13,6"/></svg>
            </button>
            <div class="mega-menu mega-menu--solutions mega-menu--wide" id="mega-solutions" role="region" aria-label="Solutions menu">
              <div class="mega-menu__inner">
                <div class="mega-menu__group">
                  <p class="mega-menu__section-label">By Challenge</p>
                  <ul class="mega-menu__list" role="list">
                    <li><a class="mega-menu__link" href="{prefix}solutions/reduce-ticket-volume.html">Reduce Ticket Volume</a></li>
                    <li><a class="mega-menu__link" href="{prefix}solutions/scale-without-headcount.html">Scale Without Headcount</a></li>
                    <li><a class="mega-menu__link" href="{prefix}solutions/improve-sla.html">Improve SLA Performance</a></li>
                  </ul>
                </div>
                <div class="mega-menu__group">
                  <p class="mega-menu__section-label">By Industry</p>
                  <ul class="mega-menu__list" role="list">
                    <li><a class="mega-menu__link" href="{prefix}solutions/healthcare.html">Healthcare MSPs</a></li>
                    <li><a class="mega-menu__link" href="{prefix}solutions/finance.html">Financial Services</a></li>
                    <li><a class="mega-menu__link" href="{prefix}solutions/government.html">Government &amp; SLED</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Pricing -->
          <div class="nav-item">
            <a class="nav-link" href="{prefix}pricing.html">Pricing</a>
          </div>

          <!-- Security -->
          <div class="nav-item">
            <a class="nav-link" href="{prefix}security.html"{current_security}>Security</a>
          </div>

          <!-- Resources -->
          <div class="nav-item" id="nav-resources">
            <button class="nav-link--dropdown" aria-expanded="false" aria-haspopup="true" aria-controls="mega-resources" id="nav-btn-resources">
              Resources
              <svg class="nav-chevron" aria-hidden="true" viewBox="0 0 16 16"><polyline points="3,6 8,11 13,6"/></svg>
            </button>
            <div class="mega-menu mega-menu--resources" id="mega-resources" role="region" aria-label="Resources menu">
              <div class="mega-menu__inner">
                <div class="mega-menu__group">
                  <p class="mega-menu__section-label">Learn</p>
                  <ul class="mega-menu__list" role="list">
                    <li><a class="mega-menu__link" href="{prefix}docs.html">Documentation</a></li>
                    <li><a class="mega-menu__link" href="{prefix}blog.html">Blog &amp; Insights</a></li>
                  </ul>
                </div>
                <div class="mega-menu__group">
                  <p class="mega-menu__section-label">Company</p>
                  <ul class="mega-menu__list" role="list">
                    <li><a class="mega-menu__link" href="{prefix}about.html"{current_about}>About RainTech</a></li>
                    <li><a class="mega-menu__link" href="{prefix}contact.html"{current_contact}>Contact</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

        </nav>

        <div class="header-actions">
          <button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark/light mode" aria-pressed="false">
            <svg class="icon-moon" aria-hidden="true" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
            <svg class="icon-sun" aria-hidden="true" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
          </button>
          <a class="btn-login" href="{prefix}login.html" aria-label="Log in to DevOps AI">Log in</a>
          <a class="nav-cta" href="{prefix}get-started.html" aria-label="Get started with DevOps AI">Get Started →</a>
          <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Open navigation menu" aria-expanded="false" aria-controls="mobile-nav">
            <span class="mobile-menu-toggle__bar" aria-hidden="true"></span>
          </button>
        </div>
      </div>
    </div>
  </header>'''


def mobile_nav_block(prefix):
    return f'''  <!-- ===== MOBILE NAV ===== -->
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation" aria-hidden="true">
    <div class="mobile-nav__overlay" id="mobile-nav-overlay" aria-hidden="true"></div>
    <div class="mobile-nav__drawer" role="dialog" aria-modal="true" aria-label="Navigation menu">
      <div class="mobile-nav__header">
        <a href="{prefix}index.html" class="header-logo" aria-label="DevOps AI — Home">
          <svg class="header-logo__img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" aria-hidden="true" focusable="false" style="height:28px">
            <circle cx="20" cy="20" r="18" fill="none" stroke="#8BDB02" stroke-width="2.5"/>
            <path d="M12 20 L20 12 L28 20 L20 28 Z" fill="#8BDB02" opacity="0.9"/>
            <circle cx="20" cy="20" r="4" fill="#17E4ED"/>
          </svg>
          <span class="header-logo__wordmark" aria-hidden="true">DevOps <span>AI</span></span>
        </a>
        <button class="mobile-nav__close" id="mobile-nav-close" aria-label="Close navigation menu">
          <svg viewBox="0 0 24 24" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18" stroke-linecap="round"/><line x1="6" y1="6" x2="18" y2="18" stroke-linecap="round"/></svg>
        </button>
      </div>
      <div class="mobile-nav__body">
        <a class="mobile-nav__link--direct" href="{prefix}platform.html">Platform</a>
        <a class="mobile-nav__link--direct" href="{prefix}pricing.html">Pricing</a>
        <a class="mobile-nav__link--direct" href="{prefix}security.html">Security</a>
        <a class="mobile-nav__link--direct" href="{prefix}architecture.html">Architecture</a>
        <a class="mobile-nav__link--direct" href="{prefix}about.html">About</a>
        <a class="mobile-nav__link--direct" href="{prefix}contact.html">Contact</a>
      </div>
      <div class="mobile-nav__footer">
        <a class="btn-login" href="{prefix}login.html" style="justify-content:center">Log in</a>
        <a class="nav-cta" href="{prefix}get-started.html" style="justify-content:center">Get Started →</a>
      </div>
    </div>
  </nav>'''


def breadcrumb_block(crumbs, prefix):
    """crumbs: list of (name, href_or_None) where last item has href=None (current page)"""
    items = []
    for i, (name, href) in enumerate(crumbs):
        if href is None:
            items.append(f'''        <li class="breadcrumb__item" aria-current="page">
          <span class="breadcrumb__current">{e(name)}</span>
        </li>''')
        else:
            items.append(f'''        <li class="breadcrumb__item">
          <a class="breadcrumb__link" href="{prefix}{href}">{e(name)}</a>
          <span class="breadcrumb__sep" aria-hidden="true">›</span>
        </li>''')
    items_html = "\n".join(items)
    return f'''  <!-- ===== BREADCRUMB ===== -->
  <div class="container" style="padding-top: calc(80px + var(--space-4))">
    <nav aria-label="Breadcrumb" class="breadcrumb">
      <ol role="list" style="display:contents">
{items_html}
      </ol>
    </nav>
  </div>'''


def footer_block(prefix):
    return f'''  <!-- ===== SITE FOOTER ===== -->
  <footer class="site-footer" role="contentinfo" id="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="{prefix}index.html" class="footer-logo" aria-label="DevOps AI — Home">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" aria-hidden="true" focusable="false" style="height:32px;width:auto">
              <circle cx="20" cy="20" r="18" fill="none" stroke="#8BDB02" stroke-width="2.5"/>
              <path d="M12 20 L20 12 L28 20 L20 28 Z" fill="#8BDB02" opacity="0.9"/>
              <circle cx="20" cy="20" r="4" fill="#17E4ED"/>
            </svg>
            <span class="footer-logo__wordmark">DevOps <span>AI</span></span>
          </a>
          <p class="footer-tagline">AI-as-a-Service for MSPs</p>
          <p class="footer-brand__desc">The AI-orchestrated MSP control plane. 15 operational zones. 157 process areas. Full data sovereignty.</p>
          <address class="footer-brand__address">
            3 S Tejon St., Suite 400<br>
            Colorado Springs, CO 80903<br>
            <a href="tel:+18448357246">+1-844-835-7246</a>
          </address>
        </div>
        <div class="footer-col">
          <h4>Platform</h4>
          <a href="{prefix}platform.html">Platform Overview</a>
          <a href="{prefix}architecture.html">Architecture</a>
          <a href="{prefix}pricing.html">Pricing</a>
        </div>
        <div class="footer-col">
          <h4>Solutions</h4>
          <a href="{prefix}solutions.html">Solutions Overview</a>
          <a href="{prefix}marketplace.html">Azure Marketplace</a>
          <a href="{prefix}why-devops-ai.html">Why DevOps AI</a>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <a href="{prefix}blog.html">Blog</a>
          <a href="{prefix}docs.html">Documentation</a>
          <a href="{prefix}contact.html">Contact</a>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <a href="{prefix}about.html">About RainTech</a>
          <a href="{prefix}careers.html">Careers</a>
          <a href="{prefix}press.html">Press</a>
        </div>
      </div>

      <div class="footer-trust" role="navigation" aria-label="Trust and legal links">
        <span class="footer-trust__label">Trust &amp; Legal</span>
        <a href="{prefix}security.html">Security Center</a>
        <span class="footer-trust__sep" aria-hidden="true">·</span>
        <a href="{prefix}legal/privacy.html">Privacy Policy</a>
        <span class="footer-trust__sep" aria-hidden="true">·</span>
        <a href="{prefix}legal/terms.html">Terms of Service</a>
        <span class="footer-trust__sep" aria-hidden="true">·</span>
        <a href="{prefix}legal/acceptable-use.html">Acceptable Use</a>
      </div>

      <div class="footer-bottom">
        <span>&copy; 2026 RainTech, Inc. All rights reserved.</span>
        <div class="footer-bottom__badges">
          <a class="badge-azure" href="https://azuremarketplace.microsoft.com/" rel="noopener" target="_blank" aria-label="Available on Azure Marketplace">
            <svg viewBox="0 0 16 16" aria-hidden="true" fill="#0078d4"><path d="M7.073 1.8L1.6 11.3h4.2l1.3-2.4h2.4l-1.8-3.1L9.6 3l-2.527-1.2zm1.6 4.5l2.327 4H4.8l3.873-4zM6.927 11.3L5.6 13.5H14.4l-1.327-2.2H6.927z"/></svg>
            Azure Marketplace
          </a>
        </div>
      </div>
    </div>
  </footer>'''


INLINE_JS = r"""(function () {
    'use strict';

    /* Theme Toggle */
    var themeToggle = document.getElementById('theme-toggle');
    var html = document.documentElement;
    function applyTheme(theme) {
      html.setAttribute('data-theme', theme);
      localStorage.setItem('devops-ai-theme', theme);
      if (themeToggle) {
        themeToggle.setAttribute('aria-pressed', theme === 'light' ? 'true' : 'false');
        themeToggle.setAttribute('aria-label', theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
      }
    }
    var savedTheme = localStorage.getItem('devops-ai-theme');
    if (savedTheme) applyTheme(savedTheme);
    if (themeToggle) {
      themeToggle.addEventListener('click', function () {
        var current = html.getAttribute('data-theme') || 'dark';
        applyTheme(current === 'dark' ? 'light' : 'dark');
      });
    }

    /* Header scroll */
    var header = document.getElementById('site-header');
    if (header) {
      var ticking = false;
      function onScroll() {
        if (!ticking) {
          window.requestAnimationFrame(function () {
            header.classList.toggle('is-scrolled', window.scrollY > 50);
            ticking = false;
          });
          ticking = true;
        }
      }
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    }

    /* Mega Menu */
    var navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(function (item) {
      var trigger = item.querySelector('.nav-link--dropdown');
      var menu = item.querySelector('.mega-menu');
      if (!trigger || !menu) return;
      trigger.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          var expanded = trigger.getAttribute('aria-expanded') === 'true';
          closeAllMegaMenus();
          if (!expanded) openMegaMenu(trigger, menu);
        }
        if (e.key === 'Escape') { closeAllMegaMenus(); trigger.focus(); }
      });
      menu.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { closeAllMegaMenus(); trigger.focus(); }
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav-item')) closeAllMegaMenus();
    });
    function openMegaMenu(trigger, menu) { trigger.setAttribute('aria-expanded', 'true'); }
    function closeAllMegaMenus() {
      navItems.forEach(function (item) {
        var trigger = item.querySelector('.nav-link--dropdown');
        if (trigger) trigger.setAttribute('aria-expanded', 'false');
      });
    }

    /* Mobile Nav */
    var mobileNav = document.getElementById('mobile-nav');
    var mobileToggle = document.getElementById('mobile-menu-toggle');
    var mobileClose = document.getElementById('mobile-nav-close');
    var mobileOverlay = document.getElementById('mobile-nav-overlay');
    var body = document.body;

    function getFocusable(container) {
      return Array.from(container.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])')).filter(function (el) {
        return !el.closest('[hidden]') && getComputedStyle(el).display !== 'none';
      });
    }
    function openMobileNav() {
      if (!mobileNav || !mobileToggle) return;
      mobileNav.classList.add('is-open');
      mobileNav.setAttribute('aria-hidden', 'false');
      mobileToggle.setAttribute('aria-expanded', 'true');
      body.style.overflow = 'hidden';
      setTimeout(function () { var first = getFocusable(mobileNav)[0]; if (first) first.focus(); }, 50);
    }
    function closeMobileNav() {
      if (!mobileNav || !mobileToggle) return;
      mobileNav.classList.remove('is-open');
      mobileNav.setAttribute('aria-hidden', 'true');
      mobileToggle.setAttribute('aria-expanded', 'false');
      body.style.overflow = '';
      mobileToggle.focus();
    }
    if (mobileToggle) mobileToggle.addEventListener('click', openMobileNav);
    if (mobileClose) mobileClose.addEventListener('click', closeMobileNav);
    if (mobileOverlay) mobileOverlay.addEventListener('click', closeMobileNav);
    if (mobileNav) {
      mobileNav.addEventListener('keydown', function (e) {
        if (!mobileNav.classList.contains('is-open')) return;
        if (e.key === 'Escape') { closeMobileNav(); return; }
        if (e.key === 'Tab') {
          var focusable = getFocusable(mobileNav);
          if (!focusable.length) return;
          var first = focusable[0], last = focusable[focusable.length - 1];
          if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      });
    }

    /* Scroll animations */
    var animatedEls = document.querySelectorAll('[data-animate]');
    if ('IntersectionObserver' in window && animatedEls.length) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1 });
      animatedEls.forEach(function (el) { el.classList.add('fade-up'); observer.observe(el); });
    }
  }());"""


def chatbot_block():
    return '''
  <!-- Chatbot Widget (FR-W20) -->
  <div id="chatbot-container"></div>
  <script>(function(){var c=document.getElementById('chatbot-container');if(c){var s=document.createElement('script');s.src='js/components/chatbot.js';s.defer=true;document.head.appendChild(s)}})();</script>'''


def build_page(filename, prefix, title, description, og_description, breadcrumbs_schema, breadcrumb_crumbs, main_content, extra_head="", extra_js="", current_page=""):
    """Assemble a full page."""
    head = head_block(title, description, filename.replace(".html", ""), og_description, breadcrumbs_schema, prefix, extra_head)
    header = header_block(prefix, current_page)
    mobile_nav = mobile_nav_block(prefix)
    breadcrumb = breadcrumb_block(breadcrumb_crumbs, prefix)
    footer = footer_block(prefix)

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
{head}
</head>
<body>

  <a class="skip-link" href="#main-content">Skip to main content</a>

{header}

{mobile_nav}

{breadcrumb}

  <!-- ===== MAIN CONTENT ===== -->
  <main id="main-content" tabindex="-1">

{main_content}

  </main>

{footer}

  <!-- ===== JS ===== -->
  <script>
  {INLINE_JS}
  </script>
{extra_js}
{chatbot_block()}

</body>
</html>
'''


# ─── Page content definitions ────────────────────────────────────────────────

def about_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient about-hero" aria-label="About hero" data-animate>
      <div class="container">
        <div class="hero__eyebrow">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.5"/>
            <path d="M8 5v3l2 2" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          Our Story
        </div>
        <h1 class="hero__title">Building the Future of Managed Services</h1>
        <p class="hero__desc">RainTech is on a mission to transform how MSPs operate — replacing fragmented tooling with a single AI-orchestrated control plane that scales without headcount.</p>
      </div>
    </section>

    <!-- Mission & Vision -->
    <section class="section" aria-label="Mission and vision" data-animate>
      <div class="container">
        <div class="about-mission-grid">
          <div class="card card--glass about-mission-card">
            <h2>Our Mission</h2>
            <p>To empower every managed service provider with enterprise-grade AI operations — making world-class service delivery accessible regardless of team size. We believe AI should augment human expertise, not replace it.</p>
          </div>
          <div class="card card--glass about-mission-card">
            <h2>Our Vision</h2>
            <p>A world where a 10-person MSP delivers the same operational excellence as a 500-person enterprise — powered by AI that handles the routine so humans can focus on what matters: relationships, strategy, and innovation.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Timeline -->
    <section class="section section--dark" aria-label="Company timeline" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>Our Journey</h2>
          <p style="margin-inline: auto;">From concept to the AI-orchestrated MSP platform trusted by operators worldwide.</p>
        </div>
        <div class="about-timeline">
          <div class="about-timeline__item" data-animate>
            <div class="about-timeline__year">2019</div>
            <div class="about-timeline__content">
              <h3>The Spark</h3>
              <p>RainTech founded in Colorado Springs with a vision to modernize managed services through intelligent automation.</p>
            </div>
          </div>
          <div class="about-timeline__item" data-animate>
            <div class="about-timeline__year">2021</div>
            <div class="about-timeline__content">
              <h3>Platform Genesis</h3>
              <p>First-generation DevOps AI platform launched with 5 operational zones and foundational AI capabilities.</p>
            </div>
          </div>
          <div class="about-timeline__item" data-animate>
            <div class="about-timeline__year">2023</div>
            <div class="about-timeline__content">
              <h3>Azure Marketplace</h3>
              <p>DevOps AI listed on Azure Marketplace. SOC 2 Type II certification achieved. Platform expanded to 10 zones.</p>
            </div>
          </div>
          <div class="about-timeline__item" data-animate>
            <div class="about-timeline__year">2024</div>
            <div class="about-timeline__content">
              <h3>Full Coverage</h3>
              <p>15 operational zones, 157 process areas, 21 roles. HIPAA and CMMC compliance. Human-in-the-loop AI controls across all zones.</p>
            </div>
          </div>
          <div class="about-timeline__item" data-animate>
            <div class="about-timeline__year">2025</div>
            <div class="about-timeline__content">
              <h3>AI-First Operations</h3>
              <p>Next-generation inference engine, multi-model orchestration, and advanced HITL controls. Deploy in under 35 minutes via Azure.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Values -->
    <section class="section" aria-label="Our values" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>Our Values</h2>
          <p style="margin-inline: auto;">The principles that guide every decision we make.</p>
        </div>
        <div class="about-values-grid">
          <div class="card card--glass about-value-card" data-animate>
            <div class="about-value-icon">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true">
                <path d="M16 4L8 8v8c0 6.6 4 11 8 12 4-1 8-5.4 8-12V8L16 4z" stroke="var(--accent)" stroke-width="2"/>
                <path d="M12 16l3 3 6-6" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3>Security First</h3>
            <p>Security isn't an afterthought — it's the foundation. Every feature, every integration, every line of code is reviewed through a security lens.</p>
          </div>
          <div class="card card--glass about-value-card" data-animate>
            <div class="about-value-icon">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true">
                <circle cx="16" cy="12" r="5" stroke="var(--cyan)" stroke-width="2"/>
                <path d="M8 26c0-4.4 3.6-8 8-8s8 3.6 8 8" stroke="var(--cyan)" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </div>
            <h3>Human in the Loop</h3>
            <p>AI augments — it never replaces. Critical decisions always have human oversight. We build guardrails, not autopilots.</p>
          </div>
          <div class="card card--glass about-value-card" data-animate>
            <div class="about-value-icon">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true">
                <rect x="6" y="6" width="20" height="20" rx="3" stroke="var(--blue-sky)" stroke-width="2"/>
                <path d="M12 16h8M16 12v8" stroke="var(--blue-sky)" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </div>
            <h3>Data Sovereignty</h3>
            <p>Your data stays yours. Full tenant isolation, your Azure subscription, your encryption keys. Zero shared infrastructure.</p>
          </div>
          <div class="card card--glass about-value-card" data-animate>
            <div class="about-value-icon">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true">
                <path d="M6 22l6-6 4 4 10-10" stroke="var(--violet-bright)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M20 10h6v6" stroke="var(--violet-bright)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h3>Operational Excellence</h3>
            <p>We eat our own cooking. DevOps AI runs on DevOps AI. Every process area we offer is one we use internally.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Team -->
    <section class="section section--dark" aria-label="Leadership team" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>Leadership</h2>
          <p style="margin-inline: auto;">The team building the future of AI-powered managed services.</p>
        </div>
        <div class="about-team-grid">
          <div class="card card--glass about-team-card" data-animate>
            <div class="about-team-avatar" aria-hidden="true">AJ</div>
            <h3>Andrew Johnson</h3>
            <p class="about-team-role">CEO &amp; Founder</p>
            <p>Visionary behind DevOps AI. 15+ years in managed services and cloud infrastructure. Passionate about making enterprise-grade AI accessible to every MSP.</p>
          </div>
          <div class="card card--glass about-team-card" data-animate>
            <div class="about-team-avatar" aria-hidden="true">RT</div>
            <h3>RainTech Engineering</h3>
            <p class="about-team-role">Platform Team</p>
            <p>A distributed team of engineers, data scientists, and security experts building the AI-orchestrated MSP control plane from Colorado Springs.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section" aria-label="Call to action" data-animate>
      <div class="container text-center">
        <h2>Ready to Transform Your MSP?</h2>
        <p style="margin-inline: auto; margin-bottom: var(--space-8);">Join the MSPs that are scaling without scaling headcount.</p>
        <div class="hero__cta">
          <a href="marketplace.html" class="btn btn--primary btn--lg">Deploy on Azure →</a>
          <a href="contact.html" class="btn btn--secondary btn--lg">Talk to Us</a>
        </div>
      </div>
    </section>'''


def contact_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient contact-hero" aria-label="Contact hero" data-animate>
      <div class="container">
        <div class="hero__eyebrow">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <rect x="2" y="4" width="12" height="9" rx="2" stroke="currentColor" stroke-width="1.5"/>
            <path d="M2 6l6 4 6-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          Get in Touch
        </div>
        <h1 class="hero__title">Let's Talk About Your MSP's Future</h1>
        <p class="hero__desc">Whether you're evaluating DevOps AI, need technical help, or want to schedule a demo — we're here.</p>
      </div>
    </section>

    <!-- Contact Form + Info -->
    <section class="section" aria-label="Contact form" data-animate>
      <div class="container">
        <div class="contact-layout">

          <!-- Form -->
          <div class="contact-form-wrapper">
            <form class="contact-form" id="contact-form" novalidate>
              <!-- Step 1: Who are you? -->
              <div class="contact-form__step is-active" id="contact-step-1" data-step="1">
                <h2>Tell us about yourself</h2>
                <div class="form-row">
                  <div class="form-group">
                    <label for="contact-first-name">First name <span class="required" aria-hidden="true">*</span></label>
                    <input type="text" id="contact-first-name" name="firstName" required autocomplete="given-name">
                  </div>
                  <div class="form-group">
                    <label for="contact-last-name">Last name <span class="required" aria-hidden="true">*</span></label>
                    <input type="text" id="contact-last-name" name="lastName" required autocomplete="family-name">
                  </div>
                </div>
                <div class="form-group">
                  <label for="contact-email">Work email <span class="required" aria-hidden="true">*</span></label>
                  <input type="email" id="contact-email" name="email" required autocomplete="email">
                </div>
                <div class="form-group">
                  <label for="contact-company">Company</label>
                  <input type="text" id="contact-company" name="company" autocomplete="organization">
                </div>
                <button type="button" class="btn btn--primary" id="contact-next-1">Next →</button>
              </div>

              <!-- Step 2: What do you need? -->
              <div class="contact-form__step" id="contact-step-2" data-step="2">
                <h2>How can we help?</h2>
                <div class="form-group">
                  <label for="contact-topic">Topic <span class="required" aria-hidden="true">*</span></label>
                  <select id="contact-topic" name="topic" required>
                    <option value="" disabled selected>Select a topic</option>
                    <option value="demo">Request a Demo</option>
                    <option value="pricing">Pricing &amp; Licensing</option>
                    <option value="technical">Technical Question</option>
                    <option value="partnership">Partnership Inquiry</option>
                    <option value="support">Support</option>
                    <option value="other">Other</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="contact-message">Message <span class="required" aria-hidden="true">*</span></label>
                  <textarea id="contact-message" name="message" rows="5" required placeholder="Tell us what you're looking for..."></textarea>
                </div>
                <div class="contact-form__actions">
                  <button type="button" class="btn btn--secondary" id="contact-back-2">← Back</button>
                  <button type="submit" class="btn btn--primary" id="contact-submit">Send Message</button>
                </div>
              </div>

              <!-- Success -->
              <div class="contact-form__success" id="contact-success" hidden>
                <svg width="48" height="48" viewBox="0 0 48 48" fill="none" aria-hidden="true">
                  <circle cx="24" cy="24" r="20" stroke="var(--accent)" stroke-width="2"/>
                  <path d="M16 24l6 6 12-12" stroke="var(--accent)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <h2>Message Sent</h2>
                <p>Thanks for reaching out. We'll get back to you within 1 business day.</p>
              </div>
            </form>
          </div>

          <!-- Contact Info Sidebar -->
          <aside class="contact-info">
            <div class="card card--glass contact-info-card">
              <h3>Direct Contact</h3>
              <address>
                <p><strong>Phone</strong><br><a href="tel:+18448357246">+1-844-835-7246</a></p>
                <p><strong>Email</strong><br><a href="mailto:hello@rain.tech">hello@rain.tech</a></p>
                <p><strong>Address</strong><br>3 S Tejon St., Suite 400<br>Colorado Springs, CO 80903</p>
              </address>
            </div>

            <div class="card card--glass contact-info-card">
              <h3>Schedule a Meeting</h3>
              <p>Book a 30-minute call with our team to discuss your MSP's needs.</p>
              <div class="contact-scheduler-placeholder">
                <p class="text-muted" style="font-size: var(--text-sm);">Meeting scheduler coming soon. In the meantime, use the form or email us directly.</p>
              </div>
            </div>

            <div class="card card--glass contact-info-card">
              <h3>For Existing Customers</h3>
              <p>Access the support portal for technical assistance.</p>
              <a href="https://platform.devops.ai.rain.tech" class="btn btn--secondary" rel="noopener" target="_blank">Open Support Portal ↗</a>
            </div>
          </aside>

        </div>
      </div>
    </section>'''


def contact_extra_js():
    return '''
  <script>
  /* Contact form multi-step */
  (function () {
    'use strict';
    var form = document.getElementById('contact-form');
    if (!form) return;

    var step1 = document.getElementById('contact-step-1');
    var step2 = document.getElementById('contact-step-2');
    var success = document.getElementById('contact-success');
    var nextBtn = document.getElementById('contact-next-1');
    var backBtn = document.getElementById('contact-back-2');

    function showStep(show, hide) {
      hide.classList.remove('is-active');
      show.classList.add('is-active');
      show.querySelector('input, select, textarea').focus();
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        var firstName = document.getElementById('contact-first-name');
        var email = document.getElementById('contact-email');
        if (!firstName.value.trim() || !email.value.trim() || !email.validity.valid) {
          firstName.reportValidity();
          email.reportValidity();
          return;
        }
        showStep(step2, step1);
      });
    }

    if (backBtn) {
      backBtn.addEventListener('click', function () {
        showStep(step1, step2);
      });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      step2.classList.remove('is-active');
      success.hidden = false;
    });
  }());
  </script>'''


def marketplace_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient marketplace-hero" aria-label="Marketplace hero" data-animate>
      <div class="container">
        <div class="hero__eyebrow">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" fill="#0078d4">
            <path d="M7.073 1.8L1.6 11.3h4.2l1.3-2.4h2.4l-1.8-3.1L9.6 3l-2.527-1.2zm1.6 4.5l2.327 4H4.8l3.873-4zM6.927 11.3L5.6 13.5H14.4l-1.327-2.2H6.927z"/>
          </svg>
          Azure Marketplace
        </div>
        <h1 class="hero__title">Deploy DevOps AI from Azure Marketplace</h1>
        <p class="hero__desc">Two deployment packages — choose the one that fits your business. Both deploy to your Azure tenant in under 35 minutes with full data sovereignty.</p>
      </div>
    </section>

    <!-- Packages: MSP and Enterprise (SEPARATE) -->
    <section class="section" aria-label="Marketplace packages" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>Two Packages, One Platform</h2>
          <p style="margin-inline: auto;">MSP and Enterprise are <strong>separate marketplace packages</strong> — each tailored to its audience with optimized configurations, licensing, and onboarding.</p>
        </div>

        <div class="marketplace-packages">

          <!-- MSP Package -->
          <div class="card card--glass marketplace-package" data-animate>
            <div class="marketplace-package__badge">MSP Package</div>
            <h3>DevOps AI for MSPs</h3>
            <p class="marketplace-package__desc">Purpose-built for managed service providers. Multi-tenant architecture, client isolation, and the full 15-zone control plane optimized for service delivery at scale.</p>
            <ul class="marketplace-feature-list">
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Multi-tenant client isolation
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                All 15 operational zones
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                157 process areas with AI automation
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Per-client SLA tracking &amp; reporting
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Role-based access for 21 MSP roles
              </li>
            </ul>
            <a href="https://azuremarketplace.microsoft.com/" class="btn btn--primary btn--lg" rel="noopener" target="_blank">Deploy MSP Package ↗</a>
          </div>

          <!-- Enterprise Package -->
          <div class="card card--glass marketplace-package" data-animate>
            <div class="marketplace-package__badge marketplace-package__badge--enterprise">Enterprise Package</div>
            <h3>DevOps AI for Enterprise</h3>
            <p class="marketplace-package__desc">For internal IT teams and large organizations. Single-tenant deployment with enterprise integrations, SSO, and advanced compliance controls.</p>
            <ul class="marketplace-feature-list">
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--cyan)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Single-tenant dedicated deployment
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--cyan)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Enterprise SSO (SAML / OIDC)
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--cyan)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Advanced compliance (SOC 2, HIPAA, CMMC)
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--cyan)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Custom integrations &amp; API access
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--cyan)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Dedicated support &amp; onboarding
              </li>
            </ul>
            <a href="https://azuremarketplace.microsoft.com/" class="btn btn--primary btn--lg marketplace-btn--enterprise" rel="noopener" target="_blank">Deploy Enterprise Package ↗</a>
          </div>

        </div>
      </div>
    </section>

    <!-- Deployment Steps -->
    <section class="section section--dark" aria-label="Deployment steps" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>Deploy in Under 35 Minutes</h2>
          <p style="margin-inline: auto;">From Azure Marketplace to fully operational — here's how.</p>
        </div>
        <div class="marketplace-steps">
          <div class="marketplace-step" data-animate>
            <div class="marketplace-step__number">1</div>
            <h3>Select Your Package</h3>
            <p>Choose MSP or Enterprise from Azure Marketplace. Review the configuration options for your deployment.</p>
          </div>
          <div class="marketplace-step" data-animate>
            <div class="marketplace-step__number">2</div>
            <h3>Configure &amp; Deploy</h3>
            <p>Select your Azure region, configure tenant settings, and click deploy. Resources provision automatically in your subscription.</p>
          </div>
          <div class="marketplace-step" data-animate>
            <div class="marketplace-step__number">3</div>
            <h3>Onboard &amp; Activate</h3>
            <p>Follow the guided onboarding wizard. Configure zones, set up roles, connect integrations. You're live in under 35 minutes.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Trust -->
    <section class="section" aria-label="Trust and security" data-animate>
      <div class="container text-center">
        <h2>Your Cloud, Your Data, Your Control</h2>
        <p style="margin-inline: auto; margin-bottom: var(--space-8);">DevOps AI deploys to <em>your</em> Azure subscription. No shared infrastructure. No data leaving your tenant. Full sovereignty from day one.</p>
        <div class="marketplace-trust-badges">
          <span class="badge badge--status" data-status="success"><span class="badge__dot"></span> SOC 2 Type II</span>
          <span class="badge badge--status" data-status="success"><span class="badge__dot"></span> HIPAA Compliant</span>
          <span class="badge badge--status" data-status="success"><span class="badge__dot"></span> CMMC Aligned</span>
          <span class="badge badge--status" data-status="info"><span class="badge__dot"></span> FedRAMP In Progress</span>
        </div>
        <div class="hero__cta" style="margin-top: var(--space-8);">
          <a href="security.html" class="btn btn--secondary btn--lg">View Security Center →</a>
          <a href="pricing.html" class="btn btn--secondary btn--lg">See Pricing →</a>
        </div>
      </div>
    </section>'''


def blog_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient blog-hero" aria-label="Blog hero" data-animate>
      <div class="container">
        <div class="hero__eyebrow">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <rect x="2" y="2" width="12" height="12" rx="2" stroke="currentColor" stroke-width="1.5"/>
            <path d="M5 5h6M5 8h4M5 11h5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          Blog &amp; Insights
        </div>
        <h1 class="hero__title">Ideas, Updates &amp; MSP Intelligence</h1>
        <p class="hero__desc">Expert perspectives on AI operations, managed services, and the future of IT service delivery.</p>
      </div>
    </section>

    <!-- Category Filters -->
    <section class="section" aria-label="Blog categories and posts" data-animate>
      <div class="container">

        <div class="blog-filters" role="tablist" aria-label="Filter posts by category">
          <button class="blog-filter is-active" role="tab" aria-selected="true" data-category="all">All Posts</button>
          <button class="blog-filter" role="tab" aria-selected="false" data-category="ai-ops">AI &amp; Automation</button>
          <button class="blog-filter" role="tab" aria-selected="false" data-category="msp">MSP Strategy</button>
          <button class="blog-filter" role="tab" aria-selected="false" data-category="security">Security</button>
          <button class="blog-filter" role="tab" aria-selected="false" data-category="product">Product Updates</button>
          <button class="blog-filter" role="tab" aria-selected="false" data-category="case-study">Case Studies</button>
        </div>

        <!-- Post Grid -->
        <div class="blog-grid" id="blog-grid">

          <article class="card card--glass blog-card" data-category="ai-ops" data-animate>
            <div class="blog-card__meta">
              <span class="blog-card__category">AI &amp; Automation</span>
              <time datetime="2025-03-15">Mar 15, 2025</time>
            </div>
            <h2 class="blog-card__title"><a href="#">How AI Triage Reduces Ticket Volume by 40%</a></h2>
            <p class="blog-card__excerpt">Discover how DevOps AI's intelligent triage engine categorizes, prioritizes, and routes tickets before a human ever sees them.</p>
            <span class="blog-card__read-time">5 min read</span>
          </article>

          <article class="card card--glass blog-card" data-category="msp" data-animate>
            <div class="blog-card__meta">
              <span class="blog-card__category">MSP Strategy</span>
              <time datetime="2025-03-08">Mar 8, 2025</time>
            </div>
            <h2 class="blog-card__title"><a href="#">Scaling Your MSP Without Scaling Headcount</a></h2>
            <p class="blog-card__excerpt">The economics of AI-first operations: how mid-market MSPs are doubling capacity without doubling staff.</p>
            <span class="blog-card__read-time">7 min read</span>
          </article>

          <article class="card card--glass blog-card" data-category="security" data-animate>
            <div class="blog-card__meta">
              <span class="blog-card__category">Security</span>
              <time datetime="2025-02-28">Feb 28, 2025</time>
            </div>
            <h2 class="blog-card__title"><a href="#">Human-in-the-Loop: Why AI Guardrails Matter</a></h2>
            <p class="blog-card__excerpt">The case for HITL controls in managed services — and how DevOps AI implements them across all 15 zones.</p>
            <span class="blog-card__read-time">6 min read</span>
          </article>

          <article class="card card--glass blog-card" data-category="product" data-animate>
            <div class="blog-card__meta">
              <span class="blog-card__category">Product Updates</span>
              <time datetime="2025-02-15">Feb 15, 2025</time>
            </div>
            <h2 class="blog-card__title"><a href="#">What's New: Multi-Model Inference Engine</a></h2>
            <p class="blog-card__excerpt">Introducing our next-gen inference engine — route tasks to the right AI model based on complexity, cost, and compliance requirements.</p>
            <span class="blog-card__read-time">4 min read</span>
          </article>

          <article class="card card--glass blog-card" data-category="case-study" data-animate>
            <div class="blog-card__meta">
              <span class="blog-card__category">Case Studies</span>
              <time datetime="2025-02-01">Feb 1, 2025</time>
            </div>
            <h2 class="blog-card__title"><a href="#">How a 25-Person MSP Manages 500+ Endpoints with DevOps AI</a></h2>
            <p class="blog-card__excerpt">A real-world case study of operational transformation — from reactive firefighting to proactive AI-driven operations.</p>
            <span class="blog-card__read-time">8 min read</span>
          </article>

          <article class="card card--glass blog-card" data-category="ai-ops" data-animate>
            <div class="blog-card__meta">
              <span class="blog-card__category">AI &amp; Automation</span>
              <time datetime="2025-01-20">Jan 20, 2025</time>
            </div>
            <h2 class="blog-card__title"><a href="#">The 157 Process Areas Explained</a></h2>
            <p class="blog-card__excerpt">A deep dive into how DevOps AI organizes MSP operations into 15 zones and 157 process areas — and why it matters.</p>
            <span class="blog-card__read-time">10 min read</span>
          </article>

        </div>

      </div>
    </section>

    <!-- Newsletter -->
    <section class="section section--dark" aria-label="Newsletter signup" data-animate>
      <div class="container text-center">
        <h2>Stay in the Loop</h2>
        <p style="margin-inline: auto; margin-bottom: var(--space-8);">Get the latest on AI operations, MSP strategy, and product updates. No spam — just signal.</p>
        <form class="blog-newsletter" id="newsletter-form">
          <div class="blog-newsletter__input-group">
            <label for="newsletter-email" class="sr-only">Email address</label>
            <input type="email" id="newsletter-email" name="email" placeholder="you@yourmsp.com" required autocomplete="email">
            <button type="submit" class="btn btn--primary">Subscribe</button>
          </div>
          <p class="blog-newsletter__note">We respect your privacy. Unsubscribe anytime.</p>
        </form>
      </div>
    </section>'''


def blog_extra_js():
    return '''
  <script>
  /* Blog category filter */
  (function () {
    'use strict';
    var filters = document.querySelectorAll('.blog-filter');
    var cards = document.querySelectorAll('.blog-card');
    if (!filters.length || !cards.length) return;

    filters.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filters.forEach(function (f) { f.classList.remove('is-active'); f.setAttribute('aria-selected', 'false'); });
        btn.classList.add('is-active');
        btn.setAttribute('aria-selected', 'true');
        var cat = btn.getAttribute('data-category');
        cards.forEach(function (card) {
          if (cat === 'all' || card.getAttribute('data-category') === cat) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }());
  </script>'''


def login_content():
    return '''    <!-- Login Redirect -->
    <section class="section" aria-label="Login redirect" style="min-height: 60vh; display: flex; align-items: center;">
      <div class="container text-center">
        <div class="login-card card card--glass" style="max-width: 480px; margin-inline: auto; padding: var(--space-12);">
          <svg width="48" height="48" viewBox="0 0 48 48" fill="none" aria-hidden="true" style="margin-inline: auto; margin-bottom: var(--space-6);">
            <circle cx="24" cy="24" r="20" stroke="var(--accent)" stroke-width="2"/>
            <path d="M20 18l8 6-8 6" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <h1>Redirecting to DevOps AI Platform</h1>
          <p style="margin-inline: auto; margin-bottom: var(--space-6);">You're being redirected to the secure login portal. If you're not redirected automatically, click the button below.</p>
          <a href="https://platform.devops.ai.rain.tech" class="btn btn--primary btn--lg" id="login-redirect-btn" rel="noopener">Go to Platform →</a>
          <p class="text-muted" style="margin-top: var(--space-4); font-size: var(--text-sm);">platform.devops.ai.rain.tech</p>
        </div>
      </div>
    </section>'''


def login_extra_js():
    return '''
  <script>
  /* Auto-redirect to platform */
  (function () {
    'use strict';
    setTimeout(function () {
      window.location.href = 'https://platform.devops.ai.rain.tech';
    }, 2000);
  }());
  </script>'''


def why_devops_ai_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient why-hero" aria-label="Why DevOps AI hero" data-animate>
      <div class="container">
        <div class="hero__eyebrow">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.5"/>
            <path d="M8 5v4M8 11h.01" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          Why DevOps AI
        </div>
        <h1 class="hero__title">Stop Stitching Tools. Start Orchestrating.</h1>
        <p class="hero__desc">Most MSPs run 10–15 disconnected tools. DevOps AI replaces the patchwork with one AI-orchestrated control plane — purpose-built for managed services.</p>
      </div>
    </section>

    <!-- Comparison Section -->
    <section class="section" aria-label="Before and after comparison" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>The Old Way vs. The DevOps AI Way</h2>
        </div>
        <div class="why-comparison">
          <div class="why-comparison__col why-comparison__before" data-animate>
            <h3>Without DevOps AI</h3>
            <ul class="why-comparison__list">
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="var(--status-error)" stroke-width="1.5" stroke-linecap="round"/></svg>
                10–15 disconnected tools with separate logins
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="var(--status-error)" stroke-width="1.5" stroke-linecap="round"/></svg>
                Manual ticket triage — every alert needs a human
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="var(--status-error)" stroke-width="1.5" stroke-linecap="round"/></svg>
                Data scattered across vendors — no single source of truth
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="var(--status-error)" stroke-width="1.5" stroke-linecap="round"/></svg>
                Scaling means hiring — linear cost growth
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 4l8 8M12 4l-8 8" stroke="var(--status-error)" stroke-width="1.5" stroke-linecap="round"/></svg>
                Compliance is a manual checklist
              </li>
            </ul>
          </div>
          <div class="why-comparison__col why-comparison__after" data-animate>
            <h3>With DevOps AI</h3>
            <ul class="why-comparison__list">
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                One control plane — 15 zones, 157 process areas
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                AI triage handles 40% of tickets automatically
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Unified data model with full observability
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Scale capacity without scaling headcount
              </li>
              <li>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4 8l3 3 5-5" stroke="var(--accent)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Continuous compliance — automated, auditable
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Differentiators -->
    <section class="section section--dark" aria-label="Key differentiators" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>What Makes DevOps AI Different</h2>
          <p style="margin-inline: auto;">Not another RMM. Not another PSA. A fundamentally different approach to managed services.</p>
        </div>
        <div class="why-differentiators">
          <div class="card card--glass why-diff-card" data-animate>
            <h3>AI-Orchestrated, Not AI-Bolted</h3>
            <p>AI isn't a feature we added — it's the foundation. Every process area has built-in AI capabilities with human-in-the-loop controls.</p>
          </div>
          <div class="card card--glass why-diff-card" data-animate>
            <h3>Full Data Sovereignty</h3>
            <p>Deploys to your Azure tenant. Your subscription, your encryption keys, your data. Zero shared infrastructure with other customers.</p>
          </div>
          <div class="card card--glass why-diff-card" data-animate>
            <h3>15 Zones, 157 Process Areas</h3>
            <p>The most comprehensive operational coverage in the industry. From Service Desk to GRC to Financial Operations — every MSP function, unified.</p>
          </div>
          <div class="card card--glass why-diff-card" data-animate>
            <h3>Deploy in 35 Minutes</h3>
            <p>Not 35 days. Not 35 weeks. Azure Marketplace deployment with guided onboarding. You're operational the same afternoon.</p>
          </div>
          <div class="card card--glass why-diff-card" data-animate>
            <h3>21 Purpose-Built Roles</h3>
            <p>Every MSP role — from CEO to NOC tech — gets a tailored experience. The right data, the right actions, the right context.</p>
          </div>
          <div class="card card--glass why-diff-card" data-animate>
            <h3>Human-in-the-Loop Everywhere</h3>
            <p>AI handles the routine. Humans handle the exceptions. Every critical decision has a human approval step — configurable per zone, per process area.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section" aria-label="Call to action" data-animate>
      <div class="container text-center">
        <h2>See It for Yourself</h2>
        <p style="margin-inline: auto; margin-bottom: var(--space-8);">The best way to understand DevOps AI is to experience it. Deploy in your Azure tenant today.</p>
        <div class="hero__cta">
          <a href="marketplace.html" class="btn btn--primary btn--lg">Deploy on Azure →</a>
          <a href="contact.html" class="btn btn--secondary btn--lg">Request a Demo</a>
        </div>
      </div>
    </section>'''


def solutions_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient solutions-hero" aria-label="Solutions hero" data-animate>
      <div class="container">
        <div class="hero__eyebrow">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <rect x="2" y="2" width="12" height="12" rx="3" stroke="currentColor" stroke-width="1.5"/>
            <path d="M5 8h6M8 5v6" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          Solutions
        </div>
        <h1 class="hero__title">The Right Solution for Every MSP Challenge</h1>
        <p class="hero__desc">Whether you're drowning in tickets, struggling to scale, or navigating compliance — DevOps AI has a purpose-built solution.</p>
      </div>
    </section>

    <!-- By Challenge -->
    <section class="section" aria-label="Solutions by challenge" id="by-challenge" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>By Challenge</h2>
          <p style="margin-inline: auto;">What's keeping you up at night? We've got answers.</p>
        </div>
        <div class="solutions-grid">
          <div class="card card--glass solutions-card" data-animate>
            <div class="solutions-card__icon" style="color: var(--accent);">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M8 24V12l8-6 8 6v12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M13 24v-6h6v6" stroke="currentColor" stroke-width="2"/></svg>
            </div>
            <h3>Reduce Ticket Volume</h3>
            <p>AI triage, auto-categorization, and intelligent routing reduce manual ticket handling by up to 40%. Your team focuses on what matters.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
          <div class="card card--glass solutions-card" data-animate>
            <div class="solutions-card__icon" style="color: var(--cyan);">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true"><path d="M6 22l6-6 4 4 10-10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 10h6v6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <h3>Scale Without Headcount</h3>
            <p>Double your managed endpoints without doubling your team. AI automation handles the volume — humans handle the complexity.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
          <div class="card card--glass solutions-card" data-animate>
            <div class="solutions-card__icon" style="color: var(--blue-sky);">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true"><circle cx="16" cy="16" r="10" stroke="currentColor" stroke-width="2"/><path d="M16 10v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </div>
            <h3>Improve SLA Performance</h3>
            <p>Real-time SLA tracking across all clients, predictive alerting before breaches, and automated escalation workflows.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
          <div class="card card--glass solutions-card" data-animate>
            <div class="solutions-card__icon" style="color: var(--violet-bright);">
              <svg width="32" height="32" viewBox="0 0 32 32" fill="none" aria-hidden="true"><rect x="6" y="6" width="8" height="8" rx="2" stroke="currentColor" stroke-width="2"/><rect x="18" y="6" width="8" height="8" rx="2" stroke="currentColor" stroke-width="2"/><rect x="6" y="18" width="8" height="8" rx="2" stroke="currentColor" stroke-width="2"/><rect x="18" y="18" width="8" height="8" rx="2" stroke="currentColor" stroke-width="2"/></svg>
            </div>
            <h3>Consolidate Tooling</h3>
            <p>Replace 10–15 disconnected tools with one platform. One login, one data model, one pane of glass for all MSP operations.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- By Industry -->
    <section class="section section--dark" aria-label="Solutions by industry" id="by-industry" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>By Industry</h2>
          <p style="margin-inline: auto;">Compliance-ready configurations for regulated industries.</p>
        </div>
        <div class="solutions-grid">
          <div class="card card--glass solutions-card" data-animate>
            <h3>Healthcare MSPs</h3>
            <p>HIPAA-compliant operations with BAA support, PHI safeguards, and healthcare-specific process areas for patient data handling.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
          <div class="card card--glass solutions-card" data-animate>
            <h3>Financial Services</h3>
            <p>SOC 2 Type II certified with financial-grade encryption, audit logging, and regulatory reporting built into every zone.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
          <div class="card card--glass solutions-card" data-animate>
            <h3>Government &amp; SLED</h3>
            <p>CMMC-aligned operations with FedRAMP in progress. Purpose-built for state, local, and education MSPs with strict compliance requirements.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
          <div class="card card--glass solutions-card" data-animate>
            <h3>Manufacturing</h3>
            <p>OT/IT convergence support, IoT endpoint management, and industrial compliance frameworks for manufacturing MSPs.</p>
            <a href="#" class="solutions-card__link">Learn more →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- By MSP Size -->
    <section class="section" aria-label="Solutions by MSP size" id="by-size" data-animate>
      <div class="container">
        <div class="text-center" style="margin-bottom: var(--space-12);">
          <h2>By MSP Size</h2>
          <p style="margin-inline: auto;">Right-sized for where you are today, scalable for where you're going.</p>
        </div>
        <div class="solutions-size-grid">
          <div class="card card--glass solutions-size-card" data-animate>
            <h3>Small MSP <span class="text-muted">(&lt;50 staff)</span></h3>
            <p>Punch above your weight. AI automation lets a small team deliver enterprise-grade service. Start with core zones, expand as you grow.</p>
            <a href="pricing.html" class="solutions-card__link">See pricing →</a>
          </div>
          <div class="card card--glass solutions-size-card" data-animate>
            <h3>Mid-Market <span class="text-muted">(50–500)</span></h3>
            <p>The sweet spot for AI-first operations. Full platform with all 15 zones, advanced reporting, and multi-client management.</p>
            <a href="pricing.html" class="solutions-card__link">See pricing →</a>
          </div>
          <div class="card card--glass solutions-size-card" data-animate>
            <h3>Enterprise MSP <span class="text-muted">(500+)</span></h3>
            <p>Enterprise-scale operations with custom integrations, dedicated support, white-label options, and advanced compliance controls.</p>
            <a href="contact.html" class="solutions-card__link">Talk to sales →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section section--dark" aria-label="Call to action" data-animate>
      <div class="container text-center">
        <h2>Find Your Solution</h2>
        <p style="margin-inline: auto; margin-bottom: var(--space-8);">Not sure which path is right? Our team can help you map DevOps AI to your specific challenges.</p>
        <div class="hero__cta">
          <a href="contact.html" class="btn btn--primary btn--lg">Talk to Us →</a>
          <a href="marketplace.html" class="btn btn--secondary btn--lg">Deploy Now</a>
        </div>
      </div>
    </section>'''


def privacy_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient legal-hero" aria-label="Privacy policy hero" data-animate>
      <div class="container">
        <h1 class="hero__title">Privacy Policy</h1>
        <p class="hero__desc">How DevOps AI by RainTech collects, uses, and protects your personal information.</p>
        <p class="legal-effective">Effective Date: March 1, 2025 &nbsp;|&nbsp; Last Updated: March 1, 2025</p>
      </div>
    </section>

    <!-- Privacy Content -->
    <section class="section" aria-label="Privacy policy content">
      <div class="container container--narrow">
        <div class="legal-content">

          <details class="legal-section" open>
            <summary><h2>1. Information We Collect</h2></summary>
            <div class="legal-section__body">
              <h3>1.1 Information You Provide</h3>
              <p>When you create an account, contact us, or use our services, we may collect: name, email address, company name, job title, phone number, and billing information.</p>
              <h3>1.2 Information Collected Automatically</h3>
              <p>We automatically collect certain technical information when you visit our website or use our platform, including: IP address, browser type, operating system, referring URLs, pages visited, and timestamps.</p>
              <h3>1.3 Cookies and Similar Technologies</h3>
              <p>We use cookies and similar tracking technologies to enhance your experience. You can manage cookie preferences through our cookie consent banner. See Section 7 for details.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>2. How We Use Your Information</h2></summary>
            <div class="legal-section__body">
              <p>We use collected information to:</p>
              <ul>
                <li>Provide, maintain, and improve our services</li>
                <li>Process transactions and send related communications</li>
                <li>Send technical notices, security alerts, and support messages</li>
                <li>Respond to your comments, questions, and requests</li>
                <li>Monitor and analyze trends, usage, and activities</li>
                <li>Detect, investigate, and prevent security incidents</li>
                <li>Comply with legal obligations</li>
              </ul>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>3. Data Sharing and Disclosure</h2></summary>
            <div class="legal-section__body">
              <p>We do not sell your personal information. We may share information with:</p>
              <ul>
                <li><strong>Service providers:</strong> Third parties that perform services on our behalf (hosting, analytics, payment processing)</li>
                <li><strong>Compliance:</strong> When required by law, subpoena, or government request</li>
                <li><strong>Business transfers:</strong> In connection with a merger, acquisition, or sale of assets</li>
                <li><strong>With your consent:</strong> When you direct us to share information with third parties</li>
              </ul>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>4. Data Security</h2></summary>
            <div class="legal-section__body">
              <p>We implement industry-standard security measures including:</p>
              <ul>
                <li>AES-256 encryption at rest</li>
                <li>TLS 1.3 encryption in transit</li>
                <li>Zero-trust network architecture</li>
                <li>SOC 2 Type II certified controls</li>
                <li>Regular security audits and penetration testing</li>
              </ul>
              <p>Platform data is deployed to your own Azure tenant with full data sovereignty. RainTech does not have access to your operational data.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>5. Data Retention</h2></summary>
            <div class="legal-section__body">
              <p>We retain personal information for as long as necessary to fulfill the purposes for which it was collected, comply with legal obligations, resolve disputes, and enforce our agreements. When data is no longer needed, it is securely deleted or anonymized.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>6. Your Rights</h2></summary>
            <div class="legal-section__body">
              <p>Depending on your location, you may have the following rights:</p>
              <ul>
                <li><strong>Access:</strong> Request a copy of your personal data</li>
                <li><strong>Correction:</strong> Request correction of inaccurate data</li>
                <li><strong>Deletion:</strong> Request deletion of your personal data</li>
                <li><strong>Portability:</strong> Request a portable copy of your data</li>
                <li><strong>Opt-out:</strong> Opt out of marketing communications</li>
              </ul>
              <p>To exercise these rights, contact us at <a href="mailto:privacy@rain.tech">privacy@rain.tech</a>.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>7. Cookie Policy</h2></summary>
            <div class="legal-section__body">
              <p>We use the following types of cookies:</p>
              <ul>
                <li><strong>Essential cookies:</strong> Required for basic site functionality</li>
                <li><strong>Analytics cookies:</strong> Help us understand how visitors interact with our site</li>
                <li><strong>Preference cookies:</strong> Remember your settings and personalization choices</li>
              </ul>
              <p>You can manage your cookie preferences at any time through the cookie consent banner on our website.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>8. Contact Us</h2></summary>
            <div class="legal-section__body">
              <p>For privacy-related inquiries:</p>
              <address>
                <p><strong>RainTech, Inc.</strong><br>
                Attn: Privacy Office<br>
                3 S Tejon St., Suite 400<br>
                Colorado Springs, CO 80903<br>
                Email: <a href="mailto:privacy@rain.tech">privacy@rain.tech</a></p>
              </address>
            </div>
          </details>

        </div>
      </div>
    </section>'''


def terms_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient legal-hero" aria-label="Terms of service hero" data-animate>
      <div class="container">
        <h1 class="hero__title">Terms of Service</h1>
        <p class="hero__desc">The legal agreement between you and RainTech, Inc. governing your use of DevOps AI.</p>
        <p class="legal-effective">Effective Date: March 1, 2025 &nbsp;|&nbsp; Last Updated: March 1, 2025</p>
      </div>
    </section>

    <!-- Terms Content -->
    <section class="section" aria-label="Terms of service content">
      <div class="container container--narrow">
        <div class="legal-content">

          <details class="legal-section" open>
            <summary><h2>1. Acceptance of Terms</h2></summary>
            <div class="legal-section__body">
              <p>By accessing or using the DevOps AI platform ("Service") provided by RainTech, Inc. ("RainTech," "we," "us"), you agree to be bound by these Terms of Service ("Terms"). If you are using the Service on behalf of an organization, you represent that you have authority to bind that organization to these Terms.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>2. Service Description</h2></summary>
            <div class="legal-section__body">
              <p>DevOps AI is an AI-orchestrated managed service provider (MSP) control plane deployed via Microsoft Azure Marketplace. The Service includes 15 operational zones, 157 process areas, and AI-assisted automation capabilities with human-in-the-loop controls.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>3. Account Registration</h2></summary>
            <div class="legal-section__body">
              <p>To use the Service, you must:</p>
              <ul>
                <li>Provide accurate and complete registration information</li>
                <li>Maintain the security of your account credentials</li>
                <li>Promptly notify us of any unauthorized access</li>
                <li>Be responsible for all activity under your account</li>
              </ul>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>4. Subscription and Payment</h2></summary>
            <div class="legal-section__body">
              <p>The Service is available through Azure Marketplace on a subscription basis. Pricing, billing cycles, and payment terms are as specified in your Azure Marketplace subscription agreement and our pricing page. RainTech reserves the right to modify pricing with 30 days' notice.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>5. Data Ownership and Sovereignty</h2></summary>
            <div class="legal-section__body">
              <p>You retain all rights to your data. DevOps AI deploys to your Azure subscription, and your data remains in your tenant at all times. RainTech does not access, process, or store your operational data outside your Azure environment. You are responsible for compliance with applicable data protection laws.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>6. Acceptable Use</h2></summary>
            <div class="legal-section__body">
              <p>You agree to use the Service in accordance with our <a href="acceptable-use.html">Acceptable Use Policy</a> and all applicable laws. You shall not use the Service to engage in any unlawful, harmful, or fraudulent activity.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>7. Intellectual Property</h2></summary>
            <div class="legal-section__body">
              <p>RainTech retains all intellectual property rights in the Service, including software, algorithms, AI models, documentation, and trademarks. Your subscription grants a limited, non-exclusive, non-transferable license to use the Service for its intended purpose.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>8. Limitation of Liability</h2></summary>
            <div class="legal-section__body">
              <p>TO THE MAXIMUM EXTENT PERMITTED BY LAW, RAINTECH SHALL NOT BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES ARISING FROM YOUR USE OF THE SERVICE. OUR TOTAL LIABILITY SHALL NOT EXCEED THE AMOUNT YOU PAID FOR THE SERVICE IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>9. Termination</h2></summary>
            <div class="legal-section__body">
              <p>Either party may terminate the subscription with 30 days' written notice. RainTech may suspend or terminate access immediately if you violate these Terms. Upon termination, your data remains in your Azure tenant — RainTech does not delete customer data.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>10. Governing Law</h2></summary>
            <div class="legal-section__body">
              <p>These Terms are governed by the laws of the State of Colorado, without regard to conflict of law principles. Any disputes shall be resolved in the state or federal courts located in El Paso County, Colorado.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>11. Contact</h2></summary>
            <div class="legal-section__body">
              <p>For questions about these Terms:</p>
              <address>
                <p><strong>RainTech, Inc.</strong><br>
                Attn: Legal Department<br>
                3 S Tejon St., Suite 400<br>
                Colorado Springs, CO 80903<br>
                Email: <a href="mailto:legal@rain.tech">legal@rain.tech</a></p>
              </address>
            </div>
          </details>

        </div>
      </div>
    </section>'''


def acceptable_use_content():
    return '''    <!-- Hero -->
    <section class="hero--page section--gradient legal-hero" aria-label="Acceptable use policy hero" data-animate>
      <div class="container">
        <h1 class="hero__title">Acceptable Use Policy</h1>
        <p class="hero__desc">Guidelines for responsible use of the DevOps AI platform.</p>
        <p class="legal-effective">Effective Date: March 1, 2025 &nbsp;|&nbsp; Last Updated: March 1, 2025</p>
      </div>
    </section>

    <!-- AUP Content -->
    <section class="section" aria-label="Acceptable use policy content">
      <div class="container container--narrow">
        <div class="legal-content">

          <details class="legal-section" open>
            <summary><h2>1. Purpose</h2></summary>
            <div class="legal-section__body">
              <p>This Acceptable Use Policy ("AUP") defines the permitted and prohibited uses of the DevOps AI platform ("Service") provided by RainTech, Inc. This AUP supplements the <a href="terms.html">Terms of Service</a> and applies to all users of the Service.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>2. Permitted Use</h2></summary>
            <div class="legal-section__body">
              <p>The Service is designed for legitimate managed service provider operations, including but not limited to:</p>
              <ul>
                <li>IT service management and ticketing</li>
                <li>Infrastructure monitoring and management</li>
                <li>Security operations and compliance management</li>
                <li>Client relationship management</li>
                <li>Financial and operational reporting</li>
                <li>AI-assisted automation within defined guardrails</li>
              </ul>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>3. Prohibited Activities</h2></summary>
            <div class="legal-section__body">
              <p>You shall not use the Service to:</p>
              <ul>
                <li>Violate any applicable law, regulation, or third-party right</li>
                <li>Transmit malware, viruses, or other harmful code</li>
                <li>Attempt to gain unauthorized access to the Service or its infrastructure</li>
                <li>Reverse-engineer, decompile, or disassemble any part of the Service</li>
                <li>Use the Service for competitive analysis or benchmarking without written consent</li>
                <li>Circumvent or disable AI safety controls and human-in-the-loop guardrails</li>
                <li>Use AI capabilities to generate deceptive, misleading, or harmful content</li>
                <li>Exceed documented API rate limits or abuse Service resources</li>
                <li>Share account credentials or allow unauthorized access</li>
                <li>Store or process data in violation of applicable data protection laws</li>
              </ul>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>4. AI Usage Guidelines</h2></summary>
            <div class="legal-section__body">
              <p>The Service includes AI-powered automation with built-in controls. Users must:</p>
              <ul>
                <li>Maintain human oversight of AI-generated actions as configured</li>
                <li>Review and validate AI outputs before taking critical actions</li>
                <li>Report any unexpected AI behavior through the platform's reporting mechanism</li>
                <li>Not attempt to override or bypass human-in-the-loop (HITL) controls</li>
                <li>Use AI capabilities only for their intended operational purposes</li>
              </ul>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>5. Resource Usage</h2></summary>
            <div class="legal-section__body">
              <p>The Service operates within your Azure tenant. You are responsible for managing your Azure resource consumption. Excessive resource usage that degrades Service performance may result in throttling. RainTech may provide guidance on resource optimization.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>6. Enforcement</h2></summary>
            <div class="legal-section__body">
              <p>Violations of this AUP may result in:</p>
              <ul>
                <li>Warning and request to remedy the violation</li>
                <li>Temporary suspension of Service access</li>
                <li>Permanent termination of Service access</li>
                <li>Legal action for damages caused by violations</li>
              </ul>
              <p>RainTech reserves the right to investigate suspected violations and take appropriate action.</p>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>7. Reporting Violations</h2></summary>
            <div class="legal-section__body">
              <p>If you become aware of any violation of this AUP, please report it to:</p>
              <address>
                <p>Email: <a href="mailto:abuse@rain.tech">abuse@rain.tech</a><br>
                Phone: <a href="tel:+18448357246">+1-844-835-7246</a></p>
              </address>
            </div>
          </details>

          <details class="legal-section">
            <summary><h2>8. Changes to This Policy</h2></summary>
            <div class="legal-section__body">
              <p>RainTech may update this AUP from time to time. We will notify users of material changes via email or platform notification at least 30 days before the changes take effect. Continued use of the Service after changes constitutes acceptance.</p>
            </div>
          </details>

        </div>
      </div>
    </section>'''


# ─── Page definitions ────────────────────────────────────────────────────────

PAGES = [
    {
        "filename": "about.html",
        "prefix": "",
        "title": "About RainTech",
        "description": "Meet the team behind DevOps AI — the AI-orchestrated MSP control plane. Learn about RainTech's mission, values, and journey from Colorado Springs to transforming managed services.",
        "og_description": "Meet the team behind DevOps AI. Learn about RainTech's mission, values, and journey to transform managed services.",
        "canonical": "about",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "About RainTech", "item": "about"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("About RainTech", None)],
        "content_fn": about_content,
        "current_page": "about",
    },
    {
        "filename": "contact.html",
        "prefix": "",
        "title": "Contact Us",
        "description": "Get in touch with the DevOps AI team. Request a demo, ask technical questions, or explore partnership opportunities. Colorado Springs, CO.",
        "og_description": "Contact the DevOps AI team. Request a demo, get technical help, or explore partnerships.",
        "canonical": "contact",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Contact", "item": "contact"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("Contact", None)],
        "content_fn": contact_content,
        "extra_js_fn": contact_extra_js,
        "current_page": "contact",
    },
    {
        "filename": "marketplace.html",
        "prefix": "",
        "title": "Azure Marketplace",
        "description": "Deploy DevOps AI from Azure Marketplace. Two packages — MSP and Enterprise — each deploy to your Azure tenant in under 35 minutes with full data sovereignty.",
        "og_description": "Deploy DevOps AI from Azure Marketplace. MSP and Enterprise packages with full data sovereignty.",
        "canonical": "marketplace",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Azure Marketplace", "item": "marketplace"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("Azure Marketplace", None)],
        "content_fn": marketplace_content,
    },
    {
        "filename": "blog.html",
        "prefix": "",
        "title": "Blog & Insights",
        "description": "Expert perspectives on AI operations, managed services, security, and the future of IT service delivery from the DevOps AI team at RainTech.",
        "og_description": "Expert perspectives on AI operations, managed services, and IT service delivery from DevOps AI.",
        "canonical": "blog",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Blog & Insights", "item": "blog"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("Blog & Insights", None)],
        "content_fn": blog_content,
        "extra_js_fn": blog_extra_js,
    },
    {
        "filename": "login.html",
        "prefix": "",
        "title": "Log In",
        "description": "Log in to the DevOps AI platform. Auto-redirects to the secure portal at platform.devops.ai.rain.tech.",
        "og_description": "Log in to the DevOps AI platform — the AI-orchestrated MSP control plane.",
        "canonical": "login",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Log In", "item": "login"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("Log In", None)],
        "content_fn": login_content,
        "extra_js_fn": login_extra_js,
    },
    {
        "filename": "why-devops-ai.html",
        "prefix": "",
        "title": "Why DevOps AI",
        "description": "Stop stitching 10-15 tools together. DevOps AI replaces the patchwork with one AI-orchestrated MSP control plane — 15 zones, 157 process areas, full sovereignty.",
        "og_description": "Replace 10-15 disconnected tools with one AI-orchestrated MSP control plane.",
        "canonical": "why-devops-ai",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Why DevOps AI", "item": "why-devops-ai"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("Why DevOps AI", None)],
        "content_fn": why_devops_ai_content,
    },
    {
        "filename": "solutions.html",
        "prefix": "",
        "title": "Solutions",
        "description": "DevOps AI solutions for every MSP challenge, industry, and size. Reduce ticket volume, scale without headcount, improve SLAs, and consolidate tooling.",
        "og_description": "DevOps AI solutions for every MSP challenge, industry, and size.",
        "canonical": "solutions",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Solutions", "item": "solutions"}
        ],
        "breadcrumb_crumbs": [("Home", "index.html"), ("Solutions", None)],
        "content_fn": solutions_content,
    },
    {
        "filename": "legal/privacy.html",
        "prefix": "../",
        "title": "Privacy Policy",
        "description": "DevOps AI Privacy Policy. How RainTech collects, uses, and protects your personal information. SOC 2 certified, HIPAA compliant.",
        "og_description": "How DevOps AI by RainTech collects, uses, and protects your personal information.",
        "canonical": "legal/privacy",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Legal", "item": "legal"},
            {"name": "Privacy Policy", "item": "legal/privacy"}
        ],
        "breadcrumb_crumbs": [("Home", "../index.html"), ("Legal", None), ("Privacy Policy", None)],
        "content_fn": privacy_content,
    },
    {
        "filename": "legal/terms.html",
        "prefix": "../",
        "title": "Terms of Service",
        "description": "DevOps AI Terms of Service. The legal agreement governing your use of the DevOps AI platform by RainTech, Inc.",
        "og_description": "Terms of Service for the DevOps AI platform by RainTech, Inc.",
        "canonical": "legal/terms",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Legal", "item": "legal"},
            {"name": "Terms of Service", "item": "legal/terms"}
        ],
        "breadcrumb_crumbs": [("Home", "../index.html"), ("Legal", None), ("Terms of Service", None)],
        "content_fn": terms_content,
    },
    {
        "filename": "legal/acceptable-use.html",
        "prefix": "../",
        "title": "Acceptable Use Policy",
        "description": "DevOps AI Acceptable Use Policy. Guidelines for responsible use of the platform, including AI usage guidelines and prohibited activities.",
        "og_description": "Guidelines for responsible use of the DevOps AI platform.",
        "canonical": "legal/acceptable-use",
        "breadcrumbs_schema": [
            {"name": "Home", "item": ""},
            {"name": "Legal", "item": "legal"},
            {"name": "Acceptable Use Policy", "item": "legal/acceptable-use"}
        ],
        "breadcrumb_crumbs": [("Home", "../index.html"), ("Legal", None), ("Acceptable Use Policy", None)],
        "content_fn": acceptable_use_content,
    },
]


def main():
    os.makedirs(os.path.join(REPO_ROOT, "legal"), exist_ok=True)

    for page in PAGES:
        # Fix breadcrumb_crumbs for legal pages — need to handle prefix in crumbs differently
        # breadcrumb_crumbs already have prefix baked into hrefs for the first item
        # but breadcrumb_block adds prefix, so for legal pages the "Home" href should be "index.html"
        # and the prefix "../" is added by breadcrumb_block

        # Actually, looking at breadcrumb_block, it adds prefix before the href.
        # So for legal pages: prefix="../" + href="index.html" = "../index.html"
        # But we already have "../index.html" in the crumbs. Fix: use "index.html" for all
        crumbs = []
        for name, href in page["breadcrumb_crumbs"]:
            if href is not None and href.startswith("../"):
                crumbs.append((name, href[3:]))  # strip ../ since prefix adds it
            else:
                crumbs.append((name, href))

        extra_js = ""
        if "extra_js_fn" in page:
            extra_js = page["extra_js_fn"]()

        html_out = build_page(
            filename=page["filename"],
            prefix=page["prefix"],
            title=page["title"],
            description=page["description"],
            og_description=page["og_description"],
            breadcrumbs_schema=page["breadcrumbs_schema"],
            breadcrumb_crumbs=crumbs,
            main_content=page["content_fn"](),
            extra_js=extra_js,
            current_page=page.get("current_page", ""),
        )

        filepath = os.path.join(REPO_ROOT, page["filename"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"  Created: {page['filename']}")

    print(f"\nGenerated {len(PAGES)} pages.")


if __name__ == "__main__":
    main()
