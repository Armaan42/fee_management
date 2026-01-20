# 6.4 Academic Hold Management

## Overview
**Academic Hold Management** is the system's enforcement arm. It integrates with other modules (Library, Exam, Transport) to automatically restrict access for defaulting students. It converts a financial problem into an operational check, ensuring services are only provided to those who have paid for them.

### Real-World Analogy
Think of this as **Airport Passport Control**.
- **The Passenger**: The Student.
- **The Flight**: The Exam / Library Book / Bus Ride.
- **The Passport**: The "Clean Financial Record".
You can walk through the terminal (attend classes), but if your passport has a red stamp (Fee Hold), the gate won't open. You cannot board the flight until you clear the hold at the counter.

## Purpose
- **Stop Revenue Leakage**: Prevent defaulters from using optional services (like Bus or Canteen) they haven't paid for.
- **Enforce Exam Discipline**: Automate the withholding of Hall Tickets, removing the burden from the Principal.
- **Asset Protection**: Prevent library books from being issued to students who might leave without paying.
- **Automate Release**: Instantly remove restrictions 24/7 the moment payment is made online.

## Key Features
- **Cross-Module Blocking**: One click in Finance blocks access in Library, exam, and Transport modules.
- **Granular Holds**: Block specific services (e.g., "Stop Bus" but "Allow Exam").
- **Temporary Amnesty**: Issue a "48-Hour Pass" to allow a student to write an exam while payment is processing.
- **Hold Certificate**: Auto-generates a "Why am I blocked?" PDF for the parent.

## Real-World Scenarios

### Scenario 1: The Hall Ticket Block
**Situation**: Final Exams start tomorrow. Student X has ₹20,000 pending.
**Action**:
1.  Fee Module triggers **"Exam Hold"**.
2.  Student logs in to download Admit Card.
3.  Screen shows: "Access Denied. Liability: ₹20,000. Pay Now to unlocking."
4.  Parent pays online at 11 PM.
5.  **Result**: Hold auto-removed at 11:01 PM. Ticket downloaded.

### Scenario 2: The Library Freeze
**Situation**: Student goes to borrow a reference book.
**Action**:
1.  Librarian scans the ID card.
2.  Library Module checks Finance Status API.
3.  Alert Pops Up: **"Financial Hold. Do Not Issue."**
**Outcome**: Book stays in the library. Asset protected.

### Scenario 3: The Transport Stop
**Situation**: Transport fee unpaid for 2 months.
**Action**:
1.  Transport Manager gets a "Stop List".
2.  Student is removed from the "Bus Route Attendance" sheet.
3.  Bus Conductor informs student to resolve the due before boarding tomorrow.
**Outcome**: Service denied until payment is made.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Emergency Exam** | Student crying at exam hall entrance with no ticket. | Superintendent uses "Emergency Override" code to print a **"Provisional Ticket"** valid for 1 day. |
| **Return vs Issue** | Defaulter wants to *return* a library book. | System must **Accept Return** (get item back) but **Reject Issue** (give new item). Never block returns! |
| **Partial Hold** | Tuition Paid, but Transport Unpaid. | Only block Transport service. Allow Exam and Library access. (Targeted Sanctions). |
| **Manual Release** | Cheque submitted but not cleared. | Accountant manually enables "Trust Release" for 3 days. If cheque bounces, hold re-applies automatically. |
| **System Offline** | Exam hall has no internet to check live status. | Download "Offline Defaulter List" (CSV) at 8 AM to check at the door manually. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Hold ID** | String | Unique reference for the block. |
| **Block Type** | Enum | `Result`, `Library`, `Transport`, `LMS`, `All`. |
| **Reason** | String | "Tuition Fee Pending > 90 Days". |
| **Active Since** | Date | When the restriction started. |
| **Override By** | User | Who temporarily bypassed the block (if any). |
| **Override Expiry** | Date | When the temporary pass ends. |

## User Actions
1.  **Check Status**: "Is this student blocked?" (Green/Red Indicator).
2.  **Apply Hold**: Manually block a student for non-financial reasons (Discipline).
3.  **Grant Amnesty**: "Allow this student for 2 days".
4.  **View Hold History**: "Was this student blocked last term?"

## Best Practices
- **Auto-Release is Key**: If you block automatically, you MUST unblock automatically. Parents hate waiting for manual approval after paying.
- **Communicate Clearly**: The error message should say *exactly* how much is due and provide a "Pay Now" button.
- **Don't Block Learning**: Avoid blocking LMS (Class notes) unless absolutely necessary. Focus on "Premium Services" (Bus, Exams, Certificates).
