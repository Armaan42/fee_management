# 11.1 Maker-Checker Configuration

## 1. Overview
The **Maker-Checker Configuration** submodule allows administrators to define the rules of engagement for verification. It answers the questions: *Who creates?*, *Who verifies?*, and *What requires verification?*.

This configuration is highly granular, allowing different policies for different modules (e.g., Fee Structure changes might require 2 approvals, while a Student Address update might require only 1).

---

## 2. Key Features
- **Role Definition**: Assign "Maker" and "Checker" capabilities to specific User Roles.
- **Scope Definition**: Select which modules or specific actions (Create, Edit, Delete) trigger the flow.
- **Approval Levels**: Configure Single-Level or Multi-Level (Sequential) approvals.
- **Self-Approval Prevention**: Enforces the rule that a user cannot approve their own requests, even if they have Super Admin privileges.

## 3. Scenarios

### Scenario 1: Configuring Multi-Level Approval for Financial Changes
- **Requirement**: "Fee Structure" changes are high-risk. They need checks by the Finance Manager AND the Principal.
- **Setup**:
    1. Go to **Settings > Verification Rules**.
    2. Select Module: **Fee Structure**.
    3. Set Levels: **2**.
    4. Level 1 Approver: **Role: Finance Manager**.
    5. Level 2 Approver: **Role: Principal**.
    6. Enable **Enforce Sequential Approval** (Level 2 cannot see it until Level 1 approves).

### Scenario 2: Excluding Low-Risk Fields
- **Requirement**: Changing a student's "Emergency Contact" is low risk and happens frequently.
- **Setup**:
    1. Select Module: **Student Profile**.
    2. Field-Level Config:
        - Name/DOB: **Requires Approval**.
        - Emergency Contact: **Auto-Approve**.
    3. Result: Clerks can update phone numbers instantly, but cannot change names without oversight.

### Scenario 3: Temporary Delegation
- **Requirement**: The Principal is on vacation for 2 weeks.
- **Setup**:
    1. Principal logs in.
    2. Navigates to **My Delegations**.
    3. Selects Delegate: **Vice Principal**.
    4. Sets Duration: **Start Date** to **End Date**.
    5. All approval requests routed to Principal now appear in Vice Principal's queue.

## 4. Edge Cases
- **Approver Resignation**: IF an assigned Approver role is vacant, requests escalate to the System Administrator.
- **Deadlock**: IF a request sits in pending for > 7 days, notify the next level up or the Super Admin.
- **Maker is also Admin**: Even if the Maker is an Admin, if the rule says "Two distinctive eyes", they cannot click the final "Approve" button on their own transaction.
