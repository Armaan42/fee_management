# 3.5 Fee Challan Generation

## Overview
**Fee Challan Generation** allows the school to outsource fee collection to a Bank. Instead of cashiers collecting money at the school counter, the system generates a specialized "Deposit Slip" (Challan) that parents take to a designated bank branch. The bank accepts the payment and updates the school later.

**In simple terms**: It's like a utility bill or electricity bill. You take the printed paper to the bank, pay the cash there, and get a stamped receipt.

**Analogy**: 
-   **Traffic Challan / Utility Bill**: You don't pay the policeman on the road. You take the "Ticket" to the court or bank to pay. Here, the school issues the ticket, and the bank collects the money.

## Purpose
To reduce cash handling risk at the school premises, avoid long queues at the school counter, and utilize the bank's infrastructure for easier collection.

## Description
This submodule creates, prints, and tracks Bank Challans. It links specific fee installments to a unique Challan Number. It also handles the reconciliation process when the bank provides the list of "Paid Challans" at the end of the day or week.

## Key Features
-   **Bulk Printing**: Generate PDF Challans for the entire class in one click.
-   **Bank Integration**: Pre-formatted templates for specific banks (SBI, HDFC, Fed, etc.).
-   **Validity Date**: Challans expire after a certain date to enforce discipline.
-   **Auto-Reconciliation**: Upload Excel file from bank to mark fees as "Paid" automatically.
-   **Barcoding**: Prints Barcode/QR code for faster scanning at the bank counter.

## Real-World Scenarios

### Scenario 1: Rural Payment Collection
**Background**: School is in a town where online payment adoption is low. Parents prefer cash but school doesn't want to handle cash.
**Action**: School prints SIB Bank Challans for all students.
**Process**: Parent goes to SIB Branch -> Pays Cash -> Teller stamps "Parent Copy" -> Parent keeps as proof.

### Scenario 2: Zero-Contact Distribution
**Background**: School sends fee details via PDF on WhatsApp.
**Action**: Parent prints the PDF at a cyber cafe and goes to the bank.

### Scenario 3: The 3-Copy System
**Background**: Standard Bank format.
**Components**: 
1.  **Bank Copy**: Retained by the teller for their records.
2.  **School Copy**: Dropped in a box at the school later (for manual verification).
3.  **Parent Copy**: Stamped key evidence of payment.

### Scenario 4: Late Fee Inclusion
**Background**: Challan generated on 15th (Due Date 10th).
**System Behavior**: System automatically adds "Late Fee: ₹50" to the Challan total before printing.

### Scenario 5: Reconciliation Day
**Background**: It's Friday. Admin downloads "CollectionReport.xlsx" from Bank Portal.
**Action**: Admin uploads this file to the School ERP.
**Result**: 450 students marked as "Paid" instantly.

## Edge Cases & Handling

### Edge Case 1: Expired Challan
**What Happens**: Valid till 20th. Parent goes to bank on 21st.
**System Behavior**: Bank teller rejects payment (System logic at bank end).
**How to Handle**: Parent must return to school for a "Revalidated Challan" (often with extra fine).

### Edge Case 2: Partial Payment at Bank
**What Happens**: Challan says ₹5000. Parent offers ₹3000 to teller.
**System Behavior**: Banks usually reject partials on Challans to avoid reconciliation mismatches.
**How to Handle**: Policy: "Challan payments must be Full Payments".

### Edge Case 3: Lost Challan
**What Happens**: Parent loses the paper.
**System Behavior**: No record of transaction yet.
**How to Handle**: Admin generates a "Duplicate Challan". (Ensure Challan ID remains same or invalidates previous one).

### Edge Case 4: Double Payment
**What Happens**: Parent pays via Challan at 10 AM. Pays Online at 11 AM (confused).
**System Behavior**: School receives money twice.
**How to Handle**: Reconciliation script detects "Already Paid". Marks second entry as "Advance/Credit".

### Edge Case 5: Invalid Challan ID
**What Happens**: Bank Teller types digit wrong (Manual entry error).
**System Behavior**: Upload fails ("Student Not Found").
**How to Handle**: Checksum digit in Challan ID (e.g., Mod-10 check) prevents typo entry.

### Edge Case 6: Fee Revision
**What Happens**: Challan printed for ₹5000. Fee hiked to ₹5500 next day.
**System Behavior**: Parent pays ₹5000.
**How to Handle**: Accepted. Balance ₹500 added to next month's due.

### Edge Case 7: Manual Reconciliation
**What Happens**: Bank file is corrupt. Parent is angry showing stamped slip.
**System Behavior**: Admin needs to mark paid manually.
**How to Handle**: "Manual Challan Settlement" screen. Input Challan No -> Mark Paid.

### Edge Case 8: Cheque Drop via Challan
**What Happens**: Parent attaches Cheque to Challan. Cheque bounces later.
**System Behavior**: Complex reconciliation.
**How to Handle**: Treat as "Cheque Bounce". Reverse the payment in ERP.

### Edge Case 9: Custom Fields
**What Happens**: Bank requires "Student Class" to be printed in bold at (X,Y) coordinates.
**System Behavior**: Template mismatch.
**How to Handle**: Flexible "Form Designer" for Challan printing.

### Edge Case 10: Challan Cancellation
**What Happens**: Parent decides to pay Online instead.
**System Behavior**: Open Challan exists.
**How to Handle**: Payment overwrites Challan status. Challan becomes void automatically.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Challan No | String | Yes | Unique ID (e.g., CH-2024-001) |
| Valid Upto | Date | Yes | Expiry date |
| Bank Name | Dropdown | Yes | Target Bank |
| Amount Breakdown | List | Yes | Tuition/Bus/Fine |
| Status | Enum | Yes | Generated / Paid / Cancelled |

## User Actions
1.  **Select Students**: Filter Class 10.
2.  **Generate**: Create Challans.
3.  **Print**: Send to printer/PDF.
4.  **Reconcile**: Upload Bank Statement.

## Business Rules
-   Challan generation locks the "Fee Structure" for that month (to prevent amount mismatch).
-   Challan ID must be unique globally.

## Permissions Required
-   **Generate**: Fee Admin.
-   **Reconcile**: Senior Accountant.

## Related Submodules
-   **3.1 Quick Receipt**: The alternative (Head Office collection).
-   **7.1 Reports**: "Challan Status Report".

## API Endpoints
```
POST /api/challans/generate - Bulk create
POST /api/challans/reconcile - Upload Excel
GET /api/students/:id/challans - History
```

## Database Schema
```sql
Table: fee_challans
- id (PK)
- challan_no (Unique)
- student_id (FK)
- total_amount (DECIMAL)
- valid_upto (DATE)
- status (PENDING/PAID)
- bank_ref_no (VARCHAR)
```

## UI/UX Considerations
-   **Print Layout**: CSS Print Media queries are critical. Must fit A4 (Landscape/Portrait) perfectly.
-   **Barcode**: Use font-based or image-based Code-128 barcode generation.

## Best Practices
1.  **Unique Series**: Prefix Challans (e.g., SIB-001, HDFC-001) to avoid bank confusion.
2.  **Instructions**: Print clear instructions on the Challan ("Do not accept after Date X").
3.  **Digital Copy**: Email the PDF to parent immediately upon generation.
