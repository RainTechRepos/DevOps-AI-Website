#!/usr/bin/env python3
"""DevOps AI Website Generator — Phase 2.

Generates:
1. 113 individual process area pages (zones/{zone}/process-areas/{pa-slug}.html)
2. legal/privacy.html
3. Updates zone pages with links to individual PA pages
4. Regenerates sitemap.xml, llms.txt, llms-full.txt
"""
import os
import json
import re
from datetime import datetime

# Import everything from the existing generator
import importlib.util
spec = importlib.util.spec_from_file_location("gen", os.path.join(os.path.dirname(os.path.abspath(__file__)), "generate_site.py"))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

ZONES = gen.ZONES
ROLES = gen.ROLES
PPLX_HEAD = gen.PPLX_HEAD
HITL_LABELS = gen.HITL_LABELS

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://devops.ai.rain.tech"


def path_prefix(page_path):
    depth = page_path.count("/")
    if depth == 0:
        return ""
    return "../" * depth


def hitl_badge(level):
    label = HITL_LABELS.get(level, level)
    return f'<span class="hitl-badge hitl-badge--{level.lower()}" title="{label}">{level} — {label}</span>'


def slugify(name):
    """Convert a PA name to a URL slug."""
    s = name.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s


# Extended content for each process area — real, substantial content
# for SEO word count targets. This builds out 600+ word pages.

