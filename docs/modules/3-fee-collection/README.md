# Module 3: Fee Collection & Receipts

## Overview
The Fee Collection & Receipts module is the operational heart of the fee management system. It handles all payment processing activities, receipt generation, and payment record management across multiple payment modes including cash, cheque, card, and online payments.

**Core Responsibility**: Process all fee payments and generate accurate receipts.

## Purpose
This module serves to:

- **Process Payments**: Accept and record fee payments through various payment modes
- **Generate Receipts**: Create official payment receipts with unique numbers
- **Handle Partial Payments**: Manage installment and partial payment scenarios
- **Process Refunds**: Handle fee refunds for withdrawals and overpayments
- **Manage Receipts**: Cancel, reprint, and maintain receipt records
- **Multi-Mode Support**: Accept cash, cheque, card, UPI, and online payments

## Submodules

### 3.1 Quick Fee Receipt
**Purpose**: Generate receipts quickly for walk-in cash/card payments at the fee counter.

**What It Does**:
- Search student by ID/name/class
- Display outstanding dues
- Accept payment amount
- Select payment mode
- Generate and print receipt instantly
- Update student payment status

**Key Features**:
- Fast student lookup
- Real-time dues calculation
- Multiple payment modes
- Instant receipt printing
- Auto-numbering
- Duplicate detection

**Example Use Case**:
Parent visits fee counter:
1. Staff searches student "Rahul Kumar - Class 10A"
2. System shows: Total Due: ₹15,000, Paid: ₹5,000, Balance: ₹10,000
3. Parent pays ₹10,000 cash
4. Receipt #FEE/2024/00123 generated
5. Receipt printed and handed to parent
6. SMS sent to registered mobile

**[View Detailed Documentation →](submodules/3.1-quick-fee-receipt/README.md)**

---

### 3.2 Partial Payment Processing
**Purpose**: Handle situations where parents pay less than the full amount due.

**What It Does**:
- Accept partial payments against total dues
- Allocate payment to specific fee heads
- Track payment history
- Calculate remaining balance
- Support installment plans
- Generate partial payment receipts

**Key Features**:
- Flexible payment amounts
- Fee head allocation
- Payment tracking
- Balance calculation
- Installment support
- Payment schedule adherence

**Example Use Case**:
Total annual fee: ₹60,000
- April: Paid ₹15,000 (25%)
- July: Paid ₹20,000 (33%)
- October: Paid ₹15,000 (25%)
- January: Paid ₹10,000 (17%)
Each payment gets separate receipt, system tracks cumulative payment.

**[View Detailed Documentation →](submodules/3.2-partial-payment/README.md)**

---

### 3.3 Advance Payment
**Purpose**: Record payments made in advance for future terms or academic years.

**What It Does**:
- Accept advance payments
- Tag payments for future periods
- Adjust against future dues
- Handle advance refunds
- Track advance balances
- Generate advance receipts

**Key Features**:
- Future period tagging
- Auto-adjustment
- Refund processing
- Balance tracking
- Interest calculation (if applicable)
- Advance reporting

**Example Use Case**:
Parent pays ₹70,000 in March 2024 for academic year 2024-25:
- Receipt generated for advance payment
- Tagged for "AY 2024-25"
- When AY starts, auto-adjusted against dues
- Excess ₹10,000 carried forward or refunded

**[View Detailed Documentation →](submodules/3.3-advance-payment/README.md)**

---

### 3.4 Multiple Payment Modes
**Purpose**: Accept payments through various methods in a single transaction.

**What It Does**:
- Combine cash + card in one payment
- Mix cheque + online payment
- Split payment across modes
- Validate total amount
- Generate consolidated receipt
- Track mode-wise collections

**Key Features**:
- Multi-mode support
- Split payment handling
- Validation checks
- Consolidated receipts
- Mode-wise tracking
- Reconciliation support

**Example Use Case**:
Parent pays ₹25,000 total:
- ₹10,000 cash
- ₹15,000 by card
Single receipt shows both modes, accounting tracks separately.

**[View Detailed Documentation →](submodules/3.4-multiple-payment-modes/README.md)**

---

### 3.5 Fee Challan Generation
**Purpose**: Generate bank deposit challans for parents who prefer bank payments.

**What It Does**:
- Create unique challan numbers
- Generate bank deposit slips
- Set challan validity period
- Track challan status
- Match deposits with challans
- Handle expired challans

**Key Features**:
- Unique challan numbers
- Bank integration
- Validity management
- Status tracking
- Auto-matching
- Expiry handling

**Example Use Case**:
Parent requests challan:
1. System generates Challan #CH/2024/00456
2. Valid for 15 days
3. Parent deposits at bank
4. Bank sends deposit confirmation
5. System matches and creates receipt
6. Parent notified

**[View Detailed Documentation →](submodules/3.5-fee-challan/README.md)**

---

### 3.6 Receipt Cancellation
**Purpose**: Cancel erroneous receipts with proper authorization and audit trail.

**What It Does**:
- Cancel incorrect receipts
- Require authorization
- Mandate cancellation reason
- Reverse payment entries
- Update student dues
- Maintain audit trail

**Key Features**:
- Authorization workflow
- Mandatory justification
- Payment reversal
- Dues update
- Audit logging
- Cancellation reports

**Example Use Case**:
Receipt #FEE/2024/00125 has wrong amount:
1. Staff requests cancellation
2. Provides reason: "Amount entered incorrectly"
3. Supervisor approves
4. Receipt marked cancelled
5. Payment reversed
6. New correct receipt generated

