# User Flows: Fee Collection & Receipts (UI/UX Perspective)

## Introduction

This document visualizes the **user interface journey** through the Fee Collection & Receipts module from a UI/UX design perspective. This module is the operational heart of the fee management system, handling all payment processing and receipt generation.

Each flowchart focuses on:
- **Screen states** and visual feedback
- **User actions** and decision points
- **Navigation paths** between interfaces
- **Error handling** and recovery flows

---

## Flow 12: Quick Fee Receipt

### User Story
*"As a Fee Counter Staff, I want to quickly generate a receipt for a parent's cash payment, so that the transaction is completed efficiently."*

### Interface Flow

```mermaid
flowchart TD
    Start([Staff at Fee Counter]) --> Dashboard[Fee Collection Dashboard]
    
    Dashboard --> ClickQuick[Click 'Quick Receipt' Button]
    ClickQuick --> SearchScreen[Student Search Screen]
    
    SearchScreen --> TypeSearch[Type Student Name or ID]
    TypeSearch --> ShowResults[Live Search Results Dropdown]
    
    ShowResults --> SelectStudent[Select Student from List]
    SelectStudent --> LoadingStudent[Loading Student Data]
    
    LoadingStudent --> StudentCard[Student Info Card Displays]
    StudentCard --> ShowDues[Outstanding Dues Summary]
    
    ShowDues --> DuesBreakdown[Expandable Dues Breakdown]
    DuesBreakdown --> EnterAmount[Enter Payment Amount]
    
    EnterAmount --> ValidateAmount{Validate Amount}
    
    ValidateAmount -->|Exceeds Dues| ShowWarning[Warning]
    ShowWarning --> ConfirmExcess{Confirm Excess Payment?}
    
    ConfirmExcess -->|No| EnterAmount
    ConfirmExcess -->|Yes| SelectMode[Select Payment Mode]
    
    ValidateAmount -->|Valid| SelectMode
    
    SelectMode --> ModeChoice{Payment Mode}
    
    ModeChoice -->|Cash| CashSelected[Cash Payment Selected]
    ModeChoice -->|Card| CardSelected[Card Payment Selected]
    ModeChoice -->|Cheque| ChequeSelected[Cheque Payment Selected]
    ModeChoice -->|UPI| UPISelected[UPI Payment Selected]
    
    CashSelected --> ClickGenerate[Click 'Generate Receipt']
    
    CardSelected --> EnterCardDetails[Enter Card Details]
    EnterCardDetails --> ProcessCard[Process Card Payment]
    ProcessCard --> ClickGenerate
    
    ChequeSelected --> EnterChequeDetails[Enter Cheque Number and Bank]
    EnterChequeDetails --> ClickGenerate
    
    UPISelected --> EnterUPIRef[Enter UPI Reference Number]
    EnterUPIRef --> ClickGenerate
    
    ClickGenerate --> ProcessingState[Processing Payment]
    ProcessingState --> ReceiptGenerated[Receipt Generated]
    
    ReceiptGenerated --> ShowReceipt[Receipt Preview Screen]
    ShowReceipt --> ActionChoice{User Action}
    
    ActionChoice -->|Print| ClickPrint[Click 'Print' Button]
    ClickPrint --> PrintDialog[Print Dialog Opens]
    PrintDialog --> Printing[Printing Receipt]
    Printing --> PrintSuccess[Receipt Printed]
    
    ActionChoice -->|Email| ClickEmail[Click 'Email' Button]
    ClickEmail --> EmailSent[Email Sent to Parent]
    
    ActionChoice -->|SMS| ClickSMS[Click 'Send SMS']
    ClickSMS --> SMSSent[SMS Sent]
    
    PrintSuccess --> NextAction{Next Action}
    EmailSent --> NextAction
    SMSSent --> NextAction
    
    NextAction -->|Another Receipt| SearchScreen
    NextAction -->|Done| UpdatedDashboard[Dashboard Updates]
    
    UpdatedDashboard --> End([Staff Continues])
    
    style StudentCard fill:#e3f2fd
    style ShowReceipt fill:#c8e6c9
    style ProcessingState fill:#fff9c4
    style ShowWarning fill:#ffe0b2
```

