# DayCosts

Daily cost parameters for different types of work time used in optimization calculations.  These costs influence how the optimizer assigns shifts by making certain work patterns more or less economically attractive. Higher costs discourage the optimizer from choosing those assignments, while lower costs make them more appealing.  **Business Impact:** - Controls overtime usage (higher overtime costs = less overtime assignments) - Manages idle time between shifts (higher idle costs = more efficient scheduling) - Balances expected vs actual work hours (flextime cost management)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_expected_hour** | **int** | Cost per hour of expected work time. Used when worker has guaranteed hours that must be paid regardless of actual assignments. | [optional] [default to 0]
**per_flextime_positive_hour** | **int** | Cost per hour when worker exceeds their standard daily hours (positive flextime). Higher values discourage over-scheduling on individual days. | [optional] [default to 8]
**per_overtime_hour** | **int** | Cost per hour of overtime work beyond regular hours. Set higher to limit overtime usage to only high-value shifts. | [optional] [default to 50]
**per_assigned_hour** | **int** | Base cost per hour for any assigned shift work. Represents the fundamental cost of having a worker on duty. | [optional] [default to 0]
**per_idle_hour_between_shifts** | **int** | Cost per hour of paid idle time between shifts on the same day. Higher values encourage tighter scheduling with fewer gaps. | [optional] [default to 1]
**per_undertime_hour** | **int** | Small cost per hour when worker is scheduled less than expected. Helps ensure workers get their expected hours when possible. | [optional] [default to 10]

## Example

```python
from pristime_sdk.models.day_costs import DayCosts

# TODO update the JSON string below
json = "{}"
# create an instance of DayCosts from a JSON string
day_costs_instance = DayCosts.from_json(json)
# print the JSON string representation of the object
print(DayCosts.to_json())

# convert the object into a dict
day_costs_dict = day_costs_instance.to_dict()
# create an instance of DayCosts from a dict
day_costs_from_dict = DayCosts.from_dict(day_costs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


