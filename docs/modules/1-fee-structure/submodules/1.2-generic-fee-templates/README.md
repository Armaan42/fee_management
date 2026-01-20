# 1.2 Generic Fee Templates

## Overview
Think of a **Fee Template** as a "Standard Package" or a "Combo Meal" for school fees. Instead of adding Tuition Fee, Sports Fee, and Library Fee one by one for every single student (which would take forever!), you create a single template called "Class 10 Standard Fee" containing all these items. Then, you just assign this **one template** to all Class 10 students.

**In simple terms**: It’s a "Master List" of fees for a specific group of students. You define the fee structure once, and apply it to hundreds of students in a few clicks.

**Real-world analogy**: When you subscribe to Netflix, you pick a "Standard Plan" or "Premium Plan". You don't pick "Movie Access" + "TV Show Access" + "HD Quality" separately. The plan bundles everything. Similarly, a Fee Template bundles all necessary fees (Tuition, Lab, Exam) into one plan for the student.

## Purpose
Set standard fee structures by class/section/stream that can be reused and assigned to multiple students.

## Description
This submodule allows administrators to create fee templates that define the complete fee structure for a particular class, section, or stream. Templates streamline the fee assignment process and ensure consistency.

## Key Features
- Create reusable fee templates
- Define multiple fee heads within a template
- Set amounts for each fee head
- Specify payment frequency
- Assign templates to classes/sections/streams
- Duplicate templates for quick creation
- Version control for templates

## Use Cases
- **Class-based Templates**: Different fee structures for Class 1, Class 2, etc.
- **Section-based Templates**: Different fees for Section A vs Section B
- **Stream-based Templates**: Different fees for Science, Commerce, Arts streams
- **Special Programs**: Templates for IB, IGCSE, or other special programs

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Template Name | Text | Yes | Descriptive name (e.g., "Class 10 - Science Stream") |
| Academic Year | Dropdown | Yes | Applicable academic year |
| Class | Dropdown | Yes | Target class |
| Section | Dropdown | No | Specific section (optional) |
| Stream | Dropdown | No | Academic stream (optional) |
| Fee Heads | Multi-select | Yes | List of applicable fee heads with amounts |
| Total Amount | Auto-calculated | Yes | Sum of all fee heads |
| Is Active | Checkbox | Yes | Whether template is currently in use |

### Fee Head Configuration within Template
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Fee Head | Dropdown | Yes | Select from defined fee heads |
| Amount | Number | Yes | Fee amount for this head |
| Frequency | Dropdown | Yes | One-time/Monthly/Quarterly/Yearly |
| Is Mandatory | Auto | Yes | Inherited from fee head |

## User Actions
1. **Create Template**
- Click "+ Create Template"
- Enter template details
- Add fee heads with amounts
- Set payment frequency for each head
- Review total amount
- Save template

2. **Duplicate Template**
- Select existing template
- Click "Duplicate"
- Modify name and details
- Adjust fee amounts as needed
- Save as new template

3. **Edit Template**
- Select template
- Modify details or fee heads
- Save changes
- System creates new version

4. **Assign Template**
- Select template
- Choose target students/class
- Bulk assign to all students
- Confirm assignment

5. **View Template**
- View all templates in grid/list
- Filter by class/section/year
- Search by name
- Preview fee breakdown

## Real-World Scenarios

### Scenario 1: Annual Fee Setup for Primary Classes
**Background**: The academic year is beginning. The school needs to set up the standard fee structure for Class 1.

**Steps**:
1.  Admin goes to **Fee Templates**.
2.  Clicks **Create Template**.
3.  Names it: "Class 1 - General - 2024-25".
4.  Adds Fee Heads:
    -   Tuition Fee: ₹25,000 (Yearly)
    -   Activity Fee: ₹2,000 (Yearly)
    -   Library Fee: ₹1,000 (Yearly)
5.  Saves the template.

**Result**: A ready-to-use fee structure for all Class 1 students.

### Scenario 2: Science Stream Implementation
**Background**: Class 11 Science students pay different fees than Commerce students due to Laboratory charges.

