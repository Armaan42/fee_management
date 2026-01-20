# 7.7 Comparative Analysis

## Overview
**Comparative Analysis** gives perspective to your financial data. Simply saying "We collected ₹10 Lakhs" is meaningless. Is that good? Is it bad? This module answers "How are we doing compared to last year / last month / last term?"

### Real-World Analogy
Think of this as **Sports Season Stats**.
- **The Score**: "We scored 50 goals this season."
- **The Comparison**: "But last season we scored 60."
- **The Insight**: "We are underperforming by 17%."
Reporting tells you *what happened*. Comparative Analysis tells you *if you should celebrate or panic*.

## Purpose
- **Measure Growth**: Track Year-on-Year (YoY) revenue increase to see if the school is financially expanding.
- **Identify Laggards**: Compare Section A vs Section B collection rates to shame (or motivate) the slower class teacher.
- **Spot Seasonality**: "Every June we see a dip." Knowing this helps in planning cash flow for next June.
- **Validate Decisions**: "We increased fees by 10%. Did our total revenue actually go up, or did dropouts drag it down?"

## Key Features
- **Period Comparison**: Select "This Month" vs "Last Month" or "Jan 2024" vs "Jan 2023".
- **Cohort Tracking**: Follow "Batch of 2024" as they move from Class 9 to Class 10.
- **Normalized Metrics**: Compare "Revenue per Student" to rule out the effect of increased admissions.
- **Visual Overlays**: Line graphs where 2023 is a grey line and 2024 is a bright blue line overlapping it.

## Real-World Scenarios

### Scenario 1: The Inflation Check
**Situation**: The school increased fees by 8% to beat inflation.
**Action**:
1.  Trustee runs **"YoY Revenue Report"**.
2.  **Result**: Total Collection increased by only 2%.
3.  **Insight**: The fee hike caused a higher dropout rate or more defaulters. The strategy backfired.

### Scenario 2: The "Best Teacher" Award
**Situation**: Principal wants to reward the teacher with the best fee recovery.
**Action**:
1.  Admin runs **"Class-wise Collection Comparison"**.
2.  Sorts by "% Collected".
3.  **Result**: Class 5B is at 98%, Class 5A is at 85%.
4.  **Outcome**: Class 5B teacher gets a commendation.

### Scenario 3: The June Dip
**Situation**: Cash flow is tight every June.
**Action**:
1.  Finance Head looks at **"5-Year Monthly Trend"**.
2.  Observation: "Consistently, June collection is 40% lower than May across all 5 years."
3.  **Action**: School saves surplus cash in May to cover June salaries.

## Edge Cases & Handling

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| **Fee Structure Change** | Last year "Bus Fee" was separate. This year it's merged into "Term Fee". | **Normalization**: The report groups heads into "Core Academics" vs "Ancillary" for apples-to-apples comparison. |
| **New Branch Added** | School opened a new branch this year. Total revenue doubled. | **Same-Store Sales**: Filter report to show only "Old Branch" data to see *organic* growth vs *expansion* growth. |
| **Academic Year Shift** | Last year session started in June. This year in April. | **Align by Month**: Compare "Month 1 of Session" vs "Month 1 of Session", regardless of the calendar month name. |
| **Covid Impact** | 2020-21 data is an outlier (very low). | **Exclude Outliers**: Option to "Ignore Academic Year 20-21" from the 5-year trend line to prevent skewed averages. |

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| **Period 1** | Date Range | e.g., Jan 2023. |
| **Period 2** | Date Range | e.g., Jan 2024. |
| **Metric** | Enum | Total Collection, Defaulter Count, New Admissions. |
| **Variance (₹)** | Currency | Period 2 - Period 1. |
| **Variance (%)** | Percentage | (Variance / Period 1) * 100. |

## User Actions
1.  **Set Benchmark**: "Compare current performance against Budget 2024".
2.  **Toggle Normalization**: "Switch view from 'Total Revenue' to 'Revenue Per Student'".
3.  **Export Presentation**: Download the "Growth Chart" as a high-res PNG for slide decks.
4.  **Forecast**: Use the trend line to predict where we will end up in March.

## Best Practices
- **Use Percentages**: "Growth of ₹1 Lakh" is vague. "Growth of 10%" is clear.
- **Annotate Events**: Allow Admin to add notes on the chart (e.g., "Fee Hike Implemented Here") to explain spikes.
- **Don't misinterpret Seasonality**: Don't panic if February collection is lower than January if that happens *every year*.
