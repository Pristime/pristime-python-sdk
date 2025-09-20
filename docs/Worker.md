# Worker

Represents a staff member available for shift assignment in workforce scheduling.  A Worker contains all the information needed to determine shift compatibility and assignment optimality including:  **Key Information:** - Basic identification - Work availability periods (preferred, unpreferred, unavailable times) - Skills and qualifications for matching with shift requirements - Labor constraints (consecutive workdays, break requirements, etc.) - Time balance tracking (overtime, flextime accumulated hours) - Cost and revenue parameters for optimization calculations  **Assignment Compatibility:** The system automatically checks worker-shift compatibility based on: - Skills matching (worker must have all skills required by shift) - Time availability (shift must not overlap unavailable periods) - Work constraints (respect minimum breaks, maximum consecutive days) - Contract limits (daily/weekly hour restrictions)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Your system&#39;s unique identifier for this worker (e.g., employee ID, database primary key). | 
**name** | **str** | Worker&#39;s display name for scheduling interfaces and reports. | 
**min_break_duration** | [**MinBreakDuration**](MinBreakDuration.md) |  | [optional] 
**max_consecutive_workdays** | [**MaxConsecutiveWorkdays**](MaxConsecutiveWorkdays.md) |  | [optional] 
**balances** | [**Balances**](Balances.md) |  | [optional] 
**periods** | [**List[PeriodContract]**](PeriodContract.md) | Contract periods defining work expectations, time limits, and labor rules for different date ranges. | [optional] 
**availability** | [**Availability**](Availability.md) |  | [optional] 
**costs** | [**WorkerCost**](WorkerCost.md) |  | [optional] 
**revenues** | [**WorkerRevenue**](WorkerRevenue.md) |  | [optional] 

## Example

```python
from pristime_sdk.models.worker import Worker

# TODO update the JSON string below
json = "{}"
# create an instance of Worker from a JSON string
worker_instance = Worker.from_json(json)
# print the JSON string representation of the object
print(Worker.to_json())

# convert the object into a dict
worker_dict = worker_instance.to_dict()
# create an instance of Worker from a dict
worker_from_dict = Worker.from_dict(worker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


