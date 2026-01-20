# 2.1 Fine Rules Configuration

## Overview
**Fine Rules Configuration** acts as the "Penalty Rulebook" for your school. It tells the system exactly how to calculate fines when fees are not paid on time. Not all late payments are the same—sometimes you charge a flat ₹100, other times you might charge ₹10 per day. This module handles all those calculations automatically.

**In simple terms**: It answers the question, "If Student X pays 5 days late, how much extra should they pay?"

**Analogy**: 
-   **Library Fine**: ₹5 for everyday the book is late.
-   **Credit Card Late Fee**: Flat ₹500 if you miss the due date.
-   **School Fine**: Can be either, or a mix of both!

## Purpose
To automate the calculation of late fees, ensuring consistency and removing manual calculation errors (and arguments with parents).

## Description
This submodule allows administrators to create reusable fine policies. You can define rules based on "Days Late" (e.g., 0-7 days late = ₹100, 7-30 days = ₹500). Once created, these rules are linked to Fee Installment Plans.

## Key Features
-   **Calculation Logic**: Fixed Amount (₹) or Daily Rate (₹/day) or Percentage (%).
-   **Slab-based Fines**: Different fines for different delay periods (Tiers).
-   **Max Cap**: Limit the maximum fine amount (e.g., Fine cannot exceed ₹2000).
-   **Grace Period Integration**: Works with grace period settings to delay fine start.
-   **Frequency**: One-time charge vs Recurring monthly charge.

## Real-World Scenarios

### Scenario 1: Daily Fine (The standard approach)
**Background**: School wants to encourage quick payment.
**Rule**: ₹50 per day for every day late.
**Outcome**:
-   Paid 2 days late: Fine = ₹100.
-   Paid 10 days late: Fine = ₹500.

### Scenario 2: Flat Penalty (One-time slap)
**Background**: School prefers simple accounting.
**Rule**: Flat ₹500 if unpaid by due date.
**Outcome**: 
-   Paid 1 day late: Fine = ₹500.
-   Paid 30 days late: Fine = ₹500.

### Scenario 3: Slab System (Incremental severity)
**Background**: "We'll be lenient for the first week, but strict after that."
**Rule**:
-   1-7 Days Late: ₹100 (Total)
-   8-30 Days Late: ₹500 (Total)
-   30+ Days Late: ₹1000 (Total)
**Outcome**: A student paying on day 6 pays ₹100. Paying on day 9 pays ₹500.

### Scenario 4: Percentage Fine (University style)
**Background**: Higher fees should attract higher fines.
**Rule**: 1% of the due amount per week.
**Outcome**: 
-   Tuition (₹50k) late by 1 week = ₹500.
-   Transport (₹2k) late by 1 week = ₹20.

### Scenario 5: Capped Daily Fine
**Background**: Parents complained that ₹50/day became ₹50,000 for a student who was sick for year.
**Rule**: ₹50/day, but Maximum Cap = ₹2,000.
**Outcome**: Even if late by 300 days, the fine stops growing at ₹2,000.

## Edge Cases & How to Handle Them

### Edge Case 1: Grace Period Overlap
**What Happens**: Due Date: 10th. Fine Rule: ₹100/day. Grace Period: 2 days (11th, 12th).
**System Behavior**: 
-   Student pays on 12th: Fine ₹0.
-   Student pays on 13th: Fine ₹300 (Calculation often counts from 10th) OR ₹100 (Counts from 13th).
**How to Handle**: Define "Fine Start Date" clearly in settings: "From Due Date" or "From Grace End Date".

### Edge Case 2: Holiday Exclusion
**What Happens**: Fine is ₹100/day. Due date passed. There were 4 Sundays and 2 Holidays in the late period.
**System Behavior**: Usually, systems charge for *calendar days* (including Sundays).
**How to Handle**: If school policy excludes Sundays, ensure the "Exclude Holidays" flag is checked.

### Edge Case 3: Fine > Fee Amount
**What Happens**: Fee Due: ₹500. Late by 100 days at ₹10/day = ₹1000 Fine.
**System Behavior**: Total Due = ₹500 + ₹1000 = ₹1500.
**How to Handle**: Enable "Fine Cap" (e.g., Max 100% of principal amount).

