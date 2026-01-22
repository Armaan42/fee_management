# User Flows: Fee Structure Setup (UI/UX Perspective)

## Introduction

This document visualizes the **user interface journey** through the Fee Structure Setup module from a UI/UX design perspective. This module handles all configuration activities that must be completed before the academic year begins, defining what fees will be collected, how much will be charged, and when payments are due.

Each flowchart focuses on:
- **Screen states** and visual feedback
- **User actions** and decision points
- **Navigation paths** between interfaces
- **Error handling** and recovery flows

---

## Flow 1: Define Fee Head

### User Story
*"As a Fee Structure Admin, I want to create a new fee category (fee head) so that I can include it in fee templates for students."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin Logs In]) --> Dashboard[Dashboard Screen]
    
    Dashboard --> ClickFee[Click 'Fee Management' in Sidebar]
    ClickFee --> FeeModule[Fee Management Landing Page<br/>Shows: Fee Heads, Templates, Assignments]
    
    FeeModule --> ClickHeads[Click 'Fee Heads' Tab]
    ClickHeads --> HeadsList[Fee Heads List Screen<br/>Table showing existing fee heads]
    
    HeadsList --> ClickNew[Click 'Create New Fee Head' Button<br/>Blue button, top-right]
    ClickNew --> FormModal[Modal Dialog Opens:<br/>'Create Fee Head']
    
    FormModal --> ShowForm[Form Fields:<br/>- Fee Head Name (required)<br/>- Category dropdown<br/>- Amount (optional default)<br/>- Mandatory/Optional toggle<br/>- Description textarea]
    
    ShowForm --> FillName[Enter Name: 'Science Lab Fee']
    FillName --> SelectCategory[Select Category: 'Academic']
    SelectCategory --> EnterAmount[Enter Default Amount: 5000]
    EnterAmount --> ToggleMandatory[Toggle: Mandatory]
    ToggleMandatory --> EnterDesc[Enter Description:<br/>'Annual fee for science lab equipment']
    
    EnterDesc --> ValidateForm{Real-time Validation}
    
    ValidateForm -->|Invalid| ShowErrors[Show Inline Errors:<br/>- Red border on invalid fields<br/>- Error message below field]
    ShowErrors --> ShowForm
    
    ValidateForm -->|Valid| EnableSave[Save Button Enabled<br/>Changes from gray to blue]
    
    EnableSave --> ClickSave[Click 'Save' Button]
    ClickSave --> LoadingState[Loading Spinner on Button<br/>'Saving...']
    
    LoadingState --> CheckDuplicate{System Checks:<br/>Duplicate Name?}
    
    CheckDuplicate -->|Duplicate Found| DuplicateError[Error Toast:<br/>'Fee head with this name already exists'<br/>Red banner, auto-dismiss 5s]
    DuplicateError --> FormModal
    
    CheckDuplicate -->|No Duplicate| SaveSuccess[Success Animation:<br/>Green checkmark]
    
    SaveSuccess --> SuccessToast[Success Toast:<br/>'Science Lab Fee created successfully'<br/>Green banner at top]
    
    SuccessToast --> ModalClose[Modal Closes Automatically]
    ModalClose --> UpdatedList[Fee Heads List Updates:<br/>- New item appears at top<br/>- Highlight animation (fade in)<br/>- Green 'Active' badge]
    
    UpdatedList --> UserChoice{User Action}
    
    UserChoice -->|Create Another| ClickNew
    UserChoice -->|Edit New Item| ClickEdit[Click Edit Icon on New Item]
    ClickEdit --> EditModal[Edit Modal Opens<br/>Pre-filled with saved data]
    
    UserChoice -->|Continue| End([User Continues Work])
    
    style FormModal fill:#e3f2fd
    style SuccessToast fill:#c8e6c9
    style DuplicateError fill:#ffcdd2
    style LoadingState fill:#fff9c4