def generate_pa_deep_content(zone_key, pa, zone_data):
    """Generate 600+ word deep content for a process area page."""
    z = zone_data
    pa_name = pa['name']
    hitl = pa['hitl']
    hitl_label = HITL_LABELS.get(hitl, hitl)
    desc = pa['desc']
    
    # Build substantial content sections based on zone and PA context
    content = f"""
      <section class="section" aria-label="Overview">
        <div class="container container--narrow">
          <div class="fade-up" style="color: var(--text-secondary); line-height: 1.8;">
            <p>{desc}</p>
            <p>Within the {z['label']} zone, {pa_name} represents a critical operational capability that DevOps AI 
            delivers through its unified platform. This process area operates at HITL Gate Level {hitl} ({hitl_label}), 
            meaning {"AI executes fully autonomously with comprehensive audit logging — no human approval required for routine operations" if hitl == "L0" else "AI executes the action and immediately notifies the assigned human, who can review, override, or escalate the outcome after the fact" if hitl == "L1" else "AI prepares recommendations and stages actions, but a designated human must explicitly approve before execution proceeds" if hitl == "L2" else "humans perform the action directly, with AI providing decision-support intelligence, risk assessments, and contextual recommendations only"}.</p>
          </div>
        </div>
      </section>

      <section class="section" aria-label="How it works" style="background: var(--bg-secondary);">
        <div class="container container--narrow">
          <div class="section-header fade-up">
            <span class="section-label">How It Works</span>
            <h2>{pa_name} in Practice</h2>
          </div>
          <div class="fade-up" style="color: var(--text-secondary); line-height: 1.8;">
            <p>DevOps AI implements {pa_name} as a fully integrated workflow within the {z['label']} zone. 
            When deployed from the Azure Marketplace, this process area is automatically provisioned with 
            role-appropriate dashboards, notification rules, and automation policies tailored to your MSP's 
            operational requirements.</p>
            
            <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Workflow Architecture</h3>
            <p>The {pa_name} workflow follows DevOps AI's standard event-driven architecture. Events are 
            ingested through the platform's connector framework — pulling data from PSA tools (ConnectWise, 
            Datto Autotask, HaloPSA), RMM platforms (NinjaRMM, Datto RMM), and Microsoft 365 tenants — then 
            processed through the AI inference pipeline before reaching the {hitl} gate for {"automated execution" if hitl in ("L0",) else "human review" if hitl in ("L1", "L2") else "human action"}.</p>

            <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Multi-Tenant Isolation</h3>
            <p>Every operation within {pa_name} respects DevOps AI's zero-trust multi-tenant architecture. 
            Client data is isolated at the Azure tenant level, encrypted at rest with customer-managed keys, 
            and processed within geo-fenced compute boundaries. No cross-client data leakage is possible — 
            even AI models are trained on anonymized, aggregated patterns rather than raw client data.</p>
          </div>
        </div>
      </section>

      <section class="section" aria-label="HITL details">
        <div class="container container--narrow">
          <div class="section-header fade-up">
            <span class="section-label">Human-in-the-Loop</span>
            <h2>Gate Level {hitl}: {hitl_label}</h2>
          </div>
          <div class="fade-up" style="color: var(--text-secondary); line-height: 1.8;">
            <p>{pa_name} is classified at HITL Gate Level {hitl}, which defines exactly when AI acts 
            autonomously and when human judgment is required. This classification was determined through 
            risk analysis of the process area's blast radius, reversibility, and compliance implications.</p>
            
            <div class="hitl-legend" style="margin: var(--space-6) 0;">
              <div class="hitl-legend__grid">
                <div class="hitl-legend__item" style="{"border-left: 3px solid var(--accent);" if hitl == "L0" else "opacity: 0.5;" }">
                  <span class="hitl-badge hitl-badge--l0">L0 — Fully Automated</span>
                  <p>AI executes autonomously with full logging. No human approval needed.</p>
                </div>
                <div class="hitl-legend__item" style="{"border-left: 3px solid var(--accent);" if hitl == "L1" else "opacity: 0.5;" }">
                  <span class="hitl-badge hitl-badge--l1">L1 — Notify</span>
                  <p>AI executes and notifies the assigned human for review.</p>
                </div>
                <div class="hitl-legend__item" style="{"border-left: 3px solid var(--accent);" if hitl == "L2" else "opacity: 0.5;" }">
                  <span class="hitl-badge hitl-badge--l2">L2 — Approve to Proceed</span>
                  <p>AI prepares and recommends; human must approve before execution.</p>
                </div>
                <div class="hitl-legend__item" style="{"border-left: 3px solid var(--accent);" if hitl == "L3" else "opacity: 0.5;" }">
                  <span class="hitl-badge hitl-badge--l3">L3 — Human Only</span>
                  <p>Humans perform the action with AI decision support only.</p>
                </div>
              </div>
            </div>

            <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Why {hitl}?</h3>
            <p>{"This process area handles routine, low-risk operations where AI accuracy is consistently above 95%. Full automation reduces mean time to resolution while maintaining comprehensive audit trails for compliance. Every automated action is logged with full provenance — what was decided, why, and what data informed the decision." if hitl == "L0" else "This process area involves moderate-risk operations where AI accuracy is high but human awareness is important. The notify-and-review model allows AI to maintain operational velocity while ensuring humans stay informed and can intervene when edge cases arise." if hitl == "L1" else "This process area involves high-impact or partially-reversible actions where human judgment adds critical value. AI handles the analysis, preparation, and recommendation — but execution requires explicit human approval. This balances efficiency with risk management." if hitl == "L2" else "This process area involves irreversible, high-stakes, or legally significant actions where human expertise and accountability are non-negotiable. AI provides comprehensive decision support — risk assessments, historical comparisons, regulatory implications — but the human makes the final call."}</p>
          </div>
        </div>
      </section>

      <section class="section" aria-label="Integration" style="background: var(--bg-secondary);">
        <div class="container container--narrow">
          <div class="section-header fade-up">
            <span class="section-label">Integration</span>
            <h2>Platform Integration</h2>
          </div>
          <div class="fade-up" style="color: var(--text-secondary); line-height: 1.8;">
            <p>{pa_name} does not exist in isolation — it integrates with other process areas across the 
            {z['label']} zone and the broader DevOps AI platform through the event mesh architecture. 
            Actions in this process area can trigger workflows in related zones, and events from other 
            zones can feed into {pa_name} operations.</p>

            <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Connector Framework</h3>
            <p>DevOps AI's connector framework provides bi-directional integration with the tools MSPs 
            already use. For {pa_name}, this typically includes PSA platforms (ConnectWise Manage, 
            Datto Autotask, HaloPSA), Microsoft Graph API (Azure AD, Intune, Defender), and specialized 
            third-party tools relevant to {z['label']} operations. All connectors are managed through the 
            platform's Marketplace zone — install once, available everywhere.</p>

            <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Analytics & Reporting</h3>
            <p>Every operation within {pa_name} generates structured telemetry that feeds into the Analytics 
            zone. Dashboards provide real-time visibility into process area health, throughput, error rates, 
            and HITL override frequency. Over time, the AI models learn from human overrides to improve 
            future recommendations — creating a continuous improvement loop that makes {pa_name} more 
            accurate with every interaction.</p>

            <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Audit Trail</h3>
            <p>Complete audit provenance is maintained for every action within {pa_name}. This includes 
            the triggering event, AI analysis results, HITL gate decisions (including who approved and when), 
            execution outcomes, and any rollback actions. Audit data is immutable, tamper-evident, and 
            exportable in OSCAL format for compliance evidence collection.</p>
          </div>
        </div>
      </section>"""
    
    return content


