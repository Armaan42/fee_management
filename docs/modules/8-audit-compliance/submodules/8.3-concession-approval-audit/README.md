# 8.3 Concession Approval Audit

## Overview
**Concession Approval Audit** tracks the lifecycle of every discount granted. Revenue leakage often happens through unauthorized or excessive scholarships. This module ensures that every rupee waived has a digital signature of authorization backing it.

### Real-World Analogy
Think of this as a **Visa Stamping Office**.
- **The Traveler**: The Student asking for a discount.
- **The Officer**: The Principal/Trustee.
- **The Stamp**: The Digital Approval.
Just as an immigration officer checks documents before stamping a passport, the School Admin checks "Income Certificate" or "Sports Certificate" before stamping a "Fee Waiver". The Audit Log records *who* stamped it, *when*, and based on *what proof*.

## Purpose
- **Prevent Favoritism**: Ensure waivers are merit-based, not relation-based.
- **Budget Compliance**: Verify that the approver has the "Spending Limit" to grant that specific amount (e.g., Coordinator can approve ₹500, but Principal can approve ₹50,000).
- **Proof Retention**: Link the approval to the supporting document (PDF/Image) forever.
- **Revocation Safety**: If a scholarship is cancelled, record *why* it was taken back.

## Key Features
- **Multi-Level Workflow**: Clerk requests -> Coordinator verifies -> Principal Approves.
- **Limit Enforcement**: System blocks a user from approving a discount higher than their assigning limit.
- **Comment Logging**: Mandatory "Remarks" field for every approval interaction.
- **Expiry Tracking**: Set an "End Date" for the concession (e.g., valid only for Academic Year 2023-24).

## Real-World Scenarios

### Scenario 1: The "Favor" Investigation
**Situation**: Auditor notices a student received a flat ₹20,000 discount.
**Action**:
1.  Opens **Concession Audit Log**.
2.  Finds: "Approved By: Vice Principal | Remark: 'Neighbor's son'".
3.  **Outcome**: This is flagged as a policy violation. Concessions must be for "Merit" or "Poverty", not "Neighbors".

### Scenario 2: The Sibling Validation
**Situation**: Parent applies for Sibling Concession.
**Action**:
1.  Clerk uploads "Birth Certificate" and clicks "Recommend".
2.  Principal sees the request on their dashboard.
3.  Checks the document.
4.  Clicks **"Approve"**.
5.  **Audit**: Log records "Principal approved Sibling Discount based on Doc ID #555".

### Scenario 3: The Expired Scholarship
**Situation**: A Sports Scholarship was given for one year only.
**Action**:
1.  System auto-revokes the concession on March 31st.
2.  **Log Entry**: "System auto-expired Concession #99 on Date: 31-Mar".
3.  **Outcome**: Next year's fees are generated at full rate.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Self-Approval** | A staff member tries to approve a discount for their own child. | **Conflict of Interest Block**: System checks if `Approver_ID == Student_Parent_ID`. If yes, block action and alert Super Admin. |
| **Retrospective Approval** | Approving a discount for a fee that was already paid 6 months ago. | **Refund Trigger**: The system must ask: "This fee is already paid. Do you want to process a refund or adjust against future fees?" |
| **Document Deletion** | The file attached as proof was deleted later. | **Soft Delete**: The file is hidden from the UI but kept in the secure storage bucket for 7 years as per audit rules. |
| **Limit Override** | Principal needs to approve ₹1 Lakh waiver, but limit is ₹50k. | **Escalation**: The request must be forwarded to the "Trustee" or "Board Member" who has a higher limit. Principal cannot force it. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Request ID** | String | Unique Ticket #. |
| **Student** | String | Beneficiary Name. |
| **Concession Type** | Enum | Merit, Sibling, Staff, Sports. |
| **Amount** | Currency | Value of the waiver. |
| **Stage** | Enum | Requested, Verified, Approved, Rejected. |
| **Action By** | User | The person who changed the stage. |
| **Proof Doc** | Link | URL to the uploaded certificate. |

## User Actions
1.  **Submit Request**: "Apply for Scholarship".
2.  **Verify Queue**: "Show me pending requests".
3.  **Bulk Approve**: Select 50 "Staff Ward" requests and approve in one click (with caution).
4.  **Revoke**: Cancel an active concession due to disciplinary issues.

## Best Practices
- **Separation of Duties**: The person *collecting* fees should never be the person *approving* discounts.
- **Annual Reset**: All recurring concessions (like Staff Ward) should require a fresh "Re-validation" click every year to ensure the staff member is still employed.
- **Sampling Audit**: Randomly check 5% of approvals every month to ensure documents are valid.
