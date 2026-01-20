# 7.4 Head-wise Collection

## Overview
**Head-wise Collection** reports break down the total revenue into its specific components. It answers the question: "Of the ₹1 Crore collected, how much belongs to Transportation, how much to Tuition, and how much is Refundable Deposit?"

### Real-World Analogy
Think of this as your **Salary Slip Breakdown**.
You don't just say "I earned ₹50,000". You analyze it:
- **Basic Pay**: ₹20,000
- **HRA**: ₹15,000
- **Travel Allowance**: ₹5,000
- **PF Deduction**: ₹2,000
Similarly, a parent pays a lump sum of ₹30,000, but the accountant needs to know that exactly ₹5,500 of that is for the "Bus Fund" to pay the contractor.

## Purpose
- **Budget Allocation**: Ensure that money collected for specific purposes (e.g., Library, Lab) is actually spent on them.
- **Liability Tracking**: Separate "Income" (Tuition) from "Liabilities" (Caution Deposit) in the balance sheet.
- **Vendor Payment**: Use "Transport Fee" collections to clear the bus vendor's monthly invoice.
- **Tax Compliance**: Some fee heads might be taxable (e.g., Sale of Books - GST applicable), while Tuition Fee is exempt.

## Key Features
- **Allocation Priority**: Define logic like "Clear Fine first, then Transport, then Tuition".
- **Refundable Flags**: Mark specific heads (like Security Deposit) as "Liability" so they don't inflate the "Revenue" report.
- **Partial Payment Logic**: Intelligent splitting of a ₹10,000 payment across 3 different heads.
- **Consolidated View**: View "Tuition Fee" collection across all classes (Nursery to Class 12).

## Real-World Scenarios

### Scenario 1: The Transport Fund Crisis
**Situation**: The Bus Contractor demands an urgent payment of ₹5 Lakhs.
**Action**:
1.  Trustee asks, "Do we have enough in the Transport Fund?"
2.  Admin runs **"Head-wise Collection Report"**.
3.  Filters Head = "Transport Fee".
4.  **Result**: "Collection this month: ₹4.5 Lakhs".
5.  **Outcome**: Decision made to pay ₹4.5 Lakhs now and the rest later.

### Scenario 2: The Annual Day Budget
**Situation**: Cultural Committee needs budget for the Annual Function.
**Action**:
1.  Admin checks "Annual Day Fee" collection status.
2.  **Result**: 90% collected. Total ₹8 Lakhs.
3.  **Outcome**: Budget of ₹7 Lakhs approved for stage and sound.

### Scenario 3: The Taxable Item (Books/Uniform)
**Situation**: School sells Uniforms (Taxable under GST) along with Fees (Exempt).
**Action**:
1.  Accountant runs Head-wise Report for "Uniform Sale".
2.  **Result**: ₹2,00,000 collected.
3.  **Action**: Accountant calculates 5% GST on this ₹2L and deposits it to the government.
**Outcome**: Compliance transparency.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Partial Pay Split** | Student owes ₹15,000 (₹10k Tuition + ₹5k Bus). Pays only ₹5,000. | **Priority Configuration**: If system is set to `Transport > Tuition`, the full ₹5,000 goes to Transport. Tuition remains "Due". |
| **Combined Heads** | "Term Fee" covers Sports, Exam, and Stationary. | **Sub-Head Mapping**: The report should be able to show the parent "Term Fee" but internally split it 40:40:20 for accounting. |
| **Waiver Impact** | Student got a ₹2,000 scholarship. Which head was reduced? | Scholarship usually reduces **Tuition Fee** first. The report shows: "Tuition Invoiced: ₹10k, Waiver: ₹2k, Collected: ₹8k". |
| **Suspense/Advance** | Parent paid ₹50,000 lump sum, but invoice is not yet generated. | Money sits in **"Advance / Suspense Head"**. It moves to specific heads (Tuition, Bus) only when the Invoice is created and "Allocated". |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Fee Head** | String | Name of the category. |
| **Account Code** | String | Tally/ERP Ledger Code (e.g., "Ledger-101"). |
| **Invoiced Amount** | Currency | Total demand raised. |
| **Waiver Amount** | Currency | Discounts given. |
| **Collected Amount** | Currency | Actual money received. |
| **Outstanding** | Currency | Yet to collect. |

## User Actions
1.  **View Summary**: Pie chart showing percentage contribution of each head.
2.  **Update Priority**: Change the order of allocation (e.g., make "Fine" the first priority to discourage delays).
3.  **Map to Ledger**: Link "Transport Fee" to the "Bank Account B" (if separate accounts are used).
4.  **Export for Tally**: Download XML to import accounting vouchers.

## Best Practices
- **Don't Mix Buckets**: Keep "Tuition" (Revenue) and "Caution Deposit" (Liability) strictly separate.
- **Review Unallocated**: Regularly check the "Suspense Head" to ensure money isn't sitting there unallocated for months.
- **Consistent Naming**: Don't use "Bus Fee" in Class 1 and "Transport Fee" in Class 5. Use global definitions.
