# DayMetrics

Tracks actual time worked and contract fulfillment for a specific date.  This class contains the actual values that result from scheduling decisions, as opposed to the constraints and limits defined elsewhere. It tracks both worker-level metrics (when they worked) and contract-level metrics (how contract obligations were met).  **Key Concepts:** - **Expected Time**: Hours the worker is contracted to work (paid regardless) - **Overtime**: Hours worked beyond the expected/standard time - **Assigned Time**: Actual hours assigned to shifts - **Flextime**: Difference between contracted and actual hours (can be positive or negative) - **Active Day**: Any day where the worker has time obligations (expected or overtime)  **Usage:** Set values to None where no tracking is needed for that metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_datetime** | **datetime** |  | [optional] 
**end_datetime** | **datetime** |  | [optional] 
**idle_time_minutes** | **int** |  | [optional] 
**has_exceeded_preferred_max_consecutive_workdays_limit** | **bool** |  | [optional] 
**has_scheduled_time** | **bool** |  | [optional] 
**has_expected_time** | **bool** |  | [optional] 
**has_overtime** | **bool** |  | [optional] 
**has_assigned_time** | **bool** |  | [optional] 
**has_max_expected_time_reached** | **bool** |  | [optional] 
**has_any_max_expected_reached** | **bool** |  | [optional] 
**expected_time_minutes** | **int** |  | [optional] 
**overtime_minutes** | **int** |  | [optional] 
**assigned_time_minutes** | **int** |  | [optional] 
**recovered_time_minutes** | **int** |  | [optional] 
**pto_time_minutes** | **int** |  | [optional] 
**flextime_negative_minutes** | **int** |  | [optional] 
**flextime_positive_minutes** | **int** |  | [optional] 
**overtime_balance_minutes** | **int** |  | [optional] 

## Example

```python
from pristime_sdk.models.day_metrics import DayMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of DayMetrics from a JSON string
day_metrics_instance = DayMetrics.from_json(json)
# print the JSON string representation of the object
print(DayMetrics.to_json())

# convert the object into a dict
day_metrics_dict = day_metrics_instance.to_dict()
# create an instance of DayMetrics from a dict
day_metrics_from_dict = DayMetrics.from_dict(day_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


