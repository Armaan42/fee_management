# 4.2 Real-time Transaction Monitor

## Overview
The **Real-time Transaction Monitor** is your live dashboard for watching all online fee payments as they happen. It gives you immediate visibility into which payments are successful, which failed, and which are still "processing" at the bank.

### Real-World Analogy
Think of this as the **Flight Arrival/Departure Board** at an airport.
- **Departed (Pending)**: The payment has left the school system and is en route to the bank.
- **Landed (Success)**: The payment successfully arrived at the bank destination.
- **Cancelled (Failed)**: The flight couldn't take off or land (insufficient funds, wrong OTP).
Just as airport staff monitor the board to help passengers, school admins monitor this screen to help parents with payment queries.

## Purpose
- **Live Visibility**: Track payment attempts the moment a parent clicks "Pay".
- **Instant Troubleshooting**: Quickly answer parents asking "Did my payment go through?".
- **Status Reconciliation**: Manually check payments that got stuck midway.
- **Failure Analysis**: Identify if many payments are failing due to a specific reason (e.g., bank downtime).

## Key Features
- **Live Feed**: Auto-refreshing list of transactions.
- **Status Indicators**: Color-coded badges (Green: Success, Red: Failed, Yellow: Pending/Created).
- **Search & Filter**: Find transactions by Student Name, Order ID, or Date.
- **Verification Button**: "Force Check" status with the gateway for stuck payments.
- **Detailed Logs**: View technical error messages for IT support.

## Real-World Scenarios

### Scenario 1: The "Deadline Day" Rush
**Situation**: It's the last day to pay fees, and hundreds of parents are paying simultaneously.
**Action**:
1.  Admin keeps the **Transaction Monitor** open on a secondary screen.
2.  Watches the feed to ensure "Success" counts are rising.
3.  Spots a cluster of "Failures" from a specific bank.
**Outcome**: Proactively puts a notice on the school app: "HDFC Bank servers are facing issues, please use other cards."

### Scenario 2: "Money Deducted, Receipt Not Received"
**Situation**: A worried parent calls saying money was cut from their account, but they didn't get a receipt.
**Action**:
1.  Admin searches the student's name in the Monitor.
2.  Finds the transaction showing "Pending" or "Authorized" (not yet Captured).
3.  Clicks the **"Verify Status"** button.
**Outcome**: The system pings the gateway, confirms the money was received, updates the status to "Success", and auto-generates the receipt.

### Scenario 3: Investigating Repeated Failures
**Situation**: One parent tries to pay 5 times and fails every time.
**Action**:
1.  Admin filters by the student's ID.
2.  Clicks "View Details" on the failed rows.
3.  Sees the error: "Insufficient Funds" or "Do Not Honor".
**Outcome**: Admin advises the parent to check their bank balance or card limits.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Stuck in Pending** | Transaction shows "Pending" for > 30 minutes. | Admin uses "Verify Status" button. If still pending, advise parent to wait 24 hours (bank reconciliation window). |
| **Late Webhook** | Payment succeeds at 10:00 AM, but "Success" signal arrives at 12:00 PM. | System auto-updates status upon receipt. No action needed, but Receipt timestamp will match the update time. |
| **Double Success** | Gateway sends two success signals for the same Order ID. | System checks if Order ID is already marked "Success". If yes, ignore the duplicate signal to prevent double receipt generation. |
| **Gateway Down** | All transactions showing "Created" but never "Success". | High probability of gateway outage. Contact Gateway Support and notify parents to pause payments. |
| **User Aborted** | Parent closes the browser window at the OTP page. | Transaction remains "Created" or "Pending" effectively forever. System auto-marks these as "Failed/Aborted" after 24 hours. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Transaction ID** | String | Unique ID from the Payment Gateway (e.g., `pay_Hq8...`). |
| **Order ID** | String | Detailed Order reference number (e.g., `order_98s...`). |
| **Student Name** | String | Name of the student for whom fees are being paid. |
| **Amount** | Currency | The total amount attempted. |
| **Status** | Status | Current state: `Created`, `Authorized`, `Captured`, `Failed`, `Refunded`. |
| **Method** | String | Payment mode used (Card, UPI, Netbanking). |
| **Date & Time** | DateTime | Exact timestamp of the attempt. |
| **Error Message** | String | Technical reason for failure (visible on hover/details). |

## User Actions
1.  **Monitor Feed**: Watch the list update in real-time.
2.  **Filter**: Narrow down to specific dates or statuses (e.g., "Show all Failed today").
3.  **Verify Status**: Manually sync status with the gateway.
4.  **View Details**: Expand a row to see full JSON logs.
5.  **Export Log**: Download the day's transaction history for offline analysis.

## Best Practices
- **Don't Panic on "Pending"**: Most pending transactions resolve themselves within minutes.
- **Verify Before Repaying**: Always check the monitor before asking a parent to try paying again to avoid double payments.
- **Regular Checks**: Review the "Failed" list daily to spot any systemic issues.
