#!/usr/bin/env python3
"""DevOps AI Website Generator — Complete Site Restructure.

Generates all zone pages, role pages, and structural pages from
authoritative taxonomy data extracted from the DevOps-AI backend.
"""
import os
import json
from datetime import datetime

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

# ═══════════════════════════════════════════════════════════════════════
# ZONE DATA — Authoritative source: control_plane_taxonomy.py
# ═══════════════════════════════════════════════════════════════════════

ZONES = {
    "service_desk": {
        "number": 1, "label": "Service Desk", "slug": "service-desk",
        "accent": "#2563EB", "icon": "🎫",
        "tagline": "AI-augmented ticket management, SLA optimization, and predictive support operations",
        "description": "The Service Desk is the operational heartbeat of every MSP. DevOps AI transforms reactive ticket queues into predictive, AI-augmented support operations — routing tickets intelligently, surfacing known-error solutions before technicians search for them, and predicting SLA breaches before they happen.",
        "process_areas": [
            {"name": "Ticket Ingestion & AI Triage", "hitl": "L0", "desc": "Automated ticket classification, priority scoring, and intelligent routing based on technician skills, workload, and client SLA tiers."},
            {"name": "Known Error Database (KEDB)", "hitl": "L0", "desc": "AI-maintained knowledge base that surfaces matching solutions as tickets are created. Self-healing when new resolutions are confirmed."},
            {"name": "SLA Management & Prediction", "hitl": "L1", "desc": "Real-time SLA tracking with predictive breach alerts. Automated escalation triggers when resolution targets are at risk."},
            {"name": "Dispatch Optimization", "hitl": "L1", "desc": "AI-optimized technician assignment considering skills matrix, current workload, client proximity, and specialization."},
            {"name": "CSAT Collection & Analysis", "hitl": "L0", "desc": "Automated satisfaction surveys post-resolution with sentiment analysis and trend detection across clients."},
            {"name": "Co-Managed IT Workflows", "hitl": "L2", "desc": "Shared ticket queues between MSP and client internal IT with role-based visibility, handoff protocols, and SLA accountability."},
            {"name": "Playbook Automation", "hitl": "L1", "desc": "Templated resolution workflows that guide technicians through standardized procedures with automated substeps."},
            {"name": "Cross-Client Problem Intelligence", "hitl": "L1", "desc": "Pattern detection across all clients — when the same issue appears at multiple sites, proactive alerts trigger before tickets are even created."},
        ],
        "related_roles": ["service_desk_manager", "msp_owner", "it_director"],
        "related_zones": ["projects", "analytics", "learning"],
    },
    "projects": {
        "number": 2, "label": "Projects", "slug": "projects",
        "accent": "#4F46E5", "icon": "📋",
        "tagline": "Migration command center with CAB governance, AI risk scoring, and phase-gated execution",
        "description": "The Projects zone is where complex IT initiatives come to life — from M365 migrations to infrastructure overhauls. DevOps AI provides a complete project command center with Change Advisory Board (CAB) governance, AI-powered risk scoring, phase-gated execution, and real-time stakeholder visibility.",
        "process_areas": [
            {"name": "CAB Submissions & AI Risk Scoring", "hitl": "L2", "desc": "Every change request is analyzed by AI for risk, impact, and blast radius. CAB members review AI-generated risk assessments before approving."},
            {"name": "Discovery & Assessment", "hitl": "L1", "desc": "Automated environment discovery — users, devices, applications, network topology, and security posture mapped before any migration begins."},
            {"name": "Phase-Gated Execution", "hitl": "L2", "desc": "Multi-phase project execution with go/no-go gates at each transition. AI validates prerequisites and flags blockers before phase advancement."},
            {"name": "Microsoft 365 Migration", "hitl": "L2", "desc": "End-to-end M365 migration with mailbox scheduling, SharePoint content mapping, Teams provisioning, and identity federation."},
            {"name": "Batch Execution Engine", "hitl": "L1", "desc": "Parallel execution of migration batches with automatic rollback on failure. Progress tracking per batch with estimated completion."},
            {"name": "Hypercare & Stabilization", "hitl": "L1", "desc": "Post-migration monitoring with elevated SLA thresholds, rapid-response queues, and automated regression detection."},
            {"name": "Working Sessions", "hitl": "L3", "desc": "Collaborative project sessions with Zoom integration, real-time transcription, and automatic action item extraction."},
            {"name": "Playbook Designer", "hitl": "L2", "desc": "Visual workflow builder for creating and customizing project playbooks with dependency mapping and role assignment."},
        ],
        "related_roles": ["project_manager", "msp_owner", "it_director", "network_engineer"],
        "related_zones": ["service_desk", "network_ops", "endpoint_management"],
    },
    "security_operations": {
        "number": 3, "label": "Security Operations", "slug": "security-operations",
        "accent": "#DC2626", "icon": "🛡️",
        "tagline": "Unified SOC command center with AI-augmented threat detection, incident response, and zero-trust enforcement",
        "description": "Security Operations is the defensive nerve center of the platform. DevOps AI consolidates threat intelligence, incident response, vulnerability management, and privileged access into a single AI-augmented command center — reducing alert fatigue while ensuring no genuine threat goes unaddressed.",
        "process_areas": [
            {"name": "Incident Response Orchestration", "hitl": "L2", "desc": "AI-coordinated incident response with automated evidence collection, containment recommendations, and chain-of-custody documentation."},
            {"name": "Detection Engineering", "hitl": "L2", "desc": "Custom detection rules with AI-assisted tuning. Correlation engine maps alerts to MITRE ATT&CK techniques automatically."},
            {"name": "EDR/XDR Integration", "hitl": "L1", "desc": "Unified endpoint detection across Wazuh, Defender, and third-party EDR platforms. AI triages 70-90% of Tier-1 alerts automatically."},
            {"name": "Zero-Knowledge Vault (ZK Vault)", "hitl": "L3", "desc": "Client-side encrypted credential storage. Secrets never leave the client's Azure tenant — the platform accesses credentials via ephemeral session tokens."},
            {"name": "Privileged Access Management (PAM)", "hitl": "L3", "desc": "Just-in-time access provisioning with full session recording. Every privileged action requires explicit approval and is logged immutably."},
            {"name": "Dark Web Monitoring", "hitl": "L1", "desc": "Continuous scanning of dark web sources for client credential leaks, domain mentions, and data exposure. Alerts with severity scoring."},
            {"name": "BCDR Planning & Testing", "hitl": "L2", "desc": "Business continuity and disaster recovery plans with automated testing schedules, RTO/RPO tracking, and failover documentation."},
            {"name": "Threat Intelligence Feeds", "hitl": "L0", "desc": "Aggregated threat intelligence from multiple feeds with automated IOC enrichment and relevance scoring per client environment."},
        ],
        "related_roles": ["security_analyst", "vciso", "compliance_officer", "msp_owner"],
        "related_zones": ["grc_compliance", "endpoint_management", "network_ops"],
    },
    "grc_compliance": {
        "number": 4, "label": "GRC & Compliance", "slug": "grc-compliance",
        "accent": "#D97706", "icon": "⚖️",
        "tagline": "Continuous compliance automation with multi-framework evidence collection and audit readiness",
        "description": "Governance, Risk, and Compliance is where regulatory obligations meet operational reality. DevOps AI automates evidence collection, maintains continuous compliance posture, and generates audit-ready documentation — satisfying SOC 2, CMMC, HIPAA, NIST, ISO 27001, and GDPR simultaneously from a single evidence stream.",
        "process_areas": [
            {"name": "Framework Lifecycle Management", "hitl": "L2", "desc": "Full lifecycle management for compliance frameworks — scoping, gap analysis, remediation tracking, evidence collection, and certification maintenance."},
            {"name": "OSCAL-Native Evidence", "hitl": "L0", "desc": "Evidence collected in OSCAL (Open Security Controls Assessment Language) format for machine-readable compliance documentation."},
            {"name": "Gap Analysis Engine", "hitl": "L1", "desc": "AI-powered gap analysis comparing current security controls against target framework requirements. Remediation recommendations prioritized by risk."},
            {"name": "CMMC SSP Builder", "hitl": "L2", "desc": "Automated System Security Plan generation for CMMC Level 2 with control mapping, boundary diagrams, and inherited control documentation."},
            {"name": "C3PAO Readiness Assessment", "hitl": "L2", "desc": "Pre-assessment checklist and evidence package preparation for C3PAO auditors. Simulated audit walkthroughs with AI-identified gaps."},
            {"name": "Audit Management", "hitl": "L2", "desc": "Audit lifecycle tracking from planning through closure. Evidence requests routed to control owners with automated collection where possible."},
            {"name": "Policy Management", "hitl": "L2", "desc": "Policy lifecycle with version control, approval workflows, distribution tracking, and attestation management."},
            {"name": "Continuous Monitoring", "hitl": "L0", "desc": "Real-time compliance posture dashboards with automated drift detection. Alerts when controls fall out of compliance."},
        ],
        "related_roles": ["compliance_officer", "vciso", "vcco", "msp_owner"],
        "related_zones": ["security_operations", "analytics", "legal"],
    },
    "network_ops": {
        "number": 5, "label": "Network Operations", "slug": "network-ops",
        "accent": "#0891B2", "icon": "🌐",
        "tagline": "Intelligent network monitoring with SLO management, topology visualization, and predictive capacity planning",
        "description": "Network Operations provides real-time visibility into the entire network infrastructure across all managed clients. From SLO-based monitoring to predictive capacity planning, DevOps AI ensures network health is maintained proactively rather than reactively.",
        "process_areas": [
            {"name": "SLO Management", "hitl": "L1", "desc": "Service Level Objective tracking with error budget consumption alerts and automated reporting for client-facing SLAs."},
            {"name": "Topology Visualization", "hitl": "L0", "desc": "Interactive network topology maps with real-time status overlays, dependency tracing, and change impact visualization."},
            {"name": "Capacity Forecasting", "hitl": "L1", "desc": "ML-driven capacity predictions based on historical utilization trends. Proactive upgrade recommendations before saturation."},
            {"name": "SSL Certificate Management", "hitl": "L1", "desc": "Automated certificate discovery, expiry tracking, and renewal workflows across all clients. Zero-downtime rotation."},
            {"name": "Ring-Based Patch Management", "hitl": "L2", "desc": "Staged patch deployment across canary, early adopter, and general availability rings with automated rollback on failure."},
            {"name": "Network Configuration Management", "hitl": "L2", "desc": "Standardized network configurations with drift detection, compliance validation, and automated remediation."},
            {"name": "Performance Monitoring", "hitl": "L0", "desc": "Real-time bandwidth, latency, and packet loss monitoring with anomaly detection and root cause analysis."},
        ],
        "related_roles": ["network_engineer", "it_director", "msp_owner"],
        "related_zones": ["endpoint_management", "security_operations", "analytics"],
    },
    "endpoint_management": {
        "number": 6, "label": "Endpoint Management", "slug": "endpoint-management",
        "accent": "#16A34A", "icon": "💻",
        "tagline": "Unified endpoint lifecycle management with Intune integration, automated patching, and fleet intelligence",
        "description": "Endpoint Management unifies the entire device lifecycle — from provisioning through retirement — across heterogeneous fleets. DevOps AI integrates with Intune, NinjaRMM, and other endpoint agents to provide a single pane of glass for device health, compliance, and security posture.",
        "process_areas": [
            {"name": "Intune Management & Compliance", "hitl": "L1", "desc": "Full Intune lifecycle management with compliance policy enforcement, conditional access configuration, and device enrollment automation."},
            {"name": "Infrastructure Monitoring", "hitl": "L0", "desc": "Agent-based monitoring for CPU, memory, disk, and process health with automated alerting and self-healing scripts."},
            {"name": "Device Lifecycle Management", "hitl": "L2", "desc": "End-to-end device lifecycle from procurement and provisioning through maintenance, refresh, and secure disposal."},
            {"name": "Automated Patching", "hitl": "L1", "desc": "OS and application patching with staged rollouts, compliance reporting, and rollback capabilities."},
            {"name": "Vulnerability Management", "hitl": "L1", "desc": "Continuous vulnerability scanning with risk-prioritized remediation queues. Integration with CVE databases for real-time threat context."},
            {"name": "DNS Filtering", "hitl": "L1", "desc": "DNS-level content filtering and threat protection with policy management per client, department, or device group."},
            {"name": "Remote Access & Support", "hitl": "L2", "desc": "Secure remote access with session recording, just-in-time elevation, and audit trail for every remote action."},
            {"name": "Fleet Intelligence", "hitl": "L0", "desc": "Cross-client device intelligence — hardware lifecycle predictions, software license optimization, and standardization recommendations."},
        ],
        "related_roles": ["it_director", "network_engineer", "security_analyst"],
        "related_zones": ["network_ops", "security_operations", "projects"],
    },
    "accounting": {
        "number": 7, "label": "Accounting", "slug": "accounting",
        "accent": "#059669", "icon": "📊",
        "tagline": "Automated billing reconciliation, contract lifecycle management, and revenue operations",
        "description": "The Accounting zone transforms MSP financial operations from manual spreadsheet chaos into automated, reconciled revenue streams. DevOps AI ingests invoices, reconciles billing against license usage, manages contract lifecycles, and ensures every dollar of MRR is captured.",
        "process_areas": [
            {"name": "Invoice Ingestion & Processing", "hitl": "L1", "desc": "Automated invoice capture via email, portal, or API with AI-powered line item extraction and vendor classification."},
            {"name": "Three-Way Billing Reconciliation", "hitl": "L1", "desc": "Automated reconciliation of agreements, actual usage, and invoices. AI flags discrepancies and missed billables — typically recovering ~10% missed MRR."},
            {"name": "Contract Lifecycle Management", "hitl": "L2", "desc": "Full contract lifecycle from creation through renewal with automated alerts, version tracking, and compliance clause monitoring."},
            {"name": "Procurement Automation", "hitl": "L2", "desc": "Streamlined procurement with vendor management, approval workflows, and purchase order tracking."},
            {"name": "Revenue Recognition", "hitl": "L1", "desc": "ASC 606-compliant revenue recognition with automated scheduling, deferred revenue tracking, and audit documentation."},
            {"name": "GL Integration", "hitl": "L1", "desc": "Bi-directional sync with general ledger systems (QuickBooks, Xero) for real-time financial visibility."},
            {"name": "CPQ (Configure, Price, Quote)", "hitl": "L2", "desc": "AI-assisted quoting with margin protection, competitive pricing analysis, and automated proposal generation."},
            {"name": "Subscription Management", "hitl": "L1", "desc": "License seat tracking, usage monitoring, and automated true-up calculations across all vendor subscriptions."},
        ],
        "related_roles": ["finance_coordinator", "msp_owner", "account_manager"],
        "related_zones": ["relationships", "vc_suite", "analytics"],
    },
    "relationships": {
        "number": 8, "label": "Relationships", "slug": "relationships",
        "accent": "#7C3AED", "icon": "🤝",
        "tagline": "Full-lifecycle relationship management from lead generation through QBR delivery",
        "description": "Relationships (formerly Business Development) manages the entire client relationship lifecycle — from first-touch lead generation through ongoing account management and quarterly business reviews. DevOps AI automates pipeline management, enriches prospect data with AI, and ensures every client touchpoint is coordinated and intentional.",
        "process_areas": [
            {"name": "Lead Generation & ICP Scoring", "hitl": "L1", "desc": "AI-powered ideal customer profile matching with automated lead scoring, enrichment, and prioritization."},
            {"name": "Sales Pipeline Management", "hitl": "L1", "desc": "Visual pipeline with AI-predicted close probabilities, deal health indicators, and automated follow-up scheduling."},
            {"name": "Marketing Campaign Orchestration", "hitl": "L2", "desc": "Multi-channel campaign management with audience segmentation, content personalization, and attribution tracking."},
            {"name": "Client Onboarding Workflows", "hitl": "L2", "desc": "Structured onboarding from signed deal to fully operational — documentation collection, access provisioning, and knowledge transfer."},
            {"name": "QBR Preparation & Delivery", "hitl": "L1", "desc": "AI-compiled quarterly business reviews with performance metrics, recommendations, and roadmap updates. Prep time drops from 4-8 hours to 20-30 minutes."},
            {"name": "Client Health Scoring", "hitl": "L0", "desc": "Composite client health score based on ticket trends, NPS, contract status, engagement metrics, and payment patterns."},
            {"name": "Churn Risk Detection", "hitl": "L1", "desc": "Early warning system for at-risk clients using behavioral signals, sentiment analysis, and engagement pattern changes."},
            {"name": "Referral & Expansion Tracking", "hitl": "L1", "desc": "Automated identification of upsell and cross-sell opportunities based on client technology gaps and growth signals."},
        ],
        "related_roles": ["account_manager", "msp_owner", "vcio"],
        "related_zones": ["accounting", "vc_suite", "analytics"],
    },
    "vc_suite": {
        "number": 9, "label": "vC-Suite", "slug": "vc-suite",
        "accent": "#475569", "icon": "🧭",
        "tagline": "Virtual executive advisory engines for CIO, CTO, CISO, and CCO functions",
        "description": "The vC-Suite provides AI-powered virtual executive advisory across four critical functions: vCIO (technology strategy), vCTO (architecture and innovation), vCISO (security leadership), and vCCO (compliance governance). Each advisory engine generates data-driven recommendations tailored to client-specific context.",
        "process_areas": [
            {"name": "vCIO Advisory Engine", "hitl": "L2", "desc": "Technology roadmap generation, budget planning, vendor evaluation, and strategic initiative prioritization — all contextualized to each client's environment."},
            {"name": "vCTO Architecture Reviews", "hitl": "L2", "desc": "Infrastructure architecture assessment, modernization recommendations, cloud migration planning, and technical debt analysis."},
            {"name": "vCISO Security Program", "hitl": "L2", "desc": "Security program maturity assessment, risk register management, security budget allocation, and board-ready reporting."},
            {"name": "vCCO Compliance Governance", "hitl": "L2", "desc": "Chief Compliance Officer advisory with regulatory landscape monitoring, compliance program oversight, and policy effectiveness scoring."},
            {"name": "Executive KPI Dashboards", "hitl": "L0", "desc": "Real-time executive dashboards with client profitability, service delivery metrics, security posture, and growth indicators."},
            {"name": "Technology Roadmap Management", "hitl": "L2", "desc": "Living technology roadmaps per client with milestone tracking, dependency mapping, and progress reporting."},
            {"name": "Client Profitability Analysis", "hitl": "L1", "desc": "Per-client profitability calculations including all direct costs, allocated overheads, and margin optimization recommendations."},
            {"name": "Strategic Recommendations", "hitl": "L1", "desc": "AI-generated strategic recommendations based on industry benchmarks, peer comparisons, and emerging technology trends."},
        ],
        "related_roles": ["vcio", "vciso", "vcco", "msp_owner"],
        "related_zones": ["analytics", "grc_compliance", "relationships"],
    },
    "analytics": {
        "number": 10, "label": "Analytics", "slug": "analytics",
        "accent": "#EA580C", "icon": "📈",
        "tagline": "Cross-domain business intelligence with predictive analytics, NL queries, and automated reporting",
        "description": "Analytics is the intelligence layer that spans all zones — aggregating data from every operational domain into actionable insights. From churn prediction to ticket volume forecasting, DevOps AI delivers predictive intelligence that helps MSPs make data-driven decisions.",
        "process_areas": [
            {"name": "QBR Aggregation Engine", "hitl": "L1", "desc": "Automated compilation of quarterly business review data from all zones — service delivery, security posture, compliance status, and recommendations."},
            {"name": "Churn Prediction Model", "hitl": "L1", "desc": "ML-driven churn risk scoring using engagement patterns, ticket sentiment, payment behavior, and service utilization signals."},
            {"name": "Ticket Volume Forecasting", "hitl": "L0", "desc": "Predictive models for ticket volume by client, category, and time period — enabling proactive staffing and resource allocation."},
            {"name": "Security Risk Scoring", "hitl": "L0", "desc": "Composite security risk scores per client combining vulnerability data, compliance gaps, threat exposure, and control effectiveness."},
            {"name": "Natural Language BI Queries", "hitl": "L0", "desc": "Ask questions in plain English — 'Which clients had the most P1 tickets last quarter?' — and get instant, accurate answers with visualizations."},
            {"name": "Automated Report Generation", "hitl": "L1", "desc": "Scheduled and ad-hoc report generation with customizable templates, data source selection, and distribution management."},
            {"name": "Cross-Domain Correlation", "hitl": "L0", "desc": "AI-powered pattern detection across zones — correlating security events with ticket spikes, compliance gaps with service issues, and more."},
            {"name": "Benchmark Intelligence", "hitl": "L0", "desc": "Anonymous peer benchmarking across the DevOps AI platform — how does this client compare to similar organizations on key metrics?"},
        ],
        "related_roles": ["msp_owner", "vcio", "it_director", "account_manager"],
        "related_zones": ["vc_suite", "service_desk", "security_operations", "grc_compliance"],
    },
    "devops": {
        "number": 11, "label": "DevOps", "slug": "devops",
        "accent": "#6B7280", "icon": "⚙️",
        "tagline": "Platform engineering with feature flags, connector toolkit, and operational observability",
        "description": "The DevOps zone is the platform's own engineering command center — managing CI/CD pipelines, feature flags, connector health, and operational observability. This is where the platform's reliability engineering and continuous improvement happen.",
        "process_areas": [
            {"name": "Feature Flag Management", "hitl": "L2", "desc": "Granular feature flags with gradual rollout, A/B testing, and emergency kill switches. Per-tenant and per-role targeting."},
            {"name": "A/B Testing Framework", "hitl": "L2", "desc": "Statistically rigorous A/B tests for platform features with automated significance detection and outcome reporting."},
            {"name": "Connector Toolkit", "hitl": "L2", "desc": "Unified connector framework for third-party integrations — NinjaRMM, ConnectWise, ServiceNow, Intune, Wazuh, and more."},
            {"name": "SRE Golden Signals", "hitl": "L0", "desc": "Latency, traffic, errors, and saturation monitoring across all platform services with automated anomaly detection."},
            {"name": "Bottleneck Detection", "hitl": "L0", "desc": "AI-powered performance analysis identifying system bottlenecks, resource contention, and optimization opportunities."},
            {"name": "Configuration Management", "hitl": "L2", "desc": "Centralized configuration with environment-specific overrides, secrets management, and change audit trail."},
            {"name": "Environment Lifecycle", "hitl": "L2", "desc": "Dev/staging/production environment management with automated provisioning, data seeding, and teardown."},
            {"name": "Integration Health Dashboard", "hitl": "L0", "desc": "Real-time health status for all third-party integrations with availability tracking, latency monitoring, and error rate alerts."},
        ],
        "related_roles": ["msp_owner", "it_director"],
        "related_zones": ["analytics", "service_desk", "security_operations"],
    },
    "learning": {
        "number": 12, "label": "Learning", "slug": "learning",
        "accent": "#0D9488", "icon": "🎓",
        "tagline": "Continuous learning platform with AI tutoring, certification tracking, and knowledge management",
        "description": "The Learning zone transforms knowledge management from scattered wikis and tribal knowledge into a structured, AI-tutored learning environment. From compliance training to technical certification, every learning path is tracked, measured, and optimized for retention.",
        "process_areas": [
            {"name": "LMS Engine", "hitl": "L1", "desc": "Full learning management system with course creation, enrollment, progress tracking, and completion certification."},
            {"name": "AI Tutoring", "hitl": "L0", "desc": "Context-aware AI tutor that answers questions using the organization's knowledge base, adapts to learning style, and suggests next steps."},
            {"name": "Certification Tracking", "hitl": "L1", "desc": "Automated tracking of professional certifications with expiry alerts, renewal workflows, and compliance evidence generation."},
            {"name": "Knowledge Store", "hitl": "L0", "desc": "Centralized knowledge repository with semantic search, automated categorization, and stale content detection."},
            {"name": "Compliance Training", "hitl": "L1", "desc": "Mandatory compliance training with SCORM/xAPI tracking, completion attestation, and audit-ready evidence."},
            {"name": "SOP & Runbook Management", "hitl": "L1", "desc": "Standard Operating Procedures and runbooks with version control, role-based distribution, and acknowledgment tracking."},
            {"name": "Skill Gap Analysis", "hitl": "L1", "desc": "AI-identified skill gaps across the organization with personalized learning path recommendations."},
            {"name": "Onboarding Journeys", "hitl": "L1", "desc": "Role-specific onboarding paths that combine training, workflow introduction, and competency verification."},
        ],
        "related_roles": ["hr_director", "msp_owner", "compliance_officer", "it_director"],
        "related_zones": ["grc_compliance", "service_desk", "people"],
    },
    "organization": {
        "number": 13, "label": "Organization", "slug": "organization",
        "accent": "#1F2937", "icon": "🏢",
        "tagline": "Organizational structure management, department hierarchy, and multi-tenant administration",
        "description": "The Organization zone manages the structural foundation of every managed client — department hierarchies, cost centers, location management, and multi-tenant boundaries. This is where organizational context is defined so every other zone can operate with proper scope and access control.",
        "process_areas": [
            {"name": "Department Hierarchy Management", "hitl": "L2", "desc": "Define and maintain organizational structure with departments, teams, and reporting relationships used across all zones."},
            {"name": "Multi-Tenant Administration", "hitl": "L3", "desc": "Client tenant provisioning, isolation verification, and cross-tenant operations for MSPs managing multiple organizations."},
            {"name": "Cost Center Management", "hitl": "L2", "desc": "Cost center definitions mapped to departments, projects, and billing entities for accurate financial allocation."},
            {"name": "Location & Site Management", "hitl": "L2", "desc": "Physical and virtual site management with timezone handling, regional compliance requirements, and service delivery scope."},
            {"name": "Organizational Policy Framework", "hitl": "L2", "desc": "Organization-wide policy definitions that cascade to all zones — data handling, access control, communication preferences."},
            {"name": "Branding & White-Label", "hitl": "L2", "desc": "Per-organization branding customization — logos, colors, email templates, and portal themes."},
        ],
        "related_roles": ["msp_owner", "it_director", "hr_director"],
        "related_zones": ["people", "accounting", "legal"],
    },
    "people": {
        "number": 14, "label": "People", "slug": "people",
        "accent": "#8B5CF6", "icon": "👥",
        "tagline": "People management with onboarding automation, access lifecycle, and workforce analytics",
        "description": "The People zone manages the human element across every managed organization — from employee onboarding and access provisioning to offboarding and workforce analytics. Every person-related workflow integrates with Learning for training and GRC for compliance.",
        "process_areas": [
            {"name": "Employee Onboarding Automation", "hitl": "L2", "desc": "Structured onboarding workflows — identity provisioning, device assignment, application access, training enrollment, and compliance attestation."},
            {"name": "Access Lifecycle Management", "hitl": "L2", "desc": "Joiner-mover-leaver workflows with automated access adjustments when roles change, departments merge, or employees depart."},
            {"name": "Offboarding & Access Revocation", "hitl": "L2", "desc": "Comprehensive offboarding with credential revocation cascade, device recovery, data preservation, and audit documentation."},
            {"name": "Workforce Analytics", "hitl": "L0", "desc": "Headcount tracking, role distribution, access patterns, and training completion rates across managed organizations."},
            {"name": "Directory Synchronization", "hitl": "L1", "desc": "Bi-directional sync with Azure AD, Google Workspace, and on-premises directories with conflict resolution."},
            {"name": "Contractor & Vendor Access", "hitl": "L2", "desc": "Time-bounded access provisioning for contractors and vendors with automated expiry and review workflows."},
        ],
        "related_roles": ["hr_director", "recruiter", "it_director", "msp_owner"],
        "related_zones": ["organization", "learning", "security_operations"],
    },
    "legal": {
        "number": 15, "label": "Legal", "slug": "legal",
        "accent": "#B45309", "icon": "⚖️",
        "tagline": "Legal operations with contract analysis, regulatory monitoring, and data privacy management",
        "description": "The Legal zone provides the legal operations framework for MSPs — from contract analysis and regulatory change monitoring to data privacy management and incident legal response. Every legal workflow integrates with GRC for compliance evidence and Accounting for contract financials.",
        "process_areas": [
            {"name": "Contract Analysis & Review", "hitl": "L3", "desc": "AI-assisted contract review with clause extraction, risk flagging, and comparison against standard templates. All final decisions require human legal review."},
            {"name": "Regulatory Change Monitoring", "hitl": "L1", "desc": "Automated monitoring of regulatory changes affecting managed clients — GDPR, CCPA, HIPAA, industry-specific regulations."},
            {"name": "Data Privacy Management", "hitl": "L2", "desc": "DSAR (Data Subject Access Request) processing, data mapping, retention policy enforcement, and privacy impact assessments."},
            {"name": "Incident Legal Response", "hitl": "L3", "desc": "Legal response coordination for security incidents — breach notification timelines, regulatory reporting, and liability assessment."},
            {"name": "NDA & Vendor Agreement Management", "hitl": "L2", "desc": "Standardized NDA and vendor agreement lifecycle with template management, approval routing, and expiry tracking."},
            {"name": "Intellectual Property Tracking", "hitl": "L2", "desc": "IP asset registry, licensing compliance, and open-source dependency auditing across managed environments."},
        ],
        "related_roles": ["compliance_officer", "vcco", "msp_owner"],
        "related_zones": ["grc_compliance", "accounting", "organization"],
    },
}

