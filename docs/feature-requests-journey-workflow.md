# Feature Request Scoping — Journey & Workflow Taxonomy

**Date:** March 16, 2026  
**Source Specification:** DevOps AI Journey & Workflow Canonical Taxonomy v1.0  
**Status:** Scoped as platform feature requests (not promotional website)

---

## Context

The Journey & Workflow Canonical Taxonomy spec (v1.0, 39 pages) defines interconnected systems that live **inside the DevOps AI platform**, not on the public-facing website. The promotional website is the *output* of these systems — when a journey is enabled for a role, the website surfaces natural, frictionless entry points for that ICP.

### What lives on the promotional website (already implemented):
- 10 role-specific pages with pre-sales journey content (Discovery → Evaluation → What Getting Started/Your Day/Growth Looks Like)
- Zone deep-dive pages that journeys link to
- Natural, frictionless content paths for each ICP

### What lives inside the DevOps AI platform (feature requests below):
- Journey Orchestrator in BD zone — enable/disable/manage website journeys per role
- People Management / Onboarding journeys — LMS-integrated, compliance-driven
- Canonical Workflow Library — standards-based starter workflows
- Workflow Creator — AI-assisted workflow design
- Workflow Dependency Visualization — interactive flowcharts

---

## FR-001: Website Journey Orchestrator (BD Zone — Platform Feature)

**Owner Zone:** Business Development (CRM / Customer Journey control plane)  
**Priority:** High  
**HITL Required:** Yes — all journey activation requires human approval  

### Description
Within the DevOps AI platform, a marketing director or BD lead navigates to the Business Development zone → Customer Journey / CRM control plane and can:

1. **Enable a Website Journey** for a specific role (e.g., "Compliance Officer")
2. The system generates/activates role-specific content, entry points, CTAs, and navigation paths for the public website
3. Generated content is **sandboxed** for HITL review before going live
4. On HITL approval, the journey goes live — compliance managers visiting the public website encounter natural, frictionless entry points tailored to their role and interests (GRC solutions, compliance automation, etc.)
5. Journey performance metrics (engagement, conversion, content interaction) are visible in the BD control plane

### Scope: Pre-Sales Journeys Only
This system manages **pre-sales** website journeys exclusively. It does not manage:
- In-app onboarding journeys (see FR-002)
- Post-sale workflow enablement (see FR-003)

### Architecture
- Journey definitions are canonicalized objects with: role target, lifecycle stages, content mappings, CTA configurations, and activation status
- Each journey maps to the 12-zone architecture and surfaces zone-specific content relevant to the target role
- Sandbox environment allows HITL to preview exactly what prospects will see before activation
- Analytics track per-role journey engagement, stage progression, and conversion

### Standards Alignment
- Customer Journey Orchestration (CJO) patterns
- ITIL 4 Service Value Chain: Engage activity
- Product-led growth (PLG) website personalization patterns

---

## FR-002: People Management / Onboarding Journeys (Platform Feature)

**Owner:** People Management (wherever people are managed by the respective HITL)  
**Priority:** High  
**Dependency:** LMS canonicalized elements, compliance-driven workflow framework  

### Description
When a new human is onboarded into the organization, the respective HITL (manager, department lead) enables onboarding journeys that:

1. **Onboard new humans into their assigned, automation-first workflows** — not generic training, but role-specific workflow mastery
2. Deep integration with the **LMS** (Learning zone) for structured learning paths, certification tracking, and compliance training evidence
3. Deep integration with all **compliance-driven workflows** — security awareness training, policy attestation, access certification
4. Integration with all **respective control planes** — user and supervisory — so onboarding progress is visible to both the individual and their manager
5. Available in all relevant user and supervisory control planes (not just one zone)

### Scope
- Post-sale, internal onboarding only
- Managed by People Management HITL, not BD/Marketing
- Covers: new hire onboarding, role change onboarding, new capability rollout training
- Compliance training with audit evidence (SCORM/xAPI tracking)

### Architecture
- Onboarding journeys are canonicalized within the LMS taxonomy
- Journey definitions are composable from reusable step primitives
- Journey state persists per-user, per-organization
- Supervisory control planes surface completion rates and adoption metrics per team
- Interactive walkthroughs use contextual in-app guidance (tooltip tours, checklists, progress indicators)
- Empty states as learning opportunities — first-use of any zone feature triggers contextual guidance

### Standards Alignment
- ITIL 4 Service Value Chain: Design & Transition
- xAPI/SCORM for compliance training evidence
- Product-Led Growth (PLG) in-app onboarding patterns (Pendo/WalkMe/Appcues model)

---

## FR-003: Canonical Workflow Library (DevOps Zone — Platform Feature)

**Owner Zone:** DevOps  
**Priority:** High  
**Access:** DevOps engineers (default); power users and department/module leads can be granted access  

### Description
A standards-based library of 37 canonical starter workflows covering four lifecycle phases:

