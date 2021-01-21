# rcc.StudyGroupValuesControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create11**](StudyGroupValuesControllerApi.md#create11) | **POST** /v2/study-groups | Create new Study Group Value for current Study based on auth token provided
[**delete8**](StudyGroupValuesControllerApi.md#delete8) | **DELETE** /v2/study-groups/{id} | Delete Study Group Value for current Study based on auth token provided
[**get_details8**](StudyGroupValuesControllerApi.md#get_details8) | **GET** /v2/study-groups/{id} | Get specified Study Group Value details
[**get_list9**](StudyGroupValuesControllerApi.md#get_list9) | **GET** /v2/study-groups | Get list of all Study Group Values for specified Study
[**update10**](StudyGroupValuesControllerApi.md#update10) | **PUT** /v2/study-groups/{id} | Update Study Group Value for current Study based on auth token provided


# **create11**
> int create11(token, body)

Create new Study Group Value for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupValuesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyGroupViewRpc() # StudyGroupViewRpc | Study Group Value Details to Save

    try:
        # Create new Study Group Value for current Study based on auth token provided
        api_response = api_instance.create11(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupValuesControllerApi->create11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyGroupViewRpc**](StudyGroupViewRpc.md)| Study Group Value Details to Save | 

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
**400** | Validation exception |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**404** | Item not found. |  -  |
**409** | ID must not be specified for this operation. |  -  |
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete8**
> int delete8(id, token)

Delete Study Group Value for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupValuesControllerApi(api_client)
    id = 56 # int | Study Group Value unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Study Group Value for current Study based on auth token provided
        api_response = api_instance.delete8(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupValuesControllerApi->delete8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Group Value unique ID | 
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
**500** | Study for Survey not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details8**
> get_details8(id, token)

Get specified Study Group Value details

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
    api_instance = rcc.StudyGroupValuesControllerApi(api_client)
    id = 56 # int | Study Group Value ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get specified Study Group Value details
        api_instance.get_details8(id, token)
    except ApiException as e:
        print("Exception when calling StudyGroupValuesControllerApi->get_details8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Group Value ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**500** | Study for Study Group not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list9**
> list[StudyGroupViewRpc] get_list9(token)

Get list of all Study Group Values for specified Study

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
    api_instance = rcc.StudyGroupValuesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Study Group Values for specified Study
        api_response = api_instance.get_list9(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupValuesControllerApi->get_list9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[StudyGroupViewRpc]**](StudyGroupViewRpc.md)

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

# **update10**
> int update10(id, token, body)

Update Study Group Value for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupValuesControllerApi(api_client)
    id = 56 # int | Study Group Value unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyGroupViewRpc() # StudyGroupViewRpc | Study Group Value Details to Save

    try:
        # Update Study Group Value for current Study based on auth token provided
        api_response = api_instance.update10(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupValuesControllerApi->update10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Group Value unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyGroupViewRpc**](StudyGroupViewRpc.md)| Study Group Value Details to Save | 

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
**404** | Item not found. |  -  |
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

