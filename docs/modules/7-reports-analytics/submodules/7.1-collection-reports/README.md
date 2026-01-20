# 7.1 Collection Reports

## Overview
**Collection Reports** act as the financial pulse check of the institution. They summarize the inflow of money across various dimensions—time, mode, user, and head. This module transforms raw transaction data into actionable "Headline" summaries for management.

### Real-World Analogy
Think of this as your **Morning Newspaper**.
You don't have time to read every single police log or stock trade (Raw Transactions). You just read the headlines:
- **"City Safe"** (Total Collection Match)
- **"Market Up"** (Online Payments Increased)
- **"Weather Alert"** (Cash Flow Dip)
The **Daily Collection Report (DCR)** is exactly that—a one-page summary placed on the Principal's desk every morning, telling the financial story of yesterday.

## Purpose
- **Transparency**: Ensure every rupee collected is accounted for and visible to the management.
- **Trend Analysis**: Identify peak collection periods (e.g., April/May) to plan investments.
- **Audit Readiness**: Provide a serialized, immutable record of daily income for external auditors.
- **Performance Tracking**: Measure which fee counter or cashier is processing the most transactions.

## Key Features
- **Dimension Slicing**: View data by Date, Class, Fee Head (Tuition/Transport), or Payment Mode.
- **Drill-Down Capabilities**: Click on "Class 10 Total" to see the list of individual students.
- **Export Formats**: One-click download to Excel (for analysis) or PDF (for signing).
- **Scheduled Delivery**: Auto-email the DCR to the Chairman at 6:00 PM every day.

## Real-World Scenarios

### Scenario 1: The Daily Huddle
**Situation**: The Principal wants to know yesterday's total income before the morning meeting.
**Action**:
1.  Opens **"Daily Collection Report"**.
2.  Selects Date = Yesterday.
3.  **Result**: "Total: ₹5,00,000" (Cash: ₹2L, Cheque: ₹1L, Online: ₹2L).
4.  **Insight**: Online payments are rising; maybe we can reduce one cash counter next year.

### Scenario 2: The "Fee Head" Split
**Situation**: The Transport Manager asks, "How much did we collect for buses this month?"
**Action**:
1.  Opens **"Head-wise Collection Report"**.
2.  Filters by "Fee Head = Transport Fee".
3.  **Result**: ₹15,00,000.
4.  **Outcome**: Manager confirms budget availability for new tires.

### Scenario 3: The "Null" Day
**Situation**: It was a Sunday or National Holiday.
**Action**:
1.  System generates the daily report.
2.  **Result**: "Total Collection: ₹0".
3.  **Outcome**: This "Zero Report" is crucial. It proves that *no* money was secretly collected on a holiday. It maintains the continuity of the audit trail.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Back-Dated Receipts** | Receipt entered Today (10th) but Transaction Date set to Yesterday (9th). | **Two Reports**: <br>1. **Transaction Report**: Shows it on the 9th. <br>2. **Entry Report**: Shows it on the 10th (for Cash Handover reconciliation). |
| **Cancelled Receipts** | A receipt of ₹5,000 was cancelled due to error. | Report shows: <br>Gross: ₹1,00,000 <br>Cancelled: (-) ₹5,000 <br>Net Collection: ₹95,000. <br>Never delete a receipt; always show it as cancelled (strikethrough). |
| **Bounced Cheque Reversal** | Cheque collected last month bounces today. | Current Day's report shows a **"Debit / Reversal"** section. It does NOT reduce today's *New Collection* figure but reduces the *Cumulative Balance*. |
| **Unsettled Online Payments** | Payment is "Success" in Gateway but money not in Bank. | Report classifies it as "Online - Transit". It moves to "Online - Settled" only after Reconciliation (Module 5.4). |
| **Multi-Campus View** | Group Chairman wants total of Branch A + Branch B. | **"Consolidated Group Report"**: Aggregates data from multiple databases into a single dashboard view. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Report Date** | Date | The period covered. |
| **Fee Head** | String | Category (Tuition, transport, Fine). |
| **Mode** | Enum | Cash, Cheque, UPI, Card. |
| **User** | String | Staff who collected the fee. |
| **Receipt Range** | String | "Rec# 1001 to Rec# 1050". |
| **Total Amount** | Currency | Sum of net receipts. |

## User Actions
1.  **Generate Report**: Select filters and click "View".
2.  **Schedule Email**: "Send this report to principal@school.com every Monday."
3.  **Print Summary**: Generate a skinny thermal-printer summary for the cash drawer.
4.  **Compare Periods**: "Compare Jan 2024 vs Jan 2023".

## Best Practices
- **Sign Off Daily**: The Accountant and Principal should physically (or digitally) sign the DCR every day.
- **Separate "Refunds"**: Don't just subtract refunds from collection. Show "Total Collection" and "Total Refunds" as separate line items for clarity.
- **Use Graphs**: A bar chart of "Last 7 Days Collection" is instantly more readable than a table of numbers.
