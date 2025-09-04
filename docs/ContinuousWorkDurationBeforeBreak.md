# ContinuousWorkDurationBeforeBreak

Continuous work time limits configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_minutes** | **int** | Minimum continuous work time in minutes before a shift can start a break | 
**max_minutes** | **int** | Maximum continuous work time in minutes before a shift can start a break | 

## Example

```python
from pristime_sdk.models.continuous_work_duration_before_break import ContinuousWorkDurationBeforeBreak

# TODO update the JSON string below
json = "{}"
# create an instance of ContinuousWorkDurationBeforeBreak from a JSON string
continuous_work_duration_before_break_instance = ContinuousWorkDurationBeforeBreak.from_json(json)
# print the JSON string representation of the object
print(ContinuousWorkDurationBeforeBreak.to_json())

# convert the object into a dict
continuous_work_duration_before_break_dict = continuous_work_duration_before_break_instance.to_dict()
# create an instance of ContinuousWorkDurationBeforeBreak from a dict
continuous_work_duration_before_break_from_dict = ContinuousWorkDurationBeforeBreak.from_dict(continuous_work_duration_before_break_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