**Steps**:
1.  Admin creates a template "Class 11 - Science - 2024-25".
2.  Adds standard heads (Tuition, Exam Fee).
3.  Adds the specific head: "Science Lab Fee" (₹5,000).
4.  Saves the template.
5.  Creates a separate template "Class 11 - Commerce - 2024-25" *without* the Lab Fee.

**Result**: Accurate billing for different streams without manual adjustment per student.

### Scenario 3: Mid-Year Fee Hike (New Admissions Only)
**Background**: The school decides to increase the Admission Fee for students joining after October.

**Steps**:
1.  Admin finds the existing "Class 5 - General" template.
2.  Clicks **Duplicate**.
3.  Renames it to "Class 5 - General - Batch 2".
4.  Updates the "Admission Fee" amount from ₹5,000 to ₹7,000.
5.  Saves the new template.

**Result**: Old students stay on the old rate; new admissions get the new rate.

### Scenario 4: Special Integrated Program (IIT/NEET Coaching)
**Background**: Some students stick back for special coaching and need to be charged extra.

**Steps**:
1.  Admin creates a template "Class 12 - Integrated Program".
2.  Adds the base Tuition Fee.
3.  Adds "Coaching Fee" (₹15,000).

**Result**: Students in this program are billed correctly for the extra service.

### Scenario 5: Correcting a Wrong Fee Amount
**Background**: Admin accidentally set Tuition Fee as ₹20,00 instead of ₹20,000 in a template.

**Steps**:
1.  Admin opens the template.
2.  Corrects the amount to ₹20,000.
3.  Saves.

**Note**: If this template was already assigned, this change creates a *new version*. You may need to re-assign or specifically update the students (depending on configuration) to reflect the fix.

## Edge Cases & How to Handle Them

### Edge Case 1: Template with Zero Total Amount
**What Happens**: Admin creates a template but enters '0' for all amounts.
**System Behavior**: System warns "Total amount is zero. Are you sure?" or blocks saving.
**How to Handle**: Ensure at least one fee head has a positive value. If it's a scholarship case, use Concessions (Module 1.4), not a zero template.

### Edge Case 2: Duplicate Fee Heads in One Template
**What Happens**: Admin adds "Tuition Fee" twice in the same template.
**System Behavior**: Error message: "Fee Head 'Tuition Fee' already exists in this template."
**How to Handle**: Remove the duplicate entry. If you need two separate charges (e.g., Term 1 Tuition, Term 2 Tuition), ensure you have separate Fee Heads defined in Module 1.1 first.

### Edge Case 3: Deleting an In-Use Template
**What Happens**: Admin tries to delete "Class 10 - Standard" which is assigned to 50 students.
**System Behavior**: "Cannot delete: Template is currently assigned to students."
**How to Handle**: Deactivate the template instead. This prevents future use but keeps history intact.

### Edge Case 4: Changing Fee Head Frequency in Template
**What Happens**: Fee Head "Annual Day" is defined as "Yearly" in Module 1.1, but Admin tries to set it as "Monthly" in the template.
**System Behavior**: System allows this override (flexibility) or restricts it based on strict rules.
**How to Handle**: Generally, the Template setting overrides the default. Ensure this is intentional.

### Edge Case 5: Missing Mandatory Fee Heads
**What Happens**: "Admission Fee" is marked Mandatory in 1.1, but Admin saves a template without it.
**System Behavior**: Error: "Mandatory Fee Head 'Admission Fee' is missing."
**How to Handle**: Add the required fee head to the template.

### Edge Case 6: Assigning Multiple Templates to One Student
**What Happens**: Student is assigned "Class 10 General" AND "Class 10 Special".
**System Behavior**: Risk of double billing. System should alert "Student already has a fee structure assigned."
**How to Handle**: Remove the old assignment before adding the new one, or use "Fee Add-ons" for extras instead of a full second template.

### Edge Case 7: Template Name Conflict
**What Happens**: Naming a new template "Class 1" when one already exists for the same year.
**System Behavior**: Error: "Template name must be unique for the academic year."
**How to Handle**: Use specific names like "Class 1 - A", "Class 1 - General", "Class 1 - Staff Wards".

### Edge Case 8: Currency Precision Issues
**What Happens**: Entering an amount like 100.33333.
**System Behavior**: System rounds to 2 decimal places (100.33).
**How to Handle**: Always input standard currency formats.

