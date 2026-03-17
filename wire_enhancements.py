#!/usr/bin/env python3
"""Wire enhancements.css and enhancements.js into all HTML pages."""
from pathlib import Path

BASE = Path(__file__).parent
modified = 0

for html_file in sorted(BASE.rglob('*.html')):
    rel = str(html_file.relative_to(BASE))
    if rel.startswith('skills/') or rel.startswith('screenshot-renderer/'):
        continue
    
    content = html_file.read_text()
    original = content
    
    depth = len(html_file.relative_to(BASE).parts) - 1
    prefix = '../' * depth if depth > 0 else ''
    
    # Add enhancements.css before </head> if not already there
    if 'enhancements.css' not in content:
        content = content.replace(
            '</head>',
            f'  <link rel="stylesheet" href="{prefix}enhancements.css">\n</head>'
        )
    
    # Add enhancements.js before </body> if not already there
    if 'enhancements.js' not in content:
        content = content.replace(
            '</body>',
            f'<script src="{prefix}enhancements.js"></script>\n</body>'
        )
    
    if content != original:
        html_file.write_text(content)
        modified += 1

print(f"Modified {modified} HTML files with enhancements")
