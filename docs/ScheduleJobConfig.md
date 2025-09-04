# ScheduleJobConfig

Configuration settings for the workforce scheduling optimization algorithm.  These settings control how the optimization engine processes your scheduling request, including performance optimizations, solver parameters, and resource allocation. Most users can use the default values for optimal performance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** |  | [optional] 
**webhook_secret** | **str** |  | [optional] 

## Example

```python
from pristime_sdk.models.schedule_job_config import ScheduleJobConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleJobConfig from a JSON string
schedule_job_config_instance = ScheduleJobConfig.from_json(json)
# print the JSON string representation of the object
print(ScheduleJobConfig.to_json())

# convert the object into a dict
schedule_job_config_dict = schedule_job_config_instance.to_dict()
# create an instance of ScheduleJobConfig from a dict
schedule_job_config_from_dict = ScheduleJobConfig.from_dict(schedule_job_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


