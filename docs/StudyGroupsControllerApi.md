# rcc.StudyGroupsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create10**](StudyGroupsControllerApi.md#create10) | **POST** /v2/study-group-clases | Create new Study Group Class for current Study based on auth token provided
[**create_bulk_academic**](StudyGroupsControllerApi.md#create_bulk_academic) | **POST** /v2/study-group-clases/academic | Create new Study Group Class for current Study based on auth token provided
[**delete7**](StudyGroupsControllerApi.md#delete7) | **DELETE** /v2/study-group-clases/{id} | Delete Study Group Class for current Study based on auth token provided
[**get_details7**](StudyGroupsControllerApi.md#get_details7) | **GET** /v2/study-group-clases/{id} | Get specified Study Group Class details
[**get_group_class_subject_assignments**](StudyGroupsControllerApi.md#get_group_class_subject_assignments) | **GET** /v2/study-group-clases/vocabularies/group-class-subject-assignments | Get available subject assignments
[**get_group_class_types**](StudyGroupsControllerApi.md#get_group_class_types) | **GET** /v2/study-group-clases/vocabularies/group-class-types | Get available study types
[**get_list8**](StudyGroupsControllerApi.md#get_list8) | **GET** /v2/study-group-clases | Get list of all Study Group Classes for specified Study
[**update9**](StudyGroupsControllerApi.md#update9) | **PUT** /v2/study-group-clases/{id} | Update Study Group Classes for current Study based on auth token provided


# **create10**
> int create10(token, body)

Create new Study Group Class for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyGroupClassViewRpc() # StudyGroupClassViewRpc | Study Group Class Details to Save

    try:
        # Create new Study Group Class for current Study based on auth token provided
        api_response = api_instance.create10(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->create10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyGroupClassViewRpc**](StudyGroupClassViewRpc.md)| Study Group Class Details to Save | 

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

# **create_bulk_academic**
> list[str] create_bulk_academic(token, body)

Create new Study Group Class for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.AcademicStudyGroupClassViewRpc() # AcademicStudyGroupClassViewRpc | Study Group Class Details to Save

    try:
        # Create new Study Group Class for current Study based on auth token provided
        api_response = api_instance.create_bulk_academic(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->create_bulk_academic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**AcademicStudyGroupClassViewRpc**](AcademicStudyGroupClassViewRpc.md)| Study Group Class Details to Save | 

### Return type

**list[str]**

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

# **delete7**
> int delete7(id, token)

Delete Study Group Class for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    id = 56 # int | Study Group Class unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Study Group Class for current Study based on auth token provided
        api_response = api_instance.delete7(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->delete7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Group Class unique ID | 
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
**500** | Study for Study Group not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details7**
> get_details7(id, token)

Get specified Study Group Class details

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    id = 56 # int | Study Group Class ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get specified Study Group Class details
        api_instance.get_details7(id, token)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->get_details7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Group Class ID | 
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
**404** | Item not found. |  -  |
**500** | Study for Study Group not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_class_subject_assignments**
> list[GenericItem] get_group_class_subject_assignments()

Get available subject assignments

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    
    try:
        # Get available subject assignments
        api_response = api_instance.get_group_class_subject_assignments()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->get_group_class_subject_assignments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **get_group_class_types**
> list[GenericItem] get_group_class_types()

Get available study types

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    
    try:
        # Get available study types
        api_response = api_instance.get_group_class_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->get_group_class_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **get_list8**
> list[StudyGroupClassViewRpc] get_list8(token)

Get list of all Study Group Classes for specified Study

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Study Group Classes for specified Study
        api_response = api_instance.get_list8(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->get_list8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[StudyGroupClassViewRpc]**](StudyGroupClassViewRpc.md)

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

# **update9**
> int update9(id, token, body)

Update Study Group Classes for current Study based on auth token provided

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
    api_instance = rcc.StudyGroupsControllerApi(api_client)
    id = 56 # int | Study Group Class unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyGroupClassViewRpc() # StudyGroupClassViewRpc | Study Group Class Details to Save

    try:
        # Update Study Group Classes for current Study based on auth token provided
        api_response = api_instance.update9(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyGroupsControllerApi->update9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Group Class unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyGroupClassViewRpc**](StudyGroupClassViewRpc.md)| Study Group Class Details to Save | 

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

