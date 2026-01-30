# 10.9 User Access Control

## 1. Overview
**User Access Control (UAC)** is the gatekeeper of the Fee Management System. It manages the digital identities of all staff members, defines their roles, and strictly controls what they can see and do. This is the foundational submodule for the **Maker-Checker** system, as it defines who the "Makers" and "Checkers" are.

## 2. Key Features
- **User Creation & Onboarding**: Streamlined process to add new staff with generated credentials.
- **Role-Based Access Control (RBAC)**: Assign pre-defined roles (e.g., "Fee Clerk", "Accountant", "Super Admin") or create custom permission sets.
- **Permission Matrix**: Granular control over "View", "Create", "Edit", and "Delete" actions for every module.
- **Account Status Management**: Suspend, Deactivate, or Archive user accounts (e.g., when a staff member leaves).
- **Session Management**: Force logout users or block access during maintenance.

## 3. Standard Roles
- **Super Admin**: Full access to all modules and configurations. (The "Pilot")
- **Principal/Trustee**: View-only access to Reports and Dashboards. (The "Observer")
- **Accountant**: Full access to Fee Collection, Structures, and Reports. (The "Checker")
- **Fee Clerk**: Restricted access to Collect Fees and View Student Profiles. (The "Maker")
- **Class Teacher**: View-only access to their specific class's fee status.

## 4. Interaction with Maker-Checker
Module `11. Verification Workflow` relies entirely on this module:
1. **Makers** are typically users with "Clerk" or "Entry" roles.
2. **Checkers** are typically users with "Manager" or "Admin" roles.
3. The **Verification Rules** defined in Module 11 grant specific "Approval" permissions to these roles.

## 5. Security Protocols
- **Weak Password Rejection**: Enforces complexity requirements.
- **2FA Support**: Optional Two-Factor Authentication for Admin roles.
- **Login Audit**: Every login success and failure is logged in Module 8 (Audit).

## 6. Real-World Scenarios

### Scenario 1: New Accountant Joins
**Situation**: A new senior accountant, Mr. Sharma, joins the school.
**Action**:
1. Admin goes to **User Access Control > Create User**.
2. Enters details and selects Role: **"Senior Accountant"**.
3. **Permissions**: System auto-assigns "Approve" rights for Fee Structure and Concessions.
4. **Outcome**: Mr. Sharma can immediately start verifying the work of junior clerks.

### Scenario 2: Staff Resignation
**Situation**: The fee clerk resigns abruptly.
**Action**:
1. Admin locates user in **User List**.
2. Changes status to **"Deactivated"**.
3. **Outcome**: Login is instantly blocked. Historical records of receipts collected by this clerk remain intact for audit.

### Scenario 3: Temporary Delegation
**Situation**: The Principal wants the Vice Principal to approve concessions while they are on leave.
**Action**:
1. Admin edits Vice Principal's user profile.
2. Adds "Concession Approval" permission temporarily.
3. **Outcome**: Business continuity is maintained without sharing passwords.
