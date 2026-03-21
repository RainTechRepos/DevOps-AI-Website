#!/usr/bin/env python3
"""
FR-W26: Sitemap Generator for DevOps AI Website
================================================
Scans the repository for all deployable HTML files and generates
a standards-compliant sitemap.xml with proper priorities and
change frequencies based on page type.

Usage:
    python scripts/generate-sitemap.py

Output:
    sitemap.xml in the repository root
"""

import os
import datetime
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom

# ─── Configuration ───────────────────────────────────────────────
SITE_URL = "https://devops.ai.rain.tech"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(REPO_ROOT, "sitemap.xml")

# Files to exclude from sitemap
EXCLUDE_FILES = {
    "_template.html",
    "404.html",
}

# Directories to exclude entirely
EXCLUDE_DIRS = {
    "docs",
    "scripts",
    "assets",
    "css",
    "js",
    "node_modules",
    ".git",
}

# Priority and changefreq rules by page type
# (pattern, priority, changefreq)
PAGE_RULES = [
    # Homepage — highest priority
    ("index.html", 1.0, "weekly"),
    # Top-level pages
    ("platform.html", 0.9, "weekly"),
    ("pricing.html", 0.9, "weekly"),
    ("architecture.html", 0.8, "monthly"),
    ("security.html", 0.8, "monthly"),
    ("roi.html", 0.8, "monthly"),
    # Role index
    ("roles/index.html", 0.8, "weekly"),
    # Individual role pages
    ("roles/", 0.7, "monthly"),
    # Zone index pages
    ("/index.html", 0.8, "weekly"),
    # Process area pages
    ("process-areas/", 0.6, "monthly"),
]

TODAY = datetime.date.today().isoformat()


def get_priority_and_freq(rel_path):
    """Determine priority and changefreq based on the file path."""
    # Root index.html
    if rel_path == "index.html":
        return 1.0, "weekly"

    # Top-level pages
    for name in ("platform.html", "pricing.html"):
        if rel_path == name:
            return 0.9, "weekly"

    for name in ("architecture.html", "security.html", "roi.html"):
        if rel_path == name:
            return 0.8, "monthly"

    # Role index
    if rel_path == "roles/index.html":
        return 0.8, "weekly"

    # Individual role pages
    if rel_path.startswith("roles/") and rel_path.endswith(".html"):
        return 0.7, "monthly"

    # Zone index pages
    if rel_path.startswith("zones/") and rel_path.endswith("/index.html"):
        return 0.8, "weekly"

    # Process area pages
    if "process-areas/" in rel_path:
        return 0.6, "monthly"

    # Default
    return 0.5, "monthly"


def path_to_url(rel_path):
    """Convert a relative file path to a full URL.

    - index.html → directory URL (trailing slash)
    - other.html → /other (no extension, clean URL)
    """
    if rel_path == "index.html":
        return SITE_URL + "/"

    if rel_path.endswith("/index.html"):
        # Zone/role index → directory URL
        directory = rel_path.replace("/index.html", "/")
        return f"{SITE_URL}/{directory}"

    # Strip .html for clean URLs
    clean = rel_path.replace(".html", "")
    return f"{SITE_URL}/{clean}"


def find_html_files():
    """Walk the repo and find all deployable HTML files."""
    html_files = []

    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        # Skip excluded directories (modify dirnames in-place)
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]

        for filename in filenames:
            if not filename.endswith(".html"):
                continue
            if filename in EXCLUDE_FILES:
                continue

            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, REPO_ROOT)
            # Normalize path separators
            rel_path = rel_path.replace("\\", "/")
            html_files.append(rel_path)

    return sorted(html_files)


def generate_sitemap():
    """Generate sitemap.xml from discovered HTML files."""
    html_files = find_html_files()

    # Build XML
    urlset = Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for rel_path in html_files:
        url_elem = SubElement(urlset, "url")

        loc = SubElement(url_elem, "loc")
        loc.text = path_to_url(rel_path)

        lastmod = SubElement(url_elem, "lastmod")
        lastmod.text = TODAY

        priority, changefreq_val = get_priority_and_freq(rel_path)

        changefreq = SubElement(url_elem, "changefreq")
        changefreq.text = changefreq_val

        priority_elem = SubElement(url_elem, "priority")
        priority_elem.text = f"{priority:.1f}"

    # Pretty-print XML
    rough_string = ET.tostring(urlset, encoding="unicode")
    # Wrap with XML declaration
    rough_string = rough_string if rough_string else ""
    dom = minidom.parseString(rough_string)
    pretty_xml = dom.toprettyxml(indent="  ", encoding=None)

    # Remove the extra XML declaration line from minidom and write our own
    lines = pretty_xml.split("\n")
    # minidom adds <?xml version="1.0" ?> — replace with proper encoding declaration
    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    for line in lines:
        if line.strip().startswith("<?xml"):
            continue
        xml_lines.append(line)

    xml_output = "\n".join(xml_lines).strip() + "\n"

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(xml_output)

    print(f"Generated sitemap.xml with {len(html_files)} URLs")
    print(f"Output: {OUTPUT_FILE}")

    # Print summary by type
    top_level = sum(1 for p in html_files if "/" not in p)
    role_pages = sum(1 for p in html_files if p.startswith("roles/"))
    zone_indexes = sum(
        1 for p in html_files
        if p.startswith("zones/") and p.endswith("/index.html")
    )
    pa_pages = sum(1 for p in html_files if "process-areas/" in p)

    print(f"\nBreakdown:")
    print(f"  Top-level pages:     {top_level}")
    print(f"  Role pages:          {role_pages}")
    print(f"  Zone index pages:    {zone_indexes}")
    print(f"  Process area pages:  {pa_pages}")
    print(f"  Total:               {len(html_files)}")


if __name__ == "__main__":
    generate_sitemap()
