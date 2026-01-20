# 9.1 Fee Due Reminders

## Overview
**Fee Due Reminders** are the automated heartbeat of the collection process. Instead of school staff manually calling hundreds of parents, this module works like a tireless assistant, sending perfectly timed notifications via SMS, Email, and App prompts to ensure parents remember to pay on time.

### Real-World Analogy
Think of this as your **Credit Card Bill Alert**.
- **Statement Generated**: "Dear User, your bill of ₹5000 is generated." (Informs availability).
- **Due Soon**: "Reminder: Bill due in 3 days." (The Nudge).
- **Due Today**: "Urgent: Bill due today. Pay to avoid charges." (The Call to Action).
Banks use this to ensure you don't default due to forgetfulness. We apply the same psychology to school fees.

## Purpose
- **Reduce Late Payments**: "I forgot" is the #1 reason for delay. Reminders eliminate this excuse.
- **Save Staff Time**: Automate the 500 phone calls the accountant would otherwise have to make.
- **Improve Cash Flow**: Prompt payments mean the school has money available to pay staff salaries on time.
- **Audit Trail**: Prove that the school *did* inform the parent before charging a fine.

## Key Features
- **Multi-Channel Delivery**: Send via SMS (for reach), Email (for detail), and WhatsApp (for convenience).
- **Dynamic Variables**: Personalize messages: "Dear {FatherName}, fees for {StudentName} is {Amount}."
- **Smart Scheduling**: Set rules like "Send 5 days before due date" and "Send on due date".
- **Payment Link**: Embedded "Pay Now" button in the message takes the parent directly to the payment gateway.

## Real-World Scenarios

### Scenario 1: The "Busy Professional" Parent
**Situation**: Parent is travelling and forgets the 10th is the fee deadline.
**Action**:
1.  System Auto-Scheduler wakes up at 9:00 AM on the 9th.
2.  Sends WhatsApp: "Reminder: School Fee for Rohan is due tomorrow. Click here to pay: [Link]".
3.  **Outcome**: Parent clicks the link and pays via UPI at the airport. Fine saved.

### Scenario 2: The "Cheque in Transit"
**Situation**: Parent dropped a cheque yesterday. Today they get a reminder.
**Action**:
1.  The reminder message includes a footer: *"Please ignore if already paid."*
2.  **Outcome**: Parent understands it's an automated system and doesn't get offended.

### Scenario 3: The "Grandparent" Payer
**Situation**: The grandfather pays the fees, but the SMS goes to the father.
**Action**:
1.  Admin configures "Secondary Contact" for notifications.
2.  **Outcome**: Both Father and Grandfather receive the reminder, doubling the chance of timely payment.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Already Paid** | Parent paid 1 hour ago. | **Live Check**: The system should query the "Balance" *just before* sending the SMS. If Balance <= 0, skip the SMS. |
| **Invalid Number** | SMS Bounced. | **Feedback Loop**: Mark the student profile with "Invalid Mobile". Alert the Class Teacher to collect the new number from the student diary. |
| **DND Filters** | Parent has "Do Not Disturb" active on their phone. | **Transactional Route**: School SMS should be registered as "Transactional" (Service Implicit) with DLT registry to bypass DND filters legally. |
| **Gateway Down** | "Pay Now" link is broken. | **Fail-Safe**: If the gateway is under maintenance, the SMS text should be auto-updated to "Please pay via Netbanking/Cash" instead of sending a dead link. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Template ID** | String | DLT-approved template code (e.g., "TEM123"). |
| **Trigger Date** | Rule | "Due Date - 3 Days". |
| **Channel** | Enum | SMS, Email, WhatsApp, App. |
| **Recipient** | Enum | Father, Mother, Guardian. |
| **Status** | Enum | Scheduled, Sent, Delivered, Failed. |

## User Actions
1.  **Configure Schedule**: "Send Reminder 1 on 1st, Reminder 2 on 5th".
2.  **Edit Template**: Change the wording from "Pay immediately" to "Kindly clear dues".
3.  **View Delivery Report**: See how many SMS were actually delivered vs failed.
4.  **Manual Blast**: "Send a special reminder for Field Trip Fees to Class 5 only".

## Best Practices
- **Time it Right**: Don't send SMS at 6:00 AM or 11:00 PM. Best time is 10:00 AM or 5:00 PM.
- **Keep it Short**: SMS has a 160-character limit. Be concise. Use Email for long explanations.
- **Verify Links**: Always test the payment link before sending 1000 messages.
