# PeriodCosts

Cost structure for period-level contract optimization.  These cost parameters influence how the optimization algorithm makes scheduling decisions over longer time periods (weeks, months). Higher costs discourage certain types of scheduling patterns, while lower costs make them more attractive.  **How Costs Work in Optimization:** The algorithm tries to minimize total cost while meeting all constraints and demands. By adjusting these cost parameters, you can influence scheduling priorities:  **Cost Strategies:** - **High expected_hour cost**: Discourages scheduling beyond minimum guaranteed hours - **High flextime cost**: Encourages consistent scheduling around contractual hours - **Low undertime cost**: Allows some flexibility when full hours aren't needed  **Example Impact:** If per_expected_hour=100 and a shift revenue=80, the algorithm won't assign the shift unless it helps meet other constraints, since the cost exceeds the revenue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_expected_hour** | **int** | Cost per hour of guaranteed time in the period. This discourages over-scheduling beyond minimum requirements. Set higher to prioritize cost control, lower to ensure full utilization. | [optional] [default to 0]
**per_flextime_positive_hour** | **int** | Cost per hour of positive flextime (time above contractual hours). Higher values encourage more consistent scheduling around standard contract hours rather than fluctuating weeks. | [optional] [default to 8]
**per_undertime_hour** | **int** | Small cost per hour of undertime (when scheduled time is below expected). Provides gentle pressure to meet minimum hour requirements without being too restrictive. | [optional] [default to 10]

## Example

```python
from pristime_sdk.models.period_costs import PeriodCosts

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodCosts from a JSON string
period_costs_instance = PeriodCosts.from_json(json)
# print the JSON string representation of the object
print(PeriodCosts.to_json())

# convert the object into a dict
period_costs_dict = period_costs_instance.to_dict()
# create an instance of PeriodCosts from a dict
period_costs_from_dict = PeriodCosts.from_dict(period_costs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


