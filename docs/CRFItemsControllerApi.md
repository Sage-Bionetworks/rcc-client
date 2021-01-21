# rcc.CRFItemsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CRFItemsControllerApi.md#create) | **POST** /v2/crf-items | Create new CRF Item for current Study based on auth token provided
[**delete**](CRFItemsControllerApi.md#delete) | **DELETE** /v2/crf-items/{id} | Delete CRF Item for current Study based on auth token provided
[**get_crf_items_list**](CRFItemsControllerApi.md#get_crf_items_list) | **GET** /v2/crf-items/crf-versions/{id} | Get list of all CRF Items for specified CRF Version
[**get_crf_items_list_for_study**](CRFItemsControllerApi.md#get_crf_items_list_for_study) | **GET** /v2/crf-items | Get list of all CRF Items for specified Study
[**get_details**](CRFItemsControllerApi.md#get_details) | **GET** /v2/crf-items/{id}/{crfVersionId} | Get CRF Item details
[**get_metadata_details**](CRFItemsControllerApi.md#get_metadata_details) | **GET** /v2/crf-items/metadata/{id} | Get CRF Item metadata details
[**get_response_sets_list**](CRFItemsControllerApi.md#get_response_sets_list) | **GET** /v2/crf-items/response-sets/crf-versions/{id} | Get list of all Response Sets for specified CRF Version
[**update**](CRFItemsControllerApi.md#update) | **PUT** /v2/crf-items/{id} | Update CRF Item for current Study based on auth token provided


# **create**
> int create(token, body)

Create new CRF Item for current Study based on auth token provided

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfItemRpc() # CrfItemRpc | CRF Item Details to Save

    try:
        # Create new CRF Item for current Study based on auth token provided
        api_response = api_instance.create(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfItemRpc**](CrfItemRpc.md)| CRF Item Details to Save | 

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

# **delete**
> int delete(id, token)

Delete CRF Item for current Study based on auth token provided

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    id = 56 # int | CRF Item unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete CRF Item for current Study based on auth token provided
        api_response = api_instance.delete(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Item unique ID | 
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
**500** | Study for CRF Item not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crf_items_list**
> list[CrfItemMetadataRpc] get_crf_items_list(id, token)

Get list of all CRF Items for specified CRF Version

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Items for specified CRF Version
        api_response = api_instance.get_crf_items_list(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->get_crf_items_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[CrfItemMetadataRpc]**](CrfItemMetadataRpc.md)

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

# **get_crf_items_list_for_study**
> list[CrfItemMetadataRpc] get_crf_items_list_for_study(token)

Get list of all CRF Items for specified Study

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Items for specified Study
        api_response = api_instance.get_crf_items_list_for_study(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->get_crf_items_list_for_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[CrfItemMetadataRpc]**](CrfItemMetadataRpc.md)

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

# **get_details**
> CrfItemRpc get_details(id, crf_version_id, token)

Get CRF Item details

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    id = 56 # int | CRF Item ID
crf_version_id = 56 # int | CRF Version ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF Item details
        api_response = api_instance.get_details(id, crf_version_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Item ID | 
 **crf_version_id** | **int**| CRF Version ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**CrfItemRpc**](CrfItemRpc.md)

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
**500** | Study for CRF Item not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_details**
> CrfItemMetadataRpc get_metadata_details(id, token)

Get CRF Item metadata details

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    id = 56 # int | CRF Item metadata ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get CRF Item metadata details
        api_response = api_instance.get_metadata_details(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->get_metadata_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Item metadata ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**CrfItemMetadataRpc**](CrfItemMetadataRpc.md)

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
**500** | Study for CRF Item not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_response_sets_list**
> list[ResponseSetRpc] get_response_sets_list(id, token)

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Response Sets for specified CRF Version
        api_response = api_instance.get_response_sets_list(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->get_response_sets_list: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> int update(id, token, body)

Update CRF Item for current Study based on auth token provided

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
    api_instance = rcc.CRFItemsControllerApi(api_client)
    id = 56 # int | CRF Item unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfItemRpc() # CrfItemRpc | CRF Item Details to Save

    try:
        # Update CRF Item for current Study based on auth token provided
        api_response = api_instance.update(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsControllerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| CRF Item unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfItemRpc**](CrfItemRpc.md)| CRF Item Details to Save | 

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

