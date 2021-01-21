# rcc.IPaaSGenerateOpenAPI3ControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_open_api**](IPaaSGenerateOpenAPI3ControllerApi.md#generate_open_api) | **GET** /v2/integration/openapi/generate/{token} | Generate named CRF fields in openapi format.


# **generate_open_api**
> object generate_open_api(token)

Generate named CRF fields in openapi format.

### Example

```python
from __future__ import print_function
import time
import rcc
from rcc.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = rcc.Configuration(
    host = "http://localhost/rest"
)


# Enter a context with an instance of the API client
with rcc.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rcc.IPaaSGenerateOpenAPI3ControllerApi(api_client)
    token = 'token_example' # str | 

    try:
        # Generate named CRF fields in openapi format.
        api_response = api_instance.generate_open_api(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSGenerateOpenAPI3ControllerApi->generate_open_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

