# 9.6 Communication Templates

## Overview
**Communication Templates** are the blueprint for all outgoing messages. They ensure that whether a parent receives an SMS, an Email, or a WhatsApp message, the tone is consistent, the branding is professional, and the content is legally compliant. This module effectively "Mail Merges" school data into pre-approved text blocks.

### Real-World Analogy
Think of this as a **Rubber Stamp / Form Letter**.
- **The Problem**: If 50 teachers hand-write "Dear Parent, please pay fees", you will get 50 different handwritings, some with spelling mistakes, some rude, some too casual.
- **The Solution**: The Principal creates a standard "Form Letter". Teachers just fill in the blanks: "Dear [Name], Amount [Amount]".
This ensures that every message leaving the school gates sounds like it came from the Principal's desk.

## Purpose
- **Brand Consistency**: Ensure the school logo, footer, and polite salutations are present in every single email.
- **Error Reduction**: Elimination of typos like "Principle" vs "Principal" or "Reciept" vs "Receipt".
- **Regulatory Compliance (DLT)**: In many countries (like India), SMS templates must be registered with the Telecom Authority (TRAI) to prevent spam. This module manages those DLT Template IDs.
- **Speed**: Sending 5000 messages takes 1 second when the system doesn't have to construct each one from scratch.

## Key Features
- **Dynamic Variable Injection**: Insert `{StudentName}`, `{TotalDue}`, `{DueDate}`, `{PaymentLink}` automatically.
- **Rich Text Editor**: Create beautiful HTML emails with Bold, Italics, Tables, and Images.
- **Channel Specifics**: Maintain a "Short Version" for SMS (160 chars) and a "Long Version" for Email (Unlimited) for the same event.
- **Previewer**: See exactly how the message will look on a Parent's iPhone or Android before sending.

## Real-World Scenarios

### Scenario 1: The "Dear Perent" Embarrassment
**Situation**: A new admin staff types a manual SMS with a spelling mistake. 500 parents mock the school's English standard.
**Action**:
1.  **Switch to Templates**: Admin selects "Fee_Reminder_v1".
2.  **System**: "Dear Parent, Fee for {Student} is due."
3.  **Outcome**: Zero chance of human error. Reputation saved.

### Scenario 2: The DLT Rejection
**Situation**: School tries to send an SMS. Telecom Operator blocks it as "Marketing Spam".
**Action**:
1.  Admin registers template: "Dear Parent, your OTP is {#var#}." -> Gets ID "100723".
2.  Enters ID "100723" in the Template Module.
3.  **Outcome**: SMS is whitelist and delivered instantly.

### Scenario 3: The Festive Greeting
**Situation**: Diwali is coming. School wants to send a card.
**Action**:
1.  Designer uploads a "Diwali.jpg" banner.
2.  Admin creates an HTML Email Template causing the image.
3.  **Outcome**: Parents receive a colorful, professional greeting card in their email, not just plain text.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Missing Variable** | Template uses `{FatherName}` but the database field is empty. | **Fallback Logic**: Replace with a generic term like "Parent" or "Guardian" (e.g., "Dear Parent" instead of "Dear "). |
| **Character Overflow** | The variable `{SchoolName}` is too long, pushing SMS count from 1 to 2 credits. | **Warning Indicator**: The editor shows a "Cost Estimator". "Warning: Message length 170 chars (2 SMS Credits)". Admin can edit to shorten. |
| **Language Support** | Sending a message in Hindi or French. | **Unicode Support**: The system must store templates in UTF-8 format to support non-English characters. |
| **Broken Links** | The `{PaymentLink}` variable generates a 404 URL. | **Link Shortener & Tracking**: The system wraps the long URL into a short tracked link (e.g., `sch.ool/pay/123`) to ensure validity and track clicks. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Template Code** | String | Unique Internal ID (e.g., FEE_REM_01). |
| **DLT ID** | String | Govt Registry ID (e.g., 1407234...). |
| **Notification Type** | Enum | Fee, Attendance, transport. |
| **Channel** | Enum | SMS, Email, WhatsApp. |
| **Subject** | String | Email Subject Line. |
| **Body Content** | Text/HTML | The message with `{variables}`. |
| **Status** | Enum | Draft, Approved, Active, Archived. |

## User Actions
1.  **Test Send**: Send a sample to the Admin's own number to verify.
2.  **Clone Template**: "Copy Term 1 Reminder" -> "Edit" -> "Save as Term 2 Reminder".
3.  **Variable Picker**: Click `{Student}` from a dropdown list to insert it (no typing needed).
4.  **Audit**: See who changed the template text last.

## Best Practices
- **Variables at End**: In SMS, put variable data (like Amounts) at the end of the sentence to keep the fixed "Brand" part at the start for better readability.
- **Unsubscribe Link**: For non-transactional emails (like Newsletters), always include `{UnsubscribeLink}` to comply with anti-spam laws.
- **A/B Testing**: Create two versions of a Payment Reminder. See which one gets more clicks, and use that one.
