# Module 1: Fee Structure Setup

## Overview
The Fee Structure Setup module is the foundational component of the entire Fee Management System. It handles all configuration and setup activities that must be completed before the academic year begins. This module defines what fees will be collected, how much will be charged, who will pay what, and when payments are due.

**Core Responsibility**: Establish the complete fee framework for the academic year.

## Purpose
This module serves as the central configuration hub for all fee-related parameters:

- **Define Fee Categories**: Create and manage all types of fees the school will collect (Tuition, Transport, Library, Lab, Sports, etc.)
- **Template Creation**: Build reusable fee structures for different classes, sections, and streams
- **Student Assignment**: Map fee structures to individual students based on their class, section, and special circumstances
- **Concession Management**: Configure scholarship and discount rules with eligibility criteria
- **Optional Fees**: Set up and manage fees for extracurricular activities, hostel, uniform, and other optional services
- **Payment Scheduling**: Define installment plans and payment timelines

## Submodules

### 1.1 Define Fee Heads
**Purpose**: Create and manage fee categories that serve as building blocks for the entire fee structure.

**What It Does**:
- Creates distinct fee categories (e.g., Tuition Fee, Transport Fee, Library Fee, Lab Fee, Sports Fee, Examination Fee)
- Categorizes fees into types (Academic, Transport, Hostel, Extra-curricular, Other)
- Marks fees as mandatory or optional
- Activates/deactivates fee heads as needed

**Key Features**:
- Unlimited fee head creation
- Category-based organization
- Active/inactive status management
- Audit trail for all changes

**Example Use Case**:
A school creates fee heads for "Class 10 Science Lab Fee" (₹5,000), "Annual Sports Fee" (₹1,500), and "Library Membership" (₹2,000). Each fee head can be independently managed and assigned to different student groups.

**[View Detailed Documentation →](submodules/1.1-define-fee-heads/README.md)**

---

### 1.2 Generic Fee Templates
**Purpose**: Create standard fee structures that can be applied to groups of students (by class, section, or stream).

**What It Does**:
- Combines multiple fee heads into a single template
- Sets specific amounts for each fee head
- Defines payment frequency (one-time, monthly, quarterly, yearly)
- Calculates total annual fee automatically
- Allows template duplication for quick creation

**Key Features**:
- Template-based fee management
- Multi-fee head support
- Auto-calculation of totals
- Version control for templates
- Bulk assignment capability

**Example Use Case**:
Create a template "Class 10 - Science Stream - 2024-25" that includes:
- Tuition Fee: ₹50,000 (Yearly)
- Science Lab Fee: ₹5,000 (Yearly)
- Library Fee: ₹2,000 (Yearly)
- Examination Fee: ₹3,000 (Yearly)
- **Total: ₹60,000**

This template can be assigned to all Class 10 Science students in one action.

**[View Detailed Documentation →](submodules/1.2-generic-fee-templates/README.md)**

---

### 1.3 Student-Specific Fee Assignment
**Purpose**: Assign fee structures to individual students and handle special cases requiring custom fee amounts.

**What It Does**:
- Assigns generic templates to students
- Allows individual fee overrides for special cases
- Handles mid-year admissions with pro-rated fees
- Manages fee structure changes for individual students
- Supports bulk assignment operations

**Key Features**:
- Template-based assignment
- Individual overrides
- Pro-rata calculations
- Bulk operations
- Change history tracking

**Example Use Case**:
Most Class 10 students get the standard template (₹60,000), but:
- Student A (scholarship recipient) gets 50% discount on tuition
- Student B (mid-year admission in July) gets pro-rated fees
- Student C (special needs) has additional support fee

**[View Detailed Documentation →](submodules/1.3-student-fee-assignment/README.md)**

---

### 1.4 Concession Configuration
**Purpose**: Define scholarship and discount rules with automated eligibility checking.

**What It Does**:
- Creates concession rules (percentage or fixed amount)
- Defines eligibility criteria (category, income, merit, sibling)
- Applies concessions automatically based on rules
- Manages approval workflows for concessions
- Tracks concession utilization

**Key Features**:
- Rule-based automation
- Multiple eligibility criteria
- Approval workflows
- Capacity limits
- Audit trail

**Example Use Case**:
Configure concession rules:
- **SC/ST Students**: 100% tuition fee waiver (government mandate)
- **Sibling Discount**: 10% on second child, 15% on third child
- **Merit Scholarship**: 50% for students scoring >95% (limited to top 10 students)
- **Income-based**: 25% for family income <₹2 lakhs/year

**[View Detailed Documentation →](submodules/1.4-concession-configuration/README.md)**

---

### 1.5 Optional Fee Setup
**Purpose**: Configure and manage fees for optional services and activities.

**What It Does**:
- Creates optional fee categories (Sports, Music, Art, Hostel, Transport)
- Sets capacity limits for optional activities
- Tracks enrollment in optional programs
- Manages availability by class/section
- Handles waitlists for full programs

