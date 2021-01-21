# rcc.StudyRolesControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_study_role**](StudyRolesControllerApi.md#delete_study_role) | **DELETE** /v2/study-roles/{studyId}/{roleId} | Delete study role
[**get_study_components_list**](StudyRolesControllerApi.md#get_study_components_list) | **GET** /v2/study-roles/{studyId}/components | Get tenant components
[**get_study_role_details**](StudyRolesControllerApi.md#get_study_role_details) | **GET** /v2/study-roles/{studyId}/{roleId} | Get study role
[**get_study_roles_list1**](StudyRolesControllerApi.md#get_study_roles_list1) | **GET** /v2/study-roles/{studyId} | Get study roles
[**get_tenant_applications**](StudyRolesControllerApi.md#get_tenant_applications) | **GET** /v2/study-roles/applications | Get tenant applications
[**get_tenant_components**](StudyRolesControllerApi.md#get_tenant_components) | **GET** /v2/study-roles/components/captions | Get tenant components
[**save_study_role_details**](StudyRolesControllerApi.md#save_study_role_details) | **POST** /v2/study-roles/{studyId} | Save study role


# **delete_study_role**
> int delete_study_role(study_id, role_id, token)

Delete study role

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    study_id = 56 # int | Study ID
role_id = 56 # int | Role ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Delete study role
        api_response = api_instance.delete_study_role(study_id, role_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->delete_study_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **role_id** | **int**| Role ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

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
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_study_components_list**
> list[StudyComponentsRpc] get_study_components_list(study_id, token)

Get tenant components

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    study_id = 56 # int | Study ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get tenant components
        api_response = api_instance.get_study_components_list(study_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->get_study_components_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**list[StudyComponentsRpc]**](StudyComponentsRpc.md)

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

# **get_study_role_details**
> StudyRoleRpc get_study_role_details(study_id, role_id, token)

Get study role

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    study_id = 56 # int | Study ID
role_id = 56 # int | Role ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study role
        api_response = api_instance.get_study_role_details(study_id, role_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->get_study_role_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **role_id** | **int**| Role ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**StudyRoleRpc**](StudyRoleRpc.md)

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

# **get_study_roles_list1**
> list[ApplicationRoleRpc] get_study_roles_list1(study_id, token)

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    study_id = 56 # int | Study ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get study roles
        api_response = api_instance.get_study_roles_list1(study_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->get_study_roles_list1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 

### Return type

[**list[ApplicationRoleRpc]**](ApplicationRoleRpc.md)

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

# **get_tenant_applications**
> list[GenericItem] get_tenant_applications(token)

Get tenant applications

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get tenant applications
        api_response = api_instance.get_tenant_applications(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->get_tenant_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_tenant_components**
> list[GenericItem] get_tenant_components(token)

Get tenant components

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.

    try:
        # Get tenant components
        api_response = api_instance.get_tenant_components(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->get_tenant_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **save_study_role_details**
> StudyRoleRpc save_study_role_details(study_id, token, body)

Save study role

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
    api_instance = rcc.StudyRolesControllerApi(api_client)
    study_id = 56 # int | Study ID
token = 'token_example' # str | Tenant access token. Used to authorize user for API calls.
body = rcc.StudyRoleRpc() # StudyRoleRpc | Records Collection

    try:
        # Save study role
        api_response = api_instance.save_study_role_details(study_id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyRolesControllerApi->save_study_role_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID | 
 **token** | **str**| Tenant access token. Used to authorize user for API calls. | 
 **body** | [**StudyRoleRpc**](StudyRoleRpc.md)| Records Collection | 

### Return type

[**StudyRoleRpc**](StudyRoleRpc.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

