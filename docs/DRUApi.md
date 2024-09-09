# unity_sps_ogc_processes_api_python_client.DRUApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_processes_post**](DRUApi.md#deploy_processes_post) | **POST** /processes | deploy a process.
[**replace_processes_process_id_put**](DRUApi.md#replace_processes_process_id_put) | **PUT** /processes/{processId} | replace a process.
[**undeploy_processes_process_id_delete**](DRUApi.md#undeploy_processes_process_id_delete) | **DELETE** /processes/{processId} | undeploy a process.


# **deploy_processes_post**
> object deploy_processes_post(w=w, ogcapppkg=ogcapppkg)

deploy a process.

Deploys a process.  For more information, see [Section 6.3](http://docs.ogc.org/DRAFTS/20-044.html#_87a6983e-d060-458c-95ab-27e232e64822).

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg import Ogcapppkg
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
    api_instance = unity_sps_ogc_processes_api_python_client.DRUApi(api_client)
    w = 'w_example' # str | Point to the workflow identifier for deploying a CWL containing multiple workflow definitions (optional)
    ogcapppkg = unity_sps_ogc_processes_api_python_client.Ogcapppkg() # Ogcapppkg |  (optional)

    try:
        # deploy a process.
        api_response = api_instance.deploy_processes_post(w=w, ogcapppkg=ogcapppkg)
        print("The response of DRUApi->deploy_processes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DRUApi->deploy_processes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **w** | **str**| Point to the workflow identifier for deploying a CWL containing multiple workflow definitions | [optional]
 **ogcapppkg** | [**Ogcapppkg**](Ogcapppkg.md)|  | [optional]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**201** | Created |  -  |
**403** | the processes is not mutable |  -  |
**409** | the processes being added is already deployed (i.e. duplicate) |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_processes_process_id_put**
> object replace_processes_process_id_put(process_id, ogcapppkg=ogcapppkg)

replace a process.

Replaces a process.  For more information, see [Section 6.4](http://docs.ogc.org/DRAFTS/20-044.html#_18582f42-ebc6-4284-9333-c089068f62b6).

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg import Ogcapppkg
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
    api_instance = unity_sps_ogc_processes_api_python_client.DRUApi(api_client)
    process_id = 'process_id_example' # str |
    ogcapppkg = unity_sps_ogc_processes_api_python_client.Ogcapppkg() # Ogcapppkg |  (optional)

    try:
        # replace a process.
        api_response = api_instance.replace_processes_process_id_put(process_id, ogcapppkg=ogcapppkg)
        print("The response of DRUApi->replace_processes_process_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DRUApi->replace_processes_process_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  |
 **ogcapppkg** | [**Ogcapppkg**](Ogcapppkg.md)|  | [optional]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**204** | successful operation (no response body) |  -  |
**403** | the processes is not mutable |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**409** | the processes being added is already deployed (i.e. duplicate) |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undeploy_processes_process_id_delete**
> object undeploy_processes_process_id_delete(process_id, force=force)

undeploy a process.

Undeploys a process. For more information, see [Section 6.5](http://docs.ogc.org/DRAFTS/20-044.html#_16391f9e-538f-4a84-9710-72a6bab82842).

### Example


```python
import unity_sps_ogc_processes_api_python_client
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
    api_instance = unity_sps_ogc_processes_api_python_client.DRUApi(api_client)
    process_id = 'process_id_example' # str |
    force = False # bool | Force undeployment even if there are active DAG runs (optional) (default to False)

    try:
        # undeploy a process.
        api_response = api_instance.undeploy_processes_process_id_delete(process_id, force=force)
        print("The response of DRUApi->undeploy_processes_process_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DRUApi->undeploy_processes_process_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**|  |
 **force** | **bool**| Force undeployment even if there are active DAG runs | [optional] [default to False]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**204** | successful operation (no response body) |  -  |
**403** | the processes is not mutable |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**409** | The process has active DAG runs and force is not set to true. |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
