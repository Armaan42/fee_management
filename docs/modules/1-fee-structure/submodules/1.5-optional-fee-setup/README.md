# 1.5 Optional Fee Setup

## Overview
**Optional Fee Setup** handles fees that a student *can choose* to pay, rather than fees that are compulsory for everyone. These are typically for facilities or activities that not every student uses, such as School Transport, Hostel, Canteen Meal Plans, or Hobby Clubs.

**In simple terms**: It’s like an "À la carte" menu compared to the "Set Menu" (Standard Fees). The parents tick a box to "Opt-in", and only then is the fee charged.

**Comparison**:
-   **Standard Fee**: Tuition Fee (Everyone pays).
-   **Optional Fee**: Bus Fee (Only bus users pay).

## Purpose
To manage fees for value-added services and facilities that are selected on a voluntary basis by students/parents.

## Description
This submodule allows administrators to define fees that require an explicit "subscription" or "enrollment". It manages the lifecycle of these subscriptions: Opt-in -> Billing -> Renewal -> Opt-out. It ensures that students are not billed for services they don't use.

## Key Features
-   **Subscription Management**: Enroll students into optional services.
-   **Seat Limits**: Define maximum capacity (e.g., only 40 seats in the Guitar Class).
-   **Pro-rata Billing**: Handle charges when a student joins the facility mid-month.
-   **Transport Routes**: Link fees to specific bus routes/stops.
-   **Hostel Allocation**: separate fees for different room types (AC vs Non-AC).

## Real-World Scenarios

### Scenario 1: School Bus Service
**Background**: 30% of students use the school bus. The fee depends on the distance (Zone).
**Steps**:
1.  Parent requests Bus Service for their child.
2.  Admin selects **Optional Fee -> Transport**.
3.  Selects Route: "Route 5 - Model Town".
4.  System confirms fee: "₹1,500 per month".
5.  Admin clicks **Enroll**.
**Result**: The monthly transport fee is added to the student's bill every month until they opt out.

### Scenario 2: Annual Picnic (One-time Event)
**Background**: The school organizes a trip to the Science Museum. Cost is ₹500. Participation is voluntary.
**Steps**:
1.  Admin creates Optional Fee: "Science Museum Trip".
2.  Teachers collect consent forms.
3.  Admin bulk-selects the 40 participating students.
4.  Assigns the fee.
**Result**: Only those 40 students are billed.

### Scenario 3: Hostel Room Allocation
**Background**: A student moves from a Day Scholar to a Hosteller.
**Steps**:
1.  Admin enrolls student in "Hostel Facility".
2.  Selects Room Type: "4-Bed Non-AC".
3.  System adds "Hostel Fee" and "Mess Fee" to the ledger.
4.  Removes "Transport Fee" (since they live on campus now).
**Result**: Fee structure flips from Transport-based to Hostel-based.

### Scenario 4: Olympiad Exam Registration
**Background**: External Math Olympiad. ₹200 fee.
**Steps**:
1.  Admin sets up "Math Olympiad Fee".
2.  Open enrollment for 2 weeks.
3.  Parents pay via the app/portal.
4.  System auto-assigns the fee upon payment.
**Result**: Self-service enrollment reducing admin work.

### Scenario 5: Swimming Class (Seasonal)
**Background**: Swimming is open only for Summer (April-June).
**Steps**:
1.  Admin sets "Swimming Fee" as active for Apr/May/Jun only.
2.  Enrolls interested students.
3.  System bills them used months.
4.  Auto-stops billing in July.

## Edge Cases & How to Handle Them

### Edge Case 1: Mid-Month Opt-in
**What Happens**: Student joins the Bus service on the 20th of the month.
**System Behavior**: 
-   **Option A**: Full month charge.
-   **Option B**: Pro-rata charge (10 days only).
**How to Handle**: Configure the "Pro-rata Rule" in settings. usually, transport is full month, but hostel might be pro-rata.

### Edge Case 2: Opting Out After Bill Generation
**What Happens**: Bill generated on 1st. Student stops using bus on 2nd.
**System Behavior**: The bill still includes the Bus Fee.
**How to Handle**: Admin must manually "Credit Note" / "Reverse" the charge for that month if the policy allows refund.

### Edge Case 3: Capacity Overflow
**What Happens**: 50 students want "Robotics Club", but room holds 20.
**System Behavior**: System should block the 21st enrollment with "Seats Full".
**How to Handle**: Maintain a Waitlist or open a second batch.

