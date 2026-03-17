#!/usr/bin/env python3
"""
Embed screenshots into the 87 PA deep-dive pages that don't have them yet.
Inserts a screenshot-showcase figure after the "X in Practice" heading.
"""
import re, json
from pathlib import Path

BASE = Path(__file__).parent

# Build mapping: PA page filename slug → screenshot ID
# Load all screenshots available
screenshots = {f.stem for f in (BASE / 'assets' / 'screenshots').glob('*.png')}

# Load manifest for PA name → screenshot mapping
manifest = json.load(open(BASE.parent / 'screenshot-renderer' / 'pa-screenshot-manifest.json'))
pa_name_to_screenshot = {item['pa']: item['id'] for item in manifest}

# Add fallbacks
FALLBACK = {
    "CAB Submissions & AI Risk Scoring": "hitl-cab-review",
    "Churn Prediction Model": "analytics-churn-prediction",
    "Detection Engineering": "security-detection-engineering",
    "EDR/XDR Integration": "security-edr-dashboard",
    "Framework Lifecycle Management": "framework-lifecycle",
    "Incident Response Orchestration": "hitl-incident-response",
    "Invoice Ingestion & Processing": "invoice-ingestion",
    "Microsoft 365 Migration": "m365-migration",
    "OSCAL-Native Evidence": "oscal-evidence",
    "Phase-Gated Execution": "phase-gated-execution",
    "SLA Management & Prediction": "service-desk-sla-dashboard",
    "Three-Way Billing Reconciliation": "accounting-reconciliation",
    "Ticket Ingestion & AI Triage": "service-desk-ai-triage",
    "Topology Visualization": "network-topology",
    "Zero-Knowledge Vault (ZK Vault)": "zk-vault",
    "vCIO Advisory Engine": "vc-suite-advisory",
}
pa_name_to_screenshot.update(FALLBACK)

modified = 0
skipped = 0
no_match = []

for pa_file in sorted(BASE.glob('zones/*/process-areas/*.html')):
    content = pa_file.read_text()
    
    # Skip pages that already have screenshots
    if 'screenshot-showcase' in content or 'assets/screenshots/' in content:
        skipped += 1
        continue
    
    # Get the PA title from the page
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.S)
    if not title_match:
        no_match.append(str(pa_file))
        continue
    
    pa_title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
    
    # Find the screenshot ID
    screenshot_id = pa_name_to_screenshot.get(pa_title)
    
    if not screenshot_id:
        # Try fuzzy matching by slug
        slug = pa_file.stem  # e.g. "known-error-database-kedb"
        # Try matching screenshot IDs
        for sid in screenshots:
            # Check if slug parts overlap
            slug_parts = set(slug.split('-'))
            sid_parts = set(sid.split('-'))
            overlap = slug_parts & sid_parts
            if len(overlap) >= 2 and len(overlap) / len(slug_parts) > 0.4:
                screenshot_id = sid
                break
    
    if not screenshot_id or screenshot_id not in screenshots:
        no_match.append(f"{pa_file.relative_to(BASE)}: '{pa_title}' -> {screenshot_id}")
        continue
    
    # Build the relative path from the PA page to the screenshot
    # PA pages are at zones/X/process-areas/Y.html
    # Screenshots are at assets/screenshots/Z.png
    img_path = f"../../../assets/screenshots/{screenshot_id}.png"
    
    # Create the screenshot showcase HTML
    showcase_html = f'''          <figure class="screenshot-showcase fade-up">
            <img src="{img_path}" alt="{pa_title} — AI-powered interface in DevOps AI" loading="lazy" width="1600" height="900">
            <figcaption>{pa_title} — Intelligent automation interface within DevOps AI</figcaption>
          </figure>'''
    
    # Insert after the "X in Practice" heading
    # Pattern: look for heading like "<h2>X in Practice</h2>" and insert after the closing </div>
    practice_pattern = re.compile(
        r'(<h2>.*?in Practice</h2>\s*</div>)',
        re.DOTALL
    )
    match = practice_pattern.search(content)
    
    if match:
        insert_pos = match.end()
        content = content[:insert_pos] + '\n' + showcase_html + '\n' + content[insert_pos:]
    else:
        # Try alternate pattern: look for "How It Works" or first h2 after hero
        alt_pattern = re.compile(
            r'(<!--\s*How It Works.*?-->.*?<h2>.*?</h2>\s*</div>)',
            re.DOTALL
        )
        alt_match = alt_pattern.search(content)
        if alt_match:
            insert_pos = alt_match.end()
            content = content[:insert_pos] + '\n' + showcase_html + '\n' + content[insert_pos:]
        else:
            # Last resort: insert before the first <div class="fade-up"> that contains workflow
            workflow_pattern = re.compile(r'(<div class="fade-up"[^>]*>\s*<p>DevOps AI)')
            wf_match = workflow_pattern.search(content)
            if wf_match:
                insert_pos = wf_match.start()
                content = content[:insert_pos] + showcase_html + '\n          ' + content[insert_pos:]
            else:
                no_match.append(f"{pa_file.relative_to(BASE)}: no insertion point found")
                continue
    
    pa_file.write_text(content)
    modified += 1

print(f"Modified: {modified}")
print(f"Skipped (already had screenshot): {skipped}")
print(f"No match ({len(no_match)}):")
for nm in no_match:
    print(f"  {nm}")
