# rcc.EventCrfsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create3**](EventCrfsControllerApi.md#create3) | **POST** /v2/event-crfs | Create new Event CRF for current Study based on auth token provided
[**delete2**](EventCrfsControllerApi.md#delete2) | **DELETE** /v2/event-crfs/{id} | Delete Event Definition for current Study based on auth token provided
[**filter_list**](EventCrfsControllerApi.md#filter_list) | **POST** /v2/event-crfs/filter | Get list of Event CRFs by filter
[**get_list2**](EventCrfsControllerApi.md#get_list2) | **GET** /v2/event-crfs | Get list of all Event Crfs for specified Study
[**save_batch**](EventCrfsControllerApi.md#save_batch) | **POST** /v2/event-crfs/save | Batch save of Event CRFs
[**update2**](EventCrfsControllerApi.md#update2) | **PUT** /v2/event-crfs | Create new Event CRF for current Study based on auth token provided


# **create3**
> EventCrfsRpc create3(token, body)

Create new Event CRF for current Study based on auth token provided

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
    api_instance = rcc.EventCrfsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventCrfsRpc() # EventCrfsRpc | Event CRF Details to Save

    try:
        # Create new Event CRF for current Study based on auth token provided
        api_response = api_instance.create3(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventCrfsControllerApi->create3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventCrfsRpc**](EventCrfsRpc.md)| Event CRF Details to Save | 

### Return type

[**EventCrfsRpc**](EventCrfsRpc.md)

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete2**
> int delete2(id, token)

Delete Event Definition for current Study based on auth token provided

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
    api_instance = rcc.EventCrfsControllerApi(api_client)
    id = 56 # int | Event CRFs unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Event Definition for current Study based on auth token provided
        api_response = api_instance.delete2(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventCrfsControllerApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event CRFs unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

**int**

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
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | Study for Event Definition not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_list**
> list[EventCrfsRpc] filter_list(token, body)

Get list of Event CRFs by filter

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
    api_instance = rcc.EventCrfsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfSubjectFilter() # CrfSubjectFilter | Filters for Study/Crf/Subjects

    try:
        # Get list of Event CRFs by filter
        api_response = api_instance.filter_list(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventCrfsControllerApi->filter_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfSubjectFilter**](CrfSubjectFilter.md)| Filters for Study/Crf/Subjects | 

### Return type

[**list[EventCrfsRpc]**](EventCrfsRpc.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list2**
> list[EventCrfsRpc] get_list2(token)

Get list of all Event Crfs for specified Study

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
    api_instance = rcc.EventCrfsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Crfs for specified Study
        api_response = api_instance.get_list2(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventCrfsControllerApi->get_list2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EventCrfsRpc]**](EventCrfsRpc.md)

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

# **save_batch**
> list[EventCrfsRpc] save_batch(token, body)

Batch save of Event CRFs

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
    api_instance = rcc.EventCrfsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.EventCrfsRpc()] # list[EventCrfsRpc] | Event CRF items to Save

    try:
        # Batch save of Event CRFs
        api_response = api_instance.save_batch(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventCrfsControllerApi->save_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[EventCrfsRpc]**](EventCrfsRpc.md)| Event CRF items to Save | 

### Return type

[**list[EventCrfsRpc]**](EventCrfsRpc.md)

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update2**
> EventCrfsRpc update2(token, body)

Create new Event CRF for current Study based on auth token provided

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
    api_instance = rcc.EventCrfsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventCrfsRpc() # EventCrfsRpc | Event CRF Details to Update

    try:
        # Create new Event CRF for current Study based on auth token provided
        api_response = api_instance.update2(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventCrfsControllerApi->update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventCrfsRpc**](EventCrfsRpc.md)| Event CRF Details to Update | 

### Return type

[**EventCrfsRpc**](EventCrfsRpc.md)

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

