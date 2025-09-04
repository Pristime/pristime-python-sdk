# ScheduleJobResponse

API response wrapper for workforce scheduling optimization jobs.  This is the top-level response object returned by both synchronous and asynchronous scheduling endpoints. It provides job tracking information and contains the complete optimization results when processing is complete.  **Response Structure:**  **Job Information:** - schedule_job_id: Unique identifier for tracking the job - status: Current job state (running, completed, failed) - message: Human-readable status updates or error information  **Optimization Results:** - result: Complete scheduling results (only present when status='completed')  **Status Values:** - **'running'**: Job is still processing (async jobs only) - **'completed'**: Job finished successfully, results available - **'failed'**: Job encountered an error, check message for details  **Usage Patterns:**  **Asynchronous Jobs** (POST /schedule-jobs, GET /schedule-jobs/{id}): - POST returns immediately with status='running' and job ID - Use GET to poll for completion and retrieve results - Recommended for production workloads  **Error Handling:** - Check status before processing results - Use message for error details when status='failed'

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_job_id** | **str** | Unique identifier for this scheduling job. Use this ID to track job progress and retrieve results via GET /schedule-jobs/{id}. | 
**status** | **str** | Current job status: &#39;running&#39; (still processing), &#39;completed&#39; (finished successfully), or &#39;failed&#39; (encountered error). | 
**message** | **str** |  | [optional] 
**result** | [**ScheduleJobResult**](ScheduleJobResult.md) |  | [optional] 

## Example

```python
from pristime_sdk.models.schedule_job_response import ScheduleJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleJobResponse from a JSON string
schedule_job_response_instance = ScheduleJobResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleJobResponse.to_json())

# convert the object into a dict
schedule_job_response_dict = schedule_job_response_instance.to_dict()
# create an instance of ScheduleJobResponse from a dict
schedule_job_response_from_dict = ScheduleJobResponse.from_dict(schedule_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


