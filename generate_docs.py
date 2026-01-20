"""
Fee Management Documentation Generator
Generates README files for all remaining submodules
"""

import os

# Base path
BASE_PATH = r"c:\Users\Armaan\Documents\YAHWEH SOFTWARE SOLUTIONS\fee_managment\docs\modules"

# Module and submodule definitions
MODULES = {
    "1-fee-structure": {
        "name": "Fee Structure Setup",
        "submodules": {
            "1.3-student-fee-assignment": "Student-Specific Fee Assignment",
            "1.4-concession-configuration": "Concession Configuration",
            "1.5-optional-fee-setup": "Optional Fee Setup",
            "1.6-fee-installment-plans": "Fee Installment Plans"
        }
    },
    "2-fine-penalty": {
        "name": "Fine & Penalty Management",
        "submodules": {
            "2.1-fine-rules-configuration": "Fine Rules Configuration",
            "2.2-grace-period-setup": "Grace Period Setup",
            "2.3-fine-exemption-rules": "Fine Exemption Rules",
            "2.4-manual-fine-waiver": "Manual Fine Waiver",
            "2.5-fine-adjustment": "Fine Adjustment"
        }
    },
    "3-fee-collection": {
        "name": "Fee Collection & Receipts",
        "submodules": {
            "3.1-quick-fee-receipt": "Quick Fee Receipt",
            "3.2-partial-payment": "Partial Payment Processing",
            "3.3-advance-payment": "Advance Payment",
            "3.4-multiple-payment-modes": "Multiple Payment Modes",
            "3.5-fee-challan": "Fee Challan Generation",
            "3.6-receipt-cancellation": "Receipt Cancellation",
            "3.7-receipt-reprint": "Receipt Reprint",
            "3.8-refund-processing": "Refund Processing"
        }
    },
    "4-payment-gateway": {
        "name": "Online Payment Gateway",
        "submodules": {
            "4.1-gateway-configuration": "Gateway Configuration",
            "4.2-realtime-transaction-monitor": "Real-time Transaction Monitor",
            "4.3-failed-transaction-management": "Failed Transaction Management",
            "4.4-gateway-reconciliation": "Gateway Reconciliation",
            "4.5-payment-link-generation": "Payment Link Generation"
        }
    },
    "5-reconciliation": {
        "name": "Reconciliation & Settlement",
        "submodules": {
            "5.1-daily-cash-reconciliation": "Daily Cash Reconciliation",
            "5.2-bank-reconciliation": "Bank Reconciliation",
            "5.3-cheque-clearance-tracking": "Cheque Clearance Tracking",
            "5.4-gateway-settlement-matching": "Gateway Settlement Matching",
            "5.5-discrepancy-investigation": "Discrepancy Investigation",
            "5.6-day-end-settlement": "Day-End Settlement"
        }
    },
    "6-defaulter-management": {
        "name": "Defaulter & Dues Management",
        "submodules": {
            "6.1-defaulter-identification": "Defaulter Identification",
            "6.2-due-reminder-automation": "Due Reminder Automation",
            "6.3-escalation-workflow": "Escalation Workflow",
            "6.4-academic-hold-management": "Academic Hold Management",
            "6.5-payment-plan-negotiation": "Payment Plan Negotiation",
            "6.6-legal-notice-generation": "Legal Notice Generation"
        }
    },
    "7-reports-analytics": {
        "name": "Fee Reports & Analytics",
        "submodules": {
            "7.1-collection-reports": "Collection Reports",
            "7.2-due-reports": "Due Reports",
            "7.3-student-payment-history": "Student Payment History",
            "7.4-headwise-collection": "Head-wise Collection",
            "7.5-concession-reports": "Concession Reports",
            "7.6-fee-summary-dashboard": "Fee Summary Dashboard",
            "7.7-comparative-analysis": "Comparative Analysis",
            "7.8-forecasting-reports": "Forecasting Reports"
        }
    },
    "8-audit-compliance": {
        "name": "Audit & Compliance",
        "submodules": {
            "8.1-transaction-audit-log": "Transaction Audit Log",
            "8.2-receipt-cancellation-audit": "Receipt Cancellation Audit",
            "8.3-concession-approval-audit": "Concession Approval Audit",
            "8.4-user-activity-log": "User Activity Log",
            "8.5-fee-structure-change-history": "Fee Structure Change History",
            "8.6-compliance-reports": "Compliance Reports"
        }
    },
    "9-notifications": {
        "name": "Notifications & Communication",
        "submodules": {
            "9.1-fee-due-reminders": "Fee Due Reminders",
            "9.2-payment-confirmation": "Payment Confirmation",
            "9.3-receipt-delivery": "Receipt Delivery",
            "9.4-overdue-notifications": "Overdue Notifications",
            "9.5-custom-announcements": "Custom Announcements",
            "9.6-communication-templates": "Communication Templates",
            "9.7-delivery-status-tracking": "Delivery Status Tracking"
        }
    },
    "10-utilities": {
        "name": "Utilities & Administration",
        "submodules": {
            "10.1-control-center": "Control Center",
            "10.2-academic-year-rollover": "Academic Year Rollover",
            "10.3-bulk-fee-assignment": "Bulk Fee Assignment",
            "10.4-bulk-receipt-generation": "Bulk Receipt Generation",
            "10.5-data-import-export": "Data Import/Export",
            "10.6-transaction-history-viewer": "Transaction History Viewer",
            "10.7-custom-report-builder": "Custom Report Builder",
            "10.8-backup-restore": "Backup & Restore"
        }
    }
}

