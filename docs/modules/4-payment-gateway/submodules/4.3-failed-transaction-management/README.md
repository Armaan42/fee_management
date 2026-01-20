# 4.3 Failed Transaction Management

## Overview
**Failed Transaction Management** is the system's "investigation unit". Not all payment attempts succeed—sometimes the internet drops, banks decline cards, or parents close the browser too early. This submodule captures every failed attempt, categorizes the reason, and provides tools to clear the confusion.

### Real-World Analogy
Think of this as the **Lost and Found Department**.
Sometimes money leaves the parent's pocket (deducted from bank) but doesn't reach the school (receipt not generated). This module identifies these "lost" cases.
- **Lost Item (Failed Txn)**: We record it.
- **Investigation (Analysis)**: We check why it happened (Insufficient funds? Bank server down?).
- **Resolution**: Either the money is automatically returned to the parent (Refund), or we help it reach the destination (Reconciliation).

## Purpose
- **Analyze Failures**: Understand why payments are failing (Technical vs. User Error).
- **Handle Disputes**: Provide proof when a parent claims "I paid, but it failed".
- **Trigger Reversals**: Ensure failed deductions are refunded to parents by the gateway.
- **Improve Success Rates**: Identify frequent failure points (e.g., a specific bank gateway acting up).

## Key Features
- **Detailed Error Logs**: "Error Code: 05 - Do Not Honor" instead of just "Failed".
- **Auto-Reversal Status**: Track if the gateway has initiated a refund for a failed transaction.
- **Retry Mechanism**: Allow parents to retry payment immediately for "Soft Failures".
- **Status Sync**: Automated background check to see if a "Failed" transaction later turns into "Success".

## Real-World Scenarios

### Scenario 1: The "Insufficient Funds" Case
**Situation**: A parent tries to pay ₹50,000 but only has ₹40,000 in their account.
**Action**:
1.  Transaction fails immediately.
2.  **Failed Transaction Manager** logs the error: "Insufficient Funds".
3.  Parent sees a helpful message: "Your bank declined the transaction due to low balance. Please check your account."
**Outcome**: Parent knows exactly what went wrong and doesn't panic calling the school.

### Scenario 2: The "Network Timeout"
**Situation**: Parent enters OTP, but their internet disconnects before the success page loads.
**Action**:
1.  System logs status as "Pending" initially, then "Failed" after timeout.
2.  School Admin checks the log. Status says: "Client Connection Reset".
3.  Admin advises parent: "The payment didn't reach us. Please wait 15 mins to see if it reverses, then try again."
**Outcome**: Clear instruction prevents double payment.

### Scenario 3: Bank Downtime (Mass Failure)
**Situation**: Suddenly, all parents using SBI Netbanking are facing failures.
**Action**:
1.  Admin sorts the Failed List by "Bank".
2.  Sees 50 failures from "SBI" in the last hour.
3.  Error: "Bank System Unavailable".
**Outcome**: Admin disables SBI Netbanking option temporarily to prevent further frustration.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Ambiguous Failure** | Gateway returns generic "Something went wrong". | Classify as "Technical Error". Advise admin to check Gateway Dashboard for raw logs. |
| **Late Reversal** | Transaction failed, money deducted, auto-reversed after 3 days. | System should periodically poll for refund status (ARN) to update the record from "Failed" to "Refunded/Reversed". |
| **User Cancelled** | Parent clicked "Cancel" on the payment page. | Log as "User Aborted". Do not send "Payment Failed" alarmist emails; it was a voluntary action. |
| **Partial Deduction** | (Rare) Bank deducts amount but Gateway denies receipt. | Admin must flag this for "Manual Reconciliation". Provide "Transaction ID" to parent for bank complaint. |
| **Success after Failure** | Status changes from Failed to Success (Late callback). | Auto-convert status to "Success", generate receipt, and email the parent: "Good news, your payment went through!" |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Attempt ID** | String | Unique reference for this specific try. |
| **Failure Code** | String | Technical code from bank (e.g., `BAD_REQUEST`, `AUTH_DECLINED`). |
| **Failure Reason** | String | Human-readable explanation (e.g., "Incorrect OTP"). |
| **Bank Name** | String | Issuing bank of the card/account used. |
| **Is Refunded** | Boolean | Whether the money has been returned to source. |
| **User Browser** | String | Info on device used (Mobile/Desktop) - helpful for debugging. |

## User Actions
1.  **View Logs**: Read detailed failure reasons.
2.  **Retry Status**: Check if a failed transaction status has changed.
3.  **Mark Resolved**: Manually close a ticket if the parent has successfully paid via another method.
4.  **Send Report**: Email failure details to the payment gateway support team.

## Best Practices
- **Transparent Messaging**: Show parents the *actual* reason (e.g., "Wrong OTP") so they can fix it, rather than a generic "Error".
- **Don't Delete**: Keep failed logs for at least 6 months. They are crucial evidence for chargeback disputes.
- **Proactive Support**: If a High Value transaction fails, call the parent to offer help (e.g., "Do you want to make a partial payment instead?").
