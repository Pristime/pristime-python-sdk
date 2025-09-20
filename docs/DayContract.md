# DayContract

Complete daily contract configuration for a worker on a specific date.  This is the primary class for defining how a worker can be scheduled on any given day. It combines time constraints and cost parameters to provide a complete picture of the worker's daily contract obligations and limitations.  **Main Components:** - **Time Constraints**: Daily hour limits and requirements (min/max work time, overtime, PTO) - **Cost Parameters**: How different types of time affect optimization calculations - **Policy Settings**: Rules for combining different time types (overtime + PTO, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_constraints** | [**DayTimeConstraints**](DayTimeConstraints.md) |  | 
**allow** | [**DayAllow**](DayAllow.md) |  | [optional] 
**costs** | [**DayCosts**](DayCosts.md) |  | [optional] 
**overtime_factor** | **int** | Multiplier applied to overtime hours before adding to the worker&#39;s overtime balance. Values &gt;1 accumulate overtime debt faster. | [optional] [default to 1]

## Example

```python
from pristime_sdk.models.day_contract import DayContract

# TODO update the JSON string below
json = "{}"
# create an instance of DayContract from a JSON string
day_contract_instance = DayContract.from_json(json)
# print the JSON string representation of the object
print(DayContract.to_json())

# convert the object into a dict
day_contract_dict = day_contract_instance.to_dict()
# create an instance of DayContract from a dict
day_contract_from_dict = DayContract.from_dict(day_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


