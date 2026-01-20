# 10.6 Transaction History Viewer

## Overview
**Transaction History Viewer** is the digital passbook of the school's finance system. It logs every single financial event—whether it's a student paying fees, a bounce charge being levied, a refund being processed, or an admin deleting a receipt. It provides an immutable timeline of events for audit and investigation.

### Real-World Analogy
Think of this as a **Bank Passbook / CCTV Playback**.
- **The Entry**: Every time money moves, a line is written.
- **The Audit**: If money goes missing, you "Rewind the Tape" (Scroll back history) to see who took it and when.
- **The Search**: Finding a specific transaction is like scanning the CCTV footage for "Tuesday at 2 PM".

## Purpose
- **Dispute Resolution**: When a parent says "I paid last month", you can check the logs to see if the payment Failed, Bounced, or Succeeded.
- **Fraud Detection**: Spotting suspicious patterns, like a receipt being generated and then deleted 5 minutes later by the same user.
- **Reconciliation**: Matching the "System Total" with the "Bank Statement" by ticking off transactions one by one.
- **Performance Analysis**: Analyzing "Which payment mode is most popular?" (UPI vs Cash) based on volume.

## Key Features
- **Global Search**: Find a transaction by Receipt No, Student Name, Cheque No, or Transaction ID.
- **Advanced Filters**: "Show me all [Cash] transactions between [1st Jan] and [31st Jan] collected by [Mr. Sharma]".
- **Status Color Codes**: Green (Success), Red (Failed), Orange (Pending), Grey (Cancelled).
- **Export to Excel**: Download the filtered list for further analysis in spreadsheets.

## Real-World Scenarios

### Scenario 1: The "Double Deduction" Claim
**Situation**: Parent claims money was cut twice from their bank account.
**Action**:
1.  Admin searches Student Name in **History Viewer**.
2.  **Result**: Shows 2 entries. One "Success" (Receipt Generated), One "Failed" (Gateway Error).
3.  **Outcome**: Admin explains "The failed transaction will be auto-refunded by your bank in 3 days." Proof provided.

### Scenario 2: The Mystery Deletion
**Situation**: Auditor finds a gap in receipt sequence. Receipt #5005 is missing.
**Action**:
1.  Admin filters by "Status: Deleted".
2.  **Result**: Finds Receipt #5005. Log says: "Deleted by Admin on 12th Aug. Reason: Wrong Class Entered."
3.  **Outcome**: Audit query resolved.

### Scenario 3: The Collection Summary
**Situation**: Principal asks "How much Cash did we collect today vs Online?"
**Action**:
1.  Admin filters Date: **Today**.
2.  Groups by **Payment Mode**.
3.  **Outcome**: Instant view: Cash ₹20,000 | Online ₹1,50,000.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Ghost Transactions** | Money deducted but no entry in software (Network Packet Drop). | **Requery Mechanism**: The viewer has a "Check Status" button that pings the Gateway Provider to fetch the missing status. |
| **Large Data Range** | Searching "All transactions" for 10 years (1 million rows). | **Pagination & Lazy Load**: System loads only 50 rows at a time. "Export" runs as a background job to prevent browser crash. |
| **Timezone Confusion** | Parent paid at 11:30 PM in USA, School sees it as next day. | **UTC Standardization**: All logs are stored in UTC but displayed in the User's Local Time (IST/EST) to ensure accuracy. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Txn ID** | String | Unique Ref (Internal). |
| **Date/Time** | DateTime | 2023-12-01 14:30:00. |
| **Amount** | Currency | ₹5000.00. |
| **Mode** | Enum | Cash, Cheque, Online. |
| **Status** | Enum | Success, Failed, Deleted. |
| **User** | String | "Admin (Ravi)". |
| **Remarks** | Text | "Late fee waived". |

## User Actions
1.  **Drill Down**: Click a row to see the full Receipt or Invoice associated with the transaction.
2.  **Void Transaction**: Cancel a successful cash receipt (Reverse entry).
3.  **Resend Receipt**: Email the proof of payment again to the parent from the history view.
4.  **Add Remark**: Append a note "Parent promised to clear bounce charge next week" to a failed cheque entry.

## Best Practices
- **Read-Only Access**: Most staff should only have "View" rights. Only Super Admin should be able to "Delete" or "Void".
- **Regular Export**: Download monthly transaction logs and archive them offline for safety.
- **Monitor Deletions**: Regularly check the "Deleted Transactions" report to ensure staff are not pocketing cash and deleting receipts.