#### A. Preparation Workflows (8)
Pre-migration readiness: data audit, identity mapping, vendor assessment, compliance gap analysis, license reconciliation, network prerequisites, communication plan, rollback planning.

#### B. Migration Workflows (10)
Data migration execution: mailbox, SharePoint, endpoint enrollment, security tools, RMM, PSA data import, compliance evidence, network configuration, identity federation, billing/agreement migration.

#### C. Management Workflows (10)
Steady-state operations: monthly billing reconciliation, QBR preparation, SLA monitoring, patch management, compliance evidence collection, backup verification, access review, vendor contract renewal, client health scoring, incident post-mortem.

#### D. Offboarding Workflows (9)
Safe transition: MSP-to-MSP handover, MSP-to-standalone transition, platform export (EU Data Act compliant), access revocation cascade, credential rotation, documentation handover, billing close, data archival with configurable retention, integration endpoint decommission.

### Architecture
- Workflows are first-class objects in the DevOps zone taxonomy
- Each workflow has: canonical ID, version, BPMN 2.0 definition, role assignments, dependency map
- Workflows can be cloned and customized per organization
- Power users and department/module leads can be granted workflow creator access (see FR-004)

### Standards Alignment
- BPMN 2.0 process notation
- EU Data Act (effective Sep 2025) data portability requirements
- GDPR Article 20 machine-readable export formats
- ITIL 4 Service Value Chain mapping per workflow
- NIST CSF 2.0 for security-relevant workflows

---

## FR-004: Workflow Creator & AI Design Sessions (DevOps Zone — Platform Feature)

**Owner Zone:** DevOps  
**Priority:** Medium  
**Access:** DevOps engineers (default); power users and department/module leads (grantable)  

### Description
An intuitive, AI-assisted workflow creation interface that:
- Provides a visual BPMN 2.0-compatible canvas for workflow design
- Surfaces all dependency data elements and inter-related workflows during editing
- Highlights impacted workflows when contemplating adjustments or combinations
- Offers AI DevOps AI-led interactive design sessions that guide users through:
  - Defining triggers, activities, gateways, and outcomes
  - Identifying automation candidates vs. human decision points
  - Mapping role assignments (swimlanes)
  - Setting SLA timers and escalation rules
  - Testing and validating before activation
- Supports combining/merging existing workflows with conflict detection
- Maintains full version history with diff visualization

### Standards Alignment
- OMG BPMN 2.0 modeling notation
- Canonical Workflow Building Blocks methodology (MIT Press 2022)
- ITIL 4 practice-based workflow design

---

## FR-005: Workflow Dependency Visualization Engine (DevOps Zone — Platform Feature)

**Owner Zone:** DevOps  
**Priority:** Medium  
**Dependency:** FR-003 (Workflow Library) must be in place first  

### Description
A highly intuitive, navigable flowchart visualization system:
- Interactive dependency graph showing workflow-to-workflow relationships
- Zoom, filter, and search across the full workflow library
- Impact analysis: select a workflow and see all upstream/downstream dependencies
- Color-coded by lifecycle phase, zone ownership, and automation level
- Uses the platform's **built-in visualization skill** for:
  - Complex, high-quality graphics rendering
  - Brand-integrated iconography (zone icons, status indicators)
  - Brand-compliant color schemes per zone accent
- Exportable as SVG/PDF for documentation
- Real-time status overlay showing active workflow instances

### Standards Alignment
- BPMN 2.0 visual notation
- W3C SVG for rendering
- WCAG 2.1 AA accessibility

---

## Dependency Map

```
FR-001 (Website Journey Orchestrator)
  └── Depends on: BD zone CRM/Journey control plane, website content generation system, sandbox/preview environment

FR-002 (People/Onboarding Journeys)
  └── Depends on: LMS canonicalized elements, People Management HITL framework, compliance workflow engine

FR-003 (Canonical Workflow Library)
  └── Depends on: DevOps zone workflow engine, BPMN 2.0 runtime

FR-004 (Workflow Creator)
  └── Depends on: FR-003 (library structure), RBAC grants, AI orchestration layer

FR-005 (Visualization Engine)
  └── Depends on: FR-003 (workflow data), built-in visualization skill
```

---

## Implementation Priority

| Priority | Feature Request | Rationale |
|----------|----------------|-----------|
| 1 | FR-001: Website Journey Orchestrator | Enables marketing to activate role-specific website experiences; direct revenue impact |
| 2 | FR-003: Canonical Workflow Library | Foundation for FR-004 and FR-005; immediate operational value |
| 3 | FR-002: People/Onboarding Journeys | Critical for user activation and retention; depends on LMS readiness |
| 4 | FR-004: Workflow Creator | Enables customization; power-user differentiator |
| 5 | FR-005: Visualization Engine | Enhances usability of FR-003/FR-004; can ship incrementally |