def generate_submodule_readme(submodule_id, submodule_name):
    """Generate a basic README template for a submodule"""
    return f"""# {submodule_id.upper()} {submodule_name}

## Purpose
[Brief description of what this submodule does]

## Description
[Detailed explanation of the submodule functionality]

## Key Features
- Feature 1
- Feature 2
- Feature 3

## Data Fields
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Field 1 | Type | Yes/No | Description |

## User Actions
1. **Action 1**
   - Step 1
   - Step 2

## Business Rules
- ✅ Rule 1
- ✅ Rule 2
- ⚠️ Important consideration

## Validation Rules
- Validation 1
- Validation 2

## Permissions Required
- **Create**: Role 1, Role 2
- **Edit**: Role 1, Role 2
- **View**: All users

## Related Submodules
- Related module 1
- Related module 2

## API Endpoints
```
POST   /api/endpoint    - Description
GET    /api/endpoint    - Description
```

## Database Schema
```sql
Table: table_name
- field1 (TYPE)
- field2 (TYPE)
```

## UI/UX Considerations
- Consideration 1
- Consideration 2

## Best Practices
1. Best practice 1
2. Best practice 2
"""

def generate_module_readme(module_id, module_name, submodules):
    """Generate README for a module"""
    submodule_list = "\n".join([f"### {sub_id.upper()} {sub_name}" for sub_id, sub_name in submodules.items()])
    
    return f"""# Module: {module_name}

## Overview
[Module overview and purpose]

## Purpose
[Detailed purpose of this module]

## Submodules

{submodule_list}

## Workflow
1. **Phase 1**
   - Step 1
   - Step 2

2. **Phase 2**
   - Step 1
   - Step 2

## Key Features
- ✅ Feature 1
- ✅ Feature 2

## Dependencies
- Dependency 1
- Dependency 2

## Related Modules
- Module 1
- Module 2
"""

# Generate all README files
def generate_all_readmes():
    count = 0
    for module_id, module_data in MODULES.items():
        # Generate module README
        module_path = os.path.join(BASE_PATH, module_id)
        module_readme_path = os.path.join(module_path, "README.md")
        
        if not os.path.exists(module_readme_path):
            with open(module_readme_path, 'w', encoding='utf-8') as f:
                f.write(generate_module_readme(module_id, module_data["name"], module_data["submodules"]))
            count += 1
            print(f"Created: {module_readme_path}")
        
        # Generate submodule READMEs
        for submodule_id, submodule_name in module_data["submodules"].items():
            submodule_path = os.path.join(module_path, "submodules", submodule_id)
            submodule_readme_path = os.path.join(submodule_path, "README.md")
            
            if not os.path.exists(submodule_readme_path):
                with open(submodule_readme_path, 'w', encoding='utf-8') as f:
                    f.write(generate_submodule_readme(submodule_id, submodule_name))
                count += 1
                print(f"Created: {submodule_readme_path}")
    
    print(f"\nTotal README files created: {count}")

if __name__ == "__main__":
    generate_all_readmes()
