# Balance

Tracks accumulated time balances (overtime, flextime) carried forward between scheduling periods.  Balances can be positive (worker has worked more than expected) or negative (worker has worked less than expected). The optimizer considers these balances when making assignments to help achieve fair workload distribution over time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_minutes** | **int** | Current accumulated balance in minutes. Positive &#x3D; worker has worked more than expected, negative &#x3D; worker has worked less than expected. | [optional] [default to 0]
**min_minutes** | **int** | Minimum allowed balance in minutes (smallest value allowed). Prevents excessive time debt to workers. | 
**max_minutes** | **int** | Maximum allowed balance in minutes (largest value allowed). Prevents excessive time debt from workers. | 

## Example

```python
from pristime_sdk.models.balance import Balance

# TODO update the JSON string below
json = "{}"
# create an instance of Balance from a JSON string
balance_instance = Balance.from_json(json)
# print the JSON string representation of the object
print(Balance.to_json())

# convert the object into a dict
balance_dict = balance_instance.to_dict()
# create an instance of Balance from a dict
balance_from_dict = Balance.from_dict(balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


