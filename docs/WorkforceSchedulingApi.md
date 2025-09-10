# pristime_sdk.WorkforceSchedulingApi

All URIs are relative to *https://pristime.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule_job**](WorkforceSchedulingApi.md#create_schedule_job) | **POST** /api/v2/schedule-jobs | Create Workforce Schedule Optimization Job
[**get_schedule_job**](WorkforceSchedulingApi.md#get_schedule_job) | **GET** /api/v2/schedule-jobs/{job_id} | Get Scheduling Job Status and Results


# **create_schedule_job**
> ScheduleJobResponse create_schedule_job(schedule_state)

Create Workforce Schedule Optimization Job

Initiates an asynchronous workforce scheduling optimization process. Takes workers, shifts, staffing demands, and constraints as input, then runs an optimization algorithm to find optimal shift assignments. Returns immediately with a job ID for tracking progress.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pristime_sdk
from pristime_sdk.models.schedule_job_response import ScheduleJobResponse
from pristime_sdk.models.schedule_state import ScheduleState
from pristime_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pristime.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pristime_sdk.Configuration(
    host = "https://pristime.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = pristime_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pristime_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pristime_sdk.WorkforceSchedulingApi(api_client)
    schedule_state = pristime_sdk.ScheduleState() # ScheduleState | 

    try:
        # Create Workforce Schedule Optimization Job
        api_response = api_instance.create_schedule_job(schedule_state)
        print("The response of WorkforceSchedulingApi->create_schedule_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkforceSchedulingApi->create_schedule_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_state** | [**ScheduleState**](ScheduleState.md)|  | 

### Return type

[**ScheduleJobResponse**](ScheduleJobResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduling job initiated successfully and is now running in the background |  -  |
**401** | Authentication required - Please provide a valid API key in the Authorization header (Bearer token) |  -  |
**403** | Access denied - Your organization needs an active subscription to use scheduling services |  -  |
**422** | Invalid request data - Please check that workers, shifts, demands, and constraints are properly formatted and follow business rules |  -  |
**500** | Server error - An unexpected error occurred while processing your scheduling request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_job**
> ScheduleJobResponse get_schedule_job(job_id)

Get Scheduling Job Status and Results

Retrieves the current status and results of a workforce scheduling optimization job. Returns the job status ('running', 'completed', or 'failed') and optimization results if completed.

### Example

* Bearer Authentication (HTTPBearer):

```python
import pristime_sdk
from pristime_sdk.models.schedule_job_response import ScheduleJobResponse
from pristime_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pristime.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pristime_sdk.Configuration(
    host = "https://pristime.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = pristime_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pristime_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pristime_sdk.WorkforceSchedulingApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get Scheduling Job Status and Results
        api_response = api_instance.get_schedule_job(job_id)
        print("The response of WorkforceSchedulingApi->get_schedule_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkforceSchedulingApi->get_schedule_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**ScheduleJobResponse**](ScheduleJobResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job status and results retrieved successfully |  -  |
**401** | Authentication required - Please provide a valid API key in the Authorization header (Bearer token) |  -  |
**403** | Access denied - Your organization needs an active subscription to use scheduling services |  -  |
**422** | Invalid request data |  -  |
**404** | Scheduling job not found - Please check the job ID is correct |  -  |
**500** | Server error - An unexpected error occurred while retrieving job status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

