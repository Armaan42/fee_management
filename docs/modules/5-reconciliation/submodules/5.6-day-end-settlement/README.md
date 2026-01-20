# 5.6 Day End Settlement

## Overview
**Day End Settlement** (also known as EOD) is the final closure of the school's financial day. It freezes all transactions for the date, ensuring that no historical data can be altered. It consolidates reports from all counters, online gateways, and manual entries into a single "Daily Collection Report" (DCR).

### Real-World Analogy
Think of this as **Locking the Main Safe**.
Throughout the day, individual cashiers (counters) have been working.
1.  **Shift End**: Cashiers count their tills and hand over cash to the Manager.
2.  **Consolidation**: The Manager verifies the total cash from all 5 counters + online bank credits.
3.  **Lock Up**: The Manager puts the cash in the Main Safe and locks it.
4.  **Reporting**: A text message is sent to the School Owner: "Total Collection Today: ₹5 Lakhs".
Once the safe is locked, you can't put more money in or take it out until tomorrow.

## Purpose
- **Financial Integrity**: Prevents back-dated entries (e.g., trying to slip in a receipt for yesterday).
- **Consolidation**: Gives a 360-degree view of Cash + Cheque + Online collections.
- **Reporting**: Triggers automated emails with the DCR to management.
- **Bank Prep**: Generates the final deposit slip for the next morning.

## Key Features
- **Multi-Counter Sync**: Pulls data from Counter 1, Counter 2, Library, and Transport Desk.
- **Business Date vs System Date**: Allows closing "Yesterday's" accounts even if the admin is working at 1 AM today.
- **Hard Freeze**: Locks the "Edit/Cancel" buttons for all receipts of the closed date.
- **Auto-Emailer**: Sends PDF summary to configured email IDs.

## Real-World Scenarios

### Scenario 1: The Manager's Approval
**Situation**: 3 Cashiers have submitted their shift reports.
**Action**:
1.  Finance Manager logs in to **Day End**.
2.  Review's Counter 1: "Matched".
3.  Review's Counter 2: "Shortage of ₹100" (Manager adds remark: "Deduct from Salary").
4.  Review's Counter 3: "Matched".
5.  **Action**: Manager clicks **"Run Day End Process"**.
**Outcome**: All counters are finalized. System Date moves to the next business day.

### Scenario 2: The Late Night Entry
**Situation**: It's 11 PM. Staff forgot to enter one manual receipt collected at 4 PM.
**Action**:
1.  Day End is NOT yet run.
2.  Staff logs in, enters the receipt with "Transaction Date = Today".
3.  Manager verifies it.
4.  Manager runs Day End at 11:30 PM.
**Outcome**: The transaction is correctly included in today's report.

### Scenario 3: Bank Holiday Handling
**Situation**: Friday settlement done. Saturday/Sunday are holidays.
**Action**:
1.  Friday's Cash remains in "Cash in Hand" ledger.
2.  Monday Morning: "Cash Handover" report shows opening balance of Friday's collection.
3.  Admin creates a "Bank Deposit" entry on Monday to clear the safe.
**Outcome**: Continuous tracking of cash movement across holidays.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Re-Opening Day** | Critical error found AFTER Day End (e.g., entered ₹50,000 instead of ₹5,000). | Restricted Action. Requires Super Admin "OTP" or "Password" to "Unfreeze" the day. Triggers High-Severity Audit Alert. |
| **Pending Reconciliation** | Online payments haven't been reconciled yet. | System allows Day End for *Cash* but keeps *Online* ledgers open? No, usually Day End freezes Cash/Counter ops only. |
| **Negative Cash** | Admin tries to deposit more money into bank than "Cash in Hand". | Block the transaction. "Insufficient Cash Balance". Check if a receipt was missed. |
| **Shift Overlap** | Night shift staff collecting fees for "Tomorrow". | System should differentiate between "Shift 1 (Today)" and "Shift 2 (Tomorrow)" receipts based on time configuration. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Settlement Date** | Date | The business date being closed. |
| **Closed By** | User | Manager who clicked the button. |
| **Total Cash** | Currency | Physical cash verified. |
| **Total Cheques** | Currency | Value of instruments collected. |
| **Total Online** | Currency | Value of digital receipts. |
| **Cash In Safe** | Currency | Running balance of cash (Opening + Coll - Deposit). |
| **Status** | Status | `Open`, `In Progress`, `Closed`. |

## User Actions
1.  **Verify Counters**: Check status of individual till closures.
2.  **Add Expense**: Record petty cash expenses (Tea/Stationery) before closing.
3.  **Run Settlement**: The "Big Red Button" to close the day.
4.  **Print DCR**: Generate the Daily Collection Report.

## Best Practices
- **Never Share Passwords**: The Day End authority should be with one senior person only.
- **Deposit Next Morning**: The "Cash in Safe" should ideally be zeroed out every morning by depositing to the bank.
- **Check Shortages**: Don't run Day End if there is an unresolved shortage. Solve it or Record it first.
