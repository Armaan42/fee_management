# 5.4 Gateway Settlement Matching

## Overview
**Gateway Settlement Matching** reconciles the money collected online. Payment gateways (like Razorpay/Stripe) don't deposit money for every single student immediately. Instead, they bundle hundreds of payments into a "Payout" or "Settlement" and transfer the lump sum to the school's bank account, often deducting their commission. This module untangles that lump sum to verify exactly whose fees have been received.

### Real-World Analogy
Think of this as solving a **Jigsaw Puzzle**.
The Bank sends you a big box (The Settlement Check), and the image on the box says "₹5,00,000". But inside, there are 200 small pieces (Student Payments).
- You need to fit every piece (Student Receipt) into the frame.
- If a piece is missing (Bank didn't pay for Rahul), the picture is incomplete.
- If a piece doesn't fit (Charges deducted), you need to trim the edges (Record Expense) to make it fit.

## Purpose
- **Verify Cash Flow**: Confirm that the "Success" on the screen turned into real money in the bank.
- **Track Expenses**: Automatically separate the Fee Amount (Income) from the Gateway Charges (Expense).
- **Detect Withholding**: Identify if the gateway is holding back money for any specific transaction (Risk Hold).
- **Close the Loop**: Mark school receipts as "Settled" so they are locked for editing.

## Key Features
- **Auto-Import**: Upload the Settlement .CSV file from the gateway dashboard.
- **Fee Splitter**: Automatically calculates Net Amount = Gross Amount - TDR (Transaction Discount Rate) - GST.
- **Settlement ID Tracking**: Tags every independent receipt with the Bank's Batch ID (UTR Number).
- **Exception flagging**: Highlights transactions present in school records but missing from the bank payout.

## Real-World Scenarios

### Scenario 1: The Weekly Payout
**Situation**: Razorpay transfers ₹3,45,000 to the school account on Monday.
**Action**:
1.  Admin uploads the Razorpay Settlement Report.
2.  System scans the file and finds 150 student payments totaling ₹3,50,000.
3.  It calculates ₹5,000 as Gateway Charges.
4.  **Match**: ₹3.50L (Gross) - ₹5k (Fees) = ₹3.45L (Net). Matches perfectly!
5.  **Result**: 150 Receipts are marked "Settled". One Expense Entry of ₹5,000 is posted.

### Scenario 2: The Chargeback Deduction
**Situation**: Bank payout is less than expected.
**Action**:
1.  System highlights a discrepancy: "Expected ₹1,00,000, Received ₹98,000".
2.  Drilling down, it finds a "Debit Adjustment" row in the CSV.
3.  Reason: "Chargeback - Parent Disputed Transaction #998877".
4.  **Result**: Creating a "Dispute Ticket" for that student and alerting the Finance Manager.

### Scenario 3: The Missing Transaction
**Situation**: A parent sent a screenshot of success, but the money isn't in the payout.
**Action**:
1.  Admin searches the Settlement Report for that Order ID.
2.  **Result**: Not found.
3.  Admin checks the Gateway Dashboard: Status is "Captured" but "Settlement Due Date" is tomorrow.
4.  **Outcome**: No panic. The money is safe, just in the next batch.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Penny Drop** | Rounding errors cause a ₹0.02 difference (e.g., ₹100.333 vs ₹100.33). | Configure a "Tolerance Limit" of ±₹1. System auto-approves differences within this limit as "Rounding Expense". |
| **Combined Payout** | One payout includes fees, uniform sales, and fine collections. | System uses "Order ID Prefixes" to route money to different ledgers (e.g., `FEE_` to Tuition, `UNI_` to Store). |
| **Gateway Refund** | Gateway initiates a refund directly to the parent. | Settlement file will show a Negative row. System auto-creates a "Refund Journal" to reverse the income. |
| **Unknown Order** | Payout contains money for an ID not in the Database. | Flag as "Suspense - Investigation Required". Check if it belongs to a sister branch or test account. |
| **Failed Settlement** | Bank transfer fails (bounces back to gateway). | Mark the entire Batch as "Bounced". No receipts are marked settled. Wait for re-initiation. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Settlement UTR** | String | Bank's Unique Transaction Reference number. |
| **Settlement Date** | Date | When the money hit the account. |
| **Gross Amount** | Currency | Total collected from parents. |
| **Tax/Fees** | Currency | Commission kept by Gateway. |
| **Net Amount** | Currency | Amount deposited to School. |
| **Count** | Integer | Number of receipts in this batch. |

## User Actions
1.  **Fetch Settlement**: Click "Sync" (if API connected) or "Upload" (if manual).
2.  **Review Match**: Check the "Matched vs. Unmatched" summary.
3.  **Approve**: Post the accounting entries.
4.  **Investigate**: Open the "Unmatched" tab to see problem cases.

## Best Practices
- **Automate It**: Use the Gateway API feature to auto-fetch settlements daily at 2 AM. Avoid manual uploads.
- **MDR is an Expense**: Never subtract fees from the student's payment. If fee is ₹100, record Income ₹100 and Expense ₹2. Don't record Income ₹98.
- **Check UTRs**: Always verify that the UTR in the report matches the UTR in your Netbanking statement.
