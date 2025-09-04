# Constraint

Custom business rule that limits which shifts can be assigned to which workers.  Constraints allow you to enforce specific business requirements that go beyond the basic availability and skills matching. They work by limiting the total number of shifts that can be assigned from a specific set to a specific group of workers.  **Common Use Cases:** - **Exclusive assignments**: Ensure only one worker from a group can be assigned to critical shifts - **Load balancing**: Distribute high-demand shifts fairly across qualified workers - **Specialization limits**: Prevent workers from being over-assigned to specialized roles - **Cross-training**: Ensure multiple workers can cover important shift types - **Conflict resolution**: Handle situations where certain workers shouldn't work together  **How it works:** The constraint specifies a maximum number of shifts from `caller_shift_ids` that can be assigned to workers in `caller_worker_ids`. For example, with max_assigned=1: - Only 1 of the specified shifts can be assigned to any of the specified workers - This could ensure exclusive coverage or prevent resource conflicts  **Example:** To ensure only one supervisor works weekend nights: - caller_shift_ids: [weekend_night_shift_1, weekend_night_shift_2] - caller_worker_ids: [supervisor_alice, supervisor_bob] - max_assigned: 1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller_shift_ids** | **List[str]** | List of shift IDs that this constraint applies to. These are the shifts that will be limited in their assignment to the specified workers. | [optional] [default to []]
**caller_worker_ids** | **List[str]** | List of worker IDs that this constraint applies to. These are the workers who are subject to the assignment limitation for the specified shifts. | [optional] [default to []]
**max_assigned** | **int** | Maximum number of shifts (from caller_shift_ids) that can be assigned to any combination of workers (from caller_worker_ids). Use 1 for exclusive assignment, higher numbers for load distribution. | [optional] [default to 1]

## Example

```python
from pristime_sdk.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print(Constraint.to_json())

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_from_dict = Constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