### Edge Case 9: Inactive Fee Heads in Template
**What Happens**: Trying to add a Fee Head that was deactivated in Module 1.1.
**System Behavior**: The inactive head won't appear in the dropdown.
**How to Handle**: Go to Module 1.1 and reactivate the fee head first.

### Edge Case 10: Modifying Template After Assignments
**What Happens**: Editing a template that is already linked to students.
**System Behavior**: This usually triggers versioning. The executed assignments (already generated receipts) are NOT auto-updated to prevent financial data corruption.
**How to Handle**: If the change is urgent for *everyone*, you might need to use a "Bulk Update" tool or re-assign the template to refresh the values for unpaid dues.

## Business Rules
- Template names must be unique within an academic year
- Must include at least one fee head
- All mandatory fee heads must be included
- Cannot delete templates assigned to students
- Editing creates new version, old assignments unchanged
- Total amount auto-calculated from fee heads
- Deactivating template prevents new assignments

## Validation Rules
- Template name: Required, 5-150 characters
- Academic year: Required
- Class: Required
- At least one fee head must be added
- Fee amounts must be positive numbers
- Cannot have duplicate fee heads in same template

## Calculation Logic
```
Total Annual Fee = Sum of all fee heads

For Monthly fees:
Annual Amount = Monthly Amount × 12

For Quarterly fees:
Annual Amount = Quarterly Amount × 4

For One-time fees:
Annual Amount = One-time Amount
```

## Permissions Required
- **Create**: Fee Structure Admin, Super Admin
- **Edit**: Fee Structure Admin, Super Admin
- **Duplicate**: Fee Structure Admin, Super Admin
- **Assign**: Fee Structure Admin, Accounts Admin, Super Admin
- **View**: All fee management users

## Related Submodules
- 1.1 Define Fee Heads (source of fee heads)
- 1.3 Student Fee Assignment (uses templates)
- 1.6 Fee Installment Plans (payment schedule)

## API Endpoints
```
POST /api/fee-templates - Create new template
GET /api/fee-templates - List all templates
GET /api/fee-templates/:id - Get specific template
PUT /api/fee-templates/:id - Update template
POST /api/fee-templates/:id/duplicate - Duplicate template
PATCH /api/fee-templates/:id/status - Activate/Deactivate
DELETE /api/fee-templates/:id - Delete (if not assigned)
POST /api/fee-templates/:id/assign - Assign to students
```

## Database Schema
```sql
Table: fee_templates
- id (PK)
- template_name (VARCHAR)
- academic_year_id (FK)
- class_id (FK)
- section_id (FK, nullable)
- stream_id (FK, nullable)
- total_amount (DECIMAL)
- is_active (BOOLEAN)
- created_by (FK to users)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

Table: fee_template_details
- id (PK)
- template_id (FK to fee_templates)
- fee_head_id (FK to fee_heads)
- amount (DECIMAL)
- frequency (ENUM: one-time, monthly, quarterly, yearly)
- created_at (TIMESTAMP)
```

## UI/UX Considerations
- Card-based or table view for templates
- Color coding by class/stream
- Quick preview of fee breakdown on hover
- Drag-and-drop fee heads into template
- Real-time total calculation
- Template comparison feature
- Bulk operations support

## Best Practices
1. Create templates before student enrollment
2. Use clear, descriptive naming (include class, section, stream)
3. Review and update templates annually
4. Test templates with sample calculations
5. Document any special conditions in template notes
6. Maintain template versioning for audit trail
7. Archive old templates instead of deleting

## Example Templates
```
Template: "Class 10 - Science Stream - 2024-25"
Tuition Fee: ₹50,000 (Yearly)
Laboratory Fee: ₹5,000 (Yearly)
Library Fee: ₹2,000 (Yearly)
Examination Fee: ₹3,000 (Yearly)
Sports Fee: ₹1,500 (Yearly)
Total: ₹61,500

Template: "Class 1 - General - 2024-25"
Tuition Fee: ₹25,000 (Yearly)
Activity Fee: ₹2,000 (Yearly)
Library Fee: ₹1,000 (Yearly)
Total: ₹28,000
```
