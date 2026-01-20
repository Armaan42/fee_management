# 1.1 Define Fee Heads

## Overview

Think of fee heads as labels or categories for different types of money the school collects from students. Just like a grocery store has different categories (vegetables, dairy, snacks), a school has different fee categories (tuition, transport, library). This module lets you create and manage these categories.

**In simple terms**: Before you can charge students any fees, you need to tell the system what types of fees exist. That's what this module does - it's like creating a menu of all possible fees your school might charge.

**Real-world analogy**: Imagine you're setting up a restaurant menu. Before you can create combo meals or take orders, you first need to list all the individual items (burger, fries, drink). Fee heads are those individual items in your school's "fee menu."

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

## Real-World Scenarios

### Scenario 1: Setting Up Fee Heads for New Academic Year

**Background**: St. Mary's School is starting a new academic year and needs to set up all fee categories.

**Steps**:
1. Principal reviews last year's fee structure
2. Identifies fees to continue: Tuition, Transport, Library, Lab, Sports
3. Identifies new fees to add: Computer Lab Fee (new computer lab built)
4. Admin logs into system
5. Creates each fee head one by one:
   - Name: "Tuition Fee", Category: Academic, Mandatory: Yes
   - Name: "Transport Fee", Category: Transport, Mandatory: No
   - Name: "Library Fee", Category: Academic, Mandatory: Yes
   - Name: "Science Lab Fee", Category: Academic, Mandatory: Yes
   - Name: "Computer Lab Fee", Category: Academic, Mandatory: Yes (NEW)
   - Name: "Sports Fee", Category: Extra-curricular, Mandatory: No

**Result**: All fee heads created and ready to be used in fee templates.

**Time Taken**: 15-20 minutes for 10-15 fee heads

---

### Scenario 2: Handling Mid-Year Fee Changes

**Background**: School decides to introduce a new "Online Learning Platform Fee" mid-year due to pandemic requirements.

**Steps**:
1. Admin creates new fee head:
   - Name: "Online Learning Platform Fee"
   - Category: Academic
   - Mandatory: Yes
   - Description: "Access to online learning platform for remote classes"
2. Fee head is created but NOT yet assigned to students
3. Admin creates new fee template including this fee
4. Admin assigns new template only to new admissions
5. For existing students, admin manually adds this fee to their accounts

**Result**: New fee head created and selectively applied without disrupting existing student fee structures.

**Important Note**: Creating a fee head doesn't automatically charge students - it just makes it available for use.

---

### Scenario 3: Discontinuing an Old Fee

**Background**: School no longer offers hostel facility, needs to stop using "Hostel Fee" head.

**Steps**:
1. Admin searches for "Hostel Fee" in fee heads list
2. Checks how many students currently have this fee assigned (finds 0 students)
3. Since no students are assigned, admin can either:
   - **Option A**: Delete the fee head completely
   - **Option B**: Deactivate it (keeps historical records)
4. Admin chooses Option B (deactivate) for audit purposes
5. Toggles "Is Active" to OFF
6. Fee head no longer appears in dropdown for new assignments
7. Historical data remains intact

**Result**: Fee head preserved for historical records but unavailable for future use.

**Best Practice**: Always deactivate instead of delete to maintain audit trail.

---

### Scenario 4: Fixing a Typo in Fee Head Name

**Background**: Admin created "Tution Fee" instead of "Tuition Fee" (typo) and it's already assigned to 500 students.

**Steps**:
1. Admin realizes the typo
2. Checks if fee head is in use (finds 500 students)
3. **Cannot delete** because it's in use
4. Admin edits the fee head name:
   - Changes "Tution Fee" to "Tuition Fee"
   - Saves changes
5. System updates the name everywhere
6. All 500 student records now show "Tuition Fee"

**Result**: Typo fixed without disrupting existing assignments.

**Important**: Name changes reflect everywhere immediately, including historical records.

---

### Scenario 5: Creating Class-Specific Fee Heads

**Background**: School wants different lab fees for different science streams.

**Steps**:
1. Admin creates specific fee heads:
   - "Physics Lab Fee" (for Physics students)
   - "Chemistry Lab Fee" (for Chemistry students)
   - "Biology Lab Fee" (for Biology students)
   - "General Science Lab Fee" (for junior classes)