# ═══════════════════════════════════════════════════════════════════════
# ROLE DATA
# ═══════════════════════════════════════════════════════════════════════

ROLES = {
    "msp_owner": {
        "title": "MSP Owner / CEO", "slug": "msp-owner", "icon": "🏢",
        "tagline": "Scale without adding headcount — unified executive dashboard, predictive analytics, and automated revenue operations",
        "primary_zones": ["vc_suite", "analytics", "relationships", "accounting"],
        "secondary_zones": ["service_desk", "security_operations", "projects"],
    },
    "vcio": {
        "title": "vCIO", "slug": "vcio", "icon": "🧭",
        "tagline": "QBR prep drops from 4-8 hours to 20-30 minutes with AI-orchestrated client advisory and living roadmaps",
        "primary_zones": ["vc_suite", "analytics", "relationships"],
        "secondary_zones": ["projects", "security_operations", "grc_compliance"],
    },
    "vciso": {
        "title": "vCISO", "slug": "vciso", "icon": "🔒", "new": True,
        "tagline": "AI-powered security program leadership — risk management, compliance oversight, and board-ready reporting",
        "primary_zones": ["security_operations", "grc_compliance", "vc_suite"],
        "secondary_zones": ["endpoint_management", "network_ops", "analytics"],
    },
    "security_analyst": {
        "title": "Security Analyst", "slug": "security-analyst", "icon": "🛡️",
        "tagline": "Unified SOC command center — 70-90% of Tier-1 alerts auto-triaged with context pre-built before you touch a case",
        "primary_zones": ["security_operations", "endpoint_management"],
        "secondary_zones": ["network_ops", "grc_compliance", "analytics"],
    },
    "service_desk_manager": {
        "title": "Service Desk Manager", "slug": "service-desk-manager", "icon": "🎫",
        "tagline": "Predictive SLA management prevents breaches — cross-client problem intelligence detects patterns automatically",
        "primary_zones": ["service_desk", "analytics"],
        "secondary_zones": ["projects", "learning", "endpoint_management"],
    },
    "compliance_officer": {
        "title": "Compliance Officer", "slug": "compliance-officer", "icon": "⚖️",
        "tagline": "Collect evidence once, satisfy SOC 2 + CMMC + HIPAA + ISO 27001 simultaneously — continuous monitoring, not annual audits",
        "primary_zones": ["grc_compliance", "security_operations"],
        "secondary_zones": ["legal", "analytics", "learning"],
    },
    "project_manager": {
        "title": "Project Manager", "slug": "project-manager", "icon": "📋",
        "tagline": "AI risk scoring for every RFC — migration command center with deal-to-delivery handoff in under 5 minutes",
        "primary_zones": ["projects", "service_desk"],
        "secondary_zones": ["network_ops", "endpoint_management", "relationships"],
    },
    "network_engineer": {
        "title": "Network Engineer", "slug": "network-engineer", "icon": "🌐",
        "tagline": "Live topology, SLO-based monitoring, ring-based patching, and SSL certificate auto-renewal across all clients",
        "primary_zones": ["network_ops", "endpoint_management"],
        "secondary_zones": ["security_operations", "projects", "devops"],
    },
    "account_manager": {
        "title": "Account Manager", "slug": "account-manager", "icon": "🚀",
        "tagline": "Unified client record with pipeline, billing, health scoring, and QBR content in one platform",
        "primary_zones": ["relationships", "accounting", "analytics"],
        "secondary_zones": ["service_desk", "vc_suite"],
    },
    "finance_coordinator": {
        "title": "Finance Coordinator", "slug": "finance-coordinator", "icon": "💰",
        "tagline": "Three-way reconciliation automated — 85% faster billing, capture ~10% missed MRR from license discrepancies",
        "primary_zones": ["accounting"],
        "secondary_zones": ["relationships", "analytics", "vc_suite"],
    },
    "it_director": {
        "title": "IT Director", "slug": "it-director", "icon": "🖥️",
        "tagline": "Client portal with real-time visibility — tickets, compliance posture, security health, and your technology roadmap",
        "primary_zones": ["vc_suite", "endpoint_management", "network_ops"],
        "secondary_zones": ["security_operations", "projects", "analytics"],
    },
    "hr_director": {
        "title": "HR Director", "slug": "hr-director", "icon": "👤", "new": True,
        "tagline": "Automated onboarding and offboarding with access lifecycle management, compliance training, and workforce analytics",
        "primary_zones": ["people", "organization", "learning"],
        "secondary_zones": ["grc_compliance", "legal"],
    },
    "recruiter": {
        "title": "Recruiter", "slug": "recruiter", "icon": "🔍", "new": True,
        "tagline": "Streamlined candidate-to-employee pipeline with automated provisioning and role-specific onboarding",
        "primary_zones": ["people", "organization"],
        "secondary_zones": ["learning"],
    },
    "vcco": {
        "title": "vCCO", "slug": "vcco", "icon": "📜", "new": True,
        "tagline": "Virtual Chief Compliance Officer — regulatory landscape monitoring, compliance program orchestration, and audit readiness",
        "primary_zones": ["grc_compliance", "legal", "vc_suite"],
        "secondary_zones": ["security_operations", "analytics"],
    },
}

