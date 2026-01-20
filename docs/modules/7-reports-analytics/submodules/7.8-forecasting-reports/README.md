# 7.8 Forecasting Reports

## Overview
**Forecasting Reports** shift the focus from "What happened?" to "What *will* happen?". By analyzing historical patterns, payment behaviors, and upcoming due dates, this module predicts future cash flow and defaulter risks. It helps the management move from reactive firefighting to proactive planning.

### Real-World Analogy
Think of this as a **Weather Forecast**.
- **Collection Report**: "It rained yesterday." (Fact)
- **Forecasting Report**: "It is 80% likely to rain tomorrow." (Prediction)
Knowing it rained yesterday is useful for history, but knowing it will rain tomorrow prompts you to carry an umbrella (Prepare Cash Reserves).

## Purpose
- **Cash Flow Planning**: Estimate if there will be enough liquid cash next month to pay staff salaries and vendor bills.
- **Risk Mitigation**: Identify "At-Risk" students who show early signs of defaulting (e.g., paying later and later each term).
- **Budgeting**: Project total revenue for the upcoming academic year based on admission enquiries and fee hikes.
- **Loan Management**: assure banks of repayment capacity based on scientifically projected inflows.

## Key Features
- **Projected Collection**: "Expected Inflow: ₹50 Lakhs between 1st-10th of next month."
- **Defaulter Probability Score**: Assigns a risk score (0-100) to each student based on past behavior.
- **Scenario Modeling**: "What if we increase Transport Fees by 5%? How does that affect total revenue?"
- **Deviation Tracking**: Compare "Forecasted" vs "Actual" to improve the accuracy of the prediction model over time.

## Real-World Scenarios

### Scenario 1: The Salary Crisis Prevention
**Situation**: It's September 25th. The Accountant worries about paying October salaries (due before Diwali).
**Action**:
1.  Runs **"Cash Flow Forecast (Next 30 Days)"**.
2.  **Prediction**: "Expected Collection: ₹40 Lakhs". "Required Outflow: ₹45 Lakhs".
3.  **Insight**: Deficit of ₹5 Lakhs predicted.
4.  **Action**: Trustee arranges an overdraft facility *now*, avoiding a last-minute crisis.

### Scenario 2: The "At-Risk" Intervention
**Situation**: Student 'Rohan' usually pays on time but paid Term 1 spread over 3 months.
**Action**:
1.  The AI Model flags Rohan as **"High Risk (75%)"** for Term 2.
2.  **Action**: School sends a *gentle* pre-reminder call 10 days early, acting as a "nudge".
3.  **Outcome**: Parent arranges funds in advance and pays on time.

### Scenario 3: The Admission Revenue Target
**Situation**: Setting targets for the Admissions Team.
**Action**:
1.  Admin inputs: "Target New Admissions = 200".
2.  System calculates: 200 * (Admission Fee + Term 1 Fee).
3.  **Result**: "Projected New Revenue: ₹1.5 Crores".
4.  **Outcome**: This becomes the benchmark for the Sales Dashboard.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Black Swan Events** | A sudden lockdown occurs. Historical data says "April is high collection", but reality is zero. | **Manual Override**: Allow Admin to apply a "Stress Factor" (e.g., reduce forecast by 50%) to adjust for external crises. |
| **New School** | School is only 6 months old. No history to model. | **Rule-Based Fallback**: Use simple logic (Due Date * 80% compliance) instead of complex AI trends until 2 years of data is built. |
| **Policy Changes** | School waives Late Fees. | The model must be told that "Late Fee Revenue" will be zero, otherwise it will over-predict. |
| **Lumpy Payments** | A rich parent pays for 5 years in advance. | **Exclude Outliers**: Remove one-off massive payments from the trend analysis so they don't skew the "Average Monthly Collection". |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Forecast Period** | Date Range | Future dates (e.g., Next Month). |
| **Confidence Level** | Percentage | e.g., "85% certain". |
| **Projected Amount** | Currency | The predicted value. |
| **Basis** | String | "Based on 3-year average". |
| **Variance Limit** | Percentage | "+/- 5%". |

## User Actions
1.  **Run Simulation**: "Show impact of 10% fee hike".
2.  **View Calibration**: See how accurate last month's forecast was compared to reality.
3.  **Export Projections**: Download Excel for Bank Loan application.
4.  **Set Alerts**: "Notify me if projected collection drops below ₹20 Lakhs".

## Best Practices
- **Conservative Estimates**: Always train the model to under-promise. Better to be pleasantly surprised by extra cash than shocked by a deficit.
- **Regular Re-training**: The model should re-learn every month as new data comes in.
- **Human Judgement**: Use the forecast as a *guide*, not gospel. The Principal knows local context (e.g., "Harvest was bad this year") that the system might miss.
