# 10.4 Bulk Receipt Generation

## Overview
**Bulk Receipt Generation** is the heavy-lifter of the documentation team. While the "Fee Assignment" module creates the demand (Invoice), this module creates the proof (Receipt). It is capable of generating thousands of PDF receipts in minutes, customized for print or email.

### Real-World Analogy
Think of this as a **High-Speed Newspaper Printing Press**.
- **Manual Mode**: A clerk handwriting 2000 receipts (Impossible).
- **Bulk Mode**: A giant press churning out 2000 copies in 10 minutes.
- **Distribution**: Just as newspapers are bundled for delivery boys, these receipts are bundled (Zipped) for class teachers or emailed directly to parents.

## Purpose
- **Mass Distribution**: At the end of the month, generate all receipts for Class 1 to 12 in one go.
- **Physical Archiving**: Many schools still keep a paper copy signed by parents. This tool prints 3 receipts per A4 page to save paper.
- **Audit Preparedness**: "Give me all receipts numbered 1001 to 5000". The system generates a consolidated PDF for the auditor.
- **Template Update**: If the school logo changes, you can "Regenerate" old receipts with the new branding instantly.

## Key Features
- **Filter & Print**: Select "Class 5 - Section A - Term 1" and click "Print".
- **Format Options**: A4 (Standard), A5 (Half Page), or Thermal (3-inch roll).
- **Zip Download**: Instead of one giant PDF, download a ZIP file containing 50 individual PDFs named `StudentName_RecNo.pdf`.
- **Watermarking**: Auto-adds "DUPLICATE" watermark if printing a receipt for the second time.

## Real-World Scenarios

### Scenario 1: The Month-End Filing
**Situation**: Accounts department needs physical copies of all 500 receipts generated today for the file.
**Action**:
1.  Admin filters: **Date = Today**.
2.  Click **"Bulk Print"**.
3.  **Outcome**: A single PDF with 500 pages is generated. Admin sends it to the laser printer.

### Scenario 2: The Email Blast
**Situation**: Parents are asking for receipts for tax proofs.
**Action**:
1.  Admin filters: **All Students**.
2.  Click **"Email Receipts"**.
3.  **Outcome**: System generates unique PDFs for each student and fires 2000 emails in the background.

### Scenario 3: The Logo Change
**Situation**: School changed its name from "St. Mary's" to "St. Mary's International". Old receipts look wrong.
**Action**:
1.  Admin updates Control Center (10.1).
2.  Runs **"Regenerate Receipts"** for the defined date range.
3.  **Outcome**: All historical receipts now carry the new header (digital version).

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Server Timeout** | Generating 5,000 PDFs constitutes a heavy load. | **Async Queue**: The request is sent to a background "Worker". User gets a notification: "Your download will be ready in 5 mins." |
| **Printer Jam** | Physical printing stopped at page 50 of 1000. | **Resume Capability**: The system allows "Print Range: 51-1000" so you don't have to restart from scratch. |
| **Missing Data** | A receipt record exists but has 0 amount. | **Skip Logic**: The generator auto-skips zero-value receipts to save paper and logs them in a "Skipped Report". |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Date Range** | DateRange | "01-Apr to 30-Apr". |
| **Class/Sec** | Filter | "Class 10-A". |
| **Template** | Enum | "Standard A4", "Thermal". |
| **Output** | Enum | PDF, ZIP, Email. |
| **Sort By** | Enum | Receipt No, Student Name. |
| **Copies** | Int | 1 (Original), 2 (Student+Office). |

## User Actions
1.  **Preview**: See the first 5 receipts to check alignment before printing 5000.
2.  **Download ZIP**: Get individual files for digital archiving.
3.  **Mark as Printed**: System flags receipts as "Hard Copy Issued" to prevent double issuance.
4.  **Filter Unprinted**: "Show me receipts generated but not yet printed".

## Best Practices
- **Paper Saving**: Use the "3-per-page" template for office copies. It saves 66% paper.
- **Naming Convention**: Generated filenames should be smart: `Class_Section_StudentName_RecID.pdf` for easy searching.
- **Nightly Jobs**: Schedule massive print jobs (entire school) for night-time to avoid slowing down the server during day operations.
