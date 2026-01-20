# Module 4: Online Payment Gateway

## Overview
The Online Payment Gateway module integrates third-party payment gateways (Razorpay, PayU, Paytm, etc.) to enable parents to pay fees online from anywhere, anytime. This module handles gateway configuration, transaction monitoring, failure management, and automatic reconciliation.

**Core Responsibility**: Enable secure online fee payments with seamless gateway integration.

### Real-World Analogy
Think of this module as the **Credit Card Machine (POS Terminal)** in a shop.
When you swipe your card at a store, the machine talks to the bank, checks if you have money, deduces it, and gives the shopkeeper a "Success" signal. Similarly, this module connects your school software to digital "banks" (Gateways like Razorpay/Stripe). It handles the technical conversation ensuring that when a parent clicks "Pay" on their phone, the money correctly lands in the school's account without anyone counting cash.

## Purpose
- **Gateway Integration**: Connect with multiple payment gateway providers
- **Real-time Monitoring**: Track online transactions as they happen
- **Failure Handling**: Manage failed transactions and retry mechanisms
- **Auto-Reconciliation**: Match gateway settlements with receipts
- **Payment Links**: Generate custom payment links for parents

## Submodules

### 4.1 Gateway Configuration
Configure payment gateway credentials, settings, and parameters.

**Key Features**: Multi-gateway support, Test/Live mode, API key management, Webhook configuration

**Example**: Configure Razorpay with API keys, set 2% convenience fee, enable UPI/Cards/Netbanking

**[View Detailed Documentation →](submodules/4.1-gateway-configuration/README.md)**

---

### 4.2 Real-time Transaction Monitor
Monitor all online payment transactions in real-time.

**Key Features**: Live dashboard, Transaction status, Success/failure tracking, Amount verification

**Example**: Dashboard shows 15 pending, 45 successful, 3 failed transactions today

**[View Detailed Documentation →](submodules/4.2-realtime-transaction-monitor/README.md)**

---

### 4.3 Failed Transaction Management
Handle and resolve failed online payment attempts.

**Key Features**: Failure reason tracking, Retry mechanism, Parent notification, Manual reconciliation

**Example**: Payment failed due to insufficient balance → Notify parent → Provide retry link

**[View Detailed Documentation →](submodules/4.3-failed-transaction-management/README.md)**

---

### 4.4 Gateway Reconciliation
Automatically match gateway settlements with school receipts.

**Key Features**: Auto-matching, Settlement reports, Discrepancy detection, Manual adjustment

**Example**: Match 150 transactions from Razorpay settlement with school receipts

**[View Detailed Documentation →](submodules/4.4-gateway-reconciliation/README.md)**

---

### 4.5 Payment Link Generation
Create custom payment links for specific students or amounts.

**Key Features**: Unique links, Expiry dates, Amount locking, SMS/Email delivery

**Example**: Generate link for ₹15,000 valid for 7 days, send via SMS to parent

**[View Detailed Documentation →](submodules/4.5-payment-link-generation/README.md)**

---

## Workflow

### Online Payment Flow
```
Parent Portal → Select Amount → Gateway Redirect → Payment → Confirmation → Receipt Generation → Notification
```

## Inbound Connections

| Source | Data/Trigger | Purpose |
|--------|-------------|---------|
| **Module 3 (Fee Collection)** | Payment initiation | Process online payment |
| **Parent Portal** | Payment request | Generate payment link |
| **Payment Gateway** | Payment callback | Confirm payment status |

## Outbound Connections

| Destination | Data/Trigger | Purpose |
|-------------|-------------|---------|
| **Module 3 (Fee Collection)** | Payment confirmation | Record payment and generate receipt |
| **Module 5 (Reconciliation)** | Gateway settlement | Reconcile payments |
| **Module 8 (Audit)** | Transaction logs | Audit trail |
| **Module 9 (Notifications)** | Payment status | Notify parents |

## Best Practices
1. Use test mode before going live
2. Monitor failed transactions daily
3. Reconcile gateway settlements weekly
4. Keep API keys secure
5. Set up webhook endpoints properly
6. Handle network failures gracefully

## Security & Permissions

| Role | Permissions |
|------|------------|
| **Super Admin** | Configure gateways, view all transactions |
| **Accounts Admin** | Monitor transactions, reconcile settlements |
| **Parent** | Make payments, view transaction history |
