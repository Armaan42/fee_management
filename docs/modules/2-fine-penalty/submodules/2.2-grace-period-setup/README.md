# 2.2 Grace Period Setup

## Overview
**Grace Period Setup** defines the "Safe Zone" after the due date where parents can still pay without attracting a fine. Usually, bank transfers take time, or a parent might just forget by one day. The Grace Period ensures that the school doesn't appear too rigid or greedy by charging late fees immediately.

**In simple terms**: It’s a buffer time. If Due Date is 10th and Grace Period is 2 days, you can pay on 11th or 12th without any penalty.

**Analogy**: 
-   **Library**: Return book by Monday. If you return Tuesday morning, librarian usually waves the fine.
-   **Credit Card**: Often gives a 3-day grace period before hitting your credit score.

## Purpose
To accommodate minor delays in payment processing or human error, improving parent satisfaction and reducing administrative friction over small fines.

## Description
This submodule allows administrators to define the number of "extra days" allowed for different fee types or plans. It handles the logic of whether the fine starts calculating from the Due Date or after the Grace Period ends.

## Key Features
-   **Configurable Days**: Set 0, 1, 2, 5, or any number of grace days.
-   **Fee Head Specific**: Different grace periods for different fees (e.g., 5 days for Tuition, 0 days for Late Bus Fee).
-   **Calculation Logic**: Decide if the fine applies retroactively to the grace days once the limit is crossed.
-   **Holiday Awareness**: Option to extend grace period if the last day falls on a Sunday/Holiday.

## Real-World Scenarios

### Scenario 1: Standard Grace (The "Polite" Buffer)
**Background**: School wants to be fair to parents who pay via NEFT which takes 24 hours.
**Setting**: Grace Period = 3 Days.
**Outcome**:
-   Due 10th. Paid 12th -> No Fine.
-   Paid 14th -> Fine applies (usually calculated from 10th).

### Scenario 2: Weekend Extension
**Background**: Due date falls on Saturday. Office closed.
**Setting**: "Extend if Holiday" = Yes.
**Outcome**: Due Saturday. Grace extends through Sunday. Monday is the last fine-free day.

### Scenario 3: Zero Tolerance (Strict)
**Background**: School bus fee must be paid to confirm seat.
**Setting**: Grace Period = 0 Days.
**Outcome**: Paid 1 day late = Fine immediately.

### Scenario 4: Cheque Clearing Buffer
**Background**: Parent submits cheque on due date, but it clears 3 days later.
**Setting**: "Cheque Payment Mode" Grace = 5 Days.
**Outcome**: System doesn't auto-apply fine while cheque is clearing.

### Scenario 5: Variable Grace
**Background**: Annual Fee is large (₹50k), so give more time. Monthly fee is small (₹2k), give less time.
**Setting**:
-   Annual Fee Head: Grace 7 Days.
-   Monthly Fee Head: Grace 2 Days.

## Edge Cases & How to Handle Them

### Edge Case 1: Payment at 11:59 PM on Last Grace Day
**What Happens**: Online payment gateway timestamp is 23:59. Server processes it at 00:01 (Next day).
**System Behavior**: System might mark it Late.
**How to Handle**: Configure system to use "Transaction Time", not "Processing Time".

### Edge Case 2: Retroactive Fine Calculation
**What Happens**: Due 1st. Grace 5 days. Paid on 6th.
**System Behavior**: 
-   **Option A (Lenient)**: Fine for 1 day (6th).
-   **Option B (Strict)**: Fine for 6 days (1st to 6th).
**How to Handle**: Most schools choose Option B (Strict). Once grace is breached, you pay for the whole delay.

### Edge Case 3: Grace Ends on Sunday
**What Happens**: Grace ends Sunday. Bank closed. Parent pays Monday.
**System Behavior**: Techinically late.
**How to Handle**: Automated "Holiday Extension" logic is best. Otherwise Admin has to manually waive.

