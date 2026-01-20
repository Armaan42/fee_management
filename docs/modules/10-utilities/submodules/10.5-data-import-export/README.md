# 10.5 Data Import Export

## Overview
**Data Import/Export** is the bridge between this software and the outside world. Whether you are migrating from an old legacy system (Import) or sending data to the Auditor's Tally software (Export), this module ensures safe, structured, and bulk movement of data without manual typing.

### Real-World Analogy
Think of this as **Movers & Packers / Shipping Containers**.
- **Import**: Bringing furniture (Data) from your old house (Excel/Legacy App) into the new house (Our System). You don't carry one chair at a time; you load a truck (CSV File).
- **Export**: Packing items to send to the accountant.
- **Validation**: The guard at the gate checks if the furniture is broken before letting it in. (System checks "Is Mobile Number 10 digits?" before importing).

## Purpose
- **Onboarding Speed**: reducing the setup time from 1 month (manual entry) to 1 day (Excel upload).
- **Interoperability**: Syncing daily collections with Accounting Software (Tally/QuickBooks) or Biometric Devices.
- **Backup/Reporting**: Letting users download "All Data" to keep a local copy for peace of mind.
- **Bulk Updates**: Need to correct the spelling of "Apartment" for 500 students? Export -> Find & Replace in Excel -> Import back.

## Key Features
- **Smart Mapping**: Map "Student Name" column in Excel to "First Name" field in Database via a drag-and-drop UI.
- **Validation Engine**: Pre-checks data for errors (e.g., Duplicate Admission No, Invalid Email) *before* saving.
- **Templates**: Download blank Excel templates (Student_Template.xlsx) to know exactly what format is required.
- **Partial Success**: If 90 out of 100 rows are correct, it imports 90 and gives an "Error Log" for the 10 failed ones.

## Real-World Scenarios

### Scenario 1: The New Setup
**Situation**: School purchases the software. They have student data in a messy Excel sheet.
**Action**:
1.  Admin downloads **"Student Import Template"**.
2.  Copies data from old sheet to new template.
3.  Uploads to system.
4.  **Outcome**: 2000 Student Profiles created in 5 minutes.

### Scenario 2: The Tally Sync
**Situation**: Accountant needs to file GST returns and wants today's collection data in Tally.
**Action**:
1.  Admin goes to **Export -> Tally XML**.
2.  Selects Date: Today.
3.  **Outcome**: A file is generated which can be directly imported into Tally, creating adjacent Vouchers automatically.

### Scenario 3: The Library Integration
**Situation**: The Library software needs a list of all active students to issue cards.
**Action**:
1.  Admin runs **Export -> CSV**.
2.  Selects fields: AdmNo, Name, Class, Section.
3.  **Outcome**: A lightweight CSV file is shared with the Librarian.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Duplicate Data** | Importing a file that contains students who already exist. | **Upsert Logic**: System asks: "Skip duplicates" or "Update existing records"? Default is Skip to prevent overwriting. |
| **Date Formats** | Excel has `12/05/2023` (Dec 5 vs May 12). | **User Prompt**: The wizard asks the user to define the format (`DD/MM/YYYY`) during upload to ambiguity. |
| **Large Files** | Uploading a 50MB CSV with 100,000 rows. | **Chunking**: The browser splits the file into small chunks (1000 rows each) and uploads them sequentially to prevent timeout. |
| **Special Characters** | Names containing accents or Emojis. | **UTF-8 Encoding**: Ensure the parser supports UTF-8 to handle names like "Renée" correctly. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Job ID** | String | Unique Import Session ID. |
| **Filename** | String | "Student_Data_Final.csv". |
| **Total Rows** | Int | 1000. |
| **Success Count** | Int | 950. |
| **Error Count** | Int | 50. |
| **Error Log** | File | Link to CSV containing failed rows. |

## User Actions
1.  **Download Template**: Get the format.
2.  **Map Columns**: "Excel Col A -> DB Field Name".
3.  **Dry Run**: Test the first 5 rows for errors.
4.  **Rollback**: "Undo Import Job #55" (deletes the 200 records created 5 mins ago).

## Best Practices
- **Never Undo**: Avoid using "Undo" for updates. It's safer to re-import with corrected data.
- **Sample Test**: Always import just 1-2 rows first to verify data lands in the right fields.
- **Sanitize Excel**: Remove formulas, macros, and formatting (Bold/Color) from the Excel sheet before uploading. Keep it raw text.
