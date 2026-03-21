#!/usr/bin/env python3
"""
FR-W27: Asset Optimization Scaffold for DevOps AI Website
==========================================================
Placeholder script for future asset optimization pipeline.
When fully implemented, this script will:

1. Minify CSS files (cssnano or similar)
2. Minify JS files (terser or similar)
3. Optimize images (WebP conversion, compression)
4. Generate critical CSS for above-the-fold content
5. Create asset manifests with content hashes for cache busting

Usage:
    python scripts/optimize-assets.py [--dry-run]

Requires (future):
    pip install csscompressor rjsmin Pillow

Currently outputs an audit of assets that would be optimized.
"""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── Asset categories ────────────────────────────────────────────
ASSET_TYPES = {
    "css": {
        "extensions": (".css",),
        "dirs": ("css",),
        "description": "Stylesheets",
    },
    "js": {
        "extensions": (".js",),
        "dirs": ("js",),
        "description": "JavaScript",
    },
    "images": {
        "extensions": (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"),
        "dirs": ("assets",),
        "description": "Images",
    },
    "fonts": {
        "extensions": (".woff", ".woff2", ".ttf", ".otf", ".eot"),
        "dirs": ("assets/fonts",),
        "description": "Fonts",
    },
}


def find_assets(asset_type):
    """Find all assets of a given type."""
    config = ASSET_TYPES[asset_type]
    assets = []

    for search_dir in config["dirs"]:
        full_dir = os.path.join(REPO_ROOT, search_dir)
        if not os.path.isdir(full_dir):
            continue

        for dirpath, _, filenames in os.walk(full_dir):
            for filename in filenames:
                if filename.endswith(config["extensions"]):
                    full_path = os.path.join(dirpath, filename)
                    rel_path = os.path.relpath(full_path, REPO_ROOT)
                    size = os.path.getsize(full_path)
                    assets.append({
                        "path": rel_path,
                        "size": size,
                        "filename": filename,
                    })

    return sorted(assets, key=lambda a: a["path"])


def format_size(bytes_val):
    """Format bytes into human-readable size."""
    if bytes_val < 1024:
        return f"{bytes_val} B"
    elif bytes_val < 1024 * 1024:
        return f"{bytes_val / 1024:.1f} KB"
    else:
        return f"{bytes_val / (1024 * 1024):.1f} MB"


def audit_assets():
    """Run an audit of all assets and report sizes."""
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("DevOps AI — Asset Optimization Audit")
    print("=" * 60)

    if dry_run:
        print("Mode: DRY RUN (no changes will be made)\n")
    else:
        print("Mode: AUDIT ONLY (optimization not yet implemented)\n")

    total_size = 0
    total_files = 0

    for asset_type, config in ASSET_TYPES.items():
        assets = find_assets(asset_type)
        if not assets:
            continue

        type_size = sum(a["size"] for a in assets)
        total_size += type_size
        total_files += len(assets)

        print(f"\n{config['description']} ({len(assets)} files, {format_size(type_size)})")
        print("-" * 50)

        for asset in assets:
            print(f"  {asset['path']:50s}  {format_size(asset['size']):>10s}")

    print(f"\n{'=' * 60}")
    print(f"Total: {total_files} files, {format_size(total_size)}")
    print(f"{'=' * 60}")

    # Recommendations
    print("\nOptimization recommendations:")
    print("  1. CSS: Minify with cssnano, extract critical CSS")
    print("  2. JS:  Minify with terser, defer non-critical scripts")
    print("  3. Images: Convert to WebP, compress PNGs/JPEGs")
    print("  4. Fonts: Subset to used characters, preload critical fonts")
    print("  5. Add content hashes to filenames for cache busting")
    print("\nTo implement: Install dependencies and re-run without --dry-run")


if __name__ == "__main__":
    audit_assets()