```

### Screen States

**1. Fee Heads List (Empty State)**
- Illustration: "No fee heads created yet"
- Message: "Create your first fee head to get started"
- Large "Create Fee Head" button centered

**2. Fee Heads List (Loaded State)**
- Table with columns: Name, Category, Default Amount, Type, Status, Actions
- Search bar at top
- Filter by category dropdown
- Sort by name/category/amount

**3. Create Modal (Empty State)**
- All fields blank with placeholder text
- Save button disabled (grayed out)
- Category dropdown shows all options
- Mandatory toggle defaults to OFF

**4. Create Modal (Filled State)**
- Fields populated with data
- Real-time validation (green checkmarks)
- Character count for description (max 500)
- Save button enabled (blue)

**5. Create Modal (Error State)**
- Invalid fields highlighted in red
- Error messages below fields
- Save button disabled
- Focus automatically on first error field

---

## Flow 2: Create Generic Fee Template

### User Story
*"As a Fee Structure Admin, I want to create a fee template for Class 10 Science students so that I can assign it to all students in that group at once."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Fee Management Page]) --> ClickTemplates[Click 'Templates' Tab]
    ClickTemplates --> TemplateList[Fee Templates List Screen<br/>Shows existing templates by class]
    
    TemplateList --> ClickNew[Click 'Create New Template' Button]
    ClickNew --> TemplateForm[Template Creation Screen<br/>Multi-step wizard]
    
    TemplateForm --> Step1[Step 1: Basic Information<br/>Progress: 1 of 3]
    
    Step1 --> FillBasic[Fill Fields:<br/>- Template Name: 'Class 10 Science 2024-25'<br/>- Academic Year: 2024-25<br/>- Class: 10<br/>- Section: All<br/>- Stream: Science]
    
    FillBasic --> ValidateStep1{Validate Step 1}
    
    ValidateStep1 -->|Invalid| ShowStep1Errors[Show Errors:<br/>Required fields highlighted]
    ShowStep1Errors --> Step1
    
    ValidateStep1 -->|Valid| ClickNext1[Click 'Next' Button]
    ClickNext1 --> Step2[Step 2: Add Fee Heads<br/>Progress: 2 of 3]
    
    Step2 --> ShowAvailable[Left Panel: Available Fee Heads<br/>- Searchable list<br/>- Grouped by category<br/>Right Panel: Selected Fee Heads<br/>- Empty initially]
    
    ShowAvailable --> SearchFee[Search: 'Tuition']
    SearchFee --> FilteredList[List Filters to Show:<br/>- Tuition Fee<br/>- Tuition Fee (Hostel)]
    
    FilteredList --> SelectTuition[Click on 'Tuition Fee'<br/>Item highlights]
    SelectTuition --> ClickAdd[Click 'Add' Button or Drag to Right]
    
    ClickAdd --> MoveToSelected[Item Moves to Right Panel<br/>Slide animation]
    
    MoveToSelected --> EnterAmount[Amount Input Field Appears:<br/>Enter: 50000]
    EnterAmount --> AddMore[Add More Fee Heads:<br/>- Science Lab Fee: 5000<br/>- Library Fee: 2000<br/>- Examination Fee: 3000]
    
    AddMore --> ShowTotal[Total Calculation (Auto):<br/>Bottom of right panel<br/>Total: ₹60,000<br/>Large, bold text]
    
    ShowTotal --> ValidateStep2{Validate Step 2:<br/>At least 1 fee head?}
    
    ValidateStep2 -->|No Fee Heads| ShowStep2Error[Warning Message:<br/>'Add at least one fee head']
    ShowStep2Error --> Step2
    
    ValidateStep2 -->|Has Fee Heads| ClickNext2[Click 'Next' Button]
    ClickNext2 --> Step3[Step 3: Review & Confirm<br/>Progress: 3 of 3]
    
    Step3 --> ShowSummary[Summary Card:<br/>- Template name<br/>- Class/Section/Stream<br/>- Fee heads table<br/>- Total amount highlighted]
    
    ShowSummary --> ReviewChoice{User Reviews}
    
    ReviewChoice -->|Need Changes| ClickBack[Click 'Back' Button]
    ClickBack --> Step2
    
    ReviewChoice -->|Looks Good| ClickCreate[Click 'Create Template' Button]
    ClickCreate --> LoadingState[Loading Overlay:<br/>'Creating template...'<br/>Spinner]
    
    LoadingState --> SuccessScreen[Success Screen:<br/>Green checkmark animation<br/>'Template Created Successfully']
    
    SuccessScreen --> ShowOptions[Action Options:<br/>- View Template<br/>- Assign to Students<br/>- Create Another Template<br/>- Back to Templates List]
    
    ShowOptions --> UserChoice{User Selects}
    
    UserChoice -->|View| ViewTemplate[Template Detail Page]
    UserChoice -->|Assign| AssignFlow[Go to Assignment Flow]
    UserChoice -->|Create Another| TemplateForm
    UserChoice -->|Back to List| UpdatedList[Templates List<br/>New template at top<br/>Badge: 'Not Assigned']
    
    UpdatedList --> End([User Continues])
    
    style Step1 fill:#e3f2fd
    style Step2 fill:#e3f2fd
    style Step3 fill:#e3f2fd
    style SuccessScreen fill:#c8e6c9
    style ShowTotal fill:#fff9c4
```

