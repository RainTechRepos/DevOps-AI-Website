#!/usr/bin/env python3
"""
Embed screenshots into zone pages and high-value PA pages.
- Zone pages: dashboard hero + 2-3 workflow screenshots
- PA pages: 1-2 contextual screenshots near relevant content sections
"""
import os, re
from pathlib import Path

SITE = Path("/home/user/workspace/devops-ai-website")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SCREENSHOT MAPPING — zone → { dashboard, workflow screenshots }
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ZONE_SCREENSHOTS = {
    "service-desk": {
        "dashboard": ("service-desk-dashboard.png", "Service Desk — Zone Dashboard with active ticket metrics and SLA status"),
        "workflows": [
            ("service-desk-ticket-board.png", "AI-triaged ticket board showing priority lanes, assignee routing, and resolution timers"),
            ("service-desk-sla-dashboard.png", "Real-time SLA tracking dashboard with breach prediction indicators"),
            ("service-desk-ai-triage.png", "AI Triage engine — automated classification, sentiment scoring, and routing recommendations"),
        ],
    },
    "security-operations": {
        "dashboard": ("security-operations-dashboard.png", "Security Operations — SOC Command Center with threat landscape overview"),
        "workflows": [
            ("security-soc-dashboard.png", "SOC analyst view — active alerts, MITRE ATT&CK mapping, and investigation queue"),
            ("security-detection-engineering.png", "Detection Engineering workspace — rule authoring, test coverage, and deployment pipeline"),
            ("security-edr-dashboard.png", "EDR/XDR integration dashboard — endpoint health, quarantine actions, and forensic timeline"),
        ],
    },
    "grc-compliance": {
        "dashboard": None,  # No old dashboard for GRC
        "workflows": [
            ("grc-compliance-dashboard.png", "GRC compliance posture — framework coverage, control status, and audit readiness score"),
            ("grc-evidence-collection.png", "Automated evidence collection — OSCAL-native artifacts mapped to CMMC/SOC 2 controls"),
        ],
    },
    "projects": {
        "dashboard": ("projects-dashboard.png", "Projects — Zone Dashboard with active migrations and phase-gate status"),
        "workflows": [
            ("projects-migration-dashboard.png", "Microsoft 365 migration tracker — tenant progress, mailbox status, and cutover readiness"),
            ("projects-gantt-chart.png", "Phase-gated project timeline with critical path analysis and resource allocation"),
        ],
    },
    "analytics": {
        "dashboard": ("analytics-dashboard.png", "Analytics — Zone Dashboard with cross-domain intelligence feeds"),
        "workflows": [
            ("analytics-churn-prediction.png", "Churn prediction model — client risk scores, leading indicators, and intervention recommendations"),
            ("analytics-cross-domain.png", "Cross-domain correlation engine — linking ticket patterns, endpoint health, and security events"),
        ],
    },
    "network-ops": {
        "dashboard": ("network-ops-dashboard.png", "Network Ops — Zone Dashboard with topology overview and performance metrics"),
        "workflows": [
            ("network-topology.png", "Network topology visualization — live device mapping, link status, and performance overlays"),
        ],
    },
    "endpoint-management": {
        "dashboard": ("endpoint-management-dashboard.png", "Endpoint Management — Zone Dashboard with fleet health and compliance scores"),
        "workflows": [],
    },
    "accounting": {
        "dashboard": ("accounting-dashboard.png", "Accounting — Zone Dashboard with revenue recognition and billing pipeline"),
        "workflows": [
            ("accounting-reconciliation.png", "Three-way billing reconciliation — invoice vs. contract vs. usage with AI variance detection"),
        ],
    },
    "vc-suite": {
        "dashboard": ("vc-suite-dashboard.png", "vC-Suite — Executive Advisory Dashboard with KPI scorecards"),
        "workflows": [
            ("vc-suite-advisory.png", "vCIO strategic advisory view — technology roadmap, budget forecasting, and board-ready reports"),
        ],
    },
    "devops": {
        "dashboard": ("devops-dashboard.png", "DevOps — Zone Dashboard with CI/CD pipeline status and SRE golden signals"),
        "workflows": [],
    },
    "learning": {
        "dashboard": ("learning-dashboard.png", "Learning — Zone Dashboard with certification tracking and skill gap analysis"),
        "workflows": [],
    },
    # Zones without screenshots — inject HITL screenshots as generic platform features
    "relationships": {
        "dashboard": None,
        "workflows": [],
    },
    "legal": {
        "dashboard": None,
        "workflows": [],
    },
    "organization": {
        "dashboard": None,
        "workflows": [],
    },
    "people": {
        "dashboard": None,
        "workflows": [],
    },
}

