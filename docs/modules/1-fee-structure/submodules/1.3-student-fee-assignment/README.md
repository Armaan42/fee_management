# 1.3 Student Fee Assignment

## Overview
Submodule 1.2 helped you create the "Menu" (Fee Templates). Now, **Submodule 1.3** is where you actually "Take the Order".

**Student Fee Assignment** is the process of linking a specific Fee Template to a specific student (or group of students). Until you do this, the system knows *what* the fees are, but doesn't know *who* needs to pay them.

**In simple terms**: It involves putting the bill in the student's name. You can do this for one student at a time (e.g., a new admission) or for an entire class at once (e.g., all Class 10 students).

**Analogy**: 
-   **Fee Head**: "Burger"
-   **Fee Template**: "Combo Meal #1"
-   **Fee Assignment**: "Giving Combo Meal #1 to Table 5"

## Purpose
To officially generate fee records for students by assigning them the appropriate fee structures. This action creates the "Due Amount" in the student's ledger.

## Description
This submodule allows administrators to assign pre-defined fee templates to students. It supports bulk assignment (by class/section) to save time, as well as individual assignment for specific cases. It also handles the 'pro-rata' assignment for students joining late.

## Key Features
-   **Bulk Assignment**: Assign fees to hundreds of students in one click based on Class/Section.
-   **Individual Assignment**: Assign fees to a single student (useful for new admissions).
-   **Filtering**: Select students by Stream, Transport Route, or Admission Number.
-   **Preview**: See exactly what total amount will be assigned before confirming.
-   **History**: View past assignments to avoid duplicates.
-   **Ad-hoc Fees**: Ability to add a single fee head (like a fine) without a full template.

## Real-World Scenarios

### Scenario 1: Beginning of Academic Year (Bulk Assign)
**Background**: The new session starts in April. 200 students are promoted to Class 10.
**Steps**:
1.  Admin selects **Batch Assignment**.
2.  Filters for: Class 10, All Sections.
3.  Selects Template: "Class 10 - General - 2024-25".
4.  Clicks **Preview**: Checks that 200 students are selected.
5.  Clicks **Assign**.
**Result**: All 200 students now have a due balance of ₹60,000 (or whatever the template total is).

### Scenario 2: Assigning Transport Fees (Selective Assign)
**Background**: Only 40 out of 200 students use the School Bus.
**Steps**:
1.  Admin selects **Batch Assignment**.
2.  Filters for: Class 10, Transport Users (if such a filter exists) OR manually ticks the 40 students.
3.  Selects Template: "Transport Fee - Zone A".
4.  Clicks **Assign**.
**Result**: Only those 40 students get the additional transport fee added to their dues.

### Scenario 3: Mid-Year Admission (Individual Assign)
**Background**: A new student, Rahul, joins Class 5 in September (halfway through the year).
**Steps**:
1.  Admin goes to **Student Assignment**.
2.  Searches for "Rahul".
3.  Selects Template: "Class 5 - General".
4.  System might ask: "Assign full year or pro-rata?"
5.  Admin manually adjusts the "Tuition Fee" to charges for Sept-March only (if policy dictates).
6.  Clicks **Assign**.
**Result**: Rahul is billed only for the months he will attend.

### Scenario 4: Charging a Late Fine (Ad-hoc)
**Background**: Student Priya returned a library book 10 days late.
**Steps**:
1.  Admin goes to Priya's profile in Fee Assignment.
2.  Clicks **Add Ad-hoc Fee**.
3.  Selects Fee Head: "Fine / Penalty".
4.  Enters Amount: ₹100.
5.  Enters Remark: "Library Book Late Return".
6.  Clicks **Save**.
**Result**: An extra ₹100 is added to Priya's next due payment.