### Screen States

**1. Student Search**
- Large search input with icon
- Live search results
- Recent students shown
- Quick filters by class

**2. Student Card**
- Photo and basic info
- Total dues highlighted
- Payment history summary
- Quick actions

**3. Dues Breakdown**
- Expandable table
- Fee heads with amounts
- Color-coded status
- Total calculation

**4. Payment Mode Selection**
- Radio buttons with icons
- Mode-specific fields appear
- Validation per mode
- Quick toggle between modes

**5. Receipt Preview**
- Full receipt display
- Print/Email/SMS buttons
- Download PDF option
- New receipt button

---

## Flow 13: Partial Payment Processing

### User Story
*"As a Fee Counter Staff, I want to accept a partial payment of ₹5,000 when the total due is ₹15,000, so that parents can pay in installments."*

### Interface Flow

```mermaid
flowchart TD
    Start([Staff on Fee Collection]) --> SearchStudent[Search and Select Student]
    SearchStudent --> StudentLoaded[Student Data Loaded]
    
    StudentLoaded --> ShowDues[Total Dues]
    ShowDues --> ClickPartial[Click 'Partial Payment' Option]
    
    ClickPartial --> PartialForm[Partial Payment Form]
    PartialForm --> EnterAmount[Enter Amount]
    
    EnterAmount --> AllocationChoice{Auto or Manual Allocation?}
    
    AllocationChoice -->|Auto| AutoAllocate[System Auto-Allocates to Fee Heads]
    AllocationChoice -->|Manual| ManualAllocate[Manual Allocation Screen]
    
    ManualAllocate --> ShowFeeHeads[List of Fee Heads]
    ShowFeeHeads --> AllocateAmounts[Allocate Amounts to Each Head]
    AllocateAmounts --> ValidateAllocation{Total Matches?}
    
    ValidateAllocation -->|No| ShowError[Error]
    ShowError --> AllocateAmounts
    
    ValidateAllocation -->|Yes| ShowSummary[Allocation Summary]
    AutoAllocate --> ShowSummary
    
    ShowSummary --> SelectMode[Select Payment Mode]
    SelectMode --> EnterModeDetails[Enter Mode-Specific Details]
    
    EnterModeDetails --> ClickGenerate[Click 'Generate Receipt']
    ClickGenerate --> ProcessingState[Processing Partial Payment]
    
    ProcessingState --> ReceiptGenerated[Partial Payment Receipt Generated]
    ReceiptGenerated --> ShowReceipt[Receipt Preview]
    
    ShowReceipt --> ShowBalance[Remaining Balance]
    ShowBalance --> PrintReceipt[Print Receipt]
    
    PrintReceipt --> UpdateDues[Dues Updated in System]
    UpdateDues --> End([Staff Continues])
    
    style PartialForm fill:#e3f2fd
    style ShowSummary fill:#fff9c4
    style ReceiptGenerated fill:#c8e6c9
```

### Screen States

**1. Partial Payment Form**
- Amount input with validation
- Auto/Manual allocation toggle
- Real-time balance calculation
- Payment mode selector

**2. Manual Allocation Screen**
- Table of fee heads
- Amount input for each
- Running total
- Validation indicators

**3. Allocation Summary**
- Before/After comparison
- Allocated amounts per head
- Remaining balance
- Confirm button

---

## Flow 14: Advance Payment

### User Story
*"As a Fee Counter Staff, I want to record an advance payment of ₹70,000 for the next academic year, so that it can be adjusted when the year starts."*

### Interface Flow

