# 3.2 Partial Payment Processing

## Overview
**Partial Payment Processing** allows parents to pay a portion of the due fees when they cannot afford to pay the full amount at once. Instead of rejecting the payment, the system accepts what is being paid and keeps the remainder as a "Balance Due" for the future.

**In simple terms**: It's like paying ₹200 now for a ₹500 bill, and promising to pay the remaining ₹300 next week.

**Analogy**: 
-   **Layaway / EMI**: You pay a down payment to secure the service (schooling), and pay the rest in smaller chunks. The system tracks exactly how much is left.

## Purpose
To increase fee collection efficiency by accepting whatever cash flow is available, rather than demanding "All or Nothing".

## Description
This submodule manages the acceptance of partial sums against specific fee heads. It handles proper allocation (e.g., clearing the Tuition Fee first, then the Bus Fee), updates the outstanding balance, and ensures the next receipt reflects the correct pending amount.

## Key Features
-   **Custom Amount Entry**: Cashier types in the exact amount received (e.g., ₹4000 instead of ₹5000).
-   **Auto-Allocation**: System decides which heads to clear first (Priority based).
-   **Manual Allocation**: Cashier can manually specify "This ₹4000 is for Bus, not Tuition".
-   **Balance Tracking**: Automatically calculates pending dues for the next receipt.
-   **Minimum Threshold**: Option to block partial payments below a certain % (e.g., must pay at least 50%).

## Real-World Scenarios

### Scenario 1: Financial Constraint
**Background**: Total Due is ₹10,000. Parent has only ₹6,500 in bank account.
**Action**: 
1.  Cashier enters "Received Amount: ₹6,500".
2.  System clears full Tuition (₹5,000) and partial Bus Fee (₹1,500).
3.  Receipt shows "Paid: ₹6,500. Balance Due: ₹3,500".

### Scenario 2: Two-Part Payment Commitment
**Background**: Parent promises to pay half today and half on salary day (1st of next month).
**Action**: Accept 50% now. System keeps the student in "Defaulter list" (technically) but marks them as "Partially Paid".

### Scenario 3: Minimum Payment Policy
**Background**: School rule says "Minimum 70% must be paid to get Exam Hall Ticket".
**Action**: Parent offers ₹2,000 against ₹10,000 due (20%).
**System Behavior**: System blocks the transaction or requires "Manager Approval" override.

### Scenario 4: Specific Allocation
**Background**: Parent wants to pay *only* the Transport Fee (₹2,000) because they might discontinue the bus next month.
**Action**: 
1.  Uncheck "Tuition Fee".
2.  Check "Transport Fee".
3.  Pay ₹2,000.
**Result**: Transport cleared. Tuition remains fully due.

### Scenario 5: Clearing the Balance
**Background**: Student comes back 1 week later to pay the remaining ₹3,500 from Scenario 1.
**Action**:
1.  Search Student.
2.  System shows "Arrears: ₹3,500".
3.  Pay ₹3,500.
**Result**: Account fully cleared.

## Edge Cases & How to Handle Them

### Edge Case 1: Very Small Amount
**What Happens**: Parent tries to pay ₹50 against ₹50,000 due.
**System Behavior**: Administratively useless transaction.
**How to Handle**: Set a global config "Minimum Partial Payment Amount" (e.g., ₹500).

### Edge Case 2: Fine Calculation on Balance
**What Happens**: Due ₹10,000. Paid ₹9,000. Balance ₹1,000.
**System Behavior**: Does the ₹50 Late Fine apply on the remaining ₹1,000?
**How to Handle**: Typically, fines apply if *any* amount is overdue. Some schools waive fine if >90% paid.

### Edge Case 3: Receipt Clarity
**What Happens**: Receipt says "Tuition Fee: ₹5000". Parent thinks they paid fully. Actually, they paid ₹4000.
**System Behavior**: Confusion.
**How to Handle**: Receipt must explicitly print columns: "Total Due | Paid Now | Balance".

