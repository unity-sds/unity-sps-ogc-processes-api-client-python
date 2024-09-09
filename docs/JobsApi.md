# unity_sps_ogc_processes_api_python_client.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dismiss_jobs_job_id_delete**](JobsApi.md#dismiss_jobs_job_id_delete) | **DELETE** /jobs/{jobId} | cancel a job execution, remove a finished job
[**get_jobs_jobs_get**](JobsApi.md#get_jobs_jobs_get) | **GET** /jobs | retrieve the list of jobs.
[**get_result_jobs_job_id_results_get**](JobsApi.md#get_result_jobs_job_id_results_get) | **GET** /jobs/{jobId}/results | retrieve the result(s) of a job
[**get_status_jobs_job_id_get**](JobsApi.md#get_status_jobs_job_id_get) | **GET** /jobs/{jobId} | retrieve the status of a job


# **dismiss_jobs_job_id_delete**
> StatusInfo dismiss_jobs_job_id_delete(job_id)

cancel a job execution, remove a finished job

Cancel a job execution and remove it from the jobs list.  For more information, see [Section 14]https://docs.ogc.org/is/18-062r2/18-062r2.html#Dismiss).

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.status_info import StatusInfo
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | local identifier of a job

    try:
        # cancel a job execution, remove a finished job
        api_response = api_instance.dismiss_jobs_job_id_delete(job_id)
        print("The response of JobsApi->dismiss_jobs_job_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->dismiss_jobs_job_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| local identifier of a job |

### Return type

[**StatusInfo**](StatusInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of a job. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_jobs_get**
> JobListInput get_jobs_jobs_get()

retrieve the list of jobs.

Lists available jobs.  For more information, see [Section 12](https://docs.ogc.org/is/18-062r2/18-062r2.html#Job_list).

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.job_list_input import JobListInput
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.JobsApi(api_client)

    try:
        # retrieve the list of jobs.
        api_response = api_instance.get_jobs_jobs_get()
        print("The response of JobsApi->get_jobs_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_jobs_jobs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JobListInput**](JobListInput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of jobs for this process. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_jobs_job_id_results_get**
> Dict[str, InlineOrRefDataInput] get_result_jobs_job_id_results_get(job_id, prefer=prefer)

retrieve the result(s) of a job

Lists available results of a job. In case of a failure, lists exceptions instead.  For more information, see [Section 7.11](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_job_results).

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_input import InlineOrRefDataInput
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | local identifier of a job
    prefer = 'prefer_example' # str | Indicates client preferences, such as whether the client wishes a self-contained or minimal response. A &#x60;return&#x3D;minimal&#x60; preference indicates that the client would prefer that links be returned to larger object to minimize the response payload. A &#x60;return&#x3D;representation&#x60; indicates that the client would prefer if the server can return a self-contained response. (optional)

    try:
        # retrieve the result(s) of a job
        api_response = api_instance.get_result_jobs_job_id_results_get(job_id, prefer=prefer)
        print("The response of JobsApi->get_result_jobs_job_id_results_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_result_jobs_job_id_results_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| local identifier of a job |
 **prefer** | **str**| Indicates client preferences, such as whether the client wishes a self-contained or minimal response. A &amp;#x60;return&amp;#x3D;minimal&amp;#x60; preference indicates that the client would prefer that links be returned to larger object to minimize the response payload. A &amp;#x60;return&amp;#x3D;representation&amp;#x60; indicates that the client would prefer if the server can return a self-contained response. | [optional]

### Return type

[**Dict[str, InlineOrRefDataInput]**](InlineOrRefDataInput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The processing results of a job. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_jobs_job_id_get**
> StatusInfo get_status_jobs_job_id_get(job_id)

retrieve the status of a job

Shows the status of a job.   For more information, see [Section 7.10](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_retrieve_status_info).

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.status_info import StatusInfo
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.JobsApi(api_client)
    job_id = 'job_id_example' # str | local identifier of a job

    try:
        # retrieve the status of a job
        api_response = api_instance.get_status_jobs_job_id_get(job_id)
        print("The response of JobsApi->get_status_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_status_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| local identifier of a job |

### Return type

[**StatusInfo**](StatusInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of a job. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