```mermaid
flowchart TD
    Start([Staff on Fee Collection]) --> SearchStudent[Search Student]
    SearchStudent --> StudentLoaded[Student Data Loaded]
    
    StudentLoaded --> ClickAdvance[Click 'Advance Payment']
    ClickAdvance --> AdvanceForm[Advance Payment Form]
    
    AdvanceForm --> EnterAmount[Enter Amount]
    EnterAmount --> SelectPeriod[Select Future Period]
    
    SelectPeriod --> PeriodChoice{Period Selection}
    
    PeriodChoice -->|Next AY| SelectNextAY[Select Academic Year 2024-25]
    PeriodChoice -->|Specific Term| SelectTerm[Select Term]
    PeriodChoice -->|Unallocated| UnallocatedAdvance[Mark as Unallocated]
    
    SelectNextAY --> EnterNotes[Enter Notes]
    SelectTerm --> EnterNotes
    UnallocatedAdvance --> EnterNotes
    
    EnterNotes --> SelectMode[Select Payment Mode]
    SelectMode --> EnterModeDetails[Enter Payment Details]
    
    EnterModeDetails --> ReviewAdvance[Review Advance Payment]
    ReviewAdvance --> ClickGenerate[Click 'Generate Receipt']
    
    ClickGenerate --> ProcessingState[Processing Advance Payment]
    ProcessingState --> ReceiptGenerated[Advance Receipt Generated]
    
    ReceiptGenerated --> ShowReceipt[Receipt Preview]
    ShowReceipt --> TaggedInfo[Shows]
    
    TaggedInfo --> PrintReceipt[Print Receipt]
    PrintReceipt --> UpdateRecords[Advance Balance Updated]
    
    UpdateRecords --> End([Staff Continues])
    
    style AdvanceForm fill:#e3f2fd
    style ReviewAdvance fill:#fff9c4
    style ReceiptGenerated fill:#c8e6c9
```

### Screen States

**1. Advance Payment Form**
- Amount input
- Period selector dropdown
- Notes textarea
- Payment mode selector

**2. Period Selection**
- Academic year dropdown
- Term selector
- Unallocated option
- Future date picker

**3. Review Screen**
- Amount summary
- Period tagging
- Payment mode
- Confirm button

---

## Flow 15: Multiple Payment Modes

### User Story
*"As a Fee Counter Staff, I want to accept ₹10,000 cash and ₹15,000 by card in a single transaction, so that the parent can use multiple payment methods."*

### Interface Flow

```mermaid
flowchart TD
    Start([Staff on Fee Collection]) --> SearchStudent[Search Student]
    SearchStudent --> StudentLoaded[Student Data Loaded]
    
    StudentLoaded --> ShowDues[Total Dues Displayed]
    ShowDues --> ClickMultiMode[Click 'Multiple Payment Modes']
    
    ClickMultiMode --> MultiModeForm[Multi-Mode Payment Form]
    MultiModeForm --> ShowTotal[Total Amount to Collect]
    
    ShowTotal --> AddMode1[Click 'Add Payment Mode']
    AddMode1 --> SelectMode1[Select Mode]
    SelectMode1 --> EnterAmount1[Enter Amount]
    
    EnterAmount1 --> AddMode2[Click 'Add Another Mode']
    AddMode2 --> SelectMode2[Select Mode]
    SelectMode2 --> EnterAmount2[Enter Amount]
    EnterAmount2 --> EnterCardDetails[Enter Card Details]
    
    EnterCardDetails --> ShowSummary[Payment Summary]
    ShowSummary --> ValidateTotal{Total Matches Dues?}
    
    ValidateTotal -->|No| ShowMismatch[Warning]
    ShowMismatch --> MultiModeForm
    
    ValidateTotal -->|Yes| ClickGenerate[Click 'Generate Receipt']
    ClickGenerate --> ProcessingState[Processing Multi-Mode Payment]
    
    ProcessingState --> ProcessCard[Process Card Payment]
    ProcessCard --> CardSuccess{Card Successful?}
    
    CardSuccess -->|No| CardError[Card Payment Failed]
    CardError --> RetryCard{Retry Card?}
    
    RetryCard -->|Yes| ProcessCard
    RetryCard -->|No| CancelTransaction[Cancel Transaction]
    
    CardSuccess -->|Yes| ReceiptGenerated[Consolidated Receipt Generated]
    ReceiptGenerated --> ShowReceipt[Receipt Preview]
    
    ShowReceipt --> ShowModeBreakdown[Mode-wise Breakdown Displayed]
    ShowModeBreakdown --> PrintReceipt[Print Receipt]
    
    PrintReceipt --> End([Staff Continues])
    CancelTransaction --> End
    
    style MultiModeForm fill:#e3f2fd
    style ShowSummary fill:#fff9c4
    style ReceiptGenerated fill:#c8e6c9
    style CardError fill:#ffcdd2
```

