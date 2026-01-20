# 4.5 Payment Link Generation

## Overview
**Payment Link Generation** gives you the power to request fees anytime, anywhere. Instead of waiting for parents to log in to the portal, you can proactively send them a direct link via SMS, WhatsApp, or Email.

### Real-World Analogy
Think of this as sending a **Digital Invoice**.
When you buy something from a freelance artist or a small vendor online, they often send you a link saying "Click here to pay ₹500". You click, enter card details, and it's done. You don't need to create an account on their website or remember a password. This module brings that same convenience to school fees.

## Purpose
- **Speed Up Collection**: Reduce friction by putting the payment button right in the parent's SMS inbox.
- **Targeted Recovery**: Send reminders specifically to overdue parents.
- **Ad-Hoc Payments**: Collect fees for field trips or events that aren't part of the standard fee structure.
- **Guest Payments**: Allow non-registered users (e.g., alumni donors) to make payments.

## Key Features
- **Instant Creation**: Generate a unique, secure link in 2 clicks.
- **Multi-Channel Sharing**: Copy link, Send via SMS, or Email directly from the dashboard.
- **Custom Amounts**: Create a link for exactly ₹5,000 or allow the parent to choose the amount.
- **Expiry Controls**: Set the link to expire after 24 hours to create urgency.
- **Status Tracking**: See exactly who clicked the link and who paid.

## Real-World Scenarios

### Scenario 1: The Overdue Reminder
**Situation**: It's the 15th of the month, and 50 parents haven't paid tuition fees.
**Action**:
1.  Admin filters the "Defaulter List".
2.  Selects all 50 students.
3.  Clicks **"Send Payment Link"**.
**Outcome**: Parents receive an SMS: "Dear Parent, fees of ₹12,000 differ. Click https://sch.ool/pay/xYz to pay now." Collections surge within hours.

### Scenario 2: The "Science Museum Trip" (Ad-Hoc Fee)
**Situation**: The school organizes a sudden trip costing ₹500/student. This fee wasn't in the annual plan.
**Action**:
1.  Admin creates a "Bulk Payment Link" titled "Science Trip".
2.  Sets amount to Fixed: ₹500.
3.  Sends it to all Class 8 parents.
**Outcome**: Parents pay specifically for the trip without the Admin needing to restructure the entire yearly fee database.

### Scenario 3: Helping a Tech-Challenged Parent
**Situation**: A grandparent wants to pay fees but finds the Student Portal too confusing to log into.
**Action**:
1.  Admin generates a specific link for that student's outstanding balance.
2.  Sends the link via WhatsApp to the grandparent.
3.  Grandparent clicks, sees the pre-filled amount, and pays via UPI.
**Outcome**: Frictionless payment experience.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Link Expiry** | Parent clicks the link 2 days after deadline. | Show a friendly "Link Expired" page. Advise them to contact the school or log in to the main portal. |
| **Double Payment** | Parent pays, then forgets and clicks the link again. | System detects the Order ID is "Paid". Show a "Payment Already Received" receipt page instead of the payment form. |
| **Fee Structure Change** | Link generated for ₹5,000, but Admin increased fee to ₹6,000 later. | Links are usually static snapshots. The parent pays ₹5,000. Use "Partial Payment" logic to show ₹1,000 pending balance later. |
| **Partial Pay Toggle** | Parent wants to pay only ₹2,000 of the requested ₹5,000. | When creating link, Admin must decide: "Allow Partial Payment?" (Yes/No). If No, parent must pay full amount or nothing. |
| **Broken Link** | SMS character limit cuts off the URL. | Use a built-in URL Shortener (e.g., `sch.ool/pay/xYz`) to ensure links fit in standard SMS templates. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Link ID** | String | Unique hash for the URL. |
| **Purpose** | String | Reason for payment (e.g., "Term 1 Fees", "Bus Fee"). |
| **Amount Type** | Enum | `Fixed Amount` or `Customer Decides`. |
| **Expiry Date** | DateTime | When the link becomes invalid. |
| **Status** | Status | `Active`, `Paid`, `Expired`, `Cancelled`. |
| **Click Count** | Integer | How many times the link was opened (Interest tracking). |

## User Actions
1.  **Create Link**: Generate single or bulk links.
2.  **Share**: Send via integrated communication channels.
3.  **Deactivate**: Manually cancel a link if sent in error.
4.  **View Report**: See conversion rate (Sent vs. Paid).

## Best Practices
- **Use Expiry Dates**: Tells parents "Pay by Friday" instead of "Pay whenever".
- **Clear Descriptions**: Title the link "Class 10 Fee - March" so parents know exactly what they are paying for.
- **Don't Spam**: Don't send links daily. Weekly reminders work best.