### Screen States

**1. Template List (Empty State)**
- Illustration: "No templates created"
- Suggestion: "Create templates for each class/stream combination"
- "Create Template" button prominent

**2. Template List (Grouped View)**
- Grouped by class (expandable accordions)
- Each template card shows: Name, Total amount, # of fee heads, Assignment status
- Quick actions: Edit, Duplicate, Assign, Delete

**3. Step 1: Basic Info**
- Clean form layout
- Academic year dropdown (current + next year)
- Class dropdown (1-12)
- Section: Multi-select checkboxes or "All" option
- Stream: Dropdown (Science/Commerce/Arts/General)

**4. Step 2: Fee Head Selection**
- Split-screen layout (50-50)
- Left: Available fee heads with search and category filters
- Right: Selected fee heads with amount inputs
- Drag-and-drop support
- Running total at bottom (sticky)

**5. Step 3: Review Summary**
- Card-based layout
- Editable inline (click to edit specific fields)
- "Back" button to previous steps
- "Create Template" button (primary, blue)

---

## Flow 3: Assign Fee Template to Student

### User Story
*"As an Accounts Admin, I want to assign the Class 10 Science template to a newly enrolled student so that their fee structure is set up correctly."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Dashboard]) --> ClickStudents[Click 'Student Fee Assignment' Menu]
    ClickStudents --> AssignmentPage[Fee Assignment Screen<br/>Two modes: Individual | Bulk]
    
    AssignmentPage --> SelectMode[Select 'Individual Assignment' Tab]
    SelectMode --> SearchStudent[Student Search Section<br/>Search by: Name, ID, Class]
    
    SearchStudent --> TypeSearch[Type Student Name: 'Sarah']
    TypeSearch --> ShowResults[Dropdown Shows Results:<br/>- Sarah Johnson (Class 10-A)<br/>- Sarah Williams (Class 9-B)<br/>Live search, updates as typing]
    
    ShowResults --> SelectStudent[Click on 'Sarah Johnson (Class 10-A)']
    SelectStudent --> LoadStudent[Loading Spinner<br/>'Loading student details...']
    
    LoadStudent --> StudentCard[Student Info Card Appears:<br/>- Photo<br/>- Name, ID, Class, Section<br/>- Current fee status badge]
    
    StudentCard --> CheckStatus{Fee Already Assigned?}
    
    CheckStatus -->|Yes| ShowWarning[Warning Banner:<br/>'Student already has fee structure'<br/>Options: View | Modify | Reassign]
    ShowWarning --> WarningChoice{User Choice}
    
    WarningChoice -->|View| ViewExisting[View Current Fee Structure<br/>Read-only modal]
    WarningChoice -->|Modify| ModifyFlow[Go to Modification Flow]
    WarningChoice -->|Reassign| ConfirmReassign[Confirmation Dialog:<br/>'Replace existing fee structure?'<br/>Warning: Cannot be undone]
    
    ConfirmReassign --> ClickCancel[Click 'Cancel']
    ClickCancel --> AssignmentPage
    
    ConfirmReassign --> ClickConfirm[Click 'Yes, Replace']
    ClickConfirm --> SelectTemplate
    
    CheckStatus -->|No| SelectTemplate[Template Selection Section<br/>Dropdown: 'Select Template']
    
    SelectTemplate --> ShowTemplates[Dropdown Shows:<br/>- Recommended (based on class/section)<br/>- All Templates (grouped by class)]
    
    ShowTemplates --> ClickRecommended[Click Recommended:<br/>'Class 10 Science 2024-25'<br/>Badge: 'Recommended']
    
    ClickRecommended --> LoadTemplate[Loading Template Details...]
    LoadTemplate --> ShowPreview[Template Preview Card:<br/>- Fee heads breakdown<br/>- Total amount<br/>- Installment plan preview]
    
    ShowPreview --> CheckConcession{Apply Concession?}
    
    CheckConcession -->|Yes| ClickConcession[Click 'Add Concession' Button]
    ClickConcession --> ConcessionModal[Concession Selection Modal]
    
    ConcessionModal --> ShowEligible[Auto-Check Eligibility:<br/>System shows:<br/>- Eligible concessions (green)<br/>- Ineligible (grayed out with reason)]
    
    ShowEligible --> SelectConcession[Select: 'Sibling Discount - 10%']
    SelectConcession --> ApplyConcession[Click 'Apply']
    
    ApplyConcession --> UpdatePreview[Preview Updates:<br/>- Original: ₹60,000<br/>- Discount: -₹6,000<br/>- Final: ₹54,000<br/>Green highlight on savings]
    
    CheckConcession -->|No| SelectInstallment[Installment Plan Section<br/>Dropdown: 'Select Plan']
    UpdatePreview --> SelectInstallment
    
    SelectInstallment --> ShowPlans[Available Plans:<br/>- Quarterly (Default)<br/>- Monthly<br/>- Half-Yearly<br/>- Annual (5% discount)]
    
    ShowPlans --> ClickPlan[Select: 'Quarterly']
    ClickPlan --> ShowSchedule[Payment Schedule Table:<br/>Q1 (Apr): ₹16,200<br/>Q2 (Jul): ₹16,200<br/>Q3 (Oct): ₹10,800<br/>Q4 (Jan): ₹10,800]
    
    ShowSchedule --> FinalReview[Final Review Section:<br/>Summary card with all details]
    
    FinalReview --> ClickAssign[Click 'Assign Fee Structure' Button<br/>Large, blue, primary button]
    
    ClickAssign --> ConfirmDialog[Confirmation Dialog:<br/>'Assign fee structure to Sarah Johnson?'<br/>Shows final amount]
    
    ConfirmDialog --> ClickConfirmAssign[Click 'Confirm']
    ClickConfirmAssign --> ProcessingState[Processing Overlay:<br/>'Assigning fee structure...'<br/>Progress bar]
    
    ProcessingState --> SuccessAnimation[Success Animation:<br/>Green checkmark<br/>Confetti effect]
    
    SuccessAnimation --> SuccessMessage[Success Screen:<br/>'Fee Structure Assigned Successfully'<br/>Receipt preview]
    
    SuccessMessage --> ActionButtons[Action Options:<br/>- Print Fee Receipt<br/>- Send to Parent (Email/SMS)<br/>- Assign Another Student<br/>- View Student Ledger]
    
    ActionButtons --> UserAction{User Selects}
    
    UserAction -->|Print| PrintReceipt[Open Print Dialog<br/>PDF generation]
    UserAction -->|Send| SendNotif[Send Notification Screen<br/>Email/SMS options]
    UserAction -->|Assign Another| SearchStudent
    UserAction -->|View Ledger| StudentLedger[Student Ledger Page]
    UserAction -->|Done| End([User Continues])
    
    style StudentCard fill:#e3f2fd
    style ShowPreview fill:#fff9c4
    style UpdatePreview fill:#c8e6c9
    style SuccessAnimation fill:#c8e6c9
    style ShowWarning fill:#ffe0b2
