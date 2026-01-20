# 5.3 Cheque Clearance Tracking

## Overview
**Cheque Clearance Tracking** manages the lifecycle of check payments. Unlike cash, a cheque is just a promise of payment. This module tracks that promise from the moment it's handed over at the fee counter until the money safely lands in the school's bank account.

### Real-World Analogy
Think of this as **Courier Packet Tracking**.
When you send a parcel, you track its status: `Picked Up` -> `In Transit` -> `Delivered` (or `Returned`).
Similarly, a cheque moves through distinct stages:
1.  **Collected**: Parent hands it over (Packet Picked Up).
2.  **Deposited**: Admin sends it to the bank (In Transit).
3.  **Appearing**: Bank acknowledges receipt (Out for Delivery).
4.  **Cleared**: Money is in the account (Delivered).
5.  **Bounced**: Bank rejects it (Return to Sender).

## Purpose
- **Visibility**: Know exactly how much money is "stuck" in the clearing pipeline.
- **Aging Analysis**: Identify cheques that haven't cleared even after 5 days.
- **Bounce Management**: Automate the penalty and reversal process for failed cheques.
- **Bulk Processing**: Update the status of 50 cheques at once using the bank's deposit slip.

## Key Features
- **Deposit Slip Generation**: Create a printable list of cheques for the bank teller.
- **Status Dashboard**: Visual pipeline showing Count/Value at each stage (Collected, Deposited, Cleared, Bounced).
- **Bulk Status Update**: Mark multiple cheques as "Cleared" in one click.
- **Bounce Workflow**: One-click action to reverse fee payment and apply "Cheque Bounce Fine".

## Real-World Scenarios

### Scenario 1: The Daily Deposit
**Situation**: The cashier has collected 25 cheques today.
**Action**:
1.  Admin goes to **Cheque Deposit**.
2.  Selects all "Collected" cheques.
3.  Clicks **"Generate Pay-in Slip"**.
4.  System updates status of all 25 cheques to **"Deposited"**.
5.  Admin prints the slip and sends the peon to the bank.
**Outcome**: System knows these cheques are now at the bank.

### Scenario 2: Marking Clearance
**Situation**: 3 days later, the admin checks the bank statement online.
**Action**:
1.  Admin opens **Cheque Clearance**.
2.  Filters by "Deposited".
3.  Matches the amounts with the bank statement.
4.  Selects the 20 cleared cheques and clicks **"Mark as Cleared"**.
**Outcome**: The students' ledgers are finalized, and the money is available for use.

### Scenario 3: The Bounce
**Situation**: One cheque for ₹15,000 returns due to "Insufficient Funds".
**Action**:
1.  Admin finds the cheque and clicks **"Mark as Bounced"**.
2.  System prompts: "Apply Penalty?". Admin selects "Yes" (Standard ₹500 fine).
3.  **Result**:
    -   Fee Receipt is cancelled.
    -   ₹15,000 is added back to Student Dues.
    -   ₹500 Fine is added to Student Dues.
    -   SMS sent to Parent: "Your cheque bounced. Please pay ₹15,500 immediately."
**Outcome**: Full accounting reversal automation in seconds.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Outstation Cheque** | Cheque from a different state takes 7 days to clear. | Flag as "Outstation" to exclude it from the "Delayed Clearance" alert report (which usually alerts after 3 days). |
| **Lost Cheque** | Bank loses the physical slip before processing. | Mark status as **"Lost/Void"**. Ask parent for a replacement cheque or online payment. |
| **Partial Clearance** | (Rare) Bank clears only part of the value (Corporate limits). | System doesn't support partial cheque clearance. Mark as Bounced, then accept partial payment via other modes. |
| **Mistaken Inputs** | Admin marked a bounced cheque as "Cleared" by accident. | "Revert Status" button allows moving a cheque back to the previous stage (with Audit Log entry). |
| **Stale Cheque** | Admin forgot to deposit cheque for 3 months. | System auto-flags "Collected" cheques > 90 days old as **"Stale/Expired"** and prevents deposit slip generation. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Cheque No** | String | 6-digit number on the cheque. |
| **Cheque Date** | Date | The date written on the leaf. |
| **Bank Name** | String | Issuing bank (e.g., HDFC, SBI). |
| **Deposit Date** | Date | When it was sent to the school's bank. |
| **Clearance Date** | Date | When money hit the account. |
| **Current Status** | Enum | `Collected`, `Deposited`, `Cleared`, `Bounced`, `Returned`, `Lost`. |

## User Actions
1.  **Generate Slip**: Group cheques into a Batch for deposit.
2.  **Update Status**: Move cheques through the lifecycle stages.
3.  **Manage Bounces**: Trigger the reversal/penalty workflow.
4.  **Search**: Find a cheque by number or parent name.

## Best Practices
- **Deposit Daily**: Don't hoard cheques. Deposit them daily to ensure constant cash flow.
- **Verify Name**: Check "Cheque Date" and "Payee Name" at the counter itself to prevent immediate rejection.
- **Wait for Clearance**: Never mark a cheque as "Cleared" until you see it in the bank statement. Creating a receipt is not the same as Money in Bank.
