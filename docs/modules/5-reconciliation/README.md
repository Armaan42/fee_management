# Module 5: Reconciliation & Settlement

## Overview
The Reconciliation & Settlement module ensures that all collected fees match with bank deposits and gateway settlements. It identifies discrepancies, tracks cheque clearances, and generates daily settlement reports for the accounts department.

**Core Responsibility**: Match all fee collections with bank records and ensure financial accuracy.

### Real-World Analogy
Think of this module as **Balancing Your Personal Chequebook**.
You write cheques, swipe your card, and withdraw cash. At the end of the month, you sit down with your bank statement to make sure what you *think* you spent matches what the bank *says* you spent. If there's a difference (maybe you forgot to record a coffee), you fix it. This module does exactly that but for millions of rupees in school fees, catching every missing penny before the auditors do.

## Purpose
- **Cash Reconciliation**: Match daily cash collections with deposits
- **Bank Reconciliation**: Match bank statements with receipts
- **Cheque Tracking**: Monitor cheque deposits and clearances
- **Gateway Settlement**: Reconcile online payment settlements
- **Discrepancy Resolution**: Identify and resolve mismatches
- **Settlement Reporting**: Generate end-of-day financial reports

## Submodules

### 5.1 Daily Cash Reconciliation
Match physical cash collected with system records.

**Key Features**: Cash counting, Denomination tracking, Variance detection, Daily reports

**Example**: Counter collected ₹1,25,000 cash, system shows ₹1,25,000 → Matched

**[View Detailed Documentation →](submodules/5.1-daily-cash-reconciliation/README.md)**

---

### 5.2 Bank Reconciliation
Match bank deposits with fee receipts.

**Key Features**: Statement import, Auto-matching, Manual matching, Unmatched tracking

**Example**: Import bank statement, auto-match 45/50 transactions, manually match remaining 5

**[View Detailed Documentation →](submodules/5.2-bank-reconciliation/README.md)**

---

### 5.3 Cheque Clearance Tracking
Monitor status of cheque deposits.

**Key Features**: Cheque register, Clearance status, Bounce handling, Redeposit tracking

**Example**: Track 20 cheques deposited, 18 cleared, 2 pending, 0 bounced

**[View Detailed Documentation →](submodules/5.3-cheque-clearance-tracking/README.md)**

---

### 5.4 Gateway Settlement Matching
Match payment gateway settlements with receipts.

**Key Features**: Settlement import, Auto-reconciliation, Fee deduction tracking, Discrepancy alerts

**Example**: Razorpay settled ₹2,45,000 (after 2% fee) → Match with 150 receipts

**[View Detailed Documentation →](submodules/5.4-gateway-settlement-matching/README.md)**

---

### 5.5 Discrepancy Investigation
Identify and resolve mismatches between collections and deposits.

**Key Features**: Discrepancy detection, Investigation workflow, Resolution tracking, Audit trail

**Example**: ₹5,000 mismatch found → Investigate → Found duplicate entry → Resolve

**[View Detailed Documentation →](submodules/5.5-discrepancy-investigation/README.md)**

---

### 5.6 Day-End Settlement
Generate comprehensive end-of-day settlement reports.

**Key Features**: Collection summary, Mode-wise breakdown, Bank deposit summary, Pending items

**Example**: Daily report shows ₹5,00,000 collected (Cash: ₹2L, Online: ₹3L), all reconciled

**[View Detailed Documentation →](submodules/5.6-day-end-settlement/README.md)**

---

## Workflow

### Daily Reconciliation Process
```
Collect Fees → Count Cash → Match with System → Prepare Deposit → Bank Deposit → Import Statement → Reconcile → Generate Report
```

## Inbound Connections

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Module 3 (Fee Collection)** | Payment records | Match with deposits |
| **Module 4 (Payment Gateway)** | Gateway settlements | Reconcile online payments |
| **Bank Systems** | Bank statements | Match transactions |

## Outbound Connections

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **Module 7 (Reports)** | Reconciliation status | Settlement reports |
| **Module 8 (Audit)** | Discrepancies | Audit trail |
| **Accounts Department** | Settlement data | Financial records |

## Best Practices
1. Reconcile cash daily before banking
2. Import bank statements regularly
3. Track cheque clearances weekly
4. Investigate discrepancies immediately
5. Maintain proper documentation
6. Archive reconciliation reports

## Security & Permissions

| Role | Permissions |
|------|------------|
| **Super Admin** | Full access to all reconciliation |
| **Accounts Admin** | Perform reconciliation, resolve discrepancies |
| **Fee Counter Staff** | Daily cash reconciliation only |
