# ShiftRevenues

Revenue parameters used by the optimization algorithm to prioritize shift assignments.  These values influence which workers get assigned to which shifts by making some assignments more economically attractive than others. Higher revenue shifts will be prioritized for assignment, and continuity bonuses encourage keeping related shifts with the same worker.  **Note:** These are optimization weights, not actual financial amounts. They help the algorithm make better assignment decisions based on business priorities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_assigned_hour** | **int** | Revenue value per work hour for optimization calculations. Higher values make this shift more attractive for assignment. | [optional] [default to 100]
**continuity_revenue** | **int** | Bonus revenue when this shift is assigned to the same worker as its preceding shift. Encourages consistent worker assignment for shift sequences. | [optional] [default to 0]

## Example

```python
from pristime_sdk.models.shift_revenues import ShiftRevenues

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftRevenues from a JSON string
shift_revenues_instance = ShiftRevenues.from_json(json)
# print the JSON string representation of the object
print(ShiftRevenues.to_json())

# convert the object into a dict
shift_revenues_dict = shift_revenues_instance.to_dict()
# create an instance of ShiftRevenues from a dict
shift_revenues_from_dict = ShiftRevenues.from_dict(shift_revenues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


