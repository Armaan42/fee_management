# 9.7 Delivery Status Tracking

## Overview
**Delivery Status Tracking** allows the school to close the loop on communication. Sending a message is only half the job; ensuring it was delivered and read is the other half. This module gives the Admin "X-Ray Vision" into the journey of every method, identifying exactly who got the message and who didn't.

### Real-World Analogy
Think of this as a **Registered Post Tracker**.
- **Sent**: Letter dropped in the postbox (One Tick).
- **Delivered**: Letter reached the destination mailbox (Two Ticks).
- **Read**: The receiver opened the envelope (Blue Ticks).
Without this tracking, the school is shouting into the void. With it, the school knows exactly whom to follow up with.

## Purpose
- **Verify Reach**: Ensure that critical announcements (like "School Closed") actually reached 100% of parents.
- **Clean Data**: Identify "Invalid Numbers" (hard bounces) and clean up the database to save costs.
- **Accountability**: Prove to a complaining parent ("I didn't know fees were due") that the message was indeed delivered to their phone on a specific date.
- **Vendor Management**: Monitor the performance of the SMS/Email Gateway provider. If delivery rates drop below 95%, it's time to switch vendors.

## Key Features
- **Granular Status**: Queued -> Dispatched -> Sent -> Delivered -> Read -> Failed.
- **Failure Reasons**: Specific error codes like "Mailbox Full", "Invalid Number", "Network Error".
- **Resend Logic**: Auto-retry failed messages via a backup channel (e.g., if WhatsApp fails, send SMS).
- **Campaign Stats**: "Email Campaign: 80% Open Rate, 5% Click Rate".

## Real-World Scenarios

### Scenario 1: The "I didn't know" Defense
**Situation**: Parent refuses to pay late fine, claiming "You never told me the due date."
**Action**:
1.  Admin searches number in **Delivery Log**.
2.  **Result**: "SMS ID #9988. Delivered: 10th Jan 10:00 AM. Status: Confirmed by Operator."
3.  **Outcome**: Parent accepts the fine. Argument resolved with data.

### Scenario 2: The Database Cleanup
**Situation**: 500 SMS failed last month. Costing money for nothing.
**Action**:
1.  Admin filters Status = "Failed" & Reason = "Invalid Number".
2.  Exports list of 50 students.
3.  **Outcome**: Class teachers are asked to get new numbers from these 50 students. Data quality improves.

### Scenario 3: The Emergency Check
**Situation**: "Riot in city. Bus 5 stuck." Emergency SMS sent.
**Action**:
1.  Transport Manager watches the **Live Delivery Dashboard**.
2.  Sees 48/50 Delivered. 2 Pending.
3.  **Outcome**: Manager personally calls the 2 parents whose delivery failed. Safety ensured.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **False Positive** | SMS says "Delivered" but phone was switched off. | **Limitation Awareness**: SMS "Delivery" means it reached the *CARRRIER*, not necessarily the *HANDSET* instantly. Use WhatsApp "Read Receipts" for higher certainty. |
| **Privacy Block** | Email "Open" tracking pixel is blocked by Gmail. | **Click Tracking**: Rely on "Link Clicks" (e.g., "Click to view circular") as a stronger signal of engagement than just "Open". |
| **DND Filters** | Status "Failed - DND". | **Route Switching**: Retry the message using the "Trans-scrub" route or Voice Call (IVR) which bypasses standard DND blocks for emergency alerts. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Message ID** | String | Gateway UUID. |
| **Recipient** | String | +91-98765xxxxx. |
| **Channel** | Enum | SMS, Email, WA. |
| **Status** | Enum | Delivered, Bounced, Failed. |
| **Cost** | Currency | ₹0.12 (Cost of this specific MSG). |
| **Latency** | Time | Time taken (Sent vs Delivered). |

## User Actions
1.  **Filter by Failed**: Show me only the problems.
2.  **Export Log**: Download 6-month history for Audit.
3.  **Check Balance**: View available SMS Credits.
4.  **Switch Gateway**: Toggle from Provider A to Provider B if A is slow.

## Best Practices
- **Auto-Clean**: If a number bounces > 3 times, auto-flag it as "Invalid" in the student profile.
- **Cost Analysis**: Weekly report showing "Spent ₹5000 on SMS, ₹2000 on Email".
- **Don't Obsess**: 100% delivery is impossible (phones off, out of network). Target >95%.
