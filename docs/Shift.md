# Shift

Represents a work shift that can be assigned to workers during scheduling optimization.  A shift defines a specific time period requiring worker coverage, including timing, location, required skills, break periods, and assignment status. Shifts can be: - **Unassigned**: Need a worker (will be optimally assigned) - **Pre-assigned**: Already have a worker but can be reassigned if beneficial - **Locked**: Have a worker and cannot be changed  **Day Assignment Rules for Night Shifts:** - The entire shift is associated with the day it **starts**, not when it ends - Uses the `day_boundary_offset_minutes` parameter for custom day boundaries - Example: Night shift 22:00 Monday → 06:00 Tuesday is a \"Monday shift\" - Workers with Monday availability can work this shift even if unavailable Tuesday  **Timing Conventions:** - Start time is included, end time is excluded [start_time, end_time) - All times must be whole minutes (no seconds or milliseconds) - Break periods are subtracted from total time to get actual work duration  **Assignment Optimization:** - Skills matching (worker must have all required skills) - Availability checking (no conflicts with unavailable periods) - Cost/revenue optimization (considers worker rates and shift value) - Constraint satisfaction (respects break requirements, consecutive day limits, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_datetime** | **datetime** | Beginning of the time period (inclusive). This exact moment is included in the period. Must be rounded to the nearest minute for scheduling precision. | 
**end_datetime** | **datetime** | End of the time period (exclusive). This exact moment is NOT included in the period, allowing periods to be adjacent without overlap. Must be rounded to the nearest minute. | 
**timezone** | **str** | Timezone for interpreting start_datetime and end_datetime | 
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**revenues** | [**ShiftRevenues**](ShiftRevenues.md) |  | [optional] 
**revenue** | **int** | Additional fixed revenue value for this specific shift, added to calculated hourly revenues. | [optional] [default to 0]
**breaks** | [**List[Period]**](Period.md) | Unpaid break periods during the shift (lunch, rest breaks). Breaks are subtracted from total shift duration to calculate actual work time. Must be entirely within the shift timeframe. | [optional] 
**tags** | **List[str]** | Descriptive labels for the shift type, location, or characteristics. Used to match shifts with demand requirements. | [optional] [default to []]
**required_skills** | **List[str]** | Skills, certifications, or qualifications that a worker must possess to be assigned to this shift. Workers without these skills will be ineligible. | [optional] [default to []]
**assignment** | [**ShiftAssignment**](ShiftAssignment.md) |  | [optional] 
**preceding_shift_id** | **str** |  | [optional] 

## Example

```python
from pristime_sdk.models.shift import Shift

# TODO update the JSON string below
json = "{}"
# create an instance of Shift from a JSON string
shift_instance = Shift.from_json(json)
# print the JSON string representation of the object
print(Shift.to_json())

# convert the object into a dict
shift_dict = shift_instance.to_dict()
# create an instance of Shift from a dict
shift_from_dict = Shift.from_dict(shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