**Key Features**:
- Capacity management
- Enrollment tracking
- Class/section restrictions
- Waitlist support
- Real-time availability

**Example Use Case**:
Set up optional fees:
- **School Bus Fee**: ₹12,000/year (Capacity: 50 students per route)
- **Hostel Fee**: ₹80,000/year (Capacity: 100 students)
- **Music Classes**: ₹5,000/year (Capacity: 30 students)
- **Swimming Pool**: ₹8,000/year (Available only for Classes 6-12)

**[View Detailed Documentation →](submodules/1.5-optional-fee-setup/README.md)**

---

### 1.6 Fee Installment Plans
**Purpose**: Define payment schedules and installment options for fee collection.

**What It Does**:
- Creates installment plans (monthly, quarterly, half-yearly, yearly)
- Sets due dates for each installment
- Defines installment percentages or amounts
- Assigns plans to classes or individual students
- Supports multiple plan options

**Key Features**:
- Flexible scheduling
- Percentage or fixed amount installments
- Multiple plan support
- Auto-calculation
- Class-wise assignment

**Example Use Case**:
Create installment plans:

**Plan A - Quarterly** (Default for most students):
- Q1 (April): 30% (₹18,000)
- Q2 (July): 30% (₹18,000)
- Q3 (October): 20% (₹12,000)
- Q4 (January): 20% (₹12,000)

**Plan B - Monthly** (For parents who prefer smaller payments):
- 12 equal installments of ₹5,000 each

**Plan C - Annual** (5% discount for upfront payment):
- Single payment: ₹57,000 (₹3,000 discount)

**[View Detailed Documentation →](submodules/1.6-fee-installment-plans/README.md)**

---

## Complete Workflow

### Phase 1: Setup (Before Academic Year Starts)
```
1. Define Fee Heads
   ↓
2. Create Generic Templates
   ↓
3. Configure Concession Rules
   ↓
4. Set Up Optional Fees
   ↓
5. Define Installment Plans
```

### Phase 2: Assignment (During Student Enrollment)
```
1. Student Enrolls
   ↓
2. System Assigns Appropriate Template (based on class/section/stream)
   ↓
3. Check Concession Eligibility → Apply if eligible
   ↓
4. Add Optional Fees (if requested by parent)
   ↓
5. Assign Installment Plan
   ↓
6. Generate Fee Structure for Student
```

### Phase 3: Maintenance (During Academic Year)
```
- Update fee structures for new requirements
- Modify student assignments for transfers/changes
- Adjust concessions based on new applications
- Handle special cases and exceptions
- Add/remove optional fees as needed
```

## Key Features

### ✅ Flexibility
- Unlimited fee heads and templates
- Customizable for any school structure
- Supports complex fee scenarios

### ✅ Automation
- Template-based assignment reduces manual work
- Rule-based concessions apply automatically
- Auto-calculation of totals and installments

### ✅ Accuracy
- Centralized fee definitions prevent errors
- Version control tracks all changes
- Audit trail for compliance

### ✅ Scalability
- Bulk operations for large student populations
- Template reuse across academic years
- Efficient management of thousands of students

### ✅ Control
- Role-based permissions
- Approval workflows for sensitive operations
- Comprehensive audit logging

## Dependencies

### Required External Systems
- **Student Management Module**: Provides student enrollment data, class/section information
- **Academic Year Configuration**: Defines academic year dates, terms, and schedules
- **User Permissions Module**: Controls who can create/modify fee structures

### Optional Integrations
- **Accounting System**: Sync fee structures with financial records
- **Parent Portal**: Display fee structures to parents
- **Government Reporting**: Export data for regulatory compliance

## Inbound Connections

### Data/Triggers Coming Into This Module

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Student Management Module** | Student enrollment data | Assign fee structures to new students |
| **Academic Year Configuration** | Academic year settings | Set up fee templates for new year |
| **Module 10 (Utilities)** | Bulk import data | Mass fee assignment and updates |
| **Parent Portal** | Optional fee requests | Add optional fees to student accounts |
| **Admission Module** | New admission data | Assign fees to newly admitted students |

## Outbound Connections

### Data/Triggers Going Out From This Module

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **Module 2 (Fine & Penalty)** | Fee structure data, due dates | Calculate fines based on fee amounts and deadlines |
| **Module 3 (Fee Collection)** | Student fee assignments | Determine payment amounts for receipts |
| **Module 6 (Defaulter Management)** | Fee due dates, amounts | Identify students with overdue payments |
| **Module 7 (Reports)** | Fee structure data | Generate fee structure and collection reports |
| **Module 8 (Audit)** | Structure changes | Maintain audit trail of all modifications |
| **Module 9 (Notifications)** | Fee assignments | Send fee structure notifications to parents |
| **Accounting System** | Fee structure data | Sync with financial records |
| **Parent Portal** | Student fee details | Display fee breakdown to parents |

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    EXTERNAL SYSTEMS                          │
│  Student Management │ Academic Year │ Parent Portal          │
└──────────┬──────────┴───────┬───────┴──────────┬────────────┘
           │                  │                   │
           ▼                  ▼                   ▼
