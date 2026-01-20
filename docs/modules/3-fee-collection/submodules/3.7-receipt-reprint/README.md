# 3.7 Receipt Reprint

## Overview
**Receipt Reprint** is a utility function to generate copies of previously issued receipts. Unlike generating a *new* receipt (which affects accounting), reprinting simply retrieves historical data and formats it for printing again. Used often when parents lose the original or when office files need duplicates.

**In simple terms**: It's like the "Print Invoice" button on Amazon for an order you placed last year.

**Analogy**: 
-   **Photocopy**: You aren't buying the item again; you are just making a xerox of the proof of purchase.

## Purpose
To provide duplicate proof of payment for administrative, legal, or personal records without altering financial ledgers.

## Description
This submodule allows users to search for past receipts by Student Name, Receipt Number, or Date Range. It supports printing in various formats (Thermal, A4, A5) and typically adds a "Duplicate" watermark to distinguishes it from the original.

## Key Features
-   **Search & Retrieve**: Fast lookup of old transactions.
-   **Duplicate Marking**: Auto-stamps "DUPLICATE" on the output.
-   **Multi-Format**: Reprint a thermal slip as an A4 document if needed.
-   **Email Copy**: Option to email the PDF instead of printing.
-   **Bulk Reprint**: Generate all receipts for a specific day or student in one go.

## Real-World Scenarios

### Scenario 1: Printer Jam
**Background**: Cashier collected fee, saved the transaction. Printer jammed and paper tore.
**Action**: 
1.  Go to "Receipt Reprint".
2.  Select "Last Transaction".
3.  Click Print.
**Result**: Parent gets their receipt. No double counting of money.

### Scenario 2: Lost Receipt (Tax Proof)
**Background**: Parent comes in March asking for "April's Receipt" to claim HRA/Tax benefits.
**Action**: Search Student -> Filter Date (April) -> Reprint.
**Result**: "Duplicate" receipt issued.

### Scenario 3: Email Copy
**Background**: Parent calls: "I am out of station, please email me the receipt."
**Action**: Search Receipt -> Click "Email".
**Result**: PDF sent to registered email ID.

### Scenario 4: Auditor Requirement (Bulk)
**Background**: Auditor wants physical copies of all "Cheque" payments from January.
**Action**: Filter Mode="Cheque", Date="Jan". Select All -> Bulk Print.

### Scenario 5: Format Change
**Background**: School changed logo. Parent wants old receipt on new stationery.
**Action**: Reprinting renders the *old data* on the *current template*.

## Edge Cases & Handling

### Edge Case 1: Duplicate Watermark
**What Happens**: Parent tries to use duplicate receipt to claim reimbursement twice.
**System Behavior**: Risk of fraud.
**How to Handle**: Configuring the system to mandatorily print "DUPLICATE COPY" on 2nd print onwards.

### Edge Case 2: Reprint Count
**What Happens**: Security concern. Why was this receipt printed 50 times?
**System Behavior**: Suspicious activity.
**How to Handle**: Log the "Print Count" counter in database. Alert Admin if count > 5.

### Edge Case 3: Modified Data
**What Happens**: Student name was "Rohan". Changed to "Rohan Kumar" later.
**System Behavior**: Should reprint show "Rohan" (Historical) or "Rohan Kumar" (Current)?
**How to Handle**: Usually, receipts should preserve Historical Snapshot (Tax compliance). If not possible, disclaimer "Reprinted on [Date]".

### Edge Case 4: Cancelled Receipt
**What Happens**: Trying to reprint a receipt that was voided.
**System Behavior**: Misleading if it looks valid.
**How to Handle**: Overlay a massive "CANCELLED" watermark across the page.

### Edge Case 5: Printer Access Control
**What Happens**: Junior staff reprinting receipts to facilitate fake claims.
**System Behavior**: Unauthorized access.
**How to Handle**: "Reprint" permission is separate from "Collect Fee" permission.

### Edge Case 6: Thermal vs A4
**What Happens**: Original was on long thermal paper. Reprint requested on A4.
**System Behavior**: Formatting issues.
**How to Handle**: Responsive print templates that adapt to paper size.

### Edge Case 7: Batch Printing limits
**What Happens**: User tries to bulk print 10,000 receipts.
**System Behavior**: Server/Printer hangs.
**How to Handle**: Cap bulk operations to 50 or 100 at a time.

### Edge Case 8: Email Bounce
**What Happens**: "Email Receipt" success message shown, but email bounced.
**System Behavior**: User assumes sent.
**How to Handle**: Notification center should show "Email Delivery Failed".

### Edge Case 9: Digital Signature
**What Happens**: Original was signed manually. Reprint has no signature.
**System Behavior**: Invalid for tax?
**How to Handle**: Use Digital Signature (Image) on reprints if legally allowed.

### Edge Case 10: Date of Issue
**What Happens**: Receipt Date: Jan 1st. Reprint Date: Mar 1st.
**System Behavior**: Confusion on when payment happened.
**How to Handle**: Clearly distinguish "Transaction Date" vs "Print Date" on the document.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Receipt No | Search | Yes | Primary Key |
| Print Count | Number | Read-only | Security counter |
| Template | Dropdown | Yes | A4 / Thermal / Letterhead |
| Watermark | Boolean | Config | Toggle Duplicate text |

## User Actions
1.  **Search**: Find the record.
2.  **Preview**: See how it looks.
3.  **Print/Email**: Dispatch.

## Business Rules
-   Reprinting does *not* create a new financial transaction.
-   Reprinting a "Cheque" receipt that is still "Uncleared" should show status "Uncleared".

## Permissions Required
-   **Reprint Own**: Cashier.
-   **Reprint Old (>30 days)**: Admin.

## Related Submodules
-   **3.1 Quick Receipt**: Generates the original.
-   **3.6 Cancellation**: Prints the cancellation slip.

## API Endpoints
```
GET /api/fee-receipts/:id/pdf - Generate PDF
POST /api/fee-receipts/:id/email - Send Email
```

## Database Schema
```sql
Table: print_logs
- id (PK)
- receipt_id (FK)
- printed_by (FK)
- printed_at (TIMESTAMP)
- medium (PAPER/EMAIL)
```

## UI/UX Considerations
-   **Preview Pane**: Always show PDF preview before triggering printer to save paper.
-   **Quick Actions**: "Email to Parent" button directly on the list view.

## Best Practices
1.  **Limit Reprints**: Don't allow unlimited un-tracked reprints.
2.  **Watermarking**: Essential for distinguishing originals from copies.
3.  **Digital First**: Prefer emailing duplicates over printing to save paper and cost.
