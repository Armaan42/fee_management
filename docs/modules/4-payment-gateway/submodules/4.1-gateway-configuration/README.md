# 4.1 Gateway Configuration

## Overview
The **Gateway Configuration** submodule is the bridge between your school's fee system and the banking world. It is where you set up and manage the digital connections that allow parents to pay fees online using credit cards, debit cards, UPI, and net banking.

### Real-World Analogy
Think of this as setting up a **Point of Sale (POS) Machine** at a shop counter. Before the machine can accept card payments, you need to link it to your shop's bank account using specific "merchant IDs" and "secret codes" provided by the bank. Similarly, this module links your software to a payment gateway (like Razorpay or Stripe) using API keys, ensuring that when a parent pays online, the money lands safely in the school's bank account.

## Purpose
- **Connect Banking Systems**: Link the fee software with external payment gateways.
- **Secure Transactions**: Encrypt and secure payment data using API keys.
- **Enable Online Collections**: Allow parents to pay via multiple digital channels.
- **Environment Management**: Switch between "Test Mode" (for safe checking) and "Live Mode" (for real money).

## Key Features
- **Multi-Gateway Support**: Configure multiple providers (Razorpay, Stripe, PayU, BillDesk).
- **Key Management**: securely store API Keys and Secrets.
- **Mode Switching**: Toggle between Sandbox (Test) and Production (Live) environments.
- **Webhook Setup**: Configure automated notifications from the bank to the school system.
- **Currency Configuration**: Set default transaction currencies.

## Real-World Scenarios

### Scenario 1: Setting Up for the New Academic Year
**Situation**: The school has decided to use Razorpay for online fee collection for the upcoming session.
**Action**:
1.  Admin logs into the Razorpay dashboard to retrieve the "Key ID" and "Key Secret".
2.  Opens **Gateway Configuration** in the fee software.
3.  Selects "Razorpay" from the provider list.
4.  Pastes the keys into the respective fields.
5.  Sets the status to "Live".
**Outcome**: The "Pay Online" button is enabled for parents, and payments are routed through Razorpay.

### Scenario 2: Testing Before Launch (Sandbox Mode)
**Situation**: The IT team wants to ensure the payment flow works without deducting real money from their accounts.
**Action**:
1.  Admin selects "Test/Sandbox" mode in the configuration.
2.  Enters the "Test API Keys" provided by the gateway.
3.  Performs a dummy transaction of ₹100 using a test card number.
**Outcome**: The system processes the payment successfully on the dummy network, confirming the integration works.

### Scenario 3: Key Rotation for Security
**Situation**: It has been a year, and for security reasons, the school wants to change their API keys.
**Action**:
1.  Admin generates new keys in the gateway's portal.
2.  Immediately updates the **Gateway Configuration** with the new keys.
3.  Deactivates the old keys.
**Outcome**: Security is maintained, and payment processing continues uninterrupted with the new credentials.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Invalid API Keys** | The keys entered are incorrect or contain extra spaces. | System validates keys immediately upon saving and shows "Authentication Failed" error. Trim whitespace automatically. |
| **Gateway Deduplication** | Trying to activate two gateways for the same payment type (e.g., two primary Credit Card gateways). | Alert the user: "Only one primary gateway can be active for Card payments at a time." |
| **Webhook Signature Mismatch** | The "Secret" for webhooks doesn't match the one in the gateway. | Log the error in "Failed Transactions" and alert Admin to checks the Webhook Secret configuration. |
| **Currency Mismatch** | Configured gateway supports only INR, but school tries to collect USD. | Validate gateway currency support during configuration. Disable unsupported currencies for that gateway. |
| **Expired Keys** | API keys expire or are revoked by the payment provider. | System catches the "Unauthorized" error from the first failed transaction and triggers a critical email alert to the Admin. |
| **Environment Mix-up** | Using Test Keys in Live Mode or vice versa. | Validate key format (e.g., Razorpay test keys start with `rzp_test_`) against the selected mode. Warn user if mismatched. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Provider Name** | Dropdown | The name of the payment gateway (e.g., Razorpay, Stripe). |
| **Merchant ID** | String | Unique identifier for the merchant account. |
| **Key ID / Public Key** | String | The public identifier for API authentication. |
| **Key Secret / Private Key** | String | The secret password for API authentication (Encrypted). |
| **Environment** | Toggle | Switch between 'Sandbox' (Test) and 'Production' (Live). |
| **Webhook Secret** | String | Secret key to verify incoming webhook notifications. |
| **Is Active** | Checkbox | Master switch to enable/disable this gateway. |

## User Actions
1.  **Add Gateway**: Configure a new payment provider.
2.  **Edit Configuration**: Update keys or change environment settings.
3.  **Test Connection**: Ping the gateway to verify credentials.
4.  **Activate/Deactivate**: Temporarily disable a gateway for maintenance.

## Best Practices
- **Double Check Keys**: Always copy-paste keys to avoid typing errors.
- **Use Test Mode First**: Never go live without processing at least one successful test transaction.
- **Restrict Access**: Only Super Admins should have permission to view or edit gateway credentials.
- **Monitor Webhooks**: Ensure webhooks are configured to receive real-time payment status updates (Success/Failure).
