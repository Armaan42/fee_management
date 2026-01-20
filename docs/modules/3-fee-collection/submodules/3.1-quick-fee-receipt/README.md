# 3.1 Quick Fee Receipt

## Overview
**Quick Fee Receipt** is the "Fast Lane" for fee collection. It is the most used screen in the entire software, designed for cashiers to collect fees from parents in the shortest possible time. It prioritizes speed, accuracy, and minimal clicks to handle long queues efficiently.

**In simple terms**: It's like the checkout counter at a supermarket. You scan the student (Select), see the bill (Dues), take the money (Payment), and print the bill (Receipt).

**Analogy**: 
-   **Supermarket Checkout**: The cashier doesn't ask "How was your day?" or check your credit history. They just scan items, take cash, and give a receipt. This module does exactly that for school fees.

## Purpose
To streamline the daily fee collection process, reducing waiting time for parents and data entry effort for cashiers.

## Description
This submodule permits authorized users (Cashiers/Admins) to search for a student, view their outstanding dues breakdown, accept payment (Cash/Cheque/Online), and generate an instant receipt. It handles the financial transaction and updates the student's ledger in real-time.

## Key Features
-   **Smart Search**: Find student by Name, Admission No, Reg No, or Parent Mobile.
-   **Auto-Calculation**: Automatically sums up Tuition, Transport, and Fines.
-   **Partial Payment**: Accepts whatever amount the parent pays (e.g., Paying ₹5000 out of ₹10000 due).
-   **Multiple Modes**: Record Cash, Cheque, UPI, or Card payments.
-   **Instant Print**: Generates PDF receipt immediately upon saving.

## Real-World Scenarios

### Scenario 1: Standard Monthly Collection
**Background**: Parent comes to pay the current month's fee in Cash.
**Action**: 
1.  Search Student "Rohan Sharma".
2.  System shows "April Fee Due: ₹2500".
3.  Cashier enters "Received: ₹2500".
4.  Click "Save & Print".
**Result**: Receipt #101 generated. Dues cleared.

### Scenario 2: Multi-Month Payment (Quarterly)
**Background**: Parent wants to pay for April, May, and June together to avoid coming back.
**Action**: 
1.  Select Student.
2.  Tick checkboxes for April, May, and June installments.
3.  System updates Total Due: ₹7500.
4.  Collect ₹7500.
**Result**: Fees cleared for 3 months.

### Scenario 3: Fine Collection
**Background**: Parent is paying 10 days late. System has added ₹50 Fine.
**Action**:
1.  System displays: Tuition ₹2000 + Late Fine ₹50. Total ₹2050.
2.  Parent argues about fine. Cashier says "System calculated".
3.  Parent pays ₹2050.
**Result**: Principal and Fine heads recorded separately in ledger.

### Scenario 4: Paying via Cheque
**Background**: Parent gives a cheque for ₹10,000.
**Action**:
1.  Select Payment Mode: "Cheque".
2.  Enter Cheque No: "123456", Date: "20-Jan-2024", Bank: "HDFC".
3.  Save.
**Result**: Receipt generated (Subject to Realization).

### Scenario 5: Search & Collect (Unknown ID)
**Background**: Grandfather comes to pay fee but doesn't know "Admission Number". Knows child is "Pinky" in "Class 4".
**Action**:
1.  Filter Class: 4.
2.  Search Name: "Pinky".
3.  Select correct Pinky from results.
4.  Proceed to pay.

## Edge Cases & How to Handle Them

### Edge Case 1: Internet Loss
**What Happens**: Cashier clicks "Save", internet disconnects.
**System Behavior**: Did the transaction go through?
**How to Handle**: Check "Last Receipt No" or "Recent Transactions" list before re-entering. If unsure, wait for connection.

### Edge Case 2: Printer Jam
**What Happens**: Software says "Saved successfully", but printer gives no paper.
**System Behavior**: Receipt is created in backend.
**How to Handle**: Do *not* create new receipt. Go to "3.7 Receipt Reprint" and print duplicate.