# ═══════════════════════════════════════════════════════════════════════
# HTML GENERATION UTILITIES
# ═══════════════════════════════════════════════════════════════════════

PPLX_HEAD = """<!--
   ______                            __
  / ____/___  ____ ___  ____  __  __/ /____  _____
 / /   / __ \\/ __ `__ \\/ __ \\/ / / / __/ _ \\/ ___/
/ /___/ /_/ / / / / / / /_/ / /_/ / /_/  __/ /
\\____/\\____/_/ /_/ /_/ .___/\\__,_/\\__/\\___/_/
                    /_/
        Created with Perplexity Computer
        https://www.perplexity.ai/computer
-->
<meta name="generator" content="Perplexity Computer">
<meta name="author" content="Perplexity Computer">
<meta property="og:see_also" content="https://www.perplexity.ai/computer">
<link rel="author" href="https://www.perplexity.ai/computer">"""


def path_prefix(page_path):
    """Return relative path prefix based on page depth."""
    depth = page_path.count("/")
    if depth == 0:
        return ""
    return "../" * depth


def generate_header(page_title, page_path, active_section=""):
    """Generate the shared site header with navigation."""
    pfx = path_prefix(page_path)
    
    # Build zone links for mega menu
    ops_zones = [("service_desk", "🎫", "Service Desk"), ("projects", "📋", "Projects"),
                 ("network_ops", "🌐", "Network Ops"), ("endpoint_management", "💻", "Endpoints")]
    sec_zones = [("security_operations", "🛡️", "Security Ops"), ("grc_compliance", "⚖️", "GRC")]
    biz_zones = [("accounting", "📊", "Accounting"), ("relationships", "🤝", "Relationships"),
                 ("vc_suite", "🧭", "vC-Suite"), ("analytics", "📈", "Analytics")]
    plat_zones = [("devops", "⚙️", "DevOps"), ("learning", "🎓", "Learning"),
                  ("organization", "🏢", "Organization"), ("people", "👥", "People"), ("legal", "⚖️", "Legal")]

    def zone_link(key, icon, label):
        z = ZONES[key]
        return f'<a href="{pfx}zones/{z["slug"]}.html" class="mega-zone-link"><span class="mzl-icon">{icon}</span> {label}</a>'

    def zone_links(lst):
        return "\n                    ".join(zone_link(k, i, l) for k, i, l in lst)

    # Role links
    col1_roles = ["msp_owner", "vcio", "vciso", "security_analyst", "service_desk_manager", "compliance_officer", "project_manager"]
    col2_roles = ["network_engineer", "account_manager", "finance_coordinator", "it_director", "hr_director", "recruiter", "vcco"]

    def role_link(key):
        r = ROLES[key]
        new = ' <span style="font-size:10px;color:var(--accent);font-weight:700">NEW</span>' if r.get("new") else ""
        return f'<a href="{pfx}roles/{r["slug"]}.html" class="mega-menu-link"><span class="link-text"><strong>{r["title"]}{new}</strong><span>{r["tagline"][:60]}...</span></span></a>'

    return f"""<a href="#main-content" class="skip-to-content">Skip to main content</a>
<div class="nav-overlay" aria-hidden="true"></div>

<header class="site-header" role="banner">
  <div class="container header-inner">
    <a href="{pfx}index.html" class="header-logo" aria-label="DevOps AI Home">
      <img src="{pfx}assets/logo-powered-by.png" alt="DevOps AI — Powered by RainTech" width="200" height="40">
    </a>
    <nav class="nav-links" role="navigation" aria-label="Main navigation">
      <div class="nav-item">
        <a href="{pfx}platform.html" class="nav-link">Platform <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu mega-menu--wide">
          <div class="mega-menu-grid">
            <div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Overview</div>
                <a href="{pfx}platform.html" class="mega-menu-link"><span class="link-text"><strong>Platform Overview</strong><span>17-zone AI-orchestrated control plane</span></span></a>
                <a href="{pfx}why-devops-ai.html" class="mega-menu-link"><span class="link-text"><strong>Why DevOps AI</strong><span>Compare to traditional MSP tools</span></span></a>
                <a href="{pfx}architecture.html" class="mega-menu-link"><span class="link-text"><strong>Architecture</strong><span>Zero-trust, Azure-native design</span></span></a>
              </div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Operations</div>
                <div class="mega-zone-grid">
                  {zone_links(ops_zones)}
                </div>
              </div>
            </div>
            <div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Security &amp; Compliance</div>
                <div class="mega-zone-grid">
                  {zone_links(sec_zones)}
                </div>
              </div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Business</div>
                <div class="mega-zone-grid">
                  {zone_links(biz_zones)}
                </div>
              </div>
              <div class="mega-menu-section">
                <div class="mega-menu-label">Platform</div>
                <div class="mega-zone-grid">
                  {zone_links(plat_zones)}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="nav-item">
        <a href="{pfx}solutions.html" class="nav-link">Solutions <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu">
          <a href="{pfx}solutions.html#healthcare" class="mega-menu-link"><span class="link-text"><strong>Healthcare &amp; HIPAA</strong><span>HIPAA-ready managed services</span></span></a>
          <a href="{pfx}solutions.html#defense" class="mega-menu-link"><span class="link-text"><strong>Defense &amp; CMMC</strong><span>CMMC Level 2 compliance</span></span></a>
          <a href="{pfx}solutions.html#financial" class="mega-menu-link"><span class="link-text"><strong>Financial Services</strong><span>SOC 2 &amp; regulatory compliance</span></span></a>
          <a href="{pfx}solutions.html#compliance" class="mega-menu-link"><span class="link-text"><strong>General Compliance</strong><span>GDPR, ISO 27001, and more</span></span></a>
        </div>
      </div>
      <div class="nav-item">
        <a href="{pfx}roles/index.html" class="nav-link">For Your Role <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu mega-menu--wide mega-menu--roles">
          <div class="mega-menu-grid">
            <div>
              {"".join(role_link(k) for k in col1_roles)}
            </div>
            <div>
              {"".join(role_link(k) for k in col2_roles)}
            </div>
          </div>
        </div>
      </div>
      <a href="{pfx}security.html" class="nav-link">Security</a>
      <a href="{pfx}marketplace.html" class="nav-link">Marketplace</a>
      <div class="nav-item">
        <a href="{pfx}about.html" class="nav-link">About <svg class="chevron" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 4.5l3 3 3-3"/></svg></a>
        <div class="mega-menu">
          <a href="{pfx}about.html" class="mega-menu-link"><span class="link-text"><strong>About RainTech</strong><span>Our mission and values</span></span></a>
          <a href="{pfx}contact.html" class="mega-menu-link"><span class="link-text"><strong>Contact</strong><span>Get in touch with our team</span></span></a>
          <a href="{pfx}roi.html" class="mega-menu-link"><span class="link-text"><strong>ROI Calculator</strong><span>Calculate your potential savings</span></span></a>
        </div>
      </div>
      <a href="{pfx}marketplace.html" class="nav-cta">Get Started
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 10h10m-4-4 4 4-4 4"/></svg>
      </a>
    </nav>
    <button class="theme-toggle" aria-label="Toggle light/dark mode" type="button">
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
    </button>
    <button class="mobile-menu-toggle" aria-label="Toggle menu" aria-expanded="false" type="button">
      <span></span>
    </button>
  </div>
</header>"""


