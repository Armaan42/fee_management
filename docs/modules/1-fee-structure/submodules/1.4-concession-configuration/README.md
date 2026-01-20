# 1.4 Concession Configuration

## Overview
**Concession Configuration** is about setting up "Discount Coupons" for your school fees.

Sometimes, you don't want a student to pay the full price. Maybe they are the child of a staff member, or they have a high academic rank (Merit Scholarship), or they have financial difficulties. This module lets you create these "Discount Rules" so the system knows how much to deduct from the total bill.

**In simple terms**: It’s the tool for managing Scholarships, Waivers, and Discounts.

**Analogy**:
-   **Fee**: The price tag on a shirt ($100).
-   **Concession**: A "20% Off" sticker.
-   **Final Bill**: $80.

## Purpose
To define and manage various types of fee discounts, scholarships, and waivers that can be applied to student fee assignments.

## Description
This submodule allows administrators to create reusable concession types. You can define whether the concession is a fixed amount (e.g., ₹5000 off) or a percentage (e.g., 50% off). You can also specify which specific Fee Heads the concession applies to (e.g., 50% off Tuition Fee, but 0% off Exam Fee).

## Key Features
-   **Concession Types**: Create categories like "Staff Ward", "Merit", "Sibling".
-   **Calculation Modes**: Support for Flat Amount (₹) or Percentage (%) reductions.
-   **Applicability**: Choose which fee heads are eligible for the discount.
-   **Approval Workflow**: Require Principal's approval before a concession becomes active (if configured).
-   **Budgeting**: Track total amount given as concessions.

## Real-World Scenarios

### Scenario 1: Staff Ward Benefit (50% Off)
**Background**: The school policy states that children of teaching staff get a 50% discount on Tuition fees, but must pay full Annual charges.
**Steps**:
1.  Admin creates a Concession: "Staff Ward Discount".
2.  Sets Type: **Percentage**.
3.  Value: **50%**.
4.  Applicable Heads: Checks "Tuition Fee" only. (Unchecks Transport, Library, etc.).
5.  Saves.
**Result**: When applied to a teacher's child, the system automatically removes 50% of the Tuition cost.

### Scenario 2: Sibling Discount (Flat Amount)
**Background**: For parents with two children in the school, the second child gets a flat ₹2,000 discount on the Admission Fee.
**Steps**:
1.  Admin creates Concession: "Sibling Discount".
2.  Sets Type: **Flat Amount**.
3.  Value: **₹2,000**.
4.  Applicable Heads: Checks "Admission Fee".
**Result**: A flat ₹2,000 is deducted from the bill.

### Scenario 3: RTE / Government Waiver (100% Free)
**Background**: Under the Right To Education (RTE) act, 25% of seats are free.
**Steps**:
1.  Admin creates Concession: "RTE Full Waiver".
2.  Sets Type: **Percentage**.
3.  Value: **100%**.
4.  Applicable Heads: Selects **All Heads**.
**Result**: The eligible students pay ₹0.

### Scenario 4: Sports Scholarship (Tuition Only)
**Background**: Students who play at the National level get free Tuition.
**Steps**:
1.  Create "National Sports Scholarship".
2.  Type: Percentage (100%).
3.  Applicable Heads: "Tuition Fee" only.
**Result**: These athletes pay for Lab, Library, and Transport, but Tuition is free.

### Scenario 5: One-Time Hardship Waiver
**Background**: A student's family faces a medical emergency. The Principal approves a one-time waiver of ₹5,000.
**Steps**:
1.  Admin creates a generic "Special Waiver".
2.  When assigning to the student, inputs ₹5,000 manual overriding amount.
**Result**: Flexible handling of humanitarian cases.

## Edge Cases & How to Handle Them

### Edge Case 1: Concession Exceeds Fee Amount
**What Happens**: Applying a ₹5,000 concession to a fee of ₹4,000.
**System Behavior**: Fee becomes ₹0 (cannot go negative). Remaining ₹1,000 is ignored/lost unless system supports "Carry Forward".
**How to Handle**: Ensure Flat Amount concessions are smaller than the fee they apply to.

### Edge Case 2: Stacking Multiple Concessions
**What Happens**: Student is a "Staff Ward" (50% off) AND a "Topper" (20% off).
**System Behavior**: 
-   **Option A**: Additive (50+20 = 70% off).
-   **Option B**: Sequential (50% off first, then 20% off the remainder).
-   **Option C**: Max Only (Take the highest, 50% off).
**How to Handle**: Define the "Stacking Rule" in global settings. Usually, "Max Only" is safer to prevent 100%+ discounts.

