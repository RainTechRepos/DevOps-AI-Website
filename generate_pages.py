#!/usr/bin/env python3
"""Generate all new pages and update existing ones for the DevOps AI website expansion."""

import os

BASE = "/home/user/workspace/devops-ai-website"

# ============================================================
# SHARED COMPONENTS
# ============================================================

PPLX_HEAD = '''<!--
   ______                            __
  / ____/___  ____ ___  ____  __  __/ /____  _____
 / /   / __ \\/ __ `__ \\/ __ \\/ / / / __/ _ \\/ ___/
/ /___/ /_/ / / / / / / /_/ / /_/ / /_/  __/ /
\\____/\\____/_/ /_/ /_/ .___/\\__,_/\\__/\\___/_/
                    /_/
        Created with Perplexity Computer
        https://www.perplexity.ai/computer
-->
<meta name="generator" content="Perplexity Computer">
<meta name="author" content="Perplexity Computer">
<meta property="og:see_also" content="https://www.perplexity.ai/computer">
<link rel="author" href="https://www.perplexity.ai/computer">'''

def nav_html(active="", depth=0):
    """Generate the mega-menu navigation. depth=0 for root pages, depth=1 for pages in subdirectories."""
    prefix = "../" if depth == 1 else ""
    
    def ac(page):
        return ' is-active' if active == page else ''
    
    return f'''<header class="site-header" role="banner">
  <div class="container header-inner">
    <a href="{prefix}index.html" class="header-logo" aria-label="DevOps AI Home">
      <img src="{prefix}assets/logo-powered-by.png" alt="DevOps AI — Powered by RainTech" width="200" height="40">
    </a>
    <nav class="nav-links" role="navigation" aria-label="Main navigation">
      <div class="nav-item">
        <a href="{prefix}platform.html" class="nav-link{ac('platform')}">Platform <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu mega-menu--wide">
          <div class="mega-menu-grid">
            <div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Overview</div>
                <a href="{prefix}platform.html" class="mega-menu-link"><span class="link-text"><strong>Platform Overview</strong><span>12-zone AI-orchestrated control plane</span></span></a>
                <a href="{prefix}why-devops-ai.html" class="mega-menu-link"><span class="link-text"><strong>Why DevOps AI</strong><span>Compare to traditional MSP tools</span></span></a>
              </div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Operations</div>
                <div class="mega-zone-grid">
                  <a href="{prefix}zones/service-desk.html" class="mega-zone-link"><span class="mzl-icon">🎫</span> Service Desk</a>
                  <a href="{prefix}zones/projects.html" class="mega-zone-link"><span class="mzl-icon">📋</span> Projects</a>
                  <a href="{prefix}zones/network-ops.html" class="mega-zone-link"><span class="mzl-icon">🌐</span> Network Ops</a>
                  <a href="{prefix}zones/endpoint-management.html" class="mega-zone-link"><span class="mzl-icon">💻</span> Endpoints</a>
                </div>
              </div>
            </div>
            <div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Security &amp; Compliance</div>
                <div class="mega-zone-grid">
                  <a href="{prefix}zones/security-operations.html" class="mega-zone-link"><span class="mzl-icon">🛡️</span> Security Ops</a>
                  <a href="{prefix}zones/grc-compliance.html" class="mega-zone-link"><span class="mzl-icon">⚖️</span> GRC</a>
                </div>
              </div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Business</div>
                <div class="mega-zone-grid">
                  <a href="{prefix}zones/accounting.html" class="mega-zone-link"><span class="mzl-icon">📊</span> Accounting</a>
                  <a href="{prefix}zones/business-development.html" class="mega-zone-link"><span class="mzl-icon">🚀</span> Biz Dev</a>
                  <a href="{prefix}zones/vc-suite.html" class="mega-zone-link"><span class="mzl-icon">🧭</span> vC-Suite</a>
                  <a href="{prefix}zones/analytics.html" class="mega-zone-link"><span class="mzl-icon">📈</span> Analytics</a>
                </div>
              </div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Platform</div>
                <div class="mega-zone-grid">
                  <a href="{prefix}zones/devops.html" class="mega-zone-link"><span class="mzl-icon">⚙️</span> DevOps</a>
                  <a href="{prefix}zones/learning.html" class="mega-zone-link"><span class="mzl-icon">🎓</span> Learning</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-item">
        <a href="{prefix}solutions.html" class="nav-link{ac('solutions')}">Solutions <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu">
          <div class="mega-menu-section">
            <a href="{prefix}solutions.html#healthcare" class="mega-menu-link"><span class="link-text"><strong>Healthcare &amp; HIPAA</strong><span>HIPAA-ready managed services</span></span></a>
            <a href="{prefix}solutions.html#defense" class="mega-menu-link"><span class="link-text"><strong>Defense &amp; CMMC</strong><span>CMMC Level 2 compliance</span></span></a>
            <a href="{prefix}solutions.html#financial" class="mega-menu-link"><span class="link-text"><strong>Financial Services</strong><span>SOC 2 &amp; regulatory compliance</span></span></a>
            <a href="{prefix}solutions.html#compliance" class="mega-menu-link"><span class="link-text"><strong>General Compliance</strong><span>GDPR, ISO 27001, and more</span></span></a>
            <a href="{prefix}solutions.html#caas" class="mega-menu-link"><span class="link-text"><strong>Compliance as a Service</strong><span>Managed compliance programs</span></span></a>
          </div>
        </div>
      </div>
      <div class="nav-item">
        <a href="#" class="nav-link{ac('roles')}">For Your Role <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu mega-menu--wide mega-menu--roles">
          <div class="mega-menu-grid">
            <div>
              <a href="{prefix}roles/msp-owner.html" class="mega-menu-link"><span class="link-text"><strong>MSP Owner / CEO</strong><span>Scale without adding headcount</span></span></a>
              <a href="{prefix}roles/vcio.html" class="mega-menu-link"><span class="link-text"><strong>vCIO / vCISO</strong><span>Strategic advisory, automated</span></span></a>
              <a href="{prefix}roles/security-analyst.html" class="mega-menu-link"><span class="link-text"><strong>Security Analyst</strong><span>AI-augmented threat operations</span></span></a>
              <a href="{prefix}roles/service-desk-manager.html" class="mega-menu-link"><span class="link-text"><strong>Service Desk Manager</strong><span>From reactive to predictive</span></span></a>
              <a href="{prefix}roles/compliance-officer.html" class="mega-menu-link"><span class="link-text"><strong>Compliance Officer</strong><span>Continuous compliance, on autopilot</span></span></a>
            </div>
            <div>
              <a href="{prefix}roles/project-manager.html" class="mega-menu-link"><span class="link-text"><strong>Project Manager</strong><span>Deliver projects on time, every time</span></span></a>
              <a href="{prefix}roles/network-engineer.html" class="mega-menu-link"><span class="link-text"><strong>Network Engineer</strong><span>Automate the routine</span></span></a>
              <a href="{prefix}roles/account-manager.html" class="mega-menu-link"><span class="link-text"><strong>Account Manager</strong><span>From lead to QBR, one platform</span></span></a>
              <a href="{prefix}roles/finance-coordinator.html" class="mega-menu-link"><span class="link-text"><strong>Finance Coordinator</strong><span>Revenue operations, simplified</span></span></a>
              <a href="{prefix}roles/it-director.html" class="mega-menu-link"><span class="link-text"><strong>IT Director</strong><span>Your MSP, supercharged</span></span></a>
            </div>
          </div>
        </div>
      </div>
      <a href="{prefix}security.html" class="nav-link{ac('security')}">Security</a>
      <a href="{prefix}marketplace.html" class="nav-link{ac('marketplace')}">Marketplace</a>
      <div class="nav-item">
        <a href="{prefix}about.html" class="nav-link{ac('about')}">About <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu">
          <a href="{prefix}about.html" class="mega-menu-link"><span class="link-text"><strong>About RainTech</strong><span>Our mission and values</span></span></a>
          <a href="{prefix}contact.html" class="mega-menu-link"><span class="link-text"><strong>Contact</strong><span>Get in touch with our team</span></span></a>
          <a href="{prefix}roi.html" class="mega-menu-link"><span class="link-text"><strong>ROI Calculator</strong><span>Calculate your potential savings</span></span></a>
        </div>
      </div>
      <a href="{prefix}marketplace.html" class="nav-cta">Get Started
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 10h10m-4-4 4 4-4 4"/></svg>
      </a>
    </nav>
    <button class="theme-toggle" aria-label="Toggle light/dark mode" type="button">
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
    </button>
    <button class="mobile-menu-toggle" aria-label="Toggle menu" aria-expanded="false" type="button">
      <span></span>
    </button>
  </div>
</header>'''

def footer_html(depth=0):
    prefix = "../" if depth == 1 else ""
    return f'''<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{prefix}assets/logo-powered-by.png" alt="DevOps AI — Powered by RainTech" width="180" height="36">
        <p>3 S Tejon St., Suite 400<br>Colorado Springs, CO 80903</p>
        <p style="margin-top: var(--space-2);">844.TEL.RAIN</p>
        <div class="footer-tagline">People First, PERIOD.&reg;</div>
      </div>
      <div class="footer-col">
        <h4>Platform</h4>
        <a href="{prefix}platform.html">Platform Overview</a>
        <a href="{prefix}zones/service-desk.html">Service Desk</a>
        <a href="{prefix}zones/security-operations.html">Security Operations</a>
        <a href="{prefix}zones/grc-compliance.html">GRC &amp; Compliance</a>
        <a href="{prefix}why-devops-ai.html">Why DevOps AI</a>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <a href="{prefix}solutions.html#healthcare">Healthcare &amp; HIPAA</a>
        <a href="{prefix}solutions.html#defense">Defense &amp; CMMC</a>
        <a href="{prefix}solutions.html#financial">Financial Services</a>
        <a href="{prefix}roi.html">ROI Calculator</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="{prefix}about.html">About RainTech</a>
        <a href="{prefix}contact.html">Contact</a>
        <a href="{prefix}marketplace.html">Azure Marketplace</a>
        <a href="{prefix}security.html">Trust &amp; Security</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 RainTech. All rights reserved.</span>
      <span>Cloud. Security. Support. Results.</span>
      <a href="https://www.perplexity.ai/computer" target="_blank" rel="noopener noreferrer">Created with Perplexity Computer</a>
    </div>
  </div>
</footer>'''

def breadcrumb_html(items, depth=0):
    """items = list of (label, url) tuples. Last item has url=None."""
    prefix = "../" if depth == 1 else ""
    parts = []
    for i, (label, url) in enumerate(items):
        if url:
            parts.append(f'<a href="{prefix}{url}">{label}</a>')
        else:
            parts.append(f'<span class="current">{label}</span>')
        if i < len(items) - 1:
            parts.append('<span class="breadcrumb-sep">/</span>')
    return f'''<nav class="breadcrumbs" aria-label="Breadcrumb">
  <div class="container">
    <ol class="breadcrumb-list">
      {"".join(parts)}
    </ol>
  </div>
</nav>'''

