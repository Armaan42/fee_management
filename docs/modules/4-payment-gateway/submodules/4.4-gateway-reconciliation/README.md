# 4.4 Gateway Reconciliation

## Overview
**Gateway Reconciliation** is the accounting checkpoint. It ensures that the funds marked as "Received" in the school software truly match the funds deposited into the school's bank account. This submodule automates the tedious process of matching thousands of transactions against bank settlement reports.

### Real-World Analogy
Think of this as **Balancing the Cash Register** at the end of a shift.
- **Sales Record**: Your POS machine (School Software) says you sold ₹10,000 worth of items.
- **Cash Count**: You count the cash in the drawer (Bank Account).
- **Matching**: Ideally, you should have ₹10,000. If you have ₹9,900, you need to find the missing ₹100.
This module uses a "Settlement Report" from the bank to automatically tick off every transaction that has safely landed in the account.

## Purpose
- **Verify Deposits**: Confirm that money collected online is actually available for use.
- **Identify Discrepancies**: Spot missing payments, short settlements, or unexpected charges.
- **Calculate Net Income**: Account for Gateway Charges (MDR) and Tax deducted by the provider.
- **Audit Compliance**: Provide a clean "Book vs. Bank" report for financial auditors.

## Key Features
- **Auto-Import**: Upload settlement CSVs from Razorpay/Stripe, and the system matches them automatically.
- **MDR Tracking**: Automatically records the "Merchant Discount Rate" (gateway fee) as an expense.
- **Date Matching**: Links a payment made on Monday to its settlement on Wednesday (T+2 cycle).
- **Exception Reporting**: Highlights "Unsettled" or "Under-settled" transactions for manual review.

## Real-World Scenarios

### Scenario 1: The T+2 Settlement Check
**Situation**: Parents paid ₹5 Lakhs on Monday. It is now Wednesday.
**Action**:
1.  Accountant downloads the "Settlement Report" from the Gateway Dashboard.
2.  Uploads it to **Gateway Reconciliation**.
3.  System scans 200 transactions.
4.  Shows: "198 Matched, 2 Pending".
**Outcome**: Accountant gets peace of mind that 99% of funds are safe and investigates the 2 pending ones.

### Scenario 2: Accounting for Commission (MDR)
**Situation**: Parent paid ₹10,000. Bank deposited ₹9,800 (keeping ₹200 as fee).
**Action**:
1.  Without this module, the accountant manually enters an expense entry for ₹200.
2.  With Reconciliation active, the system sees: Expected ₹10,000, Received ₹9,800.
3.  Auto-creates a Journal Entry: "Bank Debit ₹9,800, Bank Charges Debit ₹200, Fee Credit ₹10,000".
**Outcome**: Zero manual data entry for thousands of transactions.

### Scenario 3: The Chargeback Surprise
**Situation**: A parent disputed a payment with their credit card company, and the money was pulled back.
**Action**:
1.  Reconciliation report shows a negative entry (Debit) for a previous transaction.
2.  System flags the Student Fee Receipt as "Disputed/Reversed".
3.  Alerts the Admin to contact the parent.
**Outcome**: Prevents the school from counting that money as "income" effectively.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Timing Mismatch** | Parent pays at 11:59 PM (Day 1). School records Day 1. Bank processes on Day 2. | System matches based on "Order ID" rather than strict Date to handle timezone/cutoff differences. |
| **Bulk Deposit** | Bank deposits one lump sum of ₹50,00,000 for 5,000 transactions. | System parses the detailed "breakdown file" to match each individual student payment against the lump sum. |
| **Offline Refund** | Gateway Support refunded a parent directly, but school software doesn't know. | Reconciliation will show a mismatch (System: Paid, Bank: Refunded). Admin must manually mark the receipt as "Refunded" in software. |
| **Penny Drop** | Rounding differences (e.g., ₹100.33 vs ₹100.34) causing mismatch. | Allow a configurable "Tolerance Limit" (e.g., ±₹1.00) to auto-approve insignificant differences. |
| **Unknown txn** | Settlement contains money for a transaction ID that doesn't exist in school DB. | Flag as "Suspense Account". Required investigation (possibly from another branch or test account). |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Settlement ID** | String | Unique batch ID from the bank. |
| **Settlement Date** | Date | The date money hit the bank account. |
| **Gross Amount** | Currency | Total collected (Parent paid). |
| **MDR/Fees** | Currency | Amount deducted by gateway. |
| **Net Amount** | Currency | Actual amount deposited (Gross - Fees). |
| **Status** | Status | `Reconciled`, `Partially Reconciled`, `Unreconciled`. |
| **Breakdown** | Link | Link to the list of individual transactions in this batch. |

## User Actions
1.  **Upload Statement**: Drag and drop the settlement CSV.
2.  **Auto Reconcile**: Click button to run the matching algorithm.
3.  **Resolve Exceptions**: Manually fix the few red-flagged rows.
4.  **Post to Accounts**: Finalize the batch to update the General Ledger.

## Best Practices
- **Reconcile Weekly**: Don't wait for month-end. Weekly checks keep the data manageable.
- **Track MDR Separate**: Always separate the Gateway Fee from the Collection Amount for accurate budget reporting.
- **Automate Feed**: If using a premium gateway, enable "Auto-Fetch Settlement" API to skip manual file uploads.
