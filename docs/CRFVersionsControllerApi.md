# rcc.CRFVersionsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](CRFVersionsControllerApi.md#create1) | **POST** /v2/crf-versions | Create new CRF version for current Study based on auth token provided
[**delete1**](CRFVersionsControllerApi.md#delete1) | **DELETE** /v2/crf-versions/{id} | Delete CRF version for current Study based on auth token provided
[**filter_items**](CRFVersionsControllerApi.md#filter_items) | **POST** /v2/crf-versions/filter | Get list of CRFVersions for Filter
[**get_crf_versions_for_crf**](CRFVersionsControllerApi.md#get_crf_versions_for_crf) | **GET** /v2/crf-versions/crfs/{id} | Get CRF Versions for current CRF and Study
[**get_crf_versions_for_study_event_definition**](CRFVersionsControllerApi.md#get_crf_versions_for_study_event_definition) | **GET** /v2/crf-versions/event-definition/{id} | Get CRF Versions for current Study Event Definition
[**get_details1**](CRFVersionsControllerApi.md#get_details1) | **GET** /v2/crf-versions/{id} | Get CRF details for current Study based on auth token provided
[**get_list**](CRFVersionsControllerApi.md#get_list) | **GET** /v2/crf-versions | Get list of all CRF Versions for specified study
[**patch**](CRFVersionsControllerApi.md#patch) | **PATCH** /v2/crf-versions/{id} | Update some specific CRF Version fields
[**update1**](CRFVersionsControllerApi.md#update1) | **PUT** /v2/crf-versions/{id} | Update CRF version for current Study based on auth token provided


# **create1**
> int create1(token, body)

Create new CRF version for current Study based on auth token provided

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfVersionRpc() # CrfVersionRpc | CRF Version Details to Save

    try:
        # Create new CRF version for current Study based on auth token provided
        api_response = api_instance.create1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->create1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfVersionRpc**](CrfVersionRpc.md)| CRF Version Details to Save | 

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

# **delete1**
> int delete1(id, token)

Delete CRF version for current Study based on auth token provided

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete CRF version for current Study based on auth token provided
        api_response = api_instance.delete1(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
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
**500** | Study for CRF Version not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_items**
> list[CrfVersionViewRpc] filter_items(token, body)

Get list of CRFVersions for Filter

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfVersionFilter() # CrfVersionFilter | Study site ID

    try:
        # Get list of CRFVersions for Filter
        api_response = api_instance.filter_items(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->filter_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfVersionFilter**](CrfVersionFilter.md)| Study site ID | 

### Return type

[**list[CrfVersionViewRpc]**](CrfVersionViewRpc.md)

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

# **get_crf_versions_for_crf**
> list[CrfVersionViewRpc] get_crf_versions_for_crf(id, token)

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    id = 56 # int | CRF unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF Versions for current CRF and Study
        api_response = api_instance.get_crf_versions_for_crf(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->get_crf_versions_for_crf: %s\n" % e)
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

# **get_crf_versions_for_study_event_definition**
> list[CrfVersionViewRpc] get_crf_versions_for_study_event_definition(id, token)

Get CRF Versions for current Study Event Definition

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    id = 56 # int | Study Event definition unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF Versions for current Study Event Definition
        api_response = api_instance.get_crf_versions_for_study_event_definition(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->get_crf_versions_for_study_event_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Event definition unique ID | 
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

# **get_details1**
> CrfVersionRpc get_details1(id, token)

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF details for current Study based on auth token provided
        api_response = api_instance.get_details1(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->get_details1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**CrfVersionRpc**](CrfVersionRpc.md)

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
**500** | Study for CRF Version not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> list[CrfVersionViewRpc] get_list(token)

Get list of all CRF Versions for specified study

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Versions for specified study
        api_response = api_instance.get_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **patch**
> int patch(id, token, body)

Update some specific CRF Version fields

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.PatchObject() # PatchObject | CRF Version details object

    try:
        # Update some specific CRF Version fields
        api_response = api_instance.patch(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**PatchObject**](PatchObject.md)| CRF Version details object | 

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
**500** | Study for CRF Version not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> int update1(id, token, body)

Update CRF version for current Study based on auth token provided

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
    api_instance = rcc.CRFVersionsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfVersionRpc() # CrfVersionRpc | CRF Version Details to Save

    try:
        # Update CRF version for current Study based on auth token provided
        api_response = api_instance.update1(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFVersionsControllerApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfVersionRpc**](CrfVersionRpc.md)| CRF Version Details to Save | 

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