def breadcrumb_schema(items):
    """Generate JSON-LD BreadcrumbList from items [(name, url)]."""
    list_items = []
    for i, (name, url) in enumerate(items):
        item = {"@type": "ListItem", "position": i+1, "name": name}
        if url:
            item["item"] = f"https://devops.ai.rain.tech/{url}"
        list_items.append(item)
    return list_items

def page_shell(title, description, canonical, breadcrumbs, active, depth, body, extra_schema=""):
    prefix = "../" if depth == 1 else ""
    bc_items = breadcrumb_schema(breadcrumbs)
    bc_json = str(bc_items).replace("'", '"')
    
    schema = f'''{{"@context":"https://schema.org","@graph":[
    {{"@type":"WebPage","name":"{title}","url":"https://devops.ai.rain.tech/{canonical}","description":"{description}",
    "breadcrumb":{{"@type":"BreadcrumbList","itemListElement":{bc_json}}},
    "creator":{{"@type":"SoftwareApplication","name":"Perplexity Computer","url":"https://www.perplexity.ai/computer"}}
    }}{extra_schema}
  ]}}'''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://devops.ai.rain.tech/{canonical}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://devops.ai.rain.tech/{canonical}">
<meta property="og:site_name" content="DevOps AI by RainTech">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">

<link rel="icon" type="image/svg+xml" href="{prefix}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}base.css">
<link rel="stylesheet" href="{prefix}style.css">

<script type="application/ld+json">
{schema}
</script>
</head>
<body>

<a href="#main-content" class="skip-to-content">Skip to main content</a>
<div class="nav-overlay" aria-hidden="true"></div>

{nav_html(active, depth)}

{breadcrumb_html(breadcrumbs, depth)}

<main id="main-content">
{body}
</main>

{footer_html(depth)}

