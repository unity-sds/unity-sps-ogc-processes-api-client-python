# unity_sps_ogc_processes_api_python_client.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_health_get**](HealthApi.md#get_health_health_get) | **GET** /health | Retrieve the health status of the API.


# **get_health_health_get**
> HealthCheck get_health_health_get()

Retrieve the health status of the API.

Retrieves the health status of the API.

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.health_check import HealthCheck
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
    api_instance = unity_sps_ogc_processes_api_python_client.HealthApi(api_client)

    try:
        # Retrieve the health status of the API.
        api_response = api_instance.get_health_health_get()
        print("The response of HealthApi->get_health_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_health_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheck**](HealthCheck.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The health status of the API. |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
