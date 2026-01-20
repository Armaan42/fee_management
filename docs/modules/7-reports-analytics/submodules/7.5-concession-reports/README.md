# 7.5 Concession Reports

## Overview
**Concession Reports** track the "revenue forgone" by the school. Every scholarship, sibling discount, or staff waiver is effectively an expense—it is money the school *chose* not to collect. This module audits these decisions to prevent leakage and ensure charity budgets are respected.

### Real-World Analogy
Think of this as a **Discount Coupon Audit**.
If a shirt costs ₹100 and you sell it for ₹80, the store manager records a ₹20 "Cost of Sale".
- **The Price Tag**: The Full Fee.
- **The Coupon**: The Concession (Sibling / Merit / Staff).
- **The Cash Register**: Records "Received ₹80" + "Discount ₹20".
Without this report, the owner might think, "Why is cash low when sales are high?", not realizing that 50% of customers used a coupon.

## Purpose
- **Budget Control**: Ensure the total value of scholarships doesn't exceed the board-approved limit (e.g., ₹10 Lakhs/year).
- **Audit Verification**: Prove to auditors that every discount given has a valid approval (Principal's sign) and reason.
- **HR Analysis**: Calculate the "Cost to Company" (CTC) of free education provided to staff children.
- **Equity Check**: Analyze if concessions are distributed fairly across different classes and communities.

## Key Features
- **Category Summary**: "Total Merit Scholarship" vs "Total Sibling Discount".
- **Student-wise Detail**: List of all 50 students who got a waiver this year.
- **Approval Log**: Shows *who* authorized the discount (e.g., "Approved by: Principal").
- **Impact Analysis**: "Percentage of Revenue waived" (e.g., 5% of potential revenue was given as aid).

## Real-World Scenarios

### Scenario 1: The Charity Budget Check
**Situation**: The School Trust allows ₹10 Lakhs of charity per year.
**Action**:
1.  Trustee runs **"Concession Summary Report"**.
2.  **Result**: "Total Concessions to date: ₹9.5 Lakhs".
3.  **Outcome**: Principal is alerted to stop approving new scholarships for the rest of the year.

### Scenario 2: The Sibling Verification Audit
**Situation**: New academic year begins. 200 parents claimed "Sibling Discount".
**Action**:
1.  Admin exports the **"Sibling Concession List"**.
2.  Randomly checks 10 names to see if the "Sibling Name" field matches a real student in the database.
3.  **Discovery**: 2 students claimed discount but the elder sibling graduated 2 years ago.
4.  **Action**: Concession revoked.

### Scenario 3: The Tax Perquisite (HR)
**Situation**: HR needs to calculate income tax for staff. Free education is a taxable perk.
**Action**:
1.  HR runs **"Staff Ward Concession Report"**.
2.  Filters for "Physics Teacher's Child".
3.  **Result**: "Value of Benefit: ₹40,000".
4.  **Action**: HR adds ₹40,000 to the teacher's taxable income calculation.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Mid-Year Revocation** | Student misbehaved; scholarship cancelled in October. | Report splits usage: <br>Apr-Sep: **Concession Active** (₹5k waived). <br>Oct-Mar: **Full Fee Applied**. Total Waiver = ₹5k (not ₹10k). |
| **Double Dipping** | Student applied for *both* "Merit" and "Sibling" discount. | Report highlights these as **"Multi-Concession Alerts"**. Policy usually allows only one (the higher of the two). |
| **Retrospective Waiver** | Fee was invoiced in April. Scholarship approved in July. | The report treats the April invoice adjustment as a "Correction". The "Date of Concession" is July, but it applies to the April fee head. |
| **Fee Hike Impact** | Tuition fee increased by 10%. Does the concession value increase? | Depends on Type: <br>- **Percentage Based**: Yes (50% of ₹110 is more than 50% of ₹100). <br>- **Flat Amount**: No (Fixed ₹5000 remains ₹5000). |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Concession Name** | String | "Merit Scholarship 2024". |
| **Type** | Enum | `Percentage (%)` or `Flat Amount (₹)`. |
| **Beneficiary** | int | Count of students. |
| **Total Invoiced** | Currency | Gross Fee. |
| **Total Waived** | Currency | The discount value. |
| **Net Collected** | Currency | Actual revenue. |

## User Actions
1.  **Analyze Trends**: "Are we giving more scholarships this year compared to last year?"
2.  **Audit Approvals**: "Show me all waivers approved by the *Vice Principal*".
3.  **Export for Board**: Prepare the "social responsibility" slide for the AGM.
4.  **Identify Expiring**: "Show me concessions ending this month".

## Best Practices
- **Reason Codes**: Mandatory "Reason" field for every waiver (e.g., "Father Deceased", "State Topper"). "Other" is not a valid reason.
- **Annual Renewal**: Never make a concession "Permanent". Set it to expire in March so it forces a review next year.
- **Percentage Over Flat**: Prefer %-based concessions (e.g., 50% Off) so they auto-adjust when fees increase.