### Edge Case 3: Applying to "Optional" Fees
**What Happens**: Admin tries to give a discount on "Horse Riding Fee" (which is optional).
**System Behavior**: System allows it, but it only works if the student actually *has* the Horse Riding fee assigned.
**How to Handle**: Verify student has the fee before promising the discount.

### Edge Case 4: Expired Concession
**What Happens**: "Sibling Discount" is valid only for 1 year, but admin forgets to remove it for next year.
**System Behavior**: System continues to apply it.
**How to Handle**: Set an "Expiry Date" when creating the student-concession link.

### Edge Case 5: Revoking After Payment
**What Happens**: Parent pays the discounted fee of ₹50. Later, Admin realizes they weren't eligible and removes the concession.
**System Behavior**: The fee jumps back to ₹100. Since ₹50 is paid, the system shows ₹50 as "Due/Pending".
**How to Handle**: You must inform the parent to pay the difference.

### Edge Case 6: Precision Rounding
**What Happens**: 33.33% discount on ₹1000.
**System Behavior**: Calculated as ₹333.30 or ₹333.33. Final Fee ₹666.70.
**How to Handle**: Accept standard currency rounding.

### Edge Case 7: Changing Fee Head Amount
**What Happens**: Tuition Fee is increased from 10k to 12k. Concession is 50%.
**System Behavior**: 
-   If Percentage: Discount automatically jumps from 5k to 6k.
-   If Flat Amount: Discount stays 5k (so student pays more).
**How to Handle**: Choose Percentage type if you want the discount to scale with inflation.

### Edge Case 8: Concession on "Fine"
**What Happens**: Trying to discount a "Late Payment Fine".
**System Behavior**: Often Fines are separate entity types and standard concessions might not pick them up.
**How to Handle**: Use a specific "Fine Waiver" action instead of a general concession.

### Edge Case 9: Student Transfer
**What Happens**: Student moves from Class 5 to Class 6.
**System Behavior**: Concession linkage might be strictly "Class 5 Tuition".
**How to Handle**: Ensure Concession is linked to "Tuition Fee" (Global head) not a class-specific instance, or re-apply concession after promotion.

### Edge Case 10: Retrospective Application
**What Happens**: Scholarship approved in June, but applies from April. April fee already paid in full.
**System Behavior**: System creates a "Credit Balance" (Advance) for the student to be used in future months.
**How to Handle**: Use the credit for July fees.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Name | Text | Yes | "Merit Scholarship 2024" |
| Type | Dropdown | Yes | Percentage / Flat Amount |
| Value | Number | Yes | 50.00 or 5000.00 |
| Applicable Fee Heads | Multi-select | Yes | Which fees can be discounted |
| Is Active | Checkbox | Yes | Usage status |
| Description | Text | No | Policy details |

## User Actions
1.  **Create Concession**: Define the rule.
2.  **Assign to Student**: Link the rule to a student (done in Module 1.3 or dedicated screen).
3.  **Approve**: Principal overrides/approves the grant.
4.  **View Report**: See total revenue "lost" to concessions.

## Business Rules
-   Concessions are usually Expense or Revenue Leaks; strictly controlled permissions.
-   Cannot apply negative concession (Surcharge).
-   Must track "Who granted this" for audit.

## Permissions Required
-   **Configure**: Super Admin.
-   **Grant/Assign**: Principal, Fee Admin (with approval).

## Related Submodules
-   **1.1 Define Fee Heads**: The targets of the concession.
-   **1.3 Student Fee Assignment**: Where the concession is actually applied to a person.
-   **7.1 Reports**: "Concession Report".

## API Endpoints
```
POST /api/concessions - Create new rule
POST /api/students/:id/concessions - Grant to student
DELETE /api/students/:id/concessions/:id - Revoke
```

## Database Schema
```sql
Table: concessions
- id (PK)
- name (VARCHAR)
- type (ENUM: PERCENT, FLAT)
- value (DECIMAL)
- fee_head_ids (JSON/Array) -- IDs of heads it applies to
- is_active (BOOLEAN)

Table: student_concessions
- id (PK)
- student_id (FK)
- concession_id (FK)
- academic_year_id (FK)
```

## UI/UX Considerations
-   Show "Original Amount", "Concession Amount", and "Net Payable" clearly.
-   Use Red/Green indicators (Red for cost, Green for discount).

## Best Practices
1.  **Use Percentages**: They handle fee hikes better than flat amounts.
2.  **Naming Convention**: Include year if rules change annually (e.g., "Sib-Disc-2024").
3.  **Regular Audits**: Check concession reports monthly to spot unauthorized discounts.