### Edge Case 4: Partial Payment of Fee
**What Happens**: Due: ₹10,000. Parent pays ₹8,000. ₹2,000 pending.
**System Behavior**: Fine should continue calculating only on the pending ₹2,000 (or flat fine based on "Not Fully Paid" status).
**How to Handle**: Percentage fines work best here. Flat fines might feel unfair.

### Edge Case 5: Retroactive Rule Change
**What Happens**: Admin changes fine from ₹50 to ₹100 mid-month.
**System Behavior**: 
-   Existing unpaid fines might jump up.
-   Previously paid fines should NOT change.
**How to Handle**: System usually versions the rules. Old dues follow old rules.

### Edge Case 6: Fine on Fine
**What Happens**: Month 1: Fee ₹1000 + Fine ₹100 = ₹1100 Due. Month 2: Calculation based on ₹1100?
**System Behavior**: Compound interest illegal/unethical in schools.
**How to Handle**: Fine is calculated ONLY on the Principal Fee Amount (₹1000).

### Edge Case 7: Waived Fine Re-appearing
**What Happens**: Admin manually waives fine. Next day, nightly batch job runs.
**System Behavior**: Job sees "Overdue & No Fine", so it adds the fine again.
**How to Handle**: System must mark the fine as "Manually Waived (Do Not Re-apply)" in the database.

### Edge Case 8: Zero Value Fee
**What Happens**: Student has a 100% scholarship (Fee = 0). But entry exists.
**System Behavior**: Zero due -> No Late -> No Fine.
**How to Handle**: Correct behavior.

### Edge Case 9: Slab Transition Gaps
**What Happens**: Slab 1: 1-10 days. Slab 2: 12-20 days.
**System Behavior**: What happens on Day 11?
**How to Handle**: Validation rule must ensure Slabs are continuous (End Day + 1 = Next Start Day).

### Edge Case 10: Currency Rounding
**What Happens**: 1.5% fine on ₹1550 = ₹23.25.
**System Behavior**: Ledger shows decimals.
**How to Handle**: Auto-round simple fines to nearest whole number (₹23 or ₹24).

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Rule Name | Text | Yes | "Standard Daily Fine" |
| Calculation Type | Dropdown | Yes | Daily / Fixed / Percentage / Slabs |
| Amount/Rate | Number | Yes | Value (e.g., 50) |
| Max Amount (Cap) | Number | No | Stop calculating after this limit |
| Trigger Condition | Dropdown | Yes | "After Due Date" / "After Grace Period" |
| Recurrence | Dropdown | No | Monthly recurrence for long dues? |

## User Actions
1.  **Create Rule**: Define the policy.
2.  **Simulate**: Test "If late by 10 days, what is the fine?".
3.  **Link**: Assign rule to a Fee Installment Plan (Module 1.6).
4.  **Activate**: Make it live.

## Business Rules
-   Fines are generally recognized as "Income" only when collected (Cash basis accounting).
-   Cannot charge fine if "Is Dispute" flag is raised on a student.

## Permissions Required
-   **Manage Rules**: Fee Admin, Super Admin.
-   **View Rules**: Accounts User.

## Related Submodules
-   **1.6 Fee Installment Plans**: Where these rules are attached.
-   **2.4 Manual Fine Waiver**: To override these rules.

## API Endpoints
```
POST /api/fine-rules - Create new rule
GET /api/fine-rules - List all
POST /api/fine-rules/simulate - Test calculation
```

## Database Schema
```sql
Table: fine_rules
- id (PK)
- name (VARCHAR)
- type (ENUM: DAILY, FIXED, PERCENT, SLAB)
- amount (DECIMAL)
- max_cap (DECIMAL)
- created_at (TIMESTAMP)

Table: fine_slabs
- id (PK)
- rule_id (FK)
- from_day (INT)
- to_day (INT)
- amount (DECIMAL)
```

## UI/UX Considerations
-   **Test Calculator**: A small widget where Admin can input "Days Late" and see the result before saving.
-   **Visual Slab Graph**: Show a bar chart of how fine increases over time.

## Best Practices
1.  **Keep it Simple**: Complex fine rules confuse parents and staff. Daily or Flat fines are best.
2.  **Set a Cap**: Always define a maximum limit to avoid PR disasters (e.g., "School charges ₹1 Lakh fine!").
3.  **Grace Period**: Always allow 2-3 days grace for bank transfer delays.
