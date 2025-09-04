# Period

A time period with start and end datetimes, fundamental to workforce scheduling operations.  This class represents any time interval in the scheduling system and is used throughout for shifts, availability windows, breaks, PTO periods, and demands. It provides essential time manipulation methods for scheduling optimization.  **Critical Timing Convention - Half-Open Intervals:** - The start_datetime is **included** and the end_datetime is **excluded** [start, end) - This prevents overlaps and gaps when periods are adjacent - Example: Shift 10:00-18:00 includes 10:00:00 but excludes 18:00:00 exactly - Adjacent periods: 09:00-12:00 and 12:00-17:00 have no overlap or gap  **Common Usage in Scheduling:** - **Work Shifts**: Define when a worker is scheduled to work - **Availability**: When a worker is available for assignment - **Breaks**: Unpaid periods within shifts (subtracted from work time)  **Time Precision Rules:** - All datetimes must be whole minutes (seconds=0, microseconds=0)  **Key Features:** - Overlap detection and calculation - Period subtraction (for break handling) - Containment checking (worker availability vs. shift times) - Duration calculation in minutes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_datetime** | **datetime** | Beginning of the time period (inclusive). This exact moment is included in the period. Must be rounded to the nearest minute for scheduling precision. | 
**end_datetime** | **datetime** | End of the time period (exclusive). This exact moment is NOT included in the period, allowing periods to be adjacent without overlap. Must be rounded to the nearest minute. | 

## Example

```python
from pristime_sdk.models.period import Period

# TODO update the JSON string below
json = "{}"
# create an instance of Period from a JSON string
period_instance = Period.from_json(json)
# print the JSON string representation of the object
print(Period.to_json())

# convert the object into a dict
period_dict = period_instance.to_dict()
# create an instance of Period from a dict
period_from_dict = Period.from_dict(period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


