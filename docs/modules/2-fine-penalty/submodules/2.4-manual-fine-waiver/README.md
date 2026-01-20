# 2.4 Manual Fine Waiver

## Overview
**Manual Fine Waiver** acts as the "Manager Override" in the system. Sometimes, despite all the automated rules, you need to remove a fine for a specific student due to exceptional circumstances (e.g., technical glitches, humanitarian grounds, or a deal struck with a parent). This module provides the interface for authorised personnel to manually intervene and clear late fees.

**In simple terms**: It allows the Principal or Admin to say, "I know the system added a ₹500 fine, but remove it for this student."

**Analogy**: 
-   **Store Manager**: The cashier cannot change the price, but the Manager can use their "Key" to void an item or give a discount.
-   **School Admin**: Uses this module to void a fine that the system automatically calculated.

## Purpose
To handle edge cases and human factors that automated logic cannot predict, providing flexibility in fee collection.

## Description
This submodule allows admins to select a student, view their pending fines, and partially or fully waive them. It mandates a "Reason" for every waiver to maintain an audit trail and prevent misuse.

## Key Features
-   **Full Waiver**: Remove 100% of the fine amount.
-   **Partial Waiver**: Waive ₹200 out of a ₹500 fine.
-   **Reason Codes**: Select from standard reasons (Medical, Error, Other).
-   **Approval Workflow**: Lower-level admins can request a waiver; Higher-level admins approve it.
-   **Audit Log**: Tracks who waived what, when, and why.

## Real-World Scenarios

### Scenario 1: The "Forgotten Password" Excuse
**Background**: Parent claims they couldn't login to pay on the due date because the password reset wasn't working.
**Action**: Principal agrees to waive the ₹100 fine as a one-time gesture.
**Step**: Admin searches student -> Selects Fine -> Clicks "Waive" -> Reason: "Technical Issue".

### Scenario 2: Cashier Data Entry Delay
**Background**: Parent paid Cash on the Due Date. Cashier entered it into the system 2 days late. System auto-added fine.
**Action**: Admin waives the fine because the parent is not at fault.
**Reason**: "Administrative Error".

### Scenario 3: Settlement Negotiation
**Background**: A parent has ₹50,000 pending arrears + ₹5,000 accumulated fines. They offer to pay the full ₹50,000 immediately if the fine is waived.
**Action**: Management accepts. Admin waives ₹5,000 fine.
**Result**: School recovers the principal amount.

### Scenario 4: Post-Facto Correction
**Background**: A fine was charged last month. Parent complains today and proves they paid on time (bank receipt shown).
**Action**: Admin must reverse the fine.
**Result**: The student's ledger is corrected.

### Scenario 5: Partial Relief
**Background**: Fine is ₹2,000. Parent is financially struggling.
**Action**: Principal agrees to "meet halfway". Waives ₹1,000. Parent pays remaining ₹1,000.

## Edge Cases & How to Handle Them

### Edge Case 1: Waiving an Already Paid Fine
**What Happens**: Parent paid ₹500 fine. Later gets a waiver.
**System Behavior**: 
-   **Option A**: Create a "Credit" of ₹500 in student account (adjustable against next month).
-   **Option B**: Refund the money (Complex process).
**How to Handle**: Use Option A (Credit Adjustment) as standard practice.

### Edge Case 2: Waiver Limits
**What Happens**: Junior Clerk tries to waive ₹10,000 fine.
**System Behavior**: System blocks it. Limit for Clerk is ₹500.
**How to Handle**: Role-based limits preventing fraud.

### Edge Case 3: Re-applying Fine after Waiver
**What Happens**: Admin waived fine by mistake. Wants to undo the waiver.
**System Behavior**: "Delete Waiver" action.
**How to Handle**: System re-calculates the fine as if the waiver never happened.

### Edge Case 4: Waiver > Fine Amount
**What Happens**: Fine is ₹500. Admin types ₹600 in waiver amount.
**System Behavior**: 
-   Error: "Waiver cannot exceed Fine Amount".
-   Ledger: ₹-100 (Negative fine?).
**How to Handle**: Strictly block waivers larger than the due fine.

