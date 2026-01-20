# 1.6 Fee Installment Plans

## Overview
**Fee Installment Plans** allow schools to break down large annual fees into smaller, manageable chunks (installments) with specific due dates. This helps parents manage their finances better while ensuring the school has a predictable cash flow.

**In simple terms**: It’s like buying a car on EMI. Instead of paying the full amount on Day 1, you agree to pay in 3, 4, or 12 parts over the year.

**Analogy**: 
-   **Annual Fee**: Paying ₹120,000 once.
-   **Installment Plan**: Paying ₹10,000 every month for 12 months.

## Purpose
To configure flexible payment schedules for students, ensuring that fee collection is spread out systematically throughout the academic year.

## Description
This submodule allows administrators to create different payment split plans. A default plan (e.g., Quarterly) can be assigned to everyone, while special plans (e.g., Monthly) can be created for specific requests. It manages due dates, late fine rules per installment, and distribution of fee heads across installments.

## Key Features
-   **Flexible Splitting**: Split total fees by Percentage (25%-25%-25%-25%) or Fixed Amounts.
-   **Custom Due Dates**: Set specific dates for each installment (e.g., 10th of every month).
-   **Fee Head Allocation**: Decide which fees are collected in which installment (e.g., Tuition every month, but Admission Fee only in 1st Installment).
-   **Grade-wise Plans**: Different plans for different classes (Class 10 pays early due to Board Exams).
-   **Reminders**: Automated alerts when an installment due date is approaching.

## Real-World Scenarios

### Scenario 1: Standard Quarterly Plan (The Default)
**Background**: Most schools collect fees 4 times a year.
**Steps**:
1.  Admin creates "Standard Quarterly Plan".
2.  Defines 4 Installments:
    -   Q1 (Apr-Jun): Due Apr 10.
    -   Q2 (Jul-Sep): Due Jul 10.
    -   Q3 (Oct-Dec): Due Oct 10.
    -   Q4 (Jan-Mar): Due Jan 10.
3.  Assigns this plan to "All Classes".
**Result**: Parents receive 4 billing notifications a year.

### Scenario 2: Monthly Payment Plan (Special Request)
**Background**: A parent requests to pay monthly as they are salaried employees.
**Steps**:
1.  Admin creates "Monthly Plan - 10th Due".
2.  Defines 12 Installments (Apr to Mar).
3.  Assigns this specific plan to Student A.
**Result**: Student A has 12 smaller dues instead of 4 large ones.

### Scenario 3: Early Bird "One-Shot" Payment
**Background**: School offers 5% discount if full year fee is paid in April.
**Steps**:
1.  Admin creates "Annual One-Shot Plan".
2.  Defines 1 Installment: 100% Due on Apr 10.
3.  Links a "5% Concession" to this plan type.
**Result**: Parents who choose this pay everything at once and get the discount.

### Scenario 4: New Admission Plan (Joined in Oct)
**Background**: Student joins in Q3. Shouldn't be asked for Q1 and Q2 due dates (which are past).
**Steps**:
1.  Admin assigns fees pro-rata.
2.  Assigns a "Remaining Year Plan" which has only 2 installments (Oct, Jan).
**Result**: Appropriate schedule for late joiners.

### Scenario 5: Uneven Split for Board Exam Classes
**Background**: Class 12 finishes early (Feb). School wants to collect everything by December.
**Steps**:
1.  Admin creates "Class 12 Accelerated Plan".
2.  Installments:
    -   Apr: 40%
    -   Aug: 30%
    -   Dec: 30%
3.  Sets Due Dates accordingly.
**Result**: Full collection completed before students leave for study leave.

## Edge Cases & How to Handle Them

### Edge Case 1: Unequally Divisible Amounts
**What Happens**: Fee is ₹10,000. Plan is 3 equal installments. (10000 / 3 = 3333.333...)
**System Behavior**: 
-   Inst 1: 3333.33
-   Inst 2: 3333.33
-   Inst 3: 3333.34 (System adjusts the last penny).
**How to Handle**: Accept automated rounding adjustment.

### Edge Case 2: Switching Plans Mid-Year
**What Happens**: Parent paid Q1 and Q2 in Quarterly plan. Now wants to switch to Monthly for remaining.
**System Behavior**: Complex calculation. System must calculate "Pending Balance" and re-distribute it over the remaining months (Oct-Mar).
**How to Handle**: Use "Change Payment Plan" feature which auto-recalculates future dues.

