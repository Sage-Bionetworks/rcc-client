# rcc.IPaaSItemDataControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_save_coded_item_data**](IPaaSItemDataControllerApi.md#bulk_save_coded_item_data) | **GET** /v2/integration/items-data/coded/aggregate | Starts processing temporary observation data for key-based repeating groups.
[**bulk_save_coded_item_data1**](IPaaSItemDataControllerApi.md#bulk_save_coded_item_data1) | **POST** /v2/integration/items-data/coded/bulk | Save a collection of values for coded CRF variables.
[**prepare_coded_item_data_for_saving**](IPaaSItemDataControllerApi.md#prepare_coded_item_data_for_saving) | **POST** /v2/integration/items-data/coded/batch/prepare | Prepare value for coded CRF variable to be stored in RCC. No changes will be reflected in RCC. This is an intermediate operation.
[**save_coded_item_data**](IPaaSItemDataControllerApi.md#save_coded_item_data) | **POST** /v2/integration/items-data/coded/batch/save | Submit prepared values for coded CRF variables making them visible in RCC. This is a terminal operation.
[**save_coded_item_data1**](IPaaSItemDataControllerApi.md#save_coded_item_data1) | **POST** /v2/integration/items-data/coded | Save value for coded CRF variable.
[**save_named_item_data**](IPaaSItemDataControllerApi.md#save_named_item_data) | **POST** /v2/integration/items-data | Save values for named CRF variables.


# **bulk_save_coded_item_data**
> list[ResponseInfo] bulk_save_coded_item_data(token)

Starts processing temporary observation data for key-based repeating groups.

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
    api_instance = rcc.IPaaSItemDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Starts processing temporary observation data for key-based repeating groups.
        api_response = api_instance.bulk_save_coded_item_data(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemDataControllerApi->bulk_save_coded_item_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ResponseInfo]**](ResponseInfo.md)

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

# **bulk_save_coded_item_data1**
> list[ResponseInfo] bulk_save_coded_item_data1(token, body)

Save a collection of values for coded CRF variables.

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
    api_instance = rcc.IPaaSItemDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.EhrObservationDto()] # list[EhrObservationDto] | CRF coded variables values

    try:
        # Save a collection of values for coded CRF variables.
        api_response = api_instance.bulk_save_coded_item_data1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemDataControllerApi->bulk_save_coded_item_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[EhrObservationDto]**](EhrObservationDto.md)| CRF coded variables values | 

### Return type

[**list[ResponseInfo]**](ResponseInfo.md)

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

# **prepare_coded_item_data_for_saving**
> ResponseInfo prepare_coded_item_data_for_saving(token, body)

Prepare value for coded CRF variable to be stored in RCC. No changes will be reflected in RCC. This is an intermediate operation.

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
    api_instance = rcc.IPaaSItemDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EhrObservationDto() # EhrObservationDto | CRF coded variable value

    try:
        # Prepare value for coded CRF variable to be stored in RCC. No changes will be reflected in RCC. This is an intermediate operation.
        api_response = api_instance.prepare_coded_item_data_for_saving(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemDataControllerApi->prepare_coded_item_data_for_saving: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EhrObservationDto**](EhrObservationDto.md)| CRF coded variable value | 

### Return type

[**ResponseInfo**](ResponseInfo.md)

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

# **save_coded_item_data**
> list[ResponseInfo] save_coded_item_data(token)

Submit prepared values for coded CRF variables making them visible in RCC. This is a terminal operation.

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
    api_instance = rcc.IPaaSItemDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Submit prepared values for coded CRF variables making them visible in RCC. This is a terminal operation.
        api_response = api_instance.save_coded_item_data(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemDataControllerApi->save_coded_item_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ResponseInfo]**](ResponseInfo.md)

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

# **save_coded_item_data1**
> ResponseInfo save_coded_item_data1(token, body)

Save value for coded CRF variable.

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
    api_instance = rcc.IPaaSItemDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EhrObservationDto() # EhrObservationDto | CRF coded variable value

    try:
        # Save value for coded CRF variable.
        api_response = api_instance.save_coded_item_data1(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemDataControllerApi->save_coded_item_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EhrObservationDto**](EhrObservationDto.md)| CRF coded variable value | 

### Return type

[**ResponseInfo**](ResponseInfo.md)

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

# **save_named_item_data**
> list[ResponseInfo] save_named_item_data(token, body)

Save values for named CRF variables.

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
    api_instance = rcc.IPaaSItemDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.CrfVariablesValueRpc() # CrfVariablesValueRpc | CRF named variables values

    try:
        # Save values for named CRF variables.
        api_response = api_instance.save_named_item_data(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSItemDataControllerApi->save_named_item_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**CrfVariablesValueRpc**](CrfVariablesValueRpc.md)| CRF named variables values | 

### Return type

[**list[ResponseInfo]**](ResponseInfo.md)

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

