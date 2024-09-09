# unity_sps_ogc_processes_api_python_client.APIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_api_get**](APIApi.md#get_api_api_get) | **GET** /api | Retrieve this API definition.
[**get_api_processes_api_processes_list_get**](APIApi.md#get_api_processes_api_processes_list_get) | **GET** /api/processes-list | Retrieve the list of processes available from this API implementation &amp;amp; deployment.


# **get_api_api_get**
> object get_api_api_get(f=f)

Retrieve this API definition.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unity_sps_ogc_processes_api_python_client
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
    api_instance = unity_sps_ogc_processes_api_python_client.APIApi(api_client)
    f = 'f_example' # str | The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &#39;json&#39; or &#39;html&#39;. (optional)

    try:
        # Retrieve this API definition.
        api_response = api_instance.get_api_api_get(f=f)
        print("The response of APIApi->get_api_api_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->get_api_api_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f** | **str**| The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &amp;#39;json&amp;#39; or &amp;#39;html&amp;#39;. | [optional]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpenAPI definition of the API. |  -  |
**406** | Content negotiation failed. For example, the &amp;#x60;Accept&amp;#x60; header submitted in the request did not support any of the media types supported by the server for the requested resource. |  -  |
**422** | Validation Error |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_processes_api_processes_list_get**
> Enumeration get_api_processes_api_processes_list_get(f=f)

Retrieve the list of processes available from this API implementation &amp; deployment.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.enumeration import Enumeration
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
    api_instance = unity_sps_ogc_processes_api_python_client.APIApi(api_client)
    f = 'f_example' # str | The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &#39;json&#39; or &#39;html&#39;. (optional)

    try:
        # Retrieve the list of processes available from this API implementation &amp; deployment.
        api_response = api_instance.get_api_processes_api_processes_list_get(f=f)
        print("The response of APIApi->get_api_processes_api_processes_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIApi->get_api_processes_api_processes_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f** | **str**| The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &amp;#39;json&amp;#39; or &amp;#39;html&amp;#39;. | [optional]

### Return type

[**Enumeration**](Enumeration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An enumerated list of valid string values for API parameters. |  -  |
**404** | The requested resource does not exist on the server. For example, a path parameter had an incorrect value. |  -  |
**406** | Content negotiation failed. For example, the &amp;#x60;Accept&amp;#x60; header submitted in the request did not support any of the media types supported by the server for the requested resource. |  -  |
**422** | Validation Error |  -  |
**500** | A server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
