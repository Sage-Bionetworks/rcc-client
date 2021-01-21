# rcc.SitesControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create7**](SitesControllerApi.md#create7) | **POST** /v2/sites | Create new site based on details object and tenant API key
[**delete5**](SitesControllerApi.md#delete5) | **DELETE** /v2/sites/{id} | Delete site
[**get_details5**](SitesControllerApi.md#get_details5) | **GET** /v2/sites/{id} | Get site details using its ID
[**get_list6**](SitesControllerApi.md#get_list6) | **GET** /v2/sites | Get list of all sites for tenant user
[**get_site_types**](SitesControllerApi.md#get_site_types) | **GET** /v2/sites/types | Get list of all available site types
[**get_time_zones**](SitesControllerApi.md#get_time_zones) | **GET** /v2/sites/time-zones | Get list of all available time zones for tenant sites
[**patch2**](SitesControllerApi.md#patch2) | **PATCH** /v2/sites/{id} | Update some specific site fields
[**update6**](SitesControllerApi.md#update6) | **PUT** /v2/sites/{id} | Update Site details based on auth token provided


# **create7**
> int create7(token, body)

Create new site based on details object and tenant API key

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
    api_instance = rcc.SitesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.
body = rcc.SiteRpc() # SiteRpc | Site details object

    try:
        # Create new site based on details object and tenant API key
        api_response = api_instance.create7(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->create7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 
 **body** | [**SiteRpc**](SiteRpc.md)| Site details object | 

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
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | You do not have setup rights for this tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete5**
> int delete5(id, token)

Delete site

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
    api_instance = rcc.SitesControllerApi(api_client)
    id = 56 # int | Site unique ID
token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Delete site
        api_response = api_instance.delete5(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->delete5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site unique ID | 
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

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
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | You do not have setup rights for this tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details5**
> SiteRpc get_details5(id, token)

Get site details using its ID

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
    api_instance = rcc.SitesControllerApi(api_client)
    id = 56 # int | Site unique ID
token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get site details using its ID
        api_response = api_instance.get_details5(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->get_details5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site unique ID | 
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

### Return type

[**SiteRpc**](SiteRpc.md)

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

# **get_list6**
> list[SiteViewRpc] get_list6(token)

Get list of all sites for tenant user

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
    api_instance = rcc.SitesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get list of all sites for tenant user
        api_response = api_instance.get_list6(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->get_list6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

### Return type

[**list[SiteViewRpc]**](SiteViewRpc.md)

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

# **get_site_types**
> list[GenericItem] get_site_types(token)

Get list of all available site types

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
    api_instance = rcc.SitesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get list of all available site types
        api_response = api_instance.get_site_types(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->get_site_types: %s\n" % e)
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

# **get_time_zones**
> list[GenericItem] get_time_zones(token)

Get list of all available time zones for tenant sites

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
    api_instance = rcc.SitesControllerApi(api_client)
    token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get list of all available time zones for tenant sites
        api_response = api_instance.get_time_zones(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->get_time_zones: %s\n" % e)
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

# **patch2**
> int patch2(id, token, body)

Update some specific site fields

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
    api_instance = rcc.SitesControllerApi(api_client)
    id = 56 # int | Site unique ID
token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.
body = rcc.PatchObject() # PatchObject | Site details object

    try:
        # Update some specific site fields
        api_response = api_instance.patch2(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->patch2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site unique ID | 
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 
 **body** | [**PatchObject**](PatchObject.md)| Site details object | 

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
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | Site not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update6**
> int update6(id, token, body)

Update Site details based on auth token provided

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
    api_instance = rcc.SitesControllerApi(api_client)
    id = 56 # int | Site unique ID
token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.
body = rcc.SiteRpc() # SiteRpc | Site details object

    try:
        # Update Site details based on auth token provided
        api_response = api_instance.update6(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SitesControllerApi->update6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site unique ID | 
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 
 **body** | [**SiteRpc**](SiteRpc.md)| Site details object | 

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
**403** | Token is not allowed for IMPORT/SAVE operations. |  -  |
**500** | You do not have setup rights for this tenant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

