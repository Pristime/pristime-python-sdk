# Availability

Defines a worker's availability preferences and restrictions for scheduling.  Availability is used by the optimizer to respect worker preferences and constraints: - **Unavailable periods**: Hard constraints - worker cannot be assigned shifts during these times - **Preferred periods**: Soft preferences - optimizer tries to assign shifts during these times - **Unpreferred periods**: Soft constraints - optimizer avoids these times but can use them if needed  All periods use standard timing: start time included, end time excluded, whole minutes only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unavailable_periods** | [**List[Period]**](Period.md) | Time periods when worker cannot work at all (vacation, appointments, other commitments). These are hard constraints - no shifts will be assigned during these times. | [optional] 
**preferred_periods** | [**List[Period]**](Period.md) | Time periods when worker prefers to work (preferred hours, days off). The optimizer will prioritize assigning shifts during these times when possible. | [optional] 
**unpreferred_periods** | [**List[Period]**](Period.md) | Time periods when worker prefers not to work but is available if needed (late nights, early mornings). Used as last resort or penalized in optimization. | [optional] 

## Example

```python
from pristime_sdk.models.availability import Availability

# TODO update the JSON string below
json = "{}"
# create an instance of Availability from a JSON string
availability_instance = Availability.from_json(json)
# print the JSON string representation of the object
print(Availability.to_json())

# convert the object into a dict
availability_dict = availability_instance.to_dict()
# create an instance of Availability from a dict
availability_from_dict = Availability.from_dict(availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


