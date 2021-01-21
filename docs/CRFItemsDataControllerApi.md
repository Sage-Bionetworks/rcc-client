# rcc.CRFItemsDataControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crf_version_items_data**](CRFItemsDataControllerApi.md#get_crf_version_items_data) | **GET** /v2/items-data/crf-versions/{crfVersionId} | Get list of all CRF Items data for specified Version
[**get_filtered_items_data_list**](CRFItemsDataControllerApi.md#get_filtered_items_data_list) | **POST** /v2/items-data/filter | Get filtered list of Item Data records
[**get_subject_crf_items_data**](CRFItemsDataControllerApi.md#get_subject_crf_items_data) | **GET** /v2/items-data/subjects/{subjectId} | Get list of all CRF Items Data for specified Subject
[**get_subject_crf_items_data1**](CRFItemsDataControllerApi.md#get_subject_crf_items_data1) | **GET** /v2/items-data | Get list of all CRF Items Data for specified Study
[**get_subject_crf_items_data2**](CRFItemsDataControllerApi.md#get_subject_crf_items_data2) | **GET** /v2/items-data/subjects/{subjectId}/crf-versions/{crfVersionId} | Get list of all CRF Items Data for specified Subject and CRF Version
[**save_subject_crf_items_data**](CRFItemsDataControllerApi.md#save_subject_crf_items_data) | **POST** /v2/items-data/save | Save list of some CRF Items Data for some concrete Subject, Event Definition and CRF Version.
[**save_subjects_crf_items_data**](CRFItemsDataControllerApi.md#save_subjects_crf_items_data) | **POST** /v2/items-data/save/batch | Save list of some CRF Items Data. You can use different Subjects, Event Definitions, CRFs etc. Number of updated items is not limited.


# **get_crf_version_items_data**
> list[ItemDataValueViewRpc] get_crf_version_items_data(crf_version_id, token)

Get list of all CRF Items data for specified Version

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    crf_version_id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Items data for specified Version
        api_response = api_instance.get_crf_version_items_data(crf_version_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->get_crf_version_items_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crf_version_id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ItemDataValueViewRpc]**](ItemDataValueViewRpc.md)

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

# **get_filtered_items_data_list**
> list[SubjectMatrixValuesRpc] get_filtered_items_data_list(token, body)

Get filtered list of Item Data records

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.ItemDataFilter() # ItemDataFilter | Filtering details

    try:
        # Get filtered list of Item Data records
        api_response = api_instance.get_filtered_items_data_list(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->get_filtered_items_data_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**ItemDataFilter**](ItemDataFilter.md)| Filtering details | 

### Return type

[**list[SubjectMatrixValuesRpc]**](SubjectMatrixValuesRpc.md)

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

# **get_subject_crf_items_data**
> list[ItemDataValueViewRpc] get_subject_crf_items_data(subject_id, token)

Get list of all CRF Items Data for specified Subject

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    subject_id = 56 # int | Subject unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Items Data for specified Subject
        api_response = api_instance.get_subject_crf_items_data(subject_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->get_subject_crf_items_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **int**| Subject unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ItemDataValueViewRpc]**](ItemDataValueViewRpc.md)

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

# **get_subject_crf_items_data1**
> list[ItemDataValueViewRpc] get_subject_crf_items_data1(token)

Get list of all CRF Items Data for specified Study

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Items Data for specified Study
        api_response = api_instance.get_subject_crf_items_data1(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->get_subject_crf_items_data1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ItemDataValueViewRpc]**](ItemDataValueViewRpc.md)

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

# **get_subject_crf_items_data2**
> list[ItemDataValueViewRpc] get_subject_crf_items_data2(subject_id, crf_version_id, token)

Get list of all CRF Items Data for specified Subject and CRF Version

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    subject_id = 56 # int | Subject unique ID
crf_version_id = 56 # int | CRF Version unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all CRF Items Data for specified Subject and CRF Version
        api_response = api_instance.get_subject_crf_items_data2(subject_id, crf_version_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->get_subject_crf_items_data2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **int**| Subject unique ID | 
 **crf_version_id** | **int**| CRF Version unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[ItemDataValueViewRpc]**](ItemDataValueViewRpc.md)

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

# **save_subject_crf_items_data**
> list[IdMapItem] save_subject_crf_items_data(token, body)

Save list of some CRF Items Data for some concrete Subject, Event Definition and CRF Version.

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SubjectMatrixValuesRpc() # SubjectMatrixValuesRpc | Subject matrix values for corresponding CRF form

    try:
        # Save list of some CRF Items Data for some concrete Subject, Event Definition and CRF Version.
        api_response = api_instance.save_subject_crf_items_data(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->save_subject_crf_items_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SubjectMatrixValuesRpc**](SubjectMatrixValuesRpc.md)| Subject matrix values for corresponding CRF form | 

### Return type

[**list[IdMapItem]**](IdMapItem.md)

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

# **save_subjects_crf_items_data**
> BatchResult save_subjects_crf_items_data(token, body)

Save list of some CRF Items Data. You can use different Subjects, Event Definitions, CRFs etc. Number of updated items is not limited.

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
    api_instance = rcc.CRFItemsDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.SubjectMatrixValuesRpc()] # list[SubjectMatrixValuesRpc] | Collection of Subject matrix values for CRF form

    try:
        # Save list of some CRF Items Data. You can use different Subjects, Event Definitions, CRFs etc. Number of updated items is not limited.
        api_response = api_instance.save_subjects_crf_items_data(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CRFItemsDataControllerApi->save_subjects_crf_items_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[SubjectMatrixValuesRpc]**](SubjectMatrixValuesRpc.md)| Collection of Subject matrix values for CRF form | 

### Return type

[**BatchResult**](BatchResult.md)

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