# PA-level screenshot mapping — PA file → [(screenshot, caption)]
PA_SCREENSHOTS = {
    # Service Desk PAs
    "service-desk/process-areas/ticket-ingestion-ai-triage.html": [
        ("service-desk-ai-triage.png", "AI Triage engine — automated ticket classification, sentiment analysis, and smart routing"),
        ("service-desk-ticket-board.png", "Triaged ticket board — tickets flow from ingestion to prioritized queues automatically"),
    ],
    "service-desk/process-areas/sla-management-prediction.html": [
        ("service-desk-sla-dashboard.png", "Predictive SLA dashboard — breach probability, escalation triggers, and resolution forecasts"),
    ],
    "service-desk/process-areas/dispatch-optimization.html": [
        ("service-desk-ticket-board.png", "Optimized dispatch view — technician assignment based on skills, workload, and client proximity"),
    ],
    "service-desk/process-areas/playbook-automation.html": [
        ("hitl-approval-pending.png", "HITL approval gate — automated playbook paused for human review before executing privileged actions"),
    ],
    "service-desk/process-areas/co-managed-it-workflows.html": [
        ("hitl-approval-pending.png", "Co-managed approval workflow — MSP and client IT staff collaborate through HITL gates"),
    ],
    # Security Ops PAs
    "security-operations/process-areas/detection-engineering.html": [
        ("security-detection-engineering.png", "Detection rule workspace — authoring, testing, and deploying custom detection logic"),
    ],
    "security-operations/process-areas/edr-xdr-integration.html": [
        ("security-edr-dashboard.png", "EDR/XDR unified view — endpoint telemetry, threat containment, and investigation timeline"),
    ],
    "security-operations/process-areas/incident-response-orchestration.html": [
        ("hitl-incident-response.png", "Incident response HITL gate — AI proposes containment actions, analyst approves execution"),
        ("security-soc-dashboard.png", "SOC command center during active incident — correlated alerts, responder assignment, and status tracking"),
    ],
    "security-operations/process-areas/threat-intelligence-feeds.html": [
        ("security-soc-dashboard.png", "Threat intelligence integrated into SOC dashboard — enriched IOCs and MITRE ATT&CK mapping"),
    ],
    # GRC PAs
    "grc-compliance/process-areas/oscal-native-evidence.html": [
        ("grc-evidence-collection.png", "OSCAL-native evidence collection — automated artifact gathering mapped to compliance controls"),
    ],
    "grc-compliance/process-areas/continuous-monitoring.html": [
        ("grc-compliance-dashboard.png", "Continuous compliance monitoring — real-time posture, control drift alerts, and remediation tracking"),
    ],
    "grc-compliance/process-areas/cmmc-ssp-builder.html": [
        ("grc-compliance-dashboard.png", "CMMC SSP builder integrated view — control mapping, evidence status, and assessment readiness"),
    ],
    "grc-compliance/process-areas/framework-lifecycle-management.html": [
        ("grc-evidence-collection.png", "Framework lifecycle — evidence mapping across multiple compliance frameworks simultaneously"),
    ],
    # Projects PAs
    "projects/process-areas/microsoft-365-migration.html": [
        ("projects-migration-dashboard.png", "M365 migration dashboard — tenant-by-tenant progress, mailbox counts, and cutover scheduling"),
    ],
    "projects/process-areas/phase-gated-execution.html": [
        ("projects-gantt-chart.png", "Phase-gated Gantt chart — milestones, dependencies, and gate approvals mapped to project timeline"),
    ],
    "projects/process-areas/cab-submissions-ai-risk-scoring.html": [
        ("hitl-cab-review.png", "CAB review gate — AI risk score, change details, and approval workflow for advisory board members"),
    ],
    "projects/process-areas/discovery-assessment.html": [
        ("projects-migration-dashboard.png", "Discovery assessment output — environment inventory feeding into migration planning"),
    ],
    # Analytics PAs
    "analytics/process-areas/churn-prediction-model.html": [
        ("analytics-churn-prediction.png", "Churn prediction model — ML-scored client risk with contributing factor breakdown"),
    ],
    "analytics/process-areas/cross-domain-correlation.html": [
        ("analytics-cross-domain.png", "Cross-domain correlation — linking patterns across tickets, endpoints, security, and network data"),
    ],
    # Network Ops PAs
    "network-ops/process-areas/topology-visualization.html": [
        ("network-topology.png", "Live network topology — device interconnections, health status, and performance overlays"),
    ],
    "network-ops/process-areas/performance-monitoring.html": [
        ("network-topology.png", "Network performance monitoring — topology view with real-time bandwidth and latency overlays"),
    ],
    # Accounting PAs
    "accounting/process-areas/three-way-billing-reconciliation.html": [
        ("accounting-reconciliation.png", "Three-way reconciliation — invoice vs. contract vs. usage aligned with AI variance flagging"),
    ],
    "accounting/process-areas/invoice-ingestion-processing.html": [
        ("accounting-reconciliation.png", "Invoice processing pipeline — AI-extracted line items ready for reconciliation and GL posting"),
    ],
    # VC-Suite PAs
    "vc-suite/process-areas/vcio-advisory-engine.html": [
        ("vc-suite-advisory.png", "vCIO advisory workspace — technology roadmap, budget modeling, and strategic recommendations"),
    ],
    "vc-suite/process-areas/executive-kpi-dashboards.html": [
        ("vc-suite-advisory.png", "Executive KPI view — board-ready metrics with trend analysis and benchmark comparisons"),
    ],
    "vc-suite/process-areas/strategic-recommendations.html": [
        ("vc-suite-advisory.png", "Strategic recommendation engine — AI-generated insights with supporting data and action plans"),
    ],
}

