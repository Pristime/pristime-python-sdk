# Metrics

Comprehensive financial and operational metrics from workforce scheduling optimization.  These metrics provide detailed insights into the optimization's effectiveness, including revenue generated, costs incurred, and operational statistics. Essential for understanding the business impact and quality of scheduling decisions.  **Metric Categories:**  **Primary Metrics:** - profit: Overall optimization value (revenue - costs) - partial_profit: Profit excluding period-closing adjustments  **Revenue Sources:** - assignment_revenue: Value from assigning workers to high-value shifts - demand_revenue: Revenue from meeting staffing demand requirements - preferred_time_revenue: Bonus for scheduling during preferred hours - continuity_revenue: Value from maintaining worker schedule consistency - skill_revenue: Revenue from matching skilled workers with shifts that require their skills. - pto_time_revenue: Value from optimally scheduling paid time off  **Cost Factors:** - assignment_cost: Cost of worker assignments - overtime_cost: Cost of overtime hours - unpreferred_time_cost: Penalty for scheduling during unpreferred hours - idle_time_cost: Cost of gaps between worker shifts - variable_costs: Sum of all costs above  **Balance Management:** - period_closing_profit: Flextime and overtime balance adjustments - flextime_balance_negative_revenue: Revenue from accumulated time credit - flextime_balance_positive_cost: Cost of accumulated time credits - overtime_balance_cost: Cost of overtime balance  **Operational Statistics:** - assigned_time: Total minutes of productive work scheduled - overtime: Minutes of premium overtime scheduled - recovered_time: Overtime taken as PTO instead of cash payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | First date included in the metrics calculation period. | 
**end_date** | **date** | Last date included in the metrics calculation period. | 
**profit** | **float** | Total optimization value (all revenue minus all costs). Primary measure of scheduling effectiveness and business impact. | 
**partial_profit** | **float** | Core profit excluding period-closing balance adjustments. Shows operational scheduling value without accounting complexities. | 
**pto_time_revenue** | **float** | Revenue generated from optimally scheduling paid time off periods. Balances worker satisfaction with operational needs. | 
**assignment_revenue** | **float** | Revenue from assigning workers to shifts based on shift value and worker suitability. Core revenue from successful matches. | 
**skill_revenue** | **float** | Revenue bonus from matching workers with compatible shift requirements, skills, or preferences. Rewards optimal worker-shift pairing. | 
**continuity_revenue** | **float** | Revenue from maintaining consistent worker schedules and minimizing assignment changes. Values schedule stability for worker satisfaction. | 
**demand_revenue** | **float** | Revenue generated from meeting staffing demand requirements. Measures success in providing adequate coverage for business needs. | 
**preferred_time_revenue** | **float** | Bonus revenue from scheduling workers during their preferred time periods. Balances worker preferences with operational requirements. | 
**variable_costs** | **float** | Additional operational costs incurred from scheduling decisions. Includes dynamic costs that vary with assignment patterns. | 
**overtime_cost** | **float** | Premium labor costs for overtime hours beyond regular contract time. Reflects the additional expense of extended work periods. | 
**has_exceeded_preferred_max_consecutive_workdays_limit_cost** | **float** | Penalty cost when workers exceed preferred maximum consecutive workdays. | 
**idle_time_cost** | **float** | Cost of unproductive time gaps between worker shifts. Encourages efficient schedule compactness while respecting break requirements. | 
**assignment_cost** | **float** | Base labor costs for worker assignments including wages, benefits, and administrative overhead. Core cost of workforce utilization. | 
**unpreferred_time_cost** | **float** | Penalty for scheduling workers during periods they marked as unpreferred. Balances operational needs with worker satisfaction. | 
**period_closing_profit** | **float** | Profit adjustment for flextime and overtime balance management at period boundaries. Handles accounting for accumulated time credits/debts. | 
**flextime_balance_negative_revenue** | **float** | Revenue from workers making up time debt (negative flextime balance). Helps ensure contract hour obligations are met. | 
**flextime_balance_positive_cost** | **float** | Cost of accumulated worker time credits (positive flextime balance). Represents future time-off obligations or premium payments. | 
**overtime_balance_cost** | **float** | Cost associated with managing overtime balances and accumulated overtime compensation. Tracks overtime liability management. | 
**assigned_time** | **float** | Total minutes of productive work time assigned to workers. Core measure of workforce utilization and operational capacity. | 
**overtime** | **float** | Total minutes of overtime scheduled beyond regular contract hours. Indicates reliance on premium labor to meet demands. | 
**recovered_time** | **float** | Total minutes of overtime taken as paid time off instead of cash payment. Shows flexibility in overtime compensation management. | 

## Example

```python
from pristime_sdk.models.metrics import Metrics

# TODO update the JSON string below
json = "{}"
# create an instance of Metrics from a JSON string
metrics_instance = Metrics.from_json(json)
# print the JSON string representation of the object
print(Metrics.to_json())

# convert the object into a dict
metrics_dict = metrics_instance.to_dict()
# create an instance of Metrics from a dict
metrics_from_dict = Metrics.from_dict(metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


