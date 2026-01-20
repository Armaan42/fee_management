# Module 6: Defaulter & Dues Management

## Overview
The Defaulter & Dues Management module identifies students with overdue payments, automates reminder communications, manages escalation workflows, and implements academic holds for persistent non-payment. It helps schools maintain healthy fee collection rates while being fair to parents.

**Core Responsibility**: Identify and manage students with pending fee dues.

## Purpose
- **Auto-Identification**: Automatically identify students with overdue payments
- **Reminder Automation**: Send automated reminders at scheduled intervals
- **Escalation Management**: Implement multi-level escalation workflows
- **Academic Holds**: Restrict exam/results for non-payment
- **Payment Plans**: Negotiate custom payment schedules
- **Legal Notices**: Generate formal notices for legal action

## Submodules

### 6.1 Defaulter Identification
Automatically identify students with overdue payments.

**Key Features**: Auto-detection, Overdue calculation, Categorization (mild/moderate/severe), Reporting

**Example**: System identifies 45 students with dues >30 days, categorizes by severity

**[View Detailed Documentation →](submodules/6.1-defaulter-identification/README.md)**

---

### 6.2 Due Reminder Automation
Send automated reminders to parents with pending dues.

**Key Features**: Scheduled reminders, Multi-channel (SMS/Email/WhatsApp), Template management, Delivery tracking

**Example**: Send reminder 3 days before due date, then 7 days after, then 15 days after

**[View Detailed Documentation →](submodules/6.2-due-reminder-automation/README.md)**

---

### 6.3 Escalation Workflow
Implement multi-level escalation for persistent defaulters.

**Key Features**: Level-based escalation, Authority routing, Timeline management, Action tracking

**Example**: Level 1: Class teacher call → Level 2: Principal meeting → Level 3: Legal notice

**[View Detailed Documentation →](submodules/6.3-escalation-workflow/README.md)**

---

### 6.4 Academic Hold Management
Restrict academic services for non-payment.

**Key Features**: Hold types (exam/results/certificate), Auto-application, Release mechanism, Exception handling

**Example**: Student with 60+ days overdue → Exam hold applied → Payment made → Hold released

**[View Detailed Documentation →](submodules/6.4-academic-hold-management/README.md)**

---

### 6.5 Payment Plan Negotiation
Create custom payment schedules for struggling parents.

**Key Features**: Plan creation, Approval workflow, Installment tracking, Compliance monitoring

**Example**: Parent requests 6-month plan for ₹30,000 dues → Approved → ₹5,000/month

**[View Detailed Documentation →](submodules/6.5-payment-plan-negotiation/README.md)**

---

### 6.6 Legal Notice Generation
Generate formal legal notices for persistent defaulters.

**Key Features**: Template-based generation, Legal compliance, Delivery tracking, Response management

**Example**: Generate legal notice for ₹50,000 dues pending for 90+ days

**[View Detailed Documentation →](submodules/6.6-legal-notice-generation/README.md)**

---

## Workflow

### Defaulter Management Process
```
Identify Overdue → Send Reminder → Wait → Still Pending? → Escalate → Academic Hold → Payment Plan/Legal Notice
```

## Inbound Connections

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Module 1 (Fee Structure)** | Fee due dates | Identify overdue payments |
| **Module 3 (Fee Collection)** | Payment status | Update dues |
| **Module 2 (Fine & Penalty)** | Fine amounts | Add to total dues |

## Outbound Connections

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **Module 2 (Fine & Penalty)** | Overdue status | Apply penalties |
| **Module 7 (Reports)** | Defaulter data | Due reports |
| **Module 8 (Audit)** | Hold actions | Audit trail |
| **Module 9 (Notifications)** | Defaulter status | Send reminders |
| **Academic Module** | Academic hold | Restrict services |

## Best Practices
1. Send reminders before due dates
2. Be empathetic in communications
3. Offer payment plans proactively
4. Document all interactions
5. Follow legal procedures strictly
6. Review holds regularly

## Security & Permissions

| Role | Permissions |
|------|------------|
| **Super Admin** | Full access, apply/release holds |
| **Principal** | Approve payment plans, legal notices |
| **Accounts Admin** | Manage defaulters, send reminders |
| **Class Teacher** | View defaulters, make calls |
