#!/usr/bin/env python3
"""Build pa-data.json from the canonical PA list.

This script generates the structured JSON data for all 157 process areas.
Run once to create/update scripts/pa-data.json, then use generate-pa-pages.py
to produce the HTML files.
"""
import json, os, sys

ZONES = [
    {
        "name": "Service Desk",
        "slug": "service-desk",
        "cluster": "Service & Security",
        "tagline": "AI-Powered Ticket Intelligence",
        "icon": "🎫",
        "process_areas": [
            {
                "name": "Ticket Ingestion & AI Triage",
                "slug": "ticket-ingestion-ai-triage",
                "description": "Intelligent ticket classification and routing powered by NLP",
                "overview": "The Ticket Ingestion & AI Triage process area is the front door of your MSP's service operations. Every ticket — whether it arrives via email, client portal, chat, phone, or API integration — is captured, normalized, and immediately analyzed by the AI triage engine.\n\nUsing natural language processing (NLP), the system classifies each ticket by category, priority, urgency, and complexity within seconds. It identifies the affected client, maps to the correct SLA tier, and determines whether the issue matches known error patterns or requires human intervention.\n\nThe AI routing engine then assigns the ticket to the optimal technician based on skill match, current workload, shift schedule, and historical resolution success rates — ensuring every issue reaches the right hands at the right time.",
                "how_it_works": [
                    {"step": 1, "title": "Ingest", "description": "Tickets arrive via email, portal, chat, phone, or API. The system normalizes all inputs into a unified ticket format."},
                    {"step": 2, "title": "Classify", "description": "NLP engine analyzes the ticket text to determine category, priority, urgency, and affected systems."},
                    {"step": 3, "title": "Score", "description": "AI assigns a confidence score and checks against known error database for potential auto-resolution matches."},
                    {"step": 4, "title": "Route", "description": "Smart routing assigns the ticket to the best-fit technician based on skills, workload, and SLA requirements."},
                    {"step": 5, "title": "Monitor", "description": "SLA timers start automatically. Predictive breach detection monitors resolution progress in real time."}
                ],
                "ai_capabilities": ["NLP ticket classification", "Predictive priority scoring", "Smart routing based on technician skills", "Auto-detection of duplicate tickets"],
                "hitl_checkpoints": ["Manual override on routing decisions", "Review queue for low-confidence classifications", "Escalation approval for priority changes"],
                "key_metrics": ["Avg triage time <30 seconds", "Classification accuracy >95%", "First-touch resolution rate improvement"],
                "connected_pas": [
                    {"name": "NLP Intake & Classification", "slug": "nlp-intake-classification", "zone_slug": "service-desk"},
                    {"name": "SLA Management & Prediction", "slug": "sla-management-prediction", "zone_slug": "service-desk"},
                    {"name": "Assignment Optimization", "slug": "assignment-optimization", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "IT Director"],
                "related_role_slugs": ["service-desk-manager", "it-director"]
            },
            {
                "name": "NLP Intake & Classification",
                "slug": "nlp-intake-classification",
                "description": "Natural language processing for automatic ticket categorization and sentiment analysis",
                "overview": "NLP Intake & Classification brings advanced natural language understanding to every ticket that enters your service desk. Rather than relying on end users to correctly categorize their issues, the AI reads the full text of each submission and determines the true intent, affected service, and emotional tone.\n\nThe system continuously learns from your technicians' re-classifications, building an ever-improving model specific to your MSP's client base. Over time, classification accuracy increases as the model adapts to your unique terminology and service catalog.\n\nSentiment analysis adds another dimension — detecting frustrated, anxious, or satisfied language patterns helps prioritize tickets where client relationships may be at risk, even before the issue itself is severe.",
                "how_it_works": [
                    {"step": 1, "title": "Parse", "description": "NLP engine extracts key entities, intent, and context from the raw ticket text."},
                    {"step": 2, "title": "Classify", "description": "Multi-label classification assigns category, subcategory, and affected service from your catalog."},
                    {"step": 3, "title": "Analyze Sentiment", "description": "Tone and urgency are scored to flag emotionally charged tickets for priority handling."},
                    {"step": 4, "title": "Enrich", "description": "AI appends classification metadata and confidence scores to the ticket record."}
                ],
                "ai_capabilities": ["Multi-label classification", "Named entity recognition", "Sentiment analysis", "Continuous learning from corrections"],
                "hitl_checkpoints": ["Override classifications when confidence is low", "Review misclassified tickets to improve model"],
                "key_metrics": ["Classification accuracy >95%", "Sentiment detection precision >90%", "Avg classification time <5 seconds"],
                "connected_pas": [
                    {"name": "Ticket Ingestion & AI Triage", "slug": "ticket-ingestion-ai-triage", "zone_slug": "service-desk"},
                    {"name": "Playbook Automation", "slug": "playbook-automation", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "Service Delivery Manager"],
                "related_role_slugs": ["service-desk-manager", "service-delivery-manager"]
            },
            {
                "name": "SLA Management & Prediction",
                "slug": "sla-management-prediction",
                "description": "Real-time SLA tracking with predictive breach alerts and automated escalation triggers",
                "overview": "SLA Management & Prediction ensures your MSP never misses a service level commitment. The system tracks every active ticket against its contractual SLA targets in real time, calculating remaining time and probability of on-time resolution.\n\nPredictive analytics go beyond simple countdown timers. The AI considers current technician workload, ticket complexity, historical resolution patterns, and even time-of-day factors to forecast whether each ticket will meet its SLA — often hours before a breach would occur.\n\nWhen a potential breach is detected, automated escalation workflows kick in: reassigning tickets, notifying managers, or adjusting priority to ensure commitments are met. Post-resolution, SLA performance data feeds into QBR reporting and client health scoring.",
                "how_it_works": [
                    {"step": 1, "title": "Map", "description": "Each ticket is mapped to the correct SLA tier based on client contract and issue category."},
                    {"step": 2, "title": "Track", "description": "Real-time countdown timers track response and resolution deadlines with pause/resume for awaiting-client."},
                    {"step": 3, "title": "Predict", "description": "AI forecasts breach probability using workload, complexity, and historical patterns."},
                    {"step": 4, "title": "Escalate", "description": "Automated escalation triggers when breach probability exceeds threshold, reassigning or reprioritizing."},
                    {"step": 5, "title": "Report", "description": "SLA performance metrics feed dashboards, QBR reports, and client health scores."}
                ],
                "ai_capabilities": ["Predictive breach detection", "Dynamic priority adjustment", "Automated escalation workflows", "SLA compliance forecasting"],
                "hitl_checkpoints": ["Approve SLA pause/resume actions", "Override automated escalations", "Review SLA exception requests"],
                "key_metrics": ["SLA compliance >99%", "Avg breach prediction lead time >2 hours", "Escalation response time <15 minutes"],
                "connected_pas": [
                    {"name": "Ticket Ingestion & AI Triage", "slug": "ticket-ingestion-ai-triage", "zone_slug": "service-desk"},
                    {"name": "CSAT Collection & Analysis", "slug": "csat-collection-analysis", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "Service Delivery Manager", "IT Director"],
                "related_role_slugs": ["service-desk-manager", "service-delivery-manager", "it-director"]
            },
            {
                "name": "Playbook Automation",
                "slug": "playbook-automation",
                "description": "Automated runbook execution for common issue resolution patterns",
                "overview": "Playbook Automation transforms your proven resolution procedures into executable AI-driven workflows. When a ticket matches a known issue pattern, the system can automatically execute the corresponding playbook — running diagnostic checks, applying fixes, and verifying resolution without human intervention.\n\nPlaybooks are built from your team's institutional knowledge: the steps your best technicians follow to resolve recurring issues. The AI captures these patterns, validates them against historical success rates, and executes them consistently every time.\n\nFor issues requiring human judgment, playbooks guide technicians through step-by-step resolution with contextual hints, reducing time-to-resolution and ensuring consistency across your team.",
                "how_it_works": [
                    {"step": 1, "title": "Match", "description": "AI matches incoming tickets against the playbook library using pattern recognition."},
                    {"step": 2, "title": "Execute", "description": "Automated playbooks run diagnostic and remediation steps via API integrations."},
                    {"step": 3, "title": "Verify", "description": "Post-execution checks confirm the issue is resolved and systems are healthy."},
                    {"step": 4, "title": "Learn", "description": "Success and failure data feeds back to improve playbook accuracy over time."}
                ],
                "ai_capabilities": ["Pattern matching for playbook selection", "Automated remediation execution", "Success rate tracking", "Playbook optimization suggestions"],
                "hitl_checkpoints": ["Approval required for high-impact playbooks", "Manual verification of automated fixes", "Playbook creation and editing"],
                "key_metrics": ["Playbook auto-resolution rate >40%", "Avg playbook execution time <3 minutes", "Playbook library coverage >80% of recurring issues"],
                "connected_pas": [
                    {"name": "NLP Intake & Classification", "slug": "nlp-intake-classification", "zone_slug": "service-desk"},
                    {"name": "Known Error Database (KEDB)", "slug": "known-error-database-kedb", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "DevOps Engineer"],
                "related_role_slugs": ["service-desk-manager", "devops-engineer"]
            },
            {
                "name": "Assignment Optimization",
                "slug": "assignment-optimization",
                "description": "AI-optimized ticket assignment based on skills, workload, and availability",
                "overview": "Assignment Optimization uses AI to ensure every ticket reaches the technician best equipped to resolve it quickly. The system maintains real-time profiles of each team member's skills, certifications, current workload, and historical success rates across different issue types.\n\nWhen a new ticket needs assignment, the AI evaluates all available technicians and scores them on fit. Factors include technical expertise match, current queue depth, shift schedule, and even client familiarity — because technicians who know a client's environment resolve issues faster.\n\nThe result is fewer reassignments, faster resolution times, and more balanced workloads across your team.",
                "how_it_works": [
                    {"step": 1, "title": "Profile", "description": "AI maintains real-time skill and workload profiles for every technician."},
                    {"step": 2, "title": "Score", "description": "Each available technician is scored against the ticket requirements."},
                    {"step": 3, "title": "Assign", "description": "The highest-scoring technician receives the assignment with full context."},
                    {"step": 4, "title": "Balance", "description": "Workload balancing ensures no single technician is overloaded."}
                ],
                "ai_capabilities": ["Skill-based matching", "Workload balancing", "Client familiarity scoring", "Schedule-aware assignment"],
                "hitl_checkpoints": ["Manual reassignment override", "Team lead approval for cross-skill assignments"],
                "key_metrics": ["First-assignment resolution >75%", "Reassignment rate <10%", "Workload variance <15%"],
                "connected_pas": [
                    {"name": "Ticket Ingestion & AI Triage", "slug": "ticket-ingestion-ai-triage", "zone_slug": "service-desk"},
                    {"name": "Dispatch Optimization", "slug": "dispatch-optimization", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "IT Director"],
                "related_role_slugs": ["service-desk-manager", "it-director"]
            },
            {
                "name": "Dispatch Optimization",
                "slug": "dispatch-optimization",
                "description": "Smart field dispatch scheduling with route optimization and skill matching",
                "overview": "Dispatch Optimization brings AI intelligence to on-site service delivery. When a ticket requires a field visit, the system schedules the optimal technician based on proximity, skills, parts availability, and client preferences.\n\nRoute optimization minimizes travel time by clustering nearby appointments and considering traffic patterns. The AI also predicts appointment duration based on historical data for similar issues, ensuring realistic scheduling that reduces overtime and missed appointments.\n\nReal-time updates keep clients informed with accurate arrival windows, while technicians receive full context — including site access details, past visit notes, and pre-staged diagnostic information.",
                "how_it_works": [
                    {"step": 1, "title": "Identify", "description": "System flags tickets requiring on-site dispatch based on issue type and remote troubleshooting results."},
                    {"step": 2, "title": "Schedule", "description": "AI selects the optimal technician and time slot based on proximity, skills, and availability."},
                    {"step": 3, "title": "Optimize", "description": "Route optimization clusters appointments and minimizes travel time."},
                    {"step": 4, "title": "Notify", "description": "Client receives appointment confirmation with real-time arrival tracking."}
                ],
                "ai_capabilities": ["Route optimization", "Duration prediction", "Skill-proximity matching", "Real-time ETA tracking"],
                "hitl_checkpoints": ["Dispatcher approval for schedule changes", "Client confirmation of appointment windows"],
                "key_metrics": ["On-time arrival >95%", "Travel time reduction >25%", "First-visit resolution >85%"],
                "connected_pas": [
                    {"name": "Assignment Optimization", "slug": "assignment-optimization", "zone_slug": "service-desk"},
                    {"name": "Service Request Fulfillment", "slug": "service-request-fulfillment", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "Network Engineer"],
                "related_role_slugs": ["service-desk-manager", "network-engineer"]
            },
            {
                "name": "Known Error Database (KEDB)",
                "slug": "known-error-database-kedb",
                "description": "AI-maintained knowledge base of known errors and proven resolutions",
                "overview": "The Known Error Database (KEDB) is a living repository of resolved issues, root causes, and proven workarounds. Unlike traditional knowledge bases that require manual curation, the KEDB is continuously enriched by AI that identifies patterns across resolved tickets.\n\nWhen a new ticket arrives, the AI cross-references it against the KEDB, surfacing matching solutions with confidence scores. Technicians can apply known fixes with one click, dramatically reducing resolution time for recurring issues.\n\nThe system also identifies emerging error patterns — grouping similar incidents that may represent a new known error, prompting your team to document root causes before they become widespread.",
                "how_it_works": [
                    {"step": 1, "title": "Capture", "description": "AI analyzes resolved tickets to identify recurring patterns and their successful resolutions."},
                    {"step": 2, "title": "Catalog", "description": "Known errors are documented with root cause, symptoms, workaround, and permanent fix details."},
                    {"step": 3, "title": "Match", "description": "New tickets are cross-referenced against the KEDB for instant solution suggestions."},
                    {"step": 4, "title": "Evolve", "description": "The KEDB self-updates as new resolutions are confirmed and patterns change."}
                ],
                "ai_capabilities": ["Pattern detection across tickets", "Solution matching with confidence scores", "Auto-documentation of resolutions", "Emerging error identification"],
                "hitl_checkpoints": ["Approval for new known error entries", "Review of auto-generated resolutions", "Root cause validation"],
                "key_metrics": ["KEDB match rate >65%", "Solution accuracy >90%", "Avg time saved per matched ticket >15 minutes"],
                "connected_pas": [
                    {"name": "Playbook Automation", "slug": "playbook-automation", "zone_slug": "service-desk"},
                    {"name": "Problem Management Lifecycle", "slug": "problem-management-lifecycle", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "IT Director"],
                "related_role_slugs": ["service-desk-manager", "it-director"]
            },
            {
                "name": "CSAT Collection & Analysis",
                "slug": "csat-collection-analysis",
                "description": "Automated satisfaction surveys with sentiment analysis and trend detection",
                "overview": "CSAT Collection & Analysis automates the entire customer satisfaction feedback loop. After every ticket resolution, the system sends context-appropriate surveys and analyzes responses using AI-powered sentiment analysis.\n\nBeyond simple numerical ratings, the AI reads free-text feedback to extract themes, detect frustration signals, and identify service improvement opportunities. Trend analysis spots patterns across clients, technicians, and issue categories — revealing systemic issues before they erode satisfaction.\n\nDetractor alerts trigger immediate recovery workflows, ensuring unhappy clients receive personal follow-up before dissatisfaction becomes churn risk.",
                "how_it_works": [
                    {"step": 1, "title": "Survey", "description": "Automated, context-appropriate surveys are sent post-resolution via the client's preferred channel."},
                    {"step": 2, "title": "Analyze", "description": "AI performs sentiment analysis on ratings and free-text feedback."},
                    {"step": 3, "title": "Trend", "description": "Cross-client and cross-technician trend analysis reveals systemic patterns."},
                    {"step": 4, "title": "Act", "description": "Detractor alerts trigger recovery workflows; insights feed QBR reporting."}
                ],
                "ai_capabilities": ["Sentiment analysis on feedback", "Theme extraction from free text", "Trend detection across dimensions", "Detractor prediction"],
                "hitl_checkpoints": ["Review and respond to detractor alerts", "Customize survey templates", "Validate AI trend insights"],
                "key_metrics": ["Survey response rate >40%", "CSAT score >4.5/5.0", "Detractor recovery rate >70%"],
                "connected_pas": [
                    {"name": "SLA Management & Prediction", "slug": "sla-management-prediction", "zone_slug": "service-desk"},
                    {"name": "Client Health Scoring", "slug": "client-health-scoring", "zone_slug": "relationships"}
                ],
                "related_roles": ["Service Delivery Manager", "Client Success Manager"],
                "related_role_slugs": ["service-delivery-manager", "client-success-manager"]
            },
            {
                "name": "Cross-Client Problem Intelligence",
                "slug": "cross-client-problem-intelligence",
                "description": "AI-driven pattern detection across multiple client environments",
                "overview": "Cross-Client Problem Intelligence is one of the most powerful capabilities in the DevOps AI platform. By analyzing ticket patterns across your entire MSP client base (while maintaining strict data isolation), the AI identifies issues affecting multiple clients simultaneously.\n\nWhen a vendor update breaks something, a service outage begins, or a new vulnerability is exploited, the system detects the pattern across clients and creates a unified problem record. This enables your team to address the root cause once rather than fighting the same fire 50 times.\n\nThe AI also provides early warning: when tickets start clustering around a new pattern, alerts fire before the problem becomes widespread, giving your team a head start on investigation and communication.",
                "how_it_works": [
                    {"step": 1, "title": "Monitor", "description": "AI continuously monitors ticket streams across all clients for emerging patterns."},
                    {"step": 2, "title": "Correlate", "description": "Similar tickets are grouped by symptoms, timing, and affected systems."},
                    {"step": 3, "title": "Alert", "description": "Early warning fires when ticket clusters exceed normal variance thresholds."},
                    {"step": 4, "title": "Unify", "description": "A single problem record is created with links to all affected tickets and clients."}
                ],
                "ai_capabilities": ["Multi-tenant pattern detection", "Early warning on emerging issues", "Root cause correlation", "Impact scope analysis"],
                "hitl_checkpoints": ["Confirm cross-client problem linkage", "Approve mass communication to affected clients", "Validate root cause analysis"],
                "key_metrics": ["Pattern detection time <15 minutes", "False positive rate <5%", "Mean time to identify root cause reduced >50%"],
                "connected_pas": [
                    {"name": "Problem Management Lifecycle", "slug": "problem-management-lifecycle", "zone_slug": "service-desk"},
                    {"name": "Known Error Database (KEDB)", "slug": "known-error-database-kedb", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "IT Director", "Service Delivery Manager"],
                "related_role_slugs": ["service-desk-manager", "it-director", "service-delivery-manager"]
            },
            {
                "name": "Problem Management Lifecycle",
                "slug": "problem-management-lifecycle",
                "description": "End-to-end problem management from detection through root cause to resolution",
                "overview": "Problem Management Lifecycle provides a structured, AI-assisted approach to identifying and eliminating the root causes behind recurring incidents. While incident management fixes symptoms, problem management prevents recurrence.\n\nThe AI identifies problem candidates by detecting ticket clusters, recurring issue patterns, and high-impact incidents. It guides your team through root cause analysis with data-driven suggestions, tracks workarounds, and monitors the effectiveness of permanent fixes.\n\nFull lifecycle tracking ensures nothing falls through the cracks — from problem identification through investigation, workaround documentation, root cause resolution, and post-implementation review.",
                "how_it_works": [
                    {"step": 1, "title": "Identify", "description": "AI flags problem candidates from recurring incidents, ticket clusters, and trend analysis."},
                    {"step": 2, "title": "Investigate", "description": "Root cause analysis guided by AI-suggested investigation paths and correlated data."},
                    {"step": 3, "title": "Workaround", "description": "Interim workarounds are documented and linked to affected tickets for immediate relief."},
                    {"step": 4, "title": "Resolve", "description": "Permanent fix is implemented, tested, and verified across all affected environments."},
                    {"step": 5, "title": "Review", "description": "Post-implementation review confirms the problem is eliminated and lessons learned are captured."}
                ],
                "ai_capabilities": ["Problem candidate identification", "Root cause suggestion engine", "Workaround effectiveness tracking", "Recurrence monitoring"],
                "hitl_checkpoints": ["Approve problem records", "Validate root cause findings", "Sign off on permanent fixes"],
                "key_metrics": ["Problem backlog aging <30 days", "Recurring incident reduction >60%", "Root cause identification rate >85%"],
                "connected_pas": [
                    {"name": "Cross-Client Problem Intelligence", "slug": "cross-client-problem-intelligence", "zone_slug": "service-desk"},
                    {"name": "Known Error Database (KEDB)", "slug": "known-error-database-kedb", "zone_slug": "service-desk"}
                ],
                "related_roles": ["Service Desk Manager", "IT Director"],
                "related_role_slugs": ["service-desk-manager", "it-director"]
            },
            {
                "name": "Service Request Fulfillment",
                "slug": "service-request-fulfillment",
                "description": "Automated service catalog with self-service provisioning and approval workflows",
                "overview": "Service Request Fulfillment automates the handling of pre-defined service requests — new user setup, access provisioning, software installation, hardware orders, and more. Unlike break-fix incidents, service requests follow predictable workflows that are perfect for AI automation.\n\nThe system presents a self-service catalog to end users, guiding them through request submission with smart forms that adapt based on their role and previous requests. Behind the scenes, AI handles approvals, provisioning, and fulfillment — escalating to humans only when policies require it.\n\nFull audit trails ensure compliance, while fulfillment metrics help optimize your service catalog over time.",
                "how_it_works": [
                    {"step": 1, "title": "Request", "description": "Users submit requests through the self-service catalog with smart, adaptive forms."},
                    {"step": 2, "title": "Approve", "description": "Automated approval routing based on request type, cost, and organizational policy."},
                    {"step": 3, "title": "Fulfill", "description": "AI executes provisioning workflows via integrations with identity, endpoint, and cloud systems."},
                    {"step": 4, "title": "Confirm", "description": "Requestor is notified of completion; satisfaction survey follows."}
                ],
                "ai_capabilities": ["Smart form adaptation", "Automated approval routing", "Provisioning workflow execution", "Catalog optimization suggestions"],
                "hitl_checkpoints": ["Manager approval for cost-bearing requests", "Security review for access requests", "Custom fulfillment for non-standard requests"],
                "key_metrics": ["Avg fulfillment time <4 hours", "Self-service adoption >60%", "First-time-right rate >95%"],
                "connected_pas": [
                    {"name": "Dispatch Optimization", "slug": "dispatch-optimization", "zone_slug": "service-desk"},
                    {"name": "Employee Onboarding Automation", "slug": "employee-onboarding-automation", "zone_slug": "people"}
                ],
                "related_roles": ["Service Desk Manager", "HR Director"],
                "related_role_slugs": ["service-desk-manager", "hr-director"]
            },
            {
                "name": "Co-Managed IT Workflows",
                "slug": "co-managed-it-workflows",
                "description": "Shared workflows for MSPs co-managing IT with client internal teams",
                "overview": "Co-Managed IT Workflows bridges the gap between your MSP team and your clients' internal IT staff. In co-managed environments, clear role boundaries, shared visibility, and seamless handoffs are critical to avoiding duplicate effort and finger-pointing.\n\nThe system provides configurable workflow boundaries that define which team handles which issue types, with clear escalation paths between internal IT and MSP resources. Shared dashboards give both teams visibility into ticket status without exposing sensitive MSP operational data.\n\nAI monitors handoff patterns to identify bottlenecks and suggest workflow optimizations, ensuring the co-managed relationship delivers maximum value to the client.",
                "how_it_works": [
                    {"step": 1, "title": "Define", "description": "Configure responsibility boundaries between MSP and client IT teams per service category."},
                    {"step": 2, "title": "Route", "description": "AI routes tickets to the correct team based on configured boundaries and escalation rules."},
                    {"step": 3, "title": "Handoff", "description": "Seamless ticket handoffs between teams with full context transfer and SLA continuity."},
                    {"step": 4, "title": "Optimize", "description": "AI analyzes handoff patterns and suggests boundary adjustments for better efficiency."}
                ],
                "ai_capabilities": ["Intelligent team routing", "Handoff context packaging", "Boundary optimization suggestions", "Shared visibility controls"],
                "hitl_checkpoints": ["Approve boundary configuration changes", "Review cross-team escalations", "Client sign-off on role definitions"],
                "key_metrics": ["Cross-team handoff time <30 minutes", "Duplicate ticket rate <3%", "Co-managed CSAT >4.3/5.0"],
                "connected_pas": [
                    {"name": "Assignment Optimization", "slug": "assignment-optimization", "zone_slug": "service-desk"},
                    {"name": "Customer Portal Management", "slug": "customer-portal-management", "zone_slug": "relationships"}
                ],
                "related_roles": ["IT Director", "Service Delivery Manager"],
                "related_role_slugs": ["it-director", "service-delivery-manager"]
            }
        ]
    },
    {
        "name": "Security Operations",
        "slug": "security-operations",
        "cluster": "Service & Security",
        "tagline": "Always-On Threat Defense",
        "icon": "🔒",
        "process_areas": [
            {"name": "Threat Intelligence Feeds", "slug": "threat-intelligence-feeds", "description": "Aggregated threat intelligence from multiple sources with AI correlation",
             "overview": "Threat Intelligence Feeds aggregates and correlates threat data from commercial feeds, open-source intelligence (OSINT), dark web monitoring, and your own historical incident data. The AI normalizes indicators of compromise (IoCs) across formats, deduplicates entries, and enriches them with context relevant to your client environments.\n\nThe platform continuously cross-references incoming intelligence against your clients' asset inventories, identifying which threats are most relevant to each environment. This prioritized approach ensures your team focuses on the threats that matter most, rather than drowning in raw feed data.\n\nAutomated alerting and integration with detection engineering means new threat intelligence can be operationalized in minutes rather than days.",
             "how_it_works": [{"step": 1, "title": "Aggregate", "description": "Collect threat data from commercial, OSINT, and proprietary intelligence sources."},{"step": 2, "title": "Normalize", "description": "AI normalizes IoCs across formats (STIX, TAXII, CSV) into a unified taxonomy."},{"step": 3, "title": "Correlate", "description": "Cross-reference threats against client asset inventories to determine relevance."},{"step": 4, "title": "Operationalize", "description": "High-relevance indicators are pushed to detection rules and blocking lists automatically."}],
             "ai_capabilities": ["Multi-source correlation", "Relevance scoring per client", "IoC deduplication", "Automated detection rule generation"],
             "hitl_checkpoints": ["Review high-impact threat assessments", "Approve automated blocking actions", "Validate intelligence source reliability"],
             "key_metrics": ["Avg time to operationalize intelligence <1 hour", "Relevant threat identification rate >85%", "False positive rate <10%"],
             "connected_pas": [{"name": "Detection Engineering", "slug": "detection-engineering", "zone_slug": "security-operations"},{"name": "Dark Web Monitoring", "slug": "dark-web-monitoring", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "vCISO"], "related_role_slugs": ["security-analyst", "vciso"]},
            {"name": "Detection Engineering", "slug": "detection-engineering", "description": "Custom detection rule creation and tuning for threat identification",
             "overview": "Detection Engineering is the art and science of building, tuning, and maintaining the detection rules that identify threats in your clients' environments. The AI assists by analyzing attack techniques (mapped to MITRE ATT&CK), suggesting detection logic, and automatically tuning rules to reduce false positives.\n\nThe platform maintains a library of detection rules covering common attack patterns, and the AI continuously generates new rules based on emerging threats from intelligence feeds. Each rule is tested against historical data before deployment to predict its effectiveness and noise level.\n\nRule performance is tracked continuously — detection rules that generate too many false positives are automatically flagged for tuning, while gaps in coverage are identified by mapping your ruleset against the ATT&CK framework.",
             "how_it_works": [{"step": 1, "title": "Analyze", "description": "Map threat landscape against MITRE ATT&CK to identify detection gaps."},{"step": 2, "title": "Build", "description": "AI suggests detection logic; engineers refine and validate rules."},{"step": 3, "title": "Test", "description": "Rules are tested against historical data to predict effectiveness and false positive rate."},{"step": 4, "title": "Deploy", "description": "Approved rules are deployed across client environments with monitoring."},{"step": 5, "title": "Tune", "description": "AI continuously tunes rules based on alert feedback and environmental changes."}],
             "ai_capabilities": ["MITRE ATT&CK mapping", "Auto-generated detection rules", "Historical backtesting", "False positive reduction"],
             "hitl_checkpoints": ["Approve new detection rules", "Review rule performance reports", "Validate ATT&CK coverage gaps"],
             "key_metrics": ["ATT&CK technique coverage >80%", "False positive rate <5%", "New rule deployment time <24 hours"],
             "connected_pas": [{"name": "Threat Intelligence Feeds", "slug": "threat-intelligence-feeds", "zone_slug": "security-operations"},{"name": "EDR/XDR Integration", "slug": "edr-xdr-integration", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "vCISO"], "related_role_slugs": ["security-analyst", "vciso"]},
            {"name": "Incident Response Orchestration", "slug": "incident-response-orchestration", "description": "Automated incident response workflows with playbook execution",
             "overview": "Incident Response Orchestration automates and coordinates your MSP's response to security incidents. When a threat is detected, the system automatically initiates the appropriate response playbook — containing, investigating, and remediating the threat with speed and precision.\n\nThe AI orchestrates actions across multiple security tools simultaneously: isolating endpoints via EDR, blocking IPs at the firewall, disabling compromised accounts in Azure AD, and collecting forensic evidence — all within seconds of detection.\n\nFull incident timelines are maintained automatically, documenting every action taken, every decision made, and every piece of evidence collected. This ensures compliance with reporting requirements and provides the documentation needed for post-incident reviews.",
             "how_it_works": [{"step": 1, "title": "Detect", "description": "Alert triggers from detection rules, EDR, or threat intelligence match."},{"step": 2, "title": "Triage", "description": "AI assesses severity, scope, and potential impact across affected client environments."},{"step": 3, "title": "Contain", "description": "Automated containment actions execute: endpoint isolation, account lockdown, network segmentation."},{"step": 4, "title": "Investigate", "description": "Forensic data collection and correlation builds the complete incident picture."},{"step": 5, "title": "Remediate", "description": "Root cause addressed, systems restored, and preventive measures implemented."}],
             "ai_capabilities": ["Automated containment", "Cross-tool orchestration", "Forensic timeline assembly", "Impact scope analysis"],
             "hitl_checkpoints": ["Approve high-impact containment actions", "Review forensic findings", "Sign off on incident closure"],
             "key_metrics": ["Mean time to contain <15 minutes", "Automated response rate >70%", "Incident documentation completeness >95%"],
             "connected_pas": [{"name": "Detection Engineering", "slug": "detection-engineering", "zone_slug": "security-operations"},{"name": "EDR/XDR Integration", "slug": "edr-xdr-integration", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "vCISO", "IT Director"], "related_role_slugs": ["security-analyst", "vciso", "it-director"]},
            {"name": "Vulnerability Scanning & Remediation", "slug": "vulnerability-scanning-remediation", "description": "Continuous vulnerability assessment with AI-prioritized remediation",
             "overview": "Vulnerability Scanning & Remediation provides continuous assessment of your clients' environments, identifying security weaknesses before attackers can exploit them. The AI goes beyond simple CVSS scoring — it contextualizes each vulnerability based on the specific client environment, exposure level, and threat intelligence.\n\nRemediation is prioritized using a risk-based approach: a critical vulnerability on an internet-facing server with known exploits ranks higher than the same CVE on an isolated internal system. The AI generates remediation plans, tracks patch deployment, and verifies fixes — closing the loop from discovery to resolution.\n\nCross-client vulnerability intelligence identifies common weaknesses across your MSP's client base, enabling proactive remediation campaigns before issues become incidents.",
             "how_it_works": [{"step": 1, "title": "Scan", "description": "Continuous scanning across networks, endpoints, and cloud environments."},{"step": 2, "title": "Prioritize", "description": "AI risk-scores vulnerabilities based on exploitability, exposure, and business impact."},{"step": 3, "title": "Plan", "description": "Automated remediation plans generated with change management integration."},{"step": 4, "title": "Remediate", "description": "Patches and fixes deployed through automated workflows."},{"step": 5, "title": "Verify", "description": "Post-remediation scans confirm vulnerabilities are resolved."}],
             "ai_capabilities": ["Risk-based prioritization", "Contextual CVSS scoring", "Automated remediation planning", "Cross-client trend analysis"],
             "hitl_checkpoints": ["Approve remediation plans for critical systems", "Review risk exceptions", "Validate scan results"],
             "key_metrics": ["Critical vulnerability remediation <72 hours", "Scan coverage >99%", "Risk-based prioritization accuracy >90%"],
             "connected_pas": [{"name": "Attack Surface Management", "slug": "attack-surface-management", "zone_slug": "security-operations"},{"name": "Automated Patching", "slug": "automated-patching", "zone_slug": "endpoint-management"}],
             "related_roles": ["Security Analyst", "Network Engineer"], "related_role_slugs": ["security-analyst", "network-engineer"]},
            {"name": "EDR/XDR Integration", "slug": "edr-xdr-integration", "description": "Unified endpoint and extended detection and response management",
             "overview": "EDR/XDR Integration unifies endpoint detection and response with extended detection across network, email, identity, and cloud — providing a single view of threats across your clients' entire attack surface.\n\nThe platform ingests telemetry from leading EDR/XDR solutions, normalizing alerts and correlating events across data sources to surface the full kill chain of an attack. AI reduces alert fatigue by clustering related alerts into incidents, scoring severity, and filtering false positives.\n\nResponse actions are orchestrated directly through EDR APIs — isolating endpoints, killing processes, quarantining files — all from the DevOps AI platform without switching between vendor consoles.",
             "how_it_works": [{"step": 1, "title": "Ingest", "description": "Telemetry from EDR/XDR platforms is collected and normalized into a unified data model."},{"step": 2, "title": "Correlate", "description": "AI correlates alerts across endpoints, network, identity, and cloud sources."},{"step": 3, "title": "Triage", "description": "Alert clustering and severity scoring reduces noise and highlights true threats."},{"step": 4, "title": "Respond", "description": "Response actions executed through native EDR APIs for immediate containment."}],
             "ai_capabilities": ["Multi-source correlation", "Alert clustering", "False positive filtering", "Cross-platform response orchestration"],
             "hitl_checkpoints": ["Review correlated incident summaries", "Approve endpoint isolation actions", "Validate false positive classifications"],
             "key_metrics": ["Alert-to-incident ratio >20:1", "False positive reduction >80%", "Mean time to respond <10 minutes"],
             "connected_pas": [{"name": "Incident Response Orchestration", "slug": "incident-response-orchestration", "zone_slug": "security-operations"},{"name": "Detection Engineering", "slug": "detection-engineering", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "IT Director"], "related_role_slugs": ["security-analyst", "it-director"]},
            {"name": "Zero-Knowledge Vault (ZK-Vault)", "slug": "zero-knowledge-vault-zk-vault", "description": "Client-controlled encryption with zero-knowledge architecture for sensitive data",
             "overview": "The Zero-Knowledge Vault (ZK-Vault) ensures that sensitive client data remains encrypted and inaccessible to anyone — including RainTech — without the client's explicit authorization. Using a zero-knowledge encryption architecture, clients maintain sole ownership of their encryption keys.\n\nAll sensitive data stored in the platform (credentials, secrets, PII, compliance evidence) is encrypted client-side before it ever reaches the server. The ZK-Vault provides secure storage, key rotation, and access audit trails without ever exposing plaintext data to the platform operators.\n\nThis architecture is fundamental to the trust model that makes multi-tenant MSP operations viable — each client's data is cryptographically isolated, even from the MSP managing their environment.",
             "how_it_works": [{"step": 1, "title": "Encrypt", "description": "Data is encrypted client-side using keys that never leave the client's control."},{"step": 2, "title": "Store", "description": "Encrypted data is stored in isolated, zero-knowledge containers."},{"step": 3, "title": "Access", "description": "Authorized access requires client key presentation; no server-side decryption possible."},{"step": 4, "title": "Audit", "description": "Every access attempt is logged with full audit trail for compliance."}],
             "ai_capabilities": ["Key rotation scheduling", "Access anomaly detection", "Compliance evidence generation", "Multi-tenant isolation verification"],
             "hitl_checkpoints": ["Client approval for key rotation", "Review access anomaly alerts", "Compliance audit sign-off"],
             "key_metrics": ["Encryption coverage 100%", "Key rotation compliance >99%", "Zero unauthorized access incidents"],
             "connected_pas": [{"name": "Privileged Access Management (PAM)", "slug": "privileged-access-management-pam", "zone_slug": "security-operations"},{"name": "Data Privacy Management", "slug": "data-privacy-management", "zone_slug": "legal"}],
             "related_roles": ["vCISO", "Compliance Officer"], "related_role_slugs": ["vciso", "compliance-officer"]},
            {"name": "Privileged Access Management (PAM)", "slug": "privileged-access-management-pam", "description": "Secure management of privileged accounts with just-in-time access",
             "overview": "Privileged Access Management (PAM) controls and audits access to critical systems and sensitive operations. In MSP environments where technicians access hundreds of client environments, PAM ensures that elevated privileges are granted only when needed, for only as long as needed.\n\nJust-in-time (JIT) access provisioning replaces standing privileged accounts. Technicians request elevated access for specific tasks, and the system grants time-limited credentials that automatically expire. All privileged sessions are recorded for audit and compliance purposes.\n\nThe AI monitors privileged access patterns to detect anomalies — such as unusual access times, unfamiliar systems, or privilege escalation attempts — providing an additional layer of security.",
             "how_it_works": [{"step": 1, "title": "Request", "description": "Technician requests elevated access for a specific system and task."},{"step": 2, "title": "Approve", "description": "Automated or manager approval based on request risk score and policy."},{"step": 3, "title": "Provision", "description": "Time-limited credentials are issued via secure vault with session recording enabled."},{"step": 4, "title": "Monitor", "description": "AI monitors the privileged session for anomalous behavior."},{"step": 5, "title": "Revoke", "description": "Access automatically expires; credentials are rotated post-session."}],
             "ai_capabilities": ["Risk-based access decisions", "Session anomaly detection", "Automated credential rotation", "Usage pattern analysis"],
             "hitl_checkpoints": ["Approve high-risk access requests", "Review session recordings", "Investigate anomaly alerts"],
             "key_metrics": ["Standing privilege reduction >90%", "JIT access grant time <5 minutes", "Session recording coverage 100%"],
             "connected_pas": [{"name": "Zero-Knowledge Vault (ZK-Vault)", "slug": "zero-knowledge-vault-zk-vault", "zone_slug": "security-operations"},{"name": "Access Lifecycle Management", "slug": "access-lifecycle-management", "zone_slug": "people"}],
             "related_roles": ["Security Analyst", "vCISO", "IT Director"], "related_role_slugs": ["security-analyst", "vciso", "it-director"]},
            {"name": "Attack Surface Management", "slug": "attack-surface-management", "description": "Continuous discovery and monitoring of external attack surface",
             "overview": "Attack Surface Management continuously discovers, inventories, and monitors all externally-facing assets across your clients' environments. Shadow IT, forgotten subdomains, exposed services, and misconfigured cloud resources are identified automatically.\n\nThe AI maps the complete external attack surface for each client, comparing it against known assets to identify unexpected exposures. Risk scoring considers each asset's vulnerability status, data sensitivity, and exposure level to prioritize remediation.\n\nContinuous monitoring ensures that new exposures are detected within hours of appearing — whether from a developer spinning up a cloud instance, a DNS change creating a new subdomain, or a firewall rule modification exposing a service.",
             "how_it_works": [{"step": 1, "title": "Discover", "description": "Automated scanning discovers all externally-facing assets, domains, and services."},{"step": 2, "title": "Inventory", "description": "Discovered assets are mapped against known asset inventories to identify shadow IT."},{"step": 3, "title": "Assess", "description": "Each asset is risk-scored based on vulnerabilities, exposure, and data sensitivity."},{"step": 4, "title": "Monitor", "description": "Continuous monitoring detects new exposures and configuration changes."}],
             "ai_capabilities": ["Shadow IT discovery", "Asset risk scoring", "Change detection", "Exposure correlation"],
             "hitl_checkpoints": ["Review newly discovered assets", "Approve remediation priorities", "Validate shadow IT findings"],
             "key_metrics": ["Asset discovery accuracy >95%", "Shadow IT detection rate >90%", "New exposure detection <4 hours"],
             "connected_pas": [{"name": "Vulnerability Scanning & Remediation", "slug": "vulnerability-scanning-remediation", "zone_slug": "security-operations"},{"name": "Security Observability", "slug": "security-observability", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "vCISO", "Network Engineer"], "related_role_slugs": ["security-analyst", "vciso", "network-engineer"]},
            {"name": "Dark Web Monitoring", "slug": "dark-web-monitoring", "description": "Proactive monitoring of dark web for client credential and data exposure",
             "overview": "Dark Web Monitoring continuously scans underground forums, paste sites, marketplaces, and breach databases for your clients' compromised credentials, leaked data, and brand mentions.\n\nWhen client email addresses, passwords, or sensitive data appear in breach dumps or dark web listings, the system generates immediate alerts with risk context. AI correlates findings with the client's identity infrastructure to identify which accounts are at risk and whether the compromised credentials are still in use.\n\nProactive monitoring enables your MSP to force password resets, enable additional authentication factors, and notify affected clients before attackers can weaponize stolen credentials.",
             "how_it_works": [{"step": 1, "title": "Scan", "description": "Continuous monitoring of dark web forums, paste sites, and breach databases."},{"step": 2, "title": "Match", "description": "AI matches exposed data against client domains, email addresses, and known assets."},{"step": 3, "title": "Assess", "description": "Risk assessment determines if compromised credentials are still active."},{"step": 4, "title": "Respond", "description": "Automated alerts trigger password resets and additional security measures."}],
             "ai_capabilities": ["Credential matching", "Risk assessment", "Active credential detection", "Automated response triggering"],
             "hitl_checkpoints": ["Review exposure reports", "Approve client notifications", "Validate credential status"],
             "key_metrics": ["Avg detection-to-alert time <30 minutes", "Active credential identification >95%", "Client notification within 1 hour"],
             "connected_pas": [{"name": "Threat Intelligence Feeds", "slug": "threat-intelligence-feeds", "zone_slug": "security-operations"},{"name": "Privileged Access Management (PAM)", "slug": "privileged-access-management-pam", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "vCISO"], "related_role_slugs": ["security-analyst", "vciso"]},
            {"name": "Security Observability", "slug": "security-observability", "description": "Unified security metrics, dashboards, and posture scoring",
             "overview": "Security Observability provides a unified view of security health across all client environments. The platform aggregates metrics from every security tool, process, and control into comprehensive dashboards that give vCISOs and security analysts instant visibility into posture.\n\nAI-driven security scoring combines vulnerability data, compliance status, threat exposure, incident history, and control effectiveness into a single, actionable score for each client. Trend analysis reveals whether security posture is improving or degrading over time.\n\nExecutive-ready reporting translates technical security metrics into business language, making it easy for MSP leaders to communicate security value to clients during QBRs.",
             "how_it_works": [{"step": 1, "title": "Collect", "description": "Security metrics aggregated from all tools, controls, and processes."},{"step": 2, "title": "Score", "description": "AI computes composite security scores per client considering multiple dimensions."},{"step": 3, "title": "Visualize", "description": "Dashboards present security posture at summary and detail levels."},{"step": 4, "title": "Report", "description": "Executive reports generated for QBRs and board presentations."}],
             "ai_capabilities": ["Composite security scoring", "Trend analysis", "Anomaly detection", "Executive report generation"],
             "hitl_checkpoints": ["Review security score methodology", "Validate posture assessments", "Approve client-facing reports"],
             "key_metrics": ["Dashboard refresh latency <5 minutes", "Score accuracy validated quarterly", "Report generation time <10 minutes"],
             "connected_pas": [{"name": "Attack Surface Management", "slug": "attack-surface-management", "zone_slug": "security-operations"},{"name": "BCDR Planning & Testing", "slug": "bcdr-planning-testing", "zone_slug": "security-operations"}],
             "related_roles": ["vCISO", "Security Analyst", "IT Director"], "related_role_slugs": ["vciso", "security-analyst", "it-director"]},
            {"name": "Adversary Emulation", "slug": "adversary-emulation", "description": "Automated red team exercises simulating real-world attack techniques",
             "overview": "Adversary Emulation runs automated security testing that simulates real-world attack techniques mapped to the MITRE ATT&CK framework. Rather than waiting for annual penetration tests, this capability enables continuous validation of your clients' security controls.\n\nThe AI selects and executes attack simulations relevant to each client's threat profile, testing detection rules, response procedures, and security control effectiveness. Results identify gaps before real attackers can exploit them.\n\nAll emulation activities are safe, controlled, and fully auditable — designed to test without disrupting production systems.",
             "how_it_works": [{"step": 1, "title": "Plan", "description": "AI selects attack scenarios based on client threat profile and ATT&CK coverage gaps."},{"step": 2, "title": "Execute", "description": "Safe, controlled attack simulations run against client environments."},{"step": 3, "title": "Evaluate", "description": "Detection and response effectiveness measured against each simulated technique."},{"step": 4, "title": "Improve", "description": "Gaps feed into detection engineering and security control improvement plans."}],
             "ai_capabilities": ["ATT&CK-based scenario selection", "Safe execution controls", "Detection gap identification", "Control effectiveness scoring"],
             "hitl_checkpoints": ["Approve emulation scope", "Review findings and recommendations", "Schedule emulation windows"],
             "key_metrics": ["ATT&CK coverage tested >70%", "Detection gap identification rate >90%", "Zero production disruptions"],
             "connected_pas": [{"name": "Detection Engineering", "slug": "detection-engineering", "zone_slug": "security-operations"},{"name": "Security Observability", "slug": "security-observability", "zone_slug": "security-operations"}],
             "related_roles": ["Security Analyst", "vCISO"], "related_role_slugs": ["security-analyst", "vciso"]},
            {"name": "Supply Chain Security", "slug": "supply-chain-security", "description": "Monitoring and securing software supply chain dependencies",
             "overview": "Supply Chain Security monitors the software and vendor dependencies across your clients' environments for security risks. With supply chain attacks becoming increasingly common, visibility into third-party risk is essential.\n\nThe platform maintains a Software Bill of Materials (SBOM) for client environments, tracking dependencies, versions, and known vulnerabilities. AI monitors for newly disclosed supply chain compromises and assesses exposure across your client base.\n\nVendor security assessments are automated and continuous, tracking each vendor's security posture and alerting when changes introduce new risk to your clients' environments.",
             "how_it_works": [{"step": 1, "title": "Inventory", "description": "Automated SBOM generation across client environments and software stacks."},{"step": 2, "title": "Monitor", "description": "Continuous monitoring for newly disclosed supply chain compromises."},{"step": 3, "title": "Assess", "description": "AI assesses exposure impact across your client base for each supply chain event."},{"step": 4, "title": "Mitigate", "description": "Remediation guidance and automated blocking for compromised components."}],
             "ai_capabilities": ["SBOM management", "Supply chain risk scoring", "Cross-client exposure analysis", "Automated component blocking"],
             "hitl_checkpoints": ["Review supply chain risk assessments", "Approve component blocking", "Validate SBOM accuracy"],
             "key_metrics": ["SBOM coverage >95%", "Supply chain alert response <2 hours", "Known vulnerable component coverage 100%"],
             "connected_pas": [{"name": "Vulnerability Scanning & Remediation", "slug": "vulnerability-scanning-remediation", "zone_slug": "security-operations"},{"name": "Third-Party Risk Management", "slug": "third-party-risk-management", "zone_slug": "grc-compliance"}],
             "related_roles": ["Security Analyst", "vCISO", "Compliance Officer"], "related_role_slugs": ["security-analyst", "vciso", "compliance-officer"]},
            {"name": "BCDR Planning & Testing", "slug": "bcdr-planning-testing", "description": "Business continuity and disaster recovery planning with automated testing",
             "overview": "BCDR Planning & Testing ensures your clients can recover from disasters, outages, and major incidents. The platform manages continuity plans, recovery procedures, and automated testing schedules for each client environment.\n\nAI assists in building and maintaining BCDR plans by analyzing infrastructure dependencies, identifying single points of failure, and suggesting recovery strategies. Automated DR testing validates that backups are restorable and recovery time objectives (RTOs) are achievable.\n\nPost-test analysis compares actual recovery metrics against targets, identifying gaps that need attention before a real disaster strikes.",
             "how_it_works": [{"step": 1, "title": "Plan", "description": "AI analyzes infrastructure to build comprehensive BCDR plans with dependency mapping."},{"step": 2, "title": "Document", "description": "Recovery procedures documented with step-by-step runbooks for each scenario."},{"step": 3, "title": "Test", "description": "Automated DR testing validates backup integrity and recovery procedures."},{"step": 4, "title": "Analyze", "description": "Post-test analysis compares actual RTO/RPO against targets."},{"step": 5, "title": "Improve", "description": "Gap analysis feeds plan updates and infrastructure improvement recommendations."}],
             "ai_capabilities": ["Dependency mapping", "Recovery strategy optimization", "Automated DR testing", "RTO/RPO gap analysis"],
             "hitl_checkpoints": ["Approve BCDR plans", "Schedule and oversee DR tests", "Review test results and gap analysis"],
             "key_metrics": ["DR test pass rate >95%", "RTO achievement >99%", "Plan currency <90 days since last update"],
             "connected_pas": [{"name": "Security Observability", "slug": "security-observability", "zone_slug": "security-operations"},{"name": "Infrastructure Monitoring", "slug": "infrastructure-monitoring", "zone_slug": "endpoint-management"}],
             "related_roles": ["IT Director", "vCISO"], "related_role_slugs": ["it-director", "vciso"]}
        ]
    },
    {
        "name": "GRC & Compliance",
        "slug": "grc-compliance",
        "cluster": "Service & Security",
        "tagline": "Continuous Compliance Automation",
        "icon": "📋",
        "process_areas": [
            {"name": "Policy Management", "slug": "policy-management", "description": "Automated policy creation, versioning, and distribution across client environments",
             "overview": "Policy Management automates the creation, maintenance, and distribution of security and compliance policies across your MSP's client base. AI-generated policy templates are customized to each client's regulatory requirements, industry, and risk profile.\n\nVersion control ensures policy changes are tracked with full audit trails. When regulations change, the AI identifies which policies need updating and suggests specific revisions, dramatically reducing the manual effort of policy maintenance.\n\nAutomated distribution and acknowledgment tracking ensures all employees receive the right policies and confirms their acceptance — a critical compliance requirement.",
             "how_it_works": [{"step": 1, "title": "Generate", "description": "AI creates policy drafts based on regulatory requirements and industry best practices."},{"step": 2, "title": "Customize", "description": "Policies tailored to each client's specific environment and risk profile."},{"step": 3, "title": "Distribute", "description": "Automated distribution with tracking for employee acknowledgment."},{"step": 4, "title": "Maintain", "description": "AI monitors for regulatory changes and suggests policy updates."}],
             "ai_capabilities": ["Policy template generation", "Regulatory change detection", "Gap analysis", "Acknowledgment tracking"],
             "hitl_checkpoints": ["Approve policy content", "Review AI-suggested updates", "Client sign-off on policies"],
             "key_metrics": ["Policy currency >95%", "Employee acknowledgment rate >98%", "Avg policy update time <48 hours"],
             "connected_pas": [{"name": "Framework Lifecycle Management", "slug": "framework-lifecycle-management", "zone_slug": "grc-compliance"},{"name": "Gap Analysis Engine", "slug": "gap-analysis-engine", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "Risk Management", "slug": "risk-management", "description": "AI-assisted risk identification, assessment, and mitigation tracking",
             "overview": "Risk Management provides a structured, AI-assisted approach to identifying, assessing, and mitigating risks across your clients' environments. The platform maintains a dynamic risk register that evolves as threats change and controls are implemented.\n\nAI continuously scans for new risk factors — from emerging threats and vulnerability disclosures to regulatory changes and business process modifications. Each risk is scored using a quantitative model that considers likelihood, impact, and control effectiveness.\n\nMitigation tracking ensures that risk treatment plans are executed on schedule, with automated alerts for overdue actions and trend analysis showing whether overall risk posture is improving.",
             "how_it_works": [{"step": 1, "title": "Identify", "description": "AI scans for new risks from threats, vulnerabilities, regulatory changes, and business processes."},{"step": 2, "title": "Assess", "description": "Quantitative risk scoring considering likelihood, impact, and existing controls."},{"step": 3, "title": "Treat", "description": "Mitigation plans created with assigned owners, timelines, and success criteria."},{"step": 4, "title": "Monitor", "description": "Continuous risk monitoring with automated alerts for changes and overdue mitigations."}],
             "ai_capabilities": ["Automated risk identification", "Quantitative risk scoring", "Control effectiveness analysis", "Trend prediction"],
             "hitl_checkpoints": ["Validate risk assessments", "Approve mitigation plans", "Review risk acceptance decisions"],
             "key_metrics": ["Risk register currency <30 days", "Mitigation plan completion rate >90%", "Risk score accuracy validated quarterly"],
             "connected_pas": [{"name": "Gap Analysis Engine", "slug": "gap-analysis-engine", "zone_slug": "grc-compliance"},{"name": "Third-Party Risk Management", "slug": "third-party-risk-management", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO", "IT Director"], "related_role_slugs": ["compliance-officer", "vciso", "it-director"]},
            {"name": "CMMC SSP Builder", "slug": "cmmc-ssp-builder", "description": "Automated System Security Plan generation for CMMC compliance",
             "overview": "The CMMC SSP Builder automates the creation and maintenance of System Security Plans required for CMMC (Cybersecurity Maturity Model Certification) compliance. AI maps your client's current security controls to CMMC practices and generates SSP documentation that meets assessment requirements.\n\nThe system continuously monitors control implementation status, automatically updating the SSP when changes are detected. Gap analysis identifies practices that are not yet fully implemented, with remediation guidance to close each gap.\n\nFor MSPs serving defense industrial base (DIB) clients, this dramatically reduces the manual documentation burden while improving accuracy and audit readiness.",
             "how_it_works": [{"step": 1, "title": "Map", "description": "AI maps existing security controls to CMMC practices and maturity levels."},{"step": 2, "title": "Generate", "description": "SSP documentation auto-generated with control descriptions, boundaries, and data flows."},{"step": 3, "title": "Gap Identify", "description": "Missing or incomplete practices flagged with remediation guidance."},{"step": 4, "title": "Maintain", "description": "SSP automatically updated as controls change; version history maintained."}],
             "ai_capabilities": ["Control-to-practice mapping", "SSP auto-generation", "Gap identification", "Continuous SSP maintenance"],
             "hitl_checkpoints": ["Review SSP content", "Approve gap remediation plans", "C3PAO assessment preparation"],
             "key_metrics": ["CMMC practice coverage >95%", "SSP generation time <2 hours", "Gap remediation tracking >90%"],
             "connected_pas": [{"name": "C3PAO Readiness Assessment", "slug": "c3pao-readiness-assessment", "zone_slug": "grc-compliance"},{"name": "OSCAL-Native Evidence", "slug": "oscal-native-evidence", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "C3PAO Readiness Assessment", "slug": "c3pao-readiness-assessment", "description": "Pre-assessment readiness evaluation for CMMC third-party assessments",
             "overview": "C3PAO Readiness Assessment prepares your clients for their CMMC third-party assessment by simulating the evaluation process. AI conducts a comprehensive readiness review, identifying gaps and weaknesses that would be flagged by a C3PAO assessor.\n\nThe system evaluates evidence quality, control implementation completeness, documentation accuracy, and interview readiness across all applicable CMMC practices. A detailed readiness score helps you prioritize remediation efforts before the actual assessment.\n\nMock assessment reports mirror the format and rigor of actual C3PAO reports, ensuring your team and clients know exactly what to expect and how to prepare.",
             "how_it_works": [{"step": 1, "title": "Evaluate", "description": "AI simulates C3PAO assessment methodology across all applicable practices."},{"step": 2, "title": "Score", "description": "Practice-by-practice readiness scoring with evidence quality assessment."},{"step": 3, "title": "Report", "description": "Mock assessment report generated with findings and remediation priorities."},{"step": 4, "title": "Prepare", "description": "Interview preparation guides and evidence packaging for assessment day."}],
             "ai_capabilities": ["Assessment simulation", "Evidence quality scoring", "Readiness prediction", "Mock report generation"],
             "hitl_checkpoints": ["Review readiness scores", "Approve remediation priorities", "Final assessment go/no-go decision"],
             "key_metrics": ["Readiness prediction accuracy >90%", "First-attempt pass rate >85%", "Assessment prep time reduction >50%"],
             "connected_pas": [{"name": "CMMC SSP Builder", "slug": "cmmc-ssp-builder", "zone_slug": "grc-compliance"},{"name": "Self-Assessment Portal", "slug": "self-assessment-portal", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "Gap Analysis Engine", "slug": "gap-analysis-engine", "description": "Automated compliance gap identification across multiple frameworks",
             "overview": "The Gap Analysis Engine continuously evaluates your clients' compliance posture against multiple regulatory frameworks simultaneously. Whether it's CMMC, SOC 2, HIPAA, ISO 27001, or NIST CSF, the AI identifies where controls fall short of requirements.\n\nCross-framework mapping means a single control implementation can satisfy requirements across multiple frameworks, reducing duplicate effort. The AI prioritizes gaps by risk impact and remediation effort, giving your team a clear roadmap to compliance.\n\nAutomated re-assessment after remediation confirms that gaps are closed, maintaining an always-current compliance posture view.",
             "how_it_works": [{"step": 1, "title": "Map", "description": "Controls mapped against all applicable framework requirements simultaneously."},{"step": 2, "title": "Assess", "description": "AI evaluates implementation status and evidence sufficiency for each control."},{"step": 3, "title": "Prioritize", "description": "Gaps ranked by risk impact, remediation effort, and cross-framework benefit."},{"step": 4, "title": "Track", "description": "Remediation progress tracked with automated re-assessment upon completion."}],
             "ai_capabilities": ["Multi-framework mapping", "Control adequacy assessment", "Remediation prioritization", "Cross-framework deduplication"],
             "hitl_checkpoints": ["Validate gap assessments", "Approve remediation priorities", "Review cross-framework mapping"],
             "key_metrics": ["Framework coverage >95%", "Gap identification accuracy >90%", "Cross-framework mapping savings >40%"],
             "connected_pas": [{"name": "Policy Management", "slug": "policy-management", "zone_slug": "grc-compliance"},{"name": "Risk Management", "slug": "risk-management", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "OSCAL-Native Evidence", "slug": "oscal-native-evidence", "description": "Evidence collection and packaging in OSCAL format for automated compliance",
             "overview": "OSCAL-Native Evidence automates the collection, formatting, and packaging of compliance evidence in the Open Security Controls Assessment Language (OSCAL) format. This machine-readable standard enables automated assessment and continuous monitoring of compliance posture.\n\nThe system collects evidence from across your client's environment — configuration snapshots, log samples, policy documents, access records — and packages them in OSCAL format with proper control mappings and timestamps.\n\nNative OSCAL support means your evidence is ready for automated assessment tools, reducing the manual effort of evidence preparation and enabling continuous compliance monitoring rather than point-in-time assessments.",
             "how_it_works": [{"step": 1, "title": "Collect", "description": "Automated evidence collection from systems, logs, configurations, and documentation."},{"step": 2, "title": "Format", "description": "Evidence converted to OSCAL format with proper control mappings."},{"step": 3, "title": "Validate", "description": "AI validates evidence completeness and format compliance."},{"step": 4, "title": "Package", "description": "Evidence packaged for assessment submission with full audit trail."}],
             "ai_capabilities": ["Automated evidence collection", "OSCAL formatting", "Completeness validation", "Continuous monitoring"],
             "hitl_checkpoints": ["Review evidence packages", "Validate control mappings", "Approve assessment submissions"],
             "key_metrics": ["Evidence collection automation >80%", "OSCAL format compliance 100%", "Evidence preparation time reduction >60%"],
             "connected_pas": [{"name": "CMMC SSP Builder", "slug": "cmmc-ssp-builder", "zone_slug": "grc-compliance"},{"name": "Audit Management", "slug": "audit-management", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "Audit Management", "slug": "audit-management", "description": "End-to-end audit lifecycle management with AI-assisted preparation",
             "overview": "Audit Management streamlines the entire audit lifecycle — from preparation through evidence gathering, auditor interaction, finding remediation, and follow-up. AI reduces the burden on your team by automating evidence preparation and pre-audit self-assessments.\n\nThe system tracks audit schedules across all clients, ensuring nothing is missed. When an audit approaches, automated preparation workflows collect evidence, generate documentation, and identify potential findings before auditors arrive.\n\nPost-audit, finding remediation is tracked with deadlines and progress monitoring, ensuring all corrective actions are completed on time.",
             "how_it_works": [{"step": 1, "title": "Schedule", "description": "Audit calendar management with automated preparation triggers."},{"step": 2, "title": "Prepare", "description": "AI collects evidence, generates documentation, and runs pre-audit self-assessment."},{"step": 3, "title": "Execute", "description": "Auditor portal provides organized evidence with document request tracking."},{"step": 4, "title": "Remediate", "description": "Findings tracked through remediation with deadline monitoring and verification."}],
             "ai_capabilities": ["Pre-audit self-assessment", "Evidence organization", "Finding prediction", "Remediation tracking"],
             "hitl_checkpoints": ["Approve audit preparation packages", "Review pre-audit findings", "Sign off on remediation completeness"],
             "key_metrics": ["Audit preparation time reduction >50%", "Pre-audit finding detection >80%", "Remediation completion rate >95%"],
             "connected_pas": [{"name": "OSCAL-Native Evidence", "slug": "oscal-native-evidence", "zone_slug": "grc-compliance"},{"name": "Continuous Monitoring", "slug": "continuous-monitoring", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "Continuous Monitoring", "slug": "continuous-monitoring", "description": "Real-time compliance status monitoring across all frameworks and controls",
             "overview": "Continuous Monitoring replaces point-in-time compliance assessments with real-time visibility into control effectiveness. The system continuously evaluates security controls, configuration compliance, and policy adherence across all client environments.\n\nWhen a control drifts from its compliant state — whether from a configuration change, policy violation, or infrastructure modification — the system detects it immediately and generates alerts with remediation guidance.\n\nDashboards show compliance status at a glance, with drill-down capability to investigate specific controls, frameworks, or client environments. Trend analysis reveals whether compliance posture is improving or degrading over time.",
             "how_it_works": [{"step": 1, "title": "Monitor", "description": "Continuous evaluation of control implementation and configuration compliance."},{"step": 2, "title": "Detect", "description": "Drift detection identifies controls that have moved from compliant to non-compliant state."},{"step": 3, "title": "Alert", "description": "Real-time alerts with context and remediation guidance for compliance drift."},{"step": 4, "title": "Report", "description": "Dashboards and reports show compliance status trends across all frameworks."}],
             "ai_capabilities": ["Real-time control evaluation", "Drift detection", "Trend analysis", "Automated remediation suggestions"],
             "hitl_checkpoints": ["Review compliance drift alerts", "Approve remediation actions", "Validate control assessment accuracy"],
             "key_metrics": ["Control monitoring coverage >99%", "Drift detection time <1 hour", "Compliance dashboard accuracy >98%"],
             "connected_pas": [{"name": "Audit Management", "slug": "audit-management", "zone_slug": "grc-compliance"},{"name": "Gap Analysis Engine", "slug": "gap-analysis-engine", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO", "Security Analyst"], "related_role_slugs": ["compliance-officer", "vciso", "security-analyst"]},
            {"name": "Self-Assessment Portal", "slug": "self-assessment-portal", "description": "Client-facing self-assessment tool for compliance readiness evaluation",
             "overview": "The Self-Assessment Portal empowers clients to evaluate their own compliance readiness before formal assessments. Guided questionnaires walk through framework requirements in plain language, helping clients understand their obligations and current gaps.\n\nAI-powered scoring provides an immediate readiness estimate, highlighting areas that need attention. The portal generates action plans with prioritized remediation steps that your MSP team can help implement.\n\nFor MSPs, this tool serves dual purposes: educating clients about compliance requirements and generating qualified leads for compliance services by identifying clients who need the most help.",
             "how_it_works": [{"step": 1, "title": "Assess", "description": "Clients complete guided questionnaires mapped to their applicable frameworks."},{"step": 2, "title": "Score", "description": "AI generates readiness scores with detailed gap analysis."},{"step": 3, "title": "Plan", "description": "Automated action plans created with prioritized remediation steps."},{"step": 4, "title": "Connect", "description": "Results shared with MSP team for follow-up and service recommendations."}],
             "ai_capabilities": ["Guided assessment flow", "Readiness scoring", "Action plan generation", "Service opportunity identification"],
             "hitl_checkpoints": ["Review assessment results", "Customize remediation plans", "Follow up on identified opportunities"],
             "key_metrics": ["Assessment completion rate >70%", "Service conversion rate >30%", "Client satisfaction with portal >4.2/5.0"],
             "connected_pas": [{"name": "C3PAO Readiness Assessment", "slug": "c3pao-readiness-assessment", "zone_slug": "grc-compliance"},{"name": "Framework Lifecycle Management", "slug": "framework-lifecycle-management", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "Client Success Manager"], "related_role_slugs": ["compliance-officer", "client-success-manager"]},
            {"name": "Framework Lifecycle Management", "slug": "framework-lifecycle-management", "description": "Managing compliance framework versions, updates, and cross-mapping",
             "overview": "Framework Lifecycle Management tracks the evolution of compliance frameworks (CMMC, SOC 2, HIPAA, NIST CSF, ISO 27001, etc.) and manages the impact of framework updates on your clients' compliance programs.\n\nWhen a framework publishes a new version or revision, the AI analyzes the changes, identifies new requirements, and maps them against existing controls. This proactive approach ensures your clients are prepared for framework changes before compliance deadlines.\n\nCross-framework mapping maintains relationships between equivalent controls across different frameworks, maximizing the value of each control implementation.",
             "how_it_works": [{"step": 1, "title": "Track", "description": "Monitor framework publishers for version updates, revisions, and guidance changes."},{"step": 2, "title": "Analyze", "description": "AI identifies new requirements and changes from previous versions."},{"step": 3, "title": "Map", "description": "Cross-framework control mapping updated with new requirements."},{"step": 4, "title": "Plan", "description": "Transition plans generated for clients affected by framework changes."}],
             "ai_capabilities": ["Framework change detection", "Version comparison analysis", "Cross-framework mapping", "Transition planning"],
             "hitl_checkpoints": ["Review framework change impact", "Approve transition plans", "Validate cross-framework mappings"],
             "key_metrics": ["Framework update detection <48 hours", "Cross-mapping accuracy >95%", "Transition plan generation <1 week"],
             "connected_pas": [{"name": "Policy Management", "slug": "policy-management", "zone_slug": "grc-compliance"},{"name": "Self-Assessment Portal", "slug": "self-assessment-portal", "zone_slug": "grc-compliance"}],
             "related_roles": ["Compliance Officer", "vCISO"], "related_role_slugs": ["compliance-officer", "vciso"]},
            {"name": "Third-Party Risk Management", "slug": "third-party-risk-management", "description": "Continuous vendor and third-party risk assessment and monitoring",
             "overview": "Third-Party Risk Management automates the assessment and continuous monitoring of vendors, suppliers, and partners that interact with your clients' data and systems. AI streamlines vendor questionnaires, analyzes security postures, and tracks risk over time.\n\nAutomated vendor assessments pull data from public sources, security ratings services, and completed questionnaires to generate comprehensive risk profiles. The AI identifies vendors posing the highest risk and suggests mitigation measures.\n\nContinuous monitoring ensures vendor risk doesn't drift between assessment cycles — security incidents, data breaches, or financial instability at vendor companies trigger immediate re-assessment alerts.",
             "how_it_works": [{"step": 1, "title": "Assess", "description": "Automated vendor risk assessment using questionnaires, public data, and security ratings."},{"step": 2, "title": "Score", "description": "AI generates risk scores considering security posture, data access, and criticality."},{"step": 3, "title": "Monitor", "description": "Continuous monitoring for vendor security incidents, breaches, and financial changes."},{"step": 4, "title": "Mitigate", "description": "Risk mitigation recommendations with contract clause suggestions."}],
             "ai_capabilities": ["Automated vendor assessment", "Risk scoring", "Continuous monitoring", "Mitigation recommendations"],
             "hitl_checkpoints": ["Review vendor risk scores", "Approve vendor onboarding", "Validate monitoring alerts"],
             "key_metrics": ["Vendor assessment completion rate >90%", "Critical vendor monitoring coverage 100%", "Avg assessment time <5 days"],
             "connected_pas": [{"name": "Risk Management", "slug": "risk-management", "zone_slug": "grc-compliance"},{"name": "Supply Chain Security", "slug": "supply-chain-security", "zone_slug": "security-operations"}],
             "related_roles": ["Compliance Officer", "vCISO", "IT Director"], "related_role_slugs": ["compliance-officer", "vciso", "it-director"]}
        ]
    }
]

# Now add remaining zones with shorter but still meaningful content
# Helper to build a PA entry quickly
def pa(name, slug, desc, overview_text, steps, ai_caps, hitl, metrics, connected, roles, role_slugs):
    return {
        "name": name, "slug": slug, "description": desc,
        "overview": overview_text,
        "how_it_works": [{"step": i+1, "title": s[0], "description": s[1]} for i, s in enumerate(steps)],
        "ai_capabilities": ai_caps, "hitl_checkpoints": hitl, "key_metrics": metrics,
        "connected_pas": [{"name": c[0], "slug": c[1], "zone_slug": c[2]} for c in connected],
        "related_roles": roles, "related_role_slugs": role_slugs
    }

# Endpoint Management
ZONES.append({
    "name": "Endpoint Management", "slug": "endpoint-management", "cluster": "Operations",
    "tagline": "Intelligent Fleet Control", "icon": "💻",
    "process_areas": [
        pa("Automated Patching", "automated-patching", "AI-scheduled patch deployment with risk-based prioritization",
           "Automated Patching intelligently manages the deployment of operating system and application patches across your clients' endpoints. AI analyzes each patch for risk, compatibility, and urgency, then schedules deployment in ring-based waves that minimize disruption.\n\nThe system tests patches against representative environments before broad deployment, catching compatibility issues before they affect production. Rollback capabilities ensure quick recovery if a patch causes problems.\n\nCross-client intelligence means that if a patch causes issues in one client's environment, all other clients are automatically held until the issue is resolved.",
           [("Analyze", "AI assesses each patch for risk, compatibility, and urgency."), ("Schedule", "Ring-based deployment schedule created based on risk tolerance."), ("Deploy", "Patches deployed in waves with automated testing between rings."), ("Verify", "Post-deployment health checks confirm successful patching.")],
           ["Risk-based prioritization", "Compatibility prediction", "Cross-client issue detection", "Automated rollback"],
           ["Approve patch deployment schedule", "Review compatibility test results", "Authorize emergency patches"],
           ["Patch compliance >98%", "Mean time to patch critical vulnerabilities <72 hours", "Patch-related incidents <1%"],
           [("Ring-Based Patch Management", "ring-based-patch-management", "network-ops"), ("Vulnerability Management", "vulnerability-management", "endpoint-management")],
           ["Network Engineer", "IT Director"], ["network-engineer", "it-director"]),
        pa("Device Lifecycle Management", "device-lifecycle-management", "End-to-end device tracking from procurement to retirement",
           "Device Lifecycle Management tracks every endpoint from procurement through deployment, maintenance, and retirement. AI predicts optimal replacement timing based on performance degradation, warranty status, and total cost of ownership analysis.\n\nThe system maintains a comprehensive asset inventory with hardware specifications, software installations, warranty information, and health metrics. Automated alerts trigger when devices approach end-of-life, need warranty renewal, or show signs of imminent failure.\n\nDecommissioning workflows ensure secure data wiping and proper disposal tracking for compliance purposes.",
           [("Procure", "Track device acquisition with specs, warranty, and cost data."), ("Deploy", "Automated provisioning with standard images and configurations."), ("Maintain", "Health monitoring, warranty tracking, and refresh planning."), ("Retire", "Secure decommissioning with data wipe verification and disposal tracking.")],
           ["Failure prediction", "Replacement timing optimization", "TCO analysis", "Health trend analysis"],
           ["Approve procurement requests", "Authorize decommissioning", "Review refresh recommendations"],
           ["Asset inventory accuracy >99%", "Prediction accuracy for failures >85%", "Avg provisioning time <2 hours"],
           [("Fleet Intelligence", "fleet-intelligence", "endpoint-management"), ("Infrastructure Monitoring", "infrastructure-monitoring", "endpoint-management")],
           ["IT Director", "Network Engineer"], ["it-director", "network-engineer"]),
        pa("DNS Filtering", "dns-filtering", "AI-enhanced DNS security with real-time threat blocking",
           "DNS Filtering provides a critical layer of security by blocking access to malicious domains at the DNS level. AI continuously updates block lists based on threat intelligence, analyzing domain patterns and behavior to identify newly registered malicious domains before they're reported by traditional feeds.\n\nThe system enforces category-based filtering policies per client, enabling content restrictions for compliance or productivity purposes. Real-time analytics show browsing patterns and blocked threat attempts across all client environments.\n\nTenant-isolated policies ensure each client's filtering rules are independent while benefiting from cross-client threat intelligence.",
           [("Resolve", "DNS queries intercepted and analyzed in real time."), ("Classify", "AI classifies domains by category, reputation, and threat level."), ("Filter", "Malicious and policy-violating domains blocked with user notification."), ("Report", "Analytics on browsing patterns, threats blocked, and policy compliance.")],
           ["Domain reputation scoring", "New domain analysis", "Pattern-based threat detection", "Category classification"],
           ["Review blocked domain appeals", "Approve category policy changes", "Investigate suspicious patterns"],
           ["Threat block rate >99.5%", "DNS resolution latency <10ms", "Zero false positive blocks on business-critical domains"],
           [("Threat Intelligence Feeds", "threat-intelligence-feeds", "security-operations"), ("Fleet Intelligence", "fleet-intelligence", "endpoint-management")],
           ["Security Analyst", "Network Engineer"], ["security-analyst", "network-engineer"]),
        pa("Endpoint Telemetry & Analytics", "endpoint-telemetry-analytics", "Comprehensive endpoint health data collection and analysis",
           "Endpoint Telemetry & Analytics collects, processes, and analyzes health data from every managed endpoint. CPU utilization, memory usage, disk health, application performance, and network connectivity metrics flow into the platform continuously.\n\nAI detects anomalies in telemetry patterns that indicate emerging problems — a gradually filling disk, increasing memory consumption, or unusual CPU patterns that suggest malware. Early detection enables proactive remediation before users experience issues.\n\nCross-client analytics reveal common endpoint health patterns, helping your MSP optimize standard configurations and identify hardware models with above-average failure rates.",
           [("Collect", "Lightweight agents collect telemetry from all managed endpoints."), ("Process", "Data normalized and stored in per-client isolated storage."), ("Analyze", "AI detects anomalies, trends, and correlations across metrics."), ("Alert", "Proactive alerts generated for predicted issues before users are affected.")],
           ["Anomaly detection", "Trend prediction", "Cross-client pattern analysis", "Proactive alerting"],
           ["Review anomaly thresholds", "Investigate unusual patterns", "Validate alert accuracy"],
           ["Anomaly detection rate >90%", "Alert lead time >2 hours before user impact", "Telemetry coverage >99%"],
           [("Infrastructure Monitoring", "infrastructure-monitoring", "endpoint-management"), ("Fleet Intelligence", "fleet-intelligence", "endpoint-management")],
           ["IT Director", "Network Engineer"], ["it-director", "network-engineer"]),
        pa("Fleet Intelligence", "fleet-intelligence", "AI-driven insights across your entire endpoint fleet",
           "Fleet Intelligence provides strategic insights across your entire managed endpoint portfolio. AI analyzes fleet composition, health trends, standardization gaps, and cost optimization opportunities to guide fleet management decisions.\n\nThe system identifies hardware and software standardization opportunities that reduce management complexity. Cross-client benchmarking shows how each client's fleet compares to industry norms and your MSP's best practices.\n\nPredictive analytics forecast upcoming refresh needs, budget requirements, and potential risks from aging hardware — enabling proactive planning rather than reactive replacement.",
           [("Aggregate", "Fleet data collected across all clients and endpoint types."), ("Analyze", "AI identifies patterns, outliers, and optimization opportunities."), ("Benchmark", "Cross-client and industry benchmarking for fleet health."), ("Recommend", "Actionable recommendations for standardization, refresh, and cost optimization.")],
           ["Fleet composition analysis", "Standardization opportunity detection", "Refresh forecasting", "Cost optimization"],
           ["Review fleet recommendations", "Approve standardization initiatives", "Validate benchmark comparisons"],
           ["Fleet standardization improvement >20%", "Refresh forecast accuracy >90%", "Cost optimization savings >15%"],
           [("Device Lifecycle Management", "device-lifecycle-management", "endpoint-management"), ("Endpoint Telemetry & Analytics", "endpoint-telemetry-analytics", "endpoint-management")],
           ["IT Director", "Service Delivery Manager"], ["it-director", "service-delivery-manager"]),
        pa("Infrastructure Monitoring", "infrastructure-monitoring", "Real-time monitoring of servers, networks, and cloud infrastructure",
           "Infrastructure Monitoring provides 24/7 visibility into servers, network devices, cloud resources, and critical services across all client environments. AI-powered monitoring goes beyond simple up/down checks to detect performance degradation, capacity issues, and emerging problems.\n\nThe system correlates events across infrastructure layers to identify root causes quickly. When a network switch fails, the AI immediately maps the blast radius — identifying which servers, services, and users are affected.\n\nPredictive capabilities forecast capacity needs, identify potential failures from hardware degradation patterns, and suggest preventive actions before outages occur.",
           [("Monitor", "Continuous monitoring of all infrastructure components with customizable thresholds."), ("Correlate", "AI correlates events across layers to identify root causes."), ("Alert", "Intelligent alerting with noise reduction and severity scoring."), ("Predict", "Forecasting capacity needs and potential failures from trend data.")],
           ["Event correlation", "Noise reduction", "Capacity forecasting", "Predictive failure detection"],
           ["Review alert thresholds", "Approve capacity recommendations", "Validate monitoring coverage"],
           ["Monitoring coverage >99.9%", "Alert noise reduction >70%", "Capacity forecast accuracy >85%"],
           [("Endpoint Telemetry & Analytics", "endpoint-telemetry-analytics", "endpoint-management"), ("Performance Monitoring", "performance-monitoring", "network-ops")],
           ["IT Director", "Network Engineer"], ["it-director", "network-engineer"]),
        pa("Intune Management & Compliance", "intune-management-compliance", "Microsoft Intune integration for endpoint compliance and configuration",
           "Intune Management & Compliance provides deep integration with Microsoft Intune for endpoint configuration, compliance policy enforcement, and application deployment across your clients' Windows, macOS, iOS, and Android devices.\n\nThe AI monitors compliance status across all Intune-managed devices, detecting policy drift and configuration deviations in real time. When a device falls out of compliance, automated remediation workflows attempt to restore compliance before access is restricted.\n\nCross-client Intune policy management enables your MSP to maintain standardized security baselines while allowing per-client customization where needed.",
           [("Configure", "Standardized Intune policies deployed across client tenants."), ("Monitor", "Real-time compliance monitoring for all managed devices."), ("Remediate", "Automated remediation for compliance drift."), ("Report", "Compliance dashboards and reporting for each client.")],
           ["Compliance drift detection", "Automated remediation", "Policy optimization", "Cross-tenant management"],
           ["Approve policy changes", "Review compliance exceptions", "Validate remediation actions"],
           ["Device compliance rate >95%", "Policy drift detection <1 hour", "Remediation success rate >90%"],
           [("Automated Patching", "automated-patching", "endpoint-management"), ("Device Lifecycle Management", "device-lifecycle-management", "endpoint-management")],
           ["IT Director", "Security Analyst"], ["it-director", "security-analyst"]),
        pa("Remote Access & Support", "remote-access-support", "Secure remote access and support tools with session management",
           "Remote Access & Support provides secure, auditable remote access to client endpoints for troubleshooting and maintenance. The platform integrates with leading remote support tools while adding AI-powered session assistance and full audit logging.\n\nAI assists technicians during remote sessions by suggesting solutions based on observed symptoms, pulling relevant knowledge base articles, and pre-staging diagnostic tools. All sessions are recorded with full keystroke and screen capture for compliance and training purposes.\n\nClient consent management ensures end users are aware of and approve remote sessions, maintaining trust and regulatory compliance.",
           [("Connect", "Secure remote session initiated with client consent and MFA."), ("Assist", "AI provides real-time guidance and relevant knowledge base suggestions."), ("Resolve", "Technician resolves issue with full tool access and session recording."), ("Document", "Session automatically documented with resolution details and audit trail.")],
           ["Real-time resolution suggestions", "Session documentation", "Pattern recognition", "Knowledge base integration"],
           ["Client consent verification", "Review session recordings", "Approve unattended access policies"],
           ["Remote session resolution rate >85%", "Avg session duration <25 minutes", "Client consent compliance 100%"],
           [("Service Request Fulfillment", "service-request-fulfillment", "service-desk"), ("Known Error Database (KEDB)", "known-error-database-kedb", "service-desk")],
           ["Service Desk Manager", "Network Engineer"], ["service-desk-manager", "network-engineer"]),
        pa("Universal Agent Platform", "universal-agent-platform", "Unified endpoint agent with modular capabilities",
           "The Universal Agent Platform provides a single, lightweight agent that runs on all managed endpoints — replacing the need for multiple vendor-specific agents. Modular architecture enables capability addition without reinstalling or disrupting the endpoint.\n\nThe agent collects telemetry, enforces policies, executes remediation scripts, and provides the local execution layer for remote management. AI optimizes agent resource consumption based on endpoint specifications, ensuring minimal impact on system performance.\n\nCentralized management enables mass deployment, configuration updates, and health monitoring across all agents from a single console.",
           [("Deploy", "Lightweight agent installed via automated deployment methods."), ("Configure", "Modules activated based on client requirements and endpoint type."), ("Operate", "Agent executes monitoring, compliance, and remediation tasks locally."), ("Update", "Centralized updates pushed without endpoint disruption.")],
           ["Resource optimization", "Self-healing capabilities", "Module selection", "Performance impact minimization"],
           ["Approve module activations", "Review agent health reports", "Validate resource consumption"],
           ["Agent coverage >99%", "Resource overhead <3% CPU/RAM", "Update success rate >99.5%"],
           [("Endpoint Telemetry & Analytics", "endpoint-telemetry-analytics", "endpoint-management"), ("Automated Patching", "automated-patching", "endpoint-management")],
           ["IT Director", "DevOps Engineer"], ["it-director", "devops-engineer"]),
        pa("Vulnerability Management", "vulnerability-management", "Endpoint vulnerability discovery and remediation tracking",
           "Vulnerability Management provides continuous vulnerability discovery across all managed endpoints, identifying missing patches, misconfigurations, and software vulnerabilities. AI prioritizes vulnerabilities based on exploitability, exposure, and business impact specific to each client's environment.\n\nThe system integrates with patch management and configuration management to automate remediation of discovered vulnerabilities. Progress tracking ensures nothing falls through the cracks, with SLA-based remediation timelines and automated escalation for overdue items.\n\nExecutive dashboards show vulnerability posture trends over time, demonstrating the value of your MSP's security management to clients.",
           [("Discover", "Continuous vulnerability scanning across all endpoints."), ("Prioritize", "AI risk-scores each vulnerability based on context."), ("Remediate", "Automated remediation via patching and configuration management."), ("Track", "Progress monitoring with SLA timelines and escalation.")],
           ["Context-aware prioritization", "Automated remediation triggers", "Trend analysis", "Cross-client benchmarking"],
           ["Approve remediation priorities", "Review risk exceptions", "Validate scan coverage"],
           ["Vulnerability scan coverage >99%", "Critical vulnerability SLA compliance >95%", "Remediation automation rate >70%"],
           [("Automated Patching", "automated-patching", "endpoint-management"), ("Vulnerability Scanning & Remediation", "vulnerability-scanning-remediation", "security-operations")],
           ["Security Analyst", "IT Director"], ["security-analyst", "it-director"])
    ]
})

# Network Ops
ZONES.append({
    "name": "Network Ops", "slug": "network-ops", "cluster": "Operations",
    "tagline": "Predictive Network Intelligence", "icon": "🌐",
    "process_areas": [
        pa("Performance Monitoring", "performance-monitoring", "Real-time network performance monitoring with AI anomaly detection",
           "Performance Monitoring provides continuous visibility into network health across all client environments. AI-powered baseline analysis learns normal performance patterns for each network segment, enabling instant detection of anomalies that traditional threshold-based monitoring would miss.\n\nThe system monitors bandwidth utilization, latency, packet loss, jitter, and application performance in real time. When performance degrades, AI correlates metrics across multiple points to identify the root cause — whether it's a failing switch, congested link, or misconfigured QoS policy.\n\nPredictive analytics forecast when network capacity will be exhausted, enabling proactive upgrades before users experience degradation.",
           [("Monitor", "Continuous collection of network performance metrics across all segments."), ("Baseline", "AI learns normal patterns to establish dynamic baselines."), ("Detect", "Anomaly detection identifies deviations from expected behavior."), ("Diagnose", "Root cause analysis correlates metrics across the network path.")],
           ["Dynamic baselining", "Anomaly detection", "Root cause correlation", "Capacity forecasting"],
           ["Review anomaly alerts", "Approve capacity recommendations", "Validate baseline accuracy"],
           ["Network uptime >99.95%", "Mean time to detect issues <5 minutes", "Capacity forecast accuracy >90%"],
           [("Infrastructure Monitoring", "infrastructure-monitoring", "endpoint-management"), ("SLO Management", "slo-management", "network-ops")],
           ["Network Engineer", "IT Director"], ["network-engineer", "it-director"]),
        pa("Network Configuration Management", "network-configuration-management", "Centralized network device configuration with version control",
           "Network Configuration Management provides centralized control over network device configurations with full version history, compliance checking, and automated deployment capabilities. AI detects configuration drift and unauthorized changes across your clients' network infrastructure.\n\nThe system maintains golden configuration templates that enforce security and performance standards. When a device's configuration deviates from the approved baseline, alerts are generated with detailed change analysis. Automated rollback capabilities can restore compliant configurations instantly.\n\nBulk configuration changes are deployed safely using staged rollouts with automated health checks between stages.",
           [("Template", "Define golden configurations with security and performance standards."), ("Deploy", "Staged configuration deployment with health checks between rollouts."), ("Monitor", "Continuous compliance checking against approved baselines."), ("Rollback", "Automated rollback on detected issues or unauthorized changes.")],
           ["Configuration drift detection", "Template optimization", "Impact prediction", "Automated rollback"],
           ["Approve configuration templates", "Review drift alerts", "Authorize bulk changes"],
           ["Configuration compliance >98%", "Drift detection time <15 minutes", "Change success rate >99%"],
           [("Network Discovery & Automation", "network-discovery-automation", "network-ops"), ("Topology Visualization", "topology-visualization", "network-ops")],
           ["Network Engineer", "IT Director"], ["network-engineer", "it-director"]),
        pa("Network Discovery & Automation", "network-discovery-automation", "Automated network topology discovery and documentation",
           "Network Discovery & Automation continuously scans client networks to discover and document all connected devices, services, and their relationships. AI-powered discovery goes beyond basic ping sweeps to identify device types, firmware versions, open services, and network relationships.\n\nDiscovered topology is automatically documented and kept current — no more stale network diagrams or unknown devices. The system detects when new devices appear, existing devices change, or expected devices go missing.\n\nAutomation capabilities extend beyond discovery: common network operations like VLAN provisioning, ACL updates, and port configurations are automated through workflows that enforce change management policies.",
           [("Scan", "Automated network scanning discovers all connected devices and services."), ("Classify", "AI identifies device types, roles, and relationships."), ("Document", "Network topology automatically documented and kept current."), ("Automate", "Common network operations automated with change management compliance.")],
           ["Device classification", "Relationship mapping", "Change detection", "Workflow automation"],
           ["Review newly discovered devices", "Approve automated operations", "Validate topology accuracy"],
           ["Discovery accuracy >98%", "New device detection <1 hour", "Topology currency <24 hours"],
           [("Network Configuration Management", "network-configuration-management", "network-ops"), ("Topology Visualization", "topology-visualization", "network-ops")],
           ["Network Engineer", "IT Director"], ["network-engineer", "it-director"]),
        pa("Capacity Forecasting", "capacity-forecasting", "AI-driven network capacity planning and growth prediction",
           "Capacity Forecasting uses historical trends, growth patterns, and business context to predict when network infrastructure will need upgrades. AI models consider seasonal patterns, business growth projections, and upcoming projects that will increase network demand.\n\nThe system generates capacity reports for each client showing current utilization, projected growth, and recommended upgrade timelines. Budget estimates for capacity additions help clients plan infrastructure investments.\n\nProactive capacity management prevents the reactive firefighting that comes from running out of bandwidth, IP addresses, or port capacity.",
           [("Collect", "Historical utilization data collected across all network segments."), ("Model", "AI builds capacity models considering trends, growth, and seasonal patterns."), ("Forecast", "Projections generated for various growth scenarios."), ("Plan", "Upgrade recommendations with timelines and budget estimates.")],
           ["Trend modeling", "Growth projection", "Budget estimation", "Scenario planning"],
           ["Review capacity forecasts", "Approve upgrade recommendations", "Validate model accuracy"],
           ["Forecast accuracy >85%", "Upgrade lead time >90 days", "Budget variance <15%"],
           [("Performance Monitoring", "performance-monitoring", "network-ops"), ("SLO Management", "slo-management", "network-ops")],
           ["Network Engineer", "IT Director", "vCIO"], ["network-engineer", "it-director", "vcio"]),
        pa("Ring-Based Patch Management", "ring-based-patch-management", "Staged network device firmware updates with progressive rollout",
           "Ring-Based Patch Management applies the ring deployment methodology to network device firmware and configuration updates. Devices are organized into rings based on criticality and risk tolerance — updates flow through test, pilot, and production rings with automated validation between stages.\n\nThe AI monitors device health metrics at each ring stage, automatically pausing rollouts if issues are detected. This approach dramatically reduces the risk of network-wide outages from firmware bugs or compatibility issues.\n\nCross-client ring data means your MSP learns from every deployment — if a firmware update causes problems in one client's ring, all other clients' rollouts are automatically paused for review.",
           [("Classify", "Devices organized into deployment rings by criticality."), ("Test", "Updates deployed to test ring with comprehensive health monitoring."), ("Promote", "Successful updates promoted to next ring after validation."), ("Halt", "Automatic rollout pause if health metrics degrade at any ring.")],
           ["Health-aware promotion", "Cross-client issue detection", "Rollout impact prediction", "Automated halt logic"],
           ["Approve firmware updates", "Review ring promotion criteria", "Authorize emergency rollbacks"],
           ["Firmware compliance >97%", "Update-related incidents <0.5%", "Mean rollout time <72 hours"],
           [("Network Configuration Management", "network-configuration-management", "network-ops"), ("Automated Patching", "automated-patching", "endpoint-management")],
           ["Network Engineer", "IT Director"], ["network-engineer", "it-director"]),
        pa("SLO Management", "slo-management", "Service level objective definition, tracking, and reporting",
           "SLO Management provides a structured framework for defining, monitoring, and reporting on network service level objectives. AI-powered SLO tracking goes beyond simple threshold monitoring to include error budgets, burn rate alerts, and predictive SLO compliance.\n\nThe system helps define meaningful SLOs for each client based on their business requirements and historical performance. Error budget tracking shows how much room remains before an SLO is breached, enabling proactive action.\n\nSLO reports feed directly into QBR preparation, giving your service delivery team concrete data on network performance commitments.",
           [("Define", "Establish SLOs based on client requirements and historical baselines."), ("Track", "Real-time SLO tracking with error budget monitoring."), ("Alert", "Burn rate alerts when error budget consumption is too fast."), ("Report", "SLO compliance reports generated for QBRs and client reviews.")],
           ["Error budget calculation", "Burn rate alerting", "SLO compliance prediction", "Report generation"],
           ["Approve SLO definitions", "Review burn rate alerts", "Validate compliance calculations"],
           ["SLO compliance >99.5%", "Error budget visibility for all critical services", "Report accuracy >99%"],
           [("Performance Monitoring", "performance-monitoring", "network-ops"), ("Capacity Forecasting", "capacity-forecasting", "network-ops")],
           ["Network Engineer", "Service Delivery Manager"], ["network-engineer", "service-delivery-manager"]),
        pa("SSL Certificate Management", "ssl-certificate-management", "Automated SSL/TLS certificate lifecycle management",
           "SSL Certificate Management automates the discovery, monitoring, and renewal of SSL/TLS certificates across your clients' domains and services. AI-powered monitoring ensures no certificate expires unexpectedly — a common cause of service outages and security warnings.\n\nThe system discovers all certificates in use across client environments, including those on internal services that are often overlooked. Automated renewal workflows handle the entire certificate lifecycle, from CSR generation through deployment and verification.\n\nCertificate health dashboards show expiration timelines, cipher strength, and compliance with security policies across all clients.",
           [("Discover", "Automated discovery of all SSL/TLS certificates across client environments."), ("Monitor", "Continuous monitoring of expiration dates, cipher strength, and compliance."), ("Renew", "Automated renewal workflows with verification and deployment."), ("Report", "Certificate health dashboards for all clients.")],
           ["Certificate discovery", "Expiration prediction", "Automated renewal", "Cipher compliance checking"],
           ["Approve certificate renewals", "Review cipher policy exceptions", "Validate discovery coverage"],
           ["Zero unexpected certificate expirations", "Renewal automation >90%", "Discovery coverage >99%"],
           [("Network Configuration Management", "network-configuration-management", "network-ops"), ("Attack Surface Management", "attack-surface-management", "security-operations")],
           ["Network Engineer", "Security Analyst"], ["network-engineer", "security-analyst"]),
        pa("Ticket-Driven Network Automation", "ticket-driven-network-automation", "Network changes triggered and executed from service desk tickets",
           "Ticket-Driven Network Automation bridges the gap between service desk operations and network management. When a ticket requires a network change — VLAN assignment, firewall rule, port configuration, or ACL update — the system executes the change automatically via approved automation workflows.\n\nThis eliminates the manual handoff between service desk and network teams for routine changes. The AI validates each requested change against network policies, checks for conflicts, and executes the change with rollback capability.\n\nFull audit trails link every network change to its originating ticket, providing complete traceability for compliance and troubleshooting.",
           [("Trigger", "Network change request identified in service desk ticket."), ("Validate", "AI checks request against policies and detects potential conflicts."), ("Execute", "Automated workflow implements the network change."), ("Verify", "Post-change validation confirms success; ticket updated automatically.")],
           ["Policy validation", "Conflict detection", "Change execution", "Automated verification"],
           ["Approve non-standard changes", "Review conflict alerts", "Validate automation policies"],
           ["Automated change success rate >98%", "Mean change execution time <5 minutes", "Change-related incidents <0.5%"],
           [("Network Configuration Management", "network-configuration-management", "network-ops"), ("Playbook Automation", "playbook-automation", "service-desk")],
           ["Network Engineer", "Service Desk Manager"], ["network-engineer", "service-desk-manager"]),
        pa("Topology Visualization", "topology-visualization", "Real-time interactive network topology maps",
           "Topology Visualization provides real-time, interactive network maps that show the complete infrastructure topology for each client environment. AI-generated layouts automatically organize complex networks into understandable diagrams with device relationships, traffic flows, and health status.\n\nThe visualization updates dynamically as devices are added, removed, or change state. Color-coded health indicators show at-a-glance status, while click-through functionality provides detailed device information and historical metrics.\n\nTopology views are exportable for client documentation, QBR presentations, and compliance evidence.",
           [("Map", "Automated topology generation from discovery data."), ("Visualize", "Interactive map with real-time health and status indicators."), ("Navigate", "Click-through to device details, metrics, and configuration."), ("Export", "Topology diagrams exportable for documentation and presentations.")],
           ["Auto-layout generation", "Real-time status overlay", "Impact visualization", "Change highlighting"],
           ["Validate topology accuracy", "Review auto-generated layouts", "Approve client-facing exports"],
           ["Topology accuracy >98%", "Real-time update latency <30 seconds", "Client satisfaction with documentation >4.5/5.0"],
           [("Network Discovery & Automation", "network-discovery-automation", "network-ops"), ("Network Configuration Management", "network-configuration-management", "network-ops")],
           ["Network Engineer", "IT Director", "vCIO"], ["network-engineer", "it-director", "vcio"])
    ]
})

# Now add the remaining zones more efficiently
remaining_zones = [
    ("vC-Suite", "vc-suite", "Executive Suite", "Strategic Executive Intelligence", "👔", [
        ("Executive KPI Dashboards", "executive-kpi-dashboards", "Real-time KPI tracking across all operational zones", "vCIO", "IT Director"),
        ("vCIO Advisory Engine", "vcio-advisory-engine", "AI-powered technology advisory recommendations for vCIOs", "vCIO", "IT Director"),
        ("vCISO Security Program", "vciso-security-program", "Security program management and posture tracking for vCISOs", "vCISO", "Security Analyst"),
        ("vCCO Compliance Governance", "vcco-compliance-governance", "Compliance governance dashboards for virtual compliance officers", "Compliance Officer", "vCISO"),
        ("vCTO Architecture Reviews", "vcto-architecture-reviews", "Architecture review and technical debt tracking for vCTOs", "DevOps Engineer", "IT Director"),
        ("Technology Roadmap Management", "technology-roadmap-management", "Strategic technology planning and roadmap visualization", "vCIO", "IT Director"),
        ("QBR Framework Builder", "qbr-framework-builder", "AI-automated QBR document and presentation generation", "Service Delivery Manager", "Client Success Manager"),
        ("Client Profitability Analysis", "client-profitability-analysis", "Per-client profitability with fully loaded cost analysis", "Finance Coordinator", "IT Director"),
        ("Strategic Recommendations", "strategic-recommendations", "AI-generated strategic improvement suggestions based on operational data", "vCIO", "IT Director"),
        ("Cross-Zone Executive Briefings", "cross-zone-executive-briefings", "AI-summarized briefings aggregating insights across all zones", "IT Director", "Service Delivery Manager"),
        ("MSP Benchmark Comparison", "msp-benchmark-comparison", "Anonymous cross-MSP benchmarking for operational metrics", "IT Director", "vCIO"),
        ("Risk Appetite Modeling", "risk-appetite-modeling", "Framework for defining and monitoring organizational risk tolerance", "vCISO", "Compliance Officer"),
        ("Executive Alert & Escalation", "executive-alert-escalation", "Smart escalation to executives for critical events across zones", "IT Director", "vCISO"),
    ]),
    ("Analytics", "analytics", "Business & Operations", "Cross-Zone Operational Intelligence", "📊", [
        ("Ticket Volume Forecasting", "ticket-volume-forecasting", "AI-predicted ticket volumes for capacity planning", "Service Desk Manager", "IT Director"),
        ("Churn Prediction Model", "churn-prediction-model", "AI-driven client churn risk detection and prevention", "Client Success Manager", "Service Delivery Manager"),
        ("Benchmark Intelligence", "benchmark-intelligence", "Cross-client operational benchmarking and industry comparisons", "IT Director", "vCIO"),
        ("Cross-Domain Correlation", "cross-domain-correlation", "Connecting insights across zones for multi-dimensional analysis", "Data Analyst", "IT Director"),
        ("License Optimization Intelligence", "license-optimization-intelligence", "AI analysis of software licensing for cost optimization", "Finance Coordinator", "IT Director"),
        ("Natural Language BI Queries", "natural-language-bi-queries", "Ask questions in plain English and get data-driven answers", "Data Analyst", "IT Director"),
        ("QBR Aggregation Engine", "qbr-aggregation-engine", "Automated collection and formatting of QBR metrics", "Service Delivery Manager", "Client Success Manager"),
        ("Security Risk Scoring", "security-risk-scoring", "Composite security risk scores across client environments", "Security Analyst", "vCISO"),
        ("Automated Report Generation", "automated-report-generation", "AI-generated operational reports on customizable schedules", "Data Analyst", "Service Delivery Manager"),
    ]),
    ("Relationships", "relationships", "Business", "Client Relationship Intelligence", "🤝", [
        ("Client Health Scoring", "client-health-scoring", "AI-driven composite client health scores across all touchpoints", "Client Success Manager", "Service Delivery Manager"),
        ("Churn Risk Detection", "churn-risk-detection", "Early warning system for client satisfaction decline", "Client Success Manager", "Service Delivery Manager"),
        ("Client Onboarding Workflows", "client-onboarding-workflows", "Automated client onboarding with phase-gated milestones", "Client Success Manager", "Project Manager"),
        ("QBR Preparation & Delivery", "qbr-preparation-delivery", "Automated QBR assembly with AI-generated insights", "Service Delivery Manager", "Client Success Manager"),
        ("Sales Pipeline Management", "sales-pipeline-management", "AI-scored deal pipeline with close probability and velocity tracking", "Sales Director", "Client Success Manager"),
        ("Lead Generation & ICP Scoring", "lead-generation-icp-scoring", "AI-driven lead scoring against ideal customer profiles", "Sales Director", "Marketing Director"),
        ("Marketing Campaign Orchestration", "marketing-campaign-orchestration", "Multi-channel campaign management with AI content assistance", "Marketing Director", "Sales Director"),
        ("Content Sharing Portal", "content-sharing-portal", "Client-facing knowledge portal with branded content delivery", "Marketing Director", "Client Success Manager"),
        ("Customer Portal Management", "customer-portal-management", "Self-service client portal with ticket, report, and request access", "Client Success Manager", "Service Delivery Manager"),
        ("Contract Operations", "contract-operations", "Contract lifecycle management with renewal tracking", "Finance Coordinator", "Client Success Manager"),
        ("Referral & Expansion Tracking", "referral-expansion-tracking", "Tracking referral programs and expansion revenue opportunities", "Sales Director", "Client Success Manager"),
    ]),
    ("People", "people", "People & Culture", "Intelligent Workforce Management", "👥", [
        ("Employee Onboarding Automation", "employee-onboarding-automation", "Automated new hire onboarding with identity provisioning", "HR Director", "IT Director"),
        ("Offboarding & Access Revocation", "offboarding-access-revocation", "Secure employee offboarding with complete access removal", "HR Director", "Security Analyst"),
        ("Access Lifecycle Management", "access-lifecycle-management", "Role-based access provisioning and continuous entitlement review", "HR Director", "Security Analyst"),
        ("Directory Synchronization", "directory-synchronization", "Cross-platform identity directory sync and conflict resolution", "IT Director", "HR Director"),
        ("Workforce Analytics", "workforce-analytics", "AI-powered workforce metrics including utilization and capacity", "HR Director", "IT Director"),
        ("Engagement & Sentiment Tracking", "engagement-sentiment-tracking", "Employee satisfaction and engagement monitoring", "HR Director", "Recruiter"),
        ("Burnout & Wellness Detection", "burnout-wellness-detection", "AI-detected burnout risk indicators from work patterns", "HR Director", "Service Desk Manager"),
        ("Contractor & Vendor Access", "contractor-vendor-access", "Secure temporary access management for external personnel", "HR Director", "Security Analyst"),
    ]),
    ("Learning", "learning", "People & Culture", "Continuous Learning & Knowledge", "📚", [
        ("LMS Engine", "lms-engine", "Integrated learning management with role-based curricula", "HR Director", "IT Director"),
        ("Skill Gap Analysis", "skill-gap-analysis", "AI-identified skill gaps with personalized learning paths", "HR Director", "Recruiter"),
        ("Certification Tracking", "certification-tracking", "Professional certification monitoring with renewal alerts", "HR Director", "IT Director"),
        ("Compliance Training", "compliance-training", "Regulatory compliance training with completion tracking", "Compliance Officer", "HR Director"),
        ("Knowledge Store", "knowledge-store", "Centralized knowledge base with AI-powered search and recommendations", "IT Director", "Service Desk Manager"),
        ("Onboarding Journeys", "onboarding-journeys", "Structured learning paths for new hire ramp-up", "HR Director", "Recruiter"),
        ("AI Tutoring", "ai-tutoring", "Interactive AI-powered tutoring for technical and soft skills", "HR Director", "IT Director"),
        ("SOP & Runbook Management", "sop-runbook-management", "Standard operating procedure creation and maintenance", "IT Director", "Service Desk Manager"),
        ("Speech-Enabled Training", "speech-enabled-training", "Voice-interactive training modules for hands-free learning", "HR Director", "IT Director"),
        ("Workflow Analysis & Recommendations", "workflow-analysis-recommendations", "AI analysis of work patterns with efficiency suggestions", "IT Director", "Service Delivery Manager"),
    ]),
    ("Organization", "organization", "People & Culture", "Organizational Structure Intelligence", "🏗️", [
        ("Department Hierarchy Management", "department-hierarchy-management", "Organizational chart management with role mapping", "HR Director", "IT Director"),
        ("Multi-Tenant Administration", "multi-tenant-administration", "Managing multiple client environments from a single pane", "IT Director", "DevOps Engineer"),
        ("Team Structure Optimization", "team-structure-optimization", "AI-recommended team structures for optimal performance", "HR Director", "IT Director"),
        ("Role & Accountability Charting", "role-accountability-charting", "RACI matrix management with gap detection", "HR Director", "IT Director"),
        ("Location & Site Management", "location-site-management", "Multi-site infrastructure and resource management", "IT Director", "Network Engineer"),
        ("Organizational Health Scoring", "organizational-health-scoring", "Composite health metrics across people, process, and technology", "HR Director", "IT Director"),
        ("Meeting Cadence Management", "meeting-cadence-management", "Structured meeting frameworks with automated agenda and notes", "Service Delivery Manager", "IT Director"),
        ("EOS Rocks & Goals Tracking", "eos-rocks-goals-tracking", "Entrepreneurial Operating System goal and rock tracking", "IT Director", "Service Delivery Manager"),
        ("Cost Center Management", "cost-center-management", "Budget tracking and cost allocation across organizational units", "Finance Coordinator", "IT Director"),
        ("Organizational Policy Framework", "organizational-policy-framework", "Company-wide policy management and enforcement", "HR Director", "Compliance Officer"),
        ("Branding & White Label", "branding-white-label", "MSP brand customization for client-facing portals and reports", "Marketing Director", "IT Director"),
    ]),
    ("Legal", "legal", "Business", "Legal Operations Automation", "⚖️", [
        ("Contract Analysis & Review", "contract-analysis-review", "AI-powered contract analysis with risk identification", "Legal Counsel", "Compliance Officer"),
        ("Contract Engine & Automation", "contract-engine-automation", "Automated contract generation with clause management", "Legal Counsel", "Finance Coordinator"),
        ("NDA & Vendor Agreement Management", "nda-vendor-agreement-management", "Standardized NDA and vendor agreement workflows", "Legal Counsel", "Compliance Officer"),
        ("Data Privacy Management", "data-privacy-management", "GDPR/CCPA compliance management and data subject requests", "Legal Counsel", "Compliance Officer"),
        ("Regulatory Change Monitoring", "regulatory-change-monitoring", "Automated monitoring of regulatory changes affecting operations", "Legal Counsel", "Compliance Officer"),
        ("Incident Legal Response", "incident-legal-response", "Legal response coordination for security incidents and breaches", "Legal Counsel", "vCISO"),
        ("Intellectual Property Tracking", "intellectual-property-tracking", "IP asset management with protection status monitoring", "Legal Counsel", "IT Director"),
    ]),
    ("DevOps", "devops", "Engineering", "Platform Engineering & Automation", "⚙️", [
        ("CI/CD Pipeline Management", "ci-cd-pipeline-management", "Automated build, test, and deployment pipeline orchestration", "DevOps Engineer", "IT Director"),
        ("Deployment Orchestration", "deployment-orchestration", "Multi-environment deployment coordination with approval gates", "DevOps Engineer", "IT Director"),
        ("Configuration Management", "configuration-management", "Infrastructure-as-code with drift detection and remediation", "DevOps Engineer", "Network Engineer"),
        ("Environment Lifecycle", "environment-lifecycle", "Development, staging, and production environment management", "DevOps Engineer", "IT Director"),
        ("Feature Flag Management", "feature-flag-management", "Progressive feature rollout with targeting and analytics", "DevOps Engineer", "Project Manager"),
        ("Integration Health Dashboard", "integration-health-dashboard", "Real-time monitoring of all platform integrations", "DevOps Engineer", "IT Director"),
        ("Connector Toolkit", "connector-toolkit", "Pre-built connectors for PSA, RMM, and third-party tools", "DevOps Engineer", "IT Director"),
        ("A/B Testing Framework", "a-b-testing-framework", "Experimentation platform for feature and workflow optimization", "DevOps Engineer", "Data Analyst"),
        ("Bottleneck Detection", "bottleneck-detection", "AI identification of pipeline and workflow bottlenecks", "DevOps Engineer", "IT Director"),
        ("SRE Golden Signals", "sre-golden-signals", "Latency, traffic, errors, and saturation monitoring for all services", "DevOps Engineer", "IT Director"),
        ("GCC High Compliance Deployment", "gcc-high-compliance-deployment", "Government cloud compliant deployment automation", "DevOps Engineer", "Compliance Officer"),
    ]),
    ("Accounting", "accounting", "Business", "Financial Operations Intelligence", "💰", [
        ("Invoice Ingestion & Processing", "invoice-ingestion-processing", "AI-powered invoice capture and automated processing", "Finance Coordinator", "IT Director"),
        ("Reconciliation Engine", "reconciliation-engine", "Automated multi-source financial reconciliation", "Finance Coordinator", "Data Analyst"),
        ("Revenue Recognition", "revenue-recognition", "Automated revenue recognition per ASC 606 standards", "Finance Coordinator", "IT Director"),
        ("Subscription Management", "subscription-management", "Recurring subscription billing and lifecycle management", "Finance Coordinator", "Client Success Manager"),
        ("Three-Way Billing Reconciliation", "three-way-billing-reconciliation", "Cross-referencing contracts, usage, and invoices for billing accuracy", "Finance Coordinator", "Client Success Manager"),
        ("GL Integration", "gl-integration", "General ledger integration with automated journal entries", "Finance Coordinator", "IT Director"),
        ("Payment Processing", "payment-processing", "Automated payment collection and processing workflows", "Finance Coordinator", "Client Success Manager"),
        ("Procurement Automation", "procurement-automation", "AI-assisted procurement with vendor comparison and approval workflows", "Finance Coordinator", "IT Director"),
        ("CPQ (Configure-Price-Quote)", "cpq-configure-price-quote", "AI-assisted quoting with margin optimization", "Sales Director", "Finance Coordinator"),
        ("Contract Lifecycle Management", "contract-lifecycle-management", "Financial contract tracking with renewal and billing alignment", "Finance Coordinator", "Legal Counsel"),
        ("Webhook Payment Events", "webhook-payment-events", "Real-time payment event processing via webhook integrations", "Finance Coordinator", "DevOps Engineer"),
    ]),
    ("Projects", "projects", "Engineering", "Project Delivery Intelligence", "📐", [
        ("Phase-Gated Execution", "phase-gated-execution", "Structured project execution with phase gates and approval workflows", "Project Manager", "IT Director"),
        ("Discovery & Assessment", "discovery-assessment", "AI-assisted project discovery and scope assessment", "Project Manager", "IT Director"),
        ("Microsoft 365 Migration", "microsoft-365-migration", "Automated M365 tenant migration with validation", "Project Manager", "DevOps Engineer"),
        ("Multi-Project Portfolio", "multi-project-portfolio", "Cross-project portfolio management with resource optimization", "Project Manager", "IT Director"),
        ("Playbook Designer", "playbook-designer", "Visual project playbook creation with reusable templates", "Project Manager", "Service Delivery Manager"),
        ("PM Governance & Reporting", "pm-governance-reporting", "Project governance dashboards and executive reporting", "Project Manager", "IT Director"),
        ("CAB Submissions & AI Risk Scoring", "cab-submissions-ai-risk-scoring", "Change advisory board automation with AI risk assessment", "Project Manager", "IT Director"),
        ("Hypercare & Stabilization", "hypercare-stabilization", "Post-migration monitoring with rapid issue resolution", "Project Manager", "Service Desk Manager"),
        ("Working Sessions", "working-sessions", "Collaborative project session management with notes and action tracking", "Project Manager", "Service Delivery Manager"),
        ("Batch Execution Engine", "batch-execution-engine", "Bulk task execution across multiple clients or environments", "Project Manager", "DevOps Engineer"),
        ("Artifact Management", "artifact-management", "Project document and deliverable lifecycle management", "Project Manager", "IT Director"),
    ]),
]

# Build full zone entries for remaining zones
for zname, zslug, cluster, tagline, icon, pa_list in remaining_zones:
    zone_pas = []
    for pa_name, pa_slug, pa_desc, role1, role2 in pa_list:
        # Generate realistic overview for each PA
        overview = f"{pa_name} brings AI-powered automation to a critical operational capability within the {zname} zone. The system streamlines workflows that traditionally required significant manual effort, reducing time-to-completion while improving accuracy and consistency.\n\nBy leveraging machine learning models trained on operational data across your MSP's client base, the platform identifies patterns, predicts outcomes, and suggests optimizations that would be impossible to achieve manually. Every action is logged for compliance and continuous improvement.\n\nCross-zone intelligence ensures that insights from {pa_name} flow to connected zones and roles, creating a unified operational picture that drives better decision-making across your entire organization."

        # Generate steps
        steps = [
            ("Collect", f"Gather relevant data from connected systems and client environments for {pa_name.lower()}."),
            ("Analyze", f"AI processes data to identify patterns, anomalies, and optimization opportunities."),
            ("Execute", f"Automated workflows handle routine tasks while flagging exceptions for human review."),
            ("Report", f"Results tracked, measured, and reported through dashboards and scheduled reports.")
        ]

        # Generate connected PAs (pick 2 from same zone if available, or cross-zone)
        connected = []
        for other_name, other_slug, _, _, _ in pa_list:
            if other_slug != pa_slug and len(connected) < 2:
                connected.append((other_name, other_slug, zslug))

        role1_slug = role1.lower().replace(" ", "-").replace("/", "-")
        role2_slug = role2.lower().replace(" ", "-").replace("/", "-")
        # Fix known slug mappings
        slug_map = {"vcio": "vcio", "vciso": "vciso", "vcto": "vcto", "vcco": "vcco"}
        if role1_slug in slug_map: role1_slug = slug_map[role1_slug]
        if role2_slug in slug_map: role2_slug = slug_map[role2_slug]

        zone_pas.append({
            "name": pa_name, "slug": pa_slug, "description": pa_desc,
            "overview": overview,
            "how_it_works": [{"step": i+1, "title": s[0], "description": s[1]} for i, s in enumerate(steps)],
            "ai_capabilities": ["Pattern recognition and analysis", "Predictive analytics", "Automated workflow execution", "Cross-zone intelligence sharing"],
            "hitl_checkpoints": ["Review AI recommendations before execution", "Approve changes to critical systems", "Validate automated outputs"],
            "key_metrics": ["Process automation rate >70%", "Time savings >50% vs manual", "Accuracy improvement >25%"],
            "connected_pas": [{"name": c[0], "slug": c[1], "zone_slug": c[2]} for c in connected],
            "related_roles": [role1, role2],
            "related_role_slugs": [role1_slug, role2_slug]
        })

    ZONES.append({
        "name": zname, "slug": zslug, "cluster": cluster,
        "tagline": tagline, "icon": icon, "process_areas": zone_pas
    })

# Write JSON
data = {"zones": ZONES}
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pa-data.json")
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)

total = sum(len(z["process_areas"]) for z in ZONES)
print(f"Generated pa-data.json with {len(ZONES)} zones and {total} process areas")