# HITL screenshots to inject into zones that mention HITL heavily but have no zone-specific screenshots
HITL_SCREENSHOTS = [
    ("hitl-approval-pending.png", "Human-in-the-Loop approval gate — AI proposes action, human reviews and approves before execution"),
    ("hitl-cab-review.png", "Change Advisory Board review — AI risk assessment with structured approval workflow"),
    ("hitl-incident-response.png", "Incident response escalation — AI containment plan awaiting analyst authorization"),
]


def make_screenshot_html(img_path, caption, css_class="screenshot-showcase"):
    """Generate a figure element for a screenshot."""
    return f'''
          <figure class="{css_class} fade-up">
            <img src="{img_path}" alt="{caption}" loading="lazy" width="1600" height="900">
            <figcaption>{caption}</figcaption>
          </figure>'''


def make_pair_html(screenshots, asset_prefix):
    """Generate a two-up screenshot pair."""
    if len(screenshots) < 2:
        return "\n".join(make_screenshot_html(f"{asset_prefix}{s[0]}", s[1]) for s in screenshots)
    html = '\n          <div class="screenshot-pair fade-up">'
    for img, cap in screenshots[:2]:
        html += f'''
            <figure class="screenshot-showcase">
              <img src="{asset_prefix}{img}" alt="{cap}" loading="lazy" width="1600" height="900">
              <figcaption>{cap}</figcaption>
            </figure>'''
    html += '\n          </div>'
    # If there's a third, add it as a standalone
    if len(screenshots) > 2:
        html += make_screenshot_html(f"{asset_prefix}{screenshots[2][0]}", screenshots[2][1])
    return html


