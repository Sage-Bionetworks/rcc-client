# rcc.CRFSectionsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create6**](CRFSectionsControllerApi.md#create6) | **POST** /v2/sections | Create new CRF Section for specified CRF Version
[**delete4**](CRFSectionsControllerApi.md#delete4) | **DELETE** /v2/sections/{id} | Delete CRF Section for current Study based on auth token provided
[**get_details4**](CRFSectionsControllerApi.md#get_details4) | **GET** /v2/sections/{id} | Get CRF details for current Study based on auth token provided
[**get_list5**](CRFSectionsControllerApi.md#get_list5) | **GET** /v2/sections | Get list of all CRF Sections for specified study
[**get_list_for_crf**](CRFSectionsControllerApi.md#get_list_for_crf) | **GET** /v2/sections/crf/{id} | Get list of all Section for CRF form in specified study
[**get_list_for_crf_version**](CRFSectionsControllerApi.md#get_list_for_crf_version) | **GET** /v2/sections/crf-version/{id} | Get list of all Section for CRF form Version in specified study
[**patch1**](CRFSectionsControllerApi.md#patch1) | **PATCH** /v2/sections/{id} | Update some specific CRF Section fields
[**update5**](CRFSectionsControllerApi.md#update5) | **PUT** /v2/sections/{id} | Update CRF Section for specified CRF Version


# **create6**
> int create6(token, body)

Create new CRF Section for specified CRF Version

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SectionRpc() # SectionRpc | CRF Sections Details to Save

    try:
        # Create new CRF Section for specified CRF Version
        api_response = api_instance.create6(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->create6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SectionRpc**](SectionRpc.md)| CRF Sections Details to Save | 

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
**500** | Specified CRF version not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete4**
> int delete4(id, token)

Delete CRF Section for current Study based on auth token provided

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    id = 56 # int | CRF section unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete CRF Section for current Study based on auth token provided
        api_response = api_instance.delete4(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->delete4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF section unique ID | 
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

# **get_details4**
> SectionRpc get_details4(id, token)

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    id = 56 # int | CRF Section unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF details for current Study based on auth token provided
        api_response = api_instance.get_details4(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->get_details4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Section unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**SectionRpc**](SectionRpc.md)

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
**500** | Study for CRF Section not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list5**
> list[SectionRpc] get_list5(token)

Get list of all CRF Sections for specified study

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Sections for specified study
        api_response = api_instance.get_list5(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->get_list5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SectionRpc]**](SectionRpc.md)

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

# **get_list_for_crf**
> list[SectionRpc] get_list_for_crf(id, token)

Get list of all Section for CRF form in specified study

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    id = 56 # int | CRF unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Section for CRF form in specified study
        api_response = api_instance.get_list_for_crf(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->get_list_for_crf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SectionRpc]**](SectionRpc.md)

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

# **get_list_for_crf_version**
> list[SectionRpc] get_list_for_crf_version(id, token)

Get list of all Section for CRF form Version in specified study

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    id = 56 # int | CRF version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Section for CRF form Version in specified study
        api_response = api_instance.get_list_for_crf_version(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->get_list_for_crf_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SectionRpc]**](SectionRpc.md)

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

# **patch1**
> int patch1(id, token, body)

Update some specific CRF Section fields

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    id = 56 # int | CRF Section unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.PatchObject() # PatchObject | CRF Section details object

    try:
        # Update some specific CRF Section fields
        api_response = api_instance.patch1(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->patch1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Section unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**PatchObject**](PatchObject.md)| CRF Section details object | 

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
**500** | ID must be specified for patch operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update5**
> int update5(id, token, body)

Update CRF Section for specified CRF Version

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
    api_instance = rcc.CRFSectionsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SectionRpc() # SectionRpc | CRF Sections Details to Save

    try:
        # Update CRF Section for specified CRF Version
        api_response = api_instance.update5(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFSectionsControllerApi->update5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SectionRpc**](SectionRpc.md)| CRF Sections Details to Save | 

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
**500** | Concurrent modification exception. Item was modified by separate process after fetch. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