2. Each marked as Category: Academic, Mandatory: Yes
3. Later, when creating templates:
   - Class 11 Physics template includes "Physics Lab Fee"
   - Class 11 Chemistry template includes "Chemistry Lab Fee"
   - Class 11 Biology template includes "Biology Lab Fee"

**Result**: Granular control over which students pay which lab fees.

**Tip**: Create specific fee heads when different student groups need different charges.

## Edge Cases & How to Handle Them

### Edge Case 1: Duplicate Fee Head Names

**What Happens**: Admin tries to create "Library Fee" but it already exists.

**System Behavior**: System shows error: "Fee head with this name already exists"

**How to Handle**:
- Check existing fee heads first
- If you need a similar fee, use descriptive names: "Library Fee - Annual" vs "Library Fee - Semester"
- Or use the existing fee head if it serves the same purpose

**Prevention**: Always search before creating new fee heads

---

### Edge Case 2: Deleting Fee Head Assigned to 1000+ Students

**What Happens**: Admin tries to delete "Tuition Fee" which is assigned to all 1000 students.

**System Behavior**: System blocks deletion with message: "Cannot delete fee head. It is assigned to 1000 students."

**How to Handle**:
- You CANNOT delete fee heads in use
- Options:
  1. Deactivate it instead (recommended)
  2. Remove it from all students first (not recommended, very risky)
  3. Keep it as-is if still needed

**Prevention**: Plan fee heads carefully before assigning to students

---

### Edge Case 3: Fee Head Name Too Long

**What Happens**: Admin enters "Annual Tuition Fee for Academic Year 2024-2025 Including All Charges and Taxes" (80+ characters)

**System Behavior**: System truncates or shows error: "Fee head name must be 100 characters or less"

**How to Handle**:
- Use concise names: "Annual Tuition Fee 2024-25"
- Put detailed information in Description field instead
- Keep names short for better display in reports

**Prevention**: Use abbreviations and put details in description

---

### Edge Case 4: Changing Mandatory to Optional Mid-Year

**What Happens**: Admin changes "Examination Fee" from Mandatory to Optional after 500 students already have it assigned.

**System Behavior**: 
- Change is saved successfully
- Existing assignments remain unchanged
- New assignments treat it as optional

**How to Handle**:
- Understand that existing students keep the fee
- Only new assignments will treat it as optional
- If you want to remove from existing students, do it manually

**Prevention**: Decide mandatory/optional status carefully before assigning

---

### Edge Case 5: Deactivating Fee Head in Active Use

**What Happens**: Admin deactivates "Transport Fee" while 200 students currently have it assigned.

**System Behavior**:
- Fee head is deactivated successfully
- Existing 200 students keep the fee in their accounts
- Fee head disappears from dropdown for new assignments
- Cannot be added to new students

**How to Handle**:
- This is normal and expected behavior
- Existing students are not affected
- New students cannot be assigned this fee
- Reactivate if needed later

**Prevention**: Only deactivate when you're sure you don't need it for new students

---

### Edge Case 6: Multiple Admins Creating Same Fee Head Simultaneously

**What Happens**: Two admins try to create "Sports Fee" at the exact same time.

**System Behavior**:
- First one to save succeeds
- Second one gets error: "Fee head already exists"

**How to Handle**:
- Second admin should use the existing fee head
- Check if the existing one meets requirements
- If different, use descriptive name: "Sports Fee - Annual" vs "Sports Fee - Monthly"

**Prevention**: Coordinate with other admins, assign fee head creation to one person

---

### Edge Case 7: Special Characters in Fee Head Name

**What Happens**: Admin tries to create fee head with name "Lab Fee (Science)" or "Transport Fee - Route #5"

**System Behavior**:
- Parentheses and hyphens usually allowed
- Special characters like #, $, %, @ may be blocked
- System shows: "Only letters, numbers, spaces, hyphens, and parentheses allowed"

**How to Handle**:
- Use allowed characters only
- Replace # with "No." or "Route 5"
- Replace & with "and"

**Prevention**: Stick to simple alphanumeric names

---

### Edge Case 8: Creating 100+ Fee Heads

**What Happens**: Large school creates 150 different fee heads for various purposes.

**System Behavior**:
- System allows creation
- Dropdown lists become very long
- Difficult to find specific fee heads
- Reports become cluttered