def generate_pa_page(zone_key, pa_index):
    """Generate an individual process area page."""
    z = ZONES[zone_key]
    pa = z['process_areas'][pa_index]
    pa_slug = slugify(pa['name'])
    page_path = f"zones/{z['slug']}/process-areas/{pa_slug}.html"
    pfx = path_prefix(page_path)
    
    hitl_label = HITL_LABELS.get(pa['hitl'], pa['hitl'])
    
    # Sibling PA navigation
    sibling_links = ""
    for i, sibling in enumerate(z['process_areas']):
        sib_slug = slugify(sibling['name'])
        is_current = (i == pa_index)
        active_class = ' style="background: var(--accent); color: #001647; font-weight: 600;"' if is_current else ''
        sibling_links += f"""
            <a href="{pfx}zones/{z['slug']}/process-areas/{sib_slug}.html" class="crosslink-card"{active_class}>
              {hitl_badge(sibling['hitl'])}
              <span style="font-size: 13px;">{sibling['name']}</span>
            </a>"""
    
    # Related roles
    role_links = ""
    for rk in z.get("related_roles", []):
        if rk in ROLES:
            r = ROLES[rk]
            role_links += f"""
          <a href="{pfx}roles/{r['slug']}.html" class="crosslink-card">
            <span class="crosslink-card__icon">{r['icon']}</span>
            <span>{r['title']}</span>
          </a>"""
    
    # Related zones
    zone_links = ""
    for zk in z.get("related_zones", []):
        if zk in ZONES:
            rz = ZONES[zk]
            zone_links += f"""
          <a href="{pfx}zones/{rz['slug']}.html" class="crosslink-card">
            <span class="crosslink-card__icon">{rz['icon']}</span>
            <span>{rz['label']}</span>
          </a>"""
    
    deep_content = generate_pa_deep_content(zone_key, pa, z)
    
    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "name": "RainTech",
                "url": "https://devops.ai.rain.tech",
                "logo": pfx + "assets/logo-powered-by.png",
            },
            {
                "@type": "WebPage",
                "name": f"{pa['name']} — {z['label']} — DevOps AI",
                "url": f"{BASE_URL}/{page_path}",
                "description": pa['desc'],
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
                        {"@type": "ListItem", "position": 2, "name": "Platform", "item": f"{BASE_URL}/platform.html"},
                        {"@type": "ListItem", "position": 3, "name": z["label"], "item": f"{BASE_URL}/zones/{z['slug']}.html"},
                        {"@type": "ListItem", "position": 4, "name": pa["name"]}
                    ]
                },
                "creator": {
                    "@type": "SoftwareApplication",
                    "name": "Perplexity Computer",
                    "url": "https://www.perplexity.ai/computer"
                }
            }
        ]
    }, indent=2)
    
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{pa['name']} — {z['label']} | DevOps AI by RainTech</title>
<meta name="description" content="{pa['desc'][:155]}">
<link rel="canonical" href="{BASE_URL}/{page_path}">

<meta property="og:type" content="website">
<meta property="og:title" content="{pa['name']} — {z['label']} — DevOps AI">
<meta property="og:description" content="{pa['desc'][:155]}">
<meta property="og:url" content="{BASE_URL}/{page_path}">
<meta property="og:site_name" content="DevOps AI by RainTech">

<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}base.css">
<link rel="stylesheet" href="{pfx}style.css">

<script type="application/ld+json">
{json_ld}
</script>
</head>
<body>

{gen.generate_header(pa['name'], page_path)}

<main id="main-content">

  <!-- PA Hero -->
  <section class="zone-page-header" style="--zone-accent: {z['accent']};" aria-label="{pa['name']} overview">
    <div class="container">
      <nav class="breadcrumb fade-up" aria-label="Breadcrumb">
        <a href="{pfx}index.html">Home</a>
        <span class="breadcrumb-sep">/</span>
        <a href="{pfx}zones/{z['slug']}.html">{z['icon']} {z['label']}</a>
        <span class="breadcrumb-sep">/</span>
        <span aria-current="page">{pa['name']}</span>
      </nav>
      <div class="zone-badge fade-up">
        <span>{z['icon']}</span>
        <span>Zone {z['number']:02d} — Process Area</span>
      </div>
      <h1 class="fade-up">{pa['name']}</h1>
      <div class="fade-up" style="margin-top: var(--space-3);">
        {hitl_badge(pa['hitl'])}
      </div>
      <p class="zone-description fade-up">{pa['desc']}</p>
    </div>
  </section>

  {deep_content}

  <!-- Sibling PAs -->
  <section class="section crosslink-section" aria-label="Other process areas in {z['label']}">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">{z['icon']} {z['label']}</span>
        <h2>All Process Areas in {z['label']}</h2>
        <p>Explore other process areas within the {z['label']} zone.</p>
      </div>
      <div class="crosslink-grid fade-up" style="grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));">{sibling_links}
      </div>
    </div>
  </section>

  <!-- Related Roles -->
  <section class="section crosslink-section" aria-label="Related roles" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">For Your Role</span>
        <h2>Who Uses {pa['name']}?</h2>
      </div>
      <div class="crosslink-grid fade-up">{role_links}
      </div>
    </div>
  </section>

  <!-- Related Zones -->
  <section class="section crosslink-section" aria-label="Related zones">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Connected Zones</span>
        <h2>Works With</h2>
      </div>
      <div class="crosslink-grid fade-up">{zone_links}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" aria-label="Call to action">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>See {pa['name']} in Action</h2>
        <p>Deploy DevOps AI from the Azure Marketplace and explore {z['label']} capabilities — including {pa['name']} — in your own environment.</p>
        <a href="{pfx}marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
      </div>
    </div>
  </section>

