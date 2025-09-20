# PeriodMetrics

Time tracking for a worker over a specific period, and flextime balance at the end of the period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** |  | 
**end_date** | **date** |  | 
**day_metrics** | [**Dict[str, DayMetrics]**](DayMetrics.md) |  | 
**expected_time_minutes** | **int** |  | [optional] 
**overtime_minutes** | **int** |  | [optional] 
**assigned_time_minutes** | **int** |  | [optional] 
**recovered_time_minutes** | **int** |  | [optional] 
**pto_time_minutes** | **int** |  | [optional] 
**flextime_negative_minutes** | **int** |  | [optional] 
**flextime_positive_minutes** | **int** |  | [optional] 
**flextime_balance_minutes** | **int** |  | [optional] 
**scheduled_days** | **int** |  | [optional] 
**expected_days** | **int** |  | [optional] 

## Example

```python
from pristime_sdk.models.period_metrics import PeriodMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodMetrics from a JSON string
period_metrics_instance = PeriodMetrics.from_json(json)
# print the JSON string representation of the object
print(PeriodMetrics.to_json())

# convert the object into a dict
period_metrics_dict = period_metrics_instance.to_dict()
# create an instance of PeriodMetrics from a dict
period_metrics_from_dict = PeriodMetrics.from_dict(period_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