### Scenario 5: Correcting a Wrong Assignment
**Background**: The Admin mistakenly assigned "Science Lab Fee" to a Commerce student.
**Steps**:
1.  Admin views the student's **Fee Ledger**.
2.  Locates the "Science Lab Fee".
3.  Since no payment has been made yet, Admin clicks **Delete/Remove Assignment**.
4.  Confirms deletion.
**Result**: The fee is removed, and the student's balance is corrected.

## Edge Cases & How to Handle Them

### Edge Case 1: Double Assignment
**What Happens**: Admin accidently assigns "Class 10 Fee" to the same students twice.
**System Behavior**: System detects that "Tuition Fee" for "Apr-2024" is already assigned. It blocks the duplicate or asks for confirmation.
**How to Handle**: Always check the "Already Assigned" count before confirming bulk actions.

### Edge Case 2: Assigning to Inactive/Alumni Students
**What Happens**: Admin selects "All Class 10" including students who left last year but weren't marked 'Alumni'.
**System Behavior**: Fees get assigned to students who are not in the school.
**How to Handle**: Ensure Student Database is clean. Use filters to select only "Active" students.

### Edge Case 3: Assignment Timeout (Large Batch)
**What Happens**: Trying to assign fees to 3000 students at once causes the browser to spin and crash.
**System Behavior**: Action fails, or only completes halfway (partial data).
**How to Handle**: Assign to smaller batches (e.g., one class at a time) rather than the whole school. Check server logs if unsure.

### Edge Case 4: Fee Head Deactivated During Assignment
**What Happens**: While Admin is preparing the assignment screen, another Admin deactivates a Fee Head.
**System Behavior**: The assignment might fail with "Invalid Fee Head" error.
**How to Handle**: Refresh the page to get the latest status of fee heads/templates.

### Edge Case 5: Assigning Cross-Class Templates
**What Happens**: Assigning a "Class 1 Template" to "Class 10 Students".
**System Behavior**: System usually allows this (flexible), assuming you might have a reason (e.g., remedial class).
**How to Handle**: Double-check the Template Name matches the Student Class selected.

### Edge Case 6: Assigning Fees to Student with Pending Dues
**What Happens**: Student has unpaid fees from last year.
**System Behavior**: New fees are simply added to the total balance. Old dues remain.
**How to Handle**: This is normal. The receipt system usually clears old dues first (FIFO - First In First Out).

### Edge Case 7: Partial Assignment (Network Failure)
**What Happens**: Internet cuts out while assigning to 50 students. Only 25 get assigned.
**System Behavior**: You see 25 successes and 25 failures.
**How to Handle**: Filter the list by "Fees Not assigned" and run the assignment again for the remaining students.

### Edge Case 8: Missing Mandatory Fees
**What Happens**: Admin manually removes a "Mandatory" fee (like Tuition) while assigning.
**System Behavior**: System blocks the action: "Tuition Fee is mandatory and cannot be removed."
**How to Handle**: Mandatory fees must be assigned. If valid exception, change the fee head settings first.

### Edge Case 9: Assigning "One-Time" Fee Twice
**What Happens**: Assigning "Admission Fee" to an old student who paid it 5 years ago.
**System Behavior**: System might not know the history 5 years back. It will assign it again.
**How to Handle**: Admin must be careful not to include One-Time fees in "Annual Renewal" templates.

### Edge Case 10: Zero Value Assignment
**What Happens**: Assigning a template where all values are 0.
**System Behavior**: Creates a fee record with 0 due.
**How to Handle**: Usually harmless, but clutters the database. Avoid doing this unless tracking "Free Ship" explicitly.

### Edge Case 11: Scholarship Application Order
**What Happens**: Admin applies scholarship first, then assigns fees.
**System Behavior**: Usually, you must assign the Full Fee *first*, then apply the Concession. You can't discount a fee that doesn't exist yet.
**How to Handle**: Always Assign Fee -> Then Apply Concession.

### Edge Case 12: Calendar Mismatch (Future Date)
**What Happens**: Assigning "Feb 2025" fees in "April 2024".
**System Behavior**: Fees appear in ledger but might not be "Due" yet (depending on settings).
**How to Handle**: Check the "Due Date" field carefully during assignment.

