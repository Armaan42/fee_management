# 5.5 Discrepancy Investigation

## Overview
**Discrepancy Investigation** is the toolset for resolving financial mysteries. When the "Book Balance" and "Bank Balance" don't match even after auto-reconciliation, this module helps you dig deeper. It provides audit logs, activity trackers, and suspense accounts to identify the root cause of every missing or extra rupee.

### Real-World Analogy
Think of this as a **Detective Board**.
A discrepancy is a crime scene where money is either missing or unaccounted for.
- **The Clue**: Bank statement has ₹5,000 credit, but no student receipt.
- **The Investigation**: Search for the reference number, check emails, ask staff.
- **The Solution**: "Ah, it was Rahul's father paying directly via NEFT."
- **The Closing**: Link the money to the student and close the case.

## Purpose
- **Solve Suspense**: Identify the owner of "Unclaimed Deposits".
- **Detect Errors**: Find duplicate entries, typos, or wrong date entries.
- **Prevent Fraud**: robust Audit Trails reveal if a receipt amount was altered after collection.
- **Clean Books**: Ensure 100% of transactions are explained before finalizing the year-end accounts.

## Key Features
- **Suspense Account Manager**: A holding area for money that we have but don't know who it belongs to.
- **Global Search**: Search for a Transaction ID/UTR across all years and all students.
- **Audit Log Viewer**: See who edited a receipt, when, and what was changed.
- **Auto-Suggest**: "This ₹5,000 credit looks like it could be for Student X, who has a due of ₹5,000."

## Real-World Scenarios

### Scenario 1: The Mystery Credit (Suspense Account)
**Situation**: Bank Statement shows `IMPS-998877-KUMAR` for ₹12,500. No receipt in system.
**Action**:
1.  Admin marks it as **"Transfer to Suspense"**.
2.  It sits in the "Unidentified Income" ledger.
3.  Two days later, a parent calls: "I paid via IMPS, did you get it?"
4.  Admin searches the Suspense list, matches the amount, and assigns it to the student.
**Outcome**: Money is safely held until identified, ensuring the bank balance matches.

### Scenario 2: The Double Entry
**Situation**: Two receipts exist for the same student for the same month fees.
**Action**:
1.  Discrepancy Report flags: "Potential Duplicate - Student ID 123".
2.  Investigation reveals: Fees Counter Staff created a receipt, and Parent also paid online.
3.  **Resolution**: Admin cancels the manual receipt and refunds the excess or adjusts it against next month.
**Outcome**: Prevents overstating income.

### Scenario 3: The "Edited" Receipt (Audit Trail)
**Situation**: Daily Cash Collection is short by ₹4,000.
**Action**:
1.  Admin opens **Discrepancy Tools -> Audit Logs**.
2.  Filters by "Receipt Edits" for today.
3.  Finds: "Receipt #101 edited by Staff_John. Amount changed from ₹5,000 to ₹1,000."
4.  **Resolution**: Caught a potential fraud or mistake. The original amount is restored.
**Outcome**: Financial integrity maintained.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Write-Off** | Investigation yields no results for a small difference (e.g., ₹10) after 3 months. | Authorized Finance Manager can post a "Write-Off Journal" to clear it from the books. |
| **Cross-Branch Error** | Parent paid to High School Account instead of Primary School. | Inter-branch Transfer: Debit High School Bank, Credit Primary School Student. Requires "Multi-Branch" setup. |
| **Reversal Glitch** | Bank reversed a transaction, but software missed the webhook. | Admin manually posts a "Reversal Entry" linked to the original settlement ID to nullify the income. |
| **Currency FX** | International wire transfer of $100 becomes ₹8,200 instead of ₹8,300. | Post the difference to "Forex Gain/Loss" expense account. |
| **Ghost Receipt** | Receipt exists in system, but no money ever came to any bank. | Verify if it was a "Cash" receipt marked wrongly. If not, cancel the receipt as "Entry Error". |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Discrepancy ID** | String | Unique Case ID. |
| **Type** | Enum | `Excess Credit`, `Shortage`, `Duplicate`, `Data Mismatch`. |
| **Amount** | Currency | The value in question. |
| **Detected Date** | Date | When the mismatch was found. |
| **Assigned To** | User | Staff responsible for investigating. |
| **Status** | Status | `Open`, `Investigating`, `Resolved`, `Written-off`. |

## User Actions
1.  **Flag for Investigation**: Move a transaction from "reconcilation" to "Discrepancy".
2.  **Add Notes**: "Called bank, they said wait 24 hours."
3.  **Assign Student**: Link a suspense entry to a specific student ledger.
4.  **Write Off**: Finalize a discrepancy without finding the source (Strict permissions).

## Best Practices
- **Clear Suspense Monthly**: Don't let the "Unidentified" pile grow. It becomes harder to solve as time passes.
- **Strict Permissions**: Only the Finance Manager should have rights to "Write Off" or "Delete" entries.
- **Mandatory Remarks**: Force users to explain *why* they are editing a closed transaction.