### Screen States

**1. Multi-Mode Form**
- Total amount display
- Add mode button
- List of added modes
- Running total

**2. Mode Entry**
- Mode selector
- Amount input
- Mode-specific fields
- Remove button

**3. Payment Summary**
- Mode-wise breakdown table
- Total calculation
- Validation status
- Generate button

---

## Flow 16: Fee Challan Generation

### User Story
*"As a Fee Counter Staff, I want to generate a bank challan for a parent who prefers to pay at the bank, so that the payment can be tracked."*

### Interface Flow

```mermaid
flowchart TD
    Start([Staff on Fee Collection]) --> SearchStudent[Search Student]
    SearchStudent --> StudentLoaded[Student Data Loaded]
    
    StudentLoaded --> ShowDues[Dues Displayed]
    ShowDues --> ClickChallan[Click 'Generate Challan']
    
    ClickChallan --> ChallanForm[Challan Generation Form]
    ChallanForm --> EnterAmount[Enter Challan Amount]
    EnterAmount --> SelectBank[Select Bank]
    
    SelectBank --> SetValidity[Set Validity Period]
    SetValidity --> EnterNotes[Enter Notes]
    
    EnterNotes --> ReviewChallan[Review Challan Details]
    ReviewChallan --> ClickGenerate[Click 'Generate Challan']
    
    ClickGenerate --> ProcessingState[Generating Challan]
    ProcessingState --> ChallanGenerated[Challan Generated]
    
    ChallanGenerated --> ShowChallan[Challan Preview]
    ShowChallan --> ChallanDetails[Shows Challan Number and Validity]
    
    ChallanDetails --> ActionChoice{User Action}
    
    ActionChoice -->|Print| PrintChallan[Print Challan]
    ActionChoice -->|Email| EmailChallan[Email to Parent]
    ActionChoice -->|SMS| SMSChallan[SMS Challan Details]
    
    PrintChallan --> ChallanTracking[Challan Added to Tracking]
    EmailChallan --> ChallanTracking
    SMSChallan --> ChallanTracking
    
    ChallanTracking --> End([Staff Continues])
    
    style ChallanForm fill:#e3f2fd
    style ShowChallan fill:#c8e6c9
    style ProcessingState fill:#fff9c4
```

### Screen States

**1. Challan Form**
- Amount input
- Bank dropdown
- Validity date picker
- Notes textarea

**2. Challan Preview**
- Challan number
- Student details
- Amount and bank
- Validity date
- Barcode/QR code

**3. Challan Tracking**
- Status: Pending
- Validity countdown
- Bank details
- Actions: Cancel, Extend

---

## Flow 17: Receipt Cancellation