### Edge Case 3: Cheque Bounce Risk
**What Happens**: Collecting Cheque without entering Cheque Number.
**System Behavior**: Audit failure. Hard to track if it bounces.
**How to Handle**: Validation rule: If Mode = Cheque, field "Cheque No" is Mandatory.

### Edge Case 4: Duplicate Payment
**What Happens**: Parent paid online 5 mins ago. Standing in queue to pay cash too.
**System Behavior**: Ledger might not have refreshed if offline.
**How to Handle**: Always "Refresh" student data before accepting cash. System should warn "Recent Online Payment Detected".

### Edge Case 5: Rounding Errors
**What Happens**: Bill is ₹1000.33. Parent gives ₹1000.
**System Behavior**: ₹0.33 remains as "Due".
**How to Handle**: Use "Round Off" feature (auto-waive small decimals) or carry forward to next month.

### Edge Case 6: Backdated Receipt
**What Happens**: Fee collected yesterday manually (power cut). Entry being done today.
**System Behavior**: Receipt date defaults to Today.
**How to Handle**: Admin permission required to change "Receipt Date". Warning: Affects daily cash report of yesterday.

### Edge Case 7: Future Date
**What Happens**: Entering a receipt date of tomorrow.
**System Behavior**: Accounting mess (Future revenue?).
**How to Handle**: Strictly block future dates.

### Edge Case 8: Wrong Student
**What Happens**: Cashier selected "John Smith (Class 5)" but money was for "John Smith (Class 6)".
**System Behavior**: Money credited to wrong account.
**How to Handle**: Immediately cancel receipt (3.6) and re-do for correct student.

### Edge Case 9: Currency Denomination
**What Happens**: Cashier has ₹50,000 cash at end of day. Need to tally.
**System Behavior**: Discrepancy between System Total and Physical Cash.
**How to Handle**: Use "Denomination Input" (2000x5, 500x20) to tally exactly.

### Edge Case 10: Concurrent Access
**What Happens**: Two cashiers try to collect fee for same student simultaneously (Rare).
**System Behavior**: Double payment / Negative balance using race condition.
**How to Handle**: Database locking on Student Ledger during write operation.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Student | Search | Yes | Target payer |
| Payment Date | Date | Yes | Defaults to Today |
| Pay Mode | Dropdown | Yes | Cash/Cheque/Card/UPI |
| Amount | Currency | Yes | Total received |
| Remarks | Text | No | "Paid by Uncle" |
| Instrument No | Text | No | Cheque/Ref Number |

## User Actions
1.  **Search**: Locate student.
2.  **Verify**: Check Dues.
3.  **Input**: Enter Amount & Mode.
4.  **Save**: Commit transaction.
5.  **Print**: Handover receipt.

## Business Rules
-   Receipt cannot be generated for ₹0 amount (unless specific settings allow zero-value receipts).
-   Cannot pay more than Total Dues + Advance Limit.

## Permissions Required
-   **Create**: Fee Cashier.
-   **View**: Fee Admin.

## Related Submodules
-   **3.6 Receipt Cancellation**: To fix mistakes made here.
-   **3.7 Receipt Reprint**: If printer fails.

## API Endpoints
```
POST /api/fee-receipts - Generate new receipt
GET /api/students/:id/dues - Get dues
```

## Database Schema
```sql
Table: fee_receipts
- id (PK)
- receipt_no (Unique)
- student_id (FK)
- amount (DECIMAL)
- payment_mode (ENUM)
- transaction_date (DATE)
```

## UI/UX Considerations
-   **Tab Navigation**: Cashier should be able to operate mostly with Keyboard (Tab, Enter) for speed.
-   **Large Fonts**: Total Amount and Student Name should be very visible to avoid errors.

## Best Practices
1.  **Verify Name**: Always ask parent "Father's Name is [Name]?" before saving.
2.  **Count Cash First**: Count physical cash *before* clicking "Save".
3.  **Mandatory Remarks**: For Cheque/Draft, always type Bank Name.
