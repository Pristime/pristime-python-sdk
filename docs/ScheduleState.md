# ScheduleState

Complete workforce scheduling optimization request.  This is the main payload for scheduling jobs, containing all the information needed to optimize shift assignments across your workforce. The optimization engine will assign shifts to workers while respecting availability, skills, labor constraints, and business rules to meet staffing demands efficiently.  **Typical Workflow:** 1. Define the scheduling period and timezone 2. Add your workers with their availability and skills 3. Add shifts to be assigned (existing or new) 4. Specify staffing demands (how many workers needed when) 5. Add any custom constraints 6. Submit for optimization 7. Receive optimized shift assignments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduling_period** | [**SchedulingPeriod**](SchedulingPeriod.md) |  | 
**workers** | [**List[Worker]**](Worker.md) | Your staff members available for shift assignment. Include their availability, skills, work constraints, and contract details. | [optional] 
**shifts** | [**List[Shift]**](Shift.md) | Work shifts to be optimized. Can include assigned and unassigned shifts. | [optional] 
**demands** | [**List[Demand]**](Demand.md) | Staffing requirements over time - specify how many workers with certain skills you need at different times. | [optional] 
**config** | [**ScheduleJobConfig**](ScheduleJobConfig.md) |  | [optional] 

## Example

```python
from pristime_sdk.models.schedule_state import ScheduleState

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleState from a JSON string
schedule_state_instance = ScheduleState.from_json(json)
# print the JSON string representation of the object
print(ScheduleState.to_json())

# convert the object into a dict
schedule_state_dict = schedule_state_instance.to_dict()
# create an instance of ScheduleState from a dict
schedule_state_from_dict = ScheduleState.from_dict(schedule_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


