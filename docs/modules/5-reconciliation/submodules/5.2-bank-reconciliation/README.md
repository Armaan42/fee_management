# 5.2 Bank Reconciliation

## Overview
**Bank Reconciliation** is the process of matching the school's internal financial records with the actual bank statement. It ensures that every rupee the school accounts for is actually in the bank, and identifies any discrepancies caused by timing differences, bank errors, or missed entries.

### Real-World Analogy
Think of this as **Updating Your Passbook**.
You might have written a cheque to a friend for ₹5,000 on Monday, so you deduct it from your mental balance. But your friend only deposits it on Friday. Until then, your mental balance (Book Balance) and the Bank's Balance differ by ₹5,000.  this module finds these "Timing Differences" so you know exactly why the numbers don't match.

## Purpose
- **Verify Accuracy**: Ensure "Book Balance" = "Bank Balance" + "Unpresented Cheques" - "Uncredited Deposits".
- **Catch Errors**: Find data entry mistakes like entering ₹5600 instead of ₹6500.
- **Track Timing**: Monitor cheques that have been issued but not yet cleared.
- **Record Direct Entries**: Capture bank charges, interest, and direct transfers that happened outside the school system.

## Key Features
- **Statement Import**: Upload CSV/Excel statements from HDFC, SBI, ICICI, etc.
- **Auto-Match**: Algorithms match transactions based on Amount, Date (±3 days), and Reference Number.
- **Unreconciled List**: A clear view of all "Pending" transactions that need manual attention.
- **Reconciliation Statement**: Auto-generates the formal "Bank Reconciliation Statement (BRS)" for auditors.

## Real-World Scenarios

### Scenario 1: The "Unpresented Cheque"
**Situation**: School issued a ₹10,000 refund cheque to a parent on March 28th.
**Action**:
1.  School Book Balance reduces by ₹10,000 immediately.
2.  Bank Statement for March 31st shows the money is still there (Parent hasn't deposited it).
3.  **Reconciliation**: The module marks this transaction as "Unpresented".
4.  BRS Report: "Balance as per Bank + ₹10,000 (Unpresented Cheque) = Book Balance".
**Outcome**: Accounts match perfectly despite the different numbers.

### Scenario 2: The Direct Deposit Surprise
**Situation**: A parent transfers ₹25,000 directly via NEFT but forgets to email the proof.
**Action**:
1.  Bank Statement shows a credit of ₹25,000 with a reference number.
2.  School system has no matching receipt.
3.  **Action**: Accountant clicks "Create Receipt from Statement".
4.  Enters Student Name/ID and allocates the fee.
**Outcome**: The missing receipt is created, and the balance is reconciled.

### Scenario 3: Bank Charges
**Situation**: Bank deducts ₹250 for "SMS Alert Charges".
**Action**:
1.  Statement import shows a debit of ₹250.
2.  No expense voucher exists in the school system.
3.  **Action**: Accountant selects the row and clicks "Post Expense".
4.  Categorizes it as "Bank Charges".
**Outcome**: Expense is recorded, and balances align.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Cheque Return** | Cheque deposited 5 days ago bounces today. | System marks original deposit as "Reversed". Triggers "Cheque Bounce" workflow (Module 3.6) to cancel receipt and add penalty. |
| **Date Mismatch** | Receipt on 31st Mar (Year End), Bank Clear on 2nd Apr (Next Year). | Crucial for Audit. System treats it as "Cheque in Hand" for the closing year balance sheet. |
| **Amount Typo** | Accountant entered ₹5,600, Bank shows ₹6,500. | System highlights the ₹900 difference. Admin must edit the original receipt (with authorization) or post a "Correction Entry" to fix the ledger. |
| **Stale Cheques** | Unpresented cheque remains pending for > 3 months. | Flag as "Stale". Reverse the original entry and credit the amount back to "Accounts Payable" or "General Fund" (as per policy). |
| **Unknown Credit** | Money received but sender is unidentifiable (e.g., "IMPS REF 12345"). | Post to "Suspense Account (Liability)". Wait for parent claim or refund to source after 30 days. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Statement Date** | Date | The 'As Of' date for the reconciliation. |
| **Book Balance** | Currency | Balance in School Software Ledger. |
| **Bank Balance** | Currency | Balance as per uploaded Bank Statement. |
| **Difference** | Currency | The amount yet to be explained. |
| **Unpresented Cheques** | Currency | Cheques issued but not cleared. |
| **Uncredited Deposits** | Currency | Cash/Cheques deposited but not yet in bank. |
| **Status** | Status | `Draft`, `Balanced`, `Locked`. |

## User Actions
1.  **Select Period**: Choose the month to reconcile (e.g., April 2024).
2.  **Upload Statement**: Import the bank's XLS/CSV file.
3.  **Run Auto-Match**: Let the system find the obvious 90% matches.
4.  **Resolve Exceptions**: Manually link or create entries for the remaining 10%.
5.  **Lock Period**: Finalize the BRS so no back-dated entries can modify this month.

## Best Practices
- **Do it Monthly**: Never let reconciliation pile up for year-end. It becomes a nightmare.
- **Separate Accounts**: Maintain separate BRS for each bank account (Fee A/c, Salary A/c).
- **Investigate Old Items**: If a cheque is unpresented for 2 months, call the payee to check why.
