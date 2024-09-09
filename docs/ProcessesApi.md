# unity_sps_ogc_processes_api_python_client.ProcessesApi

All URIs are relative to *<http://localhost>*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_processes_process_id_execution_post**](ProcessesApi.md#execute_processes_process_id_execution_post) | **POST** /processes/{processId}/execution | execute a process.
[**get_process_description_processes_process_id_get**](ProcessesApi.md#get_process_description_processes_process_id_get) | **GET** /processes/{processId} | retrieve a process description
[**get_processes_processes_get**](ProcessesApi.md#get_processes_processes_get) | **GET** /processes | retrieve the list of available processes

# **execute_processes_process_id_execution_post**
>
> Execute200ResponseInput execute_processes_process_id_execution_post(process_id, response=response, prefer=prefer, execute_workflows=execute_workflows)

execute a process.

Executes a process (this may result in the creation of a job resource e.g., for *asynchronous execution*).  For more information, see [Section 7.9](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_create_job).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.execute200_response_input import Execute200ResponseInput
from unity_sps_ogc_processes_api_python_client.models.execute_workflows import ExecuteWorkflows
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str |
    response = 'response_example' # str | For executing the process using the _Collection Output_ mechanism, where the client is redirected (_303_ status) to either an OGC API landing page or collection resource, from which one or more OGC API data access mechanism is available. Data access requests may trigger processing on-demand for a given area, time and resolution of interest. (optional)
    prefer = 'prefer_example' # str | Indicates client preferences, including whether the client is capable of asynchronous processing. A &#x60;respond-async&#x60; preference indicates a preference for asynchronous processing. A &#x60;wait: &lt;x&gt;s&#x60; preference indicates that the client prefers to wait up to x seconds to receive a reponse synchronously before the server falls back to asynchronous processing. (optional)
    execute_workflows = unity_sps_ogc_processes_api_python_client.ExecuteWorkflows() # ExecuteWorkflows |  (optional)

    try:
        # execute a process.
        api_response = api_instance.execute_processes_process_id_execution_post(process_id, response=response, prefer=prefer, execute_workflows=execute_workflows)
        print("The response of ProcessesApi->execute_processes_process_id_execution_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->execute_processes_process_id_execution_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  |
 **response** | **str**| For executing the process using the *Collection Output* mechanism, where the client is redirected (*303* status) to either an OGC API landing page or collection resource, from which one or more OGC API data access mechanism is available. Data access requests may trigger processing on-demand for a given area, time and resolution of interest. | [optional]
 **prefer** | **str**| Indicates client preferences, including whether the client is capable of asynchronous processing. A &amp;#x60;respond-async&amp;#x60; preference indicates a preference for asynchronous processing. A &amp;#x60;wait: &amp;lt;x&amp;gt;s&amp;#x60; preference indicates that the client prefers to wait up to x seconds to receive a reponse synchronously before the server falls back to asynchronous processing. | [optional]
 **execute_workflows** | [**ExecuteWorkflows**](ExecuteWorkflows.md)|  | [optional]

### Return type

[**Execute200ResponseInput**](Execute200ResponseInput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of synchronous execution |  -  |
**201** | Started asynchronous execution. Created job. |  -  |
**303** | For *Collection Output* execution, redirection to an OGC API landing page or collection. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**422** | Validation Error |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_description_processes_process_id_get**
>
> ProcessInput get_process_description_processes_process_id_get(process_id)

retrieve a process description

The process description contains information about inputs and outputs and a link to the execution-endpoint for the process. The Core does not mandate the use of a specific process description to specify the interface of a process. That said, the Core requirements class makes the following recommendation:  Implementations SHOULD consider supporting the OGC process description.  For more information, see [Section 7.8](https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_description).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.process_input import ProcessInput
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.ProcessesApi(api_client)
    process_id = 'process_id_example' # str |

    try:
        # retrieve a process description
        api_response = api_instance.get_process_description_processes_process_id_get(process_id)
        print("The response of ProcessesApi->get_process_description_processes_process_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->get_process_description_processes_process_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  |

### Return type

[**ProcessInput**](ProcessInput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A process description. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_processes_processes_get**
>
> ProcessListInput get_processes_processes_get()

retrieve the list of available processes

The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process.  For more information, see [Section 7.7]<https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list>).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.process_list_input import ProcessListInput
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.ProcessesApi(api_client)

    try:
        # retrieve the list of available processes
        api_response = api_instance.get_processes_processes_get()
        print("The response of ProcessesApi->get_processes_processes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessesApi->get_processes_processes_get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ProcessListInput**](ProcessListInput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the available processes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