def generate_footer(page_path):
    """Generate the shared site footer."""
    pfx = path_prefix(page_path)
    return f"""<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{pfx}assets/logo-powered-by.png" alt="DevOps AI — Powered by RainTech" width="180" height="36">
        <p>3 S Tejon St., Suite 400<br>Colorado Springs, CO 80903</p>
        <p style="margin-top: var(--space-2);">844.TEL.RAIN</p>
        <div class="footer-tagline">People First, PERIOD.&reg;</div>
      </div>
      <div class="footer-col">
        <h4>Platform</h4>
        <a href="{pfx}platform.html">Platform Overview</a>
        <a href="{pfx}zones/service-desk.html">Service Desk</a>
        <a href="{pfx}zones/security-operations.html">Security Operations</a>
        <a href="{pfx}zones/grc-compliance.html">GRC &amp; Compliance</a>
        <a href="{pfx}architecture.html">Architecture</a>
        <a href="{pfx}why-devops-ai.html">Why DevOps AI</a>
      </div>
      <div class="footer-col">
        <h4>Solutions</h4>
        <a href="{pfx}solutions.html#healthcare">Healthcare &amp; HIPAA</a>
        <a href="{pfx}solutions.html#defense">Defense &amp; CMMC</a>
        <a href="{pfx}solutions.html#financial">Financial Services</a>
        <a href="{pfx}roi.html">ROI Calculator</a>
      </div>
      <div class="footer-col">
        <h4>For Your Role</h4>
        <a href="{pfx}roles/index.html">All Roles</a>
        <a href="{pfx}roles/msp-owner.html">MSP Owner / CEO</a>
        <a href="{pfx}roles/vcio.html">vCIO</a>
        <a href="{pfx}roles/security-analyst.html">Security Analyst</a>
        <a href="{pfx}roles/compliance-officer.html">Compliance Officer</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="{pfx}about.html">About RainTech</a>
        <a href="{pfx}contact.html">Contact</a>
        <a href="{pfx}marketplace.html">Azure Marketplace</a>
        <a href="{pfx}security.html">Trust &amp; Security</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 RainTech. All rights reserved.</span>
      <span>Cloud. Security. Support. Results.</span>
      <a href="https://www.perplexity.ai/computer" target="_blank" rel="noopener noreferrer">Created with Perplexity Computer</a>
    </div>
  </div>
</footer>"""