</main>

{gen.generate_footer(page_path)}
{gen.generate_cookie_banner()}

<script src="{pfx}app.js"></script>
</body>
</html>"""
    return page_path, page


def generate_privacy_page():
    """Generate the privacy policy page."""
    page_path = "legal/privacy.html"
    pfx = path_prefix(page_path)
    
    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [{
            "@type": "WebPage",
            "name": "Privacy Policy — DevOps AI",
            "url": f"{BASE_URL}/{page_path}",
            "description": "Privacy Policy for the DevOps AI website by RainTech.",
            "creator": {"@type": "SoftwareApplication", "name": "Perplexity Computer", "url": "https://www.perplexity.ai/computer"}
        }]
    }, indent=2)
    
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy Policy — DevOps AI | Powered by RainTech</title>
<meta name="description" content="Privacy Policy for the DevOps AI website. Learn how RainTech collects, uses, and protects your information.">
<link rel="canonical" href="{BASE_URL}/{page_path}">

<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}base.css">
<link rel="stylesheet" href="{pfx}style.css">

<script type="application/ld+json">
{json_ld}
</script>
</head>
<body>

{gen.generate_header("Privacy Policy", page_path)}

<main id="main-content">

  <section class="section" style="padding-top: 120px;" aria-label="Privacy Policy">
    <div class="container container--narrow">
      <h1 class="fade-up">Privacy Policy</h1>
      <p class="fade-up" style="color: var(--text-secondary); margin-bottom: var(--space-8);">
        Last updated: March 16, 2026
      </p>

      <div class="fade-up" style="color: var(--text-secondary); line-height: 1.8;">
        
        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Introduction</h2>
        <p>RainTech ("we," "our," or "us") respects your privacy and is committed to protecting the personal information you share with us. This Privacy Policy describes how we collect, use, disclose, and safeguard your information when you visit the DevOps AI website (devops.ai.rain.tech) and use our platform services.</p>
        <p>By accessing or using our website and services, you agree to the collection and use of information in accordance with this Privacy Policy. If you do not agree with the terms of this Privacy Policy, please do not access the website or use our services.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Information We Collect</h2>
        
        <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Information You Provide</h3>
        <p>We collect information you voluntarily provide when you:</p>
        <ul style="padding-left: var(--space-4); list-style: disc; margin: var(--space-3) 0;">
          <li>Fill out a contact form or request a demonstration</li>
          <li>Subscribe to our newsletter or marketing communications</li>
          <li>Create an account or register for our platform services</li>
          <li>Communicate with us via email, phone, or other channels</li>
          <li>Participate in surveys, promotions, or other interactive features</li>
        </ul>
        <p>This information may include your name, email address, phone number, company name, job title, and any other information you choose to provide.</p>

        <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Information Collected Automatically</h3>
        <p>When you visit our website, we automatically collect certain technical information, including:</p>
        <ul style="padding-left: var(--space-4); list-style: disc; margin: var(--space-3) 0;">
          <li>Browser type and version</li>
          <li>Operating system</li>
          <li>IP address (anonymized where required by law)</li>
          <li>Pages visited and time spent on each page</li>
          <li>Referring website or search terms</li>
          <li>Device type (desktop, mobile, tablet)</li>
        </ul>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Cookies and Tracking Technologies</h2>
        <p>We use cookies and similar tracking technologies to enhance your experience on our website. Cookies are small data files placed on your device that help us understand how you use our site and enable certain features.</p>
        
        <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Types of Cookies We Use</h3>
        <ul style="padding-left: var(--space-4); list-style: disc; margin: var(--space-3) 0;">
          <li><strong>Essential Cookies:</strong> Required for basic site functionality, such as page navigation and secure area access. These cannot be disabled.</li>
          <li><strong>Personalization Cookies:</strong> Used to remember your preferences, such as your role selection (e.g., MSP Owner, vCIO, Security Analyst) to tailor content and navigation to your needs. These cookies store a role identifier and personalization settings.</li>
          <li><strong>Analytics Cookies:</strong> Help us understand how visitors interact with our website by collecting anonymous usage data. We use this information to improve our site's performance and content.</li>
          <li><strong>Marketing Cookies:</strong> Used to track visitors across websites to display relevant advertisements. These cookies are only set with your explicit consent.</li>
        </ul>
        
        <h3 style="color: var(--text-primary); margin: var(--space-6) 0 var(--space-3);">Managing Cookies</h3>
        <p>When you first visit our website, a cookie consent banner allows you to accept all cookies or reject non-essential cookies. You can change your preferences at any time through your browser settings. Note that disabling personalization cookies will result in a generic site experience rather than one tailored to your role.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">How We Use Your Information</h2>
        <p>We use the information we collect to:</p>
        <ul style="padding-left: var(--space-4); list-style: disc; margin: var(--space-3) 0;">
          <li>Provide, operate, and maintain our website and platform services</li>
          <li>Personalize your experience based on your role and preferences</li>
          <li>Respond to your inquiries, comments, or requests</li>
          <li>Send you marketing and promotional communications (with your consent)</li>
          <li>Analyze usage trends to improve our website and services</li>
          <li>Detect, prevent, and address technical issues and security threats</li>
          <li>Comply with legal obligations and enforce our terms of service</li>
        </ul>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Data Sharing and Disclosure</h2>
        <p>We do not sell your personal information. We may share your information in the following circumstances:</p>
        <ul style="padding-left: var(--space-4); list-style: disc; margin: var(--space-3) 0;">
          <li><strong>Service Providers:</strong> With trusted third-party companies that help us operate our website and deliver services (e.g., hosting providers, analytics services, email delivery). These providers are contractually obligated to protect your information.</li>
          <li><strong>Legal Requirements:</strong> When required by law, court order, or governmental authority, or when we believe disclosure is necessary to protect our rights, your safety, or the safety of others.</li>
          <li><strong>Business Transfers:</strong> In connection with a merger, acquisition, or sale of all or a portion of our assets, your information may be transferred as part of that transaction.</li>
        </ul>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Data Security</h2>
        <p>We implement industry-standard technical and organizational security measures to protect your personal information, including encryption in transit (TLS 1.3) and at rest, access controls, and regular security assessments. However, no method of transmission over the Internet is 100% secure, and we cannot guarantee absolute security.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Data Retention</h2>
        <p>We retain your personal information only for as long as necessary to fulfill the purposes for which it was collected, including to satisfy legal, accounting, or reporting requirements. When your information is no longer needed, we will securely delete or anonymize it.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Your Rights</h2>
        <p>Depending on your jurisdiction, you may have the following rights regarding your personal information:</p>
        <ul style="padding-left: var(--space-4); list-style: disc; margin: var(--space-3) 0;">
          <li><strong>Access:</strong> Request a copy of the personal information we hold about you</li>
          <li><strong>Correction:</strong> Request correction of inaccurate or incomplete information</li>
          <li><strong>Deletion:</strong> Request deletion of your personal information (subject to legal retention requirements)</li>
          <li><strong>Portability:</strong> Request your data in a structured, machine-readable format</li>
          <li><strong>Objection:</strong> Object to processing of your personal information for marketing purposes</li>
          <li><strong>Restriction:</strong> Request restriction of processing in certain circumstances</li>
        </ul>
        <p>To exercise any of these rights, please contact us at the address below.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Children's Privacy</h2>
        <p>Our website and services are not intended for individuals under the age of 16. We do not knowingly collect personal information from children. If you believe we have inadvertently collected information from a child, please contact us so we can promptly delete it.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">International Data Transfers</h2>
        <p>Your information may be transferred to and processed in countries other than the country in which you reside. We ensure that appropriate safeguards are in place to protect your information in accordance with applicable data protection laws.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Changes to This Policy</h2>
        <p>We may update this Privacy Policy from time to time to reflect changes in our practices or applicable laws. We will notify you of material changes by posting the updated policy on this page with a revised "Last updated" date. We encourage you to review this page periodically.</p>

        <h2 style="color: var(--text-primary); margin: var(--space-8) 0 var(--space-3);">Contact Us</h2>
        <p>If you have questions about this Privacy Policy or wish to exercise your data rights, please contact us:</p>
        <p style="margin: var(--space-3) 0;">
          <strong>RainTech</strong><br>
          3 S Tejon St., Suite 400<br>
          Colorado Springs, CO 80903<br>
          Phone: 844.TEL.RAIN<br>
          Email: <a href="mailto:privacy@rain.tech" style="color: var(--accent);">privacy@rain.tech</a>
        </p>
      </div>
    </div>
  </section>

</main>

{gen.generate_footer(page_path)}
{gen.generate_cookie_banner()}

<script src="{pfx}app.js"></script>
</body>
</html>"""
    return page


