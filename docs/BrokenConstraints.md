# BrokenConstraints

Tracks constraint violations that occurred during workforce scheduling optimization.  When the optimization algorithm cannot perfectly satisfy all constraints (worker availability, labor regulations, business rules), it uses 'slack variables' to find the best possible solution. This class reports which constraints were relaxed and by how much.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** | List of soft constraint violations. These are less critical violations of preferences or flexible rules that were relaxed to find a feasible solution. | [optional] 
**errors** | **List[str]** | List of hard constraint violations. These are serious violations that prevented the optimization from finding a feasible solution. | [optional] 

## Example

```python
from pristime_sdk.models.broken_constraints import BrokenConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of BrokenConstraints from a JSON string
broken_constraints_instance = BrokenConstraints.from_json(json)
# print the JSON string representation of the object
print(BrokenConstraints.to_json())

# convert the object into a dict
broken_constraints_dict = broken_constraints_instance.to_dict()
# create an instance of BrokenConstraints from a dict
broken_constraints_from_dict = BrokenConstraints.from_dict(broken_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


