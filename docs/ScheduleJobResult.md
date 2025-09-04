# ScheduleJobResult

Complete results from workforce scheduling optimization containing all assignments, metrics, and analysis.  This is the core result object containing everything you need to understand and implement the optimized schedule. It provides the assignment decisions, performance metrics, constraint violations, and operational statistics from the optimization process.  **Key Components:**  **Schedule Results:** - shifts: All shift assignments (both your provided shifts and newly created ones) - durations: Time-based summary of schedule changes and impact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shifts** | [**Shifts**](Shifts.md) |  | 
**durations** | [**Durations**](Durations.md) |  | 
**metrics** | [**Metrics**](Metrics.md) |  | [optional] 
**broken_constraints** | [**BrokenConstraints**](BrokenConstraints.md) |  | [optional] 

## Example

```python
from pristime_sdk.models.schedule_job_result import ScheduleJobResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleJobResult from a JSON string
schedule_job_result_instance = ScheduleJobResult.from_json(json)
# print the JSON string representation of the object
print(ScheduleJobResult.to_json())

# convert the object into a dict
schedule_job_result_dict = schedule_job_result_instance.to_dict()
# create an instance of ScheduleJobResult from a dict
schedule_job_result_from_dict = ScheduleJobResult.from_dict(schedule_job_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


