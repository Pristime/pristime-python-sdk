# pristime_sdk.HealthApi

All URIs are relative to *https://pristime.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthApi.md#health_check) | **GET** /api/health | Read Health


# **health_check**
> Response health_check()

Read Health

### Example


```python
import pristime_sdk
from pristime_sdk.models.response import Response
from pristime_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pristime.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pristime_sdk.Configuration(
    host = "https://pristime.com"
)


# Enter a context with an instance of the API client
with pristime_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pristime_sdk.HealthApi(api_client)

    try:
        # Read Health
        api_response = api_instance.health_check()
        print("The response of HealthApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

