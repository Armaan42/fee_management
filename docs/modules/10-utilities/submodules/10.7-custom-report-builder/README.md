# 10.7 Custom Report Builder

## Overview
**Custom Report Builder** enables the school administration to break free from the constraints of "Standard Reports". While the system comes with 50+ pre-built reports, every school has unique needs. This module provides a "Drag-and-Drop" interface to let users analyze data their way.

### Real-World Analogy
Think of this as a **Subway Sandwich Station / Salad Bar**.
- **The Menu (Standard Reports)**: ordering a "Veggie Delight" (Fixed ingredients). Quick, but rigid.
- **The Builder (Custom Reports)**: "I want white bread, extra cheese, no onions, add olives." (You choose the columns).
- **The Result**: A report that answers *your* specific question, not just what the developer thought you might need.

## Purpose
- **Ad-Hoc Analysis**: Answering one-off questions like "List all Girls in Class 10 who take the Bus and haven't paid fees".
- **Cross-Module Data**: Combining data from "Admission" (Parent Name), "Transport" (Route No), and "Fee" (Balance) into a single view.
- **Export Flexibility**: Creating CSVs formatted exactly as required by third-party tools (e.g., Govt Scholarship Portal upload format).
- **Save & Reuse**: Build a complex query once, save it as "My Monthly Review", and run it with one click forever.

## Key Features
- **Column Picker**: Checkboxes to select which fields to show (e.g., Name, AdmNo, Balance, Mobile).
- **Filter Logic**: Add conditions like `Balance > 5000` AND `Class = 10`.
- **Sorting & Grouping**: "Group by Section", "Sort by Amount Descending".
- **Visuals**: Turn the data table into a Bar Chart or Pie Chart instantly.

## Real-World Scenarios

### Scenario 1: The Transport Audit
**Situation**: Transport Manager needs a list of students on "Route 5" with their Father's Mobile Number to create a WhatsApp Group.
**Action**:
1.  **Select Columns**: Student Name, Class, Father Mobile.
2.  **Add Filter**: `Bus Route` equals `Route 5`.
3.  **Run Report**: A list of 40 students appears.
4.  **Outcome**: Manager exports to Excel and creates the group.

### Scenario 2: The Scholarship Eligibility
**Situation**: Principal wants to find students who are "Single Girl Child" and have score > 90% (if marks module integrated).
**Action**:
1.  **Select Columns**: Name, Gender, Marks.
2.  **Add Filter**: `Gender` equals `Female` AND `Sibling Count` equals `0`.
3.  **Outcome**: Targeted list for scholarship distribution.

### Scenario 3: The "Top Defaulters" Wall of Shame
**Situation**: Accountants want a list of top 10 defaulters across the whole school.
**Action**:
1.  **Select Columns**: Name, Class, Total Due.
2.  **Sort By**: `Total Due` (Descending).
3.  **Limit**: Top 10.
4.  **Outcome**: Instant visibility on high-value pending payments.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Performance Overload** | User selects 50 columns for all 5000 students. | **Warning Throttling**: System warns "This query will take time. Run in Background?". It limits preview to first 100 rows. |
| **Permission Violation** | Junior Staff tries to add "Guardian Income" or "Staff Salary" to a report. | **Field-Level Security**: Sensitive columns are greyed out/hidden based on the User's Role. |
| **Broken References** | A saved report uses a Fee Head "Term 1" which was deleted yesterday. | **Validation Check**: When running a saved report, system checks if all columns still exist. If not, it prompts "Column 'Term 1' not found. Remove from report?". |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Report Name** | String | "Bus 5 Girls List". |
| **Columns** | JSON Array | `["name", "class", "mobile"]`. |
| **Filters** | JSON Object | `{"route": "5", "gender": "F"}`. |
| **Sort Order** | String | `name ASC`. |
| **Created By** | User | "Admin". |
| **Last Run** | Date | Today. |

## User Actions
1.  **Design**: The canvas where you build the report.
2.  **Preview**: See live data as you build.
3.  **Save As**: "Save as New Report" to keep it for later.
4.  **Schedule**: Email this report to Principal every Monday morning automatically.

## Best Practices
- **Naming Conventions**: Name reports clearly (e.g., "Transport_Route5_Phones" instead of "New Report 1").
- **Clean Filters**: Don't leave empty filters. If you don't need a filter, remove it to avoid confusing results.
- **Sharing**: Share useful reports with other users so they don't have to rebuild them from scratch.
