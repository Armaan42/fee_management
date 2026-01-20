# 10.2 Academic Year Rollover

## Overview
**Academic Year Rollover** is the grand finale of the school year. It is the automated process of closing one accounting period and opening the next. It involves promoting students to higher classes, determining who passed/failed, and most importantly, carrying forward pending dues as "Arrears" into the new financial ledger.

### Real-World Analogy
Think of this as a **TV Show Season Finale**.
- **Season 1 Ends**: The current academic year (e.g., 2023-24) is wrapped up.
- **Cliffhangers (Arrears)**: Unresolved storylines (unpaid fees of ₹5000) are carried over to Season 2.
- **Season 2 Begins**: The cast (Students) moves to a new setting (Class 5 becomes Class 6).
- **The Pilot Episode**: The opening balance of the new season is exactly the closing balance of the old one.
This module executes this transition seamlessly for thousands of students in a few clicks.

## Purpose
- **Promotion**: Bulk update student records (Class 1 -> Class 2).
- **Financial Continuity**: Ensure that debt is not lost. The ₹5000 due in March '24 becomes "Opening Due" in April '24.
- **Archive History**: Freeze the 2023-24 data as "Read Only" for future audits, while making 2024-25 active for editing.
- **Housekeeping**: Remove "Passout" students (Class 12) from the active billing cycle and mark them as Alumni.

## Key Features
- **Bulk Promotion**: "Move all students of Class 5A to 6A" logic.
- **Smart Carry Forward**: Options to carry forward "All Dues", "Principal Only", or "Write-off Small Amounts (<₹10)".
- **Detention Handling**: Manually untick students who failed, keeping them in the same class while resetting their fees for the new year.
- **Alumni Migration**: Auto-move Class 10/12 students to the "Alumni Database".

## Real-World Scenarios

### Scenario 1: The Standard Promotion
**Situation**: Session changes from 2023 to 2024.
**Action**:
1.  Admin runs **Rollover Wizard**.
2.  Selects: "Promote Class 1 to 2", "2 to 3", etc.
3.  **Outcome**: 2000 student profiles are updated with "Current Class: [New Class]". Fee Balances are moved to "Previous Year Arrears".

### Scenario 2: The "Detained" Student
**Situation**: Rohan failed in Class 9. He must repeat the year.
**Action**:
1.  In the wizard, Admin unchecks Rohan from the "Promote to Class 10" list.
2.  **Outcome**: Rohan remains in Class 9 for 2024. His old dues are carried forward, and new Class 9 fees are assigned again.

### Scenario 3: The Financial Clean Slate
**Situation**: School decides to waive off all late fines from the previous year before starting the new one.
**Action**:
1.  Admin selects: Carry Forward **"Tuition and Transport Only"** (Exclude "Fine Balance").
2.  **Outcome**: Students start the new year with only principal arrears. The penalty debt is wiped clean.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Pending Refunds** | Student has an *excess* payment of ₹500 (Credit Balance). | **Carry Forward as Credit**: The new year opening balance should be -₹500 (Advance), which will auto-adjust against the first month's fee. |
| **Mid-Process Crash** | Power failure during the rollover of 5000 students. | **Transaction Safety**: The process runs in "Batches of 50". If it crashes at batch 10, restarting it will resume from batch 11, skipping the already processed ones. |
| **Section Change** | Class 5A students are shuffled into 6A and 6B. | **Staging Area**: Promote everyone to "Class 6 - Unassigned Section". Then use the "Section Shuffler" tool to allocate sections based on new criteria. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **From Year** | Year | 2023-24. |
| **To Year** | Year | 2024-25. |
| **Transfer Dues** | Boolean | True = Carry forward debt. |
| **Transfer Credit** | Boolean | True = Carry forward advance. |
| **Write-off Limit** | Currency | "Ignore dues < ₹10". |
| **Status** | Enum | Pending, In-Progress, Completed. |

## User Actions
1.  **Simulate Rollover**: "Dry Run" to see how many students will move and what the total opening balance will be.
2.  **Execute Rollover**: The actual commit button. (Irreversible without backup).
3.  **View Exception Report**: "List of 5 students who could not be promoted due to data errors".

## Best Practices
- **Backup Mandatory**: The system forces the user to Download a Full DB Backup before enabling the "Start Rollover" button.
- **Off-Peak Execution**: Run this process on a Saturday evening or Sunday when no fee collection is happening.
- **Audit Freeze**: Once rolled over, mark the Previous Year is "Locked" to prevent back-dated edits that ruin the Opening Balance.