**[View Detailed Documentation →](submodules/3.6-receipt-cancellation/README.md)**

---

### 3.7 Receipt Reprint
**Purpose**: Reprint lost or damaged receipts for parents.

**What It Does**:
- Search original receipts
- Verify authenticity
- Generate duplicate copy
- Mark as "DUPLICATE"
- Log reprint requests
- Prevent misuse

**Key Features**:
- Receipt search
- Duplicate marking
- Reprint logging
- Misuse prevention
- Bulk reprint
- Email delivery option

**Example Use Case**:
Parent lost receipt:
1. Provides receipt number or payment date
2. Staff verifies in system
3. Generates duplicate marked "DUPLICATE COPY"
4. Logs reprint with reason
5. Optionally emails PDF to parent

**[View Detailed Documentation →](submodules/3.7-receipt-reprint/README.md)**

---

### 3.8 Refund Processing
**Purpose**: Process fee refunds for student withdrawals or overpayments.

**What It Does**:
- Calculate refundable amount
- Apply refund policies
- Process refund requests
- Generate refund receipts
- Track refund status
- Handle refund modes

**Key Features**:
- Policy-based calculation
- Approval workflow
- Multiple refund modes
- Status tracking
- Refund receipts
- Accounting integration

**Example Use Case**:
Student withdraws mid-year:
1. Calculate: Paid ₹60,000, Used ₹20,000, Refundable ₹40,000
2. Apply policy: Deduct 10% processing fee
3. Net refund: ₹36,000
4. Approval workflow
5. Refund via cheque/bank transfer
6. Refund receipt generated

**[View Detailed Documentation →](submodules/3.8-refund-processing/README.md)**

---

## Complete Workflow

### Daily Collection Process
```
1. Student/Parent Arrives at Counter
↓
2. Staff Searches Student
↓
3. System Displays Outstanding Dues
↓
4. Accept Payment (Cash/Card/Cheque/UPI)
↓
5. Validate Amount
↓
6. Generate Receipt
↓
7. Print and Hand Over
↓
8. Send SMS/Email Confirmation
↓
9. Update Accounting System
```

### Online Payment Flow
```
1. Parent Logs into Portal
↓
2. Views Fee Dues
↓
3. Initiates Payment
↓
4. Redirected to Gateway
↓
5. Completes Payment
↓
6. Gateway Confirms
↓
7. System Generates Receipt
↓
8. Email Receipt to Parent
↓
9. Update Payment Status
```

## Key Features

### Multi-Mode Support
- Cash, Cheque, Card, UPI, Online
- Mixed payment modes
- Real-time processing
- Gateway integration

### Accuracy
- Auto-calculation of dues
- Duplicate detection
- Validation checks
- Audit trail

### Speed
- Quick student lookup
- Instant receipt generation
- Fast printing
- Minimal clicks

### Flexibility
- Partial payments
- Advance payments
- Refund processing
- Receipt reprints

### Security
- Authorization for cancellations
- Audit logging
- Receipt numbering
- Fraud prevention

## Dependencies

### Required Modules
- **Module 1 (Fee Structure)**: Provides student fee assignments and amounts
- **Module 2 (Fine & Penalty)**: Provides fine amounts to add to dues
- **Module 4 (Payment Gateway)**: Processes online payments

### Optional Integrations
- **Accounting System**: Sync payment records
- **SMS Gateway**: Send payment confirmations
- **Email Service**: Email receipts
- **Printer Service**: Print receipts

## Inbound Connections

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Module 1 (Fee Structure)** | Student fee assignments | Determine payment amounts |
| **Module 2 (Fine & Penalty)** | Fine amounts | Add to total collection |
| **Module 4 (Payment Gateway)** | Online payment confirmation | Record online payments |
| **Parent Portal** | Payment initiation | Process online payments |
| **Fee Counter** | Walk-in payments | Process cash/card payments |

## Outbound Connections

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **Module 5 (Reconciliation)** | Payment records | Match with bank statements |
| **Module 6 (Defaulter Management)** | Payment status | Update dues and defaulter status |
| **Module 7 (Reports)** | Collection data | Generate collection reports |
| **Module 8 (Audit)** | Transaction records | Maintain audit trail |
| **Module 9 (Notifications)** | Receipt generated | Send to parents |
| **Accounting System** | Payment entries | Financial records |

## Best Practices

1. **Receipt Management**: Never delete receipts, only cancel with proper authorization
2. **Daily Reconciliation**: Match physical cash with system records daily
3. **Backup**: Take receipt backups regularly
4. **Training**: Train staff on all payment modes
5. **Validation**: Always verify student details before accepting payment
6. **Documentation**: Maintain proper documentation for refunds and cancellations

## Security & Permissions

| Role | Permissions |
|------|------------|
| **Super Admin** | All operations including cancellations |
| **Accounts Admin** | Process payments, cancel receipts, process refunds |
| **Fee Counter Staff** | Process payments, reprint receipts |
| **Class Teacher** | View payment status only |
| **Parent** | View receipts, make online payments |

## Troubleshooting

**Issue**: Receipt not printing
- **Solution**: Check printer connection, verify receipt template, check print queue

**Issue**: Duplicate payment recorded
- **Solution**: Cancel duplicate receipt, verify payment mode, check for system lag

**Issue**: Online payment successful but receipt not generated
- **Solution**: Check gateway callback, verify payment status, manually reconcile if needed
