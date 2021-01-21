# rcc.StudiesControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create8**](StudiesControllerApi.md#create8) | **POST** /v2/studies | Create new study based on details object for tenant user API key
[**get_categories**](StudiesControllerApi.md#get_categories) | **GET** /v2/studies/categories | Get list of all available study categories
[**get_details6**](StudiesControllerApi.md#get_details6) | **GET** /v2/studies | Get study details based on auth token provided
[**get_studies_collection**](StudiesControllerApi.md#get_studies_collection) | **GET** /v2/studies/collection | Get list of all studies for tenant user
[**get_studies_list**](StudiesControllerApi.md#get_studies_list) | **GET** /v2/studies/list | Get list of all studies for tenant user
[**get_study_allocations**](StudiesControllerApi.md#get_study_allocations) | **GET** /v2/studies/vocabularies/allocations | Get available study allocations
[**get_study_api_details**](StudiesControllerApi.md#get_study_api_details) | **GET** /v2/studies/{studyId}/assignments/{id} | Get study Assignment API details
[**get_study_api_details_list**](StudiesControllerApi.md#get_study_api_details_list) | **GET** /v2/studies/{id}/assignments | Get study API details list for tenant token
[**get_study_api_details_list1**](StudiesControllerApi.md#get_study_api_details_list1) | **POST** /v2/studies/assignments | Get list of all API assignments for tenant
[**get_study_assignments**](StudiesControllerApi.md#get_study_assignments) | **GET** /v2/studies/vocabularies/assignments | Get available study assignments types
[**get_study_classifications**](StudiesControllerApi.md#get_study_classifications) | **GET** /v2/studies/vocabularies/classifications | Get available study Classifications
[**get_study_control_types**](StudiesControllerApi.md#get_study_control_types) | **GET** /v2/studies/vocabularies/control-types | Get available study control types
[**get_study_details**](StudiesControllerApi.md#get_study_details) | **GET** /v2/studies/{id} | Get study details for tenant token
[**get_study_durations**](StudiesControllerApi.md#get_study_durations) | **GET** /v2/studies/vocabularies/durations | Get available study duration types
[**get_study_genders**](StudiesControllerApi.md#get_study_genders) | **GET** /v2/studies/vocabularies/genders | Get available study genders
[**get_study_maskings**](StudiesControllerApi.md#get_study_maskings) | **GET** /v2/studies/vocabularies/maskings | Get available study maskings
[**get_study_phases**](StudiesControllerApi.md#get_study_phases) | **GET** /v2/studies/vocabularies/phases | Get available study Phases
[**get_study_protocol_types**](StudiesControllerApi.md#get_study_protocol_types) | **GET** /v2/studies/vocabularies/protocol-types | Get available study protocol types
[**get_study_purposes**](StudiesControllerApi.md#get_study_purposes) | **GET** /v2/studies/vocabularies/purposes | Get available study purposes
[**get_study_roles_list**](StudiesControllerApi.md#get_study_roles_list) | **GET** /v2/studies/{id}/roles | Get study roles
[**get_study_selections**](StudiesControllerApi.md#get_study_selections) | **GET** /v2/studies/vocabularies/selections | Get available study selections types
[**get_study_statuses**](StudiesControllerApi.md#get_study_statuses) | **GET** /v2/studies/vocabularies/statuses | Get available study statuses
[**get_study_timing**](StudiesControllerApi.md#get_study_timing) | **GET** /v2/studies/vocabularies/timings | Get available study timing types
[**get_study_types**](StudiesControllerApi.md#get_study_types) | **GET** /v2/studies/vocabularies/study-types | Get available study types
[**get_study_user_api_details**](StudiesControllerApi.md#get_study_user_api_details) | **GET** /v2/studies/{id}/users/{userId}/assignments | Get study API details for some user and tenant token
[**get_study_versions**](StudiesControllerApi.md#get_study_versions) | **GET** /v2/studies/vocabularies/versions | Get available study versions
[**patch3**](StudiesControllerApi.md#patch3) | **PATCH** /v2/studies | Update some specific study fields
[**regenerate_study_api_token_details**](StudiesControllerApi.md#regenerate_study_api_token_details) | **GET** /v2/studies/{studyId}/assignments/{id}/regenerate-token | Regenerate Study Assignment API Token and return Assignment details.
[**update7**](StudiesControllerApi.md#update7) | **PUT** /v2/studies | Update study based on details object for tenant user API key
[**update_study_api_details**](StudiesControllerApi.md#update_study_api_details) | **POST** /v2/studies/assignments/update | Create/Update Study Assignment. Generate/Regenerate API Token.


# **create8**
> int create8(token, body)

Create new study based on details object for tenant user API key

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.
body = rcc.StudyRpc() # StudyRpc | Study details object

    try:
        # Create new study based on details object for tenant user API key
        api_response = api_instance.create8(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->create8: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 
 **body** | [**StudyRpc**](StudyRpc.md)| Study details object | 

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
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**500** | ID must not be specified for new study. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> list[GenericItem] get_categories(token)

Get list of all available study categories

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get list of all available study categories
        api_response = api_instance.get_categories(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

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
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details6**
> StudyRpc get_details6(token)

Get study details based on auth token provided

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get study details based on auth token provided
        api_response = api_instance.get_details6(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_details6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**StudyRpc**](StudyRpc.md)

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

# **get_studies_collection**
> object get_studies_collection(token)

Get list of all studies for tenant user

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get list of all studies for tenant user
        api_response = api_instance.get_studies_collection(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_studies_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

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
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_studies_list**
> list[StudyViewRpc] get_studies_list(token)

Get list of all studies for tenant user

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get list of all studies for tenant user
        api_response = api_instance.get_studies_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_studies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

### Return type

[**list[StudyViewRpc]**](StudyViewRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_allocations**
> list[GenericItem] get_study_allocations()

Get available study allocations

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study allocations
        api_response = api_instance.get_study_allocations()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_allocations: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_api_details**
> StudyAssignmentsRpc get_study_api_details(study_id, id, token)

Get study Assignment API details

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
    api_instance = rcc.StudiesControllerApi(api_client)
    study_id = 56 # int | Study ID
id = 56 # int | Assignment ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study Assignment API details
        api_response = api_instance.get_study_api_details(study_id, id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_api_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **id** | **int**| Assignment ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**StudyAssignmentsRpc**](StudyAssignmentsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**404** | Study assignments not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_api_details_list**
> list[StudyAssignmentsRpc] get_study_api_details_list(id, token)

Get study API details list for tenant token

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
    api_instance = rcc.StudiesControllerApi(api_client)
    id = 56 # int | Study ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study API details list for tenant token
        api_response = api_instance.get_study_api_details_list(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_api_details_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**list[StudyAssignmentsRpc]**](StudyAssignmentsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_api_details_list1**
> UserAssignmentsRecordsResultRpc get_study_api_details_list1(token, body)

Get list of all API assignments for tenant

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.
body = rcc.UserAssignmentsFilter() # UserAssignmentsFilter | Paging filter

    try:
        # Get list of all API assignments for tenant
        api_response = api_instance.get_study_api_details_list1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_api_details_list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 
 **body** | [**UserAssignmentsFilter**](UserAssignmentsFilter.md)| Paging filter | 

### Return type

[**UserAssignmentsRecordsResultRpc**](UserAssignmentsRecordsResultRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Too much page size value. |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_assignments**
> list[GenericItem] get_study_assignments()

Get available study assignments types

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study assignments types
        api_response = api_instance.get_study_assignments()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_assignments: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_classifications**
> list[GenericItem] get_study_classifications()

Get available study Classifications

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study Classifications
        api_response = api_instance.get_study_classifications()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_classifications: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_control_types**
> list[GenericItem] get_study_control_types()

Get available study control types

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study control types
        api_response = api_instance.get_study_control_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_control_types: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_details**
> StudyRpc get_study_details(id, token)

Get study details for tenant token

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
    api_instance = rcc.StudiesControllerApi(api_client)
    id = 56 # int | Study ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study details for tenant token
        api_response = api_instance.get_study_details(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**StudyRpc**](StudyRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_durations**
> list[GenericItem] get_study_durations()

Get available study duration types

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study duration types
        api_response = api_instance.get_study_durations()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_durations: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_genders**
> list[GenericItem] get_study_genders()

Get available study genders

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study genders
        api_response = api_instance.get_study_genders()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_genders: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_maskings**
> list[GenericItem] get_study_maskings()

Get available study maskings

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study maskings
        api_response = api_instance.get_study_maskings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_maskings: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_phases**
> list[GenericItem] get_study_phases()

Get available study Phases

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study Phases
        api_response = api_instance.get_study_phases()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_phases: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_protocol_types**
> list[GenericItem] get_study_protocol_types()

Get available study protocol types

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study protocol types
        api_response = api_instance.get_study_protocol_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_protocol_types: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_purposes**
> list[GenericItem] get_study_purposes()

Get available study purposes

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study purposes
        api_response = api_instance.get_study_purposes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_purposes: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_roles_list**
> list[GenericItem] get_study_roles_list(id, token)

Get study roles

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
    api_instance = rcc.StudiesControllerApi(api_client)
    id = 56 # int | Study ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study roles
        api_response = api_instance.get_study_roles_list(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_roles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

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
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_selections**
> list[GenericItem] get_study_selections()

Get available study selections types

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study selections types
        api_response = api_instance.get_study_selections()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_selections: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_statuses**
> list[GenericItem] get_study_statuses()

Get available study statuses

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study statuses
        api_response = api_instance.get_study_statuses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_statuses: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_timing**
> list[GenericItem] get_study_timing()

Get available study timing types

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study timing types
        api_response = api_instance.get_study_timing()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_timing: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_types**
> list[GenericItem] get_study_types()

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study types
        api_response = api_instance.get_study_types()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_types: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_user_api_details**
> list[StudyAssignmentsRpc] get_study_user_api_details(id, user_id, token)

Get study API details for some user and tenant token

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
    api_instance = rcc.StudiesControllerApi(api_client)
    id = 56 # int | Study ID
user_id = 56 # int | User ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study API details for some user and tenant token
        api_response = api_instance.get_study_user_api_details(id, user_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_user_api_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study ID | 
 **user_id** | **int**| User ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**list[StudyAssignmentsRpc]**](StudyAssignmentsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_versions**
> list[GenericItem] get_study_versions()

Get available study versions

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
    api_instance = rcc.StudiesControllerApi(api_client)
    
    try:
        # Get available study versions
        api_response = api_instance.get_study_versions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->get_study_versions: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch3**
> int patch3(token, body)

Update some specific study fields

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = {'key': 'body_example'} # dict(str, str) | Study details object

    try:
        # Update some specific study fields
        api_response = api_instance.patch3(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->patch3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**dict(str, str)**](str.md)| Study details object | 

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
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**500** | ID must be specified for patch operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_study_api_token_details**
> StudyAssignmentsRpc regenerate_study_api_token_details(study_id, id, token)

Regenerate Study Assignment API Token and return Assignment details.

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
    api_instance = rcc.StudiesControllerApi(api_client)
    study_id = 56 # int | Study ID
id = 56 # int | Assignment ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Regenerate Study Assignment API Token and return Assignment details.
        api_response = api_instance.regenerate_study_api_token_details(study_id, id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->regenerate_study_api_token_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **id** | **int**| Assignment ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**StudyAssignmentsRpc**](StudyAssignmentsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**404** | Study assignments not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update7**
> int update7(token, body)

Update study based on details object for tenant user API key

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudyRpc() # StudyRpc | Study details object

    try:
        # Update study based on details object for tenant user API key
        api_response = api_instance.update7(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->update7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudyRpc**](StudyRpc.md)| Study details object | 

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
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**500** | Study not match specified study access Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_study_api_details**
> StudyAssignmentsRpc update_study_api_details(token, body)

Create/Update Study Assignment. Generate/Regenerate API Token.

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
    api_instance = rcc.StudiesControllerApi(api_client)
    token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.
body = rcc.StudyAssignmentsRpc() # StudyAssignmentsRpc | Study Assignment Details

    try:
        # Create/Update Study Assignment. Generate/Regenerate API Token.
        api_response = api_instance.update_study_api_details(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesControllerApi->update_study_api_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 
 **body** | [**StudyAssignmentsRpc**](StudyAssignmentsRpc.md)| Study Assignment Details | 

### Return type

[**StudyAssignmentsRpc**](StudyAssignmentsRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |
**404** | Study assignments not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

