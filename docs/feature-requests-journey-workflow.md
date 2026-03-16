# Feature Request Scoping — Journey & Workflow Taxonomy

**Date:** March 16, 2026  
**Source Specification:** DevOps AI Journey & Workflow Canonical Taxonomy v1.0  
**Status:** Scoped and separated from promotional website implementation

---

## Context

The Journey & Workflow Canonical Taxonomy spec (v1.0, 39 pages) defines three interconnected systems:
1. **Website Journeys** — Role/ICP-specific content paths on the promotional website
2. **In-App Journeys** — Interactive walkthroughs, guided onboarding, and contextual learning within the product
3. **Canonical Workflows** — Standards-based operational workflows for migration, management, and offboarding

The promotional website implements **#1 only** — role/ICP journey mapping with a link to the Business Development control plane. Items #2 and #3 are scoped below as separate feature requests for the product engineering team.

---

## FR-001: In-App Welcome & Guided Walkthrough Journeys

**Owner Zone:** Learning (LMS)  
**User/Supervisory Control Planes:** All relevant user and supervisory control planes  
**Priority:** High  
**Dependency:** LMS canonicalized elements must be in place  

### Description
Interactive in-app onboarding journeys triggered at first login, role assignment, or feature activation. These include:
- Welcome journey with progressive disclosure of platform capabilities
- Role-specific guided walkthroughs (e.g., Security Analyst sees SOC Command first)
- Contextual tooltip tours for new features or underused capabilities
- Action-focused onboarding (not feature tours) — shortest path to "aha moment"
- Progress checklists with completion tracking
- Empty state utilization as learning opportunities

### Standards Alignment
- Product-Led Growth (PLG) onboarding patterns (Pendo, WalkMe, Appcues model)
- ITIL 4 Service Value Chain: Engage → Design & Transition
- xAPI/SCORM tracking for compliance training evidence

### Architecture Notes
- Journeys should be canonicalized within the LMS taxonomy and exposed in all relevant control planes
- Journey definitions should be modular — composable from reusable step primitives
- Journey state persists per-user, per-organization
- Supervisory control planes surface completion rates and adoption metrics per team

---

## FR-002: Canonical Workflow Library (Starter Workflows)

**Owner Zone:** DevOps  
**Priority:** High  
**Categories:** 4 lifecycle phases, 37 canonical workflows

### Description
A standards-based library of starter workflows covering the four lifecycle phases:

#### A. Preparation Workflows (8)
Pre-migration readiness: data audit, identity mapping, vendor assessment, compliance gap analysis, license reconciliation, network prerequisites, communication plan, rollback planning.

#### B. Migration Workflows (10)
Data migration execution: mailbox migration, SharePoint migration, endpoint enrollment, security tool migration, RMM migration, PSA data import, compliance evidence migration, network configuration migration, identity federation, billing/agreement migration.

#### C. Management Workflows (10)
Steady-state operations: monthly billing reconciliation, QBR preparation, SLA monitoring and remediation, patch management cycle, compliance evidence collection, backup verification, access review certification, vendor contract renewal, client health scoring, incident post-mortem.

#### D. Offboarding Workflows (9)
Safe transition: MSP-to-MSP handover, MSP-to-standalone transition, platform export (EU Data Act compliant), access revocation cascade, credential rotation, documentation handover, billing close and final reconciliation, data archival with configurable retention, integration endpoint decommission.

### Standards Alignment
- BPMN 2.0 process notation for workflow definitions
- EU Data Act (effective Sep 2025) data portability requirements
- GDPR Article 20 machine-readable export formats
- ITIL 4 Service Value Chain mapping per workflow
- NIST CSF 2.0 for security-relevant workflows

### Architecture Notes
- Workflows are first-class objects in the DevOps zone taxonomy
- Each workflow has a canonical ID, version, BPMN definition, role assignments, and dependency map
- Workflows can be cloned and customized per organization
- Power users and department/module leads can be granted workflow creator access (see FR-003)

---

## FR-003: Workflow Creator & AI Design Sessions

**Owner Zone:** DevOps  
**Priority:** Medium  
**Access:** DevOps engineers (default), power users and department/module leads (grantable)

### Description
An intuitive, AI-assisted workflow creation interface that:
- Provides a visual BPMN 2.0-compatible canvas for workflow design
- Surfaces all dependency data elements and inter-related workflows during editing
- Highlights impacted workflows when contemplating adjustments or combinations
- Offers AI-led interactive design sessions that guide users through:
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

### Architecture Notes
- The workflow creator is a DevOps zone capability, not a BD zone capability
- Access grants use the platform's RBAC system — department/module leads can be elevated
- AI design sessions should leverage the platform's existing AI orchestration layer
- All created workflows inherit the canonical taxonomy structure (ID, version, dependencies)

---

## FR-004: Workflow Dependency Visualization Engine

**Owner Zone:** DevOps  
**Priority:** Medium  
**Dependency:** FR-002 (Workflow Library) must be in place first

### Description
A highly intuitive, navigable flowchart visualization system for workflows and their dependencies:
- Interactive dependency graph showing workflow-to-workflow relationships
- Zoom, filter, and search capabilities across the full workflow library
- Impact analysis view: select a workflow and see all upstream/downstream dependencies
- Color-coded by lifecycle phase, zone ownership, and automation level
- Uses the platform's built-in visualization skill for:
  - Complex, high-quality graphics rendering
  - Brand-integrated iconography (zone icons, status indicators)
  - Brand-compliant color schemes per zone accent
- Exportable as SVG/PDF for documentation
- Real-time status overlay showing active workflow instances

### Standards Alignment
- BPMN 2.0 visual notation standards
- W3C SVG for rendering
- WCAG 2.1 AA accessibility for interactive elements

### Architecture Notes
- Visualization engine should be a reusable platform component (not BD-specific)
- Must handle 37+ canonical workflows plus custom workflows at scale
- Consider directed acyclic graph (DAG) layout algorithms for dependency clarity
- The built-in visualization skill should be leveraged for all complex graphics requirements
- Brand integration requirements: zone accent colors, platform iconography, Plus Jakarta Sans typography

---

## Dependency Map

```
FR-001 (In-App Journeys)
  └── Depends on: LMS canonicalized elements, user control plane framework

FR-002 (Workflow Library)
  └── Depends on: DevOps zone workflow engine, BPMN 2.0 runtime

FR-003 (Workflow Creator)
  └── Depends on: FR-002 (library structure), RBAC grants, AI orchestration layer

FR-004 (Visualization Engine)
  └── Depends on: FR-002 (workflow data), built-in visualization skill
```

---

## Implementation Priority Recommendation

| Priority | Feature Request | Rationale |
|----------|----------------|-----------|
| 1 | FR-002: Workflow Library | Foundation for FR-003 and FR-004; immediate operational value |
| 2 | FR-001: In-App Journeys | Critical for user activation and retention; PLG differentiator |
| 3 | FR-003: Workflow Creator | Enables customization; power-user differentiator |
| 4 | FR-004: Visualization | Enhances usability of FR-002/FR-003; can ship incrementally |
