# ShiftAssignmentResult

Tracks worker assignment changes for a specific shift after optimization.  This class captures the before and after state of shift assignments, enabling you to understand how the optimization algorithm changed your workforce schedule. Essential for tracking schedule modifications and their impact.  **Key Information:** - Current assignment after optimization - Previous assignment before optimization - Assignment change detection (new, changed, removed, unchanged)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_id** | **str** |  | [optional] 
**previous_worker_id** | **str** |  | [optional] 

## Example

```python
from pristime_sdk.models.shift_assignment_result import ShiftAssignmentResult

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftAssignmentResult from a JSON string
shift_assignment_result_instance = ShiftAssignmentResult.from_json(json)
# print the JSON string representation of the object
print(ShiftAssignmentResult.to_json())

# convert the object into a dict
shift_assignment_result_dict = shift_assignment_result_instance.to_dict()
# create an instance of ShiftAssignmentResult from a dict
shift_assignment_result_from_dict = ShiftAssignmentResult.from_dict(shift_assignment_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