### User Story
*"As an Accounts Admin, I want to cancel an incorrect receipt and reverse the payment, so that a correct receipt can be generated."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Fee Collection]) --> ClickCancellation[Click 'Receipt Cancellation']
    ClickCancellation --> SearchReceipt[Receipt Search Screen]
    
    SearchReceipt --> TypeReceiptNo[Enter Receipt Number]
    TypeReceiptNo --> SearchResults[Search Results]
    
    SearchResults --> SelectReceipt[Select Receipt to Cancel]
    SelectReceipt --> LoadReceipt[Load Receipt Details]
    
    LoadReceipt --> ReceiptPreview[Receipt Preview Display]
    ReceiptPreview --> CheckStatus{Receipt Status}
    
    CheckStatus -->|Already Cancelled| ShowError[Error]
    CheckStatus -->|Valid| ClickCancel[Click 'Cancel Receipt' Button]
    
    ClickCancel --> CancellationDialog[Cancellation Dialog Opens]
    CancellationDialog --> SelectReason[Select Cancellation Reason]
    
    SelectReason --> ReasonChoice{Reason Type}
    
    ReasonChoice -->|Wrong Amount| WrongAmount[Reason]
    ReasonChoice -->|Wrong Student| WrongStudent[Reason]
    ReasonChoice -->|Duplicate| Duplicate[Reason]
    ReasonChoice -->|Other| OtherReason[Enter Custom Reason]
    
    WrongAmount --> EnterDetails[Enter Detailed Explanation]
    WrongStudent --> EnterDetails
    Duplicate --> EnterDetails
    OtherReason --> TypeCustomReason[Type Custom Reason]
    TypeCustomReason --> EnterDetails
    
    EnterDetails --> AttachDoc{Attach Supporting Document?}
    
    AttachDoc -->|Yes| UploadDoc[Upload Document]
    UploadDoc --> ReviewCancellation[Review Cancellation Request]
    
    AttachDoc -->|No| ReviewCancellation
    
    ReviewCancellation --> AuthCheck{Requires Higher Approval?}
    
    AuthCheck -->|Yes| SubmitForApproval[Submit for Approval]
    SubmitForApproval --> ApprovalPending[Approval Pending Status]
    ApprovalPending --> PendingNotif[Pending Notification]
    
    AuthCheck -->|No| ClickConfirm[Click 'Confirm Cancellation']
    ClickConfirm --> ProcessingState[Processing Cancellation]
    
    ProcessingState --> ReversalSteps[Reversal Process]
    ReversalSteps --> UpdateDues[Update Student Dues]
    UpdateDues --> UpdateAccounting[Update Accounting Records]
    UpdateAccounting --> MarkCancelled[Mark Receipt as Cancelled]
    
    MarkCancelled --> SuccessScreen[Cancellation Success]
    SuccessScreen --> ShowConfirmation[Cancellation Confirmation]
    
    ShowConfirmation --> ActionChoice{User Action}
    
    ActionChoice -->|Generate New| NewReceipt[Generate Correct Receipt]
    ActionChoice -->|Print Cancellation| PrintCancel[Print Cancellation Receipt]
    ActionChoice -->|Done| End([Admin Continues])
    
    PendingNotif --> End
    ShowError --> End
    
    style CancellationDialog fill:#e3f2fd
    style ReviewCancellation fill:#fff9c4
    style SuccessScreen fill:#c8e6c9
    style ShowError fill:#ffcdd2
