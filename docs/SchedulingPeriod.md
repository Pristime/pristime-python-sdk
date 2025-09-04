# SchedulingPeriod

Defines the time period and timezone settings for workforce scheduling optimization. The scheduling period establishes the date range during which shift assignments will be optimized.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | First date to include in the scheduling optimization (inclusive). | 
**end_date** | **date** | Last date to include in the scheduling optimization (inclusive). | 
**timezone** | **str** | Primary timezone for the schedule. | 
**day_boundary_offset_minutes** | **int** | Shifts the day boundary for night shift scheduling. Positive values (e.g., +120) move the day end to 02:00, so shifts starting before 02:00 belong to the previous calendar day. Useful for 24/7 operations. | [optional] [default to 0]

## Example

```python
from pristime_sdk.models.scheduling_period import SchedulingPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingPeriod from a JSON string
scheduling_period_instance = SchedulingPeriod.from_json(json)
# print the JSON string representation of the object
print(SchedulingPeriod.to_json())

# convert the object into a dict
scheduling_period_dict = scheduling_period_instance.to_dict()
# create an instance of SchedulingPeriod from a dict
scheduling_period_from_dict = SchedulingPeriod.from_dict(scheduling_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


