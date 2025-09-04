# WorkerRevenue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_hour_of_negative_flextime_balance** | **int** | How much revenue is earned at the end of the period for each flex time balance negative hour | [optional] [default to 10]
**per_hour_of_pto** | **int** | How much revenue is earned for each pto time hour | [optional] [default to 1000]
**per_hour_of_preferred_period** | **int** | How much revenue is earned for each hour assigned during a preferred period | [optional] [default to 5]
**per_hour_of_skilled_work** | **Dict[str, int]** | Extra revenue per skill in euros per hour.         These skills are also used to determine the compatibility with shifts (shift.required_skills) and demands (demand.required_skills). | [optional] 
**per_hour_of_tagged_work** | **Dict[str, int]** | Extra revenue per tagged work in euros per hour.         This revenue is used to make the assignment fairer towards workers that are lagging behind in the number of shifts with a specific tag. | [optional] 

## Example

```python
from pristime_sdk.models.worker_revenue import WorkerRevenue

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerRevenue from a JSON string
worker_revenue_instance = WorkerRevenue.from_json(json)
# print the JSON string representation of the object
print(WorkerRevenue.to_json())

# convert the object into a dict
worker_revenue_dict = worker_revenue_instance.to_dict()
# create an instance of WorkerRevenue from a dict
worker_revenue_from_dict = WorkerRevenue.from_dict(worker_revenue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