### Edge Case 4: Frequency Limit
**What Happens**: Parent pays ₹100 every day for 30 days.
**System Behavior**: Wastes cashier time and receipt paper.
**How to Handle**: Limit partial payments to "Max 3 per installment".

### Edge Case 5: Refund of Partial Payment
**What Happens**: Parent paid ₹7,000 partial. Withdraws admission. Needs refund.
**System Behavior**: Which head do we refund from?
**How to Handle**: Reverse the transaction logic (FIFO - First In First Out reverse) or manual refund entry.

### Edge Case 6: Duplicate Partial
**What Happens**: System shows ₹3,000 balance. Parent claims they paid it yesterday. Cashier takes it again.
**System Behavior**: Excess payment (Credit).
**How to Handle**: Always refresh ledger before accepting. If taken, convert excess to "Advance".

### Edge Case 7: Cheque Partial
**What Happens**: Cheque of ₹5,000 received for ₹12,000 due. Cheque bounces.
**System Behavior**: Reversal must reopen the ₹5,000 balance + add Cheque Bounce Fine.
**How to Handle**: Standard "Cheque Bounce" module handles this, re-instating the debt.

### Edge Case 8: Online Partial Amount
**What Happens**: Payment Gateway allows user to edit amount field.
**System Behavior**: Parent changes ₹10,000 to ₹100 and pays.
**How to Handle**: If school policy forbids online partials, lock the input field. If allowed, process as normal partial.

### Edge Case 9: Tax Calculation (GST)
**What Happens**: Fee attracts 18% GST. Partial payment made.
**System Behavior**: Do we pay GST on the collected amount or billed amount?
**How to Handle**: Accounting standard usually requires GST on *collected* amount. System calculates tax portion of the ₹6,500 received.

### Edge Case 10: Fee Head Priority Conflict
**What Happens**: Parent pays ₹5,000. System allocates to Tuition. Parent wanted it for Annual Fee.
**System Behavior**: Parent complains receipt is wrong.
**How to Handle**: Allow "Manual Allocation Mode" for experienced cashiers.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Total Due | Currency | Yes | Read-only sum |
| Received Amount | Currency | Yes | User input |
| Balance Pending | Currency | Yes | Calculated (Due - Received) |
| Allocation Strategy | Dropdown | Yes | Auto / Manual |
| Minimum Limit | Config | No | Threshold check |

## User Actions
1.  **View Dues**: See total breakdown.
2.  **Edit Amount**: Overwrite "Total Due" with "Cash in Hand".
3.  **Confirm Allocation**: See where the money is going.
4.  **Pay**: Generate receipt.

## Business Rules
-   Overdue Fines are usually prioritized first (cleared before Tuition).
-   Partial payment does not automatically extend the due date for the balance.

## Permissions Required
-   **Accept Partial**: Fee Cashier.
-   **Override Minimum**: Fee Manager.

## Related Submodules
-   **3.1 Quick Receipt**: The interface where this happens.
-   **3.3 Advance Payment**: The opposite (paying more than due).

## API Endpoints
```
POST /api/fee-receipts/partial - Process transaction
GET /api/config/partial-payment-rules - Get limits
```

## Database Schema
```sql
Table: fee_allocations
- id (PK)
- receipt_id (FK)
- fee_head_id (FK)
- amount_paid (DECIMAL)
- balance_remaining (DECIMAL)
```

## UI/UX Considerations
-   **Progress Bar**: Visual indicator: "You are paying 60% of total due".
-   **Red Highlights**: Clearly highlight usage of Manual Allocation to prevent errors.

## Best Practices
1.  **Prioritize Fines**: Always clear fines and arrears first. Fresh fees come last.
2.  **Clear Documentation**: Receipt must verify "This is a PARTIAL payment".
3.  **Follow Up**: System should auto-SMS 3 days later: "Reminder: Balance of ₹X is still due."
