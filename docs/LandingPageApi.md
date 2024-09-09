# unity_sps_ogc_processes_api_python_client.LandingPageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_landing_page_get**](LandingPageApi.md#get_landing_page_get) | **GET** / | Retrieve the OGC API landing page for this service.


# **get_landing_page_get**
> LandingPage get_landing_page_get(f=f)

Retrieve the OGC API landing page for this service.

### Example


```python
import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.models.landing_page import LandingPage
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
    api_instance = unity_sps_ogc_processes_api_python_client.LandingPageApi(api_client)
    f = 'f_example' # str | The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &#39;json&#39; or &#39;html&#39;. (optional)

    try:
        # Retrieve the OGC API landing page for this service.
        api_response = api_instance.get_landing_page_get(f=f)
        print("The response of LandingPageApi->get_landing_page_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LandingPageApi->get_landing_page_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f** | **str**| The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &amp;#39;json&amp;#39; or &amp;#39;html&amp;#39;. | [optional]

### Return type

[**LandingPage**](LandingPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The landing page provides links to the API definition (link relation &amp;#x60;service-desc&amp;#x60;, in this case path &amp;#x60;/api&amp;#x60;), to the Conformance declaration (path &amp;#x60;/conformance&amp;#x60;, link relation &amp;#x60;http://www.opengis.net/def/rel/ogc/1.0/conformance&amp;#x60;), and to other resources. |  -  |
**406** | Content negotiation failed. For example, the &amp;#x60;Accept&amp;#x60; header submitted in the request did not support any of the media types supported by the server for the requested resource. |  -  |
**500** | A server error occurred. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