<script src="{prefix}app.js"></script>
</body>
</html>'''

# ============================================================
# ZONE DATA
# ============================================================

ZONES = [
    {
        "slug": "service-desk",
        "name": "Service Desk",
        "number": "01",
        "icon": "🎫",
        "accent": "#2563EB",
        "tagline": "Transform reactive support into predictive service delivery",
        "description": "AI-powered ticket routing, SLA risk prediction, known error database, and co-managed IT workflows — all in one unified service desk.",
        "challenge": """Today's MSPs manage service desks with a patchwork of PSA tools, separate RMM consoles, disconnected knowledge bases, and manual ticket routing. Technicians spend 15–20% of their day just classifying and routing tickets. When a critical issue hits, they're switching between 8–12 tools to assemble context — device info in one portal, recent changes in another, known workarounds buried in a wiki somewhere else. SLA breaches happen not because teams are slow, but because nobody saw the risk coming until it was too late. For co-managed environments, the RACI matrix lives in a SharePoint spreadsheet that nobody checks, leading to ownership disputes and dropped tickets.""",
        "features": [
            ("Live Queue with SLA Risk Heatmap", "Every open ticket displayed with real-time SLA risk scores. AI predicts which tickets will breach before they do, enabling proactive queue rebalancing rather than reactive firefighting."),
            ("AI Ticket Classification", "Natural language classification routes tickets automatically. Smart deduplication groups related submissions — 10 users reporting the same Outlook outage become a single incident with an affected user list."),
            ("Context Panel", "When a technician opens a ticket, AI surfaces device info, recent changes, KEDB matches, and relevant runbooks — all without a single tab switch. Every piece of context at the moment of investigation."),
            ("Known Error Database (KEDB)", "Semantically searchable database of published workarounds. When a ticket matches a known error, the workaround surfaces automatically. Problem management and knowledge integration embedded where technicians need them."),
            ("Co-Managed RACI Engine", "RACI encoded as ticket routing rules, not a spreadsheet. Ownership determined automatically at ticket creation. Both MSP and internal IT teams see all tickets with clear ownership and escalation triggers."),
            ("SLA Performance Analytics", "Real-time compliance tracking by client, priority, and period. Breach analysis with root cause identification, trending, and improvement actions. Scheduled and on-demand reporting for QBRs."),
        ],
        "automation": [
            ("Ticket classification & priority scoring", "Autonomous", "auto"),
            ("KEDB lookup & workaround surfacing", "Autonomous", "auto"),
            ("Duplicate/related ticket detection", "Autonomous", "auto"),
            ("SLA risk prediction", "Autonomous", "auto"),
            ("L1→L2 escalation trigger", "AI-Assisted", "assisted"),
            ("P1 major incident declaration", "Always Human", "human"),
            ("Client executive communication", "Always Human", "human"),
        ],
        "cross_zones": [
            ("📋", "Projects", "zones/projects.html", "Project-related tickets"),
            ("🛡️", "Security", "zones/security-operations.html", "Security incident escalation"),
            ("🌐", "Network Ops", "zones/network-ops.html", "Alert-generated tickets"),
            ("🎓", "Learning", "zones/learning.html", "KEDB → KB article promotion"),
            ("📈", "Analytics", "zones/analytics.html", "SLA data feeds predictions"),
        ],
        "roles": [
            ("roles/service-desk-manager.html", "Service Desk Manager"),
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/it-director.html", "IT Director"),
            ("roles/network-engineer.html", "Network Engineer"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/security-operations.html", "Security Operations Zone"),
            ("roles/service-desk-manager.html", "For Service Desk Managers"),
            ("roi.html", "ROI Calculator"),
        ],
    },
    {
        "slug": "projects",
        "name": "Projects",
        "number": "02",
        "icon": "📋",
        "accent": "#4F46E5",
        "tagline": "Deliver every project on time, on budget, with full visibility",
        "description": "Complete project lifecycle management with AI-powered risk scoring, migration command center, change management, and resource planning.",
        "challenge": """MSPs today run projects across fragmented tools — task boards in PSA, Gantt charts in separate apps, change management in spreadsheets, and migration monitoring on vendor dashboards. When a deal closes, an Account Manager spends 30–90 minutes manually creating the project, selecting templates, assigning engineers, and configuring billing. Errors are frequent: wrong templates, missing contacts, billing misconfiguration. During migrations, teams juggle 5–7 concurrent tool windows. Change risk assessment depends entirely on engineer experience, and freeze windows live in calendars that nobody checks before submitting an RFC.""",
        "features": [
            ("Deal-to-Delivery Handoff", "CRM deal close triggers automated project creation. AI selects the right template from deal type, pre-populates the charter from SOW, runs capacity checks, configures billing from contract terms, and delivers a complete context package to the PM in minutes."),
            ("Migration Command Center", "Single dashboard aggregating real-time migration tool API data, PSA task status, and client communication timelines. AI monitors health across all workloads, surfaces anomalies inline, and auto-updates client-facing status portals."),
            ("Intelligent Change Risk Engine", "Every RFC auto-scored at submission using change type, affected systems, client profile, historical outcomes, and concurrent pending changes. Risk scores drive automatic routing and readiness gates are enforced programmatically."),
            ("Portfolio Dashboard with EVM", "Track budget variance, resource utilization, and profitability across all active projects. Earned Value Management metrics (CPI, SPI, EAC) calculated in real time with AI-generated status reports."),
            ("Runbook System", "Executable runbooks where steps are marked complete, automation triggered inline. AI detects runbook drift when tool UIs change. Natural language input generates structured runbook drafts."),
            ("Resource & Capacity Planning", "12-week visual capacity board showing engineer availability against project demand. Skills matrix ensures the right technicians are assigned to the right projects."),
        ],
        "automation": [
            ("Project creation from CRM deal close", "Autonomous", "auto"),
            ("Charter pre-population from SOW", "Autonomous", "auto"),
            ("Migration progress monitoring", "Autonomous", "auto"),
            ("RFC risk scoring at submission", "Autonomous", "auto"),
            ("Runbook drafting from natural language", "AI-Assisted", "assisted"),
            ("Go/no-go decision for cutover", "Always Human", "human"),
            ("SOW amendments", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🎫", "Service Desk", "zones/service-desk.html", "Project-related tickets"),
            ("📊", "Accounting", "zones/accounting.html", "Project billing milestones"),
            ("🧭", "vC-Suite", "zones/vc-suite.html", "QBR roadmap items"),
            ("🛡️", "Security", "zones/security-operations.html", "Cutover → DR activation"),
        ],
        "roles": [
            ("roles/project-manager.html", "Project Manager"),
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/account-manager.html", "Account Manager"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/service-desk.html", "Service Desk Zone"),
            ("roles/project-manager.html", "For Project Managers"),
            ("why-devops-ai.html", "Why DevOps AI"),
        ],
    },
    {
        "slug": "security-operations",
        "name": "Security Operations",
        "number": "03",
        "icon": "🛡️",
        "accent": "#DC2626",
        "tagline": "AI-augmented threat operations with human-in-the-loop safety",
        "description": "Unified SOC command center with incident response, detection engineering, vulnerability management, BCDR, privileged access, and dark web monitoring.",
        "challenge": """Security analysts in MSPs today face a brutal reality: EDR alerts in one console, SIEM in another, threat intel in a third. Every incident involves 8–12 context switches. The industry reports a 94% noise rate in SIEM environments, causing alert fatigue and missed threats. When a real incident hits, the analyst must manually build a context package — pulling telemetry from multiple tools, looking up threat intelligence, checking asset criticality, and composing client communications. Vulnerability management means exporting CSVs from scanning tools, manually prioritizing in Excel, creating separate tickets, and hoping the patch gets deployed before exploitation.""",
        "features": [
            ("SOC Command Center", "Single incident workspace with all telemetry, enrichment, and actions unified. AI pre-builds context packages before analysts touch cases. One-click containment actions push to all relevant systems. Post-incident reports auto-generated from the action log."),
            ("AI-First Alert Triage", "All intake channels converge to a single AI engine. 70–90% of Tier-1 SIEM events auto-closed as benign. Smart deduplication. Dispatcher role evolves from reactive sorter to proactive queue health manager."),
            ("Risk-Based Vulnerability Program", "Single vulnerability workspace with AI risk scoring (CVSS × EPSS × KEV × asset criticality). One-click patch ticket that triggers pre-patch backup, deploys patch, runs verification scan, closes ticket, and updates GRC control status."),
            ("BCDR with AI Recovery Intelligence", "Veeam integration enables natural language backup queries during crises. Daily automated integrity verification with screenshots as compliance evidence. DR test orchestration with RTO auto-measured."),
            ("Privileged Access Management", "JIT access provisioning with time-bound credentials. Session recording with searchable library. Break-glass procedures. Anomaly detection in privileged sessions."),
            ("Dark Web Monitoring", "Credential exposure dashboard by client, recency, and severity. Automated password resets for standard users. Executive/VIP credential alerts escalated to human analysts."),
        ],
        "automation": [
            ("Tier-1 alert triage & benign closure", "Autonomous", "auto"),
            ("Alert enrichment & context assembly", "Autonomous", "auto"),
            ("Pre-authorized Tier-1 containment", "Autonomous", "auto"),
            ("IOC extraction & propagation", "Autonomous", "auto"),
            ("Backup job monitoring & verification", "Autonomous", "auto"),
            ("Tier-2/Tier-3 alert review", "AI-Assisted", "assisted"),
            ("Endpoint isolation (production)", "Always Human", "human"),
            ("DR activation", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🎫", "Service Desk", "zones/service-desk.html", "Security incidents create tickets"),
            ("⚖️", "GRC", "zones/grc-compliance.html", "Control failures link to incidents"),
            ("💻", "Endpoints", "zones/endpoint-management.html", "Endpoint isolation, patch status"),
            ("🌐", "Network Ops", "zones/network-ops.html", "DNS + network correlation"),
        ],
        "roles": [
            ("roles/security-analyst.html", "Security Analyst"),
            ("roles/vcio.html", "vCIO / vCISO"),
            ("roles/compliance-officer.html", "Compliance Officer"),
        ],
        "related_links": [
            ("security.html", "Trust & Security Center"),
            ("zones/grc-compliance.html", "GRC & Compliance Zone"),
            ("roles/security-analyst.html", "For Security Analysts"),
            ("solutions.html#defense", "Defense & CMMC Solutions"),
        ],
    },
    {
        "slug": "grc-compliance",
        "name": "GRC & Compliance",
        "number": "04",
        "icon": "⚖️",
        "accent": "#D97706",
        "tagline": "Collect once, satisfy many — continuous compliance on autopilot",
        "description": "Master control library, CMMC assessment pipeline, continuous M365 baseline monitoring, policy management, and audit support across all frameworks.",
        "challenge": """Compliance in MSPs is calendar-driven chaos: separate Drata/Vanta instances for each framework, manual evidence collection per standard, CMMC SSP/POA&M spreadsheets maintained by hand, and compliance reporting assembled in PowerPoint before every QBR. The overlap between SOC 2 and ISO 27001 controls is 60–80%, yet evidence is collected separately for each. M365 configuration reviews happen at onboarding only — drift is discovered at the next audit or after an incident. Only 1% of defense contractors feel fully prepared for CMMC, according to CyberSheath's State of the DIB 2025 report.""",
        "features": [
            ("Master Control Library", "Single control tagged to all applicable frameworks. Evidence collected once per control satisfies SOC 2, CMMC, NIST CSF, HIPAA, and ISO 27001 simultaneously. Reduces evidence effort by 50–70% through framework crosswalk."),
            ("CMMC Assessment Pipeline", "Dedicated CMMC workflows: SPRS score gauge, AI-maintained living SSP, POA&M tracker with 180-day close tracking, and evidence repository organized by CMMC practice for C3PAO readiness."),
            ("M365 Baseline-as-Continuous-Security", "UTCM API integration monitors 300+ resource types across all tenants every 6 hours. Drift detected → AI calculates which GRC controls are now failing. Auto-remediation for low-risk drift. Baseline-as-code with version control."),
            ("Policy Management", "Template-based policy creation with approval workflows, distribution tracking, and attestation management. Version-controlled policy library with full audit trail."),
            ("Audit Support", "One-click audit evidence packages organized per auditor format. Active audit tracking with evidence request SLAs. Finding tracker with severity, remediation status, and aging."),
            ("Continuous Monitoring Dashboard", "Real-time control drift events, evidence freshness tracking, and compliance alerts. Executive dashboards shareable via client portal."),
        ],
        "automation": [
            ("Evidence collection (technical controls)", "Autonomous", "auto"),
            ("Control drift detection", "Autonomous", "auto"),
            ("M365 low-risk drift auto-remediation", "Autonomous", "auto"),
            ("Compliance reporting generation", "Autonomous", "auto"),
            ("CMMC SSP draft generation", "AI-Assisted", "assisted"),
            ("Policy draft from template", "AI-Assisted", "assisted"),
            ("Exception approvals", "Always Human", "human"),
            ("CMMC SPRS score submission", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🛡️", "Security", "zones/security-operations.html", "Control failures → incidents"),
            ("🎫", "Service Desk", "zones/service-desk.html", "Remediation tasks → tickets"),
            ("🧭", "vC-Suite", "zones/vc-suite.html", "Compliance feeds QBR content"),
            ("📊", "Accounting", "zones/accounting.html", "Audit costs, compliance billing"),
        ],
        "roles": [
            ("roles/compliance-officer.html", "Compliance Officer"),
            ("roles/vcio.html", "vCIO / vCISO"),
            ("roles/msp-owner.html", "MSP Owner"),
        ],
        "related_links": [
            ("solutions.html#defense", "Defense & CMMC Solutions"),
            ("solutions.html#healthcare", "Healthcare & HIPAA"),
            ("zones/security-operations.html", "Security Operations Zone"),
            ("security.html", "Trust & Security Center"),
        ],
    },
    {
        "slug": "network-ops",
        "name": "Network Operations",
        "number": "05",
        "icon": "🌐",
        "accent": "#0891B2",
        "tagline": "Automate the routine, focus on the complex",
        "description": "Visual network topology, SLO-based performance monitoring, capacity forecasting, SSL certificate management, and ISP connectivity tracking.",
        "challenge": """Network engineers in MSPs juggle multiple monitoring dashboards, manually maintain topology documentation that goes stale within weeks, and track SSL certificates in spreadsheets. Performance baselines are set once and never adjusted. When a site approaches its bandwidth ceiling, nobody knows until users complain. Shadow IT devices appear on networks undetected. ISP outage tracking lives in emails and memory, not in a structured system.""",
        "features": [
            ("Live Network Topology", "Interactive network graph per client with drag-and-drop visualization. Change detection surfaces new, removed, and changed devices since last scan. Shadow IT registry flags unmanaged devices for review."),
            ("SLO-Based Performance Monitoring", "Per-site dashboards tracking bandwidth, latency, jitter, and packet loss against defined SLOs. Dynamic threshold optimization adjusts baselines as network patterns evolve."),
            ("Capacity Forecasting", "30/60/90-day bandwidth projection for all sites. Circuits approaching ceiling automatically surface as roadmap items in the vC-Suite zone for client discussion."),
            ("SSL Certificate Management", "Expiry calendar across all client domains. ACME enrollment with automated DNS-01 challenge renewal. Manual certificate tracking for non-ACME environments."),
            ("Infrastructure Health", "DNS health monitoring, DNSSEC status tracking, and ISP circuit inventory with carrier contacts and outage tracking."),
            ("Automated Monthly Reports", "AI-generated client performance reports covering all SLO metrics, anomalies, and recommendations. Account Manager review before client delivery."),
        ],
        "automation": [
            ("Network discovery & topology generation", "Autonomous", "auto"),
            ("Performance baseline calculation", "Autonomous", "auto"),
            ("Anomaly detection & root cause", "Autonomous", "auto"),
            ("SSL ACME renewal", "Autonomous", "auto"),
            ("P3 auto-resolution (low-risk)", "Autonomous", "auto"),
            ("Shadow IT device disposition", "Always Human", "human"),
            ("Core switch reboot / ISP failover", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🛡️", "Security", "zones/security-operations.html", "DNS security events"),
            ("🎫", "Service Desk", "zones/service-desk.html", "Alert-to-ticket lineage"),
            ("💻", "Endpoints", "zones/endpoint-management.html", "Device enrollment affects topology"),
            ("🧭", "vC-Suite", "zones/vc-suite.html", "Capacity planning feeds roadmap"),
        ],
        "roles": [
            ("roles/network-engineer.html", "Network Engineer"),
            ("roles/service-desk-manager.html", "Service Desk Manager"),
            ("roles/it-director.html", "IT Director"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/endpoint-management.html", "Endpoint Management Zone"),
            ("zones/security-operations.html", "Security Operations Zone"),
            ("roles/network-engineer.html", "For Network Engineers"),
        ],
    },
    {
        "slug": "endpoint-management",
        "name": "Endpoint Management",
        "number": "06",
        "icon": "💻",
        "accent": "#16A34A",
        "tagline": "Fleet-wide visibility, automated compliance, intelligent patching",
        "description": "Unified RMM fleet management, ring-based patch deployment, Intune MDM policy management, automated remediation, and asset lifecycle tracking.",
        "challenge": """Endpoint engineers manage thousands of devices across dozens of clients, each with different patching windows, compliance requirements, and MDM policies. Patch deployment is a monthly scramble — no ring-based rollout, no pre-patch snapshots, no automated verification. Intune compliance policies are managed tenant by tenant. When an endpoint fails a compliance check, there's no unified view across all clients. Asset lifecycle tracking lives in spreadsheets, and EOL devices slip through the cracks until a failure forces replacement.""",
        "features": [
            ("Fleet Dashboard", "All managed endpoints with health, patch compliance, and MDM status at a glance. AI-triaged alert queue with auto-remediations visible. Cross-tenant Intune compliance summary."),
            ("Ring-Based Patch Management", "Deployment rings (pilot → standard → broad) with pre-patch backup automation. Post-patch verification scan closes the loop. CVSS-priority scheduling ensures critical patches deploy first."),
            ("Multi-Tenant Intune Management", "Compliance policies, configuration profiles, and Autopilot provisioning managed across all tenants from a single interface. Non-compliance queue with grace periods and escalations."),
            ("Automated Remediation", "Known alert patterns trigger automatic remediation scripts. Script library categorized by type with full execution logging. Auto-remediation rules configurable per alert type."),
            ("Asset Lifecycle Dashboard", "EOL timeline for all hardware assets. Warranty tracking with procurement triggers. Retirement queue for devices flagged for decommission. Feeds directly into vC-Suite roadmap discussions."),
            ("Device Detail Page", "Comprehensive device view: hardware specs, installed software, patch status with CVE mapping, monitoring data, MDM compliance, and one-click actions (remote session, push patch, isolate, retire)."),
        ],
        "automation": [
            ("RMM agent deployment", "Autonomous", "auto"),
            ("Standard monthly patch deployment", "Autonomous", "auto"),
            ("Compliance policy deployment", "Autonomous", "auto"),
            ("Auto-remediation (known patterns)", "Autonomous", "auto"),
            ("Feature updates (Windows 10→11)", "Always Human", "human"),
            ("Server enrollment (first-time)", "Always Human", "human"),
            ("Device retirement (data risk)", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🛡️", "Security", "zones/security-operations.html", "Endpoint isolation, patch compliance"),
            ("🌐", "Network Ops", "zones/network-ops.html", "Device affects topology"),
            ("🎫", "Service Desk", "zones/service-desk.html", "Alert-to-ticket, remote session"),
            ("🧭", "vC-Suite", "zones/vc-suite.html", "Asset lifecycle feeds roadmap"),
        ],
        "roles": [
            ("roles/network-engineer.html", "Network / Endpoint Engineer"),
            ("roles/service-desk-manager.html", "Service Desk Manager"),
            ("roles/it-director.html", "IT Director"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/network-ops.html", "Network Operations Zone"),
            ("zones/security-operations.html", "Security Operations Zone"),
            ("roles/network-engineer.html", "For Network Engineers"),
        ],
    },
    {
        "slug": "accounting",
        "name": "Accounting",
        "number": "07",
        "icon": "📊",
        "accent": "#059669",
        "tagline": "Revenue operations simplified — from reconciliation to recognition",
        "description": "Three-way billing reconciliation, automated invoicing, MRR/ARR tracking, procurement, contract lifecycle management, and ASC 606 revenue recognition.",
        "challenge": """MSP billing is notoriously error-prone. Billing coordinators spend 8–40 hours per month manually correlating Microsoft Partner Center CSVs, distributor invoices, and PSA agreements. Revenue leakage from missed seat additions averages 10% of MRR. Contract renewals slip through the cracks. Accounting teams switch between Partner Center, Pax8, PSA, and QuickBooks constantly. There's no unified view of client profitability that accounts for labor, tooling, and incident frequency together.""",
        "features": [
            ("Three-Way Reconciliation Engine", "Simultaneous API pull from all vendors → automated delta report → single human approval screen. Captures missed charges and eliminates tool-switching across Partner Center, Pax8, PSA, and QuickBooks."),
            ("Automated Invoice Generation", "Monthly recurring invoicing with no-exception clients processed autonomously. Project milestone billing, pro-rata calculations, and dispute resolution workflows built in."),
            ("MRR/ARR Dashboard", "Waterfall visualization: new, expansion, contraction, and churn MRR. Per-client profitability with gross margin trending. Revenue forecasting based on pipeline, renewals, and churn risk."),
            ("Procurement Marketplace", "Unified catalog across Pax8, TD Synnex, and Ingram Micro. Order tracking, renewal calendar with 90/60/30-day windows, and vendor account management."),
            ("Contract Lifecycle", "Portfolio view of all active contracts with auto-renewal flags. Kanban renewal pipeline: identify → propose → negotiate → close. E-signature queue for pending documents."),
            ("General Ledger Integration", "Chart of accounts optimized for MSP operations. Auto-posted journal entries with PSA AR to accounting AR reconciliation. Month-end close checklist with accruals and approvals."),
        ],
        "automation": [
            ("Vendor usage data collection", "Autonomous", "auto"),
            ("Three-way reconciliation + delta report", "Autonomous", "auto"),
            ("Invoice generation (no-exception)", "Autonomous", "auto"),
            ("MRR/ARR/NRR calculation", "Autonomous", "auto"),
            ("Renewal alerts", "Autonomous", "auto"),
            ("Credit memos / billing adjustments", "Always Human", "human"),
            ("Revenue recognition (deferred)", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🚀", "Biz Dev", "zones/business-development.html", "Won deals trigger billing setup"),
            ("🎫", "Service Desk", "zones/service-desk.html", "Time entries feed billing"),
            ("📋", "Projects", "zones/projects.html", "Milestone billing"),
            ("🧭", "vC-Suite", "zones/vc-suite.html", "Margin data for QBR"),
        ],
        "roles": [
            ("roles/finance-coordinator.html", "Finance Coordinator"),
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/account-manager.html", "Account Manager"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/business-development.html", "Business Development Zone"),
            ("roles/finance-coordinator.html", "For Finance Coordinators"),
            ("roi.html", "ROI Calculator"),
        ],
    },
    {
        "slug": "business-development",
        "name": "Business Development",
        "number": "08",
        "icon": "🚀",
        "accent": "#7C3AED",
        "tagline": "From lead to close to onboarding — one unified revenue engine",
        "description": "Full-cycle CRM with AI-powered ICP scoring, CPQ quoting, proposal tracking, marketing automation, and structured client onboarding.",
        "challenge": """MSP sales teams operate across disconnected tools: CRM for pipeline, separate quoting tools, manual proposal creation, and email-based follow-ups. Lead qualification relies on gut feeling rather than data-driven ICP scoring. Proposal engagement is invisible — sales reps don't know if prospects actually read their proposals. When a deal closes, the handoff to operations is manual and error-prone. Onboarding takes weeks longer than it should because there's no standardized workflow.""",
        "features": [
            ("AI-Powered Pipeline", "Pipeline dashboard with kanban stages, weighted ARR, conversion rates, and velocity metrics. ICP scoring enriches leads with company data and technology signals. Win/loss analysis reveals patterns."),
            ("CPQ / Quoting", "Configure-Price-Quote with live distributor pricing and margin floor enforcement. Proposal engagement tracking shows time per section and page opens. Below-margin items route to manager approval."),
            ("Marketing Automation", "Campaign manager with performance metrics and lead attribution. Email sequences with A/B testing and send-time optimization. Event management for seminars and webinars."),
            ("Structured Client Onboarding", "Phased 0–90 day onboarding workflow: discovery, setup, validation, QBR. Day Zero baseline metrics capture enables ROI measurement at the 60-day mark. Risk-first approach identifies inherited vulnerabilities immediately."),
            ("Meeting Intelligence", "AI transcription of discovery calls with automatic action item extraction. Pre-meeting research briefs assembled automatically. ROI narrative generation from prospect data."),
            ("Referral & Partnership Program", "Referral source tracking with attribution and reward management. Strategic partner directory for co-marketing relationships."),
        ],
        "automation": [
            ("Lead enrichment & ICP scoring", "Autonomous", "auto"),
            ("Outreach sequence personalization", "Autonomous", "auto"),
            ("Proposal engagement tracking", "Autonomous", "auto"),
            ("Meeting transcript → action items", "Autonomous", "auto"),
            ("Discovery meeting facilitation", "Always Human", "human"),
            ("Negotiation and close", "Always Human", "human"),
        ],
        "cross_zones": [
            ("📊", "Accounting", "zones/accounting.html", "Quote → contract creation"),
            ("🧭", "vC-Suite", "zones/vc-suite.html", "At-risk clients → save workflow"),
            ("📋", "Projects", "zones/projects.html", "Deal close → project creation"),
            ("📈", "Analytics", "zones/analytics.html", "Pipeline forecasting"),
        ],
        "roles": [
            ("roles/account-manager.html", "Account Manager"),
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/vcio.html", "vCIO / vCISO"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/accounting.html", "Accounting Zone"),
            ("zones/vc-suite.html", "vC-Suite Zone"),
            ("roles/account-manager.html", "For Account Managers"),
        ],
    },
    {
        "slug": "vc-suite",
        "name": "vC-Suite",
        "number": "09",
        "icon": "🧭",
        "accent": "#475569",
        "tagline": "Strategic advisory transformed — from data assembly to strategic conversation",
        "description": "AI-orchestrated QBR preparation, technology roadmaps, client health scoring, risk registers, and vCIO/vCISO/vCTO operational workspaces.",
        "challenge": """vCIOs today spend 4–8 hours per client gathering data from RMM, PSA, M365, backup, security, and asset tools to prepare for a single QBR. With 40 clients, that's 160–320 hours per month — just on data assembly. The result is inconsistent report quality, missed insights, and QBRs that feel like data reviews instead of strategic conversations. Technology roadmaps live in separate spreadsheets per client. Risk registers are maintained manually. Client health is a gut feeling rather than a data-driven score.""",
        "features": [
            ("AI-Orchestrated QBR Preparation", "Multi-source data aggregation from every zone. AI generates natural-language narrative contextualizing metrics against history and industry benchmarks. QBR prep drops from 4–8 hours to 20–30 minutes of human review."),
            ("Client Advisory Workspace", "Per-client hub with health score, MRR, contract status, QBR history, roadmap, budget, risk register, compliance posture, and security assessment — all in one view."),
            ("Technology Roadmap", "Kanban-style roadmap per client: Backlog → Approved → In-Progress → Complete. Approved roadmap items create projects with one click. Gap analysis from operational data suggests roadmap additions."),
            ("vCISO Operations", "Security posture registry with assessment results per client. MSP-wide risk register filterable by severity, framework, and status. Security awareness program management with phishing simulation tracking."),
            ("vCTO Operations", "Architecture Decision Records (ADR) library per client. Technical debt register for MSP and client-facing systems. Technology Radar: Adopt, Trial, Assess, Hold for emerging technology evaluation."),
            ("Client Lifecycle Management", "Cross-reference onboarding tracker from Business Development. Structured 30-day offboarding manager with access revocation checklist and billing close."),
        ],
        "automation": [
            ("QBR data aggregation", "Autonomous", "auto"),
            ("QBR report draft generation", "Autonomous", "auto"),
            ("Post-meeting action items", "Autonomous", "auto"),
            ("Client health score calculation", "Autonomous", "auto"),
            ("Roadmap gap analysis", "AI-Assisted", "assisted"),
            ("QBR meeting facilitation", "Always Human", "human"),
            ("Strategic recommendations", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🎫", "Service Desk", "zones/service-desk.html", "Ticket metrics feed QBR"),
            ("📋", "Projects", "zones/projects.html", "Project outcomes → roadmap"),
            ("🛡️", "Security", "zones/security-operations.html", "Security posture → vCISO"),
            ("⚖️", "GRC", "zones/grc-compliance.html", "Compliance calendar → QBR"),
            ("📊", "Accounting", "zones/accounting.html", "Margin data → advisory"),
        ],
        "roles": [
            ("roles/vcio.html", "vCIO / vCISO"),
            ("roles/account-manager.html", "Account Manager"),
            ("roles/msp-owner.html", "MSP Owner"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/analytics.html", "Analytics Zone"),
            ("zones/grc-compliance.html", "GRC & Compliance Zone"),
            ("roles/vcio.html", "For vCIO / vCISO"),
        ],
    },
    {
        "slug": "analytics",
        "name": "Analytics",
        "number": "10",
        "icon": "📈",
        "accent": "#EA580C",
        "tagline": "Cross-domain intelligence that transforms data into decisions",
        "description": "Executive dashboards, predictive intelligence (churn, security risk, ticket forecasting), license optimization, and natural language BI queries.",
        "challenge": """MSPs generate vast amounts of operational data across PSA, RMM, billing, security, and CRM — but it's impossible to correlate into actionable intelligence. True cost-to-serve per client is unknowable when labor data lives in PSA, tool costs in billing, and incident frequency in RMM. Predictive analytics is aspirational — most MSPs lack the data infrastructure to forecast ticket volume, predict churn, or score security risk. License optimization is a manual Excel exercise, with 20–30% of E5 spend wasted on users who only need E3 features.""",
        "features": [
            ("Executive Dashboard", "Business performance (MRR, churn, NRR, EBITDA), operational health (SLA compliance, MTTR, CSAT), and security posture — all with AI-generated commentary explaining trends."),
            ("Predictive Intelligence", "Churn risk scoring for all clients with trend and intervention queue. Security risk scores with 90-day trajectory. Ticket volume forecasting for staffing decisions. Budget variance prediction for in-flight projects."),
            ("License Optimization Intelligence", "Feature-level utilization analysis across all client tenants. Identifies E5 users consuming only E3 features, inactive accounts, and add-on redundancy. Generates renewal negotiation packs with cost scenarios."),
            ("True Cost-to-Serve", "Client profitability calculated from labor (PSA) + tooling (billing) + infrastructure (cloud) + incident frequency (RMM). Reveals which clients are profitable and which are loss-leading."),
            ("Natural Language BI Queries", "Ask questions in plain English and get cross-domain answers. 'Show me clients with declining security scores and increasing ticket volume' returns structured, actionable data."),
            ("Custom Dashboard Builder", "Drag-and-drop widgets from any data source. Scheduled reports with auto-generated narrative. Report library with templates and history."),
        ],
        "automation": [
            ("Dashboard KPI calculation", "Autonomous", "auto"),
            ("Churn risk scoring", "Autonomous", "auto"),
            ("Security risk scoring", "Autonomous", "auto"),
            ("Ticket volume forecasting", "Autonomous", "auto"),
            ("License utilization audit", "Autonomous", "auto"),
            ("NL-to-BI query translation", "Autonomous", "auto"),
            ("Financial forecast (external)", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🧭", "vC-Suite", "zones/vc-suite.html", "Churn risk → QBR prep"),
            ("📊", "Accounting", "zones/accounting.html", "Profitability analytics"),
            ("🚀", "Biz Dev", "zones/business-development.html", "Pipeline forecasting"),
            ("🎫", "Service Desk", "zones/service-desk.html", "Ticket forecasting → staffing"),
        ],
        "roles": [
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/vcio.html", "vCIO / vCISO"),
            ("roles/finance-coordinator.html", "Finance Coordinator"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/vc-suite.html", "vC-Suite Zone"),
            ("roi.html", "ROI Calculator"),
            ("roles/msp-owner.html", "For MSP Owners"),
        ],
    },
    {
        "slug": "devops",
        "name": "DevOps",
        "number": "11",
        "icon": "⚙️",
        "accent": "#6B7280",
        "tagline": "The infrastructure that powers the platform itself",
        "description": "CI/CD pipeline management, configuration drift detection, integration health monitoring, feature flags, A/B testing, and AI model governance.",
        "challenge": """MSPs managing client infrastructure need CI/CD pipelines, configuration baselines, and deployment automation — but these capabilities are spread across Azure DevOps, Terraform, Intune, and various RMM tools. Configuration drift goes undetected between audits. Integration health between the platform and third-party tools is monitored reactively. Feature rollouts are all-or-nothing with no controlled experimentation. AI model governance is nonexistent, even as the EU AI Act demands transparency and auditability.""",
        "features": [
            ("Pipeline Management", "CI/CD pipeline status board with stage visibility, last run status, health indicators, and artifact tracking. Deployment queue with approval-gated releases. Multi-client release calendar with conflict detection."),
            ("Configuration Drift Detection", "Golden baselines per client for IaC, Intune, RMM, and M365 configurations. Drift heatmap classifies deviations by severity (P1–P4). Low-severity drift auto-remediated; high-severity triggers human review."),
            ("Integration Health Grid", "All connectors displayed with green/amber/red sync status. API key rotation calendar with vault management. Error log for failed syncs, webhook failures, and data drift."),
            ("Feature Flags & A/B Testing", "LaunchDarkly-pattern feature flag management with rollout percentages and targeting rules. Multivariate experiment framework with statistical significance calculation. Kill switches for rapid rollback."),
            ("Platform Health Dashboard", "API latency, error rates, queue depths, and AI model health monitored continuously. SLO/error budget tracking with P95 latency vs. target. AI-generated optimization recommendations."),
            ("Environment Management", "Environment registry for all managed environments with cost tracking. Workflow launcher for provisioning and teardown. Cloud resource cost optimization alerts."),
        ],
        "automation": [
            ("IaC template generation", "AI-Assisted", "assisted"),
            ("Build/test execution", "Autonomous", "auto"),
            ("P3/P4 drift remediation", "Autonomous", "auto"),
            ("Integration health probes", "Autonomous", "auto"),
            ("Feature flag rollout", "Autonomous", "auto"),
            ("Production deployment", "Always Human", "human"),
            ("Model promotion to production", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🛡️", "Security", "zones/security-operations.html", "Config drift → GRC control"),
            ("🎫", "Service Desk", "zones/service-desk.html", "Connector failure → ticket"),
            ("📈", "Analytics", "zones/analytics.html", "Platform usage analytics"),
            ("🎓", "Learning", "zones/learning.html", "Feature changes → training"),
        ],
        "roles": [
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/vcio.html", "vCIO / vCISO"),
            ("roles/it-director.html", "IT Director"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("security.html", "Trust & Security Center"),
            ("zones/security-operations.html", "Security Operations Zone"),
            ("why-devops-ai.html", "Why DevOps AI"),
        ],
    },
    {
        "slug": "learning",
        "name": "Learning",
        "number": "12",
        "icon": "🎓",
        "accent": "#0D9488",
        "tagline": "Build institutional memory that compounds over time",
        "description": "Integrated LMS with AI tutoring, certification management, semantic knowledge base, client documentation, and adaptive learning paths.",
        "challenge": """MSPs suffer from institutional knowledge loss every time a senior engineer leaves. New technicians need 6–12 months to reach full productivity. Knowledge bases in IT Glue or Hudu become stale because nobody reviews them. Incident resolutions disappear into closed tickets. Certification tracking lives in spreadsheets. Training is disconnected from daily work — a technician troubleshooting an issue can't easily access the course that explains the underlying technology alongside the runbook that addresses the specific problem.""",
        "features": [
            ("Adaptive Learning Paths", "AI-generated onboarding paths personalized by role and skill level. Paths adapt in real time based on assessment results and daily work patterns. Manager view shows team progress, certifications, and skill gaps."),
            ("AI Tutor", "Conversational assistant grounded in course content and the knowledge base via RAG. Technicians can ask questions in natural language and receive contextually relevant answers drawn from organizational knowledge."),
            ("Certification Management", "All certifications tracked by technician with expiry calendars and renewal paths. Coverage map shows certifications vs. client SLA requirements, highlighting gaps. Automated renewal alerts at 90/60/30 days."),
            ("Semantic Knowledge Base", "Article browser searchable by category, platform, client, and recency. Review queue for peer-reviewed technical articles. Gap queue identifies missing knowledge articles from recurring incident types."),
            ("Client Documentation", "Per-client documentation equivalent to IT Glue/Hudu with completeness scoring. Auto-population from RMM and network scan data. Documentation analytics track freshness and usage patterns."),
            ("Compliance Training", "SCORM/xAPI delivery with attestation tracking. Audit evidence generation for compliance training requirements. Scheduled assignments with completion tracking."),
        ],
        "automation": [
            ("Learning path generation", "AI-Assisted", "assisted"),
            ("Certification expiry tracking", "Autonomous", "auto"),
            ("Compliance training assignment", "Autonomous", "auto"),
            ("Semantic knowledge retrieval (RAG)", "Autonomous", "auto"),
            ("Client doc auto-population", "Autonomous", "auto"),
            ("Article publication approval", "Always Human", "human"),
        ],
        "cross_zones": [
            ("🎫", "Service Desk", "zones/service-desk.html", "KEDB → KB articles, runbooks from tickets"),
            ("📋", "Projects", "zones/projects.html", "Runbooks updated at project close"),
            ("🛡️", "Security", "zones/security-operations.html", "Security playbooks, IR procedures"),
            ("📈", "Analytics", "zones/analytics.html", "Skill gaps → staffing risk"),
        ],
        "roles": [
            ("roles/service-desk-manager.html", "Service Desk Manager"),
            ("roles/msp-owner.html", "MSP Owner"),
            ("roles/it-director.html", "IT Director"),
        ],
        "related_links": [
            ("platform.html", "Platform Overview"),
            ("zones/service-desk.html", "Service Desk Zone"),
            ("why-devops-ai.html", "Why DevOps AI"),
            ("roles/service-desk-manager.html", "For Service Desk Managers"),
        ],
    },
]

def generate_zone_page(z):
    bc = [("Home", "index.html"), ("Platform", "platform.html"), (z["name"], None)]
    
    features_html = ""
    for title, desc in z["features"]:
        features_html += f'''
        <div class="zone-feature-card fade-up">
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>'''
    
    auto_rows = ""
    for cap, level, badge_class in z["automation"]:
        auto_rows += f'''
          <tr>
            <td>{cap}</td>
            <td><span class="auto-badge auto-badge--{badge_class}">{level}</span></td>
          </tr>'''
    
    cross_html = ""
    for icon, name, url, desc in z["cross_zones"]:
        cross_html += f'''
        <a href="../{url}" class="cross-zone-card fade-up">
          <span class="cz-icon">{icon}</span>
          <span>{name}<br><small style="color: var(--text-tertiary); font-weight: normal;">{desc}</small></span>
        </a>'''
    
    role_html = ""
    for url, name in z["roles"]:
        role_html += f'<a href="../{url}" class="role-tag">{name}</a>'
    
    links_html = ""
    for url, name in z["related_links"]:
        links_html += f'<li><a href="../{url}" style="color: var(--blue-sky);">{name}</a></li>'
    
    body = f'''
  <section class="zone-hero">
    <div class="container">
      <span class="zone-hero-number">{z["number"]}</span>
      <div class="zone-hero-badge fade-up"><span class="badge-icon">{z["icon"]}</span> Zone {z["number"]}</div>
      <div class="zone-accent-bar fade-up" style="background: {z["accent"]};"></div>
      <h1 class="fade-up">{z["name"]}</h1>
      <p class="zone-hero-sub fade-up">{z["tagline"]}</p>
    </div>
  </section>

  <section class="zone-section section" aria-label="The Challenge">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">The Challenge</span>
        <h2>What MSPs Struggle With Today</h2>
      </div>
      <div class="fade-up" style="max-width: 75ch;">
        <p style="font-size: var(--text-base); line-height: 1.8;">{z["challenge"]}</p>
      </div>
    </div>
  </section>

  <section class="zone-section section" aria-label="How DevOps AI Solves It" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">The Solution</span>
        <h2>How DevOps AI Solves It</h2>
        <p>Purpose-built capabilities grounded in ITIL 4, NIST frameworks, and real MSP operational patterns.</p>
      </div>
      <div class="zone-feature-grid">
        {features_html}
      </div>
    </div>
  </section>

  <section class="zone-section section" aria-label="Automation Boundary">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">AI Boundaries</span>
        <h2>What Gets Automated vs. What Stays Human</h2>
        <p>DevOps AI follows a clear four-layer model: AI handles information gathering, routing, and monitoring. Humans handle consequential decisions.</p>
      </div>
      <div class="fade-up" style="overflow-x: auto;">
        <table class="automation-table">
          <thead>
            <tr><th>Capability</th><th>Automation Level</th></tr>
          </thead>
          <tbody>
            {auto_rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="zone-section section" aria-label="Cross-Zone Intelligence" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Connected Intelligence</span>
        <h2>Cross-Zone Intelligence</h2>
        <p>The {z["name"]} zone doesn't operate in isolation. Data flows automatically between zones, creating intelligence that fragmented tools can never achieve.</p>
      </div>
      <div class="cross-zone-grid">
        {cross_html}
      </div>
    </div>
  </section>

  <section class="zone-section section" aria-label="Built for these roles">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Role Relevance</span>
        <h2>Built for These Roles</h2>
      </div>
      <div class="role-tags fade-up">
        {role_html}
      </div>
    </div>
  </section>

  <section class="section" aria-label="Related">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Explore Further</span>
        <h2>Related Pages</h2>
      </div>
      <ul class="fade-up" style="list-style: disc; padding-left: var(--space-6); max-width: 60ch;">
        {links_html}
      </ul>
    </div>
  </section>

  <section class="section" aria-label="Call to action">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>See {z["name"]} in Action</h2>
        <p>Deploy DevOps AI from the Azure Marketplace and start transforming your {z["name"].lower()} operations today.</p>
        <a href="../marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
      </div>
    </div>
  </section>
'''
    
    return page_shell(
        title=f'{z["name"]} — DevOps AI Zone {z["number"]} | RainTech',
        description=z["description"],
        canonical=f'zones/{z["slug"]}.html',
        breadcrumbs=bc,
        active="platform",
        depth=1,
        body=body
    )


# ============================================================
# ROLE DATA
# ============================================================

ROLES = [
    {
        "slug": "msp-owner",
        "title": "MSP Owner / CEO",
        "tagline": "Scale without adding headcount",
        "description": "See how DevOps AI empowers MSP owners and CEOs to grow revenue, reduce operational costs, and scale their business without proportionally increasing staff.",
        "pain_points": [
            "Reviewing financials across disconnected PSA, billing, and accounting tools",
            "Hiring more engineers just to keep up with ticket volume growth",
            "No visibility into true client profitability or cost-to-serve",
            "QBR preparation consuming vCIO time that should be strategic",
            "Tool sprawl: 12+ separate platforms with separate licenses and logins",
            "Revenue leakage from manual billing reconciliation errors",
        ],
        "transformed": [
            "Single executive dashboard: MRR, churn, EBITDA, and operational health at a glance",
            "AI handles 70–90% of Tier-1 tickets — your team focuses on complex work",
            "True cost-to-serve per client calculated automatically from all data sources",
            "QBR prep drops from 4–8 hours to 20–30 minutes of human review",
            "One platform replaces 8–12 separate tools with unified intelligence",
            "Three-way billing reconciliation captures an average of 10% missed MRR",
        ],
        "zones": [
            ("📈", "Analytics", "Predictive intelligence: churn risk, ticket forecasting, client profitability"),
            ("🧭", "vC-Suite", "AI-orchestrated QBR prep and client advisory"),
            ("📊", "Accounting", "Automated reconciliation and revenue operations"),
            ("🚀", "Business Development", "Pipeline visibility and deal-to-delivery automation"),
        ],
        "faqs": [
            ("How quickly can we deploy DevOps AI?", "DevOps AI deploys as an Azure Managed Application in under 35 minutes. It provisions into your existing Azure tenant with private endpoints, firewall rules, and infrastructure included. Your team can start using the platform immediately."),
            ("Will our data leave our Azure tenant?", "No. All data stays in your Azure tenant. No traffic leaves the VNet. Public AI APIs are blocked at the firewall. Private endpoints are used throughout. Your data, your control, always."),
            ("How does DevOps AI reduce headcount needs?", "By automating 70–90% of Tier-1 alert triage, predictive SLA management, billing reconciliation, and QBR data assembly, your existing team handles significantly more work. Based on market data, MSPs can expect $180K–$275K in annual savings per 50-person organization from AI automation."),
            ("Can we try it before committing?", "DevOps AI is available directly through the Azure Marketplace with product-led deployment. No sales calls required. Browse, deploy, and evaluate on your own terms."),
        ],
        "stat": "$180K–$275K",
        "stat_desc": "projected annual savings per 50-person MSP from AI automation",
        "stat_cite": "Attainment Labs",
        "stat_url": "https://www.attainmentlabs.com/roi-analysis/it-msp-ai-automation",
    },
    {
        "slug": "vcio",
        "title": "vCIO / vCISO",
        "tagline": "Strategic advisory, automated",
        "description": "DevOps AI transforms vCIO and vCISO roles from data assembly to strategic conversation — with AI-orchestrated QBR prep, living roadmaps, and cross-client intelligence.",
        "pain_points": [
            "Spending 4–8 hours per client gathering data for QBR preparation",
            "Maintaining technology roadmaps in separate spreadsheets per client",
            "Manual risk register management with no real-time data feeds",
            "No unified view of security posture across the client portfolio",
            "QBRs that feel like data reviews instead of strategic conversations",
            "Inconsistent report quality depending on the vCIO's available time",
        ],
        "transformed": [
            "QBR prep drops from 4–8 hours to 20–30 minutes of review and refinement",
            "Living technology roadmaps fed by operational data — roadmap items auto-suggested from gap analysis",
            "Risk registers automatically updated from security scans, compliance drift, and incident data",
            "Portfolio-wide security posture dashboard with per-client CSF/CIS scoring",
            "AI-generated narrative commentary contextualizing every metric against history and benchmarks",
            "vCIO capacity effectively doubles without adding headcount",
        ],
        "zones": [
            ("🧭", "vC-Suite", "QBR workspace, roadmaps, client health scoring, risk registers"),
            ("🛡️", "Security", "Security posture assessment feeds vCISO advisory"),
            ("⚖️", "GRC", "Compliance calendar and framework status for QBR content"),
            ("📈", "Analytics", "Predictive intelligence for strategic decision-making"),
        ],
        "faqs": [
            ("How does AI-orchestrated QBR prep work?", "DevOps AI aggregates data from every operational zone — tickets, projects, security posture, compliance status, billing, and client health metrics. It generates a natural-language report draft with narrative commentary, benchmark comparisons, and roadmap status. The vCIO reviews and refines in 20–30 minutes instead of assembling raw data for 4–8 hours."),
            ("What if I manage 40+ clients?", "That's exactly the scale where DevOps AI delivers maximum impact. For a vCIO with 40 clients, QBR prep alone recovers 160–320 hours per month. Cross-client intelligence surfaces portfolio-wide trends and shared vulnerabilities that would be invisible when managing clients individually."),
            ("Does it replace the vCIO role?", "Absolutely not. DevOps AI amplifies the vCIO role. AI handles data gathering, report generation, and pattern detection. The vCIO handles what matters most: strategic conversation, relationship management, and business-aligned recommendations that require human judgment and empathy."),
        ],
        "stat": "80–95%",
        "stat_desc": "reduction in QBR preparation time per client",
        "stat_cite": "Based on DevOps AI platform capabilities",
        "stat_url": "https://devops.ai.rain.tech/zones/vc-suite.html",
    },
    {
        "slug": "security-analyst",
        "title": "Security Analyst",
        "tagline": "AI-augmented threat operations",
        "description": "DevOps AI gives security analysts a unified SOC command center with AI-powered alert triage, automated containment, and integrated threat intelligence — eliminating context switches.",
        "pain_points": [
            "Switching between 8–12 tools per incident (EDR, SIEM, threat intel, PSA, email)",
            "94% noise rate in SIEM environments causing alert fatigue and missed threats",
            "Manual context assembly before any investigation can begin",
            "Vulnerability management in spreadsheets with manual CVSS prioritization",
            "Dark web monitoring in a separate portal disconnected from response workflows",
            "Post-incident reports assembled manually from memory and scattered notes",
        ],
        "transformed": [
            "Single SOC command center with all telemetry, enrichment, and actions unified",
            "AI auto-closes 70–90% of Tier-1 events — focus on real threats",
            "Context packages pre-built by AI before analysts touch a case",
            "Risk-based vulnerability scoring (CVSS × EPSS × KEV) with one-click remediation",
            "Dark web alerts integrated with PAM for automated credential rotation",
            "Post-incident reports auto-generated from the action log",
        ],
        "zones": [
            ("🛡️", "Security", "SOC Command Center, detection engineering, BCDR"),
            ("⚖️", "GRC", "Control failures link to security incidents"),
            ("💻", "Endpoints", "Endpoint isolation and patch compliance"),
            ("🎫", "Service Desk", "Security incidents create tracked tickets"),
        ],
        "faqs": [
            ("How does AI alert triage work without missing real threats?", "AI uses multi-signal classification based on MITRE ATT&CK TTPs, ML-based false positive scoring, and asset criticality context. Only pre-authorized Tier-1 actions execute autonomously. All Tier-2 and Tier-3 alerts require human review. The AI surfaces enriched context and recommendations, but never makes consequential security decisions alone."),
            ("What about pre-authorized autonomous containment?", "For pre-authorized TTPs (ransomware endpoint isolation, phishing email quarantine, known C2 IP blocking), containment executes autonomously — the analyst receives notification, not a request. This is configurable per client and per action type, with full audit trail."),
            ("Is there integration with existing security tools?", "DevOps AI integrates with SentinelOne, Huntress, Wazuh, and other EDR/SIEM platforms through its connector framework. It orchestrates across these tools rather than replacing them."),
        ],
        "stat": "86%",
        "stat_desc": "reduction in ticket escalations with AI-powered automation",
        "stat_cite": "Attainment Labs",
        "stat_url": "https://www.attainmentlabs.com/roi-analysis/it-msp-ai-automation",
    },
    {
        "slug": "service-desk-manager",
        "title": "Service Desk Manager",
        "tagline": "From reactive to predictive",
        "description": "DevOps AI transforms service desk management from reactive firefighting to predictive operations — with AI ticket routing, SLA risk prediction, and cross-client problem intelligence.",
        "pain_points": [
            "Morning queue reviews that take 30+ minutes of manual prioritization",
            "SLA breaches discovered after the fact rather than prevented",
            "No visibility into cross-client patterns when the same issue hits multiple tenants",
            "Knowledge stuck in senior engineers' heads, not in searchable systems",
            "CSAT surveys disconnected from ticket resolution workflows",
            "Co-managed environments with constant ownership disputes",
        ],
        "transformed": [
            "AI pre-sorts the queue by SLA risk before anyone arrives in the morning",
            "Predictive SLA management prevents breaches instead of reporting them",
            "Cross-client problem intelligence detects patterns across your entire portfolio",
            "Semantic KEDB surfaces relevant workarounds at the moment of investigation",
            "CSAT dispatched automatically with negative-response detection for follow-up",
            "RACI encoded as routing rules — ownership clear at ticket creation",
        ],
        "zones": [
            ("🎫", "Service Desk", "Live queue, SLA risk monitor, KEDB, co-managed"),
            ("📈", "Analytics", "Ticket volume forecasting for staffing decisions"),
            ("🎓", "Learning", "Knowledge base integration and article promotion"),
            ("💻", "Endpoints", "Alert-to-ticket automation from RMM"),
        ],
        "faqs": [
            ("How does predictive SLA management work?", "Every open ticket gets a real-time SLA risk score based on time elapsed, engineer workload, historical resolution time for similar tickets, and time of day. AI recommends queue adjustments before breaches occur and flags staffing shortfalls before the week begins."),
            ("What is cross-client problem intelligence?", "When the same error signature appears across 3+ clients, AI auto-creates a cross-client problem record. Known workarounds propagate to all technicians handling related tickets. The system proactively identifies additional environments at risk."),
            ("How does the KEDB work?", "The Known Error Database is semantically searchable. When a technician opens a ticket, AI automatically surfaces matching known errors and published workarounds. Resolved incidents can be promoted to KEDB entries and eventually to full knowledge base articles."),
        ],
        "stat": "30–40%",
        "stat_desc": "ticket reduction from AI-powered automation",
        "stat_cite": "Rev.io",
        "stat_url": "https://www.rev.io/blog/how-msps-can-reduce-tickets-by-30-40-through-automation",
    },
    {
        "slug": "compliance-officer",
        "title": "GRC Consultant / Compliance Officer",
        "tagline": "Continuous compliance, on autopilot",
        "description": "DevOps AI automates evidence collection, monitors compliance drift continuously, and maintains living documentation — so compliance officers can focus on strategy, not spreadsheets.",
        "pain_points": [
            "Collecting evidence separately for each framework despite 60–80% control overlap",
            "CMMC SSPs maintained manually in Word documents that are always out of date",
            "Compliance reviews happen at audit time, not continuously",
            "M365 configuration drift discovered at the next audit, not in real time",
            "Policy management across dozens of clients without version control",
            "No unified view of portfolio compliance posture",
        ],
        "transformed": [
            "Master control library: one control, one evidence collection, satisfies all frameworks",
            "AI-maintained living SSPs always current with automated evidence freshness tracking",
            "Continuous monitoring detects control drift in hours, not at audit time",
            "M365 baseline monitoring across all tenants with auto-remediation for low-risk drift",
            "Version-controlled policy library with approval workflows and attestation tracking",
            "Portfolio heatmap: all clients × all frameworks × readiness at a glance",
        ],
        "zones": [
            ("⚖️", "GRC", "Compliance programs, CMMC pipeline, continuous monitoring"),
            ("🛡️", "Security", "Control failure detection feeds compliance status"),
            ("🧭", "vC-Suite", "Compliance data feeds QBR content automatically"),
            ("⚙️", "DevOps", "M365 baseline configuration management"),
        ],
        "faqs": [
            ("How does 'collect once, satisfy many' work?", "DevOps AI's master control library tags each control to every applicable framework. When evidence is collected for a control — automatically from technical systems or through manual attestation — that evidence satisfies SOC 2, CMMC, NIST CSF, HIPAA, and ISO 27001 simultaneously. This reduces evidence collection effort by 50–70%."),
            ("What about CMMC Level 2 specifically?", "DevOps AI includes dedicated CMMC workflows: SPRS score gauges, AI-generated SSP drafts, POA&M trackers with 180-day close tracking, and evidence repositories organized by CMMC practice. Every workflow is designed for C3PAO audit readiness."),
            ("How real-time is continuous monitoring?", "M365 baseline monitoring checks 300+ resource types every 6 hours. Control drift detection runs continuously against technical controls. Evidence freshness is tracked with automatic alerts when evidence becomes stale."),
        ],
        "stat": "Only 1%",
        "stat_desc": "of defense contractors feel fully prepared for CMMC",
        "stat_cite": "CyberSheath",
        "stat_url": "https://cybersheath.com/resources/blog/state-of-the-dib-report-2025-only-1-of-contractors-are-ready-for-cmmc/",
    },
    {
        "slug": "project-manager",
        "title": "Project Manager",
        "tagline": "Deliver projects on time, every time",
        "description": "DevOps AI gives project managers AI-powered risk scoring, automated deal-to-delivery handoffs, a migration command center, and real-time portfolio visibility.",
        "pain_points": [
            "Spending 30–90 minutes manually creating projects when deals close",
            "Managing migrations across 5–7 concurrent tool windows",
            "Change risk assessment based on gut feeling, not data",
            "No portfolio-wide view of budget variance or resource utilization",
            "Status reports assembled manually from scattered data sources",
            "Runbooks that go stale between uses",
        ],
        "transformed": [
            "Deal close → project creation in under 5 minutes, fully automated",
            "Single migration dashboard with real-time status across all workloads",
            "Every RFC auto-scored for risk at submission with data-driven routing",
            "Portfolio dashboard with EVM metrics: CPI, SPI, EAC, and burn rate",
            "AI-generated status reports from aggregated project data",
            "Living runbooks that track usage, detect drift, and improve over time",
        ],
        "zones": [
            ("📋", "Projects", "Full project lifecycle, migrations, change management"),
            ("🎫", "Service Desk", "Project-related tickets tracked in context"),
            ("📊", "Accounting", "Project milestone billing integration"),
            ("🧭", "vC-Suite", "Project outcomes feed client roadmaps"),
        ],
        "faqs": [
            ("How does the automated deal-to-delivery handoff work?", "When a CRM deal closes, DevOps AI automatically creates the project using the right template based on deal type and service SKU. It pre-populates the charter from the SOW, runs capacity checks across all engineers, configures billing from contract terms, and delivers a complete context package to the PM."),
            ("What does the Migration Command Center include?", "A single dashboard aggregating real-time data from migration tools (BitTitan, ShareGate), PSA task status, and client communications. AI monitors health across all workloads, surfaces anomalies, validates item counts post-batch, and auto-updates client-facing status portals."),
            ("How does AI risk scoring work for change requests?", "Every RFC is auto-scored at submission using change type, affected CMDB systems, client profile (regulated?), historical outcomes, current freeze calendar, and concurrent pending changes. The risk score drives automatic routing to the appropriate approval level."),
        ],
        "stat": "30–90 min → 5 min",
        "stat_desc": "project creation time with automated deal-to-delivery handoff",
        "stat_cite": "DevOps AI platform capabilities",
        "stat_url": "https://devops.ai.rain.tech/zones/projects.html",
    },
    {
        "slug": "network-engineer",
        "title": "Network / Endpoint Engineer",
        "tagline": "Automate the routine, focus on the complex",
        "description": "DevOps AI gives network and endpoint engineers automated topology mapping, SLO-based monitoring, ring-based patching, and fleet-wide endpoint visibility.",
        "pain_points": [
            "Maintaining topology documentation that goes stale within weeks",
            "SSL certificate tracking in spreadsheets with missed renewals",
            "Patching without ring-based rollout or pre-patch verification",
            "No unified view of endpoint fleet health across all clients",
            "Shadow IT devices appearing on networks undetected",
            "Alert noise from RMM creating more work, not less",
        ],
        "transformed": [
            "Auto-generated live network topology updated with every scan",
            "SSL certificates auto-renewed via ACME with expiry calendar for all domains",
            "Ring-based patch deployment: pilot → standard → broad with verification",
            "Fleet dashboard with health, compliance, and MDM status for every endpoint",
            "Shadow IT registry flags unmanaged devices automatically",
            "AI-triaged alerts with auto-remediation for known patterns",
        ],
        "zones": [
            ("🌐", "Network Ops", "Topology, SLO monitoring, capacity forecasting"),
            ("💻", "Endpoints", "Fleet management, patching, Intune MDM"),
            ("🛡️", "Security", "Vulnerability correlation and endpoint isolation"),
            ("🎫", "Service Desk", "Alert-to-ticket automation"),
        ],
        "faqs": [
            ("How does SLO-based monitoring differ from threshold alerts?", "Traditional threshold alerts fire when a static limit is crossed. SLO-based monitoring defines service-level objectives per site and tracks compliance over time. Dynamic thresholds adjust as network patterns evolve, reducing false positives while catching genuine performance degradation."),
            ("What about multi-tenant Intune management?", "DevOps AI provides a single interface to manage compliance policies, configuration profiles, and Autopilot provisioning across all client tenants. The non-compliance queue shows devices failing policies across your entire fleet with grace periods and escalation workflows."),
            ("Does auto-remediation run without approval?", "For known, low-risk alert patterns (service restart, temp file cleanup, etc.), auto-remediation runs autonomously. High-risk actions like feature updates, driver updates on servers, or device retirement always require human approval."),
        ],
        "stat": "$847B",
        "stat_desc": "projected global managed services market by 2033 (9.9% CAGR)",
        "stat_cite": "Grand View Research",
        "stat_url": "https://www.grandviewresearch.com/industry-analysis/managed-services-market",
    },
    {
        "slug": "account-manager",
        "title": "Account Manager",
        "tagline": "From lead to QBR, one platform",
        "description": "DevOps AI unifies the account manager's world: pipeline, proposals, client health, billing context, and QBR preparation — all in a single platform.",
        "pain_points": [
            "Switching between CRM, PSA, billing, and security tools for client context",
            "No visibility into proposal engagement after sending",
            "QBR preparation requiring manual data gathering from multiple systems",
            "Client health based on gut feeling rather than composite scoring",
            "Renewal management tracked in spreadsheets with frequent misses",
            "Onboarding handoffs that drop context between sales and operations",
        ],
        "transformed": [
            "Single client record linking all zone data: tickets, projects, security, billing, compliance",
            "Proposal engagement tracking shows time per section and when prospects re-open documents",
            "QBR content auto-populated from operational data across every zone",
            "Client health score: security risk + ticket sentiment + SLA compliance + churn risk",
            "Renewal pipeline with automated 90/60/30-day alerts and kanban workflow",
            "Automated deal-to-delivery handoff ensures nothing falls through the cracks",
        ],
        "zones": [
            ("🚀", "Business Development", "Pipeline, CPQ, proposals, onboarding"),
            ("🧭", "vC-Suite", "Client health and QBR preparation"),
            ("📊", "Accounting", "Billing context and renewal management"),
            ("🎫", "Service Desk", "Ticket context for client conversations"),
        ],
        "faqs": [
            ("How does client health scoring work?", "The client health score is a composite metric calculated from security risk, ticket sentiment analysis, SLA compliance, license utilization, and predictive churn risk. Clients scoring below threshold are flagged for priority QBR scheduling and proactive intervention."),
            ("Can I see billing context during client conversations?", "Yes. The unified client record includes billing history, agreement status, MRR contribution, profitability metrics, and any open reconciliation exceptions. You have full context without switching to a separate billing tool."),
            ("How does the renewal pipeline work?", "Expiring contracts automatically create opportunities in the renewal pipeline. The kanban workflow tracks each renewal through stages: identify → propose → negotiate → close. Automated alerts at 90, 60, and 30 days ensure no renewal is missed."),
        ],
        "stat": "10%",
        "stat_desc": "average MRR recovery when billing reconciliation is automated",
        "stat_cite": "Based on Gradient MSP data",
        "stat_url": "https://devops.ai.rain.tech/zones/accounting.html",
    },
    {
        "slug": "finance-coordinator",
        "title": "Finance / Billing Coordinator",
        "tagline": "Revenue operations, simplified",
        "description": "DevOps AI automates the billing coordinator's most time-consuming tasks: three-way reconciliation, invoice generation, license management, and revenue tracking.",
        "pain_points": [
            "Spending 8–40 hours per month on manual billing reconciliation",
            "Correlating Microsoft Partner Center CSVs with distributor invoices and PSA agreements",
            "Revenue leakage from missed seat additions and mid-cycle changes",
            "Contract renewals tracked in spreadsheets with frequent oversights",
            "No real-time view of MRR, churn, or client profitability",
            "Month-end close consuming days of manual journal entry work",
        ],
        "transformed": [
            "Three-way reconciliation automated: vendor API + distributor + PSA → single approval screen",
            "85% faster reconciliation with automated delta reporting",
            "~10% MRR uplift from captured missed charges and license discrepancies",
            "Renewal calendar with automated alerts and procurement workflows",
            "Real-time MRR waterfall: new, expansion, contraction, and churn",
            "Auto-posted journal entries with configurable GL account mapping",
        ],
        "zones": [
            ("📊", "Accounting", "Reconciliation, invoicing, GL, procurement"),
            ("📈", "Analytics", "Revenue analytics and profitability reporting"),
            ("🚀", "Business Development", "CPQ quotes trigger contract creation"),
            ("🧭", "vC-Suite", "Margin data feeds client advisory"),
        ],
        "faqs": [
            ("How does three-way reconciliation work?", "DevOps AI simultaneously pulls usage data via API from Microsoft Partner Center, distributors (Pax8, TD Synnex), and your PSA agreements. It automatically matches line items, identifies discrepancies, and presents a single approval screen. You review exceptions, approve in batch, and invoices generate."),
            ("What about NCE license management?", "DevOps AI tracks NCE commitment windows, renewal dates, and mid-cycle seat changes. It alerts you before commitment periods close so you can right-size subscriptions. The license manager shows per-vendor, per-client usage vs. billed with a clear delta view."),
            ("Does it integrate with QuickBooks/Xero?", "Yes. DevOps AI syncs with QuickBooks and Xero for GL account mapping, auto-posted journal entries, and PSA AR to accounting AR reconciliation. The chart of accounts is optimized for MSP operations."),
        ],
        "stat": "85%",
        "stat_desc": "faster billing reconciliation with automation",
        "stat_cite": "DevOps AI platform capabilities",
        "stat_url": "https://devops.ai.rain.tech/zones/accounting.html",
    },
    {
        "slug": "it-director",
        "title": "IT Director (Client-Side)",
        "tagline": "Your MSP, supercharged",
        "description": "As an IT director working with an MSP powered by DevOps AI, you get unprecedented visibility into your managed services — real-time dashboards, compliance posture, and strategic roadmaps.",
        "pain_points": [
            "Limited visibility into what your MSP is actually doing day-to-day",
            "QBR reports that arrive quarterly with stale data and no real-time view",
            "Compliance posture only visible during annual audits",
            "No self-service ticket portal with intelligent deflection",
            "Technology roadmap decisions based on MSP recommendations without supporting data",
            "Incident response that feels opaque — you hear about breaches after the fact",
        ],
        "transformed": [
            "Client portal with real-time ticket status, compliance posture, and security health",
            "Living QBR workspace accessible anytime — not just during quarterly meetings",
            "Continuous compliance dashboard showing framework status and control health",
            "Self-service portal with AI-powered KB deflection and CSAT feedback",
            "Technology roadmap backed by operational data: asset lifecycle, capacity trends, risk scores",
            "Security incident transparency with real-time status and AI-enriched timelines",
        ],
        "zones": [
            ("🧭", "vC-Suite", "Client advisory workspace with your roadmap and health data"),
            ("🎫", "Service Desk", "Your ticket portal with self-service and CSAT"),
            ("⚖️", "GRC", "Your compliance posture and framework status"),
            ("🛡️", "Security", "Your security health dashboard and incident transparency"),
        ],
        "faqs": [
            ("What do I see as a client portal user?", "You see your own tickets, compliance posture, QBR history and roadmap, security health dashboard, and analytics specific to your environment. You don't see other clients' data or MSP-internal operations."),
            ("Can I track compliance in real time?", "Yes. The client portal includes your framework compliance status (SOC 2, CMMC, HIPAA, etc.), control health, and evidence freshness. You can see your compliance posture at any time, not just during audits."),
            ("How does the self-service portal reduce tickets?", "The portal uses AI-powered knowledge base deflection. When a user starts to submit a ticket, the system suggests relevant KB articles and known workarounds. If the user finds their answer, the ticket is deflected. This typically reduces ticket volume while improving user satisfaction."),
        ],
        "stat": "$401B",
        "stat_desc": "global managed services market in 2025, growing at 9.9% CAGR",
        "stat_cite": "Grand View Research",
        "stat_url": "https://www.grandviewresearch.com/industry-analysis/managed-services-market",
    },
]

def generate_role_page(r):
    bc = [("Home", "index.html"), ("For Your Role", None), (r["title"], None)]
    
    pain_html = ""
    for p in r["pain_points"]:
        pain_html += f"<li>{p}</li>\n"
    
    transform_html = ""
    for t in r["transformed"]:
        transform_html += f"<li>{t}</li>\n"
    
    zones_html = ""
    for icon, name, desc in r["zones"]:
        zones_html += f'''
        <div class="zone-highlight-card fade-up">
          <div class="zh-icon">{icon}</div>
          <h3>{name}</h3>
          <p>{desc}</p>
        </div>'''
    
    faq_html = ""
    faq_schema = ""
    if r["faqs"]:
        for q, a in r["faqs"]:
            faq_html += f'''
      <div class="faq-item">
        <button class="faq-question" aria-expanded="false">
          <span>{q}</span>
          <svg class="faq-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        </button>
        <div class="faq-answer"><div class="faq-answer-inner">{a}</div></div>
      </div>'''
        
        faq_entities = []
        for q, a in r["faqs"]:
            faq_entities.append(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}')
        faq_schema = ',{"@type":"FAQPage","mainEntity":[' + ",".join(faq_entities) + ']}'
    
    body = f'''
  <section class="role-hero">
    <div class="container">
      <div class="zone-accent-bar fade-up" style="background: var(--gradient-hero);"></div>
      <h1 class="fade-up">{r["title"]}</h1>
      <p class="role-tagline fade-up">{r["tagline"]}</p>
      <p class="role-desc fade-up">{r["description"][:200]}...</p>
    </div>
  </section>

  <section class="section" aria-label="Day comparison">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">The Transformation</span>
        <h2>Your Day, Transformed</h2>
      </div>
      <div class="day-comparison">
        <div class="day-card day-card--before fade-up">
          <h3>Your Day Today</h3>
          <ul>
            {pain_html}
          </ul>
        </div>
        <div class="day-card day-card--after fade-up">
          <h3>Your Day with DevOps AI</h3>
          <ul>
            {transform_html}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-label="Key zones" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Your Zones</span>
        <h2>The Zones That Matter Most to You</h2>
        <p>DevOps AI's 12-zone architecture means every role gets a purpose-built experience. Here are the zones you'll use most.</p>
      </div>
      <div class="zone-highlight-grid">
        {zones_html}
      </div>
    </div>
  </section>

  <section class="section" aria-label="Impact statistics">
    <div class="container">
      <div class="market-stats-grid">
        <div class="market-stat-card fade-up" style="grid-column: 1 / -1; text-align: center; padding: var(--space-10);">
          <div class="stat-figure" style="font-size: var(--text-4xl);">{r["stat"]}</div>
          <div class="stat-desc" style="font-size: var(--text-lg);">{r["stat_desc"]}</div>
          <div class="stat-cite">Source: <a href="{r["stat_url"]}" target="_blank" rel="noopener noreferrer">{r["stat_cite"]}</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" aria-label="FAQ" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">FAQ</span>
        <h2>Frequently Asked Questions</h2>
      </div>
      <div class="faq-section fade-up">
        {faq_html}
      </div>
    </div>
  </section>

  <section class="section" aria-label="CTA">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>Ready to Transform Your Workflow?</h2>
        <p>See DevOps AI in the Azure Marketplace — deploy in under 35 minutes with full data sovereignty.</p>
        <a href="../marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
      </div>
    </div>
  </section>
'''
    
    return page_shell(
        title=f'{r["title"]} — DevOps AI for Your Role | RainTech',
        description=r["description"],
        canonical=f'roles/{r["slug"]}.html',
        breadcrumbs=bc,
        active="roles",
        depth=1,
        body=body,
        extra_schema=faq_schema
    )


# ============================================================
# GENERATE ALL ZONE PAGES
# ============================================================
for z in ZONES:
    path = os.path.join(BASE, "zones", f'{z["slug"]}.html')
    with open(path, "w") as f:
        f.write(generate_zone_page(z))
    print(f"  ✓ zones/{z['slug']}.html")

# ============================================================
# GENERATE ALL ROLE PAGES
# ============================================================
for r in ROLES:
    path = os.path.join(BASE, "roles", f'{r["slug"]}.html')
    with open(path, "w") as f:
        f.write(generate_role_page(r))
    print(f"  ✓ roles/{r['slug']}.html")

print("\nAll zone and role pages generated successfully!")
