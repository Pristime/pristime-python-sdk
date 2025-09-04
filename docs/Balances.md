# Balances

Container for all time balance tracking for a worker.  Helps ensure fair workload distribution across scheduling periods by carrying forward accumulated overtime and flextime balances.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overtime_balance** | [**Balance**](Balance.md) |  | 
**flextime_balance** | [**Balance**](Balance.md) |  | 

## Example

```python
from pristime_sdk.models.balances import Balances

# TODO update the JSON string below
json = "{}"
# create an instance of Balances from a JSON string
balances_instance = Balances.from_json(json)
# print the JSON string representation of the object
print(Balances.to_json())

# convert the object into a dict
balances_dict = balances_instance.to_dict()
# create an instance of Balances from a dict
balances_from_dict = Balances.from_dict(balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


