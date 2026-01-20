# 1.2 Generic Fee Templates

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
