# 5.1 Daily Cash Reconciliation

## Overview
**Daily Cash Reconciliation** is the end-of-day ritual for every fee counter. It ensures that the cash physically present in the drawer matches exactly with the collection records in the software. This step is crucial to prevent internal fraud, theft, or honest counting errors.

### Real-World Analogy
Think of this as **Closing the Till** at a supermarket.
When a cashier's shift ends, they don't just walk away. They verify:
1.  **System Says**: You sold items worth ₹50,000 in cash.
2.  **Physical Count**: You count the notes in the drawer -> ₹49,500.
3.  **Result**: Shortage of ₹500.
This module digitizes this process, forcing the cashier to enter the "Physical Count" (how many 500s, 100s, etc.) before the system generates the "Day End Report".

## Purpose
- **Detect Leakage**: Identify missing cash immediately, not weeks later.
- **Enforce Accountability**: Every cashier is responsible for their own drawer.
- **Digitize Denominations**: Track the exact breakdown of currency notes for bank deposit slips.
- **Enable Handovers**: Smoothly transfer responsibility from Morning Shift to Evening Shift.

## Key Features
- **Denomination Calculator**: Built-in tool to count notes (e.g., 100 x ₹500 = ₹50,000).
- **Blind Reconciliation**: Option to hide the "Expected Amount" so the cashier *must* count honestly without bias.
- **Overage/Shortage Tracking**: Automatically flags discrepancies for the Finance Manager to approve.
- **Digital Sign-off**: Clicks serve as a digital signature confirming "I possess this cash".

## Real-World Scenarios

### Scenario 1: The Perfect Shift
**Situation**: John collects fees from 9 AM to 2 PM.
**Action**:
1.  John clicks "Close Counter".
2.  System asks "Enter Cash Details".
3.  John counts: 50 notes of ₹500, 20 notes of ₹100. Total entered: ₹27,000.
4.  System checks: Receipts generated = ₹27,000.
5.  **Status**: "Matched". John prints the report and hands cash to the manager.
**Outcome**: Clean audit trail.

### Scenario 2: The Shortage (Honest Error)
**Situation**: Sarah closes her counter. System expects ₹40,000. She finds only ₹39,500.
**Action**:
1.  She recounts twice. Still ₹39,500.
2.  She enters ₹39,500 in the module.
3.  System highlights: **SHORTAGE (-₹500)**.
4.  She adds a remark: "Possible mistake in giving change to student Rahul (Class 5)".
5.  Manager receives an alert to investigate.
**Outcome**: Discrepancy recorded immediately. Manager can check CCTV or ask Sarah to pay the difference.

### Scenario 3: Bank Deposit Prep
**Situation**: Use collected cash to prepare a bank deposit slip.
**Action**:
1.  The module's "Denomination Table" (e.g., 2000x0, 500x40, 100x10) is auto-printed on the "Cash Handover Report".
2.  The Admin simply attaches this report to the bank Pay-in Slip.
**Outcome**: Saves time writing denomination details manually at the bank.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Excess Cash** | Drawer has ₹50 more than receipts. | Record as **OVERAGE (+₹50)**. Usually means a receipt wasn't generated for a small payment. Money goes to "Suspense Account". |
| **Pending Receipts** | A receipt was generated but printer jammed, and transaction wasn't saved properly. | Check "Failed Transactions" module first. If money was taken, mark receipt as "Manual Success" before reconciling. |
| **Petty Cash Use** | Staff took ₹200 from collection for office tea (Bad Practice). | System expects full amount. Staff must enter "Expense Voucher: ₹200" in the counter system to balance the till. |
| **Counterfeit Note** | Bank identifies a fake 500 note the next day. | The specific cashier's reconciliation report is reopened. The shortage is assigned to that cashier retrospectively. |
| **System Offline** | Internet was down, fees collected on manual receipt book. | "Offline Mode Entry": Admin must bulk-enter all manual receipt numbers into the system before closing the digital till. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Session ID** | String | Unique ID for the cashier's login session. |
| **Cashier Name** | String | User who collected the money. |
| **Opening Balance** | Currency | Cash present in drawer at start of shift (Float). |
| **System Collections** | Currency | Total calculated from generated receipts. |
| **Physical Cash** | Currency | Amount manually entered by cashier. |
| **Difference** | Currency | Physical - System (Negative = Shortage). |
| **Notes** | JSON | Breakdown of denominations (e.g., `{"500": 10, "100": 5}`). |

## User Actions
1.  **Open Counter**: Start the shift with an opening balance (Float).
2.  **Enter Denominations**: Input the count of physical notes.
3.  **Submit Reconciliation**: Lock the session and generate the report.
4.  **Approve/Reject**: Finance Manager accepts the report or sends it back for recounting.

## Best Practices
- **Blind Count**: Configure the system to hide the "Expected Amount" until the cashier enters their count. This prevents lazy counting.
- **No Personal Cash**: Strictly forbid keeping personal wallets in the fee drawer to avoid mix-ups.
- **Zero Tolerance**: Investigate even small shortages (₹10) to maintain discipline.