def update_zone_page_with_pa_links(zone_key):
    """Regenerate zone page with links to individual PA pages."""
    z = ZONES[zone_key]
    page_path = f"zones/{z['slug']}.html"
    pfx = path_prefix(page_path)
    
    # Process area cards with links to individual pages
    pa_cards = ""
    for pa in z["process_areas"]:
        pa_slug = slugify(pa['name'])
        pa_cards += f"""
        <a href="{pfx}zones/{z['slug']}/process-areas/{pa_slug}.html" class="process-card fade-up" style="text-decoration: none; color: inherit; display: block;">
          <div class="process-card__header">
            <h3 class="process-card__title">{pa['name']}</h3>
            {hitl_badge(pa['hitl'])}
          </div>
          <p class="process-card__body">{pa['desc']}</p>
          <span style="display:inline-block;margin-top:var(--space-2);font-size:13px;color:var(--accent);font-weight:600;">Deep Dive →</span>
        </a>"""

    # Related roles
    role_links = ""
    for rk in z.get("related_roles", []):
        if rk in ROLES:
            r = ROLES[rk]
            role_links += f"""
          <a href="{pfx}roles/{r['slug']}.html" class="crosslink-card">
            <span class="crosslink-card__icon">{r['icon']}</span>
            <span>{r['title']}</span>
          </a>"""

    # Related zones
    zone_links = ""
    for zk in z.get("related_zones", []):
        if zk in ZONES:
            rz = ZONES[zk]
            zone_links += f"""
          <a href="{pfx}zones/{rz['slug']}.html" class="crosslink-card">
            <span class="crosslink-card__icon">{rz['icon']}</span>
            <span>{rz['label']}</span>
          </a>"""

    # HITL legend
    hitl_legend = """
    <div class="hitl-legend fade-up">
      <h3>Understanding HITL Gate Levels</h3>
      <p>Every process area in DevOps AI is classified by its Human-in-the-Loop (HITL) gate level — defining when AI acts autonomously and when human approval is required.</p>
      <div class="hitl-legend__grid">
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l0">L0 — Fully Automated</span>
          <p>AI executes autonomously with full logging. No human approval needed. Examples: ticket classification, monitoring alerts, report generation.</p>
        </div>
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l1">L1 — Notify</span>
          <p>AI executes and notifies the assigned human. Human can review, override, or escalate after the fact. Examples: SLA predictions, patch scheduling.</p>
        </div>
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l2">L2 — Approve to Proceed</span>
          <p>AI prepares and recommends, but a human must explicitly approve before execution. Examples: change requests, contract modifications, campaign launches.</p>
        </div>
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l3">L3 — Human Only</span>
          <p>Humans perform the action with AI providing decision support only. Examples: legal review, privileged access approval, incident legal response.</p>
        </div>
      </div>
    </div>"""

    json_ld = gen.generate_json_ld("zone", {
        "title": f"{z['label']} — DevOps AI Zone {z['number']}",
        "description": z["tagline"],
        "breadcrumbs": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Platform", "item": f"{BASE_URL}/platform.html"},
            {"@type": "ListItem", "position": 3, "name": z["label"]}
        ]
    }, page_path)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{z['label']} — DevOps AI Zone {z['number']} | Powered by RainTech</title>
