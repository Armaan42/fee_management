# 3.3 Advance Payment

## Overview
**Advance Payment** allows parents to deposit fees ahead of time, which the system stores in an "Advance Wallet" for the student. When future fees become due, the system automatically uses this wallet balance to clear the dues, similar to how a prepaid mobile balance works.

**In simple terms**: It's like "Store Credit". You give the school ₹50,000 now, and they keep deducting from it every month until it runs out.

**Analogy**: 
-   **Prepaid Mobile**: You top-up ₹500. The telecom company deducts daily/monthly charges from this balance automatically. You don't need to pay every day.

## Purpose
To offer convenience to parents who prefer to pay in bulk or want to avoid monthly deadlines, and to handle excess payments gracefully.

## Description
This submodule manages the lifecycle of excess money: Accepting the advance, Tracking the balance, and Allocating it against future demands. It ensures that money received today is legally accounted for as "Liability" until it is actually consumed by a fee bill.

## Key Features
-   **Wallet System**: Maintains a running balance of credit for every student.
-   **Auto-Adjustment**: Automatically clears new dues using the advance balance (Scheduler based).
-   **Specific vs General**: Advance can be General (use for anything) or Restricted (use only for Tuition).
-   **Refundable**: Unused advance can be refunded if the student leaves.
-   **Receipts**: Generates an "Advance Receipt" document when money is deposited.

## Real-World Scenarios

### Scenario 1: The Annual Lumpsum
**Background**: Parent travels frequently and wants to pay the entire year's fee (₹1,20,000) in April.
**Action**: 
1.  Admin accepts ₹1,20,000 as "Advance Payment".
2.  In May, June, July... system automatically debits the monthly fee from this balance.
**Result**: Parent doesn't get payment reminders until the balance runs low.

### Scenario 2: Rounding Off Change
**Background**: Fee is ₹4,990. Parent hands over a ₹5,000 note. Cashier has no change (₹10).
**Action**: Cashier records ₹5,000 receipt.
**System Behavior**: ₹4,990 clears dues. ₹10 moves to "Advance Wallet".
**Result**: Next month's bill of ₹4,990 will require only ₹4,980 from parent.

### Scenario 3: Refund Adjustment
**Background**: School cancelled the Annual Picnic (Refund ₹500/student). Cash refund is messy.
**Action**: School "moves" ₹500 to everyone's Advance Wallet.
**Result**: Parents see a ₹500 credit in their app.

### Scenario 4: Sibling Transfer
**Background**: Elder child graduates Class 12. Has ₹2,000 unused advance.
**Action**: Parent asks to transfer this to younger sibling (Class 8).
**Result**: Admin performs "Wallet Transfer". Elder = ₹0, Younger = +₹2,000.

### Scenario 5: Security Deposit
**Background**: School takes ₹10,000 "Caution Money" at admission (refundable at exit).
**Action**: This is recorded as a "Restricted Advance" (Not Auto-Adjustable against tuition).
**Result**: Money stays safe until graduation.

## Edge Cases & How to Handle Them

### Edge Case 1: Auto-Adjustment Failure
**What Happens**: June Fee generated on 1st. Student has Advance. System glitch fails to run the "Debit Advance" job.
**System Behavior**: Parent gets "Fee Overdue" SMS despite having money.
**How to Handle**: Scheduler must have Retry logic + Alert Admin if auto-debit fails.

### Edge Case 2: Advance > Total Dues
**What Happens**: Fee is ₹5,000. Advance is ₹50,000.
**System Behavior**: System takes ₹5,000. Remaining ₹45,000 stays in wallet.
**How to Handle**: Correct behavior. Ensure receipt clearly shows "Paid from Advance".

### Edge Case 3: Withdrawal of Advance
**What Happens**: Parent needs cash back for emergency.
**System Behavior**: Advance is a Liability.
**How to Handle**: "Refund Receipt" process. Reduces wallet balance, Cashier hands over cash.

