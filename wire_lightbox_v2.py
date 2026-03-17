#!/usr/bin/env python3
"""
Wire clickable lightbox screenshots into all 14 role pages (v2).
Works with the new rzc-pa / role-zone-card structure.
Each rzc-pa list item becomes clickable, opening a lightbox overlay.
"""
import re, json
from pathlib import Path

BASE = Path(__file__).parent

# ── Build PA name → screenshot + page URL mapping ──
manifest = json.load(open(BASE.parent / 'screenshot-renderer' / 'pa-screenshot-manifest.json'))
pa_map = {}
for item in manifest:
    pa_map[item['pa']] = {'screenshot': item['id']}

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
for pa_name, screenshot_id in FALLBACK.items():
    if pa_name not in pa_map:
        pa_map[pa_name] = {'screenshot': screenshot_id}

# Build PA name → page URL from filesystem
pa_page_map = {}
for pa_file in BASE.glob('zones/*/process-areas/*.html'):
    content = pa_file.read_text()
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.S)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        rel = str(pa_file.relative_to(BASE))
        pa_page_map[title] = rel

# ── Lightbox CSS (adapted for rzc-pa items) ──
LIGHTBOX_CSS = '''
/* Lightbox overlay */
.pa-lightbox-overlay {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 22, 71, 0.85);
  z-index: 10000; display: none; align-items: center; justify-content: center;
  backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px);
  opacity: 0; transition: opacity 0.25s ease;
}
.pa-lightbox-overlay.active { display: flex; opacity: 1; }
.pa-lightbox-content {
  background: white; border-radius: 12px; max-width: 1100px; width: 94%;
  max-height: 90vh; overflow: hidden; box-shadow: 0 24px 80px rgba(0,0,0,0.3);
  transform: scale(0.95); transition: transform 0.25s ease;
}
.pa-lightbox-overlay.active .pa-lightbox-content { transform: scale(1); }
.pa-lightbox-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 24px; border-bottom: 1px solid #E0E0E0;
}
.pa-lightbox-title {
  font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800;
  font-size: 18px; color: #001647;
}
.pa-lightbox-close {
  width: 36px; height: 36px; border-radius: 8px; border: none;
  background: #F3F4F6; cursor: pointer; font-size: 20px; color: #97999B;
  display: flex; align-items: center; justify-content: center;
  transition: background 0.15s ease;
}
.pa-lightbox-close:hover { background: #E0E0E0; color: #001647; }
.pa-lightbox-img-wrap {
  padding: 16px 24px; overflow-y: auto; max-height: calc(90vh - 140px);
}
.pa-lightbox-img-wrap img {
  width: 100%; height: auto; border-radius: 8px;
  border: 1px solid #E0E0E0;
}
.pa-lightbox-footer {
  padding: 12px 24px 16px; border-top: 1px solid #E0E0E0;
  display: flex; align-items: center; justify-content: flex-end;
}
.pa-lightbox-link {
  display: inline-flex; align-items: center; gap: 6px;
  background: #79C600; color: white; padding: 10px 20px;
  border-radius: 8px; text-decoration: none;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 600; font-size: 14px;
  transition: background 0.15s ease;
}
.pa-lightbox-link:hover { background: #8BDB02; }
/* Make rzc-pa items clickable */
li.rzc-pa.has-preview {
  cursor: pointer; transition: background 0.15s ease;
  border-radius: 6px;
}
li.rzc-pa.has-preview:hover {
  background: rgba(121, 198, 0, 0.08);
}
li.rzc-pa.has-preview .rzc-pa__name::after {
  content: "\\1F50D"; font-size: 10px; margin-left: 6px; opacity: 0.35;
  transition: opacity 0.15s ease;
}
li.rzc-pa.has-preview:hover .rzc-pa__name::after {
  opacity: 1;
}
'''

