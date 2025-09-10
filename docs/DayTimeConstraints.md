# DayTimeConstraints

Daily time constraints and limits for a worker's contract.  This class defines the rules and boundaries for how much time a worker can work on a specific date. It sets both minimum requirements (guarantees) and maximum limits (to prevent overwork and comply with labor regulations).  **Key Constraint Types:** - **Contractual Time**: The standard daily hours for flextime calculations - **Expected Time**: Minimum guaranteed hours (worker gets paid even if no work) - **Assigned Time**: Limits on actual productive work hours - **Overtime**: Extra hours beyond regular time, often at premium pay rates - **Scheduled Time**: Total time including work, PTO, and recovery time  **Common Patterns:** - Full-time: 8 hours expected, up to 10 hours total (2 hours overtime max) - Part-time: 4 hours expected, up to 6 hours total - On-call: 0 hours expected, up to 12 hours available

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contractual_time_minutes** | **int** |  | [optional] 
**min_expected_time_minutes** | **int** | Minimum guaranteed hours in minutes the worker must be paid for on this date if they&#39;re scheduled at all. | [optional] [default to 0]
**max_expected_time_minutes** | **int** | Maximum hours in minutes the worker is expected to work on this date before it becomes overtime. Sets the boundary for regular vs overtime pay. | [optional] [default to 0]
**max_overtime_minutes** | **int** | Maximum overtime hours in minutes allowed on this date. | [optional] [default to 1440]
**min_assigned_time_minutes** | **int** | Minimum productive work time in minutes that must be assigned if the worker is scheduled. | [optional] [default to 0]
**max_assigned_time_minutes** | **int** | Maximum productive work time in minutes that can be assigned on this date. Limits actual working time regardless of total scheduled time. | [optional] [default to 1440]
**max_recovered_time_minutes** | **int** | Maximum overtime recovery time in minutes that can be taken on this date. | [optional] [default to 1440]
**max_pto_time_minutes** | **int** | Maximum paid time off minutes (vacation, sick leave) that can be taken on this date. | [optional] [default to 0]
**max_scheduled_time_minutes** | **int** | Maximum total scheduled minutes on this date including work (assigned time), PTO, and recovery time. Sets overall daily time limit regardless of activity type. | 

## Example

```python
from pristime_sdk.models.day_time_constraints import DayTimeConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of DayTimeConstraints from a JSON string
day_time_constraints_instance = DayTimeConstraints.from_json(json)
# print the JSON string representation of the object
print(DayTimeConstraints.to_json())

# convert the object into a dict
day_time_constraints_dict = day_time_constraints_instance.to_dict()
# create an instance of DayTimeConstraints from a dict
day_time_constraints_from_dict = DayTimeConstraints.from_dict(day_time_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