### Edge Case 13: Bulk Import vs UI Assignment
**What Happens**: Uploading assignments via Excel instead of using the UI.
**System Behavior**: Excel uploads might bypass some UI validations (like "Is Active check").
**How to Handle**: Be extra careful with data validation in Excel before uploading.

### Edge Case 14: SMS Notification Trigger
**What Happens**: System is configured to SMS parents on fee assignment.
**System Behavior**: 1000 SMS sent instantly, potentially alerting parents before Admin is ready.
**How to Handle**: Disable SMS triggers during bulk setup/maintenance windows.

### Edge Case 15: Rounding Differences
**What Happens**: Template says ₹100.33, assigned to 3 students. Total expected ₹300.99.
**System Behavior**: Ledger might show ₹301.00 or ₹300.99 depending on logic.
**How to Handle**: Accept minor rounding differences or use whole numbers for fees.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Student(s) | Multi-select | Yes | Who is being charged |
| Fee Template | Dropdown | No | Pre-defined structure to apply |
| Academic Year | Dropdown | Yes | Which year this fee belongs to |
| Due Date | Date | Yes | When this payment is expected |
| Fee Heads | List | Yes | Derived from template (can be modified if allowed) |
| Total Amount | Currency | Yes | Final sum to be posted to ledger |
| Remarks | Text | No | Comment for this assignment (e.g., "Late joining") |

## User Actions
1.  **Select Students**: Filter list by Class, Section, Admission No.
2.  **Choose Fee**: Pick a Template OR an individual Fee Head.
3.  **Customize (Optional)**: Adjust amounts for specific students if enabled.
4.  **Confirm Assignment**: System generates fee records.
5.  **Undo/Delete**: Remove assignment if no payment has been made against it.

## Business Rules
-   Fees cannot be assigned for a closed Academic Year.
-   Cannot remove a fee assignment if a Receipt has already been generated against it (must Cancel Receipt first).
-   One-time fees should generally strictly check for previous assignment.
-   Assignments must always have a Due Date.

## Permissions Required
-   **Create/Assign**: Fee Admin, Super Admin.
-   **Delete**: Super Admin only (sensitive action).
-   **View**: Accounts User, Fee Admin.

## Related Submodules
-   **1.2 Generic Fee Templates**: Source of the fee structures.
-   **1.4 Concession Configuration**: Applied AFTER fees are assigned.
-   **3.1 Implement Fee Collection**: The next step (taking payment).

## API Endpoints
```
POST /api/fee-assignments/bulk - Assign template to multiple students
POST /api/fee-assignments/individual - Add fee to single student
DELETE /api/fee-assignments/:id - Remove assignment
GET /api/students/:id/fee-ledger - View assigned fees for a student
```

## Database Schema
```sql
Table: student_fee_assignments
- id (PK)
- student_id (FK)
- fee_head_id (FK)
- academic_year_id (FK)
- original_amount (DECIMAL) -- Amount from template
- assigned_amount (DECIMAL) -- Actual amount charged
- due_date (DATE)
- is_paid (BOOLEAN)
- created_at (TIMESTAMP)
```

## UI/UX Considerations
-   **Progress Bar**: For bulk assignments, show a progress bar (e.g., "Assigning 45/200...").
-   **Summary Cards**: "Total Assignment Value: ₹50,00,000" before confirming.
-   **Error Handling**: If 1 out of 100 fails, report the specific failure without rolling back the successful 99.

## Best Practices
1.  **Verify First**: Always use the "Preview" button to check who is being assigned.
2.  **Batch Processing**: Assign fees class-by-class rather than all-school to manage load.
3.  **Clean Data**: Ensure Student Class/Section data is up-to-date before assignment.
4.  **Communication**: Inform parents *after* assignment is complete, not during.
