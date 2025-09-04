# DayShiftConstraints

Shift-related constraints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_count** | **int** | Maximum number of shifts allowed. | [optional] [default to 1]

## Example

```python
from pristime_sdk.models.day_shift_constraints import DayShiftConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of DayShiftConstraints from a JSON string
day_shift_constraints_instance = DayShiftConstraints.from_json(json)
# print the JSON string representation of the object
print(DayShiftConstraints.to_json())

# convert the object into a dict
day_shift_constraints_dict = day_shift_constraints_instance.to_dict()
# create an instance of DayShiftConstraints from a dict
day_shift_constraints_from_dict = DayShiftConstraints.from_dict(day_shift_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