### Edge Case 4: Dependency Missing
**What Happens**: Student wants "Horse Riding" but hasn't paid "Sports Insurance".
**System Behavior**: System warns: "Prerequisite 'Sports Insurance' missing."
**How to Handle**: Enroll in Insurance first, then Horse Riding.

### Edge Case 5: Conflicting Options
**What Happens**: Student tries to enroll in "Bus Route A" AND "Bus Route B".
**System Behavior**: Physically impossible. System should enforce "One Route Only".
**How to Handle**: The new enrollment should automatically cancel/replace the old one.

### Edge Case 6: Fee Hike for Existing Subscribers
**What Happens**: Bus fee increases from ₹1000 to ₹1200 mid-session.
**System Behavior**: The change should reflect in the *next* billing cycle for all existing users.
**How to Handle**: Update the Fee Head master. Ensure it doesn't retroactively change already paid receipts.

### Edge Case 7: Student Leave
**What Happens**: Student goes on leave for 2 months. Parents ask for Transport fee waiver.
**System Behavior**: System continues billing unless paused.
**How to Handle**: Admin uses "Pause Subscription" feature for those 2 months.

### Edge Case 8: Graduating Class
**What Happens**: Class 12 leaves in March. Bus fee assignments need to stop.
**System Behavior**: Bulk de-allocation needed.
**How to Handle**: System usually auto-stops based on "Academic Year End", but manual check is good.

### Edge Case 9: Inventory Check
**What Happens**: 100 students buy "Geometry Box" (Inventory item linked to fee). Store has 90.
**System Behavior**: System should track count.
**How to Handle**: Prevent billing if stock is zero.

### Edge Case 10: Late Joining Fine
**What Happens**: Student joins "Annual Concert" practice late.
**System Behavior**: Same fee or reduced?
**How to Handle**: Usually flat fee applies regardless of joining date for events.

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Facility Name | Text | Yes | "Bus Route 1", "Hostel Block A" |
| Fee Head | Dropdown | Yes | Link to the monetary charge |
| Billing Frequency | Dropdown | Yes | Monthly/Quarterly/One-time |
| Capacity | Number | No | Max seats available |
| Current Count | Calculation | Yes | Number of students enrolled |
| Start Date | Date | Yes | When billing starts |
| End Date | Date | No | When billing ends (optional) |

## User Actions
1.  **Define Facility**: Create the service (Bus Route, Club).
2.  **Enroll Student**: Add student to the list.
3.  **Process Billing**: Generate demands based on active list.
4.  **De-allocate**: Remove student (Opt-out).

## Business Rules
-   Opt-out usually requires Notice Period (e.g., 1 month).
-   Transport fees are often charged for 11 months (excluding June vacation) or 12 months depending on policy.
-   Hostel fees are strictly advance payment.

## Permissions Required
-   **Manage Facilities**: Transport Admin, Hostel Warden.
-   **Enroll/Bill**: Fee Admin.

## Related Submodules
-   **1.1 Define Fee Heads**: Creating the charge types.
-   **2.1 Transport Module**: detailed route management.
-   **2.2 Hostel Module**: Detailed room management.

## API Endpoints
```
POST /api/optional-facilities - Create new facility
GET /api/optional-facilities - List all
POST /api/students/:id/enroll - Subscribe student to facility
DELETE /api/students/:id/enroll - Unsubscribe
GET /api/reports/facility-utilization - Utilization stats
```

## Database Schema
```sql
Table: optional_facilities
- id (PK)
- name (VARCHAR)
- fee_head_id (FK)
- max_capacity (INT)

Table: student_facility_enrollments
- id (PK)
- student_id (FK)
- facility_id (FK)
- start_date (DATE)
- end_date (DATE)
- status (ENUM: Active, Paused, Ended)
```

## UI/UX Considerations
-   **Drag-and-Drop**: Move students into "Bus 5" list.
-   **Map View**: For transport, showing stops visually.
-   **Waitlist Indicator**: Show "5 Waiting" if capacity full.

## Best Practices
1.  **Clear Policies**: Make sure parents sign an "Opt-in Form" to avoid disputes.
2.  **Regular Reconciliation**: Check if number of students on the bus matches the billing list.
3.  **Advance Billing**: Charge optional fees in advance to prevent loss if student quits mid-month.
