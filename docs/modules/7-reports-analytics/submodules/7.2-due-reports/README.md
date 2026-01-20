# 7.2 Due Reports

## Overview
**Due Reports** identify the "Receivables" of the school—money that has been invoiced but not yet collected. While collection reports celebrate what you have earned, due reports highlight the gap between "Projected Revenue" and "Actual Revenue".

### Real-World Analogy
Think of this as a **Bill Collector's Ledger**.
A shopkeeper opens his big red book to see:
- **Who owes money?** (Student Name)
- **How much?** (Balance Amount)
- **For how long?** (Aging: 30 days vs 300 days)
Without this report, the school is flying blind, hoping parents pay on time, rather than actively managing the collection pipeline.

## Purpose
- **Targeted Follow-up**: Provide class teachers with a specific list of 5 students to call, rather than calling the whole class.
- **Cash Flow Forecasting**: Estimate how much money is *likely* to come in next month based on outstanding invoices.
- **Bad Debt Identification**: Highlight dues that are so old (e.g., > 2 years) they might need to be written off.
- **Certificate Blocking**: A quick lookup tool for the Admin before issuing a Transfer Certificate (TC).

## Key Features
- **Aging Buckets**: Automatically segments dues into 0-30 days, 31-60 days, 60-90 days, and 90+ days.
- **Head-wise Breakdown**: Shows "Total Tuition Due" vs "Total Transport Due" separately.
- **Threshold Filters**: "Show me only students who owe more than ₹5,000".
- **Dynamic Sorting**: Sort by "Highest Due Amount" to focus on the big fish first.

## Real-World Scenarios

### Scenario 1: The Class Teacher's List
**Situation**: The Principal wants Class Teachers to remind parents during the PTM (Parent-Teacher Meeting).
**Action**:
1.  Admin generates **"Class-wise Due Report"**.
2.  Filters for "Class 10-A, 10-B, 10-C".
3.  Prints 3 separate PDFs.
4.  Teachers receive a clean list: "Rahul: ₹5000, Snigdha: ₹2000".
**Outcome**: Teachers have accurate data to discuss with parents face-to-face.

### Scenario 2: The Transport Crisis
**Situation**: The Transport Contractor needs payment, but the school is low on cash.
**Action**:
1.  Trustee asks: "Why is the Transport fund empty?"
2.  Admin runs **"Head-wise Due Report"** for "Transport Fee".
3.  **Result**: "Outstanding Transport Dues: ₹25 Lakhs".
4.  **Action**: School sends a targeted SMS specifically to these parents: "Bus service will stop if dues not cleared."

### Scenario 3: The Board Exam Clearance
**Situation**: 1 month before Board Exams.
**Action**:
1.  Admin runs **"Consolidated Due Report"** for Class 10 & 12.
2.  Filters: "Due > ₹0".
3.  **Result**: List of 15 students who cannot receive Hall Tickets yet.
4.  **Action**: This list is pasted on the notice board (or sent privately) as the "Defaulter List".

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Future Dues** | Report shows "Due: ₹50,000" but includes installments due next month. | Use **"Due Till Date"** filter. If today is Jan, exclude Feb/Mar fees to see only "Arrears". |
| **Pending Cheques** | Parent gave breakdown cheques. They are in the safe but not cleared. | Report has a column **"Uncleared Cheques"**. <br>Net Due = (Total Due - Uncleared Cheques). Treat these as "Collected" for follow-up purposes. |
| **Disputed Fees** | Parent refuses to pay ₹5,000 transport fee claiming "Bus never came". | Mark the invoice as **"On Hold"**. The report will show this amount in a separate "Disputed" column, distinct from "Receivable". |
| **Advance Payments** | Student paid for the full year. Balance is negative (e.g., -₹500). | Report should show `0` in the "Due" column, or display them in a separate "Advance List". Do not mix negatives with positives in the total. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Student Name** | String | Name of the debtor. |
| **Guardian Mobile** | String | Contact number for follow-up. |
| **Total Invoiced** | Currency | Total fees charged so far. |
| **Total Paid** | Currency | Amount received. |
| **Balance Due** | Currency | Invoiced - Paid. |
| **Last Payment Date** | Date | To identify "Dead" accounts (no payment for 6 months). |

## User Actions
1.  **Run Report**: "Show me dues for Academic Year 2023-24".
2.  **Export Contact List**: Download Excel with Mobile Numbers to upload into SMS portal.
3.  **Send Reminder**: Click "Send Mail" directly from the report row.
4.  **Mark Bad Debt**: Tag a student as "Unrecoverable" (requires approval).

## Best Practices
- **Exclude Small Change**: Set a filter "Total Due > ₹100". Don't waste paper printing a report for students who owe ₹5.
- **Check Before TCs**: The Receptionist should strictly check this report before accepting a TC application.
- **Regular Review**: Review the "90+ Days Aging" bucket every month. These are the high-risk defaults.
