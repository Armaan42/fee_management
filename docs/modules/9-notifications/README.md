# Module 9: Notifications & Communication

## Overview
The Notifications & Communication module automates all fee-related communications with parents through SMS, Email, and WhatsApp. It sends timely reminders, payment confirmations, receipts, and custom announcements, ensuring parents stay informed about their child's fee status.

**Core Responsibility**: Automate parent communication regarding fees.

## Purpose
- **Due Reminders**: Automated reminders before and after due dates
- **Payment Confirmations**: Instant confirmation on successful payment
- **Receipt Delivery**: Digital receipt delivery via email/SMS
- **Overdue Notifications**: Escalating reminders for overdue payments
- **Custom Announcements**: Broadcast fee-related announcements
- **Template Management**: Manage communication templates
- **Delivery Tracking**: Track message delivery status

## Submodules

### 9.1 Fee Due Reminders
Send automated reminders before fee due dates.

**Key Features**: Scheduled sending, Multi-channel delivery, Personalization, Delivery tracking

**Example**: Send reminder 3 days before due date: "Dear Parent, ₹15,000 due on 10-Apr"

**[View Detailed Documentation →](submodules/9.1-fee-due-reminders/README.md)**

---

### 9.2 Payment Confirmation
Instant confirmation when payment is received.

**Key Features**: Real-time sending, Receipt details, Multiple channels, Delivery confirmation

**Example**: "Payment of ₹15,000 received. Receipt #FEE/2024/00123. Thank you!"

**[View Detailed Documentation →](submodules/9.2-payment-confirmation/README.md)**

---

### 9.3 Receipt Delivery
Send digital receipts to parents.

**Key Features**: PDF generation, Email/SMS delivery, WhatsApp integration, Download links

**Example**: Email with PDF receipt attached sent immediately after payment

**[View Detailed Documentation →](submodules/9.3-receipt-delivery/README.md)**

---

### 9.4 Overdue Notifications
Escalating reminders for overdue payments.

**Key Features**: Multi-level reminders, Escalation schedule, Tone management, Fine notifications

**Example**: Day 7: Polite reminder → Day 15: Firm reminder → Day 30: Final notice

**[View Detailed Documentation →](submodules/9.4-overdue-notifications/README.md)**

---

### 9.5 Custom Announcements
Broadcast fee-related announcements to all or selected parents.

**Key Features**: Bulk sending, Filtering, Scheduling, Template support

**Example**: "New academic year fees announced. Visit portal for details."

**[View Detailed Documentation →](submodules/9.5-custom-announcements/README.md)**

---

### 9.6 Communication Templates
Manage SMS/Email/WhatsApp templates.

**Key Features**: Template creation, Variable support, Multi-language, Version control

**Example**: Template: "Dear {parent_name}, {amount} due on {due_date} for {student_name}"

**[View Detailed Documentation →](submodules/9.6-communication-templates/README.md)**

---

### 9.7 Delivery Status Tracking
Track delivery status of all communications.

**Key Features**: Delivery reports, Failure tracking, Retry mechanism, Analytics

**Example**: 150 SMS sent, 148 delivered, 2 failed (invalid number)

**[View Detailed Documentation →](submodules/9.7-delivery-status-tracking/README.md)**

---

## Workflow

### Communication Flow
```
Trigger Event → Select Template → Personalize → Send via Channel → Track Delivery → Log Status
```

## Inbound Connections

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Module 1** | Fee assignments | Fee structure notifications |
| **Module 2** | Fine applied | Fine notifications |
| **Module 3** | Receipt generated | Receipt delivery |
| **Module 4** | Payment status | Payment confirmations |
| **Module 6** | Overdue status | Reminder notifications |

## Outbound Connections

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **SMS Gateway** | SMS content | Send messages |
| **Email Service** | Email content | Send emails |
| **WhatsApp API** | WhatsApp messages | Send WhatsApp |
| **Module 8** | Delivery status | Audit trail |

## Best Practices
1. Send reminders before due dates
2. Use polite, professional language
3. Personalize messages
4. Test templates before bulk sending
5. Monitor delivery rates
6. Respect communication preferences

## Security & Permissions

| Role | Permissions |
|------|------------|
| **Super Admin** | Configure templates, send announcements |
| **Accounts Admin** | Send reminders, view delivery status |
| **System** | Auto-send triggered notifications |