def generate_cookie_banner():
    return """<div class="cookie-banner" role="dialog" aria-label="Cookie consent">
  <div class="cookie-banner__text">
    We use cookies to personalize your experience and analyze site usage. By clicking "Accept All," you consent to our use of cookies. See our <a href="legal/privacy.html">Privacy Policy</a> for details.
  </div>
  <div class="cookie-banner__actions">
    <button class="cookie-btn cookie-btn--reject">Reject Non-Essential</button>
    <button class="cookie-btn cookie-btn--accept">Accept All</button>
  </div>
</div>"""


def generate_json_ld(page_type, page_data, page_path):
    """Generate JSON-LD structured data for a page."""
    pfx = "https://devops.ai.rain.tech/"
    url = pfx + page_path
    
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "name": "RainTech",
                "url": "https://devops.ai.rain.tech",
                "logo": pfx + "assets/logo-powered-by.png",
            },
            {
                "@type": "WebPage",
                "name": page_data.get("title", "DevOps AI"),
                "url": url,
                "description": page_data.get("description", ""),
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": page_data.get("breadcrumbs", [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": pfx}
                    ])
                },
                "creator": {
                    "@type": "SoftwareApplication",
                    "name": "Perplexity Computer",
                    "url": "https://www.perplexity.ai/computer"
                }
            }
        ]
    }
    return json.dumps(ld, indent=2)