### Edge Case 4: Interest Claims
**What Happens**: Parent claims "I gave you ₹1 Lakh a year ago. Give me interest."
**System Behavior**: Schools do not act as banks.
**How to Handle**: Policy statement in receipt: "Advance payments carry zero interest".

### Edge Case 5: Lapsing / Forgotten Money
**What Happens**: Student left 5 years ago. Still has ₹50 balance.
**System Behavior**: Clutters the database.
**How to Handle**: Yearly "Unclaimed Deposits" report. Policy to write-off small amounts after 3 years.

### Edge Case 6: Simultaneous Bill & Advance
**What Happens**: Parent pays Advance online at 10:00 AM. Bill generates at 10:01 AM.
**System Behavior**: Race condition. Bill might not see the advance.
**How to Handle**: Bill generation logic must always check current wallet balance *at the moment of finalization*.

### Edge Case 7: Tax on Advance (GST)
**What Happens**: GST rules often say "Tax payable on receipt of advance".
**System Behavior**: If fees are taxable, system must calculate tax when Advance is *received*, not when *settled*.
**How to Handle**: Advanced accounting config.

### Edge Case 8: Head-Specific Advance
**What Happens**: Parent gave ₹5,000 specifically for "Winter Uniform".
**System Behavior**: System uses it to pay "Tuition Fee". Parent angry.
**How to Handle**: "Restricted Advance" feature. Advance is tagged to a specific Fee Group.

### Edge Case 9: Closing Financial Year
**What Happens**: March 31st. Student has ₹10,000 Advance.
**System Behavior**: Needs to be carried forward to next Fiscal Year.
**How to Handle**: "Balance B/F" entry in new year's ledger.

### Edge Case 10: Negative Advance
**What Happens**: Glitch enables Wallet Balance to go to -₹500.
**System Behavior**: Accounting impossibility (Negative Asset?).
**How to Handle**: Validation: Wallet Balance cannot be < 0.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Student | Lookup | Yes | Account holder |
| Amount | Currency | Yes | Deposit amount |
| Is Restricted? | Boolean | Yes | Can be used for any fee? |
| Tagged Fee Head | Lookup | No | If restricted |
| Remarks | Text | No | "Transfer from sibling" |
| Current Balance | Currency | Yes | Calculated field |

## User Actions
1.  **Search Student**: View current balance.
2.  **Add Advance**: Accept payment.
3.  **Refund/Transfer**: manage unused funds.
4.  **Statement**: Print "Advance Ledger".

## Business Rules
-   Advance balance is *not* revenue. It is a liability until adjusted against a bill.
-   Advance cannot be used to pay off "Optional Fees" unless explicitly allowed.

## Permissions Required
-   **Accept Advance**: Fee Cashier.
-   **Refund Advance**: Fee Manager / Principal.

## Related Submodules
-   **3.2 Partial Payment**: Often interacts with Advance (e.g., pay partial, keep rest as advance).
-   **3.8 Refund Processing**: To return the advance.

## API Endpoints
```
POST /api/advance-wallet/credit - Add money
POST /api/advance-wallet/debit - Manual use
GET /api/students/:id/wallet - Check balance
```

## Database Schema
```sql
Table: advance_wallet_ledger
- id (PK)
- student_id (FK)
- transaction_type (CREDIT/DEBIT)
- amount (DECIMAL)
- related_receipt_id (FK)
- balance_after (DECIMAL)
```

## UI/UX Considerations
-   **Green Badge**: Show "Wallet: ₹5,000" prominently on the student profile.
-   **Auto-Suggest**: During fee collection, if wallet has balance, show pop-up "Use ₹500 from Wallet?".

## Best Practices
1.  **Encourage Advances**: It flows cash to the school early.
2.  **Automate**: Don't rely on cashiers to manually remember who has an advance. The system must auto-deduct.
3.  **Transparency**: Monthly statement to parents showing "Opening Bal -> Deductions -> Closing Bal".
