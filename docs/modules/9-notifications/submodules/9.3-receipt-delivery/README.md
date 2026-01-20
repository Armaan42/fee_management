# 9.3 Receipt Delivery

## Overview
**Receipt Delivery** ensures that the financial document reaches its intended recipient. Generating a receipt is useless if the parent never receives it. This module acts as the "Logistic Arm" of the fee department, using Email, WhatsApp, SMS Links, and Physical Printing to deliver the Invoice/Receipt.

### Real-World Analogy
Think of this as a **Courier / Postal Service**.
- **The Letter**: The Fee Receipt (PDF).
- **The Address**: Parent's Email / WhatsApp Number.
- **The Postman**: The Notification Engine.
Just as Amazon tracks a package from "Dispatch" to "Delivered", this module tracks the receipt's journey. It answers: "Did the parent receive the mail?", "Did it bounce?", "Did they open it?".

## Purpose
- **Proof of Delivery**: In case of a dispute ("I never got the bill"), the system provides a "Delivered at 10:05 AM" timestamp.
- **Proactive Communication**: Don't wait for parents to ask "Can I get a copy?". Send it *push* via WhatsApp as soon as payment is done.
- **Environment Friendly**: Shift from "Printed Paper" (Costly, Snail Mail) to "Digital PDF" (Free, Instant).
- **Accessibility**: Deliver the receipt to where the parent is active (WhatsApp) rather than where they rarely check (School Portal).

## Key Features
- **Multi-Channel Dispatch**: Send via Email (SMTP), WhatsApp (API), SMS (Short Link).
- **Delivery Tracking**: Track status: Sent -> Delivered -> Read -> Bounced.
- **On-Demand Reprint**: Allow parents to "Resend Receipt" to themselves from the App.
- **Bulk Dispatch**: Send all "Term 1 Receipts" to 1000 parents in one click (Batch Job).

## Real-World Scenarios

### Scenario 1: The "Spam" Complaint
**Situation**: Parent claims, "I paid but never got the receipt. You people are disorganized."
**Action**:
1.  Admin checks **Delivery Log**.
2.  **Result**: "Email sent to ravi@gmail.com on 10th Jan. Status: Delivered. Status: Not Opened."
3.  **Outcome**: Information is shared with the parent. "Sir, please check your Spam folder." (Found it!).

### Scenario 2: The WhatsApp Convenience
**Situation**: Parent is busy in a meeting. Receives a WhatsApp notification.
**Action**:
1.  Notification: "Fees Received. View Receipt: [PDF Link]".
2.  Parent clicks, downloads PDF, and forwards it to their spouse instantly.
3.  **Outcome**: Zero friction experience.

### Scenario 3: The Hard Copy Request
**Situation**: An elderly guardian pays cash and insists on a "Paper Receipt".
**Action**:
1.  Accountant clicks **"Print Thermal Receipt"**.
2.  A 3-inch slip prints on the POS printer (like a supermarket bill) with QR code.
3.  **Outcome**: Physical proof provided instantly.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Bounced Email** | Mailbox full or invalid domain. | **Flag & Alert**: System marks the email as "Invalid" in the student profile so Admin can ask for a new one. Stops future sending to avoid "Blacklisting". |
| **WhatsApp Failure** | Parent doesn't have WhatsApp installed on the registered number. | **Fallback**: If WhatsApp fails, auto-send an SMS with a Web Link to download the PDF. |
| **PDF Generation Error** | The receipt PDF was corrupted (0 KB) during creation. | **Retry Mechanism**: The system checks file size before sending. If 0KB, it auto-regenerates the PDF before dispatching. |
| **Opt-Out** | Parent unsubscribed from emails. | **Regulatory Override**: Transactional emails (Receipts) bypass "Unsubscribe" lists because they are essential financial communications, not marketing. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Delivery ID** | String | Unique Tracking #. |
| **Document Type** | Enum | Invoice, Receipt, Circular. |
| **Recipient** | String | email@domain.com. |
| **Channel** | Enum | Email, WA, SMS. |
| **Sent Time** | Timestamp | Dispatch time. |
| **Status** | Enum | Queued, Sent, Delivered, Read, Bounced. |
| **Error Code** | String | "550 Mailbox Full". |

## User Actions
1.  **Resend**: Click "Resend" button on a failed entry.
2.  **Update Email**: Correct a typo in the email address and retry.
3.  **View Preview**: See exactly what the email looked like.
4.  **Download Report**: "Show me all Bounced Receipts for Class 10".

## Best Practices
- **Use PDF Attachments**: Don't put the receipt details *only* in the email body. Always attach a PDF so it can be printed/saved.
- **Subject Line Clarity**: Use "Fee Receipt - {StudentName}" instead of just "Receipt". Helps in searching.
- **Sender Reputation**: Use a verified SMTP server (SendGrid/AWS SES) to prevent emails landing in Spam.