┌─────────────────────────────────────────────────────────────┐
│              MODULE 1: FEE STRUCTURE SETUP                   │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Fee Heads│→ │Templates │→ │Assignment│→ │Concession│   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│       ↓             ↓              ↓             ↓          │
│  ┌──────────┐  ┌──────────┐                                │
│  │Optional  │  │Installment│                                │
│  │  Fees    │  │  Plans   │                                │
│  └──────────┘  └──────────┘                                │
└──────────┬──────────┬──────────┬──────────┬────────────────┘
           │          │          │          │
           ▼          ▼          ▼          ▼
┌──────────────────────────────────────────────────────────────┐
│                    INTERNAL MODULES                           │
│  Module 2  │  Module 3  │  Module 6  │  Module 7  │ Module 8 │
│  (Fine)    │(Collection)│(Defaulter) │ (Reports)  │ (Audit)  │
└──────────────────────────────────────────────────────────────┘
```

## Related Modules

### Directly Connected
- **Module 2: Fine & Penalty Management** - Uses fee amounts and due dates to calculate fines
- **Module 3: Fee Collection & Receipts** - Uses fee assignments to process payments
- **Module 6: Defaulter & Dues Management** - Uses fee due dates to identify defaulters

### Indirectly Connected
- **Module 7: Fee Reports & Analytics** - Generates reports based on fee structure data
- **Module 8: Audit & Compliance** - Tracks all fee structure changes
- **Module 9: Notifications** - Sends fee-related notifications to parents
- **Module 10: Utilities** - Provides bulk operations and data management

## Best Practices

### 1. Setup Timing
- Complete fee structure setup at least 2 weeks before academic year starts
- Test with sample students before mass assignment
- Review and approve all templates before activation

### 2. Template Design
- Create templates for each class-section-stream combination
- Use clear, descriptive names (e.g., "Class-10-Science-2024-25")
- Document any special conditions in template notes

### 3. Concession Management
- Define clear eligibility criteria
- Set up approval workflows for manual concessions
- Monitor concession utilization against budget

### 4. Data Quality
- Validate all fee amounts before assignment
- Cross-check totals with previous year (with inflation adjustments)
- Ensure all mandatory fees are included in templates

### 5. Change Management
- Never modify assigned fee structures mid-year unless absolutely necessary
- Document all changes with reasons
- Communicate changes to affected parents immediately

### 6. Audit Trail
- Review audit logs regularly
- Investigate any unauthorized changes
- Maintain version history for all templates

## Common Scenarios

### Scenario 1: New Academic Year Setup
1. Duplicate previous year's fee heads (if similar)
2. Adjust amounts for inflation/new requirements
3. Create new templates for each class
4. Configure concession rules
5. Set up optional fees with capacity limits
6. Define installment plans
7. Test with sample students
8. Bulk assign to all enrolled students

### Scenario 2: Mid-Year Admission
1. Identify appropriate fee template for student's class
2. Calculate pro-rated fees based on admission date
3. Check concession eligibility
4. Add optional fees if requested
5. Assign modified installment plan
6. Generate fee structure and notify parent

### Scenario 3: Fee Structure Change
1. Create new version of template
2. Document reason for change
3. Get approval from authorized personnel
4. Apply to affected students
5. Generate notifications
6. Update accounting system

## Security & Permissions

### Role-Based Access Control

| Role | Permissions |
|------|------------|
| **Super Admin** | Full access to all operations |
| **Fee Structure Admin** | Create/edit fee heads, templates, concessions |
| **Accounts Admin** | View all, assign fees to students |
| **Class Teacher** | View assigned students' fee structures |
| **Parent** | View own child's fee structure only |

### Critical Operations Requiring Approval
- Deleting fee heads in use
- Modifying assigned fee structures mid-year
- Granting concessions above certain threshold
- Changing fee amounts after assignment

## Performance Considerations

### Optimization Tips
- Use bulk assignment for large student populations
- Cache frequently accessed templates
- Index student-fee assignments for quick lookup
- Archive old academic year data

### Scalability
- Supports 10,000+ students per academic year
- Handles 100+ fee heads
- Manages 50+ templates simultaneously
- Processes bulk assignments in background jobs

## Troubleshooting

### Common Issues

**Issue**: Student not showing correct fee amount
- **Solution**: Check template assignment, verify concessions applied, review individual overrides

**Issue**: Total fee doesn't match expected amount
- **Solution**: Verify all fee heads in template, check for hidden concessions, review optional fees

**Issue**: Cannot delete fee head
- **Solution**: Fee head is in use by templates or students, deactivate instead of delete

**Issue**: Concession not applying automatically
- **Solution**: Check eligibility criteria, verify student data matches criteria, review concession capacity limits
