# 3.4 Multiple Payment Modes

## Overview
**Multiple Payment Modes** ensures that the school can accept fees via any channel—Cash, Cheque, Card, UPI, or Bank Transfer—and record each transaction accurately. This flexibility reduces friction for parents and ensures that the school's accounts tally with the bank statement at the end of the day.

**In simple terms**: It allows the system to say "Yes" whether the parent hands over a bundle of cash, a cheque, or scans a QR code.

**Analogy**: 
-   **Digital Wallet**: Just like you can pay for Uber using PayTM, Credit Card, or Cash, the school fee system supports all these "Payment Methods" and tracks them separately.

## Purpose
To accommodate parent preferences for payment, modernize fee collection, and maintain distinct ledgers for Cash vs. Bank transactions.

## Description
This submodule configures and manages the various ways fees can be collected. It enforces data entry rules for each mode (e.g., "Cheque" requires Bank Name, "UPI" requires Transaction ID) and generates mode-specific reports for reconciliation.

## Key Features
-   **Cash Handling**: Basic receipt generation.
-   **Cheque Management**: Tracking clearing dates, bank names, and bounce status.
-   **Digital Payments**: Recording UPI/NEFT/IMPS references.
-   **Split Payment**: Accepting part Cash and part Cheque for a single bill.
-   **Offline Card Entry**: Recording "Auth Code" from external POS machines.

## Real-World Scenarios

### Scenario 1: Split Payment (Pop-Pourri)
**Background**: Total Fee ₹10,000. Parent has ₹2,000 cash in pocket desire to pay rest via Cheque.
**Action**:
1.  Select Mode "Split".
2.  Entry 1: Cash - ₹2,000.
3.  Entry 2: Cheque - ₹8,000 (Bank: SBI, No: 123).
**Result**: Single Receipt showing both details.

### Scenario 2: UPI QR Scan
**Background**: School has a printed QR code on the counter. Parent scans and pays ₹5,000.
**Action**:
1.  Select Mode "UPI".
2.  Cashier asks for "UTR / Reference Number" from parent's phone.
3.  Enter UTR: "3122XXXXXXXX".
**Result**: Transaction tagged as Bank Transfer.

### Scenario 3: Post-Dated Cheque (PDC)
**Background**: Parent gives a cheque dated 1st of next month.
**Action**:
1.  Enter Cheque Date: [Next Month].
2.  System marks status as "Received - Uncleared".
**Result**: Fee receipt generated, but Revenue not realized until cheque date.

### Scenario 4: Bank Transfer (NEFT) from Home
**Background**: Parent transfers money from home. Sends WhatsApp screenshot to Accountant.
**Action**:
1.  Accountant verifies credit in Bank Statement.
2.  Enters receipt with Mode "NEFT" and Notes "Ref verified on [Date]".
**Result**: Remote collection recorded.

### Scenario 5: Card Swipe
**Background**: School has a PineLabs machine. Parent swipes Credit Card.
**Action**:
1.  Select Mode "Card".
2.  Enter "Card Last 4 Digits" and "Auth Code" from the slip.
**Result**: Separate report for "Card Settlements" to check against bank.

## Edge Cases & Handling

### Edge Case 1: Cheque Bounce
**What Happens**: Cheque of ₹10,000 dishonored by bank due to low funds.
**System Behavior**: Money was "Received" but is now "Lost".
**How to Handle**: Use "Cheque Return" workflow -> Reverse Fee -> Add "Cheque Bounce Fine" -> Mark Dues as Pending.

### Edge Case 2: Duplicate UTR
**What Happens**: Two parents claim the same UPI Transaction ID (copy-paste error or fraud).
**System Behavior**: Duplicate entry.
**How to Handle**: System must enforce "Unique Constraint" on Transaction ID field for online modes.

### Edge Case 3: Offline Mode
**What Happens**: Card machine works, but School Server is down.
**System Behavior**: Cashier writes manual receipt.
**How to Handle**: "Backdated Entry" allowed next day with Admin Approval.

