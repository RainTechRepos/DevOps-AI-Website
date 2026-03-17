#!/usr/bin/env python3
"""
Normalize all 'People First' occurrences to brand-correct 'People, PERIOD.' treatment.

Rules:
1. HEADER / STANDOUT (footer taglines, h3s, blockquotes): 
   → Logo-style HTML with strikethrough 'First' and Rock Salt 'PERIOD.'
2. BODY TEXT (inline 'people-first'): 
   → 'People, Period.' as plain text (brand-correct inline phrasing)
3. META / TITLE tags: 
   → 'People, PERIOD.®' (plain text, no HTML)
4. aria-labels / comments: 
   → 'People, PERIOD.' (normalized)
"""
import os, re
from pathlib import Path

SITE = Path("/home/user/workspace/devops-ai-website")

# ─────────────────────────────────────────────────
# The logo-style HTML for standout placements
# ─────────────────────────────────────────────────
LOGO_HTML_FOOTER = '<span class="ppl-logo" aria-label="People, Period.">People <span class="ppl-strikethrough">First</span>, <span class="ppl-period">PERIOD.</span></span>'

LOGO_HTML_BLOCKQUOTE = f'"<span class="ppl-logo ppl-logo--lg" aria-label="People, Period.">&ldquo;People <span class="ppl-strikethrough">First</span>,<br><span class="ppl-period">PERIOD.</span>&rdquo;</span>"'

LOGO_HTML_H3 = '<span class="ppl-logo" aria-label="People, Period.">People <span class="ppl-strikethrough">First</span>, <span class="ppl-period">PERIOD.</span></span>'

# ─────────────────────────────────────────────────
# Font link addition — Rock Salt
# ─────────────────────────────────────────────────
OLD_FONT_LINK = 'href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"'
NEW_FONT_LINK = 'href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Rock+Salt&display=swap"'


def process_file(filepath):
    """Process a single HTML file for all People First normalizations."""
    html = filepath.read_text()
    changed = False
    
    # 1. Add Rock Salt to Google Fonts import
    if OLD_FONT_LINK in html and 'Rock+Salt' not in html:
        html = html.replace(OLD_FONT_LINK, NEW_FONT_LINK)
        changed = True
    
    # 2. Footer tagline: replace the div content
    old_footer = '<div class="footer-tagline">People First, PERIOD.&reg;</div>'
    new_footer = f'<div class="footer-tagline">{LOGO_HTML_FOOTER}</div>'
    if old_footer in html:
        html = html.replace(old_footer, new_footer)
        changed = True
    
    # 3. about.html specific replacements
    fname = filepath.name
    
    if fname == 'about.html':
        # Blockquote
        old_bq = '<blockquote>"<span class="accent">People First, PERIOD.</span>®"</blockquote>'
        new_bq = f'''<blockquote class="ppl-blockquote">
            <span class="ppl-logo ppl-logo--xl" aria-label="People, Period.">People <span class="ppl-strikethrough">First</span>,<br><span class="ppl-period">PERIOD.</span></span>
          </blockquote>'''
        if old_bq in html:
            html = html.replace(old_bq, new_bq)
            changed = True
        
        # Meta title
        html = html.replace(
            'About RainTech — People First, PERIOD.®',
            'About RainTech — People, PERIOD.®'
        )
        
        # Meta description — normalize 'People First philosophy' to 'People, Period.'
        html = html.replace(
            'People First philosophy',
            'People, Period. philosophy'
        )
        
        # Comment
        html = html.replace('<!-- PEOPLE FIRST -->', '<!-- PEOPLE, PERIOD. -->')
        
        # Aria label
        html = html.replace(
            'aria-label="People First philosophy"',
            'aria-label="People, Period. philosophy"'
        )
        
        # Body text: "people-first approach"
        html = html.replace(
            'a people-first approach',
            'a People, Period. approach'
        )
        
        changed = True
    
    if fname == 'index.html':
        # Body text: "people-first DevOps-as-a-Service"
        html = html.replace(
            'automation-first, people-first DevOps-as-a-Service',
            'automation-first, People, Period. DevOps-as-a-Service'
        )
        
        # Trust statement: inline with logo
        old_trust = '<p>Organizations across industries trust RainTech to deliver managed services with a People First, PERIOD.® approach.</p>'
        new_trust = f'<p>Organizations across industries trust RainTech to deliver managed services with a {LOGO_HTML_FOOTER} approach.</p>'
        html = html.replace(old_trust, new_trust)
        
        changed = True
    
    if fname == 'why-devops-ai.html':
        # H3 heading
        old_h3 = '<h3>People First, PERIOD.&reg;</h3>'
        new_h3 = f'<h3>{LOGO_HTML_H3}</h3>'
        html = html.replace(old_h3, new_h3)
        changed = True
    
    if changed:
        filepath.write_text(html)
    
    return changed


def main():
    count = 0
    # Process all HTML files
    for html_file in sorted(SITE.rglob("*.html")):
        if '.git' in str(html_file):
            continue
        if process_file(html_file):
            count += 1
    
    print(f"Updated {count} files.")
    
    # Verify no remaining 'People First' in visible content 
    # (meta tags may still have it where needed as plain text)
    print("\n=== Remaining 'People First' occurrences ===")
    for html_file in sorted(SITE.rglob("*.html")):
        if '.git' in str(html_file):
            continue
        content = html_file.read_text()
        for i, line in enumerate(content.split('\n'), 1):
            if 'People First' in line or 'people-first' in line or 'people first' in line:
                rel = html_file.relative_to(SITE)
                print(f"  {rel}:{i}: {line.strip()[:120]}")


if __name__ == "__main__":
    main()
