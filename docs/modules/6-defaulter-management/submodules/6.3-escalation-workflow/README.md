# 6.3 Escalation Workflow

## Overview
**Escalation Workflow** is the school's automated enforcement system. When polite reminders fail, this module takes progressive action. It follows a strict "Ladder of Consequences," ensuring that no defaulter is ignored while giving ample warning before severe actions are taken.

### Real-World Analogy
Think of this as a **Traffic Violation Lifecycle**.
1.  **Level 1 (Parking Ticket)**: You get a small fine (Late Fee).
2.  **Level 2 (Court Summons)**: You get a formal warning (Principal's Notice).
3.  **Level 3 (License Suspended)**: You lose privileges (Result Withheld / Access Block).
The severity increases the longer the rule is broken, but you can stop the escalation at any time by simply paying the fine (Fee).

## Purpose
- **Standardize Consequences**: Ensure every student is treated equally according to the policy.
- **Reduce Confrontation**: Staff can say, "The system automatically blocked the result," reducing personal arguments.
- **Drive Compliance**: The fear of "Level 3" actions motivates parents to pay at "Level 1".
- **Protect Revenue**: Prevents students from graduating with huge unpaid debts.

## Key Features
- **Configurable Levels**: Define what happens at Day 30, Day 60, and Day 90.
- **Action Triggers**: Auto-impose fines, disable app access, or block report cards.
- **Staff Alerts**: Notify Class Teachers to stop calling and let the Accounts Manager handle "Level 2" cases.
- **De-escalation Logic**: Instantly restore access when payment is received.

## Real-World Scenarios

### Scenario 1: The Late Fee (Level 1)
**Situation**: Student is 1 day past due (Grace period ended).
**Action**:
1.  System moves student to **Escalation Level 1**.
2.  Applies "Late Fine" of ₹50.
3.  Sends SMS: "Late fee applied. Pay now to avoid further escalation."
**Outcome**: Parent pays ₹10,050 immediately to stop the daily fine.

### Scenario 2: The Principal's Notice (Level 2)
**Situation**: Fees overdue by 45 days. SMS reminders ignored.
**Action**:
1.  System moves student to **Escalation Level 2**.
2.  Generates a formal "Defaulter Notice" PDF signed by the Principal.
3.  Emails it to the parent.
4.  Alerts the Class Teacher: "Please collect the diary note from Student X."
**Outcome**: The formality of the notice indicates seriousness.

### Scenario 3: The Result Block (Level 3)
**Situation**: Findings/Exam Term ended, but fees still pending (60+ days).
**Action**:
1.  System moves student to **Escalation Level 3**.
2.  **Action**: "Block Report Card Download".
3.  Parent logs in to view result -> Sees message: "Please clear dues to view grades."
**Outcome**: Parent rushes to the fee counter to pay. Access is restored instantly upon payment.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Manual Override** | Principal instructs to let a specific student view results despite dues. | "Super Admin" can apply a **"Whitelist Exception"** for the current exam cycle. Escalation resumes next cycle. |
| **Partial Payment** | Parent pays 50% of the overdue amount. | System policy check: "Does Level 3 require 100% clearance?". If yes, block remains. If no, system de-escalates to Level 1. |
| **Exam Policy** | School board rules forbid blocking students during board exams. | Admin enables **"Exam Amnesty Mode"** globally. Level 3 actions (Blocking) are paused until exam ends. |
| **False Positive** | Escalation triggered due to cheque clearance delay. | Admin clicks **"Revert Escalation"**. System removes fines and sends "Apology SMS". |
| **Holiday Overlap** | Level 2 (Call Parent) scheduled on a Sunday. | Task is auto-shifted to the next working day (Monday). |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Escalation ID** | String | Unique ID for the tracking event. |
| **Current Level** | Integer | 0 (Normal) to 3 (Severe). |
| **Trigger Date** | Date | When the student entered this level. |
| **Actions Taken** | List | Log of auto-actions (e.g., `["Fine Applied", "SMS Sent"]`). |
| **Next Action** | Date | When the next level kicks in. |

## User Actions
1.  **View Dashboard**: See how many students are at Level 1, 2, and 3.
2.  **Pause Escalation**: Temporarily hold actions for a specific student (e.g., medical emergency).
3.  **Execute Batch**: Manually trigger Level 2 notices for printing.
4.  **Configure Policy**: Set the number of days between levels.

## Best Practices
- **Warning First**: Never block access (Level 3) without at least 2 clear warnings (Level 1 & 2).
- **Instant Restore**: Ensure the "Unblock" happens continuously (24/7), not just when staff wakes up.
- **Human Review**: For Level 3, have a "Manager Approval" step before the block actually goes live.