```

### Screen States

**1. Search Section**
- Large search input with icon
- Placeholder: "Search by student name, ID, or class"
- Live search results dropdown
- Recent searches shown if input empty

**2. Student Info Card**
- Profile photo (left)
- Student details (center)
- Current status badge (right): "Not Assigned" | "Assigned" | "Partial"
- Color-coded status

**3. Template Preview**
- Expandable/collapsible sections
- Fee heads in table format
- Total prominently displayed
- "Edit Template" link (opens template in new tab)

**4. Concession Modal**
- List of all concessions
- Eligibility indicator (checkmark or X)
- Reason for ineligibility shown on hover
- Preview of discount amount before applying

**5. Final Review Card**
- Summary of all selections
- Edit buttons for each section
- Total amount highlighted
- Payment schedule preview

---

## Flow 4: Configure Concession Rule

### User Story
*"As a Fee Structure Admin, I want to create a sibling discount rule so that families with multiple children automatically receive a 10% discount on the second child's fees."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Fee Management]) --> ClickConcessions[Click 'Concessions' Tab]
    ClickConcessions --> ConcessionList[Concessions List Screen<br/>Shows active and inactive rules]
    
    ConcessionList --> ClickNew[Click 'Create New Concession' Button]
    ClickNew --> RuleWizard[Concession Rule Wizard<br/>Step 1 of 4]
    
    RuleWizard --> Step1Basic[Step 1: Basic Information]
    Step1Basic --> FillBasic[Fill Fields:<br/>- Rule Name: 'Sibling Discount'<br/>- Type: Percentage<br/>- Value: 10%<br/>- Priority: Medium]
    
    FillBasic --> ClickNext1[Click 'Next']
    ClickNext1 --> Step2Eligibility[Step 2: Eligibility Criteria<br/>Define who qualifies]
    
    Step2Eligibility --> ShowCriteria[Criteria Builder:<br/>Drag-and-drop rule builder]
    
    ShowCriteria --> AddCondition[Click 'Add Condition' Button]
    AddCondition --> SelectField[Select Field: 'Number of Siblings']
    SelectField --> SelectOperator[Select Operator: 'Greater than or equal to']
    SelectOperator --> EnterValue[Enter Value: 1]
    
    EnterValue --> AddAnother{Add Another Condition?}
    
    AddAnother -->|Yes| ClickAnd[Click 'AND' or 'OR' Button]
    ClickAnd --> AddCondition
    
    AddAnother -->|No| ClickNext2[Click 'Next']
    ClickNext2 --> Step3Limits[Step 3: Limits & Restrictions]
    
    Step3Limits --> SetLimits[Configure:<br/>- Max beneficiaries: 100<br/>- Valid from: Apr 1, 2024<br/>- Valid until: Mar 31, 2025<br/>- Applicable fee heads: All<br/>- Auto-apply: Yes]
    
    SetLimits --> ClickNext3[Click 'Next']
    ClickNext3 --> Step4Review[Step 4: Review & Activate]
    
    Step4Review --> ShowSummary[Summary Display:<br/>- Rule details<br/>- Eligibility criteria (visual)<br/>- Limits<br/>- Estimated impact (# students)]
    
    ShowSummary --> SimulateButton[Click 'Simulate' Button<br/>Optional: Test rule]
    
    SimulateButton --> SimulationModal[Simulation Results Modal:<br/>- # of students who qualify<br/>- Total discount amount<br/>- Budget impact]
    
    SimulationModal --> CloseSimulation[Click 'Close']
    CloseSimulation --> Step4Review
    
    Step4Review --> ActivateChoice{Activate Now?}
    
    ActivateChoice -->|Save as Draft| ClickDraft[Click 'Save as Draft']
    ClickDraft --> DraftSuccess[Success Toast:<br/>'Rule saved as draft'<br/>Status: Inactive]
    
    ActivateChoice -->|Activate| ClickActivate[Click 'Save & Activate']
    ClickActivate --> ConfirmActivate[Confirmation Dialog:<br/>'Activate concession rule?'<br/>Warning: Will apply to eligible students]
    
    ConfirmActivate --> ClickConfirmActivate[Click 'Activate']
    ClickConfirmActivate --> ProcessingState[Processing:<br/>'Applying rule to eligible students...'<br/>Progress bar with count]
    
    ProcessingState --> SuccessScreen[Success Screen:<br/>'Concession Rule Activated'<br/>Shows: # students affected]
    
    SuccessScreen --> ShowReport[Impact Report Card:<br/>- Students affected: 45<br/>- Total discount: ₹2,70,000<br/>- Download detailed report]
    
    ShowReport --> ActionChoice{User Action}
    
    ActionChoice -->|Download Report| DownloadPDF[Generate PDF Report]
    ActionChoice -->|View Students| StudentList[List of Affected Students]
    ActionChoice -->|Create Another| RuleWizard
    ActionChoice -->|Back to List| UpdatedList[Concessions List<br/>New rule at top<br/>Badge: 'Active' | '45 students']
    
    UpdatedList --> End([User Continues])
    
    style Step1Basic fill:#e3f2fd
    style Step2Eligibility fill:#e3f2fd
    style Step3Limits fill:#e3f2fd
    style Step4Review fill:#e3f2fd
    style SuccessScreen fill:#c8e6c9
    style SimulationModal fill:#fff9c4
```

