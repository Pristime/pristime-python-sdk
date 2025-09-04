# MinBreakDuration

Defines minimum rest periods required between work assignments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**between_shifts_minutes** | **int** | Minimum rest time in minutes between consecutive shifts (e.g., 480 minutes &#x3D; 8 hours). Prevents back-to-back shifts that could cause fatigue. | 
**between_days_minutes** | **int** | Minimum rest time in minutes from end of last shift on one calendar day to start of first shift on next day (e.g., 600 minutes &#x3D; 10 hours overnight rest). | 

## Example

```python
from pristime_sdk.models.min_break_duration import MinBreakDuration

# TODO update the JSON string below
json = "{}"
# create an instance of MinBreakDuration from a JSON string
min_break_duration_instance = MinBreakDuration.from_json(json)
# print the JSON string representation of the object
print(MinBreakDuration.to_json())

# convert the object into a dict
min_break_duration_dict = min_break_duration_instance.to_dict()
# create an instance of MinBreakDuration from a dict
min_break_duration_from_dict = MinBreakDuration.from_dict(min_break_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