### Edge Case 5: "Other" Reason Abuse
**What Happens**: Admin selects "Other" and types "." to bypass mandatory explanation.
**System Behavior**: Audit trail becomes useless.
**How to Handle**: Enforce minimum character limit (e.g., 10 chars) for remarks.

### Edge Case 6: Pending Approval
**What Happens**: Clerk requests waiver. Principal is on leave. Parent is standing at counter.
**System Behavior**: Status = "Pending Approval". Cannot collect fee yet?
**How to Handle**: Parent pays Principal Amount. Fine remains pending until approved/rejected.

### Edge Case 7: Bulk Waiver (Crisis Management)
**What Happens**: 50 students stuck in School Bus breakdown, couldn't reach bank.
**System Behavior**: Need to waive for all 50.
**How to Handle**: Batch operation to apply waiver to a list of IDs.

### Edge Case 8: Notification Trigger
**What Happens**: Waiver applied. Parent doesn't know.
**System Behavior**: Parent pays full amount online.
**How to Handle**: SMS/Email: "Your fine of ₹100 has been waived. Please pay balance."

### Edge Case 9: Fine Recalculation Override
**What Happens**: Fine is daily (₹10/day). Admin waives ₹50 (5 days).
**System Behavior**: Does the fine stop growing?
**How to Handle**: Usually, a waiver just pays off the *current* balance. If they still don't pay the principal, new fines might reappear tomorrow (unless "Freeze Fine" is used).

### Edge Case 10: Waiving Mandatory Fines
**What Happens**: Some fines are "Strict" (e.g., Cheque Bounce Charge).
**System Behavior**: System might block manual waiver for these specific fine heads.
**How to Handle**: Mark certain fines as "Non-Waivable" in configuration.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Student | Lookup | Yes | Who gets the waiver |
| Fine Entry | Dropdown | Yes | Specific fine transaction ID |
| Waiver Amount | Currency | Yes | How much to remove |
| Waiver Type | Dropdown | Yes | Full / Partial |
| Reason Category | Dropdown | Yes | Error / Medical / Special |
| Remarks | Text | Yes | Detailed explanation |
| Approval Status | Enum | Yes | Pending / Approved / Rejected |

## User Actions
1.  **Search**: Find student ledger.
2.  **Select**: Identify the specific fine line item.
3.  **Waive**: Input amount and reason.
4.  **Confirm**: Submit for processing.

## Business Rules
-   Waivers are considered "Expense" or "Revenue Loss" in accounting.
-   Cannot waive a fine that hasn't been generated yet (Prevention).

## Permissions Required
-   **Request Waiver**: Fee Clerk.
-   **Approve Waiver**: Principal, Fee Admin.

## Related Submodules
-   **2.1 Fine Rules**: Creates the fine.
-   **7.1 Reports**: "Waiver Report" is critical for auditing.

## API Endpoints
```
POST /api/fine-waivers - Create waiver request
PUT /api/fine-waivers/:id/approve - Approve
PUT /api/fine-waivers/:id/reject - Reject
```

## Database Schema
```sql
Table: fine_waivers
- id (PK)
- student_id (FK)
- fine_transaction_id (FK)
- amount (DECIMAL)
- reason_code (VARCHAR)
- remarks (TEXT)
- approved_by (FK)
- status (ENUM)
```

## UI/UX Considerations
-   **Red Warning**: "You are about to waive ₹5,000. This action is logged."
-   **Success Message**: "Fine successfully removed. New Balance: ₹45,000."

## Best Practices
1.  **Zero Tolerance on "Other"**: Regular audits of "Other" reasons to ensure staff aren't hiding unjustified waivers.
2.  **Two-Level Auth**: Always require a second pair of eyes for waivers above ₹1,000.
3.  **Receipt**: Issue a "Waiver Receipt" or Credit Note so the parent has proof.