### Screen States

**1. Concessions List**
- Table view with columns: Name, Type, Value, Status, # Students, Actions
- Filter by: Status (Active/Inactive), Type (Percentage/Fixed)
- Sort by: Name, # Students, Total discount
- Quick toggle to activate/deactivate

**2. Criteria Builder**
- Visual rule builder (similar to query builders)
- Drag-and-drop interface
- AND/OR logic support
- Preview of matching students count (live update)
- Syntax validation

**3. Simulation Modal**
- Bar chart showing distribution
- Pie chart of discount by class
- Table of top beneficiaries
- Export to Excel button

**4. Impact Report**
- Summary statistics
- Before/After comparison
- List of affected students (paginated)
- Audit trail of who activated

---

## Flow 5: Set Up Optional Fee

### User Story
*"As a Fee Structure Admin, I want to create an optional School Bus Fee with capacity limits so that parents can opt-in during enrollment and we don't exceed bus capacity."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Fee Management]) --> ClickOptional[Click 'Optional Fees' Tab]
    ClickOptional --> OptionalList[Optional Fees List<br/>Shows all optional fee categories]
    
    OptionalList --> ClickNew[Click 'Create Optional Fee' Button]
    ClickNew --> FormScreen[Optional Fee Form Screen]
    
    FormScreen --> FillBasic[Fill Basic Details:<br/>- Fee Name: 'School Bus Fee'<br/>- Category: Transport<br/>- Amount: ₹12,000/year<br/>- Description: 'Annual bus transportation']
    
    FillBasic --> CapacitySection[Capacity Management Section]
    
    CapacitySection --> EnableCapacity[Toggle 'Enable Capacity Limit': ON<br/>Section expands]
    
    EnableCapacity --> SetCapacity[Set Capacity:<br/>- Total capacity: 50<br/>- Per route breakdown:<br/>  Route A: 25<br/>  Route B: 25]
    
    SetCapacity --> WaitlistToggle[Toggle 'Enable Waitlist': ON]
    WaitlistToggle --> AvailabilitySection[Availability Section]
    
    AvailabilitySection --> SelectClasses[Select Available For:<br/>Checkboxes for classes 1-12<br/>Select: All classes]
    
    SelectClasses --> SetDates[Set Availability Period:<br/>- Available from: Apr 1, 2024<br/>- Available until: Mar 31, 2025]
    
    SetDates --> RequirementsSection[Requirements Section<br/>Optional: Documents needed]
    
    RequirementsSection --> AddDoc[Click 'Add Required Document']
    AddDoc --> SelectDocType[Select: 'Address Proof'<br/>Reason: 'To verify route eligibility']
    
    SelectDocType --> PreviewSection[Preview Section<br/>Shows how it appears to parents]
    
    PreviewSection --> ClickPreview[Click 'Preview Parent View']
    ClickPreview --> PreviewModal[Modal Shows Parent Portal View:<br/>- Fee card<br/>- Capacity indicator<br/>- Enrollment button]
    
    PreviewModal --> ClosePreview[Click 'Close Preview']
    ClosePreview --> FormScreen
    
    FormScreen --> ValidateForm{Validate All Fields}
    
    ValidateForm -->|Invalid| ShowErrors[Show Errors:<br/>Highlight invalid sections]
    ShowErrors --> FormScreen
    
    ValidateForm -->|Valid| ClickSave[Click 'Save Optional Fee']
    ClickSave --> LoadingState[Loading: 'Creating optional fee...']
    
    LoadingState --> SuccessToast[Success Toast:<br/>'School Bus Fee created']
    
    SuccessToast --> UpdatedList[Optional Fees List Updates:<br/>New item with:<br/>- Capacity: 0/50<br/>- Status: Active<br/>- Waitlist: 0]
    
    UpdatedList --> ShowCard[Fee Card Shows:<br/>- Name and amount<br/>- Capacity progress bar<br/>- Quick actions: Edit, Enroll, View Enrollments]
    
    ShowCard --> UserChoice{User Action}
    
    UserChoice -->|Enroll Student| EnrollFlow[Go to Enrollment Flow]
    UserChoice -->|View Enrollments| EnrollmentList[List of Enrolled Students<br/>With route assignments]
    UserChoice -->|Edit| EditForm[Edit Optional Fee Form]
    UserChoice -->|Done| End([User Continues])
    
    style FormScreen fill:#e3f2fd
    style PreviewModal fill:#fff9c4
    style SuccessToast fill:#c8e6c9
    style ShowCard fill:#e3f2fd
