# rcc.FilesControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_temporary_file**](FilesControllerApi.md#upload_temporary_file) | **POST** /v2/files/upload | Upload temporary file to use in file operations later


# **upload_temporary_file**
> list[DiskFileRpc] upload_temporary_file(token, file)

Upload temporary file to use in file operations later

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
    api_instance = rcc.FilesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
file = '/path/to/file' # file | The binary file to upload.

    try:
        # Upload temporary file to use in file operations later
        api_response = api_instance.upload_temporary_file(token, file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesControllerApi->upload_temporary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **file** | **file**| The binary file to upload. | 

### Return type

[**list[DiskFileRpc]**](DiskFileRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