HITL_LABELS = {
    "L0": "Fully Automated",
    "L1": "Notify",
    "L2": "Approve to Proceed",
    "L3": "Human Only",
}


def hitl_badge(level):
    label = HITL_LABELS.get(level, level)
    return f'<span class="hitl-badge hitl-badge--{level.lower()}" title="{label}">{level} — {label}</span>'


# ═══════════════════════════════════════════════════════════════════════
# PAGE GENERATORS
# ═══════════════════════════════════════════════════════════════════════

def generate_zone_page(zone_key):
    """Generate a complete zone page."""
    z = ZONES[zone_key]
    page_path = f"zones/{z['slug']}.html"
    pfx = path_prefix(page_path)
    
    # Process area cards
    pa_cards = ""
    for pa in z["process_areas"]:
        pa_cards += f"""
        <div class="process-card fade-up">
          <div class="process-card__header">
            <h3 class="process-card__title">{pa['name']}</h3>
            {hitl_badge(pa['hitl'])}
          </div>
          <p class="process-card__body">{pa['desc']}</p>
        </div>"""

    # Related roles
    role_links = ""
    for rk in z.get("related_roles", []):
        if rk in ROLES:
            r = ROLES[rk]
            role_links += f"""
          <a href="{pfx}roles/{r['slug']}.html" class="crosslink-card">
            <span class="crosslink-card__icon">{r['icon']}</span>
            <span>{r['title']}</span>
          </a>"""

    # Related zones
    zone_links = ""
    for zk in z.get("related_zones", []):
        if zk in ZONES:
            rz = ZONES[zk]
            zone_links += f"""
          <a href="{pfx}zones/{rz['slug']}.html" class="crosslink-card">
            <span class="crosslink-card__icon">{rz['icon']}</span>
            <span>{rz['label']}</span>
          </a>"""

    # HITL legend
    hitl_legend = """
    <div class="hitl-legend fade-up">
      <h3>Understanding HITL Gate Levels</h3>
      <p>Every process area in DevOps AI is classified by its Human-in-the-Loop (HITL) gate level — defining when AI acts autonomously and when human approval is required.</p>
      <div class="hitl-legend__grid">
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l0">L0 — Fully Automated</span>
          <p>AI executes autonomously with full logging. No human approval needed. Examples: ticket classification, monitoring alerts, report generation.</p>
        </div>
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l1">L1 — Notify</span>
          <p>AI executes and notifies the assigned human. Human can review, override, or escalate after the fact. Examples: SLA predictions, patch scheduling.</p>
        </div>
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l2">L2 — Approve to Proceed</span>
          <p>AI prepares and recommends, but a human must explicitly approve before execution. Examples: change requests, contract modifications, campaign launches.</p>
        </div>
        <div class="hitl-legend__item">
          <span class="hitl-badge hitl-badge--l3">L3 — Human Only</span>
          <p>Humans perform the action with AI providing decision support only. Examples: legal review, privileged access approval, incident legal response.</p>
        </div>
      </div>
    </div>"""

    json_ld = generate_json_ld("zone", {
        "title": f"{z['label']} — DevOps AI Zone {z['number']}",
        "description": z["tagline"],
        "breadcrumbs": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://devops.ai.rain.tech/"},
            {"@type": "ListItem", "position": 2, "name": "Platform", "item": "https://devops.ai.rain.tech/platform.html"},
            {"@type": "ListItem", "position": 3, "name": z["label"]}
        ]
    }, page_path)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{z['label']} — DevOps AI Zone {z['number']} | Powered by RainTech</title>
