# PeriodDayConstraints

Limits on the number of working days within a date range period. After a worker has reached the max_expected_days, any additional days will be scheduled as overtime.  **Common Patterns:** - **5-day work week**: scheduled_max=5 (Monday-Friday only) - **Part-time**: expected_max=3, scheduled_max=4 (3 guaranteed, up to 4 total)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_expected_days** | **int** |  | [optional] 
**max_scheduled_days** | **int** |  | [optional] 

## Example

```python
from pristime_sdk.models.period_day_constraints import PeriodDayConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodDayConstraints from a JSON string
period_day_constraints_instance = PeriodDayConstraints.from_json(json)
# print the JSON string representation of the object
print(PeriodDayConstraints.to_json())

# convert the object into a dict
period_day_constraints_dict = period_day_constraints_instance.to_dict()
# create an instance of PeriodDayConstraints from a dict
period_day_constraints_from_dict = PeriodDayConstraints.from_dict(period_day_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


