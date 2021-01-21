# rcc.IPaaSItemMetadataControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coded_items_metadata**](IPaaSItemMetadataControllerApi.md#get_coded_items_metadata) | **GET** /v2/integration/items-metadata/coded | Retrieves iPaaS metadata from CRF fields.


# **get_coded_items_metadata**
> list[ItemMetadata] get_coded_items_metadata(token)

Retrieves iPaaS metadata from CRF fields.

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
    api_instance = rcc.IPaaSItemMetadataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Retrieves iPaaS metadata from CRF fields.
        api_response = api_instance.get_coded_items_metadata(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemMetadataControllerApi->get_coded_items_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ItemMetadata]**](ItemMetadata.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