<meta name="description" content="{z['tagline']}">
<link rel="canonical" href="https://devops.ai.rain.tech/{page_path}">

<meta property="og:type" content="website">
<meta property="og:title" content="{z['label']} — DevOps AI Zone {z['number']}">
<meta property="og:description" content="{z['tagline']}">
<meta property="og:url" content="https://devops.ai.rain.tech/{page_path}">
<meta property="og:site_name" content="DevOps AI by RainTech">

<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}base.css">
<link rel="stylesheet" href="{pfx}style.css">

<script type="application/ld+json">
{json_ld}
</script>
</head>
<body>

{generate_header(z['label'], page_path)}

<main id="main-content">

  <!-- Zone Hero -->
  <section class="zone-page-header" style="--zone-accent: {z['accent']};" aria-label="{z['label']} overview">
    <div class="container">
      <div class="zone-badge fade-up">
        <span>{z['icon']}</span>
        <span>Zone {z['number']:02d}</span>
      </div>
      <h1 class="fade-up">{z['label']}</h1>
      <p class="zone-description fade-up">{z['tagline']}</p>
    </div>
  </section>

  <!-- Zone Description -->
  <section class="section" aria-label="About {z['label']}">
    <div class="container container--narrow">
      <div class="fade-up" style="font-size: var(--text-base); color: var(--text-secondary); line-height: 1.7;">
        <p>{z['description']}</p>
      </div>
    </div>
  </section>

  <!-- Process Areas -->
  <section class="section" aria-label="Process Areas" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Process Areas</span>
        <h2>{len(z['process_areas'])} Process Areas</h2>
        <p>Each process area is classified with a Human-in-the-Loop (HITL) gate level — defining the boundary between AI autonomy and human oversight.</p>
      </div>
      <div class="process-grid">{pa_cards}
      </div>
    </div>
  </section>

  <!-- HITL Legend -->
  <section class="section" aria-label="HITL gate levels">
    <div class="container container--narrow">
      {hitl_legend}
    </div>
  </section>

  <!-- Related Roles -->
  <section class="section crosslink-section" aria-label="Related roles" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">For Your Role</span>
        <h2>Who Uses {z['label']}?</h2>
        <p>See how {z['label']} transforms daily operations for these roles.</p>
      </div>
      <div class="crosslink-grid fade-up">{role_links}
      </div>
    </div>
  </section>

  <!-- Related Zones -->
  <section class="section crosslink-section" aria-label="Related zones">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Connected Zones</span>
        <h2>Works With</h2>
        <p>{z['label']} integrates deeply with these operational zones.</p>
      </div>
      <div class="crosslink-grid fade-up">{zone_links}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" aria-label="Call to action">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>See {z['label']} in Action</h2>
        <p>Deploy DevOps AI from the Azure Marketplace and explore {z['label']} capabilities in your own environment.</p>
        <a href="{pfx}marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
      </div>
    </div>
  </section>

</main>

{generate_footer(page_path)}
{generate_cookie_banner()}

