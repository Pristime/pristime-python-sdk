# Demand

Represents staffing requirements that need to be met during scheduling optimization.  A demand specifies: - **When**: Time periods requiring staff coverage (via time_series) - **How many**: Number of workers needed at each time point - **What skills**: Required qualifications for workers and shifts - **How to fulfill**: Optional shift creation settings for automatic coverage  **Time Series Format:** Demands use a time series to specify changing staffing needs over time. Each entry represents a change point where the required staffing level changes. Example: {9:00 AM: 3, 1:00 PM: 2, 5:00 PM: 0} means: - 3 workers needed from 9:00 AM to 1:00 PM - 2 workers needed from 1:00 PM to 5:00 PM - 0 workers needed after 5:00 PM  **Automatic Shift Creation:** When shift_creation_settings are provided, the system can automatically generate shifts to meet this demand if existing shifts are insufficient.  **Revenue Optimization:** Demand fulfillment generates revenue in the optimization algorithm, encouraging the system to prioritize meeting high-value staffing requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Your system&#39;s unique identifier for this demand (e.g., department ID, location ID, event ID). | 
**timezone** | **str** | Timezone for interpreting the demand time series and any automatically created shifts. Should match your local business timezone. | 
**required_skills** | **List[str]** | Skills, certifications, or qualifications that workers must possess to fulfill this demand. Only workers with all these skills will be considered. | 
**required_tags** | **List[str]** | Tags that shifts must have to count toward fulfilling this demand. Useful for matching specific shift types, locations, or characteristics. | 
**label** | **str** |  | [optional] 
**time_series** | **Dict[str, float]** | Staffing level requirements over time as change points. Each entry specifies when the required number of workers changes. Format: {timestamp: worker_count}. The last entry must be 0 to indicate demand end. | [optional] 
**upper_limit_increment** | **int** |  | [optional] 
**revenues** | **object** |  | [optional] 
**shift_creation_settings** | [**ShiftCreationSettings**](ShiftCreationSettings.md) |  | [optional] 

## Example

```python
from pristime_sdk.models.demand import Demand

# TODO update the JSON string below
json = "{}"
# create an instance of Demand from a JSON string
demand_instance = Demand.from_json(json)
# print the JSON string representation of the object
print(Demand.to_json())

# convert the object into a dict
demand_dict = demand_instance.to_dict()
# create an instance of Demand from a dict
demand_from_dict = Demand.from_dict(demand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