### Edge Case 4: Mode Switching
**What Happens**: Cashier accidentally recorded "Cash" but it was a "Cheque".
**System Behavior**: Day End Report mismatch (Cash shortage, Cheque excess).
**How to Handle**: "Edit Receipt Mode" feature (Audit log required).

### Edge Case 5: Service Charge
**What Happens**: Credit Card charges 2% MDR. Fee is ₹10,000. School gets ₹9,800.
**System Behavior**: Deficit.
**How to Handle**: 
-   Option A: Charge Parent ₹10,200 (Pass on MDR).
-   Option B: Book ₹200 as "Bank Charge Expense".

### Edge Case 6: Unclear Handwriting
**What Happens**: Cheque number typed wrong (112233 instead of 112283).
**System Behavior**: Bank reconciliation fails.
**How to Handle**: Feature to "Upload Photo" of the instrument (Cheque/Slip).

### Edge Case 7: Fake Screenshot
**What Happens**: Parent shows fake GPay success screen. Cashier generates receipt. Money never comes.
**System Behavior**: Revenue Loss.
**How to Handle**: Policy: "No Receipt until SMS confirmation on School Phone".

### Edge Case 8: Cash Handling Limit
**What Happens**: Parent tries to pay ₹2 Lakhs in cash (Govt restriction in India).
**System Behavior**: Compliance risk.
**How to Handle**: Warning popup: "Cash receives > ₹1.99L requires PAN Card / Not Allowed".

### Edge Case 9: Foreign Currency
**What Happens**: NRI parent pays in USD cash.
**System Behavior**: System base currency is INR.
**How to Handle**: Convert to INR at current exchange rate and record INR equivalent.

### Edge Case 10: Wallet/Scholarship Adjustment
**What Happens**: "Payment" is actually an internal scholarship adjustment.
**System Behavior**: No money changes hands.
**How to Handle**: Special Mode "Journal Adjustment" or "Scholarship".

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Mode Name | Text | Yes | "HDFC Cheque" |
| Instrument No | Text | Conditional | Cheque/DD/Ref No |
| Instrument Date | Date | Conditional | Date on Cheque |
| Bank Name | Text | Conditional | Issuing Bank |
| Branch | Text | No | Branch Name |
| Auth Code | Text | Conditional | For Cards |

## User Actions
1.  **Select Mode**: Choose from dropdown.
2.  **Enter Details**: Fill mandatory bank details.
3.  **Upload Proof**: Optional photo.
4.  **Confirm**: Save transaction.

## Business Rules
-   "Cash" mode does not require external reference numbers.
-   "Cheque" mode receipts are "Provisional" until cleared.

## Permissions Required
-   **Config Modes**: Fee Admin.
-   **Collection**: Fee Cashier.

## Related Submodules
-   **3.1 Quick Receipt**: Uses these modes.
-   **3.6 Receipt Cancellation**: If mode was wrong.

## API Endpoints
```
GET /api/payment-modes - List enabled modes
POST /api/cheque-bounce - Handle reversal
```

## Database Schema
```sql
Table: payment_transactions
- id (PK)
- receipt_id (FK)
- mode (ENUM)
- amount (DECIMAL)
- instrument_no (VARCHAR)
- instrument_date (DATE)
- bank_name (VARCHAR)
- status (CLEARED/PENDING/BOUNCED)
```

## UI/UX Considerations
-   **Dynamic Form**: Selecting "Cheque" reveals "Bank Name" field. Selecting "Cash" hides it.
-   **Icons**: Use visual icons for Cash, Card, Bank to speed up selection.

## Best Practices
1.  **Daily Reconciliation**: Cashier must tally Cash vs System Report and Cheques vs System Report daily.
2.  **Mandatory Fields**: Never allow "Cheque" without a number. It makes tracking impossible.
3.  **Digital First**: Incentivize digital payments to reduce cash handling risks (theft/fake notes).
