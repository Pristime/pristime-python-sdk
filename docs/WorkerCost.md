# WorkerCost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_hour_of_positive_flextime_balance** | **int** | How much compensation is granted per flex time balance positive hour | [optional] [default to 11]
**per_hour_of_positive_overtime_balance** | **int** | How much compensation is granted per over time balance hour | [optional] [default to 4]
**per_hour_of_unpreferred_period** | **int** | How much cost is incurred for each hour assigned during an unpreferred period | [optional] [default to 2]

## Example

```python
from pristime_sdk.models.worker_cost import WorkerCost

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerCost from a JSON string
worker_cost_instance = WorkerCost.from_json(json)
# print the JSON string representation of the object
print(WorkerCost.to_json())

# convert the object into a dict
worker_cost_dict = worker_cost_instance.to_dict()
# create an instance of WorkerCost from a dict
worker_cost_from_dict = WorkerCost.from_dict(worker_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