**How to Handle**:
- Use search/filter functionality
- Group similar fees under one head when possible
- Use categories effectively
- Consider if you really need that many distinct fee heads

**Prevention**: Keep fee heads to essential categories only (typically 15-30 is sufficient)

---

### Edge Case 9: Renaming Fee Head After Reports Generated

**What Happens**: Admin renames "Tution Fee" to "Tuition Fee" after annual reports were generated.

**System Behavior**:
- Name changes everywhere, including historical data
- Old reports now show new name
- Audit trail shows the change

**How to Handle**:
- This is usually fine for typo corrections
- For major changes, consider creating new fee head instead
- Export old reports before renaming if needed

**Prevention**: Double-check names before using in production

---

### Edge Case 10: Accidentally Deactivating Wrong Fee Head

**What Happens**: Admin meant to deactivate "Old Library Fee" but deactivated "Library Fee" instead.

**System Behavior**:
- "Library Fee" becomes inactive
- Cannot be assigned to new students
- Existing students keep it

**How to Handle**:
- Immediately reactivate the correct fee head
- Deactivate the intended one
- Check if any new students were affected in the meantime

**Prevention**: Always confirm fee head name before deactivating

---

### Edge Case 11: Fee Head with No Category Selected

**What Happens**: Admin forgets to select category and tries to save.

**System Behavior**: System shows error: "Category is required"

**How to Handle**:
- Select appropriate category from dropdown
- If unsure, use "Other" category
- Can change category later if needed

**Prevention**: Make category a required field (already is)

---

### Edge Case 12: Bulk Import of Fee Heads with Duplicates

**What Happens**: Admin imports Excel file with 50 fee heads, 5 of which already exist.

**System Behavior**:
- System imports 45 new fee heads
- Skips 5 duplicates
- Shows report: "45 created, 5 skipped (duplicates)"

**How to Handle**:
- Review the skipped items
- Verify they are true duplicates
- Manually handle any that need different treatment

**Prevention**: Clean data before import, check for existing fee heads

---

### Edge Case 13: Fee Head Description Exceeds Limit

**What Happens**: Admin writes 1000-word description in description field (limit is 500 characters).

**System Behavior**: System truncates or shows error: "Description must be 500 characters or less"

**How to Handle**:
- Summarize the description
- Keep essential information only
- Use external documentation for detailed explanations

**Prevention**: Keep descriptions concise and to-the-point

---

### Edge Case 14: Reactivating Old Fee Head

**What Happens**: School reintroduces hostel facility after 2 years, wants to reactivate "Hostel Fee" head.

**System Behavior**:
- Admin finds deactivated "Hostel Fee"
- Toggles "Is Active" to ON
- Fee head becomes available again
- All old configuration (category, mandatory status) remains

**How to Handle**:
- Reactivate the old fee head
- Verify all settings are still appropriate
- Update description if needed
- Start assigning to students

**Prevention**: Keep deactivated fee heads for potential future use

---

### Edge Case 15: Fee Head Created by User Who Left Organization

**What Happens**: Fee head "Annual Maintenance Fee" was created by admin who resigned 2 years ago.

**System Behavior**:
- Fee head remains active and functional
- Created by field shows ex-employee name
- Current admins can still edit/manage it

**How to Handle**:
- No action needed, fee head works normally
- Can be edited by current admins
- Creator information is just for audit trail

**Prevention**: None needed, this is expected behavior

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

## Inbound Connections

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Admin User** | Manual creation | Create new fee heads |
| **Module 10.5 (Data Import)** | Bulk import | Import multiple fee heads from Excel |
| **Academic Planning** | New academic year | Define new fees for upcoming year |

## Outbound Connections

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **Module 1.2 (Fee Templates)** | Fee head list | Use in template creation |
| **Module 1.3 (Student Assignment)** | Fee head data | Assign fees to students |
| **Module 1.4 (Concessions)** | Fee head list | Apply concessions to specific fees |
| **Module 3 (Fee Collection)** | Fee head names | Display on receipts |
| **Module 7 (Reports)** | Fee head data | Generate fee-wise reports |

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
7. Always deactivate instead of delete to preserve audit trail
8. Test fee heads with sample data before assigning to all students
9. Keep fee head names short for better display in reports
10. Coordinate with other admins to avoid duplicate creation
