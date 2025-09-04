# Shifts

Complete collection of shifts after workforce scheduling optimization.  Organizes all shifts into two categories: those you provided in your request and those created automatically by the optimization algorithm to meet demands.  **Shift Categories:**  **Provided Shifts**: Existing shifts from your request - May have new worker assignments (optimized) - May remain unassigned if no suitable worker available - Tracked by your original shift IDs for easy mapping  **Created Shifts**: New shifts generated automatically - Created when demands exceed available provided shifts - Always assigned to workers (unassigned shifts aren't created) - Have new system-generated IDs  **Usage:** - Update your system with new assignments from 'provided' - Add the 'created' shifts as new schedule entries - Use shift IDs to map results back to your original data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provided** | [**Dict[str, ShiftAssignmentResult]**](ShiftAssignmentResult.md) | Assignment results for shifts you provided in the request, keyed by your original shift IDs. Shows which worker (if any) is now assigned to each existing shift. | 
**created** | [**List[Shift]**](Shift.md) | New shifts automatically created by the optimization algorithm to meet staffing demands. These are additional shifts beyond what you originally provided, always with assigned workers. | 

## Example

```python
from pristime_sdk.models.shifts import Shifts

# TODO update the JSON string below
json = "{}"
# create an instance of Shifts from a JSON string
shifts_instance = Shifts.from_json(json)
# print the JSON string representation of the object
print(Shifts.to_json())

# convert the object into a dict
shifts_dict = shifts_instance.to_dict()
# create an instance of Shifts from a dict
shifts_from_dict = Shifts.from_dict(shifts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


