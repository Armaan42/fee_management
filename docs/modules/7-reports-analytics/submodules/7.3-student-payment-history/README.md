# 7.3 Student Payment History

## Overview
**Student Payment History** (also called the Ledger) is the complete financial biography of a student. Unlike reports that aggregate data, this is an individual-centric view. It shows exactly what was demanded (Debit), what was paid (Credit), and what remains pending (Balance) in chronological order.

### Real-World Analogy
Think of this as a **Patient's Medical File**.
When a doctor treats a patient, they need the full history:
- **Diagnosis (Debit)**: "You have an infection (Tuition Fee Due)."
- **Treatment (Credit)**: "Take this medicine (Fee Paid)."
- **Current Status (Balance)**: "You are cured (Zero Balance)."
Without this file, the accountant cannot answer the parent's question: "Why are you asking me for ₹5,000 when I paid last month?"

## Purpose
- **Resolve Disputes**: "Please look at 10th Jan. You paid ₹5,000, but the invoice was ₹10,000. That's why ₹5,000 is still due."
- **Generate Tax Proof**: Provide parents with a consolidated statement for income tax deductions.
- **Trace Adjustments**: Show clearly where a "Fine Waiver" or "Scholarship Credit" reduced the balance.
- **Refund Calculation**: Determine the exact refundable amount when a student leaves.

## Key Features
- **Ledger View**: Standard Accounting format (Date | Particulars | Debit | Credit | Balance).
- **Statement Generation**: One-click PDF download of the "Financial Statement" for any date range.
- **Drill-Down**: Click on a Receipt Number to open the full digital receipt image.
- **Remarks Visibility**: See context notes like "Cheque no. 123 bounced" directly in the timeline.

## Real-World Scenarios

### Scenario 1: The Tax Benefit Request
**Situation**: It's March. Parent needs a statement of tuition fees paid for their tax filing.
**Action**:
1.  Admin searches for Student "Rahul".
2.  Opens **"Payment History"**.
3.  Filters Date: "1st April 2023 to 31st March 2024".
4.  Clicks **"Download Tax Statement"**.
**Outcome**: A PDF is generated showing *only* the Tuition component (excluding Transport/Food), ready for the CA.

### Scenario 2: The "Missing" Payment
**Situation**: Parent claims, "I paid ₹2,000 for the Bus in June."
**Action**:
1.  Admin opens the Ledger.
2.  Scrolls to June.
3.  Finds a receipt for ₹2,000 but the narration says **"Late Fine Payment"**.
4.  **Action**: Explains to parent, "Sir, that ₹2,000 cleared your old fine. The Bus Fee is still pending."
**Outcome**: Dispute resolved with evidence.

### Scenario 3: The Refund Trace
**Situation**: Student is transferring out. Parent asks for the caution deposit back.
**Action**:
1.  Admin checks the Ledger.
2.  Rows show: "Opening Balance: ₹10,000 (Caution Deposit)".
3.  Checks for any "Library Fine" debits. Found ₹500 debit.
4.  **Result**: Refundable Amount = ₹9,500.
5.  **Action**: Posts a "Refund Voucher" to zero out the ledger.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Reversed Transactions** | A cheque bounced. | The ledger shows 3 lines: <br>1. Debit: Fee Due (₹10k) <br>2. Credit: Cheque Recd (₹10k) <br>3. **Debit: Cheque Bounce (₹10k)**. <br>Balance returns to ₹10k. |
| **Opening Balance** | New academic year starts. | The closing balance of the previous year (e.g., ₹5,000 arrears) becomes the **"Opening Balance"** row of the new year's ledger. |
| **Waived Fees** | Principal waived ₹2,000 fine. | Ledger shows a **"Credit Note"** entry: "Fine Waiver - By Principal". This reduces the debit balance without money changing hands. |
| **Advance Carryover** | Parent paid next year's fee in March. | The ledger for the current year shows a valid Credit. The *balance* is negative (e.g., -₹20,000), indicating the school owes service to the student. |
| **Duplicate Receipt** | Admin accidentally entered a receipt twice. | Admin "Cancels" one receipt. The ledger shows a "Cancellation Entry" (Debit) to offset the wrong Credit. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Date** | Date | Transaction date. |
| **Particulars** | String | "Tuition Fee Term 1", "Receipt #101". |
| **Ref No** | Link | Clickable ID (Inv# / Rec#). |
| **Debit** | Currency | Amount Demanded (Invoice/Fine). |
| **Credit** | Currency | Amount Paid / Waived. |
| **Balance** | Currency | Running Total. |

## User Actions
1.  **Search Student**: Find by Name, Admission No, or Mobile.
2.  **Filter View**: "Show me only Payments" (Hide invoices).
3.  **Download**: Export to PDF or Excel.
4.  **Email**: Send the statement directly to the parent's registered email.

## Best Practices
- **Immutable History**: Never *delete* a ledger line. If a mistake happens, add a *correction entry*. Deleting creates gaps in the audit trail.
- **Clear Narrations**: "Fee Paid" is bad narration. **"Tuition Term 1 Paid via UPI"** is good narration.
- **Share Proactively**: Email the ledger to parents every quarter so they are aware of their standing.
