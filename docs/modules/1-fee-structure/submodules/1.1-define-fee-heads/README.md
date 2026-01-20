# 1.1 Define Fee Heads

## Purpose
Create and manage fee categories that will be used throughout the school. Fee heads are the building blocks of the entire fee structure.

## Description
This submodule allows administrators to define all types of fees that the school collects. Each fee head represents a distinct category of charges.

## Key Features
- Create new fee heads with detailed descriptions
- Categorize fees (Academic, Transport, Hostel, Extra-curricular, Other)
- Mark fees as mandatory or optional
- Activate/deactivate fee heads
- Track creation and modification history

## Common Fee Heads Examples
- **Academic Fees**
- Tuition Fee
- Admission Fee
- Registration Fee
- Examination Fee
- Library Fee
- Laboratory Fee
- Computer Lab Fee
- Activity Fee

- **Transport Fees**
- Bus Fee
- Van Fee
- Transport Maintenance

- **Hostel Fees**
- Hostel Accommodation
- Hostel Mess Fee
- Hostel Security Deposit

- **Extra-curricular Fees**
- Sports Fee
- Music Fee
- Art & Craft Fee
- Dance Fee

- **Other Fees**
- Uniform Fee
- Books & Stationery
- ID Card Fee
- Medical Fee
- Insurance Fee

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Fee Head Name | Text | Yes | Name of the fee category |
| Description | Text | No | Detailed description |
| Category | Dropdown | Yes | Academic/Transport/Hostel/Extra-curricular/Other |
| Is Mandatory | Checkbox | Yes | Whether this fee is compulsory |
| Is Active | Checkbox | Yes | Whether this fee head is currently in use |
| Created Date | Auto | Yes | When the fee head was created |
| Modified Date | Auto | Yes | Last modification timestamp |

## User Actions
1. **Add Fee Head**
- Click "+ Add Fee Head" button
- Fill in fee head details
- Select category
- Mark as mandatory/optional
- Save

2. **Edit Fee Head**
- Select existing fee head
- Modify details
- Save changes
- System logs modification history

3. **Deactivate Fee Head**
- Select fee head
- Toggle "Is Active" status
- Confirm action
- Fee head becomes unavailable for new assignments

4. **View Fee Heads**
- View all fee heads in table format
- Filter by category
- Search by name
- Sort by various fields

## Business Rules
- Fee head names must be unique
- Cannot delete fee heads that are already assigned to students
- Can only deactivate (not delete) fee heads in use
- Deactivated fee heads remain in historical records
- Mandatory fees cannot be removed from templates
- Editing fee head name affects all future assignments only

## Validation Rules
- Fee head name: Required, 3-100 characters
- Description: Optional, max 500 characters
- Category: Required, must select from predefined list
- Duplicate names not allowed

## Permissions Required
- **Create**: Fee Structure Admin, Super Admin
- **Edit**: Fee Structure Admin, Super Admin
- **Deactivate**: Fee Structure Admin, Super Admin
- **View**: All fee management users

## Related Submodules
- 1.2 Generic Fee Templates (uses fee heads)
- 1.3 Student Fee Assignment (uses fee heads)
- 1.4 Concession Configuration (applies to fee heads)

## API Endpoints
```
POST /api/fee-heads - Create new fee head
GET /api/fee-heads - List all fee heads
GET /api/fee-heads/:id - Get specific fee head
PUT /api/fee-heads/:id - Update fee head
PATCH /api/fee-heads/:id/status - Activate/Deactivate
DELETE /api/fee-heads/:id - Delete (if not in use)
```

## Database Schema
```sql
Table: fee_heads
- id (PK)
- name (VARCHAR, UNIQUE)
- description (TEXT)
- category (ENUM)
- is_mandatory (BOOLEAN)
- is_active (BOOLEAN)
- created_by (FK to users)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

## UI/UX Considerations
- Display fee heads in a sortable, filterable table
- Use color coding for categories
- Show active/inactive status with badges
- Provide quick search functionality
- Bulk actions for multiple fee heads
- Confirmation dialogs for critical actions

## Best Practices
1. Create all fee heads at the beginning of the academic year
2. Use clear, descriptive names
3. Group related fees under appropriate categories
4. Review and clean up unused fee heads annually
5. Document any special fee heads in the description field
6. Maintain consistency in naming conventions
