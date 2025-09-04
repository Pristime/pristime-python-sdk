# Durations

Complete duration summary of all scheduling changes and new shift creation.  Provides a comprehensive view of how many minutes of work were affected by the optimization, split between modifications to your existing shifts and automatic creation of new shifts to meet demands.  **Total Impact Calculation:** - Changed work = provided.changed_assignment + provided.gained_assignment + provided.lost_assignment - New work = created - Total optimization impact = changed work + new work  **Usage:** - Track optimization effectiveness and coverage improvements - Calculate billing for usage-based pricing models - Estimate communication needs for schedule change notifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provided** | [**ProvidedShiftsDurations**](ProvidedShiftsDurations.md) |  | 
**created** | **int** | Total minutes of new shifts automatically created by the optimization algorithm. These shifts are always assigned to workers and represent additional coverage beyond your original request. | 

## Example

```python
from pristime_sdk.models.durations import Durations

# TODO update the JSON string below
json = "{}"
# create an instance of Durations from a JSON string
durations_instance = Durations.from_json(json)
# print the JSON string representation of the object
print(Durations.to_json())

# convert the object into a dict
durations_dict = durations_instance.to_dict()
# create an instance of Durations from a dict
durations_from_dict = Durations.from_dict(durations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


