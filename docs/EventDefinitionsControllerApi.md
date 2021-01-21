# rcc.EventDefinitionsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create4**](EventDefinitionsControllerApi.md#create4) | **POST** /v2/event-definitions | Create new Event Definition for current Study based on auth token provided
[**create_event_definition_crf**](EventDefinitionsControllerApi.md#create_event_definition_crf) | **POST** /v2/event-definitions/crfs | Create new Event Definition Crf
[**delete3**](EventDefinitionsControllerApi.md#delete3) | **DELETE** /v2/event-definitions/{id} | Delete Event Definition for current Study based on auth token provided
[**filter_items1**](EventDefinitionsControllerApi.md#filter_items1) | **POST** /v2/event-definitions/filter | Get list of Event Definitions for Filter
[**get_details2**](EventDefinitionsControllerApi.md#get_details2) | **GET** /v2/event-definitions/{id} | Get specified Event Definition details
[**get_event_definition_categories_list**](EventDefinitionsControllerApi.md#get_event_definition_categories_list) | **GET** /v2/event-definitions/categories | Get list of available Event Definition Categories
[**get_event_definition_crfs_list**](EventDefinitionsControllerApi.md#get_event_definition_crfs_list) | **GET** /v2/event-definitions/{id}/crfs | Get list of all Event Definitions CRFs for Event Definition
[**get_event_definition_crfs_list_for_site**](EventDefinitionsControllerApi.md#get_event_definition_crfs_list_for_site) | **GET** /v2/event-definitions/{id}/crfs/site/{siteId} | Get list of all Event Definitions CRFs for Event Definition and Site
[**get_event_definition_statuses_list**](EventDefinitionsControllerApi.md#get_event_definition_statuses_list) | **GET** /v2/event-definitions/statuses | Get list of available Subject Categories
[**get_event_definition_types_list**](EventDefinitionsControllerApi.md#get_event_definition_types_list) | **GET** /v2/event-definitions/types | Get list of available Event Definition Types
[**get_list3**](EventDefinitionsControllerApi.md#get_list3) | **GET** /v2/event-definitions | Get list of all Event Definitions for specified Study
[**get_study_crfs_list**](EventDefinitionsControllerApi.md#get_study_crfs_list) | **GET** /v2/event-definitions/crfs | Get list of all Event Definitions CRFs for specified Study
[**get_study_site_crfs_list**](EventDefinitionsControllerApi.md#get_study_site_crfs_list) | **GET** /v2/event-definitions/crfs/site/{siteId} | Get list of all Event Definitions CRFs for specified Study
[**update3**](EventDefinitionsControllerApi.md#update3) | **PUT** /v2/event-definitions/{id} | Update Event Definition for current Study based on auth token provided
[**update_event_definition_crf**](EventDefinitionsControllerApi.md#update_event_definition_crf) | **PUT** /v2/event-definitions/crfs/{id} | Update Event Definition Crfs


# **create4**
> int create4(token, body)

Create new Event Definition for current Study based on auth token provided

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventDefinitionRpc() # EventDefinitionRpc | Event Definition Details to Save

    try:
        # Create new Event Definition for current Study based on auth token provided
        api_response = api_instance.create4(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->create4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventDefinitionRpc**](EventDefinitionRpc.md)| Event Definition Details to Save | 

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
**400** | Event can not be created for studies without sites |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_definition_crf**
> int create_event_definition_crf(token, body)

Create new Event Definition Crf

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventDefinitionCrfsRpc() # EventDefinitionCrfsRpc | Event Definition CRF Details to Save

    try:
        # Create new Event Definition Crf
        api_response = api_instance.create_event_definition_crf(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->create_event_definition_crf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventDefinitionCrfsRpc**](EventDefinitionCrfsRpc.md)| Event Definition CRF Details to Save | 

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete3**
> int delete3(id, token)

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    id = 56 # int | Event Definition unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Event Definition for current Study based on auth token provided
        api_response = api_instance.delete3(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Definition unique ID | 
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

# **filter_items1**
> list[EventDefinitionCrfsRpc] filter_items1(token, body)

Get list of Event Definitions for Filter

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventDefinitionFilter() # EventDefinitionFilter | Study site ID

    try:
        # Get list of Event Definitions for Filter
        api_response = api_instance.filter_items1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->filter_items1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventDefinitionFilter**](EventDefinitionFilter.md)| Study site ID | 

### Return type

[**list[EventDefinitionCrfsRpc]**](EventDefinitionCrfsRpc.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details2**
> get_details2(id, token)

Get specified Event Definition details

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    id = 56 # int | Event Definition ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get specified Event Definition details
        api_instance.get_details2(id, token)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_details2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Definition ID | 
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
**500** | Study for Event Definition not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_definition_categories_list**
> list[GenericItem] get_event_definition_categories_list(token)

Get list of available Event Definition Categories

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of available Event Definition Categories
        api_response = api_instance.get_event_definition_categories_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_event_definition_categories_list: %s\n" % e)
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

# **get_event_definition_crfs_list**
> list[EventDefinitionCrfsRpc] get_event_definition_crfs_list(id, token)

Get list of all Event Definitions CRFs for Event Definition

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    id = 56 # int | Event Definition unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Definitions CRFs for Event Definition
        api_response = api_instance.get_event_definition_crfs_list(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_event_definition_crfs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Definition unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EventDefinitionCrfsRpc]**](EventDefinitionCrfsRpc.md)

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

# **get_event_definition_crfs_list_for_site**
> list[EventDefinitionCrfsRpc] get_event_definition_crfs_list_for_site(id, site_id, token)

Get list of all Event Definitions CRFs for Event Definition and Site

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    id = 56 # int | Event Definition unique ID
site_id = 56 # int | Site unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Definitions CRFs for Event Definition and Site
        api_response = api_instance.get_event_definition_crfs_list_for_site(id, site_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_event_definition_crfs_list_for_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Definition unique ID | 
 **site_id** | **int**| Site unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EventDefinitionCrfsRpc]**](EventDefinitionCrfsRpc.md)

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

# **get_event_definition_statuses_list**
> list[GenericItem] get_event_definition_statuses_list(token)

Get list of available Subject Categories

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of available Subject Categories
        api_response = api_instance.get_event_definition_statuses_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_event_definition_statuses_list: %s\n" % e)
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

# **get_event_definition_types_list**
> list[GenericItem] get_event_definition_types_list(token)

Get list of available Event Definition Types

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of available Event Definition Types
        api_response = api_instance.get_event_definition_types_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_event_definition_types_list: %s\n" % e)
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

# **get_list3**
> list[EventDefinitionViewRpc] get_list3(token)

Get list of all Event Definitions for specified Study

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Definitions for specified Study
        api_response = api_instance.get_list3(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_list3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EventDefinitionViewRpc]**](EventDefinitionViewRpc.md)

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

# **get_study_crfs_list**
> list[EventDefinitionCrfsRpc] get_study_crfs_list(token)

Get list of all Event Definitions CRFs for specified Study

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Definitions CRFs for specified Study
        api_response = api_instance.get_study_crfs_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_study_crfs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EventDefinitionCrfsRpc]**](EventDefinitionCrfsRpc.md)

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

# **get_study_site_crfs_list**
> list[EventDefinitionCrfsRpc] get_study_site_crfs_list(site_id, token)

Get list of all Event Definitions CRFs for specified Study

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    site_id = 56 # int | Site unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Definitions CRFs for specified Study
        api_response = api_instance.get_study_site_crfs_list(site_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->get_study_site_crfs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| Site unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EventDefinitionCrfsRpc]**](EventDefinitionCrfsRpc.md)

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

# **update3**
> int update3(id, token, body)

Update Event Definition for current Study based on auth token provided

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    id = 56 # int | Event Definition unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventDefinitionRpc() # EventDefinitionRpc | Event Definition Details to Save

    try:
        # Update Event Definition for current Study based on auth token provided
        api_response = api_instance.update3(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->update3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Definition unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventDefinitionRpc**](EventDefinitionRpc.md)| Event Definition Details to Save | 

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_definition_crf**
> int update_event_definition_crf(id, token, body)

Update Event Definition Crfs

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
    api_instance = rcc.EventDefinitionsControllerApi(api_client)
    id = 56 # int | Event Definition CRFs unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EventDefinitionCrfsRpc() # EventDefinitionCrfsRpc | Event Definition CRF Details to Save

    try:
        # Update Event Definition Crfs
        api_response = api_instance.update_event_definition_crf(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventDefinitionsControllerApi->update_event_definition_crf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event Definition CRFs unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EventDefinitionCrfsRpc**](EventDefinitionCrfsRpc.md)| Event Definition CRF Details to Save | 

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