<meta name="description" content="{z['tagline']}">
<link rel="canonical" href="{BASE_URL}/{page_path}">

<meta property="og:type" content="website">
<meta property="og:title" content="{z['label']} — DevOps AI Zone {z['number']}">
<meta property="og:description" content="{z['tagline']}">
<meta property="og:url" content="{BASE_URL}/{page_path}">
<meta property="og:site_name" content="DevOps AI by RainTech">

<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}base.css">
<link rel="stylesheet" href="{pfx}style.css">

<script type="application/ld+json">
{json_ld}
</script>
</head>
<body>

{gen.generate_header(z['label'], page_path)}

<main id="main-content">

  <!-- Zone Hero -->
  <section class="zone-page-header" style="--zone-accent: {z['accent']};" aria-label="{z['label']} overview">
    <div class="container">
      <div class="zone-badge fade-up">
        <span>{z['icon']}</span>
        <span>Zone {z['number']:02d}</span>
      </div>
      <h1 class="fade-up">{z['label']}</h1>
      <p class="zone-description fade-up">{z['tagline']}</p>
    </div>
  </section>

  <!-- Zone Description -->
  <section class="section" aria-label="About {z['label']}">
    <div class="container container--narrow">
      <div class="fade-up" style="font-size: var(--text-base); color: var(--text-secondary); line-height: 1.7;">
        <p>{z['description']}</p>
      </div>
    </div>
  </section>

  <!-- Process Areas -->
  <section class="section" aria-label="Process Areas" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Process Areas</span>
        <h2>{len(z['process_areas'])} Process Areas</h2>
        <p>Each process area is classified with a Human-in-the-Loop (HITL) gate level — defining the boundary between AI autonomy and human oversight. Click any process area for a deep dive.</p>
      </div>
      <div class="process-grid">{pa_cards}
      </div>
    </div>
  </section>

  <!-- HITL Legend -->
  <section class="section" aria-label="HITL gate levels">
    <div class="container container--narrow">
      {hitl_legend}
    </div>
  </section>

  <!-- Related Roles -->
  <section class="section crosslink-section" aria-label="Related roles" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">For Your Role</span>
        <h2>Who Uses {z['label']}?</h2>
        <p>See how {z['label']} transforms daily operations for these roles.</p>
      </div>
      <div class="crosslink-grid fade-up">{role_links}
      </div>
    </div>
  </section>

  <!-- Related Zones -->
  <section class="section crosslink-section" aria-label="Related zones">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Connected Zones</span>
        <h2>Works With</h2>
        <p>{z['label']} integrates deeply with these operational zones.</p>
      </div>
      <div class="crosslink-grid fade-up">{zone_links}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" aria-label="Call to action">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>See {z['label']} in Action</h2>
        <p>Deploy DevOps AI from the Azure Marketplace and explore {z['label']} capabilities in your own environment.</p>
        <a href="{pfx}marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
      </div>
    </div>
  </section>