```

### Screen States

**1. Receipt Search**
- Search by receipt number
- Search by date range
- Search by student
- Recent cancellations

**2. Cancellation Dialog**
- Reason dropdown
- Detailed explanation textarea
- Document upload
- Warning message

**3. Authorization Check**
- Shows approval threshold
- Displays required approver
- Estimated approval time
- Notification option

---

## Flow 18: Receipt Reprint

### User Story
*"As a Fee Counter Staff, I want to reprint a lost receipt for a parent, so that they have a copy for their records."*

### Interface Flow

```mermaid
flowchart TD
    Start([Staff on Fee Collection]) --> ClickReprint[Click 'Receipt Reprint']
    ClickReprint --> SearchScreen[Receipt Search Screen]
    
    SearchScreen --> SearchChoice{Search By}
    
    SearchChoice -->|Receipt Number| EnterReceiptNo[Enter Receipt Number]
    SearchChoice -->|Student Name| EnterStudentName[Enter Student Name]
    SearchChoice -->|Date| SelectDate[Select Date Range]
    
    EnterReceiptNo --> SearchResults[Search Results Display]
    EnterStudentName --> SearchResults
    SelectDate --> SearchResults
    
    SearchResults --> SelectReceipt[Select Receipt to Reprint]
    SelectReceipt --> LoadReceipt[Load Receipt Details]
    
    LoadReceipt --> ReceiptPreview[Receipt Preview Display]
    ReceiptPreview --> VerifyDetails[Verify Receipt Details]
    
    VerifyDetails --> ClickReprint2[Click 'Reprint' Button]
    ClickReprint2 --> ReprintDialog[Reprint Confirmation Dialog]
    
    ReprintDialog --> EnterReason[Enter Reason for Reprint]
    EnterReason --> ReasonChoice{Reason}
    
    ReasonChoice -->|Lost Original| LostOriginal[Reason]
    ReasonChoice -->|Damaged| Damaged[Reason]
    ReasonChoice -->|For Records| ForRecords[Reason]
    ReasonChoice -->|Other| OtherReason[Enter Custom Reason]
    
    LostOriginal --> ClickConfirm[Click 'Confirm Reprint']
    Damaged --> ClickConfirm
    ForRecords --> ClickConfirm
    OtherReason --> ClickConfirm
    
    ClickConfirm --> ProcessingState[Generating Duplicate]
    ProcessingState --> DuplicateGenerated[Duplicate Receipt Generated]
    
    DuplicateGenerated --> ShowDuplicate[Duplicate Receipt Preview]
    ShowDuplicate --> DuplicateMarking[Shows DUPLICATE Watermark]
    
    DuplicateMarking --> ActionChoice{User Action}
    
    ActionChoice -->|Print| PrintDuplicate[Print Duplicate]
    ActionChoice -->|Email| EmailDuplicate[Email to Parent]
    ActionChoice -->|Both| PrintAndEmail[Print and Email]
    
    PrintDuplicate --> LogReprint[Log Reprint Request]
    EmailDuplicate --> LogReprint
    PrintAndEmail --> LogReprint
    
    LogReprint --> End([Staff Continues])
    
    style ReprintDialog fill:#e3f2fd
    style ShowDuplicate fill:#fff9c4
    style DuplicateGenerated fill:#c8e6c9
