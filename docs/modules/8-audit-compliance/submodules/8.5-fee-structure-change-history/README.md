# 8.5 Fee Structure Change History

## Overview
**Fee Structure Change History** is the "Time Machine" of the fee configuration. It tracks every modification made to the fee amounts, due dates, and late fee rules. It allows the system to accurately reproduce an invoice from 2 years ago using the rules that were valid *at that time*.

### Real-World Analogy
Think of this as a **Restaurant Menu Versioning**.
- **Menu 2023**: Pizza was ₹100.
- **Menu 2024**: Pizza is ₹120.
If a customer brings an old bill from 2023, the accountant checks the "2023 Menu" to verify the price. They don't use the current menu.
Similarly, if a student was billed in April, and the fees increased in June, the April bill remains valid at the old rate. This module stores the "Effective Dates" of every price change.

## Purpose
- **Billing Accuracy**: Ensure that students are billed according to the fee structure that was active *history* relative to the invoice date.
- **Audit Defense**: Prove to parents that "When your bill was generated on 1st April, the Late Fee Rule was X".
- **Impact Analysis**: Before changing a fee, see how many past invoices might be affected if the change is "Retroactive".
- **Future Scheduling**: configure a fee hike today that automatically activates on "1st April Next Year".

## Key Features
- **Effective Date Range**: Every fee rule has a `Valid_From` and `Valid_To` date.
- **Version Control**: "Tuition Fee v1 (₹5000)" -> "Tuition Fee v2 (₹6000)".
- **Change Author**: Records *who* made the price change.
- **Diff View**: Visual highlighting of what changed (e.g., "Amount: ~~5000~~ -> **6000**").

## Real-World Scenarios

### Scenario 1: The "Old Rates" Dispute
**Situation**: Parent complains, "You told me Admission Fee is ₹10k, now you are asking for ₹15k."
**Action**:
1.  Admin pulls up **Change History**.
2.  **Finding**: "On Jan 1st (Admission time), Fee was ₹10k. On April 1st, it was revised to ₹15k."
3.  **Outcome**: If the parent has an Admission Letter dated Jan, the school honors the ₹10k rate.

### Scenario 2: The Accidental Zero
**Situation**: Clerk updated "Bus Fee" to ₹0 by mistake for 10 minutes. 5 students were billed ₹0.
**Action**:
1.  Admin spots the error. Corrects it back to ₹2000.
2.  **Audit History**: Shows the 10-minute window of error.
3.  **Remediation**: Admin identifies the 5 invoices generated during that window and manually corrects them.

### Scenario 3: The Scheduled Hike
**Situation**: Board decides in December to raise fees by 10% starting next April.
**Action**:
1.  Admin creates a **"Future Dated Change"**.
2.  Saves "Tuition Fee" = ₹5500 with Effective Date = "01-Apr-NextYear".
3.  **Result**: Current bills continue at old rates. System auto-switches on 1st April.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Retroactive Change** | Changing a fee amount for a past date (e.g., changing Jan fee in March). | **Warning**: System warns "This change will affect 500 existing invoices. Do you want to Recalculate?". Usually, changes should be Prospective, not Retrospective. |
| **Overlap Error** | Trying to create two different fee rules for the same date range. | **Validation**: System blocks the save. "Overlap detected with Rule #105". |
| **Deleted Head** | "Swimming Fee" is removed. What happens to old invoices? | **Soft Delete**: The fee head is marked "Inactive" but remains linked to old invoices. It won't appear for new billing. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Change ID** | String | Unique Version #. |
| **Fee Head** | String | "Tuition Fee Class 10". |
| **Old Amount** | Currency | Previous value. |
| **New Amount** | Currency | Revised value. |
| **Effective Date** | Date | When the change goes live. |
| **Changed By** | User | Admin ID. |
| **Reason** | String | "Annual Board Hike". |

## User Actions
1.  **View Timeline**: See a graphical timeline of price changes over 5 years.
2.  **Compare Versions**: Verify "What was the Late Fee Rule in 2020?".
3.  **Schedule Change**: Set up a price change for the future.
4.  **Revert**: "Undo" the last change if it was a mistake.

## Best Practices
- **Never Overwrite**: Always `INSERT` a new version row. Never `UPDATE` the existing row. This preserves history.
- **Communicate**: When a fee change is saved, the system should prompt: "Do you want to send an SMS notification to parents?"
- **Lock Past Years**: Once a financial year is audited and closed, the fee structure for that year should be Read-Only.
