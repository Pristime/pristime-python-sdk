# WorkerMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_metrics** | [**List[PeriodMetrics]**](PeriodMetrics.md) | Metrics for each period. | 

## Example

```python
from pristime_sdk.models.worker_metrics import WorkerMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of WorkerMetrics from a JSON string
worker_metrics_instance = WorkerMetrics.from_json(json)
# print the JSON string representation of the object
print(WorkerMetrics.to_json())

# convert the object into a dict
worker_metrics_dict = worker_metrics_instance.to_dict()
# create an instance of WorkerMetrics from a dict
worker_metrics_from_dict = WorkerMetrics.from_dict(worker_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


