# rcc.StudyEventsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create9**](StudyEventsControllerApi.md#create9) | **POST** /v2/study-events | Create new Study Event for current Study based on auth token provided
[**delete6**](StudyEventsControllerApi.md#delete6) | **DELETE** /v2/study-events/{id} | Delete Study Event for current Study based on auth token provided
[**filter_list1**](StudyEventsControllerApi.md#filter_list1) | **POST** /v2/study-events/filter | Get filtered list of Study Events for current Study based on auth token provided
[**get_list7**](StudyEventsControllerApi.md#get_list7) | **GET** /v2/study-events | Get list of all Study Events for specified Study
[**get_statuses_list**](StudyEventsControllerApi.md#get_statuses_list) | **GET** /v2/study-events/available-statuses | Get list of Available Statuses for Study Events
[**save_batch1**](StudyEventsControllerApi.md#save_batch1) | **POST** /v2/study-events/save | Batch save of Study Events
[**update8**](StudyEventsControllerApi.md#update8) | **PUT** /v2/study-events | Update existing Study Event for current Study based on auth token provided


# **create9**
> StudyEventsRpc create9(token, body)

Create new Study Event for current Study based on auth token provided

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyEventsRpc() # StudyEventsRpc | Study Event Details to Save

    try:
        # Create new Study Event for current Study based on auth token provided
        api_response = api_instance.create9(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->create9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyEventsRpc**](StudyEventsRpc.md)| Study Event Details to Save | 

### Return type

[**StudyEventsRpc**](StudyEventsRpc.md)

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
**409** | Study event for this subject already exists. You can create multiple event occurences only for repeating events. |  -  |
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete6**
> int delete6(id, token)

Delete Study Event for current Study based on auth token provided

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    id = 56 # int | Study Event unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Study Event for current Study based on auth token provided
        api_response = api_instance.delete6(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->delete6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Event unique ID | 
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

# **filter_list1**
> list[StudyEventsRpc] filter_list1(token, body)

Get filtered list of Study Events for current Study based on auth token provided

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventSubjectFilter() # EventSubjectFilter | Filters for Study/Event/Subjects

    try:
        # Get filtered list of Study Events for current Study based on auth token provided
        api_response = api_instance.filter_list1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->filter_list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventSubjectFilter**](EventSubjectFilter.md)| Filters for Study/Event/Subjects | 

### Return type

[**list[StudyEventsRpc]**](StudyEventsRpc.md)

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

# **get_list7**
> list[StudyEventsRpc] get_list7(token)

Get list of all Study Events for specified Study

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Study Events for specified Study
        api_response = api_instance.get_list7(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->get_list7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[StudyEventsRpc]**](StudyEventsRpc.md)

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

# **get_statuses_list**
> list[GenericItem] get_statuses_list(token)

Get list of Available Statuses for Study Events

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of Available Statuses for Study Events
        api_response = api_instance.get_statuses_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->get_statuses_list: %s\n" % e)
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

# **save_batch1**
> list[StudyEventsRpc] save_batch1(token, body)

Batch save of Study Events

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.StudyEventsRpc()] # list[StudyEventsRpc] | Event CRF items to Save

    try:
        # Batch save of Study Events
        api_response = api_instance.save_batch1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->save_batch1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[StudyEventsRpc]**](StudyEventsRpc.md)| Event CRF items to Save | 

### Return type

[**list[StudyEventsRpc]**](StudyEventsRpc.md)

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

# **update8**
> StudyEventsRpc update8(token, body)

Update existing Study Event for current Study based on auth token provided

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
    api_instance = rcc.StudyEventsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyEventsRpc() # StudyEventsRpc | Study Event Details to Save

    try:
        # Update existing Study Event for current Study based on auth token provided
        api_response = api_instance.update8(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyEventsControllerApi->update8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyEventsRpc**](StudyEventsRpc.md)| Study Event Details to Save | 

### Return type

[**StudyEventsRpc**](StudyEventsRpc.md)

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

