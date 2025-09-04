# ProvidedShiftsDurations

These metrics help you understand how much of your schedule was modified during optimization and the nature of those changes. All values are in minutes.  **Assignment Change Patterns:**  **Stability Metrics:** - kept_assignment: Shifts that kept their original worker assignments - remained_unassigned: Shifts that stayed unassigned (no available workers)  **Change Metrics:** - changed_assignment: Assigned shifts that got different workers - lost_assignment: Previously assigned shifts that became unassigned - gained_assignment: Unassigned shifts that got workers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kept_assignment_minutes** | **int** | Total minutes of shifts that kept their original worker assignment. High values indicate scheduling stability with minimal disruption. | 
**changed_assignment_minutes** | **int** | Total minutes of shifts that were reassigned to different workers. | 
**lost_assignment_minutes** | **int** | Total minutes of previously assigned shifts that became unassigned. | 
**remained_unassigned_minutes** | **int** | Total minutes of shifts that stayed unassigned. | 
**gained_assignment_minutes** | **int** | Total minutes of previously unassigned shifts that gained workers. | 

## Example

```python
from pristime_sdk.models.provided_shifts_durations import ProvidedShiftsDurations

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidedShiftsDurations from a JSON string
provided_shifts_durations_instance = ProvidedShiftsDurations.from_json(json)
# print the JSON string representation of the object
print(ProvidedShiftsDurations.to_json())

# convert the object into a dict
provided_shifts_durations_dict = provided_shifts_durations_instance.to_dict()
# create an instance of ProvidedShiftsDurations from a dict
provided_shifts_durations_from_dict = ProvidedShiftsDurations.from_dict(provided_shifts_durations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


