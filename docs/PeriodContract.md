# PeriodContract

PeriodContract represents the constraints of the contract over a period (usually a week).  **Key Features:** - **Time Limits**: Weekly/monthly hour minimums and maximums - **Day Limits**: How many days can be worked in the period - **Cost Management**: Period-level cost calculations for optimization - **Flextime Tracking**: Accumulated time debt/credit over the period - **Individual Day Rules**: Specific constraints for dates within the period  **Relationship to Daily Rules:** PeriodContract works alongside DayContract - the daily rules must be consistent with the period rules. For example, if weekly max is 40 hours, daily maximums should allow this to be achievable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | First date (inclusive) of the contract period. All period-level rules and limits begin applying from this date. | 
**end_date** | **date** | Last date (inclusive) of the contract period. All period-level rules and limits stop applying after this date. | 
**time_constraints** | [**PeriodTimeConstraints**](PeriodTimeConstraints.md) |  | [optional] 
**day_constraints** | [**PeriodDayConstraints**](PeriodDayConstraints.md) |  | [optional] 
**days** | [**Dict[str, DayContract]**](DayContract.md) |  | [optional] 
**costs** | [**PeriodCosts**](PeriodCosts.md) |  | [optional] 
**flextime_factor** | **int** | Factor by which the flextime is multiplied before being added to the flextime_balance. | [optional] [default to 1]

## Example

```python
from pristime_sdk.models.period_contract import PeriodContract

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodContract from a JSON string
period_contract_instance = PeriodContract.from_json(json)
# print the JSON string representation of the object
print(PeriodContract.to_json())

# convert the object into a dict
period_contract_dict = period_contract_instance.to_dict()
# create an instance of PeriodContract from a dict
period_contract_from_dict = PeriodContract.from_dict(period_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


