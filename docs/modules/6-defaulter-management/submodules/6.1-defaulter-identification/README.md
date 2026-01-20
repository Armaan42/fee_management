# 6.1 Defaulter Identification

## Overview
**Defaulter Identification** is the automated surveillance system of the fee management module. It continuously scans student records to identify who has missed their payment deadline. Instead of an accountant manually checking 2,000 ledgers, this module auto-flags the "rule-breakers" the moment the deadline crosss.

### Real-World Analogy
Think of this as a **Traffic Speed Camera**.
- **The Speed Limit**: The Fee Due Date (e.g., 10th of the month).
- **The Camera**: This module, watching every student account.
- **The Flash**: As soon as the clock strikes midnight on the 10th, the camera "flashes" for anyone with `Due Amount > 0`.
- **The Ticket**: The student is added to the "Defaulter List".

## Purpose
- **Automate Detection**: Eliminate manual lookups and human error.
- **Segment Offenders**: Categorize defaulters by severity (e.g., 1-month overdue vs. 3-months overdue).
- **Trigger Actions**: This is the "Trigger" for subsequent actions like SMS reminders, fines, or result blocking.
- **Filter Noise**: Ignore negligible dues (e.g., less than ₹50) to focus on real recovery.

## Key Features
- **Auto-Scan Scheduler**: Runs nightly or weekly to refresh the list.
- **Smart Filtering**: Configurable thresholds (Minimum Due Amount, Grace Period).
- **Exclusion Logic**: Whitelist specific groups (e.g., "Scholarship Students", "Staff Wards").
- **Aging Analysis**: Classifies dues into buckets (0-30 days, 31-60 days, 90+ days).

## Real-World Scenarios

### Scenario 1: The "Morning After"
**Situation**: The fee deadline was yesterday (10th May).
**Action**:
1.  System Auto-Job runs at 1:00 AM on 11th May.
2.  Scans 2,500 students.
3.  Finds 350 students with `Balance > 0`.
4.  **Result**: 350 names added to the "Defaulter Dashboard" with status "New Defaulter".
**Outcome**: Admin logs in at 9 AM and sees exactly who needs chasing.

### Scenario 2: The "Small Change" Filter
**Situation**: 50 students owe ₹10 or ₹20 due to previous rounding differences.
**Action**:
1.  Admin sets **"Minimum Defaulter Amount"** = ₹100.
2.  System scans again.
3.  It ignores the 50 students with small dues.
**Outcome**: The collections team focuses only on meaningful amounts, not annoying parents for ₹10.

### Scenario 3: The "Checks in the Mail"
**Situation**: A parent paid via Cheque on the due date, but it takes 2 days to clear.
**Action**:
1.  The Cheque is entered in the system with status "Deposited" (Submodule 5.3).
2.  Defaulter Logic checks: `Total Due - (Cleared Payment + Uncleared Cheques)`.
3.  **Result**: Net Due is 0. Student is NOT marked as a defaulter.
**Outcome**: Fair treatment. The parent paid on time; bank delay isn't their fault.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Grace Period** | Due Date is 10th, but School allows paying till 15th without tag. | Configure "Defaulter Tag Date" = Due Date + 5 Days. Student is "Overdue" but not "Defaulter" yet. |
| **Disputed Invoice** | Parent refuses to pay because the bill is wrong. | Admin marks the specific Due Installment as **"On Hold / Disputed"**. System skips this amount during scan. |
| **Partial Payment** | Parent paid ₹10,000 out of ₹15,000. | Still a defaulter, but categorized as "Partial Defaulter". Priority is lower than "Zero Payment". |
| **Technical Gateway Failure** | Gateway was down on last day. | Admin manually changes "Run Date" to +2 days, giving parents extra time before the "Defaulter Label" sticks. |
| **Staff Wards** | Teachers' children fees are deducted from salary, not paid online. | Add "Staff Child" category to the **Exclusion List**. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Student Name** | String | Name of the defaulter. |
| **Class/Section** | String | Academic cohort. |
| **Total Due** | Currency | Total outstanding amount. |
| **Days Overdue** | Integer | Count of days since the oldest unpaid invoice passed due date. |
| **Last Payment** | Date | When they last paid *anything*. |
| **Risk Category** | Enum | `Low`, `Medium`, `High`, `Critical`. |

## User Actions
1.  **Run Scan**: Manually trigger the defaulter identification process.
2.  **Download List**: Export the list to Excel for offline calling.
3.  **Exclude Student**: Manually remove a student from the list for this cycle (e.g., Principal's instructions).
4.  **View History**: See how many times a student has been a defaulter in the past.

## Best Practices
- **Run Nightly**: Data changes every day. A weekly scan is too slow.
- **Set Thresholds**: Don't sweat the small stuff. Set a reasonable minimum amount (e.g., ₹100).
- **communicate First**: Before "Defaulter" tag is public, ensure the first Reminder SMS has gone out.
