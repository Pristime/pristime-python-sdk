# PeriodTimeConstraints

Time constraints and limits for a worker over a specific date range (most commonly a week).  **Common Patterns:** - **40-hour work week**: contractual=2400 (40*60), min_expected=2400 (40*60), max_expected=2400 (40*60), max_overtime=600 (10 hours) - **Flexible Part-time contract**: contractual=1200 (20 hours), min_expected=900 (15 hours), max_expected=1500 (25 hours), max_overtime=300 (5 hours)  **Set to None to indicate no limit for that constraint.**

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contractual_time_minutes** | **int** |  | [optional] 
**min_expected_time_minutes** | **int** |  | [optional] 
**max_expected_time_minutes** | **int** |  | [optional] 
**max_overtime_minutes** | **int** |  | [optional] 
**max_assigned_time_minutes** | **int** |  | [optional] 
**max_recovered_time_minutes** | **int** |  | [optional] 
**max_pto_time_minutes** | **int** |  | [optional] 
**max_scheduled_time_minutes** | **int** |  | [optional] 

## Example

```python
from pristime_sdk.models.period_time_constraints import PeriodTimeConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodTimeConstraints from a JSON string
period_time_constraints_instance = PeriodTimeConstraints.from_json(json)
# print the JSON string representation of the object
print(PeriodTimeConstraints.to_json())

# convert the object into a dict
period_time_constraints_dict = period_time_constraints_instance.to_dict()
# create an instance of PeriodTimeConstraints from a dict
period_time_constraints_from_dict = PeriodTimeConstraints.from_dict(period_time_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


