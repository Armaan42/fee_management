# 10.3 Bulk Fee Assignment

## Overview
**Bulk Fee Assignment** is the engine of efficiency in fee management. While individual student profile edits are fine for corrections, setting up fees for 5,000 students requires power tools. This module allows the Administrator to "Broadcast" fees to entire classes, sections, or custom groups in a single click.

### Real-World Analogy
Think of this as a **Helicopter Airdrop / Crop Dusting**.
- **Manual Method**: Walking to every house to hand-deliver a package (Assigning fee one-by-one). Slow and tiring.
- **Bulk Method**: Flying a helicopter over the city and dropping packages on every roof (Assigning fee to "All Class 10"). Fast and uniform.
Whether it's the Monthly Tuition Fee or a sudden "Picnic Charge", this module spreads it across the target population instantly.

## Purpose
- **Efficiency**: Assign fees to 100 students in 2 seconds instead of 2 hours.
- **Consistency**: ensures every student in Class 5A gets exactly the same fee amount, eliminating manual data entry errors.
- **Dynamic Targeting**: Allows complex filters like "All Students using Bus Route 5" or "All Girls in Class 11".
- **Retroactive Correction**: If a fee was missed during admission, this tool can "patch" it for everyone later.

## Key Features
- **Smart Filters**: Select Audience by Class, Section, Board, House, Gender, Transport Route, or Admission Year.
- **Idempotency**: Prevents double-billing. If you run the assignment twice, it skips students who already have that fee.
- **Preview & Commit**: Shows a "Review List" (e.g., "This will affect 45 students") before the final save.
- **Exclusion List**: Ability to uncheck specific students (e.g., "Assign to all Class 10 except Staff Wards").

## Real-World Scenarios

### Scenario 1: The Annual Setup
**Situation**: New Academic Year starts. Admin needs to assign Tuition Fee for April.
**Action**:
1.  Admin selects Fee Head: **"Tuition Fee Class 10"**.
2.  Filter: **Class = 10**, **Section = All**.
3.  Click **"Assign"**.
4.  **Outcome**: 150 invoices generated instantly.

### Scenario 2: The Fuel Hike
**Situation**: Diesel prices went up. School adds a surcharge for bus users only.
**Action**:
1.  Admin creates "Fuel Surcharge: ₹200".
2.  Filter: **Transport Users Only** (excludes Walkers/Cyclists).
3.  Click **"Assign"**.
4.  **Outcome**: Only the 800 students who use the bus see the extra charge. The rest are unaffected.

### Scenario 3: The Late Admitted Student
**Situation**: Ravi joins in July. He needs to pay April, May, and June fees too.
**Action**:
1.  Admin selects Fee Head: **"Term 1 Fee"**.
2.  Filter: **Student = Ravi**.
3.  **Outcome**: System applies the back-dated fees to just his profile.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Duplicate Assignment** | Admin accidentally clicks "Assign" twice for April Fee. | **Safety Check**: System queries: "Does Student X already have Fee Y for Period Z?". If Yes, SKIP. If No, INSERT. Result: No double billing. |
| **RTE Students** | Government mandates 0 fees for RTE category. | **Auto-Exclusion**: If Filter = "All Class 1", the system automatically subtracts students where Category = "RTE", unless explicitly overruled. |
| **Old Leavers** | Assigning fees to a student who left the school last month. | **Status Check**: The query filters only `Status = 'Active'`. TC issued / Alumni students are ignored. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Fee Head** | Dropdown | "Computer Fee". |
| **Amount** | Currency | ₹500 (Override default if needed). |
| **Due Date** | Date | 10th of Month. |
| **Target Audience** | JSON | `{"Class": ["10"], "Gender": ["F"]}`. |
| **Exclusions** | List | IDs of students to skip. |
| **Action** | Enum | Add, Overwrite, Remove. |

## User Actions
1.  **Filter**: "Show me count of students in Class 5".
2.  **Dry Run**: "Simulate assignment" to check total expected revenue.
3.  **Rollback**: "Undo the last batch" (e.g., if wrong amount was assigned).
4.  **View Log**: "Who assigned this fee to Class 8?"

## Best Practices
- **Verify Count**: Always check "Selected Students: 45" matches your class register before clicking Submit.
- **Don't Rush**: For critical fees (Annual Fee), apply to one section first (Pilot Test) before applying to the whole school.
- **Notifications**: After bulk assignment, use Module 9 to send a "Fee Generated" SMS so parents know new dues are visible.
