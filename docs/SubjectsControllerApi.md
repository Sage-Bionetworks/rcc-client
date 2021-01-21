# rcc.SubjectsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create13**](SubjectsControllerApi.md#create13) | **POST** /v2/subjects | Create new Subject for current Study based on auth token provided
[**create_batch**](SubjectsControllerApi.md#create_batch) | **POST** /v2/subjects/batch | Batch create new Subjects for current Study based on auth token provided
[**delete10**](SubjectsControllerApi.md#delete10) | **DELETE** /v2/subjects/{id} | Delete Subject for current Study based on auth token provided
[**export_subject_by_enrolled_date**](SubjectsControllerApi.md#export_subject_by_enrolled_date) | **GET** /v2/subjects/filter | Get list of Subjects by Enrolled Date for specified Study
[**filter_subjects**](SubjectsControllerApi.md#filter_subjects) | **POST** /v2/subjects/filter | Get list of Subjects for Filter
[**get_details10**](SubjectsControllerApi.md#get_details10) | **GET** /v2/subjects/{id} | Get specified Subject details
[**get_list11**](SubjectsControllerApi.md#get_list11) | **GET** /v2/subjects | Get list of all Subjects for specified Study
[**get_list_for_site**](SubjectsControllerApi.md#get_list_for_site) | **GET** /v2/subjects/sites/{studySiteId} | Get list of all Subjects for specified Study Site
[**update12**](SubjectsControllerApi.md#update12) | **PUT** /v2/subjects/{id} | Update Subject for current Study based on auth token provided
[**update_batch**](SubjectsControllerApi.md#update_batch) | **PUT** /v2/subjects/batch | Butch update Subjects List for current Study based on auth token provided


# **create13**
> int create13(token, body)

Create new Subject for current Study based on auth token provided

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SubjectRpc() # SubjectRpc | Subject Details to Save

    try:
        # Create new Subject for current Study based on auth token provided
        api_response = api_instance.create13(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->create13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SubjectRpc**](SubjectRpc.md)| Subject Details to Save | 

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
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch**
> BatchResult create_batch(token, body)

Batch create new Subjects for current Study based on auth token provided

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.SubjectRpc()] # list[SubjectRpc] | Subjects List to Save

    try:
        # Batch create new Subjects for current Study based on auth token provided
        api_response = api_instance.create_batch(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->create_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[SubjectRpc]**](SubjectRpc.md)| Subjects List to Save | 

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
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete10**
> int delete10(id, token)

Delete Subject for current Study based on auth token provided

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    id = 56 # int | Subject unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Subject for current Study based on auth token provided
        api_response = api_instance.delete10(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->delete10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subject unique ID | 
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
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_subject_by_enrolled_date**
> export_subject_by_enrolled_date(token, enrollment_date=enrollment_date, page_size=page_size, page_number=page_number)

Get list of Subjects by Enrolled Date for specified Study

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
enrollment_date = 'enrollment_date_example' # str | All data from subjects with enrollmentDate. Format: <b>2019-12-10</b> (optional)
page_size = 1000 # int | Count of records per page (optional) (default to 1000)
page_number = 1 # int | Current number of page (optional) (default to 1)

    try:
        # Get list of Subjects by Enrolled Date for specified Study
        api_instance.export_subject_by_enrolled_date(token, enrollment_date=enrollment_date, page_size=page_size, page_number=page_number)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->export_subject_by_enrolled_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **enrollment_date** | **str**| All data from subjects with enrollmentDate. Format: &lt;b&gt;2019-12-10&lt;/b&gt; | [optional] 
 **page_size** | **int**| Count of records per page | [optional] [default to 1000]
 **page_number** | **int**| Current number of page | [optional] [default to 1]

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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_subjects**
> list[SubjectViewRpc] filter_subjects(token, body)

Get list of Subjects for Filter

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SubjectsFilter() # SubjectsFilter | Study site ID

    try:
        # Get list of Subjects for Filter
        api_response = api_instance.filter_subjects(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->filter_subjects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SubjectsFilter**](SubjectsFilter.md)| Study site ID | 

### Return type

[**list[SubjectViewRpc]**](SubjectViewRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details10**
> SubjectRpc get_details10(id, token)

Get specified Subject details

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    id = 56 # int | Subject ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get specified Subject details
        api_response = api_instance.get_details10(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->get_details10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subject ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**SubjectRpc**](SubjectRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list11**
> list[SubjectViewRpc] get_list11(token)

Get list of all Subjects for specified Study

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Subjects for specified Study
        api_response = api_instance.get_list11(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->get_list11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SubjectViewRpc]**](SubjectViewRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_for_site**
> list[SubjectViewRpc] get_list_for_site(study_site_id, token)

Get list of all Subjects for specified Study Site

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    study_site_id = 56 # int | Study site ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Subjects for specified Study Site
        api_response = api_instance.get_list_for_site(study_site_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->get_list_for_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_site_id** | **int**| Study site ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SubjectViewRpc]**](SubjectViewRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update12**
> int update12(id, token, body)

Update Subject for current Study based on auth token provided

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    id = 56 # int | Subject unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SubjectRpc() # SubjectRpc | Subject Details to Save

    try:
        # Update Subject for current Study based on auth token provided
        api_response = api_instance.update12(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->update12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subject unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SubjectRpc**](SubjectRpc.md)| Subject Details to Save | 

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
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_batch**
> BatchResult update_batch(token, body)

Butch update Subjects List for current Study based on auth token provided

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
    api_instance = rcc.SubjectsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.SubjectRpc()] # list[SubjectRpc] | Subjects List to Save

    try:
        # Butch update Subjects List for current Study based on auth token provided
        api_response = api_instance.update_batch(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubjectsControllerApi->update_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[SubjectRpc]**](SubjectRpc.md)| Subjects List to Save | 

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
**200** | Success |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | You do not have permissions for requested resource/operation. |  -  |
**500** | Server error occurred while processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