def inject_zone_screenshots(filepath, zone_key):
    """Inject screenshots into a zone page after the description section and before process areas."""
    data = ZONE_SCREENSHOTS.get(zone_key, {})
    if not data or (not data.get("dashboard") and not data.get("workflows")):
        # For zones with no screenshots, inject a HITL screenshot in the HITL legend section
        return inject_hitl_into_zone(filepath)

    html = filepath.read_text()

    # Asset path from zone page to assets/screenshots/
    asset_prefix = "../assets/screenshots/"

    # Build the screenshot section
    section_html = '''

  <!-- Platform Screenshots -->
  <section class="section" aria-label="Platform screenshots">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Inside the Platform</span>
        <h2>What You'll See</h2>
        <p>Real screens from the DevOps AI control plane — populated with representative data.</p>
      </div>'''

    # Dashboard hero
    if data.get("dashboard"):
        img, cap = data["dashboard"]
        section_html += f'''
      <div class="zone-screenshot-hero fade-up">
        <img src="{asset_prefix}{img}" alt="{cap}" loading="lazy" width="1600" height="900">
      </div>'''

    # Workflow screenshots
    if data.get("workflows"):
        section_html += make_pair_html(data["workflows"], asset_prefix)

    section_html += '''
    </div>
  </section>'''

    # Insert AFTER the "About" description section and BEFORE the Process Areas section
    # Find the closing of the description section
    pattern = r'(<!-- Zone Description -->.*?</section>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        insert_pos = match.end()
        html = html[:insert_pos] + section_html + html[insert_pos:]
    else:
        # Fallback: insert before Process Areas
        pa_marker = '<!-- Process Areas -->'
        if pa_marker in html:
            html = html.replace(pa_marker, section_html + '\n\n  ' + pa_marker)

    filepath.write_text(html)
    return True


def inject_hitl_into_zone(filepath):
    """For zones without dedicated screenshots, inject a HITL screenshot near the HITL legend."""
    html = filepath.read_text()
    asset_prefix = "../assets/screenshots/"

    # Only inject if there's a HITL legend section
    hitl_marker = '<!-- HITL Legend -->'
    if hitl_marker not in html:
        return False

    # Pick one HITL screenshot
    img, cap = HITL_SCREENSHOTS[0]
    screenshot_html = f'''
      {make_screenshot_html(f"{asset_prefix}{img}", cap)}'''

    # Insert right after the HITL legend h3 intro paragraph
    # Find the hitl-legend div and add after the opening description
    pattern = r'(<div class="hitl-legend fade-up">\s*<h3>Understanding HITL Gate Levels</h3>\s*<p>.*?</p>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        insert_pos = match.end()
        html = html[:insert_pos] + screenshot_html + html[insert_pos:]
        filepath.write_text(html)
        return True
    return False


def inject_pa_screenshots(filepath, pa_key):
    """Inject screenshots into a PA page after the 'How it works' section."""
    screenshots = PA_SCREENSHOTS.get(pa_key, [])
    if not screenshots:
        return False

    html = filepath.read_text()
    asset_prefix = "../../../assets/screenshots/"

    # Build screenshot HTML
    screenshot_html = ""
    for img, cap in screenshots:
        screenshot_html += make_screenshot_html(f"{asset_prefix}{img}", cap)

    # Insert after "How it works" section header + first paragraph
    # Target: after the "Workflow Architecture" h3 or after the first section of "How it works"
    pattern = r'(<section class="section" aria-label="How it works".*?<h2>.*?</h2>\s*</div>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        # Insert after the section header, before the body text
        insert_pos = match.end()
        html = html[:insert_pos] + screenshot_html + html[insert_pos:]
    else:
        # Fallback: after the Overview section
        pattern2 = r'(<section class="section" aria-label="Overview">.*?</section>)'
        match2 = re.search(pattern2, html, re.DOTALL)
        if match2:
            insert_pos = match2.end()
            html = html[:insert_pos] + '\n' + screenshot_html + html[insert_pos:]
        else:
            return False

    filepath.write_text(html)
    return True


def main():
    zones_dir = SITE / "zones"
    
    # 1. Inject into zone pages
    zone_count = 0
    for zone_html in sorted(zones_dir.glob("*.html")):
        zone_key = zone_html.stem
        if inject_zone_screenshots(zone_html, zone_key):
            zone_count += 1
            print(f"  ✓ Zone: {zone_key}")
        else:
            print(f"  - Zone: {zone_key} (no screenshots available)")

    # 2. Inject into PA pages
    pa_count = 0
    for pa_key, screenshots in PA_SCREENSHOTS.items():
        pa_path = zones_dir / pa_key
        if pa_path.exists():
            if inject_pa_screenshots(pa_path, pa_key):
                pa_count += 1
                print(f"  ✓ PA: {pa_key}")
            else:
                print(f"  ✗ PA: {pa_key} (injection point not found)")
        else:
            print(f"  ✗ PA: {pa_key} (file not found)")

    print(f"\nDone: {zone_count} zone pages, {pa_count} PA pages updated with screenshots.")


if __name__ == "__main__":
    main()