<script src="{pfx}app.js"></script>
</body>
</html>"""
    return page


def generate_role_page(role_key):
    """Generate a complete role page."""
    r = ROLES[role_key]
    page_path = f"roles/{r['slug']}.html"
    pfx = path_prefix(page_path)
    
    # Zone tags
    zone_tags = ""
    all_zones = r.get("primary_zones", []) + r.get("secondary_zones", [])
    for zk in all_zones:
        if zk in ZONES:
            z = ZONES[zk]
            zone_tags += f'<a href="{pfx}zones/{z["slug"]}.html" class="role-zone-tag" style="border-color: {z["accent"]}40; color: {z["accent"]}">{z["icon"]} {z["label"]}</a>\n            '

    # Primary zone deep-dives
    zone_sections = ""
    for zk in r.get("primary_zones", []):
        if zk in ZONES:
            z = ZONES[zk]
            relevant_pas = ""
            for pa in z["process_areas"][:4]:
                relevant_pas += f"""
              <div class="process-card__step">
                <span class="process-card__step-name">{pa['name']}</span>
                {hitl_badge(pa['hitl'])}
              </div>"""
            
            zone_sections += f"""
    <div class="journey-phase fade-up">
      <h3><a href="{pfx}zones/{z['slug']}.html" style="color: {z['accent']}">{z['icon']} {z['label']}</a></h3>
      <p class="journey-phase__desc">{z['tagline']}</p>
      <div class="process-card" style="--zone-accent: {z['accent']}">
        <div class="process-card__steps">{relevant_pas}
        </div>
        <div style="margin-top: var(--space-4)">
          <a href="{pfx}zones/{z['slug']}.html" class="btn btn-secondary" style="font-size: 13px; padding: 8px 16px;">View All {z['label']} Process Areas →</a>
        </div>
      </div>
    </div>"""

    # Discovery → Evaluation → Daily → Growth journey narrative
    journey_content = f"""
  <section class="section journey-section" aria-label="Your journey">
    <div class="container container--narrow">
      <div class="section-header fade-up">
        <span class="section-label">Your Journey</span>
        <h2>How DevOps AI Transforms Your Role</h2>
      </div>
      
      <div class="journey-phase fade-up">
        <h3 class="journey-phase__title">Discovery</h3>
        <p class="journey-phase__desc">When you first encounter DevOps AI, here is what you will find relevant to your role as {r['title']}:</p>
        <ul style="color: var(--text-secondary); padding-left: var(--space-4); list-style: disc;">
          <li>A unified platform that consolidates the tools you already use</li>
          <li>AI-augmented workflows designed specifically for {r['title']} responsibilities</li>
          <li>Human-in-the-loop safety at every critical decision point</li>
        </ul>
      </div>
      
      <div class="journey-phase fade-up">
        <h3 class="journey-phase__title">What Getting Started Looks Like</h3>
        <p class="journey-phase__desc">Deploy from the Azure Marketplace in under 35 minutes. Your environment is provisioned with role-appropriate dashboards and workflow configurations.</p>
      </div>
      
      <div class="journey-phase fade-up">
        <h3 class="journey-phase__title">What Your Day Looks Like</h3>
        <p class="journey-phase__desc">With DevOps AI, your daily workflow is transformed across these primary zones:</p>
      </div>
    </div>
  </section>

  <section class="section" aria-label="Primary zones" style="background: var(--bg-secondary);">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-label">Your Zones</span>
        <h2>Primary Operational Zones</h2>
        <p>These are the zones where you spend most of your time as {r['title']}.</p>
      </div>
      {zone_sections}
    </div>
  </section>"""

    json_ld = generate_json_ld("role", {
        "title": f"{r['title']} — DevOps AI",
        "description": r["tagline"],
    }, page_path)

    new_badge = ' <span style="display:inline-block;font-size:11px;background:var(--accent);color:#001647;padding:2px 8px;border-radius:12px;font-weight:700;vertical-align:middle;">NEW</span>' if r.get("new") else ""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{r['title']} — DevOps AI | Powered by RainTech</title>
<meta name="description" content="{r['tagline']}">
<link rel="canonical" href="https://devops.ai.rain.tech/{page_path}">

<meta property="og:type" content="website">
<meta property="og:title" content="{r['title']} — DevOps AI">
<meta property="og:description" content="{r['tagline']}">
<meta property="og:url" content="https://devops.ai.rain.tech/{page_path}">
<meta property="og:site_name" content="DevOps AI by RainTech">

<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}base.css">
<link rel="stylesheet" href="{pfx}style.css">

<script type="application/ld+json">
{json_ld}
</script>
</head>
<body>

{generate_header(r['title'], page_path)}

<main id="main-content">

  <!-- Role Hero -->
  <section class="role-hero" aria-label="{r['title']} overview">
    <div class="container">
      <div style="font-size: 48px; margin-bottom: var(--space-3);" class="fade-up">{r['icon']}</div>
      <h1 class="role-title fade-up">{r['title']}{new_badge}</h1>
      <p class="role-tagline fade-up">{r['tagline']}</p>
      <div class="role-zones fade-up">
        {zone_tags}
      </div>
    </div>
  </section>

  {journey_content}

  <!-- Growth -->
  <section class="section" aria-label="Growth path">
    <div class="container container--narrow">
      <div class="section-header fade-up">
        <span class="section-label">Growth</span>
        <h2>What Growth Looks Like</h2>
      </div>
      <div class="fade-up" style="color: var(--text-secondary); line-height: 1.7;">
        <p>As you and your team mature with DevOps AI, the platform grows with you. AI models learn from your decisions, workflows adapt to your patterns, and the platform surfaces increasingly sophisticated recommendations. The {r['title']} who started with basic automation finds themselves operating at a strategic level — with AI handling the tactical execution.</p>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section" aria-label="Call to action">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>Ready to Transform Your {r['title']} Experience?</h2>
        <p>Deploy DevOps AI from the Azure Marketplace and see how the platform transforms your daily operations.</p>
        <div class="hero-actions">
          <a href="{pfx}marketplace.html" class="btn btn-dark btn-lg">Get Started on Azure Marketplace</a>
          <a href="{pfx}contact.html" class="btn btn-secondary btn-lg">Schedule a Demo</a>
        </div>
      </div>
    </div>
  </section>

</main>

{generate_footer(page_path)}
{generate_cookie_banner()}

<script src="{pfx}app.js"></script>
</body>
</html>"""
    return page


def generate_roles_index():
    """Generate the roles landing/index page."""
    page_path = "roles/index.html"
    pfx = path_prefix(page_path)
    
    role_cards = ""
    for rk, r in ROLES.items():
        new = ' <span style="font-size:10px;background:var(--accent);color:#001647;padding:1px 6px;border-radius:8px;font-weight:700;">NEW</span>' if r.get("new") else ""
        zone_tags_mini = ""
        for zk in r.get("primary_zones", [])[:3]:
            if zk in ZONES:
                z = ZONES[zk]
                zone_tags_mini += f'<span class="role-zone-tag" style="font-size:11px;padding:2px 8px;">{z["icon"]} {z["label"]}</span> '
        
        role_cards += f"""
        <a href="{pfx}roles/{r['slug']}.html" class="role-card fade-up">
          <div class="role-card-icon">{r['icon']}</div>
          <h3>{r['title']}{new}</h3>
          <p>{r['tagline'][:120]}{'...' if len(r['tagline']) > 120 else ''}</p>
          <div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:var(--space-2);">{zone_tags_mini}</div>
          <span class="role-card-arrow">Explore →</span>
        </a>"""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
{PPLX_HEAD}

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For Your Role — DevOps AI | Powered by RainTech</title>
<meta name="description" content="Discover how DevOps AI transforms daily operations for every role in the MSP ecosystem — from MSP Owner to Security Analyst to Compliance Officer.">
<link rel="canonical" href="https://devops.ai.rain.tech/roles/">

<meta property="og:type" content="website">
<meta property="og:title" content="For Your Role — DevOps AI">
<meta property="og:description" content="Discover how DevOps AI transforms daily operations for every role in the MSP ecosystem.">
<meta property="og:url" content="https://devops.ai.rain.tech/roles/">
<meta property="og:site_name" content="DevOps AI by RainTech">

<link rel="icon" type="image/svg+xml" href="{pfx}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pfx}base.css">
<link rel="stylesheet" href="{pfx}style.css">
</head>
<body>

{generate_header("For Your Role", page_path)}

<main id="main-content">

  <section class="hero" style="min-height: 50vh;" aria-label="Roles overview">
    <div class="hero-bg"></div>
    <div class="container hero-content">
      <div class="hero-badge fade-up"><span class="dot"></span> 14 Role-Specific Experiences</div>
      <h1 class="fade-up">Built for<br>Every Role</h1>
      <p class="hero-sub fade-up">DevOps AI is designed for every role in the MSP ecosystem. Select your role to see exactly how the platform transforms your daily workflow, with specific process areas and HITL gate levels for every operation.</p>
    </div>
  </section>

  <section class="section" aria-label="All roles">
    <div class="container">
      <div class="role-grid">{role_cards}
      </div>
    </div>
  </section>

  <section class="section" aria-label="Call to action">
    <div class="container">
      <div class="cta-banner fade-up">
        <h2>Ready to See DevOps AI in Action?</h2>
        <p>Deploy from the Azure Marketplace and explore the platform with your team.</p>
        <a href="{pfx}marketplace.html" class="btn btn-dark btn-lg">Get Started</a>
      </div>
    </div>
  </section>

</main>

{generate_footer(page_path)}
{generate_cookie_banner()}

<script src="{pfx}app.js"></script>
</body>
</html>"""
    return page


# ═══════════════════════════════════════════════════════════════════════
# MAIN GENERATION
# ═══════════════════════════════════════════════════════════════════════

def main():
    """Generate all pages."""
    generated = []
    
    # Generate zone pages
    for zone_key in ZONES:
        z = ZONES[zone_key]
        filepath = os.path.join(SITE_DIR, "zones", f"{z['slug']}.html")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        content = generate_zone_page(zone_key)
        with open(filepath, "w") as f:
            f.write(content)
        generated.append(filepath)
        print(f"  ✓ zones/{z['slug']}.html")

    # Generate role pages
    for role_key in ROLES:
        r = ROLES[role_key]
        filepath = os.path.join(SITE_DIR, "roles", f"{r['slug']}.html")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        content = generate_role_page(role_key)
        with open(filepath, "w") as f:
            f.write(content)
        generated.append(filepath)
        print(f"  ✓ roles/{r['slug']}.html")

    # Roles index
    filepath = os.path.join(SITE_DIR, "roles", "index.html")
    with open(filepath, "w") as f:
        f.write(generate_roles_index())
    generated.append(filepath)
    print(f"  ✓ roles/index.html")
    
    print(f"\nGenerated {len(generated)} pages total.")
    return generated


if __name__ == "__main__":
    main()
