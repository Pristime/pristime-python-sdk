# DayAllow

Allowed combinations of time types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overtime_with_recovery** | **bool** | Whether the worker can do overtime with recovered time. | [optional] [default to False]
**overtime_with_pto** | **bool** | Whether the worker can do overtime with PTO time. | [optional] [default to False]

## Example

```python
from pristime_sdk.models.day_allow import DayAllow

# TODO update the JSON string below
json = "{}"
# create an instance of DayAllow from a JSON string
day_allow_instance = DayAllow.from_json(json)
# print the JSON string representation of the object
print(DayAllow.to_json())

# convert the object into a dict
day_allow_dict = day_allow_instance.to_dict()
# create an instance of DayAllow from a dict
day_allow_from_dict = DayAllow.from_dict(day_allow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


