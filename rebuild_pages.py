#!/usr/bin/env python3
"""Rebuild platform.html (zone tile grid) + all 14 role pages (interactive zone card grid).
Also adds screenshot lightbox modal CSS/JS and wires screenshots to zone pages."""

import os
import re
import json

BASE = os.path.dirname(os.path.abspath(__file__))

# ─── Zone Data (copied from generate_platform.py) ────────────────────────────
ZONES = [
    {"num": 1, "slug": "service-desk", "name": "Service Desk", "icon": "🎫", "accent": "#2563EB",
     "tagline": "AI-augmented ticket management, SLA optimization, and predictive support operations",
     "pa_count": 8,
     "screenshots": ["service-desk-dashboard", "service-desk-ticket-board", "service-desk-sla-dashboard", "service-desk-ai-triage"],
     "roles": [("service-desk-manager", "🎫", "Service Desk Manager"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director")],
     "connected": [("projects", "📋", "Projects"), ("analytics", "📈", "Analytics"), ("learning", "🎓", "Learning")],
    },
    {"num": 2, "slug": "projects", "name": "Projects", "icon": "📋", "accent": "#4F46E5",
     "tagline": "Phase-gated project execution with AI risk scoring, migration workflows, and CAB automation",
     "pa_count": 8,
     "screenshots": ["projects-dashboard", "projects-gantt-chart", "projects-migration-dashboard", "hitl-cab-review"],
     "roles": [("project-manager", "📋", "Project Manager"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director")],
     "connected": [("service-desk", "🎫", "Service Desk"), ("network-ops", "🌐", "Network Ops"), ("endpoint-management", "💻", "Endpoints")],
    },
    {"num": 3, "slug": "security-operations", "name": "Security Operations", "icon": "🛡️", "accent": "#DC2626",
     "tagline": "Unified SOC command center with incident response, detection engineering, and ZK Vault",
     "pa_count": 8,
     "screenshots": ["security-operations-dashboard", "security-soc-dashboard", "security-detection-engineering", "security-edr-dashboard"],
     "roles": [("security-analyst", "🛡️", "Security Analyst"), ("vciso", "🔒", "vCISO"), ("compliance-officer", "⚖️", "Compliance Officer")],
     "connected": [("grc-compliance", "⚖️", "GRC & Compliance"), ("endpoint-management", "💻", "Endpoints"), ("network-ops", "🌐", "Network Ops")],
    },
    {"num": 4, "slug": "grc-compliance", "name": "GRC & Compliance", "icon": "⚖️", "accent": "#D97706",
     "tagline": "OSCAL-native evidence, CMMC SSP builder, gap analysis, and continuous compliance monitoring",
     "pa_count": 8,
     "screenshots": ["grc-compliance-dashboard", "grc-evidence-collection"],
     "roles": [("compliance-officer", "⚖️", "Compliance Officer"), ("vciso", "🔒", "vCISO"), ("vcco", "📋", "vCCO")],
     "connected": [("security-operations", "🛡️", "Security Ops"), ("legal", "⚖️", "Legal"), ("analytics", "📈", "Analytics")],
    },
    {"num": 5, "slug": "network-ops", "name": "Network Operations", "icon": "🌐", "accent": "#0891B2",
     "tagline": "SLO-based monitoring, live topology, capacity forecasting, and SSL lifecycle management",
     "pa_count": 7,
     "screenshots": ["network-ops-dashboard", "network-topology"],
     "roles": [("network-engineer", "🌐", "Network Engineer"), ("it-director", "🖥️", "IT Director"), ("msp-owner", "🏢", "MSP Owner / CEO")],
     "connected": [("endpoint-management", "💻", "Endpoints"), ("security-operations", "🛡️", "Security Ops"), ("service-desk", "🎫", "Service Desk")],
    },
    {"num": 6, "slug": "endpoint-management", "name": "Endpoint Management", "icon": "💻", "accent": "#16A34A",
     "tagline": "Intune management, automated patching, device lifecycle, and fleet intelligence",
     "pa_count": 8,
     "screenshots": ["endpoint-management-dashboard"],
     "roles": [("it-director", "🖥️", "IT Director"), ("network-engineer", "🌐", "Network Engineer"), ("security-analyst", "🛡️", "Security Analyst")],
     "connected": [("network-ops", "🌐", "Network Ops"), ("security-operations", "🛡️", "Security Ops"), ("service-desk", "🎫", "Service Desk")],
    },
    {"num": 7, "slug": "accounting", "name": "Accounting", "icon": "📊", "accent": "#059669",
     "tagline": "Automated invoice ingestion, three-way reconciliation, and revenue recognition",
     "pa_count": 8,
     "screenshots": ["accounting-dashboard", "accounting-reconciliation"],
     "roles": [("finance-coordinator", "💰", "Finance Coordinator"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("account-manager", "🤝", "Account Manager")],
     "connected": [("relationships", "🤝", "Relationships"), ("analytics", "📈", "Analytics"), ("vc-suite", "🧭", "vC-Suite")],
    },
    {"num": 8, "slug": "relationships", "name": "Relationships", "icon": "🤝", "accent": "#7C3AED",
     "tagline": "Sales pipeline, ICP scoring, marketing orchestration, and client health scoring",
     "pa_count": 8,
     "screenshots": [],
     "roles": [("account-manager", "🤝", "Account Manager"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("vcio", "🧭", "vCIO")],
     "connected": [("accounting", "📊", "Accounting"), ("analytics", "📈", "Analytics"), ("vc-suite", "🧭", "vC-Suite")],
    },
    {"num": 9, "slug": "vc-suite", "name": "vC-Suite", "icon": "🧭", "accent": "#475569",
     "tagline": "Executive advisory engines for vCIO, vCTO, vCISO, and vCCO functions",
     "pa_count": 8,
     "screenshots": ["vc-suite-dashboard", "vc-suite-advisory"],
     "roles": [("vcio", "🧭", "vCIO"), ("vciso", "🔒", "vCISO"), ("vcco", "📋", "vCCO"), ("msp-owner", "🏢", "MSP Owner / CEO")],
     "connected": [("analytics", "📈", "Analytics"), ("accounting", "📊", "Accounting"), ("grc-compliance", "⚖️", "GRC & Compliance")],
    },
    {"num": 10, "slug": "analytics", "name": "Analytics", "icon": "📈", "accent": "#EA580C",
     "tagline": "QBR aggregation, churn prediction, cross-domain correlation, and NL BI queries",
     "pa_count": 8,
     "screenshots": ["analytics-dashboard", "analytics-churn-prediction", "analytics-cross-domain"],
     "roles": [("msp-owner", "🏢", "MSP Owner / CEO"), ("vcio", "🧭", "vCIO"), ("it-director", "🖥️", "IT Director")],
     "connected": [("vc-suite", "🧭", "vC-Suite"), ("relationships", "🤝", "Relationships"), ("service-desk", "🎫", "Service Desk")],
    },
    {"num": 11, "slug": "devops", "name": "DevOps", "icon": "⚙️", "accent": "#6B7280",
     "tagline": "Feature flags, A/B testing, connector toolkit, and SRE golden signals",
     "pa_count": 8,
     "screenshots": ["devops-dashboard"],
     "roles": [("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director")],
     "connected": [("analytics", "📈", "Analytics"), ("service-desk", "🎫", "Service Desk"), ("learning", "🎓", "Learning")],
    },
    {"num": 12, "slug": "learning", "name": "Learning", "icon": "🎓", "accent": "#0D9488",
     "tagline": "LMS engine, AI tutoring, certification tracking, and skill gap analysis",
     "pa_count": 8,
     "screenshots": ["learning-dashboard"],
     "roles": [("hr-director", "👤", "HR Director"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("compliance-officer", "⚖️", "Compliance Officer")],
     "connected": [("people", "👥", "People"), ("grc-compliance", "⚖️", "GRC & Compliance"), ("service-desk", "🎫", "Service Desk")],
    },
    {"num": 13, "slug": "organization", "name": "Organization", "icon": "🏢", "accent": "#1F2937",
     "tagline": "Department hierarchy, multi-tenant admin, and white-label branding",
     "pa_count": 6,
     "screenshots": [],
     "roles": [("hr-director", "👤", "HR Director"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("compliance-officer", "⚖️", "Compliance Officer")],
     "connected": [("people", "👥", "People"), ("grc-compliance", "⚖️", "GRC & Compliance"), ("service-desk", "🎫", "Service Desk")],
    },
    {"num": 14, "slug": "people", "name": "People", "icon": "👥", "accent": "#B45309",
     "tagline": "Employee lifecycle, recruitment pipeline, performance management, and payroll integration",
     "pa_count": 8,
     "screenshots": [],
     "roles": [("hr-director", "👤", "HR Director"), ("recruiter", "📋", "Recruiter"), ("it-director", "🖥️", "IT Director")],
     "connected": [("organization", "🏢", "Organization"), ("learning", "🎓", "Learning"), ("security-operations", "🛡️", "Security Ops")],
    },
    {"num": 15, "slug": "legal", "name": "Legal", "icon": "⚖️", "accent": "#991B1B",
     "tagline": "Contract lifecycle, NDA management, regulatory tracking, and IP management",
     "pa_count": 6,
     "screenshots": [],
     "roles": [("compliance-officer", "⚖️", "Compliance Officer"), ("vcco", "📋", "vCCO"), ("msp-owner", "🏢", "MSP Owner / CEO")],
     "connected": [("grc-compliance", "⚖️", "GRC & Compliance"), ("people", "👥", "People"), ("organization", "🏢", "Organization")],
    },
]

ZONE_BY_SLUG = {z["slug"]: z for z in ZONES}

# HITL level helpers
HITL_LABELS = {"L0": "Fully Automated", "L1": "Notify", "L2": "Approve to Proceed", "L3": "Human Only"}

def hitl_pills(pa_count):
    """Generate small HITL summary pills for a zone tile."""
    return f'<span class="zt-pa-count">{pa_count} process areas</span>'


# ══════════════════════════════════════════════════════════════════════════════
# PLATFORM PAGE — Zone Tile Grid
# ══════════════════════════════════════════════════════════════════════════════

def build_platform_zone_grid():
    """Build the 15-zone tile grid matching homepage design."""
    tiles = []
    for z in ZONES:
        screenshot_attr = ""
        if z["screenshots"]:
            screenshot_attr = f' data-screenshot="assets/screenshots/{z["screenshots"][0]}.png"'
        tiles.append(f'''        <a href="zones/{z['slug']}.html" class="zone-card fade-up" style="--zone-accent: {z['accent']};"{screenshot_attr}>
          <div class="zone-icon" style="background: {z['accent']}15; color: {z['accent']}">
            <span class="zone-icon__emoji">{z['icon']}</span>
          </div>
          <span class="zone-number">{z['num']:02d}</span>
          <h3>{z['name']}</h3>
          <p>{z['tagline']}</p>
          <div class="zt-meta">
            {hitl_pills(z['pa_count'])}
          </div>
        </a>''')
    return '\n'.join(tiles)


def build_platform_html():
    """Rewrite the zone section of platform.html to use tile grid."""
    with open(os.path.join(BASE, 'platform.html'), 'r') as f:
        html = f.read()

    # Find the zones section and replace it
    # Section starts at: <section class="section" id="zones"
    # Section ends at: </section> before the AI Orchestration section
    zones_start = html.find('<section class="section" id="zones"')
    if zones_start == -1:
        print("ERROR: Could not find zones section")
        return

    # Find the closing </section> for the zones section
    # The next section after zones is AI Orchestration
    ai_orch_start = html.find('<!-- AI Orchestration', zones_start)
    if ai_orch_start == -1:
        ai_orch_start = html.find('<section class="section" style="background:var(--bg-secondary);" aria-label="AI Orchestration">', zones_start)
    if ai_orch_start == -1:
        # Try finding the section by label
        ai_orch_start = html.find('AI Orchestration Engine', zones_start)
        if ai_orch_start != -1:
            # Back up to find the section tag
            ai_orch_start = html.rfind('<section', zones_start, ai_orch_start)

    # Find the </section> just before AI Orchestration
    zones_end = html.rfind('</section>', zones_start, ai_orch_start)
    if zones_end == -1:
        print("ERROR: Could not find end of zones section")
        return
    zones_end += len('</section>')

    # Also find and remove the workflow gallery section
    wf_start = html.find('<section class="section" id="workflows"')
    wf_end = -1
    if wf_start != -1:
        # Find closing </section>
        depth = 0
        i = wf_start
        while i < len(html):
            if html[i:i+8] == '<section':
                depth += 1
            elif html[i:i+10] == '</section>':
                depth -= 1
                if depth == 0:
                    wf_end = i + 10
                    break
            i += 1

    # Build new zones section
    new_zones = f'''<section class="section" id="zones" aria-label="15-Zone Architecture">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Architecture</span>
        <h2>15 Operational Zones</h2>
        <p>Each zone is a fully featured control plane module with dedicated process areas, HITL governance gates, and cross-zone integrations. Select any zone to explore its complete journey.</p>
      </div>
      <div class="zone-grid">
{build_platform_zone_grid()}
      </div>
    </div>
  </section>'''

    # Replace zones section
    html = html[:zones_start] + new_zones + html[zones_end:]

    # Remove workflow gallery if found (recalculate positions after first replacement)
    if wf_start != -1:
        wf_start2 = html.find('<section class="section" id="workflows"')
        if wf_start2 != -1:
            depth = 0
            i = wf_start2
            while i < len(html):
                if html[i:i+8] == '<section':
                    depth += 1
                elif html[i:i+10] == '</section>':
                    depth -= 1
                    if depth == 0:
                        wf_end2 = i + 10
                        break
                i += 1
            # Remove the section + any surrounding whitespace
            html = html[:wf_start2].rstrip() + '\n\n  ' + html[wf_end2:].lstrip()

    with open(os.path.join(BASE, 'platform.html'), 'w') as f:
        f.write(html)
    print(f"  platform.html updated — zone tile grid with {len(ZONES)} zones")


# ══════════════════════════════════════════════════════════════════════════════
# ROLE PAGES — Interactive Zone Card Grid with Expandable
# ══════════════════════════════════════════════════════════════════════════════

# Role → zone data mapping (extracted from existing role pages)
ROLE_ZONES = {
    "vcio": {
        "zones": ["vc-suite", "analytics", "relationships", "projects", "security-operations", "grc-compliance"],
        "process_areas": {
            "vc-suite": [("vCIO Advisory Engine", "L2"), ("vCTO Architecture Reviews", "L2"), ("vCISO Security Program", "L2"), ("vCCO Compliance Governance", "L2")],
            "analytics": [("QBR Aggregation Engine", "L1"), ("Churn Prediction Model", "L1"), ("Ticket Volume Forecasting", "L0"), ("Security Risk Scoring", "L0")],
            "relationships": [("Lead Generation &amp; ICP Scoring", "L1"), ("Sales Pipeline Management", "L1"), ("Marketing Campaign Orchestration", "L2"), ("Client Onboarding Workflows", "L2")],
        }
    },
    "vciso": {
        "zones": ["security-operations", "grc-compliance", "vc-suite", "analytics", "endpoint-management", "network-ops"],
        "process_areas": {
            "security-operations": [("Incident Response Orchestration", "L2"), ("Detection Engineering", "L1"), ("EDR/XDR Integration", "L1"), ("Zero-Knowledge Vault (ZK Vault)", "L3")],
            "grc-compliance": [("Framework Lifecycle Management", "L2"), ("OSCAL-Native Evidence", "L0"), ("Gap Analysis Engine", "L0"), ("CMMC SSP Builder", "L2")],
            "vc-suite": [("vCISO Security Program", "L2"), ("vCTO Architecture Reviews", "L2"), ("Executive KPI Dashboards", "L0"), ("Technology Roadmap Management", "L2")],
        }
    },
    "vcco": {
        "zones": ["grc-compliance", "vc-suite", "legal", "analytics", "security-operations", "organization"],
        "process_areas": {
            "grc-compliance": [("Framework Lifecycle Management", "L2"), ("OSCAL-Native Evidence", "L0"), ("Gap Analysis Engine", "L0"), ("C3PAO Readiness Assessment", "L2")],
            "vc-suite": [("vCCO Compliance Governance", "L2"), ("Executive KPI Dashboards", "L0"), ("Strategic Recommendations", "L1")],
            "legal": [("Regulatory Change Tracking", "L1"), ("Contract Lifecycle Management", "L2"), ("Compliance Documentation", "L1")],
        }
    },
    "msp-owner": {
        "zones": ["vc-suite", "analytics", "relationships", "accounting", "service-desk", "projects", "organization"],
        "process_areas": {
            "vc-suite": [("vCIO Advisory Engine", "L2"), ("Executive KPI Dashboards", "L0"), ("Client Profitability Analysis", "L1"), ("Strategic Recommendations", "L1")],
            "analytics": [("QBR Aggregation Engine", "L0"), ("Churn Prediction Model", "L0"), ("Cross-Domain Correlation", "L1"), ("Benchmark Intelligence", "L1")],
            "relationships": [("Sales Pipeline Management", "L1"), ("Client Health Scoring", "L0"), ("Churn Risk Detection", "L0"), ("Referral &amp; Expansion Tracking", "L1")],
            "accounting": [("Three-Way Billing Reconciliation", "L1"), ("Revenue Recognition", "L1"), ("CPQ (Configure, Price, Quote)", "L1"), ("Subscription Management", "L1")],
        }
    },
    "it-director": {
        "zones": ["service-desk", "endpoint-management", "network-ops", "projects", "analytics", "devops"],
        "process_areas": {
            "service-desk": [("Ticket Ingestion &amp; AI Triage", "L0"), ("SLA Management &amp; Prediction", "L1"), ("Dispatch Optimization", "L1"), ("Playbook Automation", "L1")],
            "endpoint-management": [("Intune Management &amp; Compliance", "L1"), ("Automated Patching", "L1"), ("Fleet Intelligence", "L0"), ("Vulnerability Management", "L1")],
            "network-ops": [("SLO Management", "L1"), ("Topology Visualization", "L0"), ("Capacity Forecasting", "L1"), ("Performance Monitoring", "L0")],
        }
    },
    "service-desk-manager": {
        "zones": ["service-desk", "endpoint-management", "projects", "learning", "analytics"],
        "process_areas": {
            "service-desk": [("Ticket Ingestion &amp; AI Triage", "L0"), ("Known Error Database (KEDB)", "L0"), ("SLA Management &amp; Prediction", "L1"), ("Dispatch Optimization", "L1")],
            "endpoint-management": [("Infrastructure Monitoring", "L0"), ("Remote Access &amp; Support", "L0"), ("Fleet Intelligence", "L0")],
        }
    },
    "security-analyst": {
        "zones": ["security-operations", "endpoint-management", "network-ops", "grc-compliance", "analytics"],
        "process_areas": {
            "security-operations": [("Incident Response Orchestration", "L2"), ("Detection Engineering", "L1"), ("EDR/XDR Integration", "L1"), ("Dark Web Monitoring", "L0")],
            "endpoint-management": [("Vulnerability Management", "L1"), ("DNS Filtering", "L1"), ("Automated Patching", "L1")],
        }
    },
    "network-engineer": {
        "zones": ["network-ops", "endpoint-management", "security-operations", "projects", "service-desk"],
        "process_areas": {
            "network-ops": [("SLO Management", "L1"), ("Topology Visualization", "L0"), ("Capacity Forecasting", "L1"), ("Network Configuration Management", "L2")],
            "endpoint-management": [("Infrastructure Monitoring", "L0"), ("Automated Patching", "L1"), ("Device Lifecycle Management", "L2")],
        }
    },
    "project-manager": {
        "zones": ["projects", "service-desk", "network-ops", "endpoint-management", "analytics"],
        "process_areas": {
            "projects": [("CAB Submissions &amp; AI Risk Scoring", "L2"), ("Phase-Gated Execution", "L2"), ("Microsoft 365 Migration", "L2"), ("Hypercare &amp; Stabilization", "L1")],
            "service-desk": [("Ticket Ingestion &amp; AI Triage", "L0"), ("SLA Management &amp; Prediction", "L1")],
        }
    },
    "account-manager": {
        "zones": ["relationships", "accounting", "analytics", "vc-suite", "service-desk", "projects"],
        "process_areas": {
            "relationships": [("Lead Generation &amp; ICP Scoring", "L1"), ("Sales Pipeline Management", "L1"), ("QBR Preparation &amp; Delivery", "L1"), ("Client Health Scoring", "L0")],
            "accounting": [("Invoice Ingestion &amp; Processing", "L0"), ("CPQ (Configure, Price, Quote)", "L1"), ("Subscription Management", "L1")],
            "analytics": [("QBR Aggregation Engine", "L0"), ("Churn Prediction Model", "L0"), ("Benchmark Intelligence", "L1")],
        }
    },
    "finance-coordinator": {
        "zones": ["accounting", "analytics", "relationships", "vc-suite"],
        "process_areas": {
            "accounting": [("Invoice Ingestion &amp; Processing", "L0"), ("Three-Way Billing Reconciliation", "L1"), ("Revenue Recognition", "L1"), ("GL Integration", "L1")],
        }
    },
    "compliance-officer": {
        "zones": ["grc-compliance", "security-operations", "legal", "organization", "learning"],
        "process_areas": {
            "grc-compliance": [("Framework Lifecycle Management", "L2"), ("OSCAL-Native Evidence", "L0"), ("Gap Analysis Engine", "L0"), ("Audit Management", "L2")],
            "security-operations": [("BCDR Planning &amp; Testing", "L2"), ("Threat Intelligence Feeds", "L0")],
        }
    },
    "hr-director": {
        "zones": ["people", "organization", "learning", "accounting", "legal", "grc-compliance"],
        "process_areas": {
            "people": [("Employee Lifecycle Management", "L2"), ("Recruitment Pipeline", "L1"), ("Performance Management", "L2"), ("Payroll Integration", "L1")],
            "organization": [("Department Hierarchy Management", "L2"), ("Cost Center Management", "L2"), ("Organizational Policy Framework", "L2")],
            "learning": [("LMS Engine", "L1"), ("Compliance Training", "L1"), ("Onboarding Journeys", "L1")],
        }
    },
    "recruiter": {
        "zones": ["people", "organization", "learning", "relationships", "analytics"],
        "process_areas": {
            "people": [("Recruitment Pipeline", "L1"), ("Employee Lifecycle Management", "L2"), ("Performance Management", "L2")],
            "organization": [("Department Hierarchy Management", "L2")],
        }
    },
}


def build_role_zone_cards(role_slug, max_visible=3):
    """Build zone card grid for a role page with expandable functionality."""
    role_data = ROLE_ZONES.get(role_slug, {})
    zone_slugs = role_data.get("zones", [])
    role_pas = role_data.get("process_areas", {})

    cards = []
    for idx, zslug in enumerate(zone_slugs):
        z = ZONE_BY_SLUG.get(zslug)
        if not z:
            continue

        # Build process area links
        pas = role_pas.get(zslug, [])
        pa_html_items = []
        for pa_name, hitl in pas:
            level_class = hitl.lower()
            level_label = HITL_LABELS.get(hitl, hitl)
            pa_html_items.append(f'''                <li class="rzc-pa">
                  <span class="rzc-pa__name">{pa_name}</span>
                  <span class="hitl-badge hitl-badge--{level_class}" title="{level_label}">{hitl}</span>
                </li>''')

        pa_list = '\n'.join(pa_html_items) if pa_html_items else ''

        view_all_link = f'<a href="zones/{zslug}.html" class="rzc-view-all">View all {z["pa_count"]} process areas <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>' if z["pa_count"] > len(pas) else ''

        hidden_class = ' rzc--hidden' if idx >= max_visible else ''

        cards.append(f'''      <div class="role-zone-card fade-up{hidden_class}" style="--zone-accent: {z['accent']}">
            <a href="zones/{zslug}.html" class="rzc-header">
              <span class="rzc-icon">{z['icon']}</span>
              <span class="rzc-name">{z['name']}</span>
              <svg class="rzc-arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </a>
            <p class="rzc-tagline">{z['tagline']}</p>
            <ul class="rzc-pa-list">
{pa_list}
            </ul>
            {view_all_link}
          </div>''')

    # Build expand button if needed
    expand_btn = ''
    if len(zone_slugs) > max_visible:
        hidden_count = len(zone_slugs) - max_visible
        expand_btn = f'''
      <div class="rzc-expand-wrap fade-up">
        <button class="rzc-expand-btn" data-expanded="false" onclick="this.dataset.expanded = this.dataset.expanded === 'false' ? 'true' : 'false'; this.closest('.role-zone-grid').classList.toggle('is-expanded'); this.querySelector('.rzc-expand-label').textContent = this.dataset.expanded === 'true' ? 'Show fewer zones' : 'Show {hidden_count} more zone' + ({hidden_count} > 1 ? 's' : '');">
          <span class="rzc-expand-label">Show {hidden_count} more zone{"s" if hidden_count > 1 else ""}</span>
          <svg class="rzc-expand-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
        </button>
      </div>'''

    return '\n'.join(cards) + expand_btn


def update_role_page(role_slug):
    """Update a single role page with the new zone card grid."""
    filepath = os.path.join(BASE, 'roles', f'{role_slug}.html')
    if not os.path.exists(filepath):
        print(f"  WARNING: {filepath} not found, skipping")
        return False

    with open(filepath, 'r') as f:
        html = f.read()

    # Find the "Primary Operational Zones" section
    zones_section_start = html.find('aria-label="Primary zones"')
    if zones_section_start == -1:
        print(f"  WARNING: No 'Primary zones' section found in {role_slug}.html")
        return False

    # Back up to the <section tag
    section_start = html.rfind('<section', 0, zones_section_start)
    if section_start == -1:
        print(f"  WARNING: Could not find <section> tag for Primary zones in {role_slug}.html")
        return False

    # Find the closing </section>
    depth = 0
    i = section_start
    section_end = -1
    while i < len(html):
        if html[i:i+8] == '<section':
            depth += 1
        elif html[i:i+10] == '</section>':
            depth -= 1
            if depth == 0:
                section_end = i + 10
                break
        i += 1

    if section_end == -1:
        print(f"  WARNING: Could not find closing </section> for Primary zones in {role_slug}.html")
        return False

    role_data = ROLE_ZONES.get(role_slug, {})
    zone_slugs = role_data.get("zones", [])
    total_zones = len(zone_slugs)

    # Adjust href prefix — role pages are in roles/ subdir so need ../zones/
    cards_html = build_role_zone_cards(role_slug, max_visible=3)
    # Fix zone links to use relative paths from roles/ directory
    cards_html = cards_html.replace('href="zones/', 'href="../zones/')

    new_section = f'''<section class="section" aria-label="Primary zones" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Your Zones</span>
        <h2>Primary Operational Zones</h2>
        <p>These are the zones where you spend most of your time. Each process area links to its full deep-dive.</p>
      </div>
      <div class="role-zone-grid">
{cards_html}
      </div>
    </div>
  </section>'''

    html = html[:section_start] + new_section + html[section_end:]

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"  {role_slug}.html updated — {total_zones} zone cards ({min(3, total_zones)} visible, {'expandable' if total_zones > 3 else 'all shown'})")
    return True


# ══════════════════════════════════════════════════════════════════════════════
# CSS — New components
# ══════════════════════════════════════════════════════════════════════════════

NEW_CSS = '''
/* ===================================================
   PLATFORM PAGE — Zone Tile Enhancements
   =================================================== */

.zone-card .zt-meta {
  margin-top: var(--space-4);
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.zt-pa-count {
  font-size: 11px;
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-tertiary);
  background: var(--bg-secondary);
  padding: 3px 8px;
  border-radius: var(--radius-sm);
}

.zone-icon__emoji {
  font-size: 22px;
  line-height: 1;
}

/* ===================================================
   ROLE PAGES — Zone Card Grid with Expandable
   =================================================== */

.role-zone-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(400px, 100%), 1fr));
  gap: var(--space-5);
}

.role-zone-card {
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: var(--space-5);
  transition: all var(--duration-normal) var(--ease-out);
  position: relative;
  overflow: hidden;
}

.role-zone-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: var(--zone-accent, var(--accent));
  opacity: 0.6;
  transition: opacity var(--duration-normal);
}

.role-zone-card:hover {
  border-color: var(--border-strong);
  box-shadow: var(--shadow-md);
}

.role-zone-card:hover::before {
  opacity: 1;
}

/* Hidden cards (expandable) */
.role-zone-card.rzc--hidden {
  display: none;
}
.role-zone-grid.is-expanded .role-zone-card.rzc--hidden {
  display: block;
}

/* Card header */
.rzc-header {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  text-decoration: none;
  color: var(--zone-accent, var(--text-primary));
  margin-bottom: var(--space-2);
  transition: color var(--duration-fast);
}

.rzc-header:hover {
  color: var(--zone-accent, var(--accent));
}

.rzc-header:hover .rzc-arrow {
  transform: translateX(3px);
}

.rzc-icon {
  font-size: 24px;
  line-height: 1;
}

.rzc-name {
  font-size: var(--text-lg);
  font-weight: var(--font-weight-bold);
  flex: 1;
}

.rzc-arrow {
  opacity: 0.5;
  transition: all var(--duration-fast);
}

.rzc-tagline {
  font-size: var(--text-sm);
  color: var(--text-secondary);
  margin-bottom: var(--space-4);
  line-height: 1.5;
}

/* Process area list */
.rzc-pa-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1px;
}

.rzc-pa {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  transition: background var(--duration-fast);
}

.rzc-pa:hover {
  background: var(--bg-secondary);
}

.rzc-pa__name {
  font-size: var(--text-sm);
  color: var(--text-primary);
  font-weight: var(--font-weight-medium);
}

/* View all link */
.rzc-view-all {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  color: var(--zone-accent, var(--accent));
  text-decoration: none;
  margin-top: var(--space-3);
  padding: var(--space-2) 0;
  transition: opacity var(--duration-fast);
}

.rzc-view-all:hover {
  opacity: 0.8;
}

.rzc-view-all svg {
  transition: transform var(--duration-fast);
}

.rzc-view-all:hover svg {
  transform: translateX(3px);
}

/* Expand button */
.rzc-expand-wrap {
  grid-column: 1 / -1;
  display: flex;
  justify-content: center;
  padding-top: var(--space-2);
}

.role-zone-grid.is-expanded .rzc-expand-wrap {
  padding-top: var(--space-4);
}

.rzc-expand-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  background: var(--bg-card);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-full);
  padding: var(--space-2) var(--space-5);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all var(--duration-normal) var(--ease-out);
  font-family: inherit;
}

.rzc-expand-btn:hover {
  background: var(--bg-card-hover);
  border-color: var(--border-strong);
  color: var(--text-primary);
}

.rzc-expand-chevron {
  transition: transform var(--duration-normal) var(--ease-out);
}

.role-zone-grid.is-expanded .rzc-expand-chevron {
  transform: rotate(180deg);
}

/* Responsive */
@media (max-width: 768px) {
  .role-zone-grid {
    grid-template-columns: 1fr;
  }

  .rzc-pa {
    padding: var(--space-2);
  }

  .rzc-pa__name {
    font-size: 13px;
  }
}
'''


def update_css():
    """Replace old zone-entry and wf-gallery CSS with new components."""
    filepath = os.path.join(BASE, 'style.css')
    with open(filepath, 'r') as f:
        css = f.read()

    # Remove old zone-entry CSS block if it exists
    old_block_start = css.find('/* ===================================================\n   PLATFORM PAGE — Zone Journey Entry Points')
    if old_block_start != -1:
        # Find the end — next major section comment or end of file
        next_section = css.find('\n/* ===', old_block_start + 10)
        if next_section == -1:
            # Remove to end
            css = css[:old_block_start].rstrip()
        else:
            css = css[:old_block_start].rstrip() + '\n\n' + css[next_section:]
        print("  Removed old PLATFORM PAGE zone entry CSS")

    # Remove old workflow gallery CSS if it exists
    old_wf_start = css.find('/* ===================================================\n   PLATFORM PAGE — Workflow Gallery')
    if old_wf_start != -1:
        next_section = css.find('\n/* ===', old_wf_start + 10)
        if next_section == -1:
            css = css[:old_wf_start].rstrip()
        else:
            css = css[:old_wf_start].rstrip() + '\n\n' + css[next_section:]
        print("  Removed old Workflow Gallery CSS")

    # Remove old responsive overrides for zone-entry
    old_resp_start = css.find('/* ===================================================\n   PLATFORM PAGE — Responsive Overrides')
    if old_resp_start != -1:
        next_section = css.find('\n/* ===', old_resp_start + 10)
        if next_section == -1:
            css = css[:old_resp_start].rstrip()
        else:
            css = css[:old_resp_start].rstrip() + '\n\n' + css[next_section:]
        print("  Removed old Responsive Overrides CSS")

    # Check if new CSS already exists
    if '.role-zone-grid' in css:
        print("  New role-zone-grid CSS already exists, skipping append")
    else:
        css = css.rstrip() + '\n' + NEW_CSS
        print("  Appended new CSS components")

    with open(filepath, 'w') as f:
        f.write(css)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("═" * 60)
    print("Rebuilding Platform + Role Pages")
    print("═" * 60)

    print("\n[1] Updating CSS...")
    update_css()

    print("\n[2] Rebuilding platform.html zone tile grid...")
    build_platform_html()

    print("\n[3] Updating role pages...")
    roles = sorted(ROLE_ZONES.keys())
    for role in roles:
        update_role_page(role)

    print("\n" + "═" * 60)
    print("Done. All pages updated.")
    print("═" * 60)
