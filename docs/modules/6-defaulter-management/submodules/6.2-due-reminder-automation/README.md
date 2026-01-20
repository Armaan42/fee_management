# 6.2 Due Reminder Automation

## Overview
**Due Reminder Automation** is the communication engine that nudges parents to pay on time. It moves away from the manual "calling each parent" approach to a set-and-forget autopilot system that sends personalized SMS, Emails, and App Notifications at scheduled intervals.

### Real-World Analogy
Think of this as a **Smart Alarm Clock**.
- **Before Time (Snooze)**: A gentle chime at 7 AM ("Fees due in 3 days").
- **On Time (Ring)**: A standard ring at 8 AM ("Fees due Today").
- **Late (Siren)**: A loud, persistent beep if you oversleep ("Overdue! Please pay immediately").
Just like an alarm stops once you wake up (Pay), this system automatically stops sending reminders the moment the fee is cleared.

## Purpose
- **Reduce Human Effort**: No need for staff to manually draft 2,000 emails.
- **Improve Cash Flow**: "Pre-due" reminders significantly increase on-time payments.
- **Maintain Relationship**: Automated polite messages are less confrontational than personal calls.
- **Create Urgency**: "Late Fee starts tomorrow" messages drive immediate action.

## Key Features
- **Multi-Channel Delivery**: SMS, WhatsApp, Email, Mobile App Push Notification.
- **Dynamic Templates**: "Dear {{ParentName}}, fees of {{DueAmount}} for {{StudentName}} is pending."
- **Trigger Logic**: Configure rules like "T-3 Days" (Before), "T+0 Days" (On Due Date), "T+5 Days" (After).
- **Auto-Stop**: Intelligent logic ensures no reminders are sent if `Balance <= 0`.

## Real-World Scenarios

### Scenario 1: The "Pre-emptive Strike"
**Situation**: Fee due date is 10th. It is currently 7th.
**Action**:
1.  System wakes up at 10 AM.
2.  Filters students with `Due > 0`.
3.  Sends SMS: "Gentle Reminder: School fees for T1 are due on 10th. Pay online to avoid rush."
**Outcome**: 30% of parents pay immediately, reducing the load on the due date.

### Scenario 2: The "Overdue" Escalation
**Situation**: It is the 15th. 50 parents still haven't paid.
**Action**:
1.  System detects these 50 defaulters.
2.  Sends a stricter Email: "URGENT: Fee Key overdue. Late fine of ₹50/day applicable from tomorrow."
3.  Attached the Invoice PDF automatically.
**Outcome**: Creates financial urgency without manual intervention.

### Scenario 3: The "Snooze" (Hold)
**Situation**: A parent calls and says, "Salary delayed, I will pay on 20th. Please don't message me."
**Action**:
1.  Admin opens the student profile.
2.  Sets **"Pause Reminders Until"** = 20th.
3.  System skips this student in the daily blast until the 20th.
**Outcome**: Respects the parent's request and prevents annoyance.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Stop After Payment** | Parent pays at 10:00 AM. Reminder scheduled for 10:05 AM. | System checks Balance in real-time *just before* sending. If 0, it aborts the message for that user. |
| **Wrong Number** | SMS fails to deliver (Bounce). | Log failure. Fallback to Email immediately. Flag student profile as "Invalid Mobile". |
| **DND Filters** | Parent has "Do Not Disturb" active on phone. | Use "Transactional" SMS route (Template registred with DLT) which overrides DND for service alerts. |
| **Duplicate Spam** | Student has 2 different overdue invoices. | System aggregates them. Instead of 2 SMS, send 1 SMS saying "Total Due: ₹15,000" (Sum of both). |
| **Gateway Down** | Payment gateway is down today. | **CRITICAL**: Admin must Pause the "Due Today" reminder to avoid panic. Send a manual "Maintenance" alert instead. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Reminder ID** | String | Unique ID for the scheduled job. |
| **Trigger Date** | Date | When to send (Relative to Due Date). |
| **Channel** | Enum | `SMS`, `Email`, `Check`, `App`. |
| **Template** | Text | The message body with variables. |
| **Audience** | Count | Number of students targeted. |
| **Sent/Failed** | Count | Delivery report stats. |

## User Actions
1.  **Configure Rule**: Set up "Send SMS 2 days after Due Date".
2.  **Edit Template**: Modify the wording of the message.
3.  **View Logs**: See exactly who received the message and who didn't.
4.  **Pause/Resume**: Globally stop all reminders during holidays or emergencies.

## Best Practices
- **Time it Right**: Don't send SMS at 6 AM or 11 PM. 10 AM - 5 PM is the safe window.
- **Include Payment Link**: Always add the generic or specific payment link (`sch.ool/pay`) in the SMS.
- **Be Polite but Firm**: Start with "Dear Parent...", move to "Urgent Attention..." only after the deadline.
