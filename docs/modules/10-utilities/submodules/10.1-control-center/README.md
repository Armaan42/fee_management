# 10.1 Control Center

## Overview
**Control Center** is the central nervous system of the Fee Management Software. It is the place where global parameters, school identity, and system-wide behaviors are defined. Changes made here ripple across every module, receipt, and report in existence.

### Real-World Analogy
Think of this as an **Airplane Cockpit**.
- **The Passengers**: Teachers and Accountants doing their daily jobs.
- **The Pilot**: The Super Administrator.
- **The Controls**: The Control Center.
The pilot decides the destination (Academic Year), creates the rules (Receipt Prefixes), and can turn on the "Fasten Seatbelt" sign (Maintenance Mode) to pause activity. A wrong button press here affects the entire flight.

## Purpose
- **Identity Management**: Define "Who we are" (School Name, Logo, Address, Affiliation No) which appears on every printed document.
- **Localization**: Configure Currency (₹/$), Date Format (DD-MM-YYYY), and Time Zone.
- **Sequence Control**: Manage the auto-incrementing counters for Receipt Numbers, Admission Numbers, and Inquiry IDs.
- **Feature Toggles**: Enable/Disable optional features like "Online Payment" or "SMS Integration" globally.

## Key Features
- **General Settings**: School Name, Address, Contact Info.
- **Financial Configuration**: Current Financial Year, Tax ID (GST/PAN).
- **Numbering Series**: Define prefixes (e.g., `REC/23-24/001`).
- **Notification Gateways**: API keys for SMS (Twilio/DLT) and Email (SMTP/SendGrid).
- **System Maintenance**: "Lockdown" switch to prevent user login during updates.

## Real-World Scenarios

### Scenario 1: The New Session Setup
**Situation**: It's March 31st. The school moves from 2023-24 to 2024-25.
**Action**:
1.  Admin changes "Current Academic Year" to **2024-25**.
2.  Updates Receipt Series Prefix to **REC/24-25/**.
3.  **Outcome**: The very next receipt generated automatically carries the new year tag. No manual intervention needed by the accountant.

### Scenario 2: The Campus Shift
**Situation**: The school moved to a new building. All receipts still show the old address.
**Action**:
1.  Admin updates **School Address** in Control Center.
2.  **Outcome**: Every reprinted receipt, new invoice, and report header instantly reflects the new location.

### Scenario 3: The "Stop Work" Order
**Situation**: A critical bug is found, or a server migration is planned.
**Action**:
1.  Admin toggles **"Maintenance Mode"** to ON.
2.  **Outcome**: All staff attempting to login see: "System under maintenance. Please try after 2 hours." Data corruption is prevented.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Currency Switch** | Changing "INR" to "USD" when INR transactions already exist. | **Hard Block**: System prevents changing base currency if transactions exist. Requires a database wipe or a separate "Multi-Currency" module activation. |
| **Prefix Reset** | Resetting Receipt Number to 1 mid-year. | **Collision Check**: Before saving, the system checks if "REC-001" already exists. If yes, it throws an error: "Duplicate Sequence Detected". |
| **Gateway Failure** | SMS API settings are wrong. | **Sandboxed Test**: The "Save" button for API keys triggers a "Test Message". Settings are saved *only if* the test succeeds. |
| **Logo Distortion** | Uploading a 4000x4000px image for the logo. | **Auto-Resize**: System automatically scales and compresses the image to fit the standard 150x150px receipt header area. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **School Name** | String | Official registered name. |
| **Logo URL** | String | Path to the branding image. |
| **Current FY** | Year | 2023-2024. |
| **Receipt Prefix** | String | "FEE/". |
| **Starting No** | Int | 1001. |
| **Timezone** | Enum | Asia/Kolkata (IST). |
| **Currency** | Enum | INR (₹). |

## User Actions
1.  **Update Profile**: Change phone numbers printed on receipts.
2.  **Configure SMTP**: Set up the email server for notifications.
3.  **View System Health**: Check database size and last backup time.
4.  **Manage Plugins**: Enable/Disable "Transport Module" or "Library Module".

## Best Practices
- **Restricted Access**: Only the Principal or IT Head should have access to this module.
- **Audit Logs**: Every change in Control Center (e.g., changing Receipt #) must be logged with high priority.
- **Backup First**: Before changing critical settings like "Financial Year", always trigger a manual system backup.
