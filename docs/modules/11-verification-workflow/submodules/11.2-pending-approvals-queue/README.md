# 11.2 Pending Approvals Queue

## 1. Overview
The **Pending Approvals Queue** is the central "Inbox" for all Checkers (Approvers). Instead of hunting through different modules to find what needs attention, all requests requiring their sign-off are aggregated here.

It provides a unified interface to View, Compare, Comment, Approve, or Reject requests from any module in the system.

---

## 2. Key Features
- **Unified Dashboard**: See Fee changes, Admission requests, and Expense vouchers in one list.
- **Diff View (Before/After)**: Visually highlight exactly what changed (e.g., "Old Fee: 5000" vs "New Fee: 500 [ALERT: -90%]").
- **Bulk Actions**: Select multiple low-risk items and approve them in one go (if allowed).
- **Comment Threads**: Checkers can ask clarifying questions directly on the request before engaging in a formal Rejection.

## 3. Scenarios

### Scenario 1: reviewing a Fee Concession
- **Action**: Approver opens the queue and sees "Concession Request: John Doe - 30%".
- **Review**: 
    1. Clicks **View Details**.
    2. System shows the student's payment history and the uploaded "Medical Certificate".
    3. Approver types comment: "Approved on compassionate grounds".
    4. Clicks **Approve**.

### Scenario 2: Catching a Data Entry Error (The "Diff" View)
- **Action**: Approver sees "Student Profile Update".
- **Review**:
    - **Old Name**: "Sarah Jones"
    - **New Name**: "Sarah Jons"
- **Decision**: The Approver suspects a typo.
- **Action**: Clicks **Reject** with note: "Please verify spelling. Did you mean Jones?".
- **Result**: The change is discarded; the Maker is notified to fix it.

### Scenario 3: Urgent Priority Handling
- **Action**: It is admissions season. The Principal has 500 pending approvals.
- **Feature**: Sort by **Priority: High** or **Date: Oldest First**.
- **Outcome**: The Principal clears the "Scholarship Applications" (High Priority) first, leaving standard "Address Updates" for later.

## 4. Edge Cases
- **Concurrent Review**: Two approvers (e.g., VP and Principal) view the same request. If VP rejects it, the Principal's screen refreshes to show "Closed".
- **Stale Data**: If the underlying record was modified by another process while the request was pending, the system invalidates the request: "Data changed. Please resubmit."
- **Attachment Preview Fail**: If a supporting document cannot be loaded (corrupted file), the Approver MUST Reject with "Re-upload document".
