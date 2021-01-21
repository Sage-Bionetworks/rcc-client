# rcc.ResponseSetsForCRFItemsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create5**](ResponseSetsForCRFItemsControllerApi.md#create5) | **POST** /v2/response-sets | Create new Response Sets
[**get_details3**](ResponseSetsForCRFItemsControllerApi.md#get_details3) | **GET** /v2/response-sets/{id} | Get CRF Item Response Set details
[**get_list4**](ResponseSetsForCRFItemsControllerApi.md#get_list4) | **GET** /v2/response-sets | Get list of all used Response Sets for specified Study
[**get_response_sets_list1**](ResponseSetsForCRFItemsControllerApi.md#get_response_sets_list1) | **GET** /v2/response-sets/crf-versions/{id} | Get list of all Response Sets for specified CRF Version
[**update4**](ResponseSetsForCRFItemsControllerApi.md#update4) | **PUT** /v2/response-sets | Update Response Sets


# **create5**
> int create5(token, body)

Create new Response Sets

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
    api_instance = rcc.ResponseSetsForCRFItemsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.ResponseSetRpc() # ResponseSetRpc | Response Set Details to Save

    try:
        # Create new Response Sets
        api_response = api_instance.create5(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponseSetsForCRFItemsControllerApi->create5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**ResponseSetRpc**](ResponseSetRpc.md)| Response Set Details to Save | 

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
**500** | Study for CRF not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details3**
> ResponseSetRpc get_details3(id, token)

Get CRF Item Response Set details

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
    api_instance = rcc.ResponseSetsForCRFItemsControllerApi(api_client)
    id = 56 # int | Response Set ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF Item Response Set details
        api_response = api_instance.get_details3(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponseSetsForCRFItemsControllerApi->get_details3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Response Set ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**ResponseSetRpc**](ResponseSetRpc.md)

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
**500** | Study for Response Set not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list4**
> list[ResponseSetRpc] get_list4(token)

Get list of all used Response Sets for specified Study

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
    api_instance = rcc.ResponseSetsForCRFItemsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all used Response Sets for specified Study
        api_response = api_instance.get_list4(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponseSetsForCRFItemsControllerApi->get_list4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ResponseSetRpc]**](ResponseSetRpc.md)

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

# **get_response_sets_list1**
> list[ResponseSetRpc] get_response_sets_list1(id, token)

Get list of all Response Sets for specified CRF Version

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
    api_instance = rcc.ResponseSetsForCRFItemsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Response Sets for specified CRF Version
        api_response = api_instance.get_response_sets_list1(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponseSetsForCRFItemsControllerApi->get_response_sets_list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ResponseSetRpc]**](ResponseSetRpc.md)

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
**500** | Study for Response Set not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update4**
> int update4(token, body)

Update Response Sets

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
    api_instance = rcc.ResponseSetsForCRFItemsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.ResponseSetRpc() # ResponseSetRpc | Response Set Details to Save

    try:
        # Update Response Sets
        api_response = api_instance.update4(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponseSetsForCRFItemsControllerApi->update4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**ResponseSetRpc**](ResponseSetRpc.md)| Response Set Details to Save | 

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
**500** | Study for Response Set not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

