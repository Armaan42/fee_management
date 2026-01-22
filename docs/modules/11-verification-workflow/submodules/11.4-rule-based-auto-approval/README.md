# 11.4 Rule-Based Auto-Approval

## 1. Overview
Not every change requires human intervention. **Rule-Based Auto-Approval** allows the organization to define "Safe Zones" where the system acts as the Checker. This reduces "approval fatigue" and prevents the queue from being clogged with trivial tasks.

---

## 2. Key Features
- **Threshold Configuration**: Set numeric limits (e.g., "Waivers under $10 are auto-approved").
- **Whitelisting**: Trusted Makers (e.g., Senior Accountant) might have higher auto-approval limits than a Junior Clerk.
- **Field-Specific Rules**: "Typos in Remarks? Auto-approve." vs "Change in Amount? Require Human."
- **Random Sampling**: Optional setting to auto-approve 90% but randomly send 10% to a human for Quality Assurance.

## 3. Scenarios

### Scenario 1: Rounding Off Differences
- **Context**: Sometimes calculations result in fractional cents (e.g., $100.01).
- **Rule**: "Fee Adjustments < $1.00 -> Auto-Approve".
- **Benefit**: Accountants don't need the Principal's signature to fix a 1-cent rounding error.

### Scenario 2: Standard Concessions
- **Context**: The school offers a standard "Sibling Discount" of 10%.
- **Rule**: IF Concession Type = "Sibling" AND Value = "10%", THEN Auto-Approve.
- **Logic**: Since the policy is fixed, no decision is needed, only validation that the sibling exists (which the system checks).

### Scenario 3: Profile Updates by Parents
- **Context**: Parents update their own email address via the Portal.
- **Rule**: "Contact Info Updates by Parent Role -> Auto-Approve".
- **Constraint**: "Address Changes -> Human Review" (to check for transport zone impact).

## 4. Edge Cases
- **Rule Conflicts**: If two rules apply (one says Approve, one says Reject), the **Most Restrictive** rule wins (Human Verification required).
- **Limit Splitting**: A Maker tries to bypass a "$100 Limit" by creating ten distinct "$10 waivers".
    - **Defense**: The system tracks "Cumulative Daily Limit". If User's daily total > $100, trigger Human Review.
