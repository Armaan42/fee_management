# 3.6 Receipt Cancellation

## Overview
**Receipt Cancellation** is a critical financial control feature. Humans make mistakes—selecting the wrong student, entering the wrong amount, or accepting a cheque that later bounces. In accounting, you cannot simply "delete" a record as if it never happened. Instead, you must "Cancel" or "Void" it to reverse the transaction while keeping an audit trail of the error.

**In simple terms**: It's like tearing up a cheque. You don't just throw it away; you cross it out and write "VOID" so everyone knows it's invalid.

**Analogy**: 
-   **Invoicing**: If you send an invoice with a typo, you issue a "Credit Note" or cancel the invoice. You don't use whiteout to erase the numbers in the ledger.

## Purpose
To rectify invalid or erroneously generated fee receipts while maintaining a transparent audit log and correcting the student's due balance.

## Description
This submodule allows authorized admins to search for a specific receipt and mark it as Cancelled. The system automatically reverses the financial impact (e.g., re-opening the "Due" amount for the student) and logs the reason for cancellation.

## Key Features
-   **Full Reversal**: Instantly adds the cancelled amount back to the "Total Due".
-   **Mandatory Remarks**: Forces the user to explain *why* it is being cancelled.
-   **Audit Log**: Tracks Who, When, and Why.
-   **Cheque Bounce Integration**: Dedicated workflow for cancelling receipts due to dishonored cheques.
-   **SMS Alert**: Notifies parent that the payment has been reversed.

## Real-World Scenarios

### Scenario 1: Wrong Student Selected
**Background**: Cashier collected ₹5,000. In a hurry, selected "John (Class 5)" but the money was actually from "John (Class 6)".
**Action**:
1.  Cancel Receipt for John (Class 5).
2.  Generate new Receipt for John (Class 6).
**Result**: John (Class 5) shows ₹5,000 Due again. John (Class 6) shows Paid.

### Scenario 2: Cheque Bounce
**Background**: Receipt #105 was issued for a Cheque. Bank returned it unpaid.
**Action**: Admin cancels Receipt #105 with reason "Cheque Bounced".
**System Behavior**: Tuition Fee becomes "Overdue" again. A "Cheque Bounce Fine" is added.

### Scenario 3: Typing Error (Extra Zero)
**Background**: Fee was ₹500. Cashier entered ₹5,000.
**Action**: Immediate cancellation required to fix the Daily Cash Report.
**Result**: Ledger corrected.

### Scenario 4: Policy Change (Backdated Waiver)
**Background**: Parent paid fee. Principal later grants a scholarship valid from start of year.
**Action**: Cancel the paid receipt -> Apply Scholarship -> Re-take payment (if any balance remains).

### Scenario 5: Duplicate Entry
**Background**: Internet lag caused "Save" to be clicked twice. Two identical receipts generated.
**Action**: Cancel one of them as "Duplicate Entry".

## Edge Cases & Handling

### Edge Case 1: Cancelled after Day End
**What Happens**: Cashier realizes mistake next day. Cash already deposited in bank.
**System Behavior**: System allows cancellation.
**How to Handle**: Accountant interprets this as a "Withdrawal" from collected funds in the next reconciliation.

### Edge Case 2: Partial Cancellation
**What Happens**: Receipt has Tuition (₹5k) + Bus (₹2k). Refund only Bus.
**System Behavior**: Cannot cancel half a receipt.
**How to Handle**: Cancel Full Receipt (₹7k). Create new Receipt for Tuition (₹5k).

### Edge Case 3: Linked Advance
**What Happens**: Receipt was paid using ₹500 from Advance Wallet.
**System Behavior**: Choosing to cancel the receipt.
**How to Handle**: The ₹500 must be *credited back* to the Advance Wallet automatically.

### Edge Case 4: SMS Panic
**What Happens**: Parent gets SMS "Payment Cancelled". Thinks money is stolen.
**System Behavior**: Valid concern.
**How to Handle**: SMS Template: "Receipt #123 cancelled due to admin error. Please ignore/Contact office."

### Edge Case 5: Tax Reversal
**What Happens**: GST was applicable on the fee.
**System Behavior**: Government tax liability created.
**How to Handle**: System creates a "Credit Note" to reverse the GST liability in accounting reports.

### Edge Case 6: Archived Year
**What Happens**: Trying to cancel a receipt from 2021 in 2024.
**System Behavior**: Financial year closed.
**How to Handle**: Strictly block. Use "Refund" or "Journal Entry" instead.

### Edge Case 7: Re-using Receipt No
**What Happens**: Cancel Receipt #101. Next receipt generated is #102.
**System Behavior**: Gap in sequence (#100, #102).
**How to Handle**: Accepted accounting practice. Do *not* reuse #101. The voided record #101 should appear in reports as "Cancelled".

### Edge Case 8: Approval Workflow
**What Happens**: Cashier tries to cancel a high-value receipt (₹1 Lakh) to steal cash.
**System Behavior**: Fraud risk.
**How to Handle**: Receipts > ₹10k require OTP/Approval from Manager to cancel.

### Edge Case 9: Refund vs Cancellation
**What Happens**: Parent wants money back because student is leaving.
**System Behavior**: Admin cancels receipt.
**How to Handle**: Wrong approach. Use "Refund Process". Cancellation implies the transaction *never happened*. Refund implies it happened but is returned.

### Edge Case 10: Cash Drawer Impact
**What Happens**: Cancelling a cash receipt.
**System Behavior**: Does "Expected Cash in Drawer" decrease?
**How to Handle**: Yes, immediately updates the "Cash in Hand" tile on dashboard.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Receipt No | Lookup | Yes | Target to void |
| Reason | Dropdown | Yes | Wrong Entry / Bounce / Duplicate |
| Remarks | Text | Yes | "Correcting error by Staff X" |
| Cancelled By | User | Auto | Audit trail |
| Date | Date | Auto | Timestamp of cancellation |

## User Actions
1.  **Search**: Find receipt.
2.  **View**: Verify details.
3.  **Cancel**: Click button -> Enter Reason.
4.  **Confirm**: "Are you sure? This cannot be undone."

## Business Rules
-   Cancelled receipts remain in the database with status = CANCELLED.
-   Cannot cancel a receipt that has already been "Reconciled" with Bank Statement (unless unreconciled first).

## Permissions Required
-   **Cancel Receipt**: Fee Manager / Principal.
-   **Cancel Own Entry**: Cashier (within same day only).

## Related Submodules
-   **3.1 Quick Receipt**: The source of the receipt.
-   **3.8 Refund Processing**: The alternative to cancellation.

## API Endpoints
```
PUT /api/fee-receipts/:id/cancel - Execute cancellation
GET /api/reports/cancelled-receipts - Audit list
```

## Database Schema
```sql
Table: fee_receipts
- status (PAID/CANCELLED)
- cancellation_reason (TEXT)
- cancelled_at (TIMESTAMP)
- cancelled_by (FK)
```

## UI/UX Considerations
-   **Strikethrough**: Display cancelled receipts in lists with a ~~strikethrough~~ style.
-   **Red Label**: Explicit "CANCELLED" stamp on the view screen.

## Best Practices
1.  **Strict Reasons**: Disable free-text "Other" reasons if possible. Force users to categorize mistakes.
2.  **Notification**: Always notify the Super Admin via email for cancellations > ₹10,000.
3.  **Physical Receipt**: If the parent has the physical receipt, ask them to return it or write "CANCELLED" on school copy to prevent future disputes.
