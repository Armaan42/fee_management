# 8.1 Transaction Audit Log

## Overview
**Transaction Audit Log** is the "Black Box" of the fee system. It records every single action taken by any user—every receipt created, every fee modified, and every student deleted. It ensures accountability and provides a forensic trail in case of discrepancies.

### Real-World Analogy
Think of this as a **Bank's CCTV Control Room**.
- **The Teller**: The Accountant using the software.
- **The Cash**: The Fee Data.
- **The Camera**: The Audit Log.
If money goes missing or a ledger entry looks suspicious, the Manager rewinds the CCTV tape to see *exactly* who was at the counter, what they typed, and at what time. The Audit Log provides this same "rewind" capability for digital transactions.

## Purpose
- **Forensic Investigation**: Answer the question "Who deleted this receipt?" with 100% certainty.
- **Deterrence**: When staff know "everything is logged", they are less likely to attempt fraud.
- **Compliance**: Meet legal and board requirements for financial transparency.
- **Error Tracing**: Identify if a system bug or a human error caused a calculation mistake.

## Key Features
- **Immutable Records**: Once a log is written, it cannot be deleted or edited—even by the Super Admin.
- **Before/After Values**: "Old Value: ₹5000" -> "New Value: ₹2000". Captures the *change*, not just the final state.
- **IP Address Tracking**: Logs the physical location (network) of the user.
- **Searchable Interface**: "Show me all actions by 'User: John' on 'Date: 10th Jan'".

## Real-World Scenarios

### Scenario 1: The "Deleted" Receipt
**Situation**: Parent claims they paid. Accountant says "No record found".
**Action**:
1.  Admin opens **Transaction Audit Log**.
2.  Filters by "Action: Delete" and "Module: Fee Collection".
3.  **Result**: Found a log entry: "Date: Yesterday 5:00 PM | User: Clerk_Ravi | Action: Deleted Receipt #1055".
4.  **Outcome**: Clerk_Ravi is questioned. Fraud prevented.

### Scenario 2: The Sudden Fee Hike
**Situation**: Parents complain that "Transport Fee" suddenly increased by ₹500 overnight.
**Action**:
1.  Principal checks the Audit Log for "Fee Structure" changes.
2.  **Result**: "Date: 2:00 AM | User: Admin_System | Update: Transport Fee changed from ₹2000 to ₹2500".
3.  **Outcome**: It was an authorized update, but the communication to parents was missed.

### Scenario 3: The Suspicious Discount
**Situation**: A student received a 100% waiver. The approval paper is missing.
**Action**:
1.  Trustee checks the log for "Waiver Applied".
2.  **Result**: "User: Guest_User | IP: 192.168.1.55".
3.  **Insight**: Someone shared the "Guest" password.
4.  **Action**: Password changed immediately.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Direct DB Edit** | A developer changes the fee amount directly in the SQL database, bypassing the app. | **Handling**: The Application Log won't catch this. *Solution*: Enable **Database-Level Triggers** to log SQL updates to a separate shadow table. |
| **System Auto-Actions** | The "Late Fee" was applied by the nightly scheduler, not a human. | **User ID**: Log these actions under a special system user "SYSTEM_BOT" or "CRON_JOB" to distinguish them from human actions. |
| **Log Volume** | Millions of logs generated, slowing down the system. | **Archival Policy**: Move logs older than 12 months to "Cold Storage" (Archive Database), keeping the live system light. |
| **Sensitive Data** | A user updated a password. Should the log show the new password? | **Redaction**: Never log sensitive PII or secrets. Show "Password Updated [REDACTED]" instead of the actual string. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Timestamp** | DateTime | Exact second of the action. |
| **User ID** | String | Who performed the action. |
| **Action** | Enum | `Create`, `Update`, `Delete`, `Login`. |
| **Target Object** | String | "Receipt #101" or "Student: Rahul". |
| **Old Value** | JSON | Data before change (snapshot). |
| **New Value** | JSON | Data after change. |
| **IP Address** | String | Device identifier. |

## User Actions
1.  **Filter Logs**: Search by Date Range, User, or Module.
2.  **Export Audit Trail**: Download a CSV for external auditors.
3.  **View Diff**: See a side-by-side comparison of "Before" vs "After".
4.  **Purge Old Logs**: (Only if permitted) Move 3-year-old logs to backup.

## Best Practices
- **Log EVERYTHING**: It's better to have too much data than to miss the one critical event.
- **Read-Only Access**: Even the Principal should only have *View* access to logs. No one should have *Delete* access.
- **Regular Review**: Don't wait for a crisis. Randomly review logs once a month to spot anomalies.