### Edge Case 3: Missed Installment
**What Happens**: Parent misses Due Date for Inst 1.
**System Behavior**: Inst 1 becomes "Overdue". Late fine applies. Inst 2 remains "Future Due".
**How to Handle**: System handles this automatically via Late Fee module.

### Edge Case 4: Advance Payment of Future Installment
**What Happens**: Parent wants to pay Inst 4 while Inst 2 is currently due.
**System Behavior**: System creates a "Credit" in the ledger or forces sequential payment (Inst 2 -> Inst 3 -> Inst 4).
**How to Handle**: Encouraging sequential payment keeps accounting cleaner.

### Edge Case 5: Fee Head Specificity
**What Happens**: "Admission Fee" (One time) is split into 12 months?
**System Behavior**: Usually bad practice. Admission fee should be "100% in Inst 1". Tuition fee should be "Split across all".
**How to Handle**: Configure "Fee Head Allocation" rules properly inside the plan.

### Edge Case 6: Installment Total != Fee Total
**What Happens**: Plan defined as Fixed Amounts: 5000 + 5000 + 5000 = 15000. But Student's assigned fee is 16000.
**System Behavior**: Where does the extra 1000 go?
**How to Handle**: Always use Percentage splits (25% x 4) rather than fixed amounts to avoid mismatch.

### Edge Case 7: Weekend Due Dates
**What Happens**: Due date falls on Sunday.
**System Behavior**: Online payments work. Cash counter is closed.
**How to Handle**: Configurable "Grace Period" ensures they can pay on Monday without fine.

### Edge Case 8: Leap Year
**What Happens**: Monthly due date set to "30th". Feb has 28/29 days.
**System Behavior**: System should auto-adjust to "Last Day of Month".
**How to Handle**: Use "Last Day" logic instead of hardcoded date.

### Edge Case 9: SMS Trigger on Bulk Generation
**What Happens**: Generating Installments triggers thousands of SMS.
**System Behavior**: Server load / Cost spike.
**How to Handle**: Schedule SMS notifications in batches.

### Edge Case 10: Cancelled Installment
**What Happens**: School cancellation (COVID). Fee for Q4 waived.
**System Behavior**: Admin needs to "Void" the Q4 installment.
**How to Handle**: Remove the due amount. Ledger updates.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Plan Name | Text | Yes | "Standard Quarterly" |
| No. of Installments | Number | Yes | 4 |
| Frequency | Dropdown | Yes | Monthly/Quarterly/Custom |
| Due Day | Number | No | "10th of the month" |
| Late Fee Rule | Dropdown | No | Link to fine policy |
| Allocation Logic | JSON | Yes | How heads are distributed |
| Is Default | Checkbox | No | Auto-apply to new students? |

## User Actions
1.  **Create Plan**: Define the structure.
2.  **Assign Plan**: Link valid classes/students.
3.  **Generate Dues**: System post installments to student ledgers.
4.  **Monitor**: View "Defaulters List" per installment.

## Business Rules
-   Sum of installment percentages must be exactly 100%.
-   Past due dates cannot be changed once fines are applied.
-   Plan change requests usually require Admin approval.

## Permissions Required
-   **Configure Plans**: Fee Admin.
-   **Change Student Plan**: Principal / Senior Admin.

## Related Submodules
-   **1.2 Generic Fee Templates**: The total amount comes from here.
-   **3.1 Implement Fee Collection**: Collecting against these installments.
-   **3.2 Late Fee Configuration**: Rules for missed due dates.

## API Endpoints
```
POST /api/installment-plans - Create plan
GET /api/installment-plans - List
POST /api/students/:id/change-plan - Switch plan
GET /api/students/:id/installments - View schedule
```

## Database Schema
```sql
Table: fee_installment_plans
- id (PK)
- name (VARCHAR)
- total_installments (INT)
- academic_year_id (FK)

Table: plan_installments
- id (PK)
- plan_id (FK)
- installment_number (INT)
- due_date (DATE)
- percentage (DECIMAL)
- title (VARCHAR) -- "Q1 Installment"
```

## UI/UX Considerations
-   **Calendar View**: Show due dates on a calendar.
-   **Visual Graph**: Pie chart showing split.
-   **Timeline**: Horizontal timeline for parents to see upcoming payments.

## Best Practices
1.  **Align with Salary Dates**: Set due dates around 5th-10th (after parents get salary).
2.  **Avoid Too Many Plans**: Stick to 2-3 standard options (Annual, Quarterly, Monthly) to simplify accounting.
3.  **Clear Communication**: Send reminders 3 days before due date.
