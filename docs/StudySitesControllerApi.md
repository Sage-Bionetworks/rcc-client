# rcc.StudySitesControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create12**](StudySitesControllerApi.md#create12) | **POST** /v2/study/sites | Create new Study Site for current Study based on auth token provided
[**delete9**](StudySitesControllerApi.md#delete9) | **DELETE** /v2/study/sites/{id} | Delete Survey for current Study based on auth token provided
[**get_details9**](StudySitesControllerApi.md#get_details9) | **GET** /v2/study/sites/{id} | Get specified Study Site details
[**get_list10**](StudySitesControllerApi.md#get_list10) | **GET** /v2/study/sites | Get list of all Study Sites for specified Study
[**update11**](StudySitesControllerApi.md#update11) | **PUT** /v2/study/sites/{id} | Update Study Site for current Study based on auth token provided


# **create12**
> int create12(token, body)

Create new Study Site for current Study based on auth token provided

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
    api_instance = rcc.StudySitesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudySiteRpc() # StudySiteRpc | Study Site Details to Save

    try:
        # Create new Study Site for current Study based on auth token provided
        api_response = api_instance.create12(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudySitesControllerApi->create12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudySiteRpc**](StudySiteRpc.md)| Study Site Details to Save | 

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
**500** | You do not have permissions for requested resource/operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete9**
> int delete9(id, token)

Delete Survey for current Study based on auth token provided

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
    api_instance = rcc.StudySitesControllerApi(api_client)
    id = 56 # int | Study Site unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Survey for current Study based on auth token provided
        api_response = api_instance.delete9(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudySitesControllerApi->delete9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Site unique ID | 
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

# **get_details9**
> get_details9(id, token)

Get specified Study Site details

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
    api_instance = rcc.StudySitesControllerApi(api_client)
    id = 56 # int | Study Site ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get specified Study Site details
        api_instance.get_details9(id, token)
    except ApiException as e:
        print("Exception when calling StudySitesControllerApi->get_details9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Site ID | 
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
**500** | Study for Study Site not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list10**
> list[StudySiteViewRpc] get_list10(token)

Get list of all Study Sites for specified Study

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
    api_instance = rcc.StudySitesControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Study Sites for specified Study
        api_response = api_instance.get_list10(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudySitesControllerApi->get_list10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[StudySiteViewRpc]**](StudySiteViewRpc.md)

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

# **update11**
> int update11(id, token, body)

Update Study Site for current Study based on auth token provided

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
    api_instance = rcc.StudySitesControllerApi(api_client)
    id = 56 # int | Study Site unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.StudySiteRpc() # StudySiteRpc | Study Site Details to Save

    try:
        # Update Study Site for current Study based on auth token provided
        api_response = api_instance.update11(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudySitesControllerApi->update11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Site unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**StudySiteRpc**](StudySiteRpc.md)| Study Site Details to Save | 

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

