# 3.8 Refund Processing

## Overview
**Refund Processing** handles the outflow of money from the school back to the parent. Whether it's returning a security deposit, correcting an overpayment, or refunding fees due to admission withdrawal, this module ensures the payout is recorded, approved, and accounted for correctly.

**In simple terms**: It's the "Returns Counter" at a store. If you returned the item (or left the school), you get your money back.

**Analogy**: 
-   **Security Deposit**: Like getting your rental bond back when you vacate an apartment.

## Purpose
To manage legitimate financial returns while preventing leakage, fraud, or unauthorized payouts.

## Description
This submodule allows users to initiate a refund request against a student account. It supports refunding specific fee heads (e.g., Caution Money) or general excess balances. It typically involves an approval workflow to ensure the Principal or Accountant signs off before cash is released.

## Key Features
-   **Source Linking**: Link refund to the original receipt (Proof of original payment).
-   **Approval Workflow**: Cashier requests -> Manager approves -> Accountant pays.
-   **Mode of Refund**: Cash, Cheque, or Bank Transfer.
-   **Partial Refund**: Returning only a portion of the original amount.
-   **Refund Receipt**: Generates a "Payment Voucher" for the parent to sign.

## Real-World Scenarios

### Scenario 1: Excess Payment (Double Click)
**Background**: Parent paid ₹10,000 online. System glitch debited bank twice.
**Action**: School verifies double credit. Initiates refund of ₹10,000.
**Result**: Ledger corrected.

### Scenario 2: Security Deposit Return
**Background**: Student graduated Class 12. Leaving school.
**Action**: Admin checks "Caution Money" balance (₹5,000). Processes refund.
**Result**: Student account closed.

### Scenario 3: Scholarship Retroactive
**Background**: Parent paid Full Fee in April. Student won a sports scholarship in May (50% waver).
**Action**:
1.  Apply Scholarship (Credit Note).
2.  Account has "Excess Balance" of ₹15,000.
3.  Process Refund of ₹15,000 to parent.

### Scenario 4: Trip Cancellation
**Background**: School Trip (₹2,000 per head) cancelled due to bad weather.
**Action**: Bulk refund initiated for all 50 students. Money moved to "Advance Wallet" or refunded in Cash.

### Scenario 5: Admission Withdrawal
**Background**: Parent paid admission fee but got transferred to another city within 1 week.
**Action**: As per policy, refund 90% of fee. Deduct 10% as processing charge.

## Edge Cases & Handling

### Edge Case 1: Refund > Amount Paid
**What Happens**: Receipt was ₹5,000. Admin tries to refund ₹6,000.
**System Behavior**: Fraud risk.
**How to Handle**: Validation: Refund Amount <= (Original Receipt Amount - Already Refunded Amount).

### Edge Case 2: Mode Mismatch
**What Happens**: Parent paid Cash. Wants refund via Online Transfer.
**System Behavior**: Allowed, but audit trail matches "Cash In" to "Bank Out".
**How to Handle**: Require "Bank Account Details" input for online refunds.

### Edge Case 3: Cheque Bounce Risk
**What Happens**: Parent paid via Cheque yesterday. Requests refund today. Cheque hasn't cleared yet.
**System Behavior**: Risk: Cheque might bounce tomorrow.
**How to Handle**: Block refunds on "Uncleared" receipts. Wait for clearance (3-5 days).

### Edge Case 4: Tax Reversal (GST)
**What Happens**: Original fee included ₹180 GST. Refund is occurring.
**System Behavior**: School already paid tax to Govt.
**How to Handle**: refund the *Gross* amount? Or issue Credit Note for GST? usually, refund full amount and adjust GST liability in next filing.

### Edge Case 5: Refund from Advance Wallet
**What Happens**: Parent has ₹5,000 in Advance. Wants it back.
**System Behavior**: No specific receipt linked.
**How to Handle**: "Wallet Refund" transaction type.

### Edge Case 6: Cash Availability
**What Happens**: Refund ₹20,000 in Cash. Drawer only has ₹5,000.
**System Behavior**: Cashier cannot pay.
**How to Handle**: Check "Cash in Hand" before approving cash refund. Issue Cheque for large amounts.

### Edge Case 7: Approval Chain
**What Happens**: Junior Clerk processes refund to their own pocket.
**System Behavior**: Theft.
**How to Handle**: Mandatory: Refunds > ₹0 require Manager approval.

### Edge Case 8: Bank Reconciliation
**What Happens**: Refund Cheque issued. Parent hasn't encashed it for 3 months.
**System Behavior**: Money still in school account but booked as expense.
**How to Handle**: "Unpresented Cheque" report.

### Edge Case 9: Partial Refund Logic
**What Happens**: Refund ₹500 against a ₹2000 receipt.
**System Behavior**: Receipt status becomes "Partially Refunded".
**How to Handle**: Update ledger to show remaining valid payment is ₹1500.

### Edge Case 10: Formatting Receipt
**What Happens**: Parent needs proof of refund.
**System Behavior**: Generate "Refund Voucher".
**How to Handle**: Print voucher -> Get Parent Signature -> File it.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Student | Lookup | Yes | Recipient |
| Amount | Currency | Yes | Payout |
| Mode | Dropdown | Yes | Cash/Cheque/Transfer |
| Reason | Text | Yes | "Withdrawal", "Excess" |
| Source Receipt | Link | No | Optional linkage |
| Approved By | User | Auto | Manager ID |

## User Actions
1.  **Search**: Find Student/Receipt.
2.  **Request Refund**: Enter Amount & Reason.
3.  **Approve**: Manager logs in to approve.
4.  **Disburse**: Cashier pays out.

## Business Rules
-   Refunds are "Expenses" or "Revenue Reversals".
-   Refund date must be Today. Cannot backdate a refund.

## Permissions Required
-   **Request**: Fee Cashier.
-   **Approve**: Principal / Trustee.

## Related Submodules
-   **3.6 Cancellation**: Reverses the *record*. Refund reverses the *cash*.
-   **3.3 Advance Payment**: Often the source of refunds.

## API Endpoints
```
POST /api/refunds/request - Initiate
POST /api/refunds/:id/approve - Authorize
POST /api/refunds/:id/pay - Record payout
```

## Database Schema
```sql
Table: refunds
- id (PK)
- student_id (FK)
- amount (DECIMAL)
- status (REQUESTED/APPROVED/PAID)
- mode (ENUM)
- reference_no (VARCHAR)
```

## UI/UX Considerations
-   **Warning Color**: Use Red/Orange for Refund buttons to indicate cash outflow.
-   **Signature Box**: Space on the printed voucher for "Receiver's Signature".

## Best Practices
1.  **No Cash Refunds > ₹X**: Policy to always use Cheque/NEFT for refunds above ₹2,000 to leave a bank trail.
2.  **Document Proof**: Attach "Application for Withdrawal" doc to the refund record.
3.  **Notification**: SMS Parent: "Refund of ₹X processed successfully."
