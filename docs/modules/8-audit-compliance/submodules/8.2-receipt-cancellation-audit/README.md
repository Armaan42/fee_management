# 8.2 Receipt Cancellation Audit

## Overview
**Receipt Cancellation Audit** is the safety valve of the collection system. It manages the delicate process of invalidating a transaction that has already been recorded. It ensures that "undoing" a transaction doesn't create a "black hole" in the accounts where money disappears without a trace.

### Real-World Analogy
Think of this as **Voiding a Tax Invoice**.
In a shop, if a cashier makes a mistake, they cannot simply use an eraser or throw the bill in the dustbin.
1.  They must take a red pen.
2.  Write **"VOID"** across the bill.
3.  Staple it to the carbon copy.
4.  File it for the auditor.
This module does exactly that digitally. The receipt isn't deleted; it's marked "Cancelled", ensuring the receipt number sequence (101, 102, 103...) remains broken but accounted for.

## Purpose
- **Prevent Skimming**: A common fraud is to print a receipt, give it to the parent, take the cash, and then delete the receipt. This module makes deletion impossible—only "Cancellation" is allowed, which leaves a visible scar on the ledger.
- **Maintain Sequence**: Ensure that Receipt #105 is followed by #106. If #105 is cancelled, it still exists in the database as a "Dead" record to prove no one stole the blank receipt paper.
- **Reverse Accounting**: Automatically undo the financial impact—Debit the Cash Account and Credit the Student Due Account.

## Key Features
- **Mandatory Reason**: Forces the user to select *why* they are cancelling (e.g., "Wrong Amount", "Cheque Bounce").
- **Supervisor Approval**: Optionally requires a Manager's OTP or approval click to authorize a cancellation.
- **Restoration**: Automatically adds the fee amount back to the student's "Pending Dues" so it's not lost.
- **Watermarking**: Overlays a "CANCELLED" watermark on the digital PDF of the receipt.

## Real-World Scenarios

### Scenario 1: The "Fat Finger" Error
**Situation**: Accountant intended to collect ₹500 but typed ₹5000.
**Action**:
1.  Clicks **"Cancel Receipt"** on the wrong entry.
2.  Selects Reason: "Data Entry Error".
3.  System updates status to "Cancelled".
4.  System restores ₹5000 to the "Fee Due" bucket.
5.  **Outcome**: Accountant creates a fresh receipt for ₹500.

### Scenario 2: The Dishonoured Cheque
**Situation**: A receipt was issued for a cheque of ₹10,000. The bank returned it unpaid.
**Action**:
1.  Accountant locates the receipt using Cheque Number.
2.  Selects Reason: **"Cheque Dishonoured"**.
3.  System cancels the receipt.
4.  System adds ₹10,000 + ₹500 (Bounce Penalty) to the student's dues.
5.  **Outcome**: The student is a defaulter again.

### Scenario 3: The Cancelled Refund
**Situation**: A parent paid fees, then withdrew admission 2 days later and asked for the money back.
**Action**:
1.  **Do NOT Cancel**. This is a valid transaction followed by a refund.
2.  Issue a separate **"Refund Voucher"**.
3.  **Rule**: "Cancellation" is for mistakes. "Refund" is for returns. They are different.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Partial Cancellation** | A receipt has Tuition + Transport. I only want to cancel Transport. | **Not Allowed**. You must cancel the *entire* receipt and issue a new split receipt. Partial voids cause severe accounting mismatches. |
| **Closed Financial Year** | Trying to cancel a receipt from March 2023 in April 2024. | **Block Action**: "Financial Year Closed". You must pass a "Credit Note" (Adjustment) in the *current* year instead of changing history. |
| **Shift Separation** | Cashier A collected. Shift ended. Manager B tries to cancel it. | **Warning**: "You are cancelling a receipt collected by another user." Requires Supervisor privileges. |
| **System Down** | Internet cut while cancelling. | **Atomic Transaction**: The database ensures either *all* steps (Status update + Ledger Reversal) happen, or *none* happen. No half-cancelled states. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Receipt No** | String | The ID of the voided record. |
| **Original Amount** | Currency | Value before voiding. |
| **Cancelled By** | User | Who initiated the void. |
| **Approved By** | User | Manager who authorized it. |
| **Reason Code** | Enum | Error, Bounce, Duplicate. |
| **Comments** | Text | "Parent requested change of mode". |
| **Reverse Txn ID** | String | ID of the contra-entry in ledger. |

## User Actions
1.  **Request Cancellation**: Submit a request (if lacking perm).
2.  **Approve/Reject**: Manager reviews the queue.
3.  **View Cancelled List**: Report of all voided bills today.
4.  **Reprint Cancelled**: Print a copy with the "Void" stamp for the file.

## Best Practices
- **Never Delete**: As a rule, `DELETE FROM receipts` is forbidden. Use `UPDATE receipts SET status='CANCELLED'`.
- **Notify Parents**: Send an auto-SMS: "Your receipt #123 has been cancelled. If you did not authorize this, contact School." This prevents fraud.
- **Monitor Ratios**: If a cashier cancels >5% of their receipts, investigate for training issues or fraud.