```

### Screen States

**1. Receipt Search**
- Multiple search options
- Advanced filters
- Recent reprints shown
- Quick search

**2. Receipt Preview**
- Full receipt display
- Original/Duplicate indicator
- Reprint history
- Verify button

**3. Duplicate Receipt**
- DUPLICATE watermark
- Original receipt number
- Reprint date and time
- Reprint reason shown

---

## Flow 19: Refund Processing

### User Story
*"As an Accounts Admin, I want to process a refund of ₹36,000 for a student who withdrew mid-year, so that the parent receives their money back."*

### Interface Flow

```mermaid
flowchart TD
    Start([Admin on Fee Collection]) --> ClickRefund[Click 'Refund Processing']
    ClickRefund --> SearchStudent[Search Student]
    
    SearchStudent --> StudentLoaded[Student Data Loaded]
    StudentLoaded --> CheckEligibility{Eligible for Refund?}
    
    CheckEligibility -->|No| ShowIneligible[Error]
    CheckEligibility -->|Yes| RefundCalculator[Refund Calculator Screen]
    
    RefundCalculator --> ShowPaid[Amount Paid]
    ShowPaid --> ShowUsed[Amount Used]
    ShowUsed --> CalculateRefundable[Refundable]
    
    CalculateRefundable --> ApplyPolicy[Apply Refund Policy]
    ApplyPolicy --> ShowDeductions[Deductions Display]
    
    ShowDeductions --> ProcessingFee[Processing Fee]
    ProcessingFee --> NetRefund[Net Refund]
    
    NetRefund --> SelectRefundMode[Select Refund Mode]
    SelectRefundMode --> ModeChoice{Refund Mode}
    
    ModeChoice -->|Cheque| ChequeDetails[Enter Cheque Details]
    ModeChoice -->|Bank Transfer| BankDetails[Enter Bank Account Details]
    ModeChoice -->|Cash| CashRefund[Cash Refund Selected]
    
    ChequeDetails --> EnterNotes[Enter Refund Notes]
    BankDetails --> EnterNotes
    CashRefund --> EnterNotes
    
    EnterNotes --> AttachDocs[Attach Supporting Documents]
    AttachDocs --> ReviewRefund[Review Refund Request]
    
    ReviewRefund --> SubmitApproval[Submit for Approval]
    SubmitApproval --> ApprovalWorkflow[Approval Workflow]
    
    ApprovalWorkflow --> ApprovalDecision{Approval Decision}
    
    ApprovalDecision -->|Rejected| RejectedNotif[Rejection Notification]
    RejectedNotif --> End([Admin Continues])
    
    ApprovalDecision -->|Approved| ProcessRefund[Process Refund]
    ProcessRefund --> GenerateRefundReceipt[Generate Refund Receipt]
    
    GenerateRefundReceipt --> UpdateRecords[Update Student Records]
    UpdateRecords --> UpdateAccounting[Update Accounting]
    
    UpdateAccounting --> SuccessScreen[Refund Processed Successfully]
    SuccessScreen --> ShowConfirmation[Refund Confirmation]
    
    ShowConfirmation --> ActionChoice{User Action}
    
    ActionChoice -->|Print| PrintRefundReceipt[Print Refund Receipt]
    ActionChoice -->|Email| EmailRefund[Email to Parent]
    ActionChoice -->|Track| TrackRefund[Add to Refund Tracking]
    
    PrintRefundReceipt --> End
    EmailRefund --> End
    TrackRefund --> End
    ShowIneligible --> End
    
    style RefundCalculator fill:#e3f2fd
    style ReviewRefund fill:#fff9c4
    style SuccessScreen fill:#c8e6c9
    style ShowIneligible fill:#ffcdd2
```

### Screen States

**1. Refund Calculator**
- Amount paid display
- Amount used calculation
- Refundable amount
- Policy deductions
- Net refund highlighted

**2. Refund Mode Selection**
- Radio buttons for modes
- Mode-specific form fields
- Validation per mode
- Processing time estimates

**3. Approval Workflow**
- Current approver
- Approval status
- Estimated time
- Notification options

**4. Refund Receipt**
- Refund details
- Calculation breakdown
- Mode of refund
- Reference numbers

---

## UI/UX Design Patterns Used

### Visual Feedback Patterns

**Loading States**
- Skeleton screens for data loading
- Progress bars for processing
- Spinners for quick actions
- Status indicators

**Success States**
- Green color scheme
- Checkmark animations
- Toast notifications
- Success screens

**Error States**
- Red color scheme
- Inline error messages
- Field-level validation
- Recovery instructions

**Warning States**
- Orange/yellow color scheme
- Warning icons
- Confirmation dialogs
- Impact previews

### Form Design Patterns

**Quick Entry Forms**
- Minimal fields
- Auto-complete
- Keyboard shortcuts
- Tab navigation

**Multi-Step Processes**
- Progress indicators
- Back/Next navigation
- Save draft option
- Step validation

**Validation**
- Real-time validation
- Inline error messages
- Summary of errors
- Prevent submission if invalid

### Receipt Design

**Receipt Preview**
- Professional layout
- School branding
- Clear amount breakdown
- QR code for verification
- Print-optimized format

**Duplicate Marking**
- DUPLICATE watermark
- Different color scheme
- Original receipt reference
- Reprint information

---

## Mobile Responsive Considerations

**Fee Collection Dashboard**
- Card layout
- Quick action buttons
- Recent transactions
- Summary widgets

**Receipt Forms**
- Single column layout
- Larger touch targets
- Native input types
- Sticky action buttons

**Receipt Preview**
- Optimized for mobile viewing
- Pinch to zoom
- Share options
- Mobile-friendly print
