# rcc.CRFsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](CRFsControllerApi.md#create2) | **POST** /v2/crfs | Create new CRF and CRF version for current Study based on auth token provided
[**get_crf_details**](CRFsControllerApi.md#get_crf_details) | **GET** /v2/crfs/{id} | Get CRF details for current Study based on auth token provided
[**get_crf_versions**](CRFsControllerApi.md#get_crf_versions) | **GET** /v2/crfs/{id}/versions | Get CRF Versions for current CRF and Study
[**get_list1**](CRFsControllerApi.md#get_list1) | **GET** /v2/crfs | Get list of all CRFs for specified study


# **create2**
> int create2(token, body)

Create new CRF and CRF version for current Study based on auth token provided

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
    api_instance = rcc.CRFsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfVersionRpc() # CrfVersionRpc | CRF Details to Save

    try:
        # Create new CRF and CRF version for current Study based on auth token provided
        api_response = api_instance.create2(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFsControllerApi->create2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfVersionRpc**](CrfVersionRpc.md)| CRF Details to Save | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | CRF cannot be marked as Screening because is used in Event Definition(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crf_details**
> CrfViewRpc get_crf_details(id, token)

Get CRF details for current Study based on auth token provided

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
    api_instance = rcc.CRFsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF details for current Study based on auth token provided
        api_response = api_instance.get_crf_details(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFsControllerApi->get_crf_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**CrfViewRpc**](CrfViewRpc.md)

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
**500** | Study for CRF not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crf_versions**
> list[CrfVersionViewRpc] get_crf_versions(id, token)

Get CRF Versions for current CRF and Study

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
    api_instance = rcc.CRFsControllerApi(api_client)
    id = 56 # int | CRF unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF Versions for current CRF and Study
        api_response = api_instance.get_crf_versions(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFsControllerApi->get_crf_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[CrfVersionViewRpc]**](CrfVersionViewRpc.md)

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

# **get_list1**
> list[GenericItem] get_list1(token)

Get list of all CRFs for specified study

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
    api_instance = rcc.CRFsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRFs for specified study
        api_response = api_instance.get_list1(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFsControllerApi->get_list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[GenericItem]**](GenericItem.md)

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

