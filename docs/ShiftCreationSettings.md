# ShiftCreationSettings

Configuration for automatically creating shifts to fulfill staffing demands.  When a demand cannot be fully satisfied by existing shifts, the system can automatically generate new shifts with these specifications. This is useful for:  - **Dynamic scheduling**: Create shifts on-demand based on actual staffing needs - **Gap filling**: Generate shifts to cover periods with insufficient existing coverage - **Uniform coverage**: Ensure consistent shift characteristics across time periods - **Skill-specific coverage**: Create shifts that require specific worker qualifications  **Important:** All created shifts must be compatible with the parent demand's requirements. For example, if the demand requires shifts with tag \"ICU\", the shift creation settings must include \"ICU\" in their tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone for all automatically created shifts. Should typically match the demand&#39;s timezone and your business location. | 
**break_minutes** | **int** | Duration in minutes for break periods that will be automatically added to created shifts. Breaks are unpaid time subtracted from work hours. | 
**work_duration** | [**WorkDuration**](WorkDuration.md) |  | 
**continuous_work_duration_before_break** | [**ContinuousWorkDurationBeforeBreak**](ContinuousWorkDurationBeforeBreak.md) |  | 
**required_skills** | **List[str]** | Skills, certifications, or qualifications required for workers to be assigned to created shifts. Must be a superset of the demand&#39;s required_skills. | [optional] [default to []]
**tags** | **List[str]** | Descriptive tags that will be applied to all created shifts. Must be a superset of the demand&#39;s required_shift_tags to ensure compatibility. | [optional] [default to []]
**day_boundary_offset_minutes** | **int** | Day boundary adjustment for created shifts, useful for night shift operations. Positive values shift the day end later (e.g., +120 &#x3D; day ends at 2:00 AM). | [optional] [default to 0]

## Example

```python
from pristime_sdk.models.shift_creation_settings import ShiftCreationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftCreationSettings from a JSON string
shift_creation_settings_instance = ShiftCreationSettings.from_json(json)
# print the JSON string representation of the object
print(ShiftCreationSettings.to_json())

# convert the object into a dict
shift_creation_settings_dict = shift_creation_settings_instance.to_dict()
# create an instance of ShiftCreationSettings from a dict
shift_creation_settings_from_dict = ShiftCreationSettings.from_dict(shift_creation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


