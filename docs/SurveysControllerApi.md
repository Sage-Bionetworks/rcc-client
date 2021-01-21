# rcc.SurveysControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create14**](SurveysControllerApi.md#create14) | **POST** /v2/surveys | Create new Survey for current Study based on auth token provided
[**delete11**](SurveysControllerApi.md#delete11) | **DELETE** /v2/surveys/{id} | Delete Survey for current Study based on auth token provided
[**get_details11**](SurveysControllerApi.md#get_details11) | **GET** /v2/surveys/{id} | Get specified Survey details
[**get_filtered_survey_links**](SurveysControllerApi.md#get_filtered_survey_links) | **POST** /v2/surveys/links | Get filtered list of Survey Links
[**get_list12**](SurveysControllerApi.md#get_list12) | **GET** /v2/surveys | Get list of all Surveys for specified Study
[**get_study_event_definitions_list**](SurveysControllerApi.md#get_study_event_definitions_list) | **GET** /v2/surveys/event-definitions | Get list of all Event Definitions for specified Study
[**get_survey_event_definitions_list**](SurveysControllerApi.md#get_survey_event_definitions_list) | **GET** /v2/surveys/{id}/event-definitions | Get list of all Survey Event Definitions for specified Study
[**update13**](SurveysControllerApi.md#update13) | **PUT** /v2/surveys/{id} | Update Survey for current Study based on auth token provided


# **create14**
> int create14(token, body)

Create new Survey for current Study based on auth token provided

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
    api_instance = rcc.SurveysControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SurveyRpc() # SurveyRpc | Survey Details to Save

    try:
        # Create new Survey for current Study based on auth token provided
        api_response = api_instance.create14(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->create14: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SurveyRpc**](SurveyRpc.md)| Survey Details to Save | 

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

# **delete11**
> int delete11(id, token)

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
    api_instance = rcc.SurveysControllerApi(api_client)
    id = 56 # int | Survey unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Delete Survey for current Study based on auth token provided
        api_response = api_instance.delete11(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->delete11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Survey unique ID | 
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

# **get_details11**
> get_details11(id, token)

Get specified Survey details

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
    api_instance = rcc.SurveysControllerApi(api_client)
    id = 56 # int | Survey ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get specified Survey details
        api_instance.get_details11(id, token)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->get_details11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Survey ID | 
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
**500** | Study for Survey not match specified Token! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_survey_links**
> SurveyLinksRecordsResultRpc get_filtered_survey_links(token, body)

Get filtered list of Survey Links

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
    api_instance = rcc.SurveysControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SurveyLinkFilter() # SurveyLinkFilter | Survey Links filter

    try:
        # Get filtered list of Survey Links
        api_response = api_instance.get_filtered_survey_links(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->get_filtered_survey_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SurveyLinkFilter**](SurveyLinkFilter.md)| Survey Links filter | 

### Return type

[**SurveyLinksRecordsResultRpc**](SurveyLinksRecordsResultRpc.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Too much page size value. |  -  |
**401** | User Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list12**
> list[SurveyViewRpc] get_list12(token)

Get list of all Surveys for specified Study

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
    api_instance = rcc.SurveysControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Surveys for specified Study
        api_response = api_instance.get_list12(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->get_list12: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SurveyViewRpc]**](SurveyViewRpc.md)

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

# **get_study_event_definitions_list**
> list[SurveyEventDefinitionViewRpc] get_study_event_definitions_list(token)

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
    api_instance = rcc.SurveysControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Definitions for specified Study
        api_response = api_instance.get_study_event_definitions_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->get_study_event_definitions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SurveyEventDefinitionViewRpc]**](SurveyEventDefinitionViewRpc.md)

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

# **get_survey_event_definitions_list**
> list[SurveyEventDefinitionViewRpc] get_survey_event_definitions_list(id, token)

Get list of all Survey Event Definitions for specified Study

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
    api_instance = rcc.SurveysControllerApi(api_client)
    id = 56 # int | Survey unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Survey Event Definitions for specified Study
        api_response = api_instance.get_survey_event_definitions_list(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->get_survey_event_definitions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Survey unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[SurveyEventDefinitionViewRpc]**](SurveyEventDefinitionViewRpc.md)

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

# **update13**
> int update13(id, token, body)

Update Survey for current Study based on auth token provided

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
    api_instance = rcc.SurveysControllerApi(api_client)
    id = 56 # int | Survey unique ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.SurveyRpc() # SurveyRpc | Survey Details to Save

    try:
        # Update Survey for current Study based on auth token provided
        api_response = api_instance.update13(id, token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SurveysControllerApi->update13: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Survey unique ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**SurveyRpc**](SurveyRpc.md)| Survey Details to Save | 

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

