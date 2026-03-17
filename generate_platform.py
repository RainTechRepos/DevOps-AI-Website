#!/usr/bin/env python3
"""Generate the complete platform.html with full zone journey entry points,
workflow screenshots, and taxonomical control plane wiring."""

import textwrap

# ─── Zone Data ───────────────────────────────────────────────────────────────
ZONES = [
    {
        "num": 1, "slug": "service-desk", "name": "Service Desk",
        "icon": "🎫", "accent": "#2563EB",
        "tagline": "AI-augmented ticket management, SLA optimization, and predictive support operations",
        "description": "The Service Desk is the operational heartbeat of every MSP. DevOps AI transforms reactive ticket queues into predictive, AI-augmented support operations — routing tickets intelligently, surfacing known-error solutions before technicians search, and predicting SLA breaches before they happen.",
        "process_areas": [
            ("Ticket Ingestion &amp; AI Triage", "L0", "Automated classification, priority scoring, and intelligent routing based on technician skills, workload, and client SLA tiers."),
            ("Known Error Database (KEDB)", "L0", "AI-maintained knowledge base that surfaces matching solutions as tickets are created. Self-healing when new resolutions are confirmed."),
            ("SLA Management &amp; Prediction", "L1", "Real-time SLA tracking with predictive breach alerts. Automated escalation triggers when resolution targets are at risk."),
            ("Dispatch Optimization", "L1", "AI-optimized technician assignment considering skills matrix, current workload, client proximity, and specialization."),
            ("CSAT Collection &amp; Analysis", "L0", "Automated satisfaction surveys post-resolution with sentiment analysis and trend detection across clients."),
            ("Co-Managed IT Workflows", "L2", "Shared ticket queues between MSP and client internal IT with role-based visibility, handoff protocols, and SLA accountability."),
            ("Playbook Automation", "L1", "Templated resolution workflows that guide technicians through standardized procedures with automated substeps."),
            ("Cross-Client Problem Intelligence", "L1", "Pattern detection across all clients — when the same issue appears at multiple sites, proactive alerts trigger before tickets are created."),
        ],
        "screenshots": ["service-desk-dashboard", "service-desk-ticket-board", "service-desk-sla-dashboard", "service-desk-ai-triage"],
        "roles": [("service-desk-manager", "🎫", "Service Desk Manager"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director")],
        "connected": [("projects", "📋", "Projects"), ("analytics", "📈", "Analytics"), ("learning", "🎓", "Learning")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
    },
    {
        "num": 2, "slug": "projects", "name": "Projects",
        "icon": "📋", "accent": "#4F46E5",
        "tagline": "Phase-gated project execution with AI risk scoring, migration workflows, and CAB automation",
        "description": "The Projects zone manages everything from RFC submissions through hypercare stabilization. AI risk scoring evaluates every change request, phase-gated execution enforces quality milestones, and the M365 migration command center orchestrates complex tenant migrations.",
        "process_areas": [
            ("CAB Submissions &amp; AI Risk Scoring", "L2", "Every RFC is scored by AI across impact, complexity, and historical success rates. CAB reviewers see risk heat maps."),
            ("Discovery &amp; Assessment", "L1", "Pre-project discovery automation — environment scanning, dependency mapping, and stakeholder identification."),
            ("Phase-Gated Execution", "L2", "Structured project phases with mandatory gate reviews, deliverable checklists, and go/no-go automation."),
            ("Microsoft 365 Migration", "L2", "End-to-end M365 migration command center — mailbox, SharePoint, Teams, and identity federation workflows."),
            ("Batch Execution Engine", "L1", "Parallel task execution for large-scale operations — device enrollment, policy deployment, and configuration pushes."),
            ("Hypercare &amp; Stabilization", "L1", "Post-migration monitoring with automated issue detection, escalation paths, and client communication."),
            ("Working Sessions", "L2", "Collaborative session management with agenda templates, action item tracking, and automated meeting summaries."),
            ("Playbook Designer", "L2", "Visual workflow builder for creating reusable project playbooks with step templates and automation hooks."),
        ],
        "screenshots": ["projects-dashboard", "projects-gantt-chart", "projects-migration-dashboard", "hitl-cab-review"],
        "roles": [("project-manager", "📋", "Project Manager"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director")],
        "connected": [("service-desk", "🎫", "Service Desk"), ("network-ops", "🌐", "Network Ops"), ("endpoint-management", "💻", "Endpoints")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg>',
    },
    {
        "num": 3, "slug": "security-operations", "name": "Security Operations",
        "icon": "🛡️", "accent": "#DC2626",
        "tagline": "Unified SOC command center with incident response orchestration, detection engineering, and ZK Vault",
        "description": "Security Operations provides a unified SOC command center where 70-90% of Tier-1 alerts are auto-triaged by AI. Incident response orchestration, detection engineering, and the Zero-Knowledge Vault work together to maintain a defense-in-depth security posture across all managed clients.",
        "process_areas": [
            ("Incident Response Orchestration", "L2", "Structured incident workflows from detection through post-mortem — automated evidence collection, containment playbooks, and stakeholder notifications."),
            ("Detection Engineering", "L1", "Custom detection rule creation with AI-assisted SIGMA/KQL authoring, backtesting, and automated deployment to SIEM/XDR."),
            ("EDR/XDR Integration", "L1", "Unified endpoint detection across SentinelOne, Huntress, and Wazuh with correlated threat intelligence."),
            ("Zero-Knowledge Vault (ZK Vault)", "L3", "Cryptographically isolated credential storage — even platform operators cannot access stored secrets without client authorization."),
            ("Privileged Access Management (PAM)", "L2", "Just-in-time privileged access with session recording, automatic expiration, and approval workflows."),
            ("Dark Web Monitoring", "L0", "Continuous scanning of dark web sources for compromised credentials, data leaks, and brand impersonation."),
            ("BCDR Planning &amp; Testing", "L2", "Business continuity and disaster recovery plans with automated tabletop exercises and recovery testing."),
            ("Threat Intelligence Feeds", "L0", "Aggregated threat intelligence from multiple sources with automated IoC matching and contextual enrichment."),
        ],
        "screenshots": ["security-operations-dashboard", "security-soc-dashboard", "security-detection-engineering", "security-edr-dashboard"],
        "roles": [("security-analyst", "🛡️", "Security Analyst"), ("vciso", "🔒", "vCISO"), ("compliance-officer", "⚖️", "Compliance Officer")],
        "connected": [("grc-compliance", "⚖️", "GRC &amp; Compliance"), ("endpoint-management", "💻", "Endpoints"), ("network-ops", "🌐", "Network Ops")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    },
    {
        "num": 4, "slug": "grc-compliance", "name": "GRC &amp; Compliance",
        "icon": "⚖️", "accent": "#D97706",
        "tagline": "Automated gap analysis, OSCAL-native evidence, CMMC SSP builder, and continuous compliance monitoring",
        "description": "GRC &amp; Compliance eliminates the manual spreadsheet grind of compliance management. Collect evidence once and satisfy SOC 2, CMMC, HIPAA, and ISO 27001 simultaneously. The OSCAL-native engine generates machine-readable compliance artifacts that auditors can verify programmatically.",
        "process_areas": [
            ("Framework Lifecycle Management", "L2", "Manage multiple compliance frameworks with unified control mapping — SOC 2, CMMC, HIPAA, ISO 27001, PCI DSS."),
            ("OSCAL-Native Evidence", "L0", "Machine-readable compliance documents in NIST OSCAL format — automated evidence collection tied to control objectives."),
            ("Gap Analysis Engine", "L0", "AI-powered compliance gap detection across frameworks with prioritized remediation recommendations."),
            ("CMMC SSP Builder", "L2", "Guided CMMC System Security Plan creation with pre-populated controls, evidence links, and POA&amp;M tracking."),
            ("C3PAO Readiness Assessment", "L2", "Pre-audit self-assessment simulating C3PAO evaluation criteria with scoring and remediation guidance."),
            ("Audit Management", "L2", "End-to-end audit lifecycle — auditor portal, evidence request tracking, finding response, and remediation workflows."),
            ("Policy Management", "L1", "Policy lifecycle management with version control, approval workflows, attestation tracking, and automated distribution."),
            ("Continuous Monitoring", "L0", "Real-time compliance posture monitoring with drift detection and automated re-evidence collection."),
        ],
        "screenshots": ["grc-compliance-dashboard", "grc-evidence-collection"],
        "roles": [("compliance-officer", "⚖️", "Compliance Officer"), ("vciso", "🔒", "vCISO"), ("vcco", "📋", "vCCO")],
        "connected": [("security-operations", "🛡️", "Security Ops"), ("legal", "⚖️", "Legal"), ("analytics", "📈", "Analytics")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    },
    {
        "num": 5, "slug": "network-ops", "name": "Network Operations",
        "icon": "🌐", "accent": "#0891B2",
        "tagline": "SLO-based monitoring, live topology visualization, capacity forecasting, and SSL lifecycle management",
        "description": "Network Operations provides real-time visibility into every managed network — SLO-based monitoring replaces alert fatigue with meaningful service-level tracking, live topology visualization shows the current state of every device and link, and AI-powered capacity forecasting predicts bandwidth needs before clients notice degradation.",
        "process_areas": [
            ("SLO Management", "L1", "Service-level objective tracking with automated reporting, breach prediction, and escalation triggers."),
            ("Topology Visualization", "L0", "Live network topology maps with device status, link utilization, and change history overlays."),
            ("Capacity Forecasting", "L1", "AI-powered bandwidth and resource utilization forecasting with upgrade recommendation timelines."),
            ("SSL Certificate Management", "L0", "Automated SSL certificate discovery, expiration tracking, and renewal orchestration across all clients."),
            ("Ring-Based Patch Management", "L2", "Progressive patch deployment using ring-based rollout — canary, early adopters, broad deployment with automated rollback."),
            ("Network Configuration Management", "L2", "Centralized network device configuration with version control, drift detection, and compliance auditing."),
            ("Performance Monitoring", "L0", "Real-time network performance metrics — latency, jitter, packet loss, throughput — with baseline deviation alerting."),
        ],
        "screenshots": ["network-ops-dashboard", "network-topology"],
        "roles": [("network-engineer", "🌐", "Network Engineer"), ("it-director", "🖥️", "IT Director"), ("msp-owner", "🏢", "MSP Owner / CEO")],
        "connected": [("endpoint-management", "💻", "Endpoints"), ("security-operations", "🛡️", "Security Ops"), ("service-desk", "🎫", "Service Desk")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="2"/><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg>',
    },
    {
        "num": 6, "slug": "endpoint-management", "name": "Endpoint Management",
        "icon": "💻", "accent": "#16A34A",
        "tagline": "Intune management, automated patching, device lifecycle operations, and fleet intelligence",
        "description": "Endpoint Management unifies device operations across the entire fleet — from initial enrollment through retirement. Intune compliance enforcement, automated patching orchestration, and fleet intelligence dashboards give IT directors complete visibility into every managed endpoint.",
        "process_areas": [
            ("Intune Management &amp; Compliance", "L1", "Microsoft Intune policy management with compliance scoring, configuration profiles, and conditional access enforcement."),
            ("Infrastructure Monitoring", "L0", "Unified infrastructure monitoring dashboards — server health, storage utilization, and service availability."),
            ("Device Lifecycle Management", "L2", "End-to-end device lifecycle from procurement through decommission — asset tracking, warranty management, refresh planning."),
            ("Automated Patching", "L1", "Intelligent patch orchestration with compliance scoring, ring-based deployment, and automated rollback on failure."),
            ("Vulnerability Management", "L1", "Continuous vulnerability scanning with risk-based prioritization and remediation workflow integration."),
            ("DNS Filtering", "L1", "DNS-layer security filtering with category-based policies, threat blocking, and per-client configuration."),
            ("Remote Access &amp; Support", "L0", "Secure remote access tooling with session recording, consent management, and technician routing."),
            ("Fleet Intelligence", "L0", "AI-powered fleet analytics — hardware age distribution, OS version adoption, compliance drift, and capacity planning."),
        ],
        "screenshots": ["endpoint-management-dashboard"],
        "roles": [("it-director", "🖥️", "IT Director"), ("network-engineer", "🌐", "Network Engineer"), ("security-analyst", "🛡️", "Security Analyst")],
        "connected": [("network-ops", "🌐", "Network Ops"), ("security-operations", "🛡️", "Security Ops"), ("service-desk", "🎫", "Service Desk")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    },
    {
        "num": 7, "slug": "accounting", "name": "Accounting",
        "icon": "📊", "accent": "#059669",
        "tagline": "Automated invoice ingestion, three-way reconciliation, contract lifecycle management, and revenue recognition",
        "description": "The Accounting zone automates the financial backbone of MSP operations — from invoice ingestion through revenue recognition. Three-way reconciliation matches contracts, usage data, and invoices automatically, while AI flags discrepancies before they become billing disputes.",
        "process_areas": [
            ("Invoice Ingestion &amp; Processing", "L0", "Automated invoice capture via email, portal, and API with OCR extraction, validation, and GL coding."),
            ("Three-Way Billing Reconciliation", "L1", "Contract terms ↔ usage data ↔ invoice validation with discrepancy flagging and automated resolution."),
            ("Contract Lifecycle Management", "L2", "Contract creation, negotiation tracking, renewal management, and automated compliance verification."),
            ("Procurement Automation", "L2", "Purchase requisition workflows with approval routing, vendor comparison, and budget impact analysis."),
            ("Revenue Recognition", "L1", "ASC 606-compliant revenue recognition with performance obligation tracking and deferred revenue management."),
            ("GL Integration", "L1", "Bi-directional general ledger synchronization with QuickBooks, Xero, and enterprise ERP systems."),
            ("CPQ (Configure, Price, Quote)", "L1", "AI-assisted quoting with dynamic pricing, bundling recommendations, and margin analysis."),
            ("Subscription Management", "L1", "Recurring billing management with usage metering, tier upgrades/downgrades, and churn prediction."),
        ],
        "screenshots": ["accounting-dashboard", "accounting-reconciliation"],
        "roles": [("finance-coordinator", "💰", "Finance Coordinator"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("account-manager", "🤝", "Account Manager")],
        "connected": [("relationships", "🤝", "Relationships"), ("analytics", "📈", "Analytics"), ("vc-suite", "🧭", "vC-Suite")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    },
    {
        "num": 8, "slug": "relationships", "name": "Relationships",
        "icon": "🤝", "accent": "#7C3AED",
        "tagline": "Sales pipeline management, ICP scoring, marketing orchestration, and client health scoring",
        "description": "The Relationships zone manages the entire client lifecycle — from lead generation through expansion and renewal. AI-powered ICP scoring identifies ideal prospects, client health scoring predicts churn before it happens, and QBR automation transforms quarterly reviews from dreaded admin into strategic conversations.",
        "process_areas": [
            ("Lead Generation &amp; ICP Scoring", "L1", "AI-driven Ideal Client Profile matching with lead scoring, enrichment, and prioritized outreach recommendations."),
            ("Sales Pipeline Management", "L1", "Visual pipeline tracking with stage automation, probability forecasting, and bottleneck detection."),
            ("Marketing Campaign Orchestration", "L2", "Multi-channel campaign management with audience segmentation, content scheduling, and performance analytics."),
            ("Client Onboarding Workflows", "L2", "Structured onboarding with checklist automation, stakeholder introductions, and service activation verification."),
            ("QBR Preparation &amp; Delivery", "L1", "AI-aggregated quarterly business reviews — metrics compilation, presentation generation, and action item tracking."),
            ("Client Health Scoring", "L0", "Composite health scores from ticket volume, SLA performance, engagement metrics, and sentiment analysis."),
            ("Churn Risk Detection", "L0", "Predictive churn modeling using behavioral signals, satisfaction trends, and contract utilization patterns."),
            ("Referral &amp; Expansion Tracking", "L1", "NPS-driven referral program management with upsell opportunity identification and expansion revenue tracking."),
        ],
        "screenshots": [],
        "roles": [("account-manager", "🤝", "Account Manager"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("vcio", "🧭", "vCIO")],
        "connected": [("accounting", "📊", "Accounting"), ("analytics", "📈", "Analytics"), ("vc-suite", "🧭", "vC-Suite")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    },
    {
        "num": 9, "slug": "vc-suite", "name": "vC-Suite",
        "icon": "🧭", "accent": "#475569",
        "tagline": "Executive KPI dashboards, technology roadmap management, and strategic advisory engines for vCIO/vCISO/vCCO/vCTO",
        "description": "The vC-Suite provides dedicated advisory engines for virtual C-level roles — vCIO, vCISO, vCCO, and vCTO. Each advisory engine aggregates cross-zone data into executive-ready insights, strategic recommendations, and board-level reporting.",
        "process_areas": [
            ("vCIO Advisory Engine", "L2", "Technology roadmap management with budget planning, vendor evaluation, and digital transformation recommendations."),
            ("vCTO Architecture Reviews", "L2", "Technical architecture assessment with security posture scoring, scalability analysis, and modernization roadmaps."),
            ("vCISO Security Program", "L2", "Security program leadership — risk register management, security roadmap, and compliance program oversight."),
            ("vCCO Compliance Governance", "L2", "Regulatory landscape monitoring with compliance program maturity scoring and board reporting."),
            ("Executive KPI Dashboards", "L0", "Cross-zone executive dashboards with drill-down capabilities and trend analysis."),
            ("Technology Roadmap Management", "L2", "Multi-year technology roadmaps with budget allocation, milestone tracking, and stakeholder communication."),
            ("Client Profitability Analysis", "L1", "Per-client profitability modeling with cost allocation, margin analysis, and pricing optimization."),
            ("Strategic Recommendations", "L1", "AI-generated strategic recommendations based on cross-zone operational data and industry benchmarks."),
        ],
        "screenshots": ["vc-suite-dashboard", "vc-suite-advisory"],
        "roles": [("vcio", "🧭", "vCIO"), ("vciso", "🔒", "vCISO"), ("vcco", "📋", "vCCO"), ("msp-owner", "🏢", "MSP Owner / CEO")],
        "connected": [("analytics", "📈", "Analytics"), ("accounting", "📊", "Accounting"), ("grc-compliance", "⚖️", "GRC &amp; Compliance")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    },
    {
        "num": 10, "slug": "analytics", "name": "Analytics",
        "icon": "📈", "accent": "#EA580C",
        "tagline": "QBR aggregation, churn prediction, cross-domain correlation, and natural language BI queries",
        "description": "The Analytics zone is the intelligence layer of DevOps AI — aggregating data across all zones to surface actionable insights. Natural language BI queries let anyone ask questions in plain English, churn prediction identifies at-risk clients before they leave, and cross-domain correlation reveals hidden patterns across operations.",
        "process_areas": [
            ("QBR Aggregation Engine", "L0", "Automated quarterly business review data compilation from all zones — metrics, trends, and recommendations."),
            ("Churn Prediction Model", "L0", "Machine learning churn prediction using behavioral signals, satisfaction metrics, and engagement patterns."),
            ("Ticket Volume Forecasting", "L0", "Predictive ticket volume modeling by client, category, and time period for staffing optimization."),
            ("Security Risk Scoring", "L0", "Composite security risk scores per client using vulnerability data, compliance posture, and threat intelligence."),
            ("Natural Language BI Queries", "L0", "Ask questions in plain English — 'Show me our top 5 clients by ticket volume this quarter' — and get instant visualizations."),
            ("Automated Report Generation", "L1", "Scheduled report generation with dynamic content assembly, chart rendering, and distribution."),
            ("Cross-Domain Correlation", "L1", "Pattern detection across zones — correlating ticket spikes with patch deployments, or churn risk with SLA performance."),
            ("Benchmark Intelligence", "L1", "Industry benchmark comparisons — how does each client's environment compare to peers in their vertical?"),
        ],
        "screenshots": ["analytics-dashboard", "analytics-churn-prediction", "analytics-cross-domain"],
        "roles": [("msp-owner", "🏢", "MSP Owner / CEO"), ("vcio", "🧭", "vCIO"), ("it-director", "🖥️", "IT Director")],
        "connected": [("vc-suite", "🧭", "vC-Suite"), ("relationships", "🤝", "Relationships"), ("service-desk", "🎫", "Service Desk")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    },
    {
        "num": 11, "slug": "devops", "name": "DevOps",
        "icon": "⚙️", "accent": "#6B7280",
        "tagline": "Feature flags, A/B testing, connector toolkit, SRE golden signals, and integration health monitoring",
        "description": "The DevOps zone is the platform's own operational backbone — managing feature flags, A/B testing infrastructure, the connector development toolkit, and SRE golden signals monitoring. This is where the platform itself is continuously improved and where third-party integrations are built and monitored.",
        "process_areas": [
            ("Feature Flag Management", "L2", "Gradual feature rollout with targeting rules, percentage deployment, and instant kill switches."),
            ("A/B Testing Framework", "L2", "Multivariate testing infrastructure with statistical significance calculation and automated winner selection."),
            ("Connector Toolkit", "L2", "SDK and development environment for building third-party integrations with the DevOps AI platform."),
            ("SRE Golden Signals", "L0", "Platform reliability monitoring — latency, traffic, errors, saturation — with SLO-based alerting."),
            ("Bottleneck Detection", "L0", "AI-powered performance analysis identifying processing bottlenecks across the platform."),
            ("Configuration Management", "L2", "Platform configuration versioning with diff visualization, rollback, and approval workflows."),
            ("Environment Lifecycle", "L2", "Development, staging, and production environment management with promotion pipelines."),
            ("Integration Health Dashboard", "L0", "Real-time health monitoring for all active integrations with error rate tracking and automatic failover."),
        ],
        "screenshots": ["devops-dashboard"],
        "roles": [("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director")],
        "connected": [("analytics", "📈", "Analytics"), ("service-desk", "🎫", "Service Desk"), ("learning", "🎓", "Learning")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    },
    {
        "num": 12, "slug": "learning", "name": "Learning",
        "icon": "🎓", "accent": "#0D9488",
        "tagline": "LMS engine, AI tutoring, certification tracking, compliance training, and skill gap analysis",
        "description": "The Learning zone powers continuous education across the organization — from structured LMS curricula through AI-powered tutoring. Certification tracking ensures compliance training stays current, skill gap analysis identifies development priorities, and onboarding journeys activate new team members faster.",
        "process_areas": [
            ("LMS Engine", "L1", "Full-featured learning management with course authoring, enrollment management, and progress tracking."),
            ("AI Tutoring", "L0", "Context-aware AI tutoring that adapts to the learner's role, skill level, and learning pace."),
            ("Certification Tracking", "L0", "Automated certification expiration monitoring with renewal reminders and compliance evidence."),
            ("Knowledge Store", "L1", "Centralized knowledge repository with AI-powered search, content recommendations, and usage analytics."),
            ("Compliance Training", "L1", "Mandatory training management with SCORM/xAPI tracking, attestation collection, and audit evidence."),
            ("SOP &amp; Runbook Management", "L1", "Standard operating procedure versioning with approval workflows and contextual in-app surfacing."),
            ("Skill Gap Analysis", "L1", "AI-powered skill assessment across teams with personalized development recommendations."),
            ("Onboarding Journeys", "L1", "Structured onboarding paths for new team members with role-specific curricula and milestone tracking."),
        ],
        "screenshots": ["learning-dashboard"],
        "roles": [("hr-director", "👤", "HR Director"), ("msp-owner", "🏢", "MSP Owner / CEO"), ("compliance-officer", "⚖️", "Compliance Officer")],
        "connected": [("people", "👥", "People"), ("grc-compliance", "⚖️", "GRC &amp; Compliance"), ("service-desk", "🎫", "Service Desk")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    },
    {
        "num": 13, "slug": "organization", "name": "Organization",
        "icon": "🏢", "accent": "#1F2937",
        "tagline": "Organizational structure management, department hierarchy, multi-tenant administration, and white-label branding",
        "description": "The Organization zone manages the structural foundation of every managed client — department hierarchies, cost centers, location management, and multi-tenant boundaries. This is where organizational context is defined so every other zone can operate with proper scope and access control.",
        "process_areas": [
            ("Department Hierarchy Management", "L2", "Define and maintain organizational structure with departments, teams, and reporting relationships used across all zones."),
            ("Multi-Tenant Administration", "L3", "Client tenant provisioning, isolation verification, and cross-tenant operations for MSPs managing multiple organizations."),
            ("Cost Center Management", "L2", "Cost center definitions mapped to departments, projects, and billing entities for accurate financial allocation."),
            ("Location &amp; Site Management", "L2", "Physical and virtual site management with timezone handling, regional compliance requirements, and service delivery scope."),
            ("Organizational Policy Framework", "L2", "Organization-wide policy definitions that cascade to all zones — data handling, access control, communication preferences."),
            ("Branding &amp; White-Label", "L2", "Per-organization branding customization — logos, colors, email templates, and portal themes."),
        ],
        "screenshots": [],
        "roles": [("msp-owner", "🏢", "MSP Owner / CEO"), ("it-director", "🖥️", "IT Director"), ("hr-director", "👤", "HR Director")],
        "connected": [("people", "👥", "People"), ("accounting", "📊", "Accounting"), ("grc-compliance", "⚖️", "GRC &amp; Compliance")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>',
    },
    {
        "num": 14, "slug": "people", "name": "People",
        "icon": "👥", "accent": "#8B5CF6",
        "tagline": "Employee onboarding automation, access lifecycle management, workforce analytics, and directory synchronization",
        "description": "The People zone manages the human element of IT operations — from employee onboarding through offboarding. Automated access lifecycle management ensures the right people have the right access at the right time, while workforce analytics provide visibility into team capacity, utilization, and development needs.",
        "process_areas": [
            ("Employee Onboarding Automation", "L2", "Structured onboarding workflows with identity provisioning, access grants, device enrollment, and training enrollment."),
            ("Access Lifecycle Management", "L2", "Continuous access review with risk-based certification, orphaned account detection, and automated remediation."),
            ("Offboarding &amp; Access Revocation", "L2", "Comprehensive offboarding checklists with cascading access revocation, device recovery, and knowledge transfer."),
            ("Workforce Analytics", "L0", "Team capacity and utilization analytics with skill mapping, workload distribution, and development tracking."),
            ("Directory Synchronization", "L1", "Bi-directional sync with Azure AD, on-premises AD, and HR systems for a single source of truth."),
            ("Contractor &amp; Vendor Access", "L2", "Time-bounded vendor and contractor access with approval workflows, session monitoring, and automatic expiration."),
        ],
        "screenshots": [],
        "roles": [("hr-director", "👤", "HR Director"), ("recruiter", "📋", "Recruiter"), ("it-director", "🖥️", "IT Director")],
        "connected": [("organization", "🏢", "Organization"), ("learning", "🎓", "Learning"), ("security-operations", "🛡️", "Security Ops")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    },
    {
        "num": 15, "slug": "legal", "name": "Legal",
        "icon": "⚖️", "accent": "#B45309",
        "tagline": "Contract analysis, regulatory change monitoring, data privacy management, and IP tracking",
        "description": "The Legal zone provides AI-assisted legal operations — from contract analysis through regulatory change monitoring. AI reviews contracts for risk clauses, tracks regulatory changes relevant to your clients' industries, and manages data privacy obligations across jurisdictions.",
        "process_areas": [
            ("Contract Analysis &amp; Review", "L3", "AI-assisted contract review with risk clause identification, obligation extraction, and comparison against standard terms."),
            ("Regulatory Change Monitoring", "L1", "Automated monitoring of regulatory changes with impact assessment across the client portfolio."),
            ("Data Privacy Management", "L2", "GDPR, CCPA, and cross-jurisdiction privacy obligation tracking with data mapping and DSAR workflow automation."),
            ("Incident Legal Response", "L3", "Legal response coordination for security incidents — breach notification requirements, regulatory obligations, and evidence preservation."),
            ("NDA &amp; Vendor Agreement Management", "L2", "Template-based NDA and vendor agreement generation with approval routing and obligation tracking."),
            ("Intellectual Property Tracking", "L2", "IP portfolio management — patents, trademarks, trade secrets — with renewal tracking and infringement monitoring."),
        ],
        "screenshots": [],
        "roles": [("compliance-officer", "⚖️", "Compliance Officer"), ("vcco", "📋", "vCCO"), ("msp-owner", "🏢", "MSP Owner / CEO")],
        "connected": [("grc-compliance", "⚖️", "GRC &amp; Compliance"), ("people", "👥", "People"), ("organization", "🏢", "Organization")],
        "svg": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
    },
]

# ─── Workflow Screenshots ────────────────────────────────────────────────────
# Organized by tag/role for the connector section replacement
WORKFLOW_CATEGORIES = [
    {
        "label": "Service Desk Workflows",
        "tag": "Service Desk Manager · IT Director",
        "items": [
            {"img": "service-desk-dashboard", "alt": "Service Desk zone dashboard — real-time ticket queue with AI routing, SLA compliance gauges, and CSAT trending", "caption": "Zone Dashboard — Real-time queue management with AI routing intelligence"},
            {"img": "service-desk-ticket-board", "alt": "AI-triaged ticket board with priority lanes, assignee routing, and resolution timers", "caption": "Ticket Board — Priority lanes with AI-assigned routing and SLA countdown"},
        ]
    },
    {
        "label": "Security &amp; Compliance Workflows",
        "tag": "Security Analyst · vCISO · Compliance Officer",
        "items": [
            {"img": "security-operations-dashboard", "alt": "SOC command center with threat timeline, active incidents, and detection coverage map", "caption": "SOC Command Center — Unified threat timeline with detection coverage"},
            {"img": "grc-evidence-collection", "alt": "GRC evidence collection dashboard with framework progress bars and automated collection status", "caption": "Evidence Collection — Automated compliance evidence across frameworks"},
        ]
    },
    {
        "label": "Executive &amp; Advisory Workflows",
        "tag": "MSP Owner · vCIO · vCISO · vCCO",
        "items": [
            {"img": "vc-suite-dashboard", "alt": "Executive KPI dashboard with cross-zone metrics, profitability analysis, and strategic recommendations", "caption": "Executive Dashboard — Cross-zone KPIs with AI strategic recommendations"},
            {"img": "vc-suite-advisory", "alt": "vCIO advisory engine with technology roadmap, budget planning, and client advisory preparation", "caption": "Advisory Engine — Technology roadmap with budget allocation and milestones"},
        ]
    },
    {
        "label": "Project &amp; Change Workflows",
        "tag": "Project Manager · Network Engineer",
        "items": [
            {"img": "projects-dashboard", "alt": "Projects zone dashboard with active projects, phase-gate status, and resource allocation", "caption": "Project Command Center — Phase-gated execution with resource tracking"},
            {"img": "hitl-cab-review", "alt": "Change Advisory Board review interface with AI risk scoring and approval workflow", "caption": "CAB Review — AI risk scoring with human-in-the-loop approval gates"},
        ]
    },
    {
        "label": "Infrastructure &amp; Monitoring Workflows",
        "tag": "Network Engineer · IT Director",
        "items": [
            {"img": "network-ops-dashboard", "alt": "Network operations dashboard with SLO tracking, device health, and bandwidth utilization", "caption": "Network Operations — SLO-based monitoring with capacity intelligence"},
            {"img": "endpoint-management-dashboard", "alt": "Endpoint management dashboard with fleet compliance, patch status, and device lifecycle tracking", "caption": "Fleet Management — Endpoint compliance with automated patching status"},
        ]
    },
    {
        "label": "Analytics &amp; Intelligence Workflows",
        "tag": "MSP Owner · vCIO · Account Manager",
        "items": [
            {"img": "analytics-dashboard", "alt": "Analytics zone dashboard with cross-domain metrics, trend analysis, and natural language BI", "caption": "Analytics Hub — Cross-domain correlation with natural language queries"},
            {"img": "analytics-churn-prediction", "alt": "Churn prediction model with risk scoring, behavioral signals, and intervention recommendations", "caption": "Churn Intelligence — Predictive risk scoring with intervention triggers"},
        ]
    },
    {
        "label": "Human-in-the-Loop Control Planes",
        "tag": "All Roles · HITL Governance",
        "items": [
            {"img": "hitl-approval-pending", "alt": "HITL approval gate — AI proposes action, human reviews and approves before execution", "caption": "Approval Gate — AI proposes, human reviews and authorizes execution"},
            {"img": "hitl-incident-response", "alt": "Incident response HITL workflow with severity classification and coordinated response", "caption": "Incident Response — Coordinated response with severity-based escalation"},
        ]
    },
]

# ─── HITL Levels ─────────────────────────────────────────────────────────────
HITL_MAP = {
    "L0": ("hitl-badge--l0", "Fully Automated"),
    "L1": ("hitl-badge--l1", "Notify"),
    "L2": ("hitl-badge--l2", "Approve to Proceed"),
    "L3": ("hitl-badge--l3", "Human Only"),
}

def hitl_badge(level):
    cls, label = HITL_MAP[level]
    return f'<span class="hitl-badge {cls}" title="{label}">{level} — {label}</span>'

def zone_card(z):
    """Generate one complete zone entry point card."""
    pa_html = ""
    for name, hitl, desc in z["process_areas"][:4]:
        pa_html += f'''
              <div class="zone-pa-card">
                <div class="zone-pa-header">
                  <span class="zone-pa-name">{name}</span>
                  {hitl_badge(hitl)}
                </div>
                <p class="zone-pa-desc">{desc}</p>
              </div>'''

    remaining = len(z["process_areas"]) - 4
    if remaining > 0:
        pa_html += f'''
              <div class="zone-pa-more">+ {remaining} more process areas in zone deep dive</div>'''

    # Screenshots (max 2 in the card)
    ss_html = ""
    if z["screenshots"]:
        shots = z["screenshots"][:2]
        ss_html = '<div class="zone-screenshots">'
        for s in shots:
            ss_html += f'''
              <figure class="zone-ss-fig">
                <img src="assets/screenshots/{s}.png" alt="{z['name']} — platform screenshot" loading="lazy" width="800" height="450">
              </figure>'''
        ss_html += '</div>'

    # Related roles
    roles_html = '<div class="zone-roles">'
    for slug, icon, name in z["roles"]:
        roles_html += f'<a href="roles/{slug}.html" class="zone-role-chip"><span>{icon}</span> {name}</a>'
    roles_html += '</div>'

    # Connected zones
    conn_html = '<div class="zone-connected">'
    for slug, icon, name in z["connected"]:
        conn_html += f'<a href="zones/{slug}.html" class="zone-conn-chip"><span>{icon}</span> {name}</a>'
    conn_html += '</div>'

    return f'''
        <article class="zone-entry fade-up" style="--zone-accent: {z['accent']};" id="zone-{z['slug']}">
          <div class="zone-entry__header">
            <div class="zone-entry__badge">
              <span class="zone-entry__icon">{z['icon']}</span>
              <span class="zone-entry__number">Zone {z['num']:02d}</span>
            </div>
            <div class="zone-entry__titles">
              <h3 class="zone-entry__name">{z['name']}</h3>
              <p class="zone-entry__tagline">{z['tagline']}</p>
            </div>
          </div>
          <div class="zone-entry__body">
            <p class="zone-entry__desc">{z['description']}</p>
            <div class="zone-entry__section">
              <h4 class="zone-entry__section-title">Process Areas <span class="zone-pa-count">{len(z['process_areas'])}</span></h4>
              <div class="zone-pa-grid">{pa_html}
              </div>
            </div>
            {ss_html}
            <div class="zone-entry__meta">
              <div class="zone-meta-col">
                <span class="zone-meta-label">Relevant Roles</span>
                {roles_html}
              </div>
              <div class="zone-meta-col">
                <span class="zone-meta-label">Connected Zones</span>
                {conn_html}
              </div>
            </div>
            <a href="zones/{z['slug']}.html" class="zone-entry__cta">
              Explore {z['name']} Zone
              <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 10h10m-4-4 4 4-4 4"/></svg>
            </a>
          </div>
        </article>'''

def workflow_gallery():
    """Generate the workflow screenshot gallery."""
    html = ""
    for cat in WORKFLOW_CATEGORIES:
        items_html = ""
        for item in cat["items"]:
            items_html += f'''
            <figure class="wf-screenshot">
              <img src="assets/screenshots/{item['img']}.png" alt="{item['alt']}" loading="lazy" width="1600" height="900">
              <figcaption>{item['caption']}</figcaption>
            </figure>'''

        html += f'''
        <div class="wf-category fade-up">
          <div class="wf-category__header">
            <h3 class="wf-category__title">{cat['label']}</h3>
            <span class="wf-category__tag">{cat['tag']}</span>
          </div>
          <div class="wf-category__grid">{items_html}
          </div>
        </div>'''
    return html


# ─── Read existing header/footer from the current file ──────────────────────
# We'll build the complete page

with open("platform.html", "r") as f:
    existing = f.read()

# Extract header (lines 1-170) and footer (515-end) from existing
lines = existing.split("\n")

# Get header through </header>
header_end = None
for i, line in enumerate(lines):
    if "</header>" in line:
        header_end = i + 1
        break

# Get footer from </main>
footer_start = None
for i, line in enumerate(lines):
    if "</main>" in line:
        footer_start = i
        break

header_html = "\n".join(lines[:header_end])
footer_html = "\n".join(lines[footer_start:])

# ─── Build the complete page ─────────────────────────────────────────────────

# Fix the title to say 17-zone
header_html = header_html.replace("12-Zone Architecture", "17-Zone Architecture")
header_html = header_html.replace("15 operational zones", "17 operational zones")

# Zone cards
zone_cards = ""
for z in ZONES:
    zone_cards += zone_card(z)

# Workflow gallery
wf_gallery = workflow_gallery()

main_content = f'''
<main id="main-content">

  <!-- PAGE HERO -->
  <section class="page-hero">
    <div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a> <span class="sep">/</span> <span aria-current="page">Platform</span>
      </nav>
      <h1 class="fade-up">Platform Deep&nbsp;Dive</h1>
      <p class="fade-up">A comprehensive look at the 17-zone architecture, AI orchestration engine, cross-zonal workflow gallery, and technology stack that powers DevOps&nbsp;AI.</p>
    </div>
  </section>

  <!-- 17-ZONE JOURNEY ENTRY POINTS -->
  <section class="section" id="zones" aria-label="17-Zone Architecture">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Architecture</span>
        <h2>17 Operational Zones</h2>
        <p>Each zone is a fully featured control plane module with dedicated process areas, HITL governance gates, and cross-zone integrations. Select any zone to explore its complete journey.</p>
      </div>

      <div class="zone-entry-grid">{zone_cards}
      </div>
    </div>
  </section>

  <!-- AI ORCHESTRATION -->
  <section class="section" style="background:var(--bg-secondary);" aria-label="AI Orchestration">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Intelligence</span>
        <h2>AI Orchestration Engine</h2>
        <p>Multi-model routing, chain-of-thought reasoning, and safety gates — ensuring every AI action is explainable, auditable, and approved.</p>
      </div>
      <div class="diff-grid">
        <div class="diff-card fade-up">
          <div class="diff-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v4m0 14v4m-8.66-15 3.46 2m10.4 6 3.46 2M1 12h4m14 0h4"/></svg></div>
          <h3>Multi-Model Routing</h3>
          <p>Cost-effective routing via Azure OpenAI — the engine selects the optimal model for each task, balancing capability, cost, and latency.</p>
        </div>
        <div class="diff-card fade-up">
          <div class="diff-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
          <h3>Chain-of-Thought Reasoning</h3>
          <p>Every AI decision includes a transparent reasoning chain — visible to operators and archived for compliance auditing.</p>
        </div>
        <div class="diff-card fade-up">
          <div class="diff-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg></div>
          <h3>Safety Gates</h3>
          <p>Human-in-the-loop approval for all significant actions. Configurable escalation thresholds with RBAC-based authorization.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CROSS-ZONAL WORKFLOW GALLERY -->
  <section class="section" id="workflows" aria-label="Cross-Zonal Workflow Gallery">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Workflows in Action</span>
        <h2>Cross-Zonal Workflow Gallery</h2>
        <p>Real screens from the DevOps AI control planes — populated with representative data. Each workflow demonstrates how zones interconnect through the AI orchestration layer.</p>
      </div>
      <div class="wf-gallery">{wf_gallery}
      </div>
    </div>
  </section>

  <!-- TECH STACK / ARCHITECTURE DIAGRAM -->
  <section class="section" style="background:var(--bg-secondary);" aria-label="Technology Stack">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Stack</span>
        <h2>Technology Architecture</h2>
        <p>Enterprise-grade infrastructure built on Azure — with full data sovereignty and zero public endpoints.</p>
      </div>
      <div class="arch-diagram fade-up">
        <div class="arch-layer arch-layer--ai">
          <span class="arch-label">AI Layer</span>
          <div class="arch-items">
            <span>Azure OpenAI</span>
            <span>Multi-Model Routing</span>
            <span>CoT Reasoning</span>
            <span>HITL Safety Gates</span>
          </div>
        </div>
        <div class="arch-layer arch-layer--data">
          <span class="arch-label">Application</span>
          <div class="arch-items">
            <span>FastAPI (Python 3.11+)</span>
            <span>React 18 / TypeScript</span>
            <span>Fluent UI v9</span>
            <span>Pydantic v2</span>
          </div>
        </div>
        <div class="arch-layer arch-layer--infra">
          <span class="arch-label">Data &amp; Messaging</span>
          <div class="arch-items">
            <span>Azure Cosmos DB</span>
            <span>PostgreSQL</span>
            <span>Redis Cache</span>
            <span>Azure Service Bus</span>
            <span>Event Hub</span>
            <span>Azure Blob Storage</span>
          </div>
        </div>
        <div class="arch-layer arch-layer--security">
          <span class="arch-label">Infrastructure</span>
          <div class="arch-items">
            <span>Azure Kubernetes Service</span>
            <span>Azure Firewall Premium</span>
            <span>Private Endpoints</span>
            <span>Private DNS</span>
            <span>MSAL / Azure AD B2C</span>
            <span>GitHub Actions CI/CD</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CONNECTOR ECOSYSTEM -->
  <section class="section" id="connectors" aria-label="Connector Ecosystem">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Integrations</span>
        <h2>Connector Ecosystem</h2>
        <p>DevOps AI orchestrates the tools your MSP already uses — no rip-and-replace required.</p>
      </div>
      <div class="connector-grid fade-up">
        <span class="connector-chip">NinjaRMM</span>
        <span class="connector-chip">ConnectWise</span>
        <span class="connector-chip">ServiceNow</span>
        <span class="connector-chip">Autotask / Datto</span>
        <span class="connector-chip">NinjaOne</span>
        <span class="connector-chip">Huntress</span>
        <span class="connector-chip">SentinelOne</span>
        <span class="connector-chip">Veeam</span>
        <span class="connector-chip">Microsoft Intune</span>
        <span class="connector-chip">Wazuh</span>
        <span class="connector-chip">SharePoint</span>
        <span class="connector-chip">Azure DevOps</span>
        <span class="connector-chip">Pax8</span>
        <span class="connector-chip">HubSpot</span>
        <span class="connector-chip">QuickBooks / Xero</span>
        <span class="connector-chip">Gradient MSP</span>
        <span class="connector-chip">ScalePad</span>
        <span class="connector-chip">myITprocess</span>
        <span class="connector-chip">Drata / Vanta</span>
        <span class="connector-chip">GitHub</span>
        <span class="connector-chip">IT Glue / Hudu</span>
        <span class="connector-chip">Auvik</span>
        <span class="connector-chip">Inforcer</span>
        <span class="connector-chip">N8N / Roost</span>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>Experience the Platform</h2>
        <p>Deploy DevOps AI into your Azure tenant in under 35 minutes — fully private, fully yours.</p>
        <a href="marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
      </div>
    </div>
  </section>

'''

output = header_html + "\n" + main_content + "\n" + footer_html

with open("platform.html", "w") as f:
    f.write(output)

print(f"Generated platform.html — {len(output)} bytes, {len(ZONES)} zones")