# ── Lightbox HTML + JS ──
LIGHTBOX_JS = '''
<div class="pa-lightbox-overlay" id="paLightbox">
  <div class="pa-lightbox-content">
    <div class="pa-lightbox-header">
      <span class="pa-lightbox-title" id="paLightboxTitle"></span>
      <button class="pa-lightbox-close" id="paLightboxClose">&times;</button>
    </div>
    <div class="pa-lightbox-img-wrap">
      <img id="paLightboxImg" src="" alt="" loading="lazy">
    </div>
    <div class="pa-lightbox-footer">
      <a class="pa-lightbox-link" id="paLightboxLink" href="#">Explore this Process Area &rarr;</a>
    </div>
  </div>
</div>
<script>
(function() {
  var overlay = document.getElementById('paLightbox');
  var img = document.getElementById('paLightboxImg');
  var title = document.getElementById('paLightboxTitle');
  var link = document.getElementById('paLightboxLink');
  var closeBtn = document.getElementById('paLightboxClose');

  function openLightbox(paName, imgSrc, pageUrl) {
    title.textContent = paName;
    img.src = imgSrc;
    img.alt = paName + ' screenshot';
    link.href = pageUrl;
    overlay.style.display = 'flex';
    requestAnimationFrame(function() {
      overlay.classList.add('active');
    });
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    overlay.classList.remove('active');
    setTimeout(function() {
      overlay.style.display = 'none';
      img.src = '';
    }, 250);
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', closeLightbox);
  overlay.addEventListener('click', function(e) {
    if (e.target === overlay) closeLightbox();
  });
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeLightbox();
  });

  document.querySelectorAll('li.rzc-pa.has-preview').forEach(function(li) {
    li.addEventListener('click', function() {
      openLightbox(
        this.getAttribute('data-pa-name'),
        this.getAttribute('data-pa-img'),
        this.getAttribute('data-pa-url')
      );
    });
  });
})();
</script>
'''

# ── Process each role page ──
role_dir = BASE / 'roles'
modified = 0
total_wired = [0]

for role_file in sorted(role_dir.glob('*.html')):
    if role_file.name == 'index.html':
        continue
    
    content = role_file.read_text()
    original = content
    
    # Skip if already wired
    if 'pa-lightbox-overlay' in content:
        print(f"  SKIP {role_file.name} (already wired)")
        continue
    
    # Add lightbox CSS before </head>
    content = content.replace('</head>', f'<style>{LIGHTBOX_CSS}</style>\n</head>')
    
    # Handle both structures: rzc-pa (new) and process-card__step (old)
    # New structure: <li class="rzc-pa"><span class="rzc-pa__name">PA Name</span>...
    def replace_rzc_pa(match):
        full = match.group(0)
        name_match = re.search(r'rzc-pa__name">(.*?)</span>', full)
        if not name_match:
            return full
        
        # The name may have &amp; etc, decode HTML entities
        pa_name_html = name_match.group(1).strip()
        pa_name = pa_name_html.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        
        info = pa_map.get(pa_name, {})
        screenshot_id = info.get('screenshot', '')
        
        if not screenshot_id or not (BASE / 'assets' / 'screenshots' / f'{screenshot_id}.png').exists():
            return full
        
        # Find page URL
        page_url = ''
        if pa_name in pa_page_map:
            page_url = pa_page_map[pa_name]
        else:
            for pname, purl in pa_page_map.items():
                if pa_name.lower() == pname.lower():
                    page_url = purl
                    break
        
        img_path = f'../assets/screenshots/{screenshot_id}.png'
        pa_link = f'../{page_url}' if page_url else '#'
        
        new_li = full.replace(
            'class="rzc-pa"',
            f'class="rzc-pa has-preview" data-pa-name="{pa_name_html}" data-pa-img="{img_path}" data-pa-url="{pa_link}"'
        )
        total_wired[0] += 1
        return new_li
    
    content = re.sub(
        r'<li class="rzc-pa">.*?</li>',
        replace_rzc_pa,
        content,
        flags=re.DOTALL
    )
    
    # Also handle old process-card__step structure if present
    def replace_step(match):
        full = match.group(0)
        name_match = re.search(r'process-card__step-name">(.*?)</span>', full)
        if not name_match:
            return full
        
        pa_name = name_match.group(1).strip()
        info = pa_map.get(pa_name, {})
        screenshot_id = info.get('screenshot', '')
        
        if not screenshot_id or not (BASE / 'assets' / 'screenshots' / f'{screenshot_id}.png').exists():
            return full
        
        page_url = ''
        if pa_name in pa_page_map:
            page_url = pa_page_map[pa_name]
        else:
            for pname, purl in pa_page_map.items():
                if pa_name.lower() == pname.lower():
                    page_url = purl
                    break
        
        img_path = f'../assets/screenshots/{screenshot_id}.png'
        pa_link = f'../{page_url}' if page_url else '#'
        
        new_div = full.replace(
            'class="process-card__step"',
            f'class="process-card__step has-preview" data-pa-name="{pa_name}" data-pa-img="{img_path}" data-pa-url="{pa_link}"'
        )
        total_wired[0] += 1
        return new_div
    
    content = re.sub(
        r'<div class="process-card__step">.*?</div>',
        replace_step,
        content,
        flags=re.DOTALL
    )
    
    # Add lightbox HTML + JS before </body>
    content = content.replace('</body>', f'{LIGHTBOX_JS}\n</body>')
    
    if content != original:
        role_file.write_text(content)
        modified += 1
        print(f"  ✓ {role_file.name}")

print(f"\nModified {modified} role pages")
print(f"Total items wired: {total_wired[0]}")
