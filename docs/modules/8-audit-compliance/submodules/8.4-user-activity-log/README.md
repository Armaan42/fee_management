# 8.4 User Activity Log

## Overview
**User Activity Log** is the digital footprint of every user in the system. While the "Transaction Log" focuses on *what changed* (money/data), the "Activity Log" focuses on *access and behavior*. It answers: "When did they login?", "What did they view?", and "Did they try to export data?".

### Real-World Analogy
Think of this as an **Office Swipe Card & Browser History**.
- **Swipe Card**: Records when you enter and leave the building (Login/Logout).
- **CCTV**: Records which rooms you entered (Pages Viewed).
- **Scanner**: Records if you photocopied sensitive documents (Data Export).
If a confidential file is leaked, the first thing the security officer checks is: "Who entered the Record Room last night?" This module provides that intelligence.

## Purpose
- **Security Monitoring**: Detect unauthorized access attempts (e.g., failed logins, logins from foreign countries).
- **Productivity Analysis**: Verify if staff members are actually using the system during working hours.
- **Data Leak Prevention**: Track who clicked "Download Excel" on sensitive reports like "Student Mobile Numbers".
- **Compromised Account Detection**: Identify "Ghost Logins" (one ID being used by two people simultaneously).

## Key Features
- **Session Tracking**: Start Time, End Time, Duration, and IP Address.
- **Action Categories**: Navigation, Export, Print, Search.
- **Failed Login Alerts**: Highlights multiple failed password attempts in red.
- **Device Fingerprinting**: Records "Chrome on Windows 10" vs "Safari on iPhone".

## Real-World Scenarios

### Scenario 1: The Data Breach Investigation
**Situation**: A competitor school started calling your parents. The database was leaked.
**Action**:
1.  Admin opens **User Activity Log**.
2.  Filters Action = "Export to Excel" and Period = "Last 7 Days".
3.  **Result**: "User: Clerk_Amit downloaded 'All Student List' on Sunday at 11:30 PM".
4.  **Outcome**: Evidence secured for legal action.

### Scenario 2: The "Overworked" Employee
**Situation**: An accountant claims, "I worked late last night entering receipts."
**Action**:
1.  Manager checks the log.
2.  **Result**: Last activity was at 5:05 PM. No login after that.
3.  **Outcome**: The claim is proven false.

### Scenario 3: The Shared Password
**Situation**: "User: Principal" is logged in. But the IP address changes from Delhi to Mumbai within 10 minutes.
**Action**:
1.  System flags **"Simultaneous Login Alert"**.
2.  **Insight**: The Principal shared their password with a relative or staff member in another city.
3.  **Action**: Force Logout and Password Reset.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Session Timeout** | User closes the browser without clicking "Logout". | **Auto-Close**: The system marks the session as "Expired" after 20 minutes of inactivity. End time is recorded as "Last Active Time". |
| **Impersonation** | Admin uses "Login As Parent" feature to debug. | **Traceability**: The log records "Actor: Admin (acting as Parent_Ravi)". It distinguishes between the *real* user and the *effective* user. |
| **Mobile App Usage** | User logs in via App. | **Source Tagging**: Log shows "Source: Android App" vs "Source: Web Portal". |
| **Log Flooding** | User refreshes the page 100 times. | **Debounce**: Group repeated "Page View" events within 1 minute into a single log entry ("Viewed Dashboard (x10)") to save space. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Session ID** | String | Unique hash for the login session. |
| **User** | String | Name/Role. |
| **Event Time** | DateTime | When it happened. |
| **Event Type** | Enum | Login, View, Edit, Export, Print. |
| **Module** | String | "Fee Collection", "Reports". |
| **IP Address** | String | 203.0.113.1. |
| **Browser/OS** | String | User Agent string. |

## User Actions
1.  **Monitor Live**: "Who is online right now?".
2.  **Investigate User**: "Show me everything 'Accountant_Raj' did today".
3.  **Geolocate**: Show a map view of login locations.
4.  **Force Logout**: Kick a suspicious session offline immediately.

## Best Practices
- **Export Restricted**: By default, only the Super Admin should have the "Export" button enabled. Log every export usage.
- **Password Hygiene**: If the log shows "Failed Login (Wrong Password)" > 3 times, auto-lock the account for 15 minutes.
- **Privacy**: Do not log the *contents* of what was viewed (e.g., don't log the student's marks), just the *fact* that it was viewed.
