# 2.5 Fine Adjustment

## Overview
**Fine Adjustment** is a tool for correcting the final fine balance when standard rules and waivers are not enough. Sometimes, systems make calculation errors (e.g., due to leap years or rounding), or specific administrative decisions require adding or removing a specific amount from the fine ledger.

**In simple terms**: It allows you to say, "The system says the fine is ₹100, but I want to make it ₹150 (Debit) or ₹50 (Credit)."

**Analogy**: 
-   **Restaurant Bill**: The bill is $50. The waiter adds a "Custom Charge" of $5 for extra cheese (Debit Adjustment) or removes $5 because the soup was cold (Credit Adjustment).

## Purpose
To ensure the accuracy of the fine ledger by allowing manual plus/minus adjustments for exceptional scenarios.

## Description
This submodule permits authorized users to post debit (add) or credit (deduct) entries specifically against the "Fine" head. Unlike a "Waiver" which only removes fines, an "Adjustment" can also *increase* them (e.g., for disciplinary reasons).

## Key Features
-   **Debit Adjustment**: Add a new fine amount manually.
-   **Credit Adjustment**: Reduce an existing fine amount manually.
-   **Link to Fee**: Adjustments are linked to specific fee installments.
-   **Audit Note**: Mandatory remarks explaining the manual change.
-   **Balance Recalculation**: Automatically updates the total due after adjustment.

## Real-World Scenarios

### Scenario 1: Disciplinary Fine (Debit)
**Background**: Student broke a window. School policy says "Fine them ₹500".
**Action**: Admin creates a **Debit Adjustment**.
**Amount**: ₹500.
**Reason**: "Property Damage - Window".

### Scenario 2: Rounding Correction (Credit/Debit)
**Background**: Fee was ₹3333.33. System calculated fine as ₹33.33. Policy says round to ₹35.
**Action**: Admin adds a **Debit Adjustment** of ₹1.67.
**Result**: Total Fine = ₹35.00.

### Scenario 3: Refund Adjustment (Credit)
**Background**: Parent paid a fine twice due to a glitch.
**Action**: Admin cannot just "delete" the transaction. Creates a **Credit Adjustment** (Negative Fine).
**Amount**: -₹500.
**Result**: Student balance drops by ₹500, effectively refunding the excess.

### Scenario 4: Transferring Fine (Correction)
**Background**: Fine of ₹100 was wrongly charged under "Tuition Fine". It should be "Bus Fine".
**Action**:
1.  Credit Adjustment of ₹100 on Tuition Fine.
2.  Debit Adjustment of ₹100 on Bus Fine.
**Result**: Ledger accurate.

### Scenario 5: Write-off (Credit)
**Background**: Student left the school. Outstanding fine of ₹10 is unrecoverable.
**Action**: Credit Adjustment of ₹10.
**Reason**: "Bad Debt / Write-off".

## Edge Cases & How to Handle Them

### Edge Case 1: Adjustment > Principal Amount
**What Happens**: Fine is ₹100. Admin adds ₹2000 adjustment.
**System Behavior**: Allowed (e.g., major damage fine).
**How to Handle**: Ensure high-value adjustments trigger an approval workflow.

### Edge Case 2: Negative Fine Balance
**What Happens**: Fine Due: ₹0. Credit Adjustment: ₹100.
**System Behavior**: Fine Balance becomes -₹100 (Credit).
**How to Handle**: This amount should be adjustable against future fees.

### Edge Case 3: Adjusting Closed Financial Year
**What Happens**: Admin tries to adjust a fine from March 2023 in April 2024.
**System Behavior**: Accounting period is closed.
**How to Handle**: Block adjustments on closed periods. Post it in current period with a remark "Ref Year 2023".

### Edge Case 4: Receipt Linkage
**What Happens**: Fine was paid. Receipt #123 generated. Admin tries to "Adjust" that specific fine.
**System Behavior**: Cannot modify settled transactions.
**How to Handle**: Void Receipt #123 first, then adjust.

### Edge Case 5: Currency Precision
**What Happens**: Admin tries to adjust ₹0.005.
**System Behavior**: Database handles 2 decimals.
**How to Handle**: Round to nearest valid currency unit.

### Edge Case 6: Missing Reason
**What Happens**: Admin posts adjustment without explanation.
**System Behavior**: Audit failure.
**How to Handle**: Mandatory text field "Reason".

### Edge Case 7: Bulk Adjustment
**What Happens**: "Late Exam Registration Fine" of ₹50 to be added to 200 students.
**System Behavior**: Manual entry 200 times is slow.
**How to Handle**: Use "Bulk Debit" tool.

### Edge Case 8: Notification
**What Happens**: Student charged extra ₹500. Parent unaware.
**System Behavior**: Parent pays normal fee, gets "Partial Payment" error.
**How to Handle**: Send SMS immediately upon Debit Adjustment.

### Edge Case 9: Tax Implication
**What Happens**: Fine attracts 18% GST. Admin adds ₹100 adjustment.
**System Behavior**: Does system add ₹18 tax on top?
**How to Handle**: If fines are taxable, adjustments must also calculate tax.

### Edge Case 10: Recurring Adjustment
**What Happens**: Admin wants to add ₹50 every month manually.
**System Behavior**: System doesn't support "Recurring Adjustments".
**How to Handle**: Use "Recurring Fee Head" instead of manual adjustment.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Student | Lookup | Yes | Target student |
| Period | Date | Yes | Which month/installment |
| Type | Dropdown | Yes | Debit (+) / Credit (-) |
| Amount | Currency | Yes | ₹500 |
| Reason | Text | Yes | "Damage to desk" |
| Date | Date | Yes | Transaction date |

## User Actions
1.  **Select Student**: Open ledger.
2.  **Add Adjustment**: Choose type and amount.
3.  **Approve**: If amount > limit.
4.  **Save**: Updates balance instantly.

## Business Rules
-   Debit Adjustments increase the "Receivable" (Asset).
-   Credit Adjustments reduce the "Receivable" (Expense/Loss).

## Permissions Required
-   **Create Adjustment**: Senior Accountant.
-   **Approve**: Fee Manager.

## Related Submodules
-   **2.4 Manual Waiver**: A specific type of Credit Adjustment.
-   **7.1 Reports**: "Adjustments Register".

## API Endpoints
```
POST /api/fine-adjustments - Create entry
GET /api/fine-adjustments/:id - View details
```

## Database Schema
```sql
Table: fine_adjustments
- id (PK)
- student_id (FK)
- type (ENUM: DEBIT, CREDIT)
- amount (DECIMAL)
- reason (TEXT)
- created_by (FK)
- created_at (TIMESTAMP)
```

## UI/UX Considerations
-   **Color Coding**: Red for Debit (You owe more), Green for Credit (You owe less).
-   **History**: Show a timeline of all adjustments for transparency.

## Best Practices
1.  **Use Sparely**: Frequent manual adjustments indicate a problem with the automated rules.
2.  **Monitor Credits**: High volume of Credit Adjustments means potential revenue leakage.
3.  **Notification**: Always notify parents of Debit Adjustments (extra charges).
