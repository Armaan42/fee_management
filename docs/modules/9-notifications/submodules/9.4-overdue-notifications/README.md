# 9.4 Overdue Notifications

## Overview
**Overdue Notifications** manage the delicate art of debt recovery. While "Reminders" are polite nudges before the due date, "Overdue Notifications" are firmer calls to action after the deadline has passed. This module automates the escalation process, increasing the urgency of communication as the delay grows.

### Real-World Analogy
Think of this as a **Traffic Callan Escalation**.
1.  **Violation**: You jump a red light (Due Date Crossed).
2.  **SMS 1**: "You have been fined ₹500. Pay within 15 days." (Standard Notice).
3.  **SMS 2**: "Urgent: Payment overdue. Late fee applied." (Escalation).
4.  **Final Notice**: "Pay immediately or Court Summons will be issued." (Consequence).
This module moves the parent from "I'll do it later" to "I must do it now".

## Purpose
- **Accelerate Recovery**: Reduce the "Days Sales Outstanding" (DSO) by constantly following up.
- **Automate Policy**: Enforce the "Late Fee" and "Access Block" rules automatically without human intervention.
- **Documentation**: Create a legal trail showing that "3 notices were sent" before taking any strict action like striking off the name.
- **Identify Risk**: If a parent ignores 3 sequential notifications, they are flagged as a "High-Risk Defaulter".

## Key Features
- **Escalation Ladder**: Define stages (Day 1 -> Day 7 -> Day 15 -> Day 30).
- **Tone Adjustment**: Template changes from "Gentle" to "Firm" to "Strict".
- **Dynamic Penalty**: "Your fine has increased to ₹200." (Updates daily).
- **Snooze/Promise**: Ability for Admin to "Pause" notifications if the parent promises to pay on a specific date.

## Real-World Scenarios

### Scenario 1: The "Busy" Parent
**Situation**: Parent missed the deadline by 2 days.
**Action**:
1.  **Day 1 Overdue**: System sends a gentle text: "Dear Parent, it seems you missed the fee deadline. Please pay to avoid late charges."
2.  **Outcome**: Parent pays immediately. Relationship remains positive.

### Scenario 2: The "Stubborn" Payer
**Situation**: Parent hasn't paid for 30 days. Total Due = ₹50,000.
**Action**:
1.  **Day 30 Overdue**: System sends "Final Notice".
2.  **Message**: "Urgent: Fees overdue by 30 days. Access to School App will be blocked tomorrow."
3.  **Outcome**: The threat of service interruption forces the parent to act.

### Scenario 3: The "Snooze" Request
**Situation**: Parent calls the Principal. "I have a medical emergency. I will pay on the 25th."
**Action**:
1.  Principal clicks **"Snooze Notifications"** -> Select Date: 25th.
2.  **System**: Stops sending SMS until the 25th. Resumes on 26th if still unpaid.
3.  **Outcome**: Empathy shown, but system control maintained.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Disputed Fee** | Parent claims the bill is wrong. | **Hold Status**: Mark the invoice as "Under Dispute". This suppresses all automated notifications until the Accountant resolves it. |
| **Partial Payment** | Parent paid ₹5k out of ₹10k. | **Smart Context**: The message should say "Please pay the *remaining balance* of ₹5k", not "Please pay fees". |
| **Gateway Failure** | Parent tried to pay but failed. | **Comfort Interval**: If a failed transaction is detected, pause notifications for 24 hours to give them time to retry without pestering. |
| **Legal Case** | School has filed a case against the parent. | **Stop Logic**: Once flagged as "Legal Case", ALL automated communication stops. Only lawyers communicate. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Trigger Day** | Integer | "Days Past Due" (e.g., +5, +15). |
| **Severity** | Enum | Low, Medium, High, Critical. |
| **Channels** | List | SMS, Email, App Push, IVR Call. |
| **Template** | String | The message body. |
| **Snooze Until** | Date | If set, overrides triggers. |

## User Actions
1.  **View Queue**: "Who is receiving a notice today?".
2.  **Manual Override**: Remove "Mr. Sharma" from today's blast list.
3.  **Log Call**: Admin calls the parent and records "Spoke to Father. He said..." in the system.
4.  **Block Services**: Manually trigger "Block App Access" for a defaulter.

## Best Practices
- **Don't Spam**: Limit frequency. Once a week is "Following up". Once a day is "Harassment".
- **Offer Solutions**: Include a "Request Extension" link in the email for genuine cases.
- **Privacy**: Don't put the exact amount in the SMS if it's sent to a possibly shared number. Use "Please check portal for details".
