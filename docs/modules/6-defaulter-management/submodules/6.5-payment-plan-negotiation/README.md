# 6.5 Payment Plan Negotiation

## Overview
**Payment Plan Negotiation** offers a structured way to handle families in financial distress. Instead of forcing an impossible lump-sum payment (which leads to default), this module allows the school to approve custom installment plans. It turns a "Bad Debt" into a "Recoverable Loan".

### Real-World Analogy
Think of this as **Converting a Credit Card Bill to EMIs**.
- **The Situation**: You have a bill of ₹50,000. You simply cannot pay it all today.
- ** The Option**: If the bank demands it all, you default. If they say "Pay ₹17,000 for 3 months", you agree.
- **The Contract**: You promise to pay on specific new dates.
- **The Catch**: If you miss even one EMI, the deal is off, and the full original amount (plus interest) becomes due immediately.

## Purpose
- **Recover Revenue**: Getting 100% of the money over 3 months is better than getting 0% forever.
- **Structured Flexibility**: Give staff a clear policy (e.g., "Max 3 installments") so they don't make ad-hoc promises.
- **Track Commitments**: Systematically monitor "Promise to Pay" dates instead of relying on sticky notes.
- **Avoid Dropouts**: Keep the student in school by easing the immediate financial burden.

## Key Features
- **Plan Builder**: "Split ₹20,000 into -> ₹10k (Now) + ₹5k (Next Month) + ₹5k (Dec)".
- **Approval Workflow**: Junior Staff proposes -> Finance Manager approves -> Plan Active.
- **PDC Tracking**: Record Post-Dated Cheque numbers against each future installment.
- **Auto-Breach**: If an installment is missed, system automatically cancels the plan and re-applies the original "Defaulter" status.

## Real-World Scenarios

### Scenario 1: The Medical Emergency
**Situation**: Parent had a surgery and requests 2 months to clear the ₹30,000 Term Fee.
**Action**:
1.  Admin creates a **"Hardship Plan"**.
2.  Installment 1: ₹5,000 (Immediate token payment).
3.  Installment 2: ₹12,500 (Date: 30 days later).
4.  Installment 3: ₹12,500 (Date: 60 days later).
5.  Finance Manager clicks "Approve".
**Outcome**: Parent feels supported; School secures the revenue.

### Scenario 2: The PDC Security
**Situation**: School policy requires cheques for all payment plans.
**Action**:
1.  Parent hands over 3 cheques dated 1st of Oct, Nov, Dec.
2.  Admin enters Cheque Numbers into the Payment Plan screen.
3.  System links these cheques to the future invoices.
**Outcome**: Guaranteed recovery mechanism.

### Scenario 3: The Breach (Broken Promise)
**Situation**: Parent misses the 2nd installment date.
**Action**:
1.  System runs nightly check. Finds "Missed Installment".
2.  **Action**: Plan Status changed to "Breached".
3.  Total Outstanding (₹25,000) becomes "Overdue" immediately.
4.  Defaulter Level jumps to **Level 2** (Principal Notice).
**Outcome**: Zero tolerance for broken repayment promises.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **New Fees Added** | A new "Transport Fee" is generated while the Tuition Plan is active. | Configuring Policy: Does the plan cover *future* fees too? Usually, NO. New fees must be paid separately or added to a *new* consolidated plan. |
| **Partial Installment** | Parent pays ₹5,000 against a ₹7,000 installment. | Plan remains "Active" but "At Risk". 7-day grace period given to clear the remaining ₹2,000. |
| **Early Closure** | Parent gets a bonus and wants to clear the whole plan early. | "Foreclose Plan" button. Accepts full balance `₹X` and marks all future installments as `Paid`. |
| **Staff Authority** | Clerk tries to give a 12-month extension. | System Restriction: "Role 'Clerk' can only approve plans up to 30 days. Request sent to 'Principal'." |
| **Fee Concession** | Parent asks for a discount *and* a payment plan. | Discount must be applied *first* (Module 1.4). The Payment Plan is built on the *Net Payable* amount. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Plan ID** | String | Unique ID for the agreement. |
| **Original Due** | Currency | The total debt before splitting. |
| **Installments** | Array | List of `{Date, Amount, Status}`. |
| **Reason** | String | "Medical", "Job Loss", "Request". |
| **Supported By** | String | "Cheque #123, #124". |
| **Status** | Status | `Proposed`, `Active`, `Completed`, `Breached`. |

## User Actions
1.  **Propose Plan**: Select invoices and choose "Convert to Installments".
2.  **Upload Proof**: Attach email/letter from parent requesting time.
3.  **Approve/Reject**: Manager reviews the proposed schedule.
4.  **Revoke Plan**: Manually cancel the deal if the parent's behavior is rude or non-compliant.

## Best Practices
- **Token Amount**: Always demand *some* payment (e.g., 10-20%) immediately to activate a plan. Never give a 0-down plan.
- **Get it in Writing**: Generate a "Payment Agreement PDF" and make the parent sign it.
- **Limit Duration**: Don't extend plans beyond the current Academic Year.
