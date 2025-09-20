# MaxConsecutiveWorkdays

Limits consecutive working days to prevent worker fatigue and ensure adequate rest periods.  **Two-tier system:** - **Preferred maximum**: Soft constraint - optimizer tries to respect this limit but can exceed if necessary - **Absolute maximum**: Hard constraint - optimizer will never exceed this limit under any circumstances  Common patterns: - 5 preferred, 6 absolute: Standard Monday-Friday with weekend flexibility - 3 preferred, 5 absolute: Part-time workers with occasional full-time coverage - 6 preferred, 7 absolute: Full-time workers in 24/7 operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute** | **int** |  | [optional] 
**preferred** | **int** |  | [optional] 

## Example

```python
from pristime_sdk.models.max_consecutive_workdays import MaxConsecutiveWorkdays

# TODO update the JSON string below
json = "{}"
# create an instance of MaxConsecutiveWorkdays from a JSON string
max_consecutive_workdays_instance = MaxConsecutiveWorkdays.from_json(json)
# print the JSON string representation of the object
print(MaxConsecutiveWorkdays.to_json())

# convert the object into a dict
max_consecutive_workdays_dict = max_consecutive_workdays_instance.to_dict()
# create an instance of MaxConsecutiveWorkdays from a dict
max_consecutive_workdays_from_dict = MaxConsecutiveWorkdays.from_dict(max_consecutive_workdays_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