```

### Screen States

**1. Optional Fees List**
- Card-based layout (grid view)
- Each card shows: Name, Amount, Capacity bar, Status
- Filter by: Category, Status, Availability
- Sort by: Name, Enrollments, Capacity

**2. Form Screen (Capacity Section)**
- Capacity input with visual indicator
- Route breakdown (if applicable)
- Real-time capacity calculator
- Warning if capacity too low

**3. Parent Portal Preview**
- Exactly as parents will see it
- Shows availability status
- "Enroll Now" button (disabled in preview)
- Capacity indicator (color-coded)

**4. Fee Card (List View)**
- Progress bar for capacity (green → yellow → red)
- Badge: "Available" | "Limited" | "Full" | "Waitlist"
- Quick stats: Enrolled, Waitlist, Revenue

---

## Flow 6: Create Installment Plan

### User Story
*"As a Fee Structure Admin, I want to create a quarterly installment plan so that parents can pay fees in 4 installments throughout the year instead of one lump sum."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Fee Management]) --> ClickPlans[Click 'Installment Plans' Tab]
    ClickPlans --> PlansList[Installment Plans List<br/>Shows existing plans]
    
    PlansList --> ClickNew[Click 'Create New Plan' Button]
    ClickNew --> PlanForm[Installment Plan Form]
    
    PlanForm --> FillBasic[Fill Basic Info:<br/>- Plan Name: 'Quarterly Plan 2024-25'<br/>- Academic Year: 2024-25<br/>- Number of Installments: 4]
    
    FillBasic --> InstallmentBuilder[Installment Builder Section<br/>Shows 4 empty installment slots]
    
    InstallmentBuilder --> Installment1[Installment 1 Configuration]
    
    Installment1 --> FillInst1[Fill Details:<br/>- Name: 'Q1 - April'<br/>- Due Date: Apr 30, 2024<br/>- Percentage: 30%<br/>- Description: 'First quarter payment']
    
    FillInst1 --> ShowCalc1[Auto-Calculate:<br/>For ₹60,000 total:<br/>Amount: ₹18,000<br/>Green checkmark]
    
    ShowCalc1 --> Installment2[Installment 2 Configuration]
    
    Installment2 --> FillInst2[Fill Details:<br/>- Name: 'Q2 - July'<br/>- Due Date: Jul 31, 2024<br/>- Percentage: 30%<br/>- Description: 'Second quarter payment']
    
    FillInst2 --> ShowCalc2[Auto-Calculate:<br/>Amount: ₹18,000]
    
    ShowCalc2 --> Installment3[Installment 3 Configuration]
    
    Installment3 --> FillInst3[Fill Details:<br/>- Name: 'Q3 - October'<br/>- Due Date: Oct 31, 2024<br/>- Percentage: 20%]
    
    FillInst3 --> ShowCalc3[Auto-Calculate:<br/>Amount: ₹12,000]
    
    ShowCalc3 --> Installment4[Installment 4 Configuration]
    
    Installment4 --> FillInst4[Fill Details:<br/>- Name: 'Q4 - January'<br/>- Due Date: Jan 31, 2025<br/>- Percentage: 20%]
    
    FillInst4 --> ShowCalc4[Auto-Calculate:<br/>Amount: ₹12,000]
    
    ShowCalc4 --> ValidateTotal{Validate:<br/>Total = 100%?}
    
    ValidateTotal -->|Not 100%| ShowTotalError[Error Banner:<br/>'Total must equal 100%'<br/>Current: 95%<br/>Red banner at top]
    ShowTotalError --> InstallmentBuilder
    
    ValidateTotal -->|Equals 100%| ShowSummary[Summary Section:<br/>- Timeline visualization<br/>- Amount breakdown<br/>- Total validation (green)]
    
    ShowSummary --> DiscountSection[Optional: Early Payment Discount]
    
    DiscountSection --> AddDiscount{Add Discount?}
    
    AddDiscount -->|Yes| ClickAddDiscount[Click 'Add Discount' Button]
    ClickAddDiscount --> DiscountModal[Discount Configuration Modal]
    
    DiscountModal --> FillDiscount[Fill:<br/>- Discount Type: Percentage<br/>- Value: 5%<br/>- Condition: 'Full payment by Apr 30']
    
    FillDiscount --> ApplyDiscount[Click 'Apply']
    ApplyDiscount --> UpdateSummary[Summary Updates:<br/>- Standard: ₹60,000<br/>- With discount: ₹57,000<br/>- Savings: ₹3,000 (highlighted)]
    
    AddDiscount -->|No| ApplicabilitySection[Applicability Section]
    UpdateSummary --> ApplicabilitySection
    
    ApplicabilitySection --> SelectClasses[Select Applicable To:<br/>- All Classes (default)<br/>- Specific Classes (checkboxes)<br/>Select: All]
    
    SelectClasses --> DefaultToggle[Toggle 'Set as Default Plan': ON<br/>Info tooltip: 'Will be auto-assigned']
    
    DefaultToggle --> FinalReview[Final Review Card:<br/>- Plan summary<br/>- Installment schedule table<br/>- Discount details<br/>- Applicability]
    
    FinalReview --> ClickSave[Click 'Save Plan' Button]
    ClickSave --> LoadingState[Loading: 'Creating installment plan...']
    
    LoadingState --> SuccessScreen[Success Screen:<br/>'Installment Plan Created'<br/>Green checkmark animation]
    
    SuccessScreen --> ActionOptions[Action Options:<br/>- Assign to Students<br/>- Set as Default<br/>- Create Another Plan<br/>- Back to Plans List]
    
    ActionOptions --> UserChoice{User Selects}
    
    UserChoice -->|Assign| AssignFlow[Bulk Assignment Screen]
    UserChoice -->|Set Default| SetDefault[Confirmation Dialog<br/>Replace current default?]
    UserChoice -->|Create Another| PlanForm
    UserChoice -->|Back| UpdatedList[Plans List Updates:<br/>New plan with badge:<br/>'Default' | '0 students assigned']
    
    UpdatedList --> End([User Continues])
    
    style InstallmentBuilder fill:#e3f2fd
    style ShowSummary fill:#fff9c4
    style UpdateSummary fill:#c8e6c9
    style SuccessScreen fill:#c8e6c9
    style ShowTotalError fill:#ffcdd2
```

