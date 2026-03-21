# DevOps AI Website Redesign — Comprehensive Specification

**Document:** Website Redesign Specification & Feature Request Decomposition  
**Version:** 1.0  
**Date:** March 21, 2026  
**Author:** RainTech Engineering  
**Repository:** RainTechRepos/DevOps-AI-Website (branch: `full-site-backup`)  
**Domain:** devops.ai.rain.tech  
**Platform URL:** platform.devops.ai.rain.tech

---

## Table of Contents

1. [Design Philosophy & Principles](#part-1-design-philosophy--principles)
2. [Information Architecture](#part-2-information-architecture)
3. [Page-by-Page Specifications](#part-3-page-by-page-specifications)
4. [Interactive Components](#part-4-interactive-components)
5. [Design System Evolution](#part-5-design-system-evolution)
6. [Technical Architecture](#part-6-technical-architecture)
7. [FR Decomposition for Parallel Orchestration](#part-7-fr-decomposition-for-parallel-orchestration)

---

## Part 1: Design Philosophy & Principles

### 1.1 AI-First Design Language

DevOps AI is not another SaaS tool website. It represents a fundamental shift in how Managed Service Providers operate — from reactive, human-only workflows to an ambient intelligence layer that orchestrates 157+ process areas across 15 operational zones. The design language must communicate this paradigm shift without resorting to generic "AI-powered" platitudes.

**What makes this different from every other MSP website:**

| Dimension | Traditional MSP Websites (Kaseya, Datto, ConnectWise) | DevOps AI |
|-----------|-------------------------------------------------------|-----------|
| Visual Language | Conservative blue/white, stock photography, CMS templates | Dark-first, glassmorphic depth, product-as-hero, real UI |
| AI Positioning | "AI-powered" as a feature bullet | AI as the operating system — ambient, always-on, 157 process areas |
| Content Model | Feature lists organized by product SKU | Role-based journeys organized by human intent |
| Interaction | Static pages, gated demos, "Contact Sales" | Interactive demos, live metrics, ungated exploration |
| Trust Model | Logo walls and generic testimonials | Trust Center with compliance architecture, HITL controls, data residency maps |
| Depth | Shallow marketing pages | 198-page deep-dive into every zone, process area, and role |

**Design Principles:**

1. **Ambient Intelligence, Not Feature Lists** — The site should feel like the platform itself: intelligent, anticipatory, quietly powerful. Content surfaces contextually based on who you are and what you need, mirroring how DevOps AI works inside the platform.

2. **Product as Proof** — Every claim is backed by real platform UI. The 160+ screenshots are not supplementary illustrations — they ARE the marketing. When we say "AI-powered ticket triage," the visitor sees the actual triage interface.

3. **Human-First AI** — The design communicates that DevOps AI amplifies humans, not replaces them. Every AI capability shown includes the human-in-the-loop control point. This is a regulatory and ethical differentiator.

4. **Progressive Depth** — The homepage speaks in outcomes ("Resolve 70% of L1 tickets automatically"). Zone pages speak in capabilities. Process area pages speak in technical specifications. The visitor controls their depth.

5. **Operational Maturity Signaled Through Design Consistency** — A 198-page site with perfect design consistency across every page signals that the product behind it is equally well-architected. No page should feel like an afterthought.

### 1.2 The "New Paradigm" Positioning

DevOps AI represents a new category: **AI-as-a-Service for Managed Service Providers**. This is not:
- Another RMM/PSA tool (Kaseya, ConnectWise, Datto)
- A generic AI chatbot bolted onto existing workflows
- An automation tool that handles a few tasks

This IS:
- A multi-tenant platform spanning 15 operational zones and 157+ process areas
- A 3-tier branding engine (Platform → MSP → Client) that white-labels at every level
- An inference infrastructure with Azure OpenAI, admin control planes, and granular security
- A role-aware intelligence layer serving 20+ distinct personas simultaneously

**Positioning Statement (for all copy direction):**
> "DevOps AI is the operating intelligence for modern MSPs. It doesn't just automate tasks — it transforms how your entire organization thinks, decides, and acts across every operational zone."

**Competitive Frame:**
- ConnectWise claims "agentic AI-native platform" — but they bolt AI onto existing PSA/RMM tools
- DevOps AI IS AI-native — built from the ground up with AI at every process area, not retrofitted

### 1.3 Visual Design Direction

**Evolution, Not Revolution:** The existing design system (dark cetacean blue, green accent, Plus Jakarta Sans) is already strong. The redesign evolves it toward a more sophisticated, glassmorphic, depth-aware aesthetic while preserving brand continuity.

**Direction: "Deep Intelligence"**

| Element | Current | Evolved |
|---------|---------|---------|
| Background | Flat cetacean blue (#001647) | Layered depth: gradient backgrounds with subtle aurora effects, glassmorphic panels floating above |
| Accent | Green (#8BDB02) — flat | Green (#8BDB02) with glow effects, gradient trails, and animated pulse for AI-activity indicators |
| Cards | `rgba(255,255,255,0.04)` flat | Glassmorphic: `backdrop-filter: blur(12px)`, subtle border glow, layered shadows |
| Typography | Plus Jakarta Sans (all weights) | Plus Jakarta Sans retained, but with more dramatic size contrast: hero text at `--text-hero`, tighter letter-spacing for headlines |
| Imagery | 160 screenshots displayed inline | Screenshots in device mockups or floating glassmorphic frames with subtle parallax |
| Depth | Flat 2D layout | Z-axis hierarchy: background aurora → mid-layer content → floating cards → glassmorphic overlays |
| Motion | Basic fade-up on scroll | CSS scroll-driven animations, particle effects for AI activity, subtle parallax |

**Color Palette Evolution:**

```
Primary Background:    #001647 (cetacean blue — retained)
Deep Background:       #000E2E (deeper for contrast layering)
Surface Background:    #001a52 (elevated surfaces)
Card Background:       rgba(255, 255, 255, 0.05) → rgba(255, 255, 255, 0.08) on hover

Accent Primary:        #8BDB02 (green — retained)
Accent Secondary:      #17E4ED (cyan — for AI indicators)
Accent Tertiary:       #C616EA (violet — for alerts/highlights)
Accent Warm:           #2272E0 (blue-mid — for links/interactive)

Gradient Hero:         linear-gradient(135deg, #8BDB02 0%, #17E4ED 100%) — retained
Gradient AI Activity:  linear-gradient(90deg, #8BDB02, #17E4ED, #C616EA) — new animated gradient
Gradient Depth:        radial-gradient(ellipse at 50% 0%, #05108E 0%, #001647 50%, #000E2E 100%) — new

Text Primary:          #F7F7FF (ghost white — retained)
Text Secondary:        rgba(247, 247, 255, 0.72)
Text Tertiary:         rgba(247, 247, 255, 0.48)
```

### 1.4 Motion and Interaction Philosophy

**Principle: Purposeful restraint with moments of spectacle.**

Motion serves three purposes on this site:
1. **Orientation** — scroll-triggered reveals help visitors understand content hierarchy
2. **Delight** — key moments (hero entry, role selection, chatbot activation) have crafted animations
3. **Communication** — particle effects and glow animations communicate "AI is working"

**Motion Budget:**

| Context | Animation Type | Duration | Trigger |
|---------|---------------|----------|---------|
| Section entry | Fade-up + slight scale | 400–600ms | Scroll into view (CSS `animation-timeline: view()`) |
| Card hover | Scale(1.02) + border glow + shadow lift | 150ms | `:hover` / `:focus-visible` |
| Hero entry | Staggered text reveal + gradient sweep | 1200ms total | Page load |
| Neural network BG | Slow ambient drift | Continuous | Page load (only on homepage, entry point) |
| Number counters | Count-up animation | 1500ms | Scroll into view |
| Page transitions | Crossfade opacity | 250ms | Navigation |
| Chatbot open | Slide-up + fade | 300ms | Click |
| Screenshot lightbox | Scale-up + backdrop blur | 250ms | Click |

**Reduced Motion:** All animations respect `prefers-reduced-motion: reduce`. Alternatives:
- Fade-up → instant opacity change
- Count-up → static display of final number
- Parallax → static positioning
- Neural network → static gradient background
- Continuous animations → frozen at final state

**Performance Rules:**
- Only animate `transform` and `opacity` (compositor-friendly)
- Use CSS `animation-timeline: view()` for scroll reveals (no JS IntersectionObserver)
- Three.js only on journey entry point — lazy loaded, with WebGL capability check
- All motion under 1s unless it's a deliberate narrative sequence (hero, entry point)
- Never `transition: all` — explicitly list properties

### 1.5 Accessibility Approach

**Baseline: WCAG 2.2 AA** with forward-looking APCA-compatible decisions.

| Requirement | Implementation |
|-------------|---------------|
| Color Contrast | 4.5:1 minimum for normal text, 3:1 for large text. Green accent (#8BDB02) on dark blue (#001647) = 7.3:1 ✓. All color combinations pre-validated. |
| Focus Indicators | 2px solid `var(--accent)` outline, 3px offset. Visible on all focusable elements. Enhanced for dark mode visibility. |
| Target Size | Minimum 44×44px touch targets on mobile, 24×24px on desktop (WCAG 2.2 Level AA) |
| Keyboard Navigation | Full keyboard operability. Skip-to-content link. Logical tab order. Visible focus states. Arrow key navigation in role picker. |
| Screen Readers | Semantic HTML first (no ARIA unless necessary). `aria-live` for dynamic content (chatbot, live metrics). `aria-label` on all icon-only buttons. Heading hierarchy enforced. |
| Reduced Motion | `@media (prefers-reduced-motion: reduce)` — provide alternatives, not just disable |
| Reduced Transparency | `@media (prefers-reduced-transparency: reduce)` — solid backgrounds instead of glassmorphic |
| High Contrast | `@media (forced-colors: active)` — transparent borders as fallbacks, system colors respected |
| Content | Max 70ch line length. Flesch-Kincaid grade 8–10 for marketing copy. Clear heading hierarchy. |
| Forms | Associated labels, error messages linked via `aria-describedby`, no time limits, no re-entry of data |

**Forward-Looking (WCAG 3.0 preparation):**
- Design token names are semantic (`--text-primary`, not `--white`)
- Color system supports APCA-based contrast calculations
- Cognitive accessibility patterns: consistent navigation, findable help (chatbot), clear language

---

## Part 2: Information Architecture

### 2.1 Complete Sitemap

```
devops.ai.rain.tech/
│
├── index.html                          ← Homepage
├── platform.html                       ← Platform Overview
├── why-devops-ai.html                  ← Why DevOps AI / Value Proposition
├── architecture.html                   ← Technical Architecture
├── security.html                       ← Security & Trust Center
├── solutions.html                      ← Solutions Hub (by industry/use case)
├── pricing.html                        ← Pricing (MSP tiers — no Enterprise toggle)
├── roi.html                            ← ROI Calculator
├── marketplace.html                    ← Azure Marketplace / Getting Started
├── about.html                          ← About RainTech
├── contact.html                        ← Contact / Sales / Support
├── blog.html                           ← Blog & Resources Hub
├── login.html                          ← Login Redirect → platform.devops.ai.rain.tech
│
├── roles/
│   ├── index.html                      ← All Roles Overview
│   │
│   │ ── Executive Suite ──
│   ├── msp-owner.html                  ← MSP Owner / CEO
│   ├── vcio.html                       ← vCIO
│   ├── vciso.html                      ← vCISO
│   ├── vcco.html                       ← vCCO
│   ├── vcto.html                       ← vCTO (NEW)
│   │
│   │ ── Operations ──
│   ├── it-director.html                ← IT Director
│   ├── service-delivery-manager.html   ← Service Delivery Manager (NEW — separated from PM)
│   ├── project-manager.html            ← Project Manager (refined — migration/deployment focus)
│   ├── service-desk-manager.html       ← Service Desk Manager
│   ├── network-engineer.html           ← Network Engineer
│   ├── devops-engineer.html            ← DevOps Engineer
│   │
│   │ ── Security & Compliance ──
│   ├── security-analyst.html           ← Security Analyst
│   ├── compliance-officer.html         ← Compliance Officer
│   │
│   │ ── Business & Relationships ──
│   ├── client-success-manager.html     ← Client Success Manager (renamed from Account Manager)
│   ├── finance-coordinator.html        ← Finance Coordinator
│   ├── sales-director.html             ← Sales Director
│   ├── marketing-director.html         ← Marketing Director
│   ├── data-analyst.html               ← Data Analyst / BI Lead
│   │
│   │ ── People & Culture ──
│   ├── hr-director.html                ← HR Director
│   ├── recruiter.html                  ← Recruiter
│   ├── legal-counsel.html              ← Legal Counsel
│
├── zones/
│   ├── service-desk/
│   │   ├── index.html                  ← Zone Overview
│   │   └── process-areas/
│   │       ├── ticket-ingestion-ai-triage.html
│   │       ├── nlp-intake-classification.html
│   │       ├── ... (12 process areas)
│   │
│   ├── security-operations/            ← (13 process areas)
│   ├── grc-compliance/                 ← (11 process areas)
│   ├── endpoint-management/            ← (10 process areas)
│   ├── network-ops/                    ← (9 process areas)
│   ├── vc-suite/                       ← (13 process areas)
│   ├── analytics/                      ← (9 process areas)
│   ├── relationships/                  ← (11 process areas)
│   ├── people/                         ← (8 process areas)
│   ├── learning/                       ← (10 process areas)
│   ├── organization/                   ← (11 process areas)
│   ├── legal/                          ← (7 process areas)
│   ├── devops/                         ← (11 process areas)
│   ├── accounting/                     ← (11 process areas)
│   └── projects/                       ← (11 process areas)
│
├── legal/
│   ├── privacy.html                    ← Privacy Policy
│   ├── terms.html                      ← Terms of Service (NEW)
│   └── acceptable-use.html             ← Acceptable Use Policy (NEW)
│
├── docs/
│   └── (existing documentation assets)
│
├── assets/
│   └── screenshots/                    ← 160 platform screenshots
│
├── sitemap.xml
├── robots.txt
├── llms.txt                            ← NEW: AI/LLM discoverability
├── CNAME                               ← devops.ai.rain.tech
└── 404.html                            ← Custom 404
```

**Total Pages: ~210** (198 existing + vCTO, SDM, terms, acceptable-use, blog, login, 404, llms.txt)

### 2.2 Navigation Structure

#### Primary Navigation (Desktop)

```
┌─────────────────────────────────────────────────────────────┐
│  [DevOps AI Logo]                                           │
│                                                             │
│  Platform ▾ │ Solutions ▾ │ Pricing │ Security │ Resources ▾ │
│                                                             │
│                               [Login]  [Get Started →]      │
└─────────────────────────────────────────────────────────────┘
```

**Platform Mega-Menu:**
```
┌──────────────────────────────────────────────────────────┐
│ PLATFORM OVERVIEW                                        │
│ The complete AI operating system for MSPs                │
│                                                          │
│ ── By Zone ──                    ── Capabilities ──      │
│ Service Desk                     AI & Automation         │
│ Security Operations              Multi-Tenant Branding   │
│ GRC & Compliance                 Inference Infrastructure│
│ Endpoint Management              Role-Based Intelligence │
│ Network Ops                      Integration Ecosystem   │
│ vC-Suite                                                 │
│ Analytics                        ── Technical ──         │
│ + 8 more zones →                 Architecture            │
│                                  API & Integrations      │
│ ── By Role ──                    Azure Marketplace       │
│ I'm an MSP Owner                                         │
│ I'm a Technical Leader                                   │
│ I'm on the Help Desk                                     │
│ See all 21 roles →                                       │
└──────────────────────────────────────────────────────────┘
```

**Solutions Mega-Menu:**
```
┌──────────────────────────────────────────────────────────┐
│ ── By Challenge ──               ── By Industry ──       │
│ Reduce Ticket Volume             Healthcare MSPs         │
│ Scale Without Hiring             Financial Services      │
│ Improve SLA Compliance           Government/GovCloud     │
│ Automate Compliance              Legal/Professional Svcs │
│ Unify Tool Sprawl                                        │
│                                  ── By Size ──           │
│ ── By Journey ──                 Startup MSPs (1-10)     │
│ New MSP Setup                    Growth MSPs (10-50)     │
│ Migration from Legacy            Enterprise MSPs (50+)   │
│ Scale & Optimize                                         │
└──────────────────────────────────────────────────────────┘
```

**Resources Mega-Menu:**
```
┌──────────────────────────────────────────────────────────┐
│ ── Learn ──                      ── Company ──           │
│ Blog                             About RainTech          │
│ ROI Calculator                   Contact                 │
│ Interactive Demo                 Careers                 │
│ Documentation                                            │
│                                  ── Trust ──             │
│ ── Community ──                  Security & Trust Center  │
│ MSP Benchmark Report             Privacy Policy          │
│ Webinars & Events                Compliance Docs         │
│ Partner Program                                          │
└──────────────────────────────────────────────────────────┘
```

#### Mobile Navigation
- Hamburger menu (right side)
- Full-screen overlay with accordion sections matching mega-menus
- Persistent bottom bar with [Get Started] CTA
- Thumb-zone optimized: all interactive elements within bottom 60% of screen

#### Footer Navigation

```
┌──────────────────────────────────────────────────────────────┐
│  [DevOps AI Logo]          AI-as-a-Service for MSPs          │
│                                                               │
│  Platform          Solutions        Resources       Company   │
│  ─────────         ─────────        ─────────       ───────   │
│  Overview          By Challenge     Blog            About     │
│  All 15 Zones      By Industry      ROI Calculator  Contact   │
│  All 21 Roles      By MSP Size      Demo            Careers   │
│  Architecture      Case Studies     Docs            Press     │
│  Integrations                       Webinars                  │
│                                                               │
│  Trust & Legal     Connect                                    │
│  ─────────────     ───────                                    │
│  Security Center   LinkedIn                                   │
│  Privacy Policy    GitHub                                     │
│  Terms of Service  YouTube                                    │
│  Compliance                                                   │
│                                                               │
│  ─────────────────────────────────────────────────────────── │
│  © 2026 RainTech. All rights reserved.                       │
│  DevOps AI is deployed via Azure Marketplace.                │
│  Created with Perplexity Computer                            │
└──────────────────────────────────────────────────────────────┘
```

### 2.3 Role-Based Journey Paths

**21 roles across 5 categories** (adding vCTO and Service Delivery Manager; renaming Account Manager to Client Success Manager):

#### Executive Suite (5 roles)
| Role | Primary Journey | Key Zones | CTA Path |
|------|----------------|-----------|----------|
| MSP Owner / CEO | ROI, growth metrics, competitive positioning | vC-Suite, Analytics, Relationships | Book Demo → Pricing → Marketplace |
| vCIO | Technology roadmaps, budget forecasting, strategic advisory | vC-Suite, Projects, Analytics | Architecture → Demo → Marketplace |
| vCISO | Security program management, risk scoring, compliance automation | Security Ops, GRC, vC-Suite | Security Center → Demo → Marketplace |
| vCCO | Framework lifecycle, audit automation, compliance governance | GRC, vC-Suite, Legal | Security Center → Compliance → Marketplace |
| vCTO | Architecture reviews, infrastructure strategy, technical debt management | DevOps, Network Ops, vC-Suite | Architecture → Demo → Marketplace |

#### Operations (6 roles)
| Role | Primary Journey | Key Zones | CTA Path |
|------|----------------|-----------|----------|
| IT Director | Unified operations, tool consolidation, team productivity | Service Desk, Endpoint, Network Ops | Platform Overview → Demo → Pricing |
| Service Delivery Manager (NEW) | Ongoing service quality, SLA management, escalation, QBR delivery | Service Desk, Analytics, Relationships | Solutions → Role Page → Demo |
| Project Manager (refined) | Migration planning, deployment timelines, phase-gated execution | Projects, Service Desk, Analytics | Solutions → Role Page → Demo |
| Service Desk Manager | AI triage, dispatch optimization, predictive SLA management | Service Desk, Endpoint, Analytics | Platform → Zone → Demo |
| Network Engineer | Topology, capacity forecasting, automated patching | Network Ops, Endpoint, Security Ops | Architecture → Zone → Demo |
| DevOps Engineer | CI/CD pipelines, infrastructure automation, platform operations | DevOps, Network Ops, Security Ops | Architecture → Zone → Demo |

#### Security & Compliance (2 roles)
| Role | Primary Journey | Key Zones | CTA Path |
|------|----------------|-----------|----------|
| Security Analyst | Threat detection, incident response, zero-trust governance | Security Ops, GRC, Endpoint | Security Center → Zone → Demo |
| Compliance Officer | CMMC/SOC 2/HIPAA, continuous monitoring, OSCAL evidence | GRC, Legal, Security Ops | Security Center → Zone → Demo |

#### Business & Relationships (5 roles)
| Role | Primary Journey | Key Zones | CTA Path |
|------|----------------|-----------|----------|
| Client Success Manager | Client health scoring, churn prediction, onboarding, QBR | Relationships, Service Desk, Analytics | Solutions → Role Page → Demo |
| Finance Coordinator | Invoice ingestion, reconciliation, revenue recognition | Accounting, Analytics, Relationships | ROI Calculator → Zone → Demo |
| Sales Director | Lead generation, ICP scoring, pipeline management, proposals | Relationships, Analytics, vC-Suite | Solutions → ROI → Demo |
| Marketing Director | Campaign orchestration, content management, brand comms | Relationships, Analytics, Learning | Solutions → Role Page → Demo |
| Data Analyst / BI Lead | Cross-zone analytics, AI report review, data integrity | Analytics, vC-Suite, Accounting | Platform → Zone → Demo |

#### People & Culture (3 roles)
| Role | Primary Journey | Key Zones | CTA Path |
|------|----------------|-----------|----------|
| HR Director | Workforce analytics, access lifecycle, automated onboarding | People, Learning, Organization | Solutions → Zone → Demo |
| Recruiter | Skill gap analysis, onboarding automation, directory sync | People, Learning, Organization | Solutions → Zone → Demo |
| Legal Counsel | Contract review, regulatory filings, compliance docs | Legal, GRC, vC-Suite | Security Center → Zone → Demo |

### 2.4 Content Hierarchy Per Page Type

**Hierarchy Model:** Every page follows a Z-pattern scan path:

```
Level 1: WHAT (Headline — what is this page about?) — 2 seconds
Level 2: WHY (Value proposition — why should I care?) — 5 seconds
Level 3: HOW (Evidence — how does it work? Show me.) — 15 seconds
Level 4: PROOF (Social proof — who else uses this?) — 30 seconds
Level 5: ACTION (CTA — what do I do next?) — conversion point
```

---

## Part 3: Page-by-Page Specifications

### 3.1 Homepage (`index.html`)

**Purpose:** Primary landing page. Must communicate the platform's scope, differentiation, and value in under 5 seconds while providing clear paths for 5 buyer categories.

**Audience:** All visitors — first-time and returning. MSP owners, technical leads, help desk staff, executives, evaluators.

**Content Sections:**

#### Section 1: Hero
- **Headline:** "The AI Operating System for Modern MSPs" (7 words, outcome-focused)
- **Rotating Sub-headline:** Cycles through role-specific value:
  - "Resolve 70% of L1 tickets before a human touches them"
  - "15 zones. 157 process areas. One intelligent platform."
  - "Built for MSPs who refuse to scale by hiring alone"
- **Visual:** Product screenshot in a floating glassmorphic frame — showing the actual platform dashboard with AI triage in action. Subtle parallax on scroll. Neural network particle effect in background (evolved from existing `entry-point.js` background canvas).
- **CTAs:**
  - Primary: "Start Free Evaluation" (filled green button)
  - Secondary: "Watch 2-Min Demo" (outlined, with play icon)
- **Trust micro-bar:** "Deployed via Azure Marketplace • SOC 2 Type II • Multi-Tenant Isolation"

#### Section 2: Trust Bar
- MSP customer/partner logos (6–8 logos, grayscale → color on hover)
- Key metrics bar: "X Zones | Y Process Areas | Z Roles Supported"
- Animated number counters on scroll entry

#### Section 3: Problem / Solution
- **Headline:** "Your MSP Challenges. Solved by Intelligence."
- Three-column problem/solution cards:
  - Problem: "Drowning in tickets" → Solution: "AI triage resolves L1 automatically"
  - Problem: "Can't scale without hiring" → Solution: "157 automated process areas"
  - Problem: "Compliance is a nightmare" → Solution: "OSCAL-native evidence collection"
- Each card links to relevant zone page

#### Section 4: Product Showcase (Bento Grid)
- **Headline:** "See What 15 Zones of Intelligence Looks Like"
- Bento grid layout with 6–8 tiles of varying sizes:
  - Large tile: Hero screenshot of the dashboard with glassmorphic overlay
  - Medium tiles: Service Desk AI Triage, Security Operations, Compliance Automation
  - Small tiles: Network Ops, Analytics, vC-Suite KPIs
- Each tile shows a real screenshot with a brief capability label
- Tiles expand on hover (Active Grid pattern) to show 2–3 sentence description
- Click → relevant zone page

#### Section 5: Role-Based Entry Paths
- **Headline:** "Built for Every Role in Your MSP"
- 5 category cards (matching existing group structure):
  - Executive Suite (5 roles) — "Strategic intelligence for leadership"
  - Operations (6 roles) — "Unified ops, AI-powered"
  - Security & Compliance (2 roles) — "Zero-trust, always-on"
  - Business & Relationships (5 roles) — "Client success, automated"
  - People & Culture (3 roles) — "Your team, amplified"
- Each card lists the roles within, links to roles/index.html
- CTA: "Find Your Role →" (triggers journey entry point experience)

#### Section 6: How It Works
- **Headline:** "From Azure Marketplace to AI-Powered Operations"
- Three-step visual flow:
  1. "Deploy" — One-click Azure Marketplace deployment
  2. "Configure" — 3-tier branding, role assignment, zone activation
  3. "Transform" — AI begins working across all active zones
- Each step has an icon, brief description, and link to relevant page

#### Section 7: Interactive Demo Preview
- Embedded interactive demo component (see Section 4.2)
- **Headline:** "See AI Resolve a Ticket in 30 Seconds"
- Guided walkthrough showing a ticket entering → AI classifying → routing → resolution
- CTA: "Try the Full Interactive Demo →"

#### Section 8: Social Proof
- **Headline:** "Trusted by MSPs Who Demand More"
- 2–3 featured testimonials with name, title, company, photo
- Quantified results: "40 minutes saved per technician per day"
- Link to case studies

#### Section 9: Live Platform Metrics (optional — depends on data availability)
- Real-time or daily-refreshed metrics:
  - "Tickets triaged by AI today: X"
  - "Process areas active: Y"
  - "Compliance checks passed: Z"
- Animated counters with subtle glow effect

#### Section 10: Pricing Preview
- **Headline:** "Transparent Pricing for MSPs of Every Size"
- 3 tier cards (preview — not full detail):
  - Starter, Professional, Enterprise
  - Starting price + key differentiator for each
- CTA: "See Full Pricing →"
- Note: "Available on Azure Marketplace"

#### Section 11: Final CTA
- Full-width dark section with gradient border
- **Headline:** "Ready to Transform Your MSP?"
- Dual CTAs: "Start Free Evaluation" + "Talk to Our Team"
- Chatbot widget visible in corner as alternative contact method

**Layout:** Full-width sections, alternating between contained (1280px max) and edge-to-edge (for visual sections). Generous `--section-padding` between sections.

**SEO:**
- Title: "DevOps AI — AI-as-a-Service Platform for MSPs | 15 Zones, 157+ Process Areas"
- Meta description: "The AI operating system for Managed Service Providers. Automate ticket triage, compliance, security operations, and 157+ process areas across 15 zones. Deploy via Azure Marketplace."
- Structured data: Organization, WebSite, SoftwareApplication
- Open Graph + Twitter Card tags

### 3.2 Platform Overview (`platform.html`)

**Purpose:** Comprehensive overview of the platform's zone architecture, AI capabilities, and integration ecosystem. The "what we built" page.

**Audience:** Technical evaluators, IT Directors, vCIOs — people who need to understand the platform's scope.

**Content Sections:**

1. **Hero:** "15 Zones. 157+ Process Areas. One Platform."
   - Interactive zone architecture diagram (SVG-based, clickable)
   - Each zone node links to its zone page

2. **Zone Grid:** All 15 zones displayed in a categorized grid
   - Grouped by cluster: Service & Security, Operations, Business & Analytics, People & Legal, DevOps & Projects
   - Each zone card: icon, name, process area count, 1-line description
   - Click → zone page

3. **AI Capabilities:**
   - Inference Infrastructure (Azure OpenAI default, admin control plane)
   - Multi-Tenant Intelligence (3-tier branding isolation)
   - Role-Based AI Personalization (21 role-aware contexts)
   - Human-in-the-Loop Controls (every AI action has override/audit)

4. **Integration Ecosystem:**
   - PSA integrations (ConnectWise, Autotask, etc.)
   - RMM integrations
   - Identity providers (Entra ID, Google OIDC)
   - Azure services

5. **Architecture Preview:**
   - Simplified technical diagram
   - CTA: "See Full Architecture →"

6. **Screenshots Gallery:** Curated selection of the most impressive screenshots

**CTA Strategy:** "Start Free Evaluation" + "See Pricing"

### 3.3 Zone Pages (15 pages)

**Purpose:** Deep-dive into a specific operational zone. Each zone page serves as a landing page for visitors interested in that domain (e.g., someone Googling "MSP service desk automation").

**Audience:** Technical evaluators, practitioners, and decision-makers focused on this specific domain.

**Template Structure (applies to all 15 zone pages):**

1. **Hero:** Zone name + tagline + process area count
   - "Service Desk Zone — AI-Powered Ticket Intelligence"
   - "12 process areas working together to transform your help desk"
   - Background: Subtle zone-specific color accent

2. **Zone Overview:** 2–3 paragraphs explaining this zone's role in the platform

3. **Process Area Grid:** All process areas in this zone
   - Card for each PA: name, 1-line description, key metric/outcome
   - Click → process area page

4. **Key Screenshots:** 3–5 most compelling screenshots from this zone
   - Lightbox on click with full-resolution view and description

5. **Use Cases:** 2–3 scenario-based examples
   - "When a P1 ticket arrives at 2 AM..."
   - "When your client needs SOC 2 evidence for an audit..."

6. **Connected Roles:** Which roles primarily interact with this zone
   - Links to role pages

7. **Connected Zones:** How this zone integrates with others
   - Visual connection diagram (simplified from the 3D entry point)

8. **CTA:** "See [Zone Name] in Action" → demo + "Explore [Related Zone]" → next zone

**Zone List with Taglines:**

| Zone | Tagline | Process Areas |
|------|---------|--------------|
| Service Desk | AI-Powered Ticket Intelligence | 12 |
| Security Operations | Always-On Threat Defense | 13 |
| GRC & Compliance | Continuous Compliance Automation | 11 |
| Endpoint Management | Unified Device Intelligence | 10 |
| Network Ops | Predictive Network Operations | 9 |
| vC-Suite | Executive Intelligence & Advisory | 13 |
| Analytics | Cross-Zone Data Intelligence | 9 |
| Relationships | Client Success Automation | 11 |
| People | Workforce Intelligence | 8 |
| Learning | Knowledge & Skill Automation | 10 |
| Organization | Operational Governance | 11 |
| Legal | Legal Operations & Risk | 7 |
| DevOps | Platform Operations & CI/CD | 11 |
| Accounting | Financial Operations Intelligence | 11 |
| Projects | Project Intelligence & Execution | 11 |

### 3.4 Process Area Pages (157 pages)

**Purpose:** Granular technical deep-dive into a single process area. These pages serve both marketing (showing depth) and SEO (long-tail keyword capture) purposes.

**Audience:** Technical practitioners evaluating specific capabilities. Often arriving from search.

**Template Structure:**

1. **Breadcrumb:** Home > Platform > [Zone Name] > [Process Area Name]

2. **Hero:** Process area name + zone badge + brief description
   - "Ticket Ingestion & AI Triage"
   - Badge: "Service Desk Zone"
   - "Intelligent ticket classification and routing powered by NLP"

3. **Overview:** 2–3 paragraphs on what this process area does

4. **How It Works:** Step-by-step breakdown with numbered stages
   - Each stage: title, description, screenshot
   - Example for AI Triage: Ingest → Classify → Prioritize → Route → Monitor

5. **AI Capabilities:** What AI does in this process area
   - Specific model usage (NLP classification, predictive routing, etc.)
   - Human-in-the-loop checkpoints
   - Override/audit capabilities

6. **Screenshots:** 1–3 real platform screenshots of this PA in action
   - Lightbox with full-resolution view

7. **Key Metrics:** What outcomes this PA delivers
   - "70% of L1 tickets auto-resolved"
   - "3-second average classification time"

8. **Connected Process Areas:** Links to related PAs within the same zone and cross-zone

9. **Related Roles:** Who uses this PA most

10. **CTA:** "See [PA Name] in the Demo" + breadcrumb back to zone

**SEO:** Each PA page targets a specific long-tail keyword:
- Title: "[PA Name] — [Zone Name] | DevOps AI Platform"
- Structured data: SoftwareApplication with featureList

### 3.5 Role Journey Pages (21 pages)

**Purpose:** Persona-specific landing pages that show DevOps AI through the lens of a specific role. These are the most conversion-optimized pages — visitors who self-identify with a role are further down the funnel.

**Audience:** Individual practitioners who have identified themselves (or been identified via the journey entry point).

**Template Structure:**

1. **Hero:** Role name + persona-specific headline
   - Icon/illustration representing the role
   - "Project Manager — Ship On Time, Every Time"
   - "Service Delivery Manager — Own the Outcome, Not the Firefight"
   - Sub-headline from `ROLE_HERO_TEXT` (personalization.js)

2. **Day-in-the-Life:** "Your Day With DevOps AI"
   - Timeline visualization showing a typical day
   - Before (manual) vs. After (AI-assisted) comparison
   - Specific tasks automated, time saved per task

3. **Your Zones:** The 3 primary zones this role interacts with
   - Zone card with relevance explanation
   - "As a Project Manager, you'll spend most of your time in Projects, Service Desk, and Analytics"

4. **Key Process Areas:** The 5–8 most relevant PAs for this role
   - Brief description of how each PA helps THIS role specifically
   - Link to PA page for depth

5. **Screenshots:** Role-relevant screenshots (filtered from the 160+ available)

6. **Testimonial:** Role-specific quote from a practitioner

7. **CTA:** "Start Your [Role Name] Journey" → role-specific onboarding path

**CRITICAL: PM vs SDM Separation**
The Project Manager and Service Delivery Manager pages must clearly differentiate:

| Aspect | Project Manager | Service Delivery Manager |
|--------|----------------|--------------------------|
| Focus | Migration, deployment, timelines | Ongoing service quality, relationship |
| Cadence | Project-based (start → end) | Continuous (ongoing operations) |
| Key Metrics | On-time delivery, budget adherence | SLA compliance, CSAT, NPS |
| Key PAs | Phase-gated execution, migration workflows, project intelligence | SLA management, escalation handling, QBR delivery |
| Key Zones | Projects, Service Desk, Analytics | Service Desk, Analytics, Relationships |

### 3.6 Pricing Page (`pricing.html`)

**Purpose:** Transparent pricing for MSPs. No "Contact Sales" gatekeeping for standard tiers. Clear Azure Marketplace deployment path.

**Audience:** Decision-makers evaluating cost. Often visited multiple times before conversion.

**Content Sections:**

1. **Hero:** "Pricing That Scales With Your MSP"
   - Sub: "Transparent pricing. No surprises. Deploy via Azure Marketplace."

2. **Tier Cards:** 3 tiers displayed side-by-side
   - **Starter:** For MSPs starting their AI journey (1–3 technicians)
     - Core zones activated
     - Basic AI capabilities
     - Standard support
   - **Professional:** For growing MSPs (4–15 technicians) — MOST POPULAR badge
     - All 15 zones
     - Full AI capabilities
     - Priority support
     - Custom branding (MSP tier of 3-tier engine)
   - **Enterprise:** For large MSPs (15+ technicians)
     - Everything in Professional
     - Client-level branding (full 3-tier engine)
     - Dedicated success manager
     - Custom integrations
     - SLA guarantees

3. **Feature Comparison Table:** Expandable/collapsible
   - Organized by zone
   - Clear checkmarks/limits per tier
   - Sticky header on scroll

4. **FAQ:** Common pricing questions
   - "What about Enterprise packages?" → "Enterprise packages are available as separate Azure Marketplace listings with custom configurations."
   - "Can I switch tiers?" → "Yes, upgrade anytime..."
   - "Is there a free trial?" → "Yes, 14-day free evaluation..."

5. **Azure Marketplace Badge:** "Deploy in one click from Azure Marketplace"

6. **CTA:** "Start Free Evaluation" + "Talk to Sales for Custom Pricing"

**CRITICAL: No MSP/Enterprise Toggle.** Enterprise is a separate Azure Marketplace package, not a UI toggle. The pricing page shows MSP tiers only. Enterprise customers are directed to contact sales or the separate Marketplace listing.

### 3.7 Security & Trust Center (`security.html`)

**Purpose:** Centralized hub for all security, compliance, and data governance information. This page is a deal-breaker for enterprise MSP buyers — it must be comprehensive and transparent.

**Audience:** vCISOs, Compliance Officers, Security Analysts, IT Directors, and procurement teams running security questionnaires.

**Content Sections:**

1. **Hero:** "Security is Our Foundation, Not a Feature"
   - Trust badges: SOC 2 Type II, GDPR, data residency icons
   - Sub: "Enterprise-grade security architecture built for multi-tenant MSP operations"

2. **Security Architecture:**
   - Multi-tenant isolation diagram
   - Data flow visualization
   - Encryption at rest and in transit details
   - Network architecture (private endpoints, VNet integration)

3. **AI Governance:**
   - **Inference Infrastructure:** Azure OpenAI default (stays in Azure tenant, private endpoint, same VNet)
   - **Admin Control Plane:** Operators provide their own inference API key, can rotate/rate-limit/revoke
   - **Human-in-the-Loop:** Every AI action has override capability, audit trail, and escalation path
   - **Data Usage:** Clear statement on what data is/isn't used for model training
   - **3rd Party Fallback:** Admin/security/DevOps granular controls for non-Azure inference providers

4. **Compliance Certifications:**
   - Current certifications with badge + explanation + evidence link
   - Roadmap for upcoming certifications

5. **Data Residency:**
   - Where data is stored and processed
   - Region-specific deployment options
   - Subprocessor list

6. **Identity & Access:**
   - Multi-IDP auth (Entra ID, Google OIDC)
   - RBAC model overview
   - MFA enforcement
   - Privileged access management

7. **Incident Response:**
   - Public incident response process
   - Status page link
   - Responsible disclosure policy

8. **Downloadable Resources:**
   - Security whitepaper (PDF)
   - SOC 2 Type II report (gated — NDA required)
   - Data processing agreement template
   - Security questionnaire pre-fills

**CTA:** "Request Security Documentation" + "Schedule Security Review"

### 3.8 Architecture Page (`architecture.html`)

**Purpose:** Technical deep-dive for IT Directors, DevOps Engineers, vCIOs, and anyone evaluating the platform's technical foundation.

**Audience:** Technical decision-makers and evaluators.

**Content Sections:**

1. **Hero:** "Built on Azure. Engineered for Scale."

2. **Architecture Diagram:** Interactive SVG showing:
   - Azure infrastructure layer
   - Multi-tenant application layer
   - 3-tier branding engine
   - Inference infrastructure (InferenceRouter with Azure OpenAI)
   - Identity layer (Multi-IDP abstraction)
   - 15-zone process layer

3. **Technology Stack:**
   - Infrastructure: Azure (App Service, SQL, Storage, Key Vault, etc.)
   - Identity: Entra ID, Google OIDC, custom auth abstraction
   - AI: Azure OpenAI (default), InferenceRouter with fallback chain
   - Frontend: Branding provider, role-based UI adaptation

4. **Multi-Tenancy Architecture:**
   - Tenant isolation model
   - Data partitioning strategy
   - Performance isolation

5. **Integration Architecture:**
   - API-first design
   - Webhook system
   - PSA/RMM integration patterns
   - Identity federation

6. **Deployment Model:**
   - Azure Marketplace one-click deployment
   - Configuration automation
   - Update/upgrade process

**CTA:** "Deploy from Azure Marketplace" + "Request Architecture Briefing"

### 3.9 About / Company (`about.html`)

**Purpose:** RainTech story, mission, team, and why this platform exists.

**Audience:** Late-funnel evaluators, potential partners, media, prospective employees.

**Content Sections:**

1. **Hero:** "We're RainTech. We Build the Future of MSP Operations."
2. **Mission:** Why DevOps AI exists — the problem with MSP tool sprawl
3. **Team:** Key team members with photos and brief bios
4. **Timeline:** Company milestones and product evolution
5. **Values:** Engineering principles and company culture
6. **Careers:** Open positions or "We're hiring" section
7. **Contact:** Quick links to get in touch

### 3.10 Contact (`contact.html`)

**Purpose:** Multi-channel contact for sales, support, partnership, and general inquiries.

**Content Sections:**

1. **Hero:** "Let's Talk"
2. **Contact Form:** Multi-step form with inquiry type routing:
   - Sales inquiry → Collect company size, current tools, timeline
   - Support → Redirect to platform support portal
   - Partnership → Collect partnership type, company info
   - General → Open text field
3. **Direct Contact:** Email, phone (if applicable)
4. **Meeting Scheduler:** Embedded Calendly or similar
5. **Chatbot:** AI chatbot widget prominently featured as alternative

### 3.11 Azure Marketplace (`marketplace.html`)

**Purpose:** Deployment guide and getting-started tutorial for Azure Marketplace.

**Content Sections:**

1. **Hero:** "Deploy DevOps AI in Minutes"
2. **Prerequisites:** Azure subscription requirements, Entra ID setup
3. **Step-by-Step Guide:** Numbered deployment walkthrough with screenshots
4. **Post-Deployment:** Initial configuration checklist
5. **Support:** Where to get help during deployment
6. **CTA:** Link to Azure Marketplace listing

### 3.12 ROI Calculator (`roi.html`)

**Purpose:** Interactive tool that quantifies DevOps AI's value for a specific MSP.

**Audience:** MSP owners, finance coordinators, and anyone building a business case.

**Content Sections:**

1. **Hero:** "Calculate Your ROI"
2. **Calculator:** Interactive component (see Section 4.4)
3. **Methodology:** How the calculations work, industry benchmarks cited
4. **Case Studies:** Examples of real MSP ROI results
5. **CTA:** "See These Savings in Action → Book Demo"

### 3.13 Solutions Pages (`solutions.html` + sub-pages)

**Purpose:** Landing pages organized by industry vertical or business challenge.

**Audience:** Visitors who think in terms of problems, not product categories.

**Sub-pages (optional — can be sections on solutions.html initially):**
- By Challenge: "Reduce Ticket Volume," "Scale Without Hiring," "Automate Compliance"
- By Industry: "Healthcare MSPs," "Financial Services," "Government"

### 3.14 Blog / Resources Hub (`blog.html`)

**Purpose:** Thought leadership, SEO content, and resource library.

**Content Sections:**

1. **Hero:** "Insights for the AI-Powered MSP"
2. **Featured Post:** Large card with hero image
3. **Category Filters:** AI & Automation, MSP Operations, Security & Compliance, Platform Updates
4. **Post Grid:** Card layout with thumbnail, title, date, category, read time
5. **Newsletter Signup:** Inline email capture

**Note:** Blog posts will be individual HTML pages generated via a Python script from markdown source. The blog hub page is a static listing.

### 3.15 Login Redirect (`login.html`)

**Purpose:** Branded entry point that redirects to `platform.devops.ai.rain.tech`.

**Content:**
- DevOps AI logo + loading animation
- "Redirecting to your platform..."
- Auto-redirect via `<meta http-equiv="refresh">` and JavaScript
- Manual link if redirect fails
- MSP branding support (if accessed via custom subdomain)

### 3.16 Privacy Policy / Legal

**Purpose:** Legal compliance pages.

**Pages:**
- `legal/privacy.html` — Privacy Policy (existing, needs update)
- `legal/terms.html` — Terms of Service (NEW)
- `legal/acceptable-use.html` — Acceptable Use Policy (NEW)

**Format:** Clean typographic layout with table of contents, version dates, and expandable sections.

---

## Part 4: Interactive Components

### 4.1 AI Chatbot Widget

**Description:** Embedded AI chatbot available on all pages, powered by the platform's PUBLIC_CHATBOT_PROFILE.

**Technical Specification:**

| Aspect | Detail |
|--------|--------|
| Model | gpt-4o (via Azure OpenAI, through InferenceRouter) |
| Max Tokens | 1024 per response |
| Rate Limit | 30 RPM |
| Spend Cap | $50/month |
| Tools | None (public profile — no tool access) |
| Context | Website content, platform documentation, pricing info |
| Personality | Helpful, knowledgeable about DevOps AI, professional tone |

**UI Specification:**
- **Trigger:** Floating action button (FAB) in bottom-right corner
  - Glassmorphic circle with DevOps AI logo/chat icon
  - Subtle green glow pulse every 10s to attract attention
  - Badge showing "Ask AI" on first visit
- **Chat Panel:** Slides up from FAB on click
  - 400px wide, 500px tall (desktop)
  - Full-screen on mobile
  - Glassmorphic background matching site design
  - Message bubbles: user (right, accent background) + assistant (left, surface background)
  - Markdown rendering in responses
  - Typing indicator with animated dots
- **Header:** "DevOps AI Assistant" + minimize/close buttons
- **Input:** Text field with send button, placeholder "Ask about DevOps AI..."
- **Suggested Prompts:** On first open:
  - "What does DevOps AI do?"
  - "How does AI triage tickets?"
  - "What's included in each tier?"
  - "Is my data secure?"

**Admin Control Plane Requirement:**
The chatbot widget calls an API endpoint that is governed by the platform's admin control plane:
- MSP operator provides their own Azure OpenAI API key
- Operator can rotate, rate-limit, or revoke the key
- Usage metrics visible in admin dashboard
- Fallback behavior when key is invalid: graceful degradation to static FAQ

**Implementation Notes:**
- The chatbot widget is a self-contained JavaScript module
- API calls go to a lightweight proxy endpoint (Azure Function or similar) that applies rate limiting and key management
- For the static website, the proxy URL is configured via a `data-chatbot-endpoint` attribute on the script tag
- Fallback: If API is unavailable, show a static FAQ panel with common questions and answers

### 4.2 Interactive Product Demo

**Description:** Guided walkthrough of key DevOps AI workflows. Self-serve, ungated, embedded on the homepage and accessible from multiple CTAs throughout the site.

**Demo Scenarios:**

1. **"Watch AI Resolve a Ticket" (Primary — homepage embed)**
   - Ticket arrives in Service Desk
   - NLP classifies the issue (animated classification)
   - AI determines severity and assigns priority
   - Automated playbook executes resolution
   - Ticket resolved + notification sent
   - Duration: 60–90 seconds, self-paced with click-through steps

2. **"Compliance in Real-Time" (Security Center)**
   - CMMC control objective appears
   - System collects evidence automatically from connected tools
   - OSCAL document generated
   - Compliance dashboard updated
   - Duration: 45 seconds

3. **"Your MSP at a Glance" (Platform Overview)**
   - Executive KPI dashboard loads
   - Cross-zone analytics populate
   - AI generates weekly executive briefing
   - Role-specific views demonstrate personalization
   - Duration: 45 seconds

**Implementation:**
- Built as a custom HTML/CSS/JS component (no third-party demo tool required)
- Uses simulated data and animated screenshots
- Step-based progression with narration text, highlighted hotspots, and transitions
- Progress indicator showing current step / total steps
- Can be embedded inline (homepage) or opened in a lightbox
- Mobile-responsive: stacks vertically with swipe navigation

### 4.3 Journey Entry Point (Evolved 3D Experience)

**Description:** Evolution of the existing `entry-point.js` — the full-screen role selection experience. This is the signature interactive moment of the site.

**Evolution from Current:**

| Aspect | Current | Evolved |
|--------|---------|---------|
| 3D Visualization | Three.js force graph with sphere nodes | Refined with better aesthetics: glass-like nodes, animated connection pulses, ambient aurora |
| Card Grid Fallback | Basic cards in 5 groups | Glassmorphic cards with hover previews, animated zone connections |
| Role Selection | Click → detail panel → confirm | Click → expanded card with day-in-life preview → confirm with guided path suggestion |
| Mobile Experience | Simple card grid | Swipeable card carousel with category tabs |
| Performance | Full Three.js loaded for all desktop | Capability detection + progressive loading: CSS-only ambient background → 2D canvas → WebGL |
| Entry Trigger | Feature-flagged, shown on first visit | Smart trigger: shown on homepage for new visitors, available via "Find Your Role" CTA anywhere |

**21 Roles (Updated):**

```javascript
var ROLES = [
  // Executive Suite (5)
  { id: 'msp-owner', label: 'MSP Owner / CEO', group: 'executive' },
  { id: 'vcio', label: 'vCIO', group: 'executive' },
  { id: 'vciso', label: 'vCISO', group: 'executive' },
  { id: 'vcco', label: 'vCCO', group: 'executive' },
  { id: 'vcto', label: 'vCTO', group: 'executive' },
  
  // Operations (6)
  { id: 'it-director', label: 'IT Director', group: 'operations' },
  { id: 'service-delivery-manager', label: 'Service Delivery Manager', group: 'operations' },
  { id: 'project-manager', label: 'Project Manager', group: 'operations' },
  { id: 'service-desk-manager', label: 'Service Desk Manager', group: 'operations' },
  { id: 'network-engineer', label: 'Network Engineer', group: 'operations' },
  { id: 'devops-engineer', label: 'DevOps Engineer', group: 'operations' },
  
  // Security & Compliance (2)
  { id: 'security-analyst', label: 'Security Analyst', group: 'security' },
  { id: 'compliance-officer', label: 'Compliance Officer', group: 'security' },
  
  // Business & Relationships (5)
  { id: 'client-success-manager', label: 'Client Success Manager', group: 'business' },
  { id: 'finance-coordinator', label: 'Finance Coordinator', group: 'business' },
  { id: 'sales-director', label: 'Sales Director', group: 'business' },
  { id: 'marketing-director', label: 'Marketing Director', group: 'business' },
  { id: 'data-analyst', label: 'Data Analyst / BI Lead', group: 'business' },
  
  // People & Culture (3)
  { id: 'hr-director', label: 'HR Director', group: 'people' },
  { id: 'recruiter', label: 'Recruiter', group: 'people' },
  { id: 'legal-counsel', label: 'Legal Counsel', group: 'people' }
];
```

### 4.4 ROI Calculator

**Description:** Interactive calculator that takes MSP-specific inputs and calculates estimated savings and ROI from DevOps AI adoption.

**Inputs:**
- Number of technicians
- Average tickets per month
- Average ticket resolution time (minutes)
- Current tool costs (monthly)
- Number of managed endpoints
- Industry vertical (optional — adjusts benchmarks)

**Outputs:**
- Estimated time saved per technician per day
- Estimated tickets auto-resolved per month
- Estimated monthly cost savings
- ROI percentage (annual)
- Time to ROI (months)

**Visualization:**
- Animated bar chart comparing "Current State" vs. "With DevOps AI"
- Dollar savings counter
- "Share this report" → generates a URL with parameters

**Implementation:** Pure JavaScript calculator with pre-defined industry benchmarks. No server-side processing needed.

### 4.5 Live Metrics Display

**Description:** Real-time (or daily-refreshed) platform statistics displayed on the homepage and relevant pages.

**Metrics:**
- Total AI-assisted ticket resolutions (cumulative)
- Active zones across all tenants
- Compliance checks passed this month
- Average AI classification accuracy

**Implementation:**
- Fetches from a lightweight JSON API endpoint (Azure Function)
- Falls back to static "last known" values if API unavailable
- Animated number counters with `requestAnimationFrame`
- Updated every 60 seconds on the homepage

**If real-time data is not yet available:** Use static impressive numbers with a note "Platform statistics updated monthly" until the API is built.

### 4.6 Screenshot Lightbox

**Description:** Enhanced lightbox for viewing the 160+ platform screenshots in full resolution.

**Features:**
- Click any screenshot thumbnail → full-resolution overlay
- Glassmorphic backdrop (backdrop-filter: blur)
- Caption with screenshot description and zone/PA context
- Navigation arrows for browsing related screenshots
- Keyboard navigation (arrow keys, Escape to close)
- Pinch-to-zoom on mobile
- Lazy loading for all screenshot thumbnails

**Evolution from Current:** The current implementation is basic. The evolved version uses:
- `<dialog>` element for proper accessibility
- CSS-only backdrop blur (no JavaScript overlay management)
- Smooth scale-up animation from thumbnail position
- Share button (copies URL with anchor to specific screenshot)

### 4.7 Cookie Consent & Personalization System

**Description:** Evolution of the existing 4-layer GDPR-compliant consent and personalization system.

**Layers (retained from current):**
1. **Cookie Consent Banner** — Essential + Analytics + Personalization toggles
2. **Role Selection** — Via journey entry point or inline picker
3. **Journey Tracking** — Page visit tracking for returning visitors
4. **Personalized Content** — Welcome bar, role-specific hero text, recommended zones, personalized CTAs

**Evolution:**
- Consent banner redesigned with glassmorphic treatment
- Granular controls: expandable detail view showing exactly what each category tracks
- Consent state persisted to localStorage (not just cookies) for cross-page consistency
- Cookie policy link in footer always visible
- Re-consent mechanism if policy changes

**New Personalization Features:**
- **Lifecycle-aware CTAs:** Awareness visitors see "Learn More," Evaluation visitors see "Book Demo," Onboarding visitors see "Deploy Now"
- **Recent Activity Resume:** "Continue where you left off" section for returning visitors
- **Role-specific navigation highlighting:** Zone pages most relevant to selected role get a subtle indicator in nav

---

## Part 5: Design System Evolution

### 5.1 Evolved Design Tokens

The design tokens evolve from the current `base.css` while maintaining backward compatibility. All existing token names are preserved; new tokens are added.

```css
:root {
  /* ═══════════════════════════════════════════
     BRAND COLORS (retained)
     ═══════════════════════════════════════════ */
  --green-primary: #79C600;
  --green-bright: #8BDB02;
  --blue-cetacean: #001647;
  --blue-royal: #05108E;
  --blue-sky: #20BAE7;
  --white-ghost: #F7F7FF;
  --violet-bright: #C616EA;
  --gray: #97999B;
  --black: #000000;
  --cyan: #17E4ED;
  --blue-mid: #2272E0;

  /* ═══════════════════════════════════════════
     SEMANTIC COLORS — Dark Mode Default (evolved)
     ═══════════════════════════════════════════ */
  --bg-primary: #001647;
  --bg-secondary: #000E2E;         /* ← darker for more contrast */
  --bg-tertiary: #001a52;
  --bg-card: rgba(255, 255, 255, 0.05);      /* ← slightly more visible */
  --bg-card-hover: rgba(255, 255, 255, 0.10);  /* ← stronger hover */
  --bg-surface: #00204f;
  --bg-glass: rgba(0, 22, 71, 0.65);          /* NEW: glassmorphic surfaces */
  --bg-glass-light: rgba(255, 255, 255, 0.06); /* NEW: light glass */
  
  --text-primary: #F7F7FF;
  --text-secondary: rgba(247, 247, 255, 0.72);
  --text-tertiary: rgba(247, 247, 255, 0.48);
  --text-muted: rgba(247, 247, 255, 0.32);
  --text-accent: #8BDB02;                      /* NEW: accent-colored text */
  
  --border-default: rgba(255, 255, 255, 0.10);
  --border-strong: rgba(255, 255, 255, 0.20);
  --border-glass: rgba(255, 255, 255, 0.12);   /* NEW: glass borders */
  --border-glow: rgba(139, 219, 2, 0.3);       /* NEW: accent glow border */
  
  --accent: #8BDB02;
  --accent-hover: #79C600;
  --accent-glow: rgba(139, 219, 2, 0.15);
  --accent-glow-strong: rgba(139, 219, 2, 0.30); /* NEW */
  
  /* Status Colors (NEW) */
  --status-success: #8BDB02;
  --status-warning: #FFB347;
  --status-error: #FF4757;
  --status-info: #17E4ED;

  /* ═══════════════════════════════════════════
     GRADIENTS (evolved)
     ═══════════════════════════════════════════ */
  --gradient-hero: linear-gradient(135deg, #8BDB02 0%, #17E4ED 100%);
  --gradient-blue: linear-gradient(135deg, #05108E 0%, #001647 100%);
  --gradient-cyan: linear-gradient(135deg, #17E4ED 0%, #2272E0 100%);
  --gradient-royal: linear-gradient(135deg, #05108E 0%, #2272E0 100%);
  --gradient-violet: linear-gradient(135deg, #C616EA 0%, #5D24FC 100%);
  --gradient-ai: linear-gradient(90deg, #8BDB02, #17E4ED, #C616EA);  /* NEW: AI activity */
  --gradient-depth: radial-gradient(ellipse at 50% 0%, #05108E 0%, #001647 50%, #000E2E 100%); /* NEW */
  --gradient-surface: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%); /* NEW: card surface */

  /* ═══════════════════════════════════════════
     TYPOGRAPHY (retained + enhanced)
     ═══════════════════════════════════════════ */
  --font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace; /* NEW: code font */
  
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;

  /* Fluid Type Scale (retained) */
  --text-xs: clamp(0.694rem, 0.66rem + 0.17vw, 0.8rem);
  --text-sm: clamp(0.833rem, 0.78rem + 0.27vw, 1rem);
  --text-base: clamp(1rem, 0.93rem + 0.36vw, 1.2rem);
  --text-lg: clamp(1.2rem, 1.1rem + 0.5vw, 1.5rem);
  --text-xl: clamp(1.44rem, 1.3rem + 0.7vw, 1.875rem);
  --text-2xl: clamp(1.728rem, 1.53rem + 0.99vw, 2.344rem);
  --text-3xl: clamp(2.074rem, 1.79rem + 1.42vw, 2.93rem);
  --text-4xl: clamp(2.488rem, 2.08rem + 2.04vw, 3.66rem);
  --text-hero: clamp(2.986rem, 2.4rem + 2.93vw, 4.58rem);

  /* Letter Spacing (NEW) */
  --tracking-tight: -0.03em;
  --tracking-normal: -0.02em;
  --tracking-wide: 0.05em;
  --tracking-caps: 0.1em;

  /* ═══════════════════════════════════════════
     SPACING (retained)
     ═══════════════════════════════════════════ */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-20: 5rem;
  --space-24: 6rem;
  --space-32: 8rem;

  /* ═══════════════════════════════════════════
     LAYOUT (retained + enhanced)
     ═══════════════════════════════════════════ */
  --max-width: 1280px;
  --max-width-narrow: 960px;
  --max-width-wide: 1440px;
  --gutter: clamp(1rem, 3vw, 2rem);
  --section-padding: clamp(4rem, 8vw, 8rem);
  --section-padding-sm: clamp(2rem, 4vw, 4rem);  /* NEW: tighter sections */

  /* ═══════════════════════════════════════════
     RADIUS (retained + enhanced)
     ═══════════════════════════════════════════ */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-2xl: 32px;  /* NEW: extra large for hero cards */
  --radius-full: 9999px;

  /* ═══════════════════════════════════════════
     SHADOWS (retained + glassmorphic additions)
     ═══════════════════════════════════════════ */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.4);
  --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.5);   /* NEW */
  --shadow-glow: 0 0 40px rgba(139, 219, 2, 0.15);
  --shadow-glow-strong: 0 0 60px rgba(139, 219, 2, 0.25); /* NEW */
  --shadow-glass: 0 8px 32px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.05); /* NEW */

  /* ═══════════════════════════════════════════
     GLASSMORPHISM TOKENS (NEW)
     ═══════════════════════════════════════════ */
  --glass-blur: 12px;
  --glass-blur-heavy: 24px;
  --glass-bg: rgba(0, 22, 71, 0.65);
  --glass-bg-light: rgba(255, 255, 255, 0.06);
  --glass-border: 1px solid rgba(255, 255, 255, 0.12);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);

  /* ═══════════════════════════════════════════
     TRANSITIONS (retained + enhanced)
     ═══════════════════════════════════════════ */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);  /* NEW: spring easing */
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 400ms;
  --duration-slower: 600ms;  /* NEW */

  /* ═══════════════════════════════════════════
     Z-INDEX (retained)
     ═══════════════════════════════════════════ */
  --z-header: 100;
  --z-dropdown: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-chatbot: 500;  /* NEW: chatbot always on top */
  --z-toast: 600;    /* NEW */
}
```

### 5.2 Component Library Specification

**Core Components:**

| Component | Purpose | CSS Class | Key Properties |
|-----------|---------|-----------|----------------|
| `.btn` | Primary action button | `.btn--primary`, `.btn--secondary`, `.btn--ghost` | Green fill, white text, 44px min-height, `--radius-full` |
| `.btn--primary` | Main CTA | — | `background: var(--accent)`, `color: var(--blue-cetacean)`, glow on hover |
| `.btn--secondary` | Secondary action | — | Outlined, `border: 1px solid var(--accent)`, transparent bg |
| `.btn--ghost` | Subtle action | — | No border, text-only, accent color, underline on hover |
| `.card` | Content container | `.card--glass`, `.card--solid` | Glassmorphic or solid surface, `--radius-lg`, hover lift |
| `.card--glass` | Glassmorphic card | — | `backdrop-filter: blur(var(--glass-blur))`, glass border, glass shadow |
| `.badge` | Label/tag | `.badge--zone`, `.badge--role`, `.badge--status` | Pill shape, `--radius-full`, small text, accent background |
| `.section` | Page section | `.section--dark`, `.section--gradient` | `padding-block: var(--section-padding)` |
| `.hero` | Page hero | `.hero--home`, `.hero--page`, `.hero--zone` | Full-viewport height or auto, gradient background |
| `.grid` | Layout grid | `.grid--bento`, `.grid--cards`, `.grid--zones` | CSS Grid, responsive, gap tokens |
| `.nav` | Navigation | `.nav--primary`, `.nav--mega`, `.nav--footer` | Sticky header, glassmorphic on scroll |
| `.lightbox` | Image overlay | — | `<dialog>` element, backdrop blur, keyboard nav |
| `.metric` | Stat display | `.metric--counter`, `.metric--static` | Large number + label, count-up animation |
| `.breadcrumb` | Navigation path | — | Semantic `<nav>` with `aria-label="Breadcrumb"` |
| `.testimonial` | Customer quote | — | Photo, name, title, company, quote text |
| `.screenshot` | Platform screenshot | `.screenshot--framed`, `.screenshot--float` | Device frame, glassmorphic border, lightbox on click |
| `.chatbot` | Chat widget | `.chatbot--fab`, `.chatbot--panel` | FAB trigger + slide-up panel |
| `.consent` | Cookie banner | — | Bottom-fixed, glassmorphic, toggles for each category |
| `.toast` | Notification | — | Top-right, auto-dismiss, `aria-live="polite"` |
| `.accordion` | Expandable content | — | `<details>`/`<summary>`, smooth height animation |
| `.tabs` | Tab interface | — | Horizontal tabs, `role="tablist"`, keyboard nav |
| `.code` | Code block | — | Monospace font, syntax highlighting colors, copy button |

### 5.3 Responsive Breakpoints

```css
/* Mobile-first: no media query = mobile default */

/* Tablet */
@media (min-width: 640px) { /* --bp-sm */ }

/* Tablet landscape / small desktop */
@media (min-width: 768px) { /* --bp-md */ }

/* Desktop */
@media (min-width: 1024px) { /* --bp-lg */ }

/* Large desktop */
@media (min-width: 1280px) { /* --bp-xl */ }

/* Extra large */
@media (min-width: 1440px) { /* --bp-2xl */ }
```

**Layout Behavior:**
- Mobile (< 640px): Single column, stacked sections, hamburger nav, full-width cards
- Tablet (640–1023px): Two-column grids where appropriate, abbreviated nav
- Desktop (1024+): Full layout, mega-menu nav, multi-column grids, glassmorphic effects
- Large (1280+): Max-width containers, increased spacing, 3D entry point available

### 5.4 Dark/Light Mode Strategy

**Dark mode is the default and primary experience.** The site is designed dark-first because:
1. Technical/MSP audiences expect dark interfaces (Linear, GitHub, VS Code)
2. The existing brand (cetacean blue) is inherently dark
3. Glassmorphic effects look dramatically better on dark backgrounds
4. Screenshots pop against dark backgrounds

**Light mode is available** as an opt-in toggle (sun/moon icon in header). The existing `[data-theme="light"]` tokens are preserved and enhanced.

**System preference detection:**
```css
@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    /* Apply light mode tokens */
  }
}
```

**Priority:** `data-theme` attribute > System preference > Default (dark)

### 5.5 Icon System

**Approach:** SVG icons, inline where possible, with CSS `currentColor` for theme compatibility.

**Icon Sources:**
- Custom SVG icons for zone and role representations (designed to match the brand)
- Lucide Icons (MIT license) for UI elements (arrows, chevrons, close, search, etc.)
- Loaded as inline SVG — no icon font dependency, no external requests

**Icon Sizing:**
- Small (16px): inline text, breadcrumbs
- Medium (20px): buttons, navigation
- Large (24px): cards, feature lists
- Hero (32–48px): section headers, zone icons

### 5.6 Image/Screenshot Treatment

**Screenshot Display Modes:**

1. **Framed:** Screenshot inside a browser/device mockup frame
   - Glassmorphic frame with subtle gradient border
   - Appropriate for hero sections and feature showcases

2. **Floating:** Screenshot with rounded corners, shadow, and slight rotation
   - Parallax on scroll (subtle, 5–10px range)
   - Appropriate for in-content placement

3. **Inline:** Screenshot at full width within content flow
   - Rounded corners (`--radius-lg`)
   - Click-to-lightbox
   - Caption below with zone/PA context

4. **Grid:** Multiple screenshots in a bento or masonry layout
   - Click any for lightbox
   - Appropriate for zone and PA pages

**Image Optimization:**
- All screenshots served as WebP with PNG fallback
- Lazy loading via `loading="lazy"` attribute
- Responsive images via `srcset` and `sizes` attributes
- Blur-up placeholder (low-res base64 inline) for LCP-critical images
- Maximum width: 1200px (2x for retina displays)

---

## Part 6: Technical Architecture

### 6.1 Static Site Architecture

**The site MUST remain a static site on GitHub Pages.** No framework migration, no build step required for deployment.

```
devops-ai-website/
├── index.html
├── platform.html
├── pricing.html
├── security.html
├── architecture.html
├── solutions.html
├── roi.html
├── marketplace.html
├── about.html
├── contact.html
├── blog.html
├── login.html
├── why-devops-ai.html
├── 404.html
│
├── css/
│   ├── base.css              ← Reset + design tokens (evolved from current)
│   ├── components.css        ← Component library (NEW)
│   ├── layout.css            ← Header, footer, nav, grid system (replaces parts of style.css)
│   ├── pages.css             ← Page-specific styles (replaces parts of style.css)
│   ├── animations.css        ← All animation definitions (NEW — extracted from enhancements.css)
│   └── personalization.css   ← Consent, role picker, entry point (evolved from current)
│
├── js/
│   ├── app.js                ← Core: theme toggle, mobile nav, scroll animations, lazy loading
│   ├── components/
│   │   ├── chatbot.js        ← AI chatbot widget (NEW)
│   │   ├── demo.js           ← Interactive product demo (NEW)
│   │   ├── roi-calculator.js ← ROI calculator logic (evolved from current)
│   │   ├── lightbox.js       ← Screenshot lightbox (NEW — extracted/enhanced)
│   │   ├── metrics.js        ← Live metrics display (NEW)
│   │   └── counter.js        ← Animated number counters (NEW)
│   ├── personalization.js    ← Cookie consent + role selection + journey tracking (evolved)
│   └── entry-point.js        ← 3D/card grid role selection (evolved)
│
├── roles/                    ← 21 role pages + index
├── zones/                    ← 15 zone directories with process area sub-pages
├── legal/                    ← Privacy, terms, acceptable use
├── docs/                     ← Documentation assets
│
├── assets/
│   ├── screenshots/          ← 160+ platform screenshots (preserved)
│   ├── icons/                ← SVG icon files (NEW)
│   ├── images/               ← General images (logos, illustrations) (NEW)
│   └── fonts/                ← Plus Jakarta Sans + JetBrains Mono (self-hosted) (NEW)
│
├── CNAME                     ← devops.ai.rain.tech (preserved)
├── sitemap.xml               ← Auto-generated sitemap
├── robots.txt
├── llms.txt                  ← AI/LLM discoverability file (NEW)
├── manifest.json             ← PWA manifest (NEW — optional)
└── scripts/
    ├── generate-pa-pages.py  ← Python: generates process area HTML from template + data
    ├── generate-sitemap.py   ← Python: generates sitemap.xml from file system
    └── optimize-images.py    ← Python: converts screenshots to WebP, generates srcsets
```

### 6.2 CSS Architecture

**File Structure (6 files, loaded in order):**

```html
<!-- Critical: inline in <head> for LCP -->
<style>
  /* Inlined: design tokens + above-the-fold hero styles (~2KB) */
</style>

<!-- Non-critical: loaded async -->
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/layout.css">
<link rel="stylesheet" href="css/components.css">
<link rel="stylesheet" href="css/pages.css">
<link rel="stylesheet" href="css/animations.css" media="(prefers-reduced-motion: no-preference)">
<link rel="stylesheet" href="css/personalization.css">
```

**Key Principles:**
- CSS custom properties for all values (theming, responsive adjustments)
- No CSS preprocessor required — vanilla CSS with custom properties is sufficient
- CSS nesting (native, supported in all modern browsers) for component scoping
- `@layer` for cascade management: `@layer reset, tokens, layout, components, pages, utilities`
- `animation.css` loaded conditionally — only when user hasn't requested reduced motion
- No `!important` except for accessibility overrides

### 6.3 JavaScript Architecture

**Loading Strategy:**

```html
<!-- In <head> — critical path -->
<script>
  // Inline: theme detection, consent check (~500 bytes)
  (function() {
    var theme = localStorage.getItem('devopsai-theme');
    if (theme) document.documentElement.setAttribute('data-theme', theme);
    else if (window.matchMedia('(prefers-color-scheme: light)').matches) {
      document.documentElement.setAttribute('data-theme', 'light');
    }
  })();
</script>

<!-- At end of <body> — non-blocking -->
<script src="js/app.js" defer></script>
<script src="js/personalization.js" defer></script>

<!-- Lazy-loaded components (only on pages that need them) -->
<!-- Loaded dynamically by app.js when elements are detected in DOM -->
```

**Module Loading Pattern:**

`app.js` acts as the entry point and lazy-loads components based on DOM presence:

```javascript
// app.js — Core initialization
(function() {
  'use strict';

  // 1. Scroll-driven animations (CSS handles most, JS for IntersectionObserver fallback)
  // 2. Mobile navigation toggle
  // 3. Theme toggle
  // 4. Lazy image loading (native + fallback)
  // 5. Component detection and lazy loading:

  // If chatbot mount point exists, load chatbot.js
  if (document.querySelector('[data-chatbot]')) {
    import('./components/chatbot.js');
  }

  // If demo mount point exists, load demo.js
  if (document.querySelector('[data-demo]')) {
    import('./components/demo.js');
  }

  // If ROI calculator exists, load calculator.js
  if (document.querySelector('[data-roi-calculator]')) {
    import('./components/roi-calculator.js');
  }

  // If lightbox triggers exist, load lightbox.js
  if (document.querySelector('[data-lightbox]')) {
    import('./components/lightbox.js');
  }

  // If metric counters exist, load counter.js
  if (document.querySelector('[data-counter]')) {
    import('./components/counter.js');
  }

  // If live metrics exist, load metrics.js
  if (document.querySelector('[data-live-metrics]')) {
    import('./components/metrics.js');
  }
})();
```

**Progressive Enhancement:**
- All content readable without JavaScript
- CSS handles scroll animations where `animation-timeline: view()` is supported
- JavaScript provides fallback IntersectionObserver for browsers without CSS scroll timeline support
- Interactive components (chatbot, demo, calculator) are enhancements — page works without them

### 6.4 Performance Budget

| Metric | Target | Measurement |
|--------|--------|-------------|
| LCP | < 2.5s | 75th percentile, Lighthouse mobile |
| CLS | < 0.1 | 75th percentile |
| INP | < 200ms | 75th percentile |
| Total Page Weight | < 500KB (initial load, excluding screenshots) | Homepage |
| CSS Total | < 80KB (all files combined) | Uncompressed |
| JS Total | < 60KB (initial load, before lazy components) | Uncompressed |
| Font Files | < 100KB | Plus Jakarta Sans subset + JetBrains Mono subset |
| Time to Interactive | < 3.5s | Mobile 4G (Lighthouse) |
| First Byte (TTFB) | < 800ms | GitHub Pages via Fastly CDN |

**Optimization Techniques:**
- Critical CSS inlined in `<head>` (~2KB)
- Fonts: self-hosted, subset to Latin characters, `font-display: swap`
- Images: WebP format, lazy loading, responsive `srcset`
- JavaScript: `defer` for all scripts, dynamic `import()` for components
- `<link rel="preconnect">` for CDN domains
- `<link rel="preload">` for hero image and primary font
- No render-blocking third-party scripts
- Brotli/Gzip compression (GitHub Pages handles this via Fastly)

### 6.5 SEO Strategy

**Foundation (enhanced from current):**

1. **Structured Data (JSON-LD):**
   - `Organization` — RainTech company info
   - `WebSite` — with SearchAction for site search
   - `SoftwareApplication` — DevOps AI platform
   - `BreadcrumbList` — on all interior pages
   - `FAQPage` — on pricing and security pages
   - `Article` — on blog posts
   - `creator` attribution: `{ "@type": "SoftwareApplication", "name": "Perplexity Computer", "url": "https://www.perplexity.ai/computer" }`

2. **Sitemap:** Auto-generated via Python script, submitted to Google Search Console

3. **Meta Tags:**
   - Unique title and description for every page
   - Open Graph tags for social sharing
   - Twitter Card tags
   - Canonical URLs
   - `hreflang` if multi-language is planned

4. **`llms.txt` (NEW):**
   - Machine-readable file describing the site's content and structure
   - Helps AI systems (ChatGPT, Gemini, Perplexity, etc.) discover and understand the platform
   - Located at `/llms.txt`

   ```
   # DevOps AI
   > AI-as-a-Service platform for Managed Service Providers

   ## Platform
   - 15 operational zones
   - 157+ process areas
   - 21 role-based journeys
   - Multi-tenant, 3-tier branding
   - Azure OpenAI inference infrastructure

   ## Docs
   - [Platform Overview](https://devops.ai.rain.tech/platform.html)
   - [Architecture](https://devops.ai.rain.tech/architecture.html)
   - [Security & Trust](https://devops.ai.rain.tech/security.html)
   - [Pricing](https://devops.ai.rain.tech/pricing.html)
   - [All Zones](https://devops.ai.rain.tech/zones/)
   - [All Roles](https://devops.ai.rain.tech/roles/)
   ```

5. **Internal Linking:**
   - Every PA page links to its parent zone and related PAs
   - Every zone page links to connected roles
   - Every role page links to relevant zones and PAs
   - Breadcrumbs on all interior pages
   - "Related" sections at the bottom of content pages

6. **Technical SEO:**
   - Clean URL structure (no query parameters for navigation)
   - 404 page with search and navigation
   - Redirect map for any URL changes from current site
   - Image alt text on all screenshots
   - `<html lang="en">` on all pages

### 6.6 Build/Deploy Pipeline

**Development Workflow:**

```
1. Edit HTML/CSS/JS directly
2. Run Python generation scripts (if PA pages or sitemap changed):
   $ python scripts/generate-pa-pages.py    # Generates process area HTML
   $ python scripts/generate-sitemap.py     # Generates sitemap.xml
   $ python scripts/optimize-images.py      # Converts images to WebP
3. Preview locally (any static file server):
   $ python -m http.server 8000
4. Commit to full-site-backup branch
5. Merge to main → GitHub Pages auto-deploys
```

**No build step required for deployment.** The Python scripts are development-time tools only. The deployed site is pure HTML/CSS/JS.

**CI (optional — GitHub Actions):**
- Run `generate-sitemap.py` on push to ensure sitemap is current
- Run Lighthouse CI for performance regression detection
- HTML validation via `html5-validator`
- Accessibility checks via `axe-core`

---

## Part 7: FR Decomposition for Parallel Orchestration

### Wave Structure Overview

```
Wave 1: Foundation ──────────────── (must complete first)
  FR-W01: Design System
  FR-W02: Shared Templates
  FR-W03: JS Infrastructure
            │
            ├──── Wave 2: Core Pages ────── (parallel, after Wave 1)
            │       FR-W04: Homepage
            │       FR-W05: Platform Overview
            │       FR-W06: Pricing
            │       FR-W07: Security & Trust
            │       FR-W08: Architecture
            │
            ├──── Wave 3: Role Pages ────── (parallel, after Wave 1)
            │       FR-W09: Executive Suite
            │       FR-W10: Operations
            │       FR-W11: Security & Compliance
            │       FR-W12: Business & Relationships
            │       FR-W13: People & Culture
            │
            ├──── Wave 4: Zone Pages ────── (parallel, after Wave 1)
            │       FR-W14: Service/Security/Compliance zones
            │       FR-W15: Operations/Network/Endpoint zones
            │       FR-W16: Business/Analytics/vC-Suite zones
            │       FR-W17: People/Learning/Org/Legal zones
            │       FR-W18: DevOps/Accounting/Projects zones
            │       FR-W19: PA page template + generation script
            │
            └──── Wave 5: Interactive ───── (start after Wave 1, integrate after Wave 2)
                    FR-W20: AI Chatbot
                    FR-W21: Journey Entry Point
                    FR-W22: Interactive Demo
                    FR-W23: ROI Calculator
                    FR-W24: Personalization evolution
                          │
                          └──── Wave 6: Polish ── (final pass)
                                  FR-W25: Secondary pages
                                  FR-W26: SEO optimization
                                  FR-W27: Performance & accessibility
```

---

### FR-W01: Design System Evolution

**ID:** FR-W01  
**Title:** Design System Evolution — Tokens, Reset, Glassmorphism, Component CSS  
**Wave:** 1 (Foundation)  
**Estimated Complexity:** L  
**Dependencies:** None  

**Description:**  
Evolve the existing `base.css` design tokens and create the component CSS library. This is the foundation all other FRs build on. Must preserve all existing token names while adding glassmorphism tokens, animation tokens, status colors, and the new component classes.

**Files to Create/Modify:**
- `css/base.css` — Evolved from root `/base.css` (add new tokens, preserve existing)
- `css/components.css` — NEW: full component library (buttons, cards, badges, metrics, etc.)
- `css/animations.css` — NEW: all animation keyframes and scroll-driven animation definitions
- `assets/fonts/` — Self-host Plus Jakarta Sans and JetBrains Mono (WOFF2 subset files)

**Acceptance Criteria:**
- [ ] All existing `base.css` token names preserved (backward compatible)
- [ ] New tokens added per Section 5.1 (glassmorphism, AI gradient, status colors, etc.)
- [ ] Glassmorphic card component renders correctly on dark background
- [ ] All buttons (primary, secondary, ghost) styled per spec
- [ ] Badge, metric, breadcrumb, accordion, tabs components implemented
- [ ] Fonts self-hosted with `font-display: swap`
- [ ] `animations.css` conditional on `prefers-reduced-motion: no-preference`
- [ ] CSS passes validation (no errors)
- [ ] All color combinations meet WCAG 2.2 AA contrast ratios
- [ ] `@layer` ordering: reset, tokens, layout, components, pages, utilities
- [ ] Light mode tokens updated in `[data-theme="light"]`
- [ ] Total CSS size: `base.css` < 15KB, `components.css` < 30KB, `animations.css` < 15KB

---

### FR-W02: Shared Page Template & Layout

**ID:** FR-W02  
**Title:** Shared Page Template — Header, Footer, Navigation, Layout Grid  
**Wave:** 1 (Foundation)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01  

**Description:**  
Create the shared header, footer, mega-menu navigation, and layout system that all pages use. The header must be glassmorphic-on-scroll, include the mega-menu dropdowns (Platform, Solutions, Resources), and the mobile hamburger nav. The footer must include the full navigation structure per Section 2.2.

**Files to Create/Modify:**
- `css/layout.css` — NEW: header, footer, nav, grid system, section utilities
- `_template.html` — NEW: reference template showing the complete page shell (header + main + footer). Not deployed; used as copy-paste source by other FRs.
- `404.html` — NEW: custom 404 page using the shared template

**Acceptance Criteria:**
- [ ] Header: sticky, glassmorphic on scroll (`backdrop-filter: blur` after 50px scroll)
- [ ] Header: DevOps AI logo (SVG inline), primary nav items, Login + Get Started CTAs
- [ ] Mega-menu: Platform, Solutions, Resources dropdowns with content per Section 2.2
- [ ] Mobile nav: hamburger toggle, full-screen overlay, accordion sections
- [ ] Footer: 5-column layout per Section 2.2, responsive to single column on mobile
- [ ] Footer: Perplexity Computer attribution link
- [ ] Skip-to-content link (existing — preserved and styled)
- [ ] Grid system: `.container`, `.container--narrow`, `.container--wide` preserved
- [ ] Grid system: `.grid--bento`, `.grid--cards`, `.grid--zones` responsive layouts
- [ ] Breadcrumb component: `<nav aria-label="Breadcrumb">` with schema.org markup
- [ ] 404 page: friendly message, search suggestion, popular links
- [ ] Template validates as accessible (axe-core, no violations)
- [ ] Mobile nav: all touch targets ≥ 44px

---

### FR-W03: JavaScript Infrastructure

**ID:** FR-W03  
**Title:** JavaScript Infrastructure — App Core, Lazy Loading, Theme, Scroll Animations  
**Wave:** 1 (Foundation)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02  

**Description:**  
Create the core `app.js` that handles theme toggling, mobile navigation, scroll-triggered animations (with fallback for browsers without CSS scroll timeline), lazy image loading, and dynamic component loading. This is the JavaScript entry point that all pages load.

**Files to Create/Modify:**
- `js/app.js` — NEW: core application JavaScript
- `js/components/counter.js` — NEW: animated number counter component
- `js/components/lightbox.js` — NEW: screenshot lightbox using `<dialog>`

**Acceptance Criteria:**
- [ ] Theme toggle: toggles `data-theme` attribute, persists to localStorage
- [ ] Mobile nav: opens/closes hamburger menu, traps focus, closes on Escape
- [ ] Scroll animations: detects `[data-animate]` elements, adds `.is-visible` on scroll entry
- [ ] Scroll animations: uses CSS `animation-timeline: view()` where supported, IntersectionObserver fallback
- [ ] Lazy loading: dynamic `import()` for components based on DOM presence (chatbot, demo, etc.)
- [ ] Counter: counts up from 0 to target value over 1500ms, triggered by IntersectionObserver
- [ ] Lightbox: `<dialog>` element, backdrop blur, keyboard nav (arrows, Escape), pinch-to-zoom
- [ ] All JS uses strict mode and IIFE pattern (no global pollution)
- [ ] `app.js` < 15KB uncompressed, no external dependencies
- [ ] Progressive enhancement: all pages functional without JavaScript

---

### FR-W04: Homepage Redesign

**ID:** FR-W04  
**Title:** Homepage — Complete Redesign  
**Wave:** 2 (Core Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Complete redesign of `index.html` per Section 3.1. The homepage is the most important page — it must communicate the platform's scope, differentiation, and value in under 5 seconds.

**Files to Create/Modify:**
- `index.html` — MODIFY: complete rewrite of page content
- `css/pages.css` — MODIFY: add homepage-specific styles (hero, bento grid, trust bar, etc.)

**Acceptance Criteria:**
- [ ] Hero: headline, rotating sub-headline (CSS animation or JS), product screenshot, dual CTAs
- [ ] Hero: neural network particle background (subtle, CSS canvas or inline SVG animation)
- [ ] Trust bar: logo row (grayscale → color on hover) + metrics bar with counters
- [ ] Problem/Solution: 3-column cards linking to relevant zones
- [ ] Product Showcase: bento grid with 6–8 screenshots, Active Grid hover expansion
- [ ] Role-Based Paths: 5 category cards with role lists
- [ ] How It Works: 3-step visual flow
- [ ] Social Proof: testimonials section (placeholder content acceptable if real quotes unavailable)
- [ ] Pricing Preview: 3 tier cards with CTA to pricing page
- [ ] Final CTA: full-width section with dual CTAs
- [ ] All sections use `[data-animate]` for scroll-triggered reveals
- [ ] Responsive: all sections work at 375px, 768px, 1280px+
- [ ] LCP < 2.5s (hero image preloaded, critical CSS inlined)
- [ ] SEO: title, meta description, structured data (Organization, WebSite, SoftwareApplication)

---

### FR-W05: Platform Overview Page

**ID:** FR-W05  
**Title:** Platform Overview Page  
**Wave:** 2 (Core Pages)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Redesign `platform.html` per Section 3.2. Comprehensive overview of the 15-zone architecture, AI capabilities, and integration ecosystem.

**Files to Create/Modify:**
- `platform.html` — MODIFY: complete rewrite
- `css/pages.css` — MODIFY: add platform page styles

**Acceptance Criteria:**
- [ ] Hero with zone architecture count (15 zones, 157+ PAs)
- [ ] Interactive zone grid: all 15 zones displayed with process area counts
- [ ] Zone grid grouped by cluster with clear visual hierarchy
- [ ] AI Capabilities section: 4 capability cards (inference, multi-tenant, role-based, HITL)
- [ ] Integration ecosystem section
- [ ] Architecture preview with CTA to architecture.html
- [ ] Screenshot gallery section
- [ ] All zones link to their zone pages
- [ ] Responsive and accessible

---

### FR-W06: Pricing Page

**ID:** FR-W06  
**Title:** Pricing Page  
**Wave:** 2 (Core Pages)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Redesign `pricing.html` per Section 3.6. Three MSP tiers, no Enterprise toggle, feature comparison table.

**Files to Create/Modify:**
- `pricing.html` — MODIFY: complete rewrite (or NEW if not existing)
- `css/pages.css` — MODIFY: add pricing page styles

**Acceptance Criteria:**
- [ ] 3 tier cards: Starter, Professional (MOST POPULAR), Enterprise
- [ ] Each tier: price (or "Contact Sales" for Enterprise), key features, CTA
- [ ] Feature comparison table: expandable/collapsible sections organized by zone
- [ ] Sticky header on comparison table during scroll
- [ ] FAQ section with accordion
- [ ] Azure Marketplace badge/link
- [ ] No MSP/Enterprise toggle — note about separate Marketplace package for Enterprise
- [ ] Responsive: tier cards stack on mobile
- [ ] SEO: FAQPage structured data

---

### FR-W07: Security & Trust Center

**ID:** FR-W07  
**Title:** Security & Trust Center  
**Wave:** 2 (Core Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Redesign `security.html` per Section 3.7. Comprehensive security, compliance, AI governance, and data residency information.

**Files to Create/Modify:**
- `security.html` — MODIFY: complete rewrite
- `css/pages.css` — MODIFY: add security page styles

**Acceptance Criteria:**
- [ ] Hero with trust badges (SOC 2, GDPR icons)
- [ ] Security architecture section: multi-tenant isolation diagram (SVG)
- [ ] AI Governance section: InferenceRouter, admin control plane, HITL, data usage
- [ ] Compliance certifications section with badge + explanation
- [ ] Data residency section with region information
- [ ] Identity & access section: Multi-IDP auth, RBAC, MFA
- [ ] Incident response process section
- [ ] Downloadable resources section (gated and ungated)
- [ ] All diagrams accessible (alt text, `aria-label`)
- [ ] Responsive layout
- [ ] SEO: Organization structured data with compliance info

---

### FR-W08: Architecture Page

**ID:** FR-W08  
**Title:** Technical Architecture Page  
**Wave:** 2 (Core Pages)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Redesign `architecture.html` per Section 3.8. Technical deep-dive with architecture diagrams.

**Files to Create/Modify:**
- `architecture.html` — MODIFY: complete rewrite
- `css/pages.css` — MODIFY: add architecture page styles

**Acceptance Criteria:**
- [ ] Hero: "Built on Azure. Engineered for Scale."
- [ ] Interactive architecture diagram (clickable SVG)
- [ ] Technology stack section
- [ ] Multi-tenancy architecture section
- [ ] Integration architecture section
- [ ] Deployment model section (Azure Marketplace)
- [ ] Code/API examples where relevant (using `--font-mono`)
- [ ] Responsive diagrams (stack or scroll on mobile)

---

### FR-W09: Role Journey Pages — Executive Suite

**ID:** FR-W09  
**Title:** Role Pages — MSP Owner, vCIO, vCISO, vCCO, vCTO  
**Wave:** 3 (Journey & Role Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Create/redesign 5 role journey pages for the Executive Suite group plus the roles index page.

**Files to Create/Modify:**
- `roles/index.html` — MODIFY: complete rewrite (all-roles overview with 5 groups)
- `roles/msp-owner.html` — MODIFY: complete rewrite per role template (Section 3.5)
- `roles/vcio.html` — MODIFY: complete rewrite
- `roles/vciso.html` — MODIFY: complete rewrite
- `roles/vcco.html` — MODIFY: complete rewrite
- `roles/vcto.html` — NEW: vCTO role page
- `css/pages.css` — MODIFY: add role page styles (shared across all role FRs)

**Acceptance Criteria:**
- [ ] `roles/index.html`: 5 group sections, all 21 roles listed with links
- [ ] Each role page follows Section 3.5 template: hero, day-in-the-life, your zones, key PAs, screenshots, CTA
- [ ] vCTO page created with appropriate zones (DevOps, Network Ops, vC-Suite) and PAs
- [ ] Each role page has unique persona-specific headline and hero text
- [ ] All role pages link to relevant zone and PA pages
- [ ] Role page styles are shared (single CSS section, not per-role)
- [ ] Responsive: timeline visualization stacks on mobile
- [ ] SEO: unique title and description per role

---

### FR-W10: Role Journey Pages — Operations

**ID:** FR-W10  
**Title:** Role Pages — IT Director, SDM (NEW), PM (refined), Service Desk Manager, Network Engineer, DevOps Engineer  
**Wave:** 3 (Journey & Role Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W09 (for shared role CSS)  

**Description:**  
Create/redesign 6 role journey pages for the Operations group. CRITICAL: Service Delivery Manager is a NEW page separated from Project Manager. PM is refined to focus on migration/deployment/timelines.

**Files to Create/Modify:**
- `roles/it-director.html` — MODIFY: complete rewrite
- `roles/service-delivery-manager.html` — NEW: SDM role page (ongoing service quality, SLA, QBR)
- `roles/project-manager.html` — MODIFY: refine to migration/deployment/timelines focus
- `roles/service-desk-manager.html` — MODIFY: complete rewrite
- `roles/network-engineer.html` — MODIFY: complete rewrite
- `roles/devops-engineer.html` — NEW (if not existing) or MODIFY

**Acceptance Criteria:**
- [ ] SDM page clearly differentiated from PM per the table in Section 3.5
- [ ] SDM focus: ongoing service quality, SLA management, escalation, QBR delivery
- [ ] PM focus: migration, deployment, timelines, phase-gated execution
- [ ] SDM zones: Service Desk, Analytics, Relationships
- [ ] PM zones: Projects, Service Desk, Analytics
- [ ] Each page follows the role template structure
- [ ] DevOps Engineer page includes CI/CD, infrastructure automation, platform operations content
- [ ] All pages responsive and accessible

---

### FR-W11: Role Journey Pages — Security & Compliance

**ID:** FR-W11  
**Title:** Role Pages — Security Analyst, Compliance Officer  
**Wave:** 3 (Journey & Role Pages)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W09 (for shared role CSS)  

**Description:**  
Redesign 2 role journey pages for the Security & Compliance group.

**Files to Create/Modify:**
- `roles/security-analyst.html` — MODIFY: complete rewrite
- `roles/compliance-officer.html` — MODIFY: complete rewrite

**Acceptance Criteria:**
- [ ] Security Analyst: threat detection, incident response, zero-trust content
- [ ] Compliance Officer: CMMC, SOC 2, HIPAA, OSCAL content
- [ ] Both link to Security & Trust Center
- [ ] Each follows role template structure
- [ ] Responsive and accessible

---

### FR-W12: Role Journey Pages — Business & Relationships

**ID:** FR-W12  
**Title:** Role Pages — Client Success Manager, Finance Coordinator, Sales Director, Marketing Director, Data Analyst  
**Wave:** 3 (Journey & Role Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W09 (for shared role CSS)  

**Description:**  
Create/redesign 5 role journey pages for the Business & Relationships group. Account Manager is renamed to Client Success Manager.

**Files to Create/Modify:**
- `roles/client-success-manager.html` — MODIFY (rename from account-manager.html content) or NEW
- `roles/finance-coordinator.html` — MODIFY: complete rewrite
- `roles/sales-director.html` — NEW (if not existing) or MODIFY
- `roles/marketing-director.html` — NEW (if not existing) or MODIFY
- `roles/data-analyst.html` — NEW (if not existing) or MODIFY

**Acceptance Criteria:**
- [ ] Client Success Manager replaces Account Manager — redirect from old URL if possible
- [ ] Each page follows role template structure
- [ ] Finance Coordinator links to ROI Calculator
- [ ] Sales Director includes pipeline management and proposal workflow content
- [ ] Data Analyst includes cross-zone analytics content
- [ ] All responsive and accessible

---

### FR-W13: Role Journey Pages — People & Culture

**ID:** FR-W13  
**Title:** Role Pages — HR Director, Recruiter, Legal Counsel  
**Wave:** 3 (Journey & Role Pages)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W09 (for shared role CSS)  

**Description:**  
Redesign 3 role journey pages for the People & Culture group.

**Files to Create/Modify:**
- `roles/hr-director.html` — MODIFY: complete rewrite
- `roles/recruiter.html` — MODIFY: complete rewrite
- `roles/legal-counsel.html` — NEW (if not existing) or MODIFY

**Acceptance Criteria:**
- [ ] HR Director: workforce analytics, access lifecycle, onboarding content
- [ ] Recruiter: skill gap analysis, onboarding automation content
- [ ] Legal Counsel: contract review, regulatory filings, compliance docs content
- [ ] Each follows role template structure
- [ ] Responsive and accessible

---

### FR-W14: Zone Pages — Service Desk, Security Operations, GRC & Compliance

**ID:** FR-W14  
**Title:** Zone Pages — Service/Security/Compliance Cluster  
**Wave:** 4 (Zone & Process Area Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Redesign 3 zone pages: Service Desk (12 PAs), Security Operations (13 PAs), GRC & Compliance (11 PAs).

**Files to Create/Modify:**
- `zones/service-desk/index.html` — MODIFY: complete rewrite per zone template (Section 3.3)
- `zones/security-operations/index.html` — MODIFY: complete rewrite
- `zones/grc-compliance/index.html` — MODIFY: complete rewrite
- `css/pages.css` — MODIFY: add zone page styles (shared across all zone FRs)

**Acceptance Criteria:**
- [ ] Each zone page follows Section 3.3 template
- [ ] Process area grid lists all PAs in the zone with correct counts
- [ ] Key screenshots from each zone displayed with lightbox
- [ ] Use cases section with 2–3 scenarios
- [ ] Connected roles and connected zones sections
- [ ] Zone-specific accent color subtly applied
- [ ] All PA links point to correct process-area sub-pages
- [ ] Responsive and accessible

---

### FR-W15: Zone Pages — Endpoint Management, Network Ops

**ID:** FR-W15  
**Title:** Zone Pages — Operations/Network/Endpoint Cluster  
**Wave:** 4 (Zone & Process Area Pages)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W14 (for shared zone CSS)  

**Description:**  
Redesign 2 zone pages: Endpoint Management (10 PAs), Network Ops (9 PAs).

**Files to Create/Modify:**
- `zones/endpoint-management/index.html` — MODIFY: complete rewrite
- `zones/network-ops/index.html` — MODIFY: complete rewrite

**Acceptance Criteria:**
- [ ] Each follows zone template
- [ ] All PAs listed with correct links
- [ ] Key screenshots included
- [ ] Responsive and accessible

---

### FR-W16: Zone Pages — Relationships, Analytics, vC-Suite

**ID:** FR-W16  
**Title:** Zone Pages — Business/Analytics/vC-Suite Cluster  
**Wave:** 4 (Zone & Process Area Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W14 (for shared zone CSS)  

**Description:**  
Redesign 3 zone pages: Relationships (11 PAs), Analytics (9 PAs), vC-Suite (13 PAs).

**Files to Create/Modify:**
- `zones/relationships/index.html` — MODIFY: complete rewrite
- `zones/analytics/index.html` — MODIFY: complete rewrite
- `zones/vc-suite/index.html` — MODIFY: complete rewrite

**Acceptance Criteria:**
- [ ] Each follows zone template
- [ ] vC-Suite includes vCTO-related process areas
- [ ] All PAs listed with correct links
- [ ] Key screenshots included
- [ ] Responsive and accessible

---

### FR-W17: Zone Pages — People, Learning, Organization, Legal

**ID:** FR-W17  
**Title:** Zone Pages — People/Learning/Organization/Legal Cluster  
**Wave:** 4 (Zone & Process Area Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W14 (for shared zone CSS)  

**Description:**  
Redesign 4 zone pages: People (8 PAs), Learning (10 PAs), Organization (11 PAs), Legal (7 PAs).

**Files to Create/Modify:**
- `zones/people/index.html` — MODIFY: complete rewrite
- `zones/learning/index.html` — MODIFY: complete rewrite
- `zones/organization/index.html` — MODIFY: complete rewrite
- `zones/legal/index.html` — MODIFY: complete rewrite

**Acceptance Criteria:**
- [ ] Each follows zone template
- [ ] All PAs listed with correct links
- [ ] Key screenshots included
- [ ] Responsive and accessible

---

### FR-W18: Zone Pages — DevOps, Accounting, Projects

**ID:** FR-W18  
**Title:** Zone Pages — DevOps/Accounting/Projects Cluster  
**Wave:** 4 (Zone & Process Area Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W14 (for shared zone CSS)  

**Description:**  
Redesign 3 zone pages: DevOps (11 PAs), Accounting (11 PAs), Projects (11 PAs).

**Files to Create/Modify:**
- `zones/devops/index.html` — MODIFY: complete rewrite
- `zones/accounting/index.html` — MODIFY: complete rewrite
- `zones/projects/index.html` — MODIFY: complete rewrite

**Acceptance Criteria:**
- [ ] Each follows zone template
- [ ] All PAs listed with correct links
- [ ] Key screenshots included
- [ ] Responsive and accessible

---

### FR-W19: Process Area Page Template + Generation Script

**ID:** FR-W19  
**Title:** Process Area Page Template & Python Generation Script  
**Wave:** 4 (Zone & Process Area Pages)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Create the process area page template (Section 3.4) and a Python generation script that produces all 157 PA pages from a data source (JSON/YAML). This ensures consistency across all PA pages and makes future content updates easy.

**Files to Create/Modify:**
- `scripts/generate-pa-pages.py` — NEW: Python script that reads PA data and generates HTML
- `scripts/pa-data.json` — NEW: structured data for all 157 process areas (name, zone, description, key metrics, related PAs, related roles, screenshot refs)
- `zones/*/process-areas/*.html` — ALL 157 files regenerated from template
- `css/pages.css` — MODIFY: add process area page styles

**Acceptance Criteria:**
- [ ] Python script generates all 157 PA pages from `pa-data.json`
- [ ] Generated pages follow Section 3.4 template exactly
- [ ] Each page has: breadcrumb, hero, overview, how-it-works, AI capabilities, screenshots, metrics, connected PAs, related roles, CTA
- [ ] Each page has unique SEO title and meta description
- [ ] BreadcrumbList structured data on every page
- [ ] Screenshots referenced correctly (paths match existing `assets/screenshots/` structure)
- [ ] Script is idempotent (running twice produces identical output)
- [ ] All 157 pages validate as accessible HTML
- [ ] Script runs in < 30 seconds

---

### FR-W20: AI Chatbot Widget

**ID:** FR-W20  
**Title:** AI Chatbot Widget  
**Wave:** 5 (Interactive Components)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W03  

**Description:**  
Build the AI chatbot widget per Section 4.1. Floating action button on all pages, chat panel with message history, suggested prompts, and graceful fallback.

**Files to Create/Modify:**
- `js/components/chatbot.js` — NEW: chatbot widget logic
- `css/components.css` — MODIFY: add chatbot styles (`.chatbot--fab`, `.chatbot--panel`, message bubbles)

**Acceptance Criteria:**
- [ ] FAB: glassmorphic circle in bottom-right, subtle green pulse, "Ask AI" badge on first visit
- [ ] Chat panel: 400px wide, 500px tall (desktop), full-screen mobile
- [ ] Chat panel: glassmorphic background, message bubbles, typing indicator
- [ ] Suggested prompts on first open (4 suggestions per spec)
- [ ] Markdown rendering in assistant responses
- [ ] API integration: calls configurable endpoint (`data-chatbot-endpoint`)
- [ ] Rate limiting: respects 30 RPM limit, shows "Please wait" if exceeded
- [ ] Fallback: if API unavailable, shows static FAQ panel
- [ ] Keyboard accessible: Escape closes panel, Tab navigates within
- [ ] Screen reader: `aria-live` for new messages
- [ ] No interference with page scroll when panel is open (mobile: prevents body scroll)
- [ ] Widget loads via dynamic `import()` — zero impact on pages without it
- [ ] Chat history persisted to sessionStorage (cleared on tab close)

---

### FR-W21: Journey Entry Point Evolution

**ID:** FR-W21  
**Title:** Journey Entry Point — Evolved 3D/Card Grid Role Selection  
**Wave:** 5 (Interactive Components)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W03  

**Description:**  
Evolve the existing `entry-point.js` and its CSS per Section 4.3. Updated to 21 roles, improved aesthetics, better mobile experience, smarter triggering.

**Files to Create/Modify:**
- `js/entry-point.js` — MODIFY: evolution of existing (updated roles, improved 3D aesthetics, mobile carousel)
- `css/personalization.css` — MODIFY: evolved entry point styles (glassmorphic cards, mobile carousel)

**Acceptance Criteria:**
- [ ] 21 roles displayed (including vCTO and Service Delivery Manager)
- [ ] Role groups match updated ROLE_GROUPS (5 categories)
- [ ] 3D mode: improved node aesthetics (glass-like, better bloom, smoother aurora)
- [ ] Card grid mode: glassmorphic cards with hover previews
- [ ] Mobile: swipeable card carousel with category tabs
- [ ] Role selection flow: click → expanded card with zone preview → confirm
- [ ] Progressive loading: CSS-only bg → 2D canvas → WebGL based on device capability
- [ ] "Find Your Role" CTA available anywhere (not just first visit)
- [ ] Works with updated personalization system
- [ ] Reduced motion: static card grid, no 3D, no canvas animation

---

### FR-W22: Interactive Product Demo

**ID:** FR-W22  
**Title:** Interactive Product Demo Component  
**Wave:** 5 (Interactive Components)  
**Estimated Complexity:** L  
**Dependencies:** FR-W01, FR-W03  

**Description:**  
Build the interactive product demo per Section 4.2. Self-paced guided walkthrough of key workflows, embeddable on homepage and standalone.

**Files to Create/Modify:**
- `js/components/demo.js` — NEW: demo walkthrough logic
- `css/components.css` — MODIFY: add demo styles (step indicators, hotspots, transitions)
- `assets/demo/` — NEW: demo-specific screenshots or animations

**Acceptance Criteria:**
- [ ] Primary demo: "Watch AI Resolve a Ticket" (5–7 steps, 60–90 seconds)
- [ ] Step-based progression: click to advance, back button, progress indicator
- [ ] Each step: narration text, highlighted hotspot on screenshot, smooth transition
- [ ] Embeddable inline (homepage section) and openable in lightbox
- [ ] Mobile responsive: stacks vertically, swipe to advance
- [ ] Completion CTA: "See this with your own data → Book Demo"
- [ ] Keyboard accessible: arrow keys to navigate
- [ ] Lazy loaded: zero impact until invoked

---

### FR-W23: ROI Calculator

**ID:** FR-W23  
**Title:** Interactive ROI Calculator  
**Wave:** 5 (Interactive Components)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W03  

**Description:**  
Evolve the existing ROI calculator per Section 4.4. Interactive inputs, real-time calculation, visual output.

**Files to Create/Modify:**
- `js/components/roi-calculator.js` — NEW (or evolved from existing `roi.html` inline JS)
- `roi.html` — MODIFY: redesign with new layout and calculator component
- `css/pages.css` — MODIFY: add ROI calculator styles

**Acceptance Criteria:**
- [ ] Input fields: technicians, tickets/month, resolution time, current costs, endpoints, industry
- [ ] Real-time calculation as inputs change (no submit button)
- [ ] Output: time saved, tickets auto-resolved, monthly savings, ROI %, time-to-ROI
- [ ] Animated bar chart: "Current State" vs. "With DevOps AI"
- [ ] Dollar savings counter animation
- [ ] "Share this report" generates URL with parameters
- [ ] Input validation: reasonable ranges, helpful error messages
- [ ] Responsive: inputs stack on mobile, chart adapts
- [ ] No server-side processing — pure client-side JavaScript

---

### FR-W24: Personalization System Evolution

**ID:** FR-W24  
**Title:** Personalization System — Cookie Consent, Role Tracking, Personalized Content  
**Wave:** 5 (Interactive Components)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03, FR-W21  

**Description:**  
Evolve the existing `personalization.js` and `personalization.css` per Section 4.7. Updated role list (21 roles), lifecycle-aware CTAs, glassmorphic consent banner.

**Files to Create/Modify:**
- `js/personalization.js` — MODIFY: updated roles (add vCTO, SDM, rename Account Manager → Client Success Manager), lifecycle-aware CTAs, improved journey tracking
- `css/personalization.css` — MODIFY: glassmorphic consent banner, updated welcome bar, role picker styles

**Acceptance Criteria:**
- [ ] Cookie consent banner: glassmorphic design, 3 toggles (essential/analytics/personalization)
- [ ] Granular consent detail view (expandable) showing what each category tracks
- [ ] Updated ROLES array: 21 roles including vCTO and SDM
- [ ] Account Manager → Client Success Manager rename
- [ ] ROLE_ZONES updated for new roles (vCTO, SDM)
- [ ] ROLE_HERO_TEXT updated for new roles
- [ ] ROLE_DESCRIPTIONS updated for new roles
- [ ] Lifecycle-aware CTAs: different CTA text based on awareness/evaluation/onboarding stage
- [ ] "Continue where you left off" for returning visitors
- [ ] Consent persisted to localStorage + cookies
- [ ] Re-consent mechanism (version number check)
- [ ] PM and SDM clearly separated in role picker and hero text

---

### FR-W25: Secondary Pages

**ID:** FR-W25  
**Title:** About, Contact, Marketplace, Blog Hub, Legal Pages  
**Wave:** 6 (Content & Polish)  
**Estimated Complexity:** M  
**Dependencies:** FR-W01, FR-W02, FR-W03  

**Description:**  
Create or redesign the secondary pages: About, Contact, Azure Marketplace, Blog Hub, Login redirect, and Legal pages.

**Files to Create/Modify:**
- `about.html` — MODIFY: complete rewrite per Section 3.9
- `contact.html` — MODIFY: complete rewrite per Section 3.10
- `marketplace.html` — MODIFY: complete rewrite per Section 3.11
- `blog.html` — NEW: blog/resources hub per Section 3.14
- `login.html` — NEW: login redirect per Section 3.15
- `why-devops-ai.html` — MODIFY: refresh content and design
- `solutions.html` — MODIFY: redesign per Section 3.13
- `legal/privacy.html` — MODIFY: update design, add expandable sections
- `legal/terms.html` — NEW: Terms of Service
- `legal/acceptable-use.html` — NEW: Acceptable Use Policy

**Acceptance Criteria:**
- [ ] All pages use shared header/footer from FR-W02
- [ ] About: team section, timeline, values, mission
- [ ] Contact: multi-step form with inquiry routing, embedded meeting scheduler placeholder
- [ ] Marketplace: step-by-step Azure deployment guide with screenshots
- [ ] Blog: category filters, post grid layout, newsletter signup
- [ ] Login: auto-redirect to platform.devops.ai.rain.tech, manual fallback link
- [ ] Legal pages: table of contents, version dates, expandable sections
- [ ] All responsive and accessible
- [ ] SEO: unique titles and descriptions for each page

---

### FR-W26: SEO Optimization

**ID:** FR-W26  
**Title:** SEO Optimization — Sitemap, Structured Data, llms.txt, Meta Tags  
**Wave:** 6 (Content & Polish)  
**Estimated Complexity:** M  
**Dependencies:** FR-W04 through FR-W25 (all content pages)  

**Description:**  
Comprehensive SEO pass across all ~210 pages. Generate sitemap, validate structured data, create llms.txt, ensure all meta tags are unique and descriptive.

**Files to Create/Modify:**
- `scripts/generate-sitemap.py` — NEW: Python script that crawls the file system and generates sitemap.xml
- `sitemap.xml` — GENERATED by script
- `robots.txt` — MODIFY: add sitemap reference, ensure no disallow on important paths
- `llms.txt` — NEW: AI/LLM discoverability file per Section 6.5
- ALL HTML files — MODIFY: verify/add structured data, meta tags, Open Graph, canonical URLs

**Acceptance Criteria:**
- [ ] `sitemap.xml` includes all ~210 pages with correct lastmod dates
- [ ] `robots.txt` references sitemap, allows all important paths
- [ ] `llms.txt` created per specification
- [ ] Every page has unique `<title>` (60 chars max) and `<meta name="description">` (155 chars max)
- [ ] Every page has Open Graph tags (og:title, og:description, og:image, og:url)
- [ ] Every page has Twitter Card tags
- [ ] Every page has canonical URL (`<link rel="canonical">`)
- [ ] Structured data validates via Google Rich Results Test
- [ ] BreadcrumbList on all interior pages
- [ ] Image alt text on all screenshots
- [ ] Internal linking verified: no broken links, all zones/roles/PAs cross-linked
- [ ] Redirect map for any changed URLs (via 404.html client-side or `.htaccess` equivalent)

---

### FR-W27: Performance Optimization & Accessibility Audit

**ID:** FR-W27  
**Title:** Performance Optimization, Accessibility Audit, Final Polish  
**Wave:** 6 (Content & Polish)  
**Estimated Complexity:** L  
**Dependencies:** All previous FRs  

**Description:**  
Final optimization and quality pass. Ensure all Core Web Vitals targets are met, all accessibility requirements are satisfied, cross-browser testing, and final design polish.

**Files to Create/Modify:**
- `scripts/optimize-images.py` — NEW: Python script to convert screenshots to WebP, generate srcset variants
- ALL CSS files — MODIFY: minification comments, unused style removal
- ALL HTML files — MODIFY: add critical CSS inline, preload/preconnect directives
- `manifest.json` — NEW (optional): PWA manifest for installability

**Acceptance Criteria:**
- [ ] Lighthouse scores: Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95
- [ ] Core Web Vitals: LCP < 2.5s, CLS < 0.1, INP < 200ms (measured on homepage)
- [ ] Total initial page weight < 500KB (excluding lazy-loaded images)
- [ ] All screenshots converted to WebP with PNG fallback
- [ ] Critical CSS inlined in `<head>` for homepage and all core pages
- [ ] `<link rel="preload">` for hero image and primary font
- [ ] `<link rel="preconnect">` for any external domains
- [ ] Font files subset to Latin characters
- [ ] `font-display: swap` on all @font-face declarations
- [ ] Accessibility audit: zero WCAG 2.2 AA violations (axe-core)
- [ ] Keyboard navigation works on every page (tab order, focus visible, skip link)
- [ ] Screen reader testing: heading hierarchy, alt text, aria-labels, live regions
- [ ] `prefers-reduced-motion` respected on all animations
- [ ] `prefers-color-scheme` respected (dark default, light available)
- [ ] Cross-browser: Chrome, Firefox, Safari, Edge (last 2 versions)
- [ ] Mobile testing: iOS Safari, Chrome Android
- [ ] CNAME preserved: `devops.ai.rain.tech`
- [ ] All 160+ screenshot assets preserved and accessible
- [ ] No console errors on any page
- [ ] Progressive enhancement verified: all pages readable without JavaScript

---

## Appendix A: Existing Asset Inventory

### Screenshot Assets (160 files in `assets/screenshots/`)

All 160 screenshots MUST be preserved and utilized in the redesign. The Python generation script (`generate-pa-pages.py`) should map screenshots to their respective zone and process area pages.

### Zone and Process Area Counts

| Zone | PA Count | Zone Directory |
|------|----------|---------------|
| Service Desk | 12 | `zones/service-desk/` |
| Security Operations | 13 | `zones/security-operations/` |
| GRC & Compliance | 11 | `zones/grc-compliance/` |
| Endpoint Management | 10 | `zones/endpoint-management/` |
| Network Ops | 9 | `zones/network-ops/` |
| vC-Suite | 13 | `zones/vc-suite/` |
| Analytics | 9 | `zones/analytics/` |
| Relationships | 11 | `zones/relationships/` |
| People | 8 | `zones/people/` |
| Learning | 10 | `zones/learning/` |
| Organization | 11 | `zones/organization/` |
| Legal | 7 | `zones/legal/` |
| DevOps | 11 | `zones/devops/` |
| Accounting | 11 | `zones/accounting/` |
| Projects | 11 | `zones/projects/` |
| **Total** | **157** | |

### CSS File Evolution Map

| Current File | Evolves Into |
|-------------|-------------|
| `base.css` | `css/base.css` (tokens, reset, typography) |
| `style.css` | `css/layout.css` (header/footer/nav) + `css/pages.css` (page-specific) |
| `enhancements.css` | `css/components.css` (components) + `css/animations.css` (animations) |
| `personalization.css` | `css/personalization.css` (evolved consent + role picker) |

### JavaScript File Evolution Map

| Current File | Evolves Into |
|-------------|-------------|
| `app.js` | `js/app.js` (core + lazy loading) |
| `personalization.js` | `js/personalization.js` (evolved) |
| `entry-point.js` | `js/entry-point.js` (evolved) |
| `enhancements.js` | Absorbed into `js/app.js` and `js/components/*.js` |

## Appendix B: Role Changes Summary

| Change Type | Role | Notes |
|------------|------|-------|
| NEW | vCTO | Architecture reviews, infrastructure strategy, technical debt |
| NEW | Service Delivery Manager | Ongoing service quality, SLA, escalation, QBR — separated from PM |
| REFINED | Project Manager | Now focused on migration, deployment, timelines — no longer covers SDM duties |
| RENAMED | Client Success Manager | Was "Account Manager" — better reflects role scope |
| RETAINED | All other 17 roles | Content updated but role identity unchanged |

## Appendix C: Key Product Decisions (From Andrew)

These decisions from the product owner MUST be reflected in all relevant pages:

1. **PM and SDM are SEPARATE roles** — distinct pages, distinct journeys, distinct zone mappings
2. **MSP vs Enterprise are separate Marketplace packages** — no MSP/Enterprise toggle on pricing page
3. **Chatbot has admin control plane** — operators provide their own inference API key, can manage it
4. **Azure AI first for inference** — Azure OpenAI is default, admin controls for 3rd party fallback

## Appendix D: File Conflict Prevention Matrix

Each FR operates on specific files. This matrix ensures no two parallel FRs modify the same file:

| File | Owned By | Modified By |
|------|----------|-------------|
| `css/base.css` | FR-W01 | FR-W01 only |
| `css/components.css` | FR-W01 | FR-W01, FR-W20, FR-W22 (append only — each adds its own component section) |
| `css/layout.css` | FR-W02 | FR-W02 only |
| `css/pages.css` | FR-W04 | FR-W04–W08, FR-W09 (role), FR-W14 (zone), FR-W19 (PA), FR-W23, FR-W25 (each appends own page section) |
| `css/animations.css` | FR-W01 | FR-W01 only |
| `css/personalization.css` | FR-W24 | FR-W21, FR-W24 |
| `js/app.js` | FR-W03 | FR-W03 only |
| `js/personalization.js` | FR-W24 | FR-W24 only |
| `js/entry-point.js` | FR-W21 | FR-W21 only |
| `js/components/chatbot.js` | FR-W20 | FR-W20 only |
| `js/components/demo.js` | FR-W22 | FR-W22 only |
| `js/components/roi-calculator.js` | FR-W23 | FR-W23 only |
| `js/components/lightbox.js` | FR-W03 | FR-W03 only |
| `js/components/counter.js` | FR-W03 | FR-W03 only |
| `js/components/metrics.js` | FR-W03 | FR-W03 only (stub — populated by FR-W04 integration) |
| `index.html` | FR-W04 | FR-W04 only |
| `platform.html` | FR-W05 | FR-W05 only |
| `pricing.html` | FR-W06 | FR-W06 only (NEW if doesn't exist) |
| `security.html` | FR-W07 | FR-W07 only |
| `architecture.html` | FR-W08 | FR-W08 only |
| `roles/*.html` | FR-W09–W13 | Each FR owns its assigned role files |
| `zones/*/index.html` | FR-W14–W18 | Each FR owns its assigned zone files |
| `zones/*/process-areas/*.html` | FR-W19 | FR-W19 only (generated) |
| `about.html`, `contact.html`, etc. | FR-W25 | FR-W25 only |
| `sitemap.xml`, `llms.txt`, `robots.txt` | FR-W26 | FR-W26 only |

**Conflict Resolution for `css/pages.css` and `css/components.css`:**
These files are modified by multiple FRs, but each FR appends its own clearly delineated section:

```css
/* ═══ FR-W04: Homepage ═══ */
.home-hero { ... }
.home-bento { ... }

/* ═══ FR-W05: Platform Overview ═══ */
.platform-hero { ... }
.platform-zones { ... }

/* ═══ FR-W09: Role Pages ═══ */
.role-hero { ... }
.role-timeline { ... }
```

Each FR MUST prefix its CSS selectors with a page/section-specific namespace to prevent collisions.

---

*End of Specification*
