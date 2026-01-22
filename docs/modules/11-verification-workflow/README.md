# 11. Verification Workflow (Maker-Checker Module)

## 1. Overview
The **Verification Workflow** (also known as the **Maker-Checker** or **4-Eyes Principle**) is a critical system-wide security and quality control layer. It ensures that **no sensitive action or record creation is finalized by a single individual**. Every "creation" or "modification" initiated by a **Maker** must be reviewed and approved by a distinct **Checker** before it becomes active in the system.

This module does not just handle fees; it wraps **every** transactional and configuration change across the entire ERP, including Student Admissions, Fee Structures, Fine Rules, Concessions, and User Management.

---

## 2. Core Concepts

### 2.1 The Maker (Initiator)
- **Role**: Staff, Accountants, or Clerks who perform data entry.
- **Action**: Enters data, creates records, or modifies settings.
- **Result**: The record is saved in a **"Pending Approval"** or **"Draft"** state. It is **NOT** active.

### 2.2 The Checker (Approver)
- **Role**: Supervisors, Principals, or Administrators.
- **Action**: Reviews the "Pending" records.
- **Decision**:
    - **Approve**: The record becomes "Active" and affects the system (e.g., fee demands are raised, receipts are valid).
    - **Reject**: The record is returned to the Maker with comments for correction.

---

## 3. Real-World Scenarios

### Scenario 1: Fee Structure Approval
- **Situation**: The Accountant (Maker) sets the new tuition fee for Grade 10 at $5,000.
- **Safe-guard**: If this error goes live, hundreds of wrong invoices will be generated.
- **Flow**:
    1. Accountant saves Fee Structure. Status: **Pending Authorization**.
    2. Principal (Checker) receives a notification.
    3. Principal views the audit trail & proposed values.
    4. Principal clicks **Approve**.
    5. Fee Structure Status: **Active**.

### Scenario 2: High-Value Concession
- **Situation**: A clerk tries to grant a 50% waiver to a student.
- **Safe-guard**: Preventing unauthorized revenue loss.
- **Flow**:
    1. Clerk applies concession. System blocks immediate application.
    2. Request sent to "Pending Approvals Queue".
    3. Administrator reviews the documents attached.
    4. Administrator **Rejects** request asking for "Income Certificate".
    5. Clerk provides document and re-submits.

### Scenario 3: Employee Onboarding
- **Situation**: HR Assistant creates a new staff profile.
- **Safe-guard**: Preventing ghost employees.
- **Flow**: New user accounts remain **Locked** until a Manager verifies the details.

---

## 4. Systems & Components
- **Pending Approvals Queue**: A centralized dashboard for Checkers to see all items awaiting their attention.
- **Delegation**: Allow Checkers to delegate approval authority temporarily (e.g., during leave).
- **Multi-Level Approval**: Configurable rules (e.g., transactions > $10,000 need 2 Approvers).

## 5. Submodules
- **11.1 Maker-Checker Configuration**: Setting up the rules, levels, and user roles.
- **11.2 Pending Approvals Queue**: The interface for managing incoming requests.
- **11.3 Verification History**: Historical logs of all approvals and rejections for audit.
- **11.4 Rule-Based Auto-Approval**: configuring "safe" thresholds where manual approval is skipped.
