# ShiftAssignment

Tracks the current assignment status of a shift to a worker.  **Assignment States:** - **Unassigned**: worker_id is None, can be assigned to any compatible worker - **Assigned**: worker_id is set, can be reassigned if not locked - **Locked**: worker_id is set and is_locked is True, cannot be changed  **Locking Behavior:** - Locked shifts maintain their current assignment during optimization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_id** | **str** |  | [optional] 
**is_locked** | **bool** | Whether this assignment is locked and cannot be changed during optimization. Use to preserve critical or confirmed assignments. | [optional] [default to False]

## Example

```python
from pristime_sdk.models.shift_assignment import ShiftAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftAssignment from a JSON string
shift_assignment_instance = ShiftAssignment.from_json(json)
# print the JSON string representation of the object
print(ShiftAssignment.to_json())

# convert the object into a dict
shift_assignment_dict = shift_assignment_instance.to_dict()
# create an instance of ShiftAssignment from a dict
shift_assignment_from_dict = ShiftAssignment.from_dict(shift_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