</main>

{gen.generate_footer(page_path)}
{gen.generate_cookie_banner()}

<script src="{pfx}app.js"></script>
</body>
</html>"""
    return page


def generate_sitemap():
    """Generate comprehensive sitemap.xml."""
    now = datetime.now().strftime("%Y-%m-%d")
    
    urls = []
    
    # Root pages
    root_pages = [
        ("index.html", "1.0", "weekly"),
        ("platform.html", "0.9", "weekly"),
        ("architecture.html", "0.8", "monthly"),
        ("why-devops-ai.html", "0.8", "monthly"),
        ("solutions.html", "0.8", "monthly"),
        ("security.html", "0.8", "monthly"),
        ("marketplace.html", "0.9", "monthly"),
        ("about.html", "0.7", "monthly"),
        ("contact.html", "0.7", "monthly"),
        ("roi.html", "0.7", "monthly"),
        ("roles/index.html", "0.8", "weekly"),
        ("legal/privacy.html", "0.5", "yearly"),
    ]
    
    for path, priority, freq in root_pages:
        urls.append(f"""  <url>
    <loc>{BASE_URL}/{path}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>""")
    
    # Zone pages
    for zk, z in ZONES.items():
        urls.append(f"""  <url>
    <loc>{BASE_URL}/zones/{z['slug']}.html</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")
        
        # Process area pages
        for pa in z['process_areas']:
            pa_slug = slugify(pa['name'])
            urls.append(f"""  <url>
    <loc>{BASE_URL}/zones/{z['slug']}/process-areas/{pa_slug}.html</loc>
    <lastmod>{now}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")
    
    # Role pages
    for rk, r in ROLES.items():
        urls.append(f"""  <url>
    <loc>{BASE_URL}/roles/{r['slug']}.html</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>""")
    
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
    return sitemap


def generate_llms_txt():
    """Generate llms.txt for AI crawler discovery."""
    lines = [
        "# DevOps AI by RainTech",
        "",
        "> AI-powered operational platform for Managed Service Providers (MSPs), deployed from the Azure Marketplace.",
        "",
        "## Core Pages",
        f"- [Home]({BASE_URL}/)",
        f"- [Platform Overview]({BASE_URL}/platform.html)",
        f"- [Architecture]({BASE_URL}/architecture.html)",
        f"- [Why DevOps AI]({BASE_URL}/why-devops-ai.html)",
        f"- [Solutions]({BASE_URL}/solutions.html)",
        f"- [Security]({BASE_URL}/security.html)",
        f"- [Marketplace]({BASE_URL}/marketplace.html)",
        f"- [About]({BASE_URL}/about.html)",
        f"- [Contact]({BASE_URL}/contact.html)",
        f"- [ROI Calculator]({BASE_URL}/roi.html)",
        f"- [Privacy Policy]({BASE_URL}/legal/privacy.html)",
        "",
        "## Zones (15 Operational Zones)",
    ]
    
    for zk, z in ZONES.items():
        lines.append(f"- [{z['label']}]({BASE_URL}/zones/{z['slug']}.html)")
    
    lines.extend(["", "## Roles (14 Role-Specific Experiences)"])
    for rk, r in ROLES.items():
        lines.append(f"- [{r['title']}]({BASE_URL}/roles/{r['slug']}.html)")
    
    lines.extend(["", "## Process Areas (113 Deep-Dive Pages)"])
    for zk, z in ZONES.items():
        for pa in z['process_areas']:
            pa_slug = slugify(pa['name'])
            lines.append(f"- [{pa['name']} ({z['label']})]({BASE_URL}/zones/{z['slug']}/process-areas/{pa_slug}.html)")
    
    return "\n".join(lines)


def generate_llms_full_txt():
    """Generate llms-full.txt with complete content for AI crawlers."""
    sections = [
        "# DevOps AI — Complete Content Reference",
        "",
        "This document contains the full structured content of the DevOps AI website for AI/LLM consumption.",
        "",
        "## Platform Overview",
        "DevOps AI is an AI-powered operational platform for Managed Service Providers (MSPs). It organizes MSP operations into 15 zones, each containing process areas with defined Human-in-the-Loop (HITL) gate levels.",
        "",
        "## HITL Gate Levels",
        "- L0 (Fully Automated): AI executes autonomously with full logging",
        "- L1 (Notify): AI executes and notifies human for review",
        "- L2 (Approve to Proceed): AI recommends, human must approve",
        "- L3 (Human Only): Human acts with AI decision support",
        "",
    ]
    
    for zk, z in ZONES.items():
        sections.append(f"## Zone {z['number']:02d}: {z['label']}")
        sections.append(f"**Tagline:** {z['tagline']}")
        sections.append(f"**Description:** {z['description']}")
        sections.append("")
        sections.append("### Process Areas")
        for pa in z['process_areas']:
            sections.append(f"- **{pa['name']}** [{pa['hitl']}]: {pa['desc']}")
        sections.append("")
    
    sections.append("## Roles")
    for rk, r in ROLES.items():
        sections.append(f"### {r['title']}")
        sections.append(f"**Tagline:** {r['tagline']}")
        pz = ", ".join(ZONES[zk]['label'] for zk in r.get('primary_zones', []) if zk in ZONES)
        sections.append(f"**Primary Zones:** {pz}")
        sections.append("")
    
    return "\n".join(sections)


def main():
    generated = []
    
    print("Phase 2: Generating process area pages...")
    
    # 1. Generate all PA pages
    pa_count = 0
    for zone_key, z in ZONES.items():
        zone_dir = os.path.join(SITE_DIR, "zones", z['slug'], "process-areas")
        os.makedirs(zone_dir, exist_ok=True)
        
        for i, pa in enumerate(z['process_areas']):
            pa_path, pa_html = generate_pa_page(zone_key, i)
            filepath = os.path.join(SITE_DIR, pa_path)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w") as f:
                f.write(pa_html)
            generated.append(filepath)
            pa_count += 1
            pa_slug = slugify(pa['name'])
            print(f"  ✓ zones/{z['slug']}/process-areas/{pa_slug}.html")
    
    print(f"\nGenerated {pa_count} process area pages.")
    
    # 2. Generate privacy page
    print("\nGenerating privacy page...")
    privacy_dir = os.path.join(SITE_DIR, "legal")
    os.makedirs(privacy_dir, exist_ok=True)
    filepath = os.path.join(privacy_dir, "privacy.html")
    with open(filepath, "w") as f:
        f.write(generate_privacy_page())
    generated.append(filepath)
    print("  ✓ legal/privacy.html")
    
    # 3. Update zone pages with PA links
    print("\nUpdating zone pages with PA links...")
    for zone_key, z in ZONES.items():
        filepath = os.path.join(SITE_DIR, "zones", f"{z['slug']}.html")
        with open(filepath, "w") as f:
            f.write(update_zone_page_with_pa_links(zone_key))
        generated.append(filepath)
        print(f"  ✓ zones/{z['slug']}.html (updated)")
    
    # 4. Regenerate sitemap
    print("\nRegenerating sitemap.xml...")
    filepath = os.path.join(SITE_DIR, "sitemap.xml")
    with open(filepath, "w") as f:
        f.write(generate_sitemap())
    print("  ✓ sitemap.xml")
    
    # 5. Regenerate llms.txt
    print("\nRegenerating llms.txt...")
    filepath = os.path.join(SITE_DIR, "llms.txt")
    with open(filepath, "w") as f:
        f.write(generate_llms_txt())
    print("  ✓ llms.txt")
    
    # 6. Regenerate llms-full.txt
    print("\nRegenerating llms-full.txt...")
    filepath = os.path.join(SITE_DIR, "llms-full.txt")
    with open(filepath, "w") as f:
        f.write(generate_llms_full_txt())
    print("  ✓ llms-full.txt")
    
    # Count totals
    total_html = 0
    for root, dirs, files in os.walk(SITE_DIR):
        for f in files:
            if f.endswith('.html'):
                total_html += 1
    
    print(f"\n{'='*50}")
    print(f"Phase 2 complete!")
    print(f"  New pages generated: {pa_count + 1}")  # PAs + privacy
    print(f"  Zone pages updated: 15")
    print(f"  Total HTML pages: {total_html}")
    print(f"{'='*50}")
    
    return generated


if __name__ == "__main__":
    main()