### Edge Case 4: Partial Payment in Grace
**What Happens**: Due ₹10k. Pays ₹5k on grace day.
**System Behavior**: Is the remaining ₹5k overdue?
**How to Handle**: Yes, remaining amount becomes overdue after grace period implies fine on the balance.

### Edge Case 5: Manual Grace Extension
**What Happens**: Server down on last day. Principal says "Extend dates by 2 days".
**System Behavior**: Admin updates setting for "All Students".
**How to Handle**: Ensure the update doesn't trigger recalc errors for those who already paid.

### Edge Case 6: Grace Period > Billing Cycle
**What Happens**: Monthly bill. Grace period 35 days.
**System Behavior**: Next month's bill generated before previous month's deadline. Confusion.
**How to Handle**: Validation rule: Grace Period must be less than Billing Frequency (e.g., Max 15 days for Monthly).

### Edge Case 7: Different Timezones
**What Happens**: Parent in USA pays for child in India. Timezone difference makes it "Next Day" in India.
**System Behavior**: Timestamp mismatch.
**How to Handle**: Standardize on School's Local Time (IST).

### Edge Case 8: Fine on "Grace Period" itself?
**What Happens**: Is there a fee to "buy" extra grace days?
**System Behavior**: Rare logic.
**How to Handle**: Not standard. Stick to simple grace days.

### Edge Case 9: Conflicting Grace Periods
**What Happens**: Student assigned Fee Plan A (Grace 2 days) and Fee Plan B (Grace 5 days).
**System Behavior**: Which rule wins?
**How to Handle**: Usually the most specific rule wins, or the maximum benefit (5 days) is given.

### Edge Case 10: Recurring Grace
**What Happens**: Parent habitually pays on last grace day every month.
**System Behavior**: Allowable.
**How to Handle**: No penalty, but maybe a report to flag "Chronic Late Payers".

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Rule Name | Text | Yes | "Standard 3-Day Grace" |
| Days Count | Number | Yes | 3 |
| Apply To | Dropdown | Yes | All Fees / Specific Fee Head |
| Holiday Logic | Checkbox | No | "Extend if ends on holiday?" |
| Fine Calculation | Dropdown | Yes | "From Due Date" / "From Grace End" |

## User Actions
1.  **Define Policy**: Set the global grace period.
2.  **Override**: Set specific grace for specific Fee Heads if needed.
3.  **Monitor**: View "In Grace Period" report to see upcoming defaulters.

## Business Rules
-   Grace period does not change the "Due Date" field used for accounting; it only suppresses the fine.
-   Once grace is over, the status changes from "Due" to "Overdue".

## Permissions Required
-   **Configure**: Fee Admin.
-   **Manual Extension**: Super Admin.

## Related Submodules
-   **2.1 Fine Rules**: Grace period decides *when* these rules trigger.
-   **2.5 Fine Adjustment**: To fix issues if grace logic fails.

## API Endpoints
```
POST /api/grace-rules - Create rule
GET /api/grace-rules - List
```

## Database Schema
```sql
Table: grace_period_rules
- id (PK)
- name (VARCHAR)
- days (INT)
- extend_on_holiday (BOOLEAN)
- calculation_mode (ENUM: FROM_DUE_DATE, FROM_GRACE_END)
```

## UI/UX Considerations
-   **Countdown**: Show "2 Days of Grace Remaining" on Parent Portal dashboard.
-   **Color Coding**: Yellow for "In Grace Period", Red for "Overdue".

## Best Practices
1.  **Be Consistent**: Don't change grace periods monthly. Confusion leads to angry parents.
2.  **Communicate**: "Due by 10th" is better than "Due by 10th (but you have until 13th)". Mention grace only in fine print or late reminders.
3.  **Strict Calculation**: If grace is breached, charge fine from Due Date. This prevents people from "using up" grace days as a right.
