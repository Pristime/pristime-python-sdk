# WorkDuration

Work time limits configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_minutes** | **int** | Minimum work time in minutes in a shift (not including breaks) | 
**max_minutes** | **int** | Maximum work time in minutes in a shift (not including breaks) | 

## Example

```python
from pristime_sdk.models.work_duration import WorkDuration

# TODO update the JSON string below
json = "{}"
# create an instance of WorkDuration from a JSON string
work_duration_instance = WorkDuration.from_json(json)
# print the JSON string representation of the object
print(WorkDuration.to_json())

# convert the object into a dict
work_duration_dict = work_duration_instance.to_dict()
# create an instance of WorkDuration from a dict
work_duration_from_dict = WorkDuration.from_dict(work_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


