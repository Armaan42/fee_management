# 9.5 Custom Announcements

## Overview
**Custom Announcements** enable the school to broadcast non-fee related messages. While "Reminders" are transactional (1-to-1), "Announcements" are usually broadcast (1-to-Many). This module replaces the physical notice board, the school diary note, and the morning assembly announcement with a digital push.

### Real-World Analogy
Think of this as a **Digital PA System / Smart Notice Board**.
- **The Old way**: Peon takes a circular to every class. Teacher reads it out. Students forget to tell parents.
- **The New Way**: Principal types a message. Clicks "Send". 2000 Parents get a ping instantly.
It handles everything from "Emergency Holiday due to Rain" (High Priority) to "Annual Day Invitation" (General Info).

## Purpose
- **Crisis Communication**: The fastest way to inform parents about bus breakdowns, riots, or sudden holidays.
- **Targeted Messaging**: Send "Maths Exam Tips" only to Class 10, not to Nursery.
- **Cost Saving**: Replaces printed circulars (paper cost) and phone calls (staff time).
- **Engagement**: Keeps parents involved in school activities (Sports Day, Science Fair) with rich media invites.

## Key Features
- **Audience Filter**: Select by Class, Section, Gender ("Girls Verification"), Bus Route ("Bus No 5 Breakdown"), or House ("Red House Meeting").
- **Rich Media**: Attach Photos, PDFs (Date Sheets), or Voice Notes (Principal's message).
- **Scheduling**: Draft the "Happy Diwali" message today, schedule it to auto-send on Diwali morning.
- **Approval Workflow**: Teachers can draft a message, but it sends only after Principal approves.

## Real-World Scenarios

### Scenario 1: The Rainy Day Alert
**Situation**: Heavy rains at 6:00 AM. School must declare holiday.
**Action**:
1.  Principal opens App -> **"Emergency Announcement"**.
2.  Types: "School closed today due to heavy rain."
3.  Selects: **"All Users"**. Channels: **"SMS (Priority)"**.
4.  **Outcome**: Parents receive SMS before the bus leaves. Confusion avoided.

### Scenario 2: The Exam Date Sheet
**Situation**: Admin wants to share the Final Exam schedule.
**Action**:
1.  Creates "Exam Schedule" announcement.
2.  Attaches `Datesheet.pdf`.
3.  Selects Recipients: **"Class 10 & 12"**.
4.  **Outcome**: Only relevant parents get the file. Class 1 parents are not disturbed.

### Scenario 3: The Bus Breakdown
**Situation**: School Bus No. 12 has a flat tyre. Will be 30 mins late.
**Action**:
1.  Transport Manager filters User Base: **"Route No. 12"**.
2.  Sends: "Bus 12 is delayed by 30 mins."
3.  **Outcome**: Only the 40 parents on that route are notified. Others don't panic.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Unauthorized Collection** | Teacher tries to send "Bring ₹200 for Party". | **Workflow Lock**: Any message containing currency symbols (₹, Rs) or keywords like "Pay/Collect" auto-routes to Principal for approval. |
| **DND Override** | Sending "School Closed" alert to parents with DND active. | **Priority Route**: Emergency messages are flagged as "Service Implicit" (Govt Approved) to bypass DND blocks. General marketing is blocked. |
| **Character Limit** | Message is 500 characters long. | **Concatenation vs Link**: If SMS > 160 chars, system splits it (costly). Better strategy: "Dear Parent, important circular regarding Exams. Click here to read: [Link]". |
| **Mixed Audience** | Sending to "Class 10" + "Bus Route 5". Some students might be in both. | **De-Duplication**: System ensures a parent receives the message *only once*, even if they fall into multiple filter categories. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Circular ID** | String | Unique Ref #. |
| **Title** | String | "Summer Vacation Dates". |
| **Body** | Text | The main content. |
| **Attachments** | List | URLs of uploaded files. |
| **Filter Criteria** | JSON | `{"class": ["10"], "route": ["12"]}`. |
| **Sent By** | User | Principal/Admin. |
| **Priority** | Enum | Normal, High, Emergency. |

## User Actions
1.  **Draft**: Write now, send later.
2.  **Preview**: See how it looks on a Mobile Screen.
3.  **Clone**: Copy last year's "Republic Day Invite" to save typing.
4.  **Recall**: (If App based) Delete a message sent by mistake (before it's read).

## Best Practices
- **Use Titles**: "Important: School Closed" is better than no title.
- **Timing Matters**: Don't send "Homework details" at 11 PM. Respect family time.
- **Don't Overuse**: If you send 10 messages a day, parents will mute the school notifications.
