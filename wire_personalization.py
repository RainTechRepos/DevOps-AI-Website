#!/usr/bin/env python3
"""
Wire the 4-layer personalization system into all HTML pages.
- Remove old cookie-banner div
- Add personalization.css link
- Add personalization.js script
- Remove old cookie consent JS from app.js
"""
import re
from pathlib import Path

BASE = Path(__file__).parent
modified = 0

for html_file in sorted(BASE.rglob('*.html')):
    # Skip non-website files
    rel = str(html_file.relative_to(BASE))
    if rel.startswith('skills/') or rel.startswith('screenshot-renderer/'):
        continue
    
    content = html_file.read_text()
    original = content
    
    # 1. Remove old cookie-banner div (with all its contents)
    content = re.sub(
        r'\n*<div class="cookie-banner"[^>]*>.*?</div>\s*</div>\s*\n*',
        '\n',
        content,
        flags=re.DOTALL
    )
    
    # 2. Calculate relative path to root
    depth = len(html_file.relative_to(BASE).parts) - 1
    prefix = '../' * depth if depth > 0 else ''
    
    # 3. Add personalization.css before </head> if not already there
    if 'personalization.css' not in content:
        content = content.replace(
            '</head>',
            f'  <link rel="stylesheet" href="{prefix}personalization.css">\n</head>'
        )
    
    # 4. Add personalization.js before </body> if not already there
    if 'personalization.js' not in content:
        content = content.replace(
            '</body>',
            f'<script src="{prefix}personalization.js"></script>\n</body>'
        )
    
    if content != original:
        html_file.write_text(content)
        modified += 1

print(f"Modified {modified} HTML files")

# 5. Remove old cookie consent IIFE from app.js
app_js = BASE / 'app.js'
app_content = app_js.read_text()

# Remove the cookie consent section
cookie_start = app_content.find('// ---- Cookie Consent (GDPR/CCPA Compliant) ----')
if cookie_start >= 0:
    app_content = app_content[:cookie_start].rstrip() + '\n'
    app_js.write_text(app_content)
    print("Removed old cookie consent code from app.js")
else:
    print("No old cookie consent code found in app.js")
