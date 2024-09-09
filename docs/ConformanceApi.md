# unity_sps_ogc_processes_api_python_client.ConformanceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conformance_conformance_get**](ConformanceApi.md#get_conformance_conformance_get) | **GET** /conformance | Retrieve the set of OGC API conformance classes that are supported by this service.


# **get_conformance_conformance_get**
> ConfClasses get_conformance_conformance_get(f=f)

Retrieve the set of OGC API conformance classes that are supported by this service.

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.conf_classes import ConfClasses
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
    api_instance = unity_sps_ogc_processes_api_python_client.ConformanceApi(api_client)
    f = 'f_example' # str | The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &#39;json&#39; or &#39;html&#39;. (optional)

    try:
        # Retrieve the set of OGC API conformance classes that are supported by this service.
        api_response = api_instance.get_conformance_conformance_get(f=f)
        print("The response of ConformanceApi->get_conformance_conformance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConformanceApi->get_conformance_conformance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f** | **str**| The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &amp;#39;json&amp;#39; or &amp;#39;html&amp;#39;. | [optional]

### Return type

[**ConfClasses**](ConfClasses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URIs of all conformance classes supported by the server  To support \\&amp;quot;generic\\&amp;quot; clients that want to access multiple OGC API - Processes implementations - and not \\&amp;quot;just\\&amp;quot; a specific API / server, the server declares the conformance classes it implements and conforms to. |  -  |
**406** | Content negotiation failed. For example, the &amp;#x60;Accept&amp;#x60; header submitted in the request did not support any of the media types supported by the server for the requested resource. |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
