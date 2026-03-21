# Self-hosted Fonts

This directory will hold WOFF2 font files for the DevOps AI design system.

## Fonts Required

### Plus Jakarta Sans (variable / static)
| Weight | Filename |
|--------|----------|
| 400    | `plus-jakarta-sans-400.woff2` |
| 500    | `plus-jakarta-sans-500.woff2` |
| 600    | `plus-jakarta-sans-600.woff2` |
| 700    | `plus-jakarta-sans-700.woff2` |
| 800    | `plus-jakarta-sans-800.woff2` |

### JetBrains Mono
| Weight | Filename |
|--------|----------|
| 400    | `jetbrains-mono-400.woff2` |
| 700    | `jetbrains-mono-700.woff2` |

## Status

`@font-face` declarations are already wired in `css/base.css` using Google Fonts CDN
URLs as `src`. Replace each CDN URL with a local `url('../assets/fonts/<filename>.woff2')`
path once the WOFF2 files are downloaded and placed here.

## Download Commands (run once)

```bash
# Example using curl — replace URLs with correct Google Fonts static file URLs
curl -L "https://fonts.gstatic.com/s/plusjakartasans/..." -o plus-jakarta-sans-400.woff2
```

Alternatively, use [google-webfonts-helper](https://gwfh.mranftl.com/fonts) to batch-download
all weights as WOFF2.