### Screen States

**1. Plans List**
- Table view: Name, # Installments, # Students, Default badge, Actions
- Quick view: Hover to see installment breakdown
- Filter by: Academic year, Default status
- Sort by: Name, # Students

**2. Installment Builder**
- Accordion-style (expandable sections)
- Each installment shows: Name, Date picker, Percentage slider, Amount (calculated)
- Running total at bottom (updates live)
- Visual timeline (horizontal bar showing distribution)

**3. Summary Visualization**
- Timeline chart showing installment dates
- Bar chart showing amount distribution
- Pie chart showing percentage breakdown
- Table with all details

**4. Discount Configuration**
- Conditional logic builder
- Preview of discounted amount
- Eligibility criteria (date-based, payment method, etc.)
- Impact calculator

---

## UI/UX Design Patterns Used

### Visual Feedback Patterns

**Loading States**
- Skeleton screens for list loading
- Button spinners for form submissions
- Progress bars for multi-step processes
- Percentage indicators for bulk operations

**Success States**
- Green color scheme
- Checkmark animations
- Toast notifications (auto-dismiss)
- Success screens with next actions

**Error States**
- Red color scheme
- Inline error messages
- Field-level validation
- Error summaries at top of forms

**Warning States**
- Orange/yellow color scheme
- Warning icons
- Confirmation dialogs for destructive actions
- Capacity warnings

### Form Design Patterns

**Multi-Step Wizards**
- Progress indicator at top
- Back/Next navigation
- Save draft option
- Step validation before proceeding

**Auto-Calculation**
- Real-time total updates
- Visual indicators for calculations
- Validation of totals (must equal 100%)
- Currency formatting

**Search and Filter**
- Live search with debouncing
- Filter chips (removable)
- Sort options (ascending/descending)
- Clear all filters button

### Data Visualization

**Capacity Indicators**
- Progress bars (color-coded)
- Percentage labels
- Visual warnings at thresholds
- Real-time updates

**Financial Summaries**
- Large, bold total amounts
- Breakdown tables
- Before/After comparisons
- Savings highlighted in green

---

## Mobile Responsive Considerations

**List Views (Mobile)**
- Card layout instead of tables
- Swipe actions for quick operations
- Bottom sheet for filters
- Floating action button for create

**Forms (Mobile)**
- Single column layout
- Larger touch targets (48px minimum)
- Native date/number pickers
- Sticky save button at bottom

**Wizards (Mobile)**
- Full-screen steps
- Swipe to navigate between steps
- Progress dots instead of bar
- Bottom navigation bar
