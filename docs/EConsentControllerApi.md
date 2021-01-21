# rcc.EConsentControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_event_crf_id**](EConsentControllerApi.md#get_by_event_crf_id) | **GET** /v2/e-consent/subjectId/{id} | Get info by subject ID
[**get_e_consent_crf_pdf_by_subject_id**](EConsentControllerApi.md#get_e_consent_crf_pdf_by_subject_id) | **GET** /v2/e-consent/pdf/subjectId/{id} | Get PDF file with eConsent CRFs by subject ID


# **get_by_event_crf_id**
> EConsentInfoRpc get_by_event_crf_id(id, token)

Get info by subject ID

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
    api_instance = rcc.EConsentControllerApi(api_client)
    id = 56 # int | Subject ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get info by subject ID
        api_response = api_instance.get_by_event_crf_id(id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EConsentControllerApi->get_by_event_crf_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subject ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**EConsentInfoRpc**](EConsentInfoRpc.md)

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

# **get_e_consent_crf_pdf_by_subject_id**
> get_e_consent_crf_pdf_by_subject_id(id, token)

Get PDF file with eConsent CRFs by subject ID

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
    api_instance = rcc.EConsentControllerApi(api_client)
    id = 56 # int | Subject ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get PDF file with eConsent CRFs by subject ID
        api_instance.get_e_consent_crf_pdf_by_subject_id(id, token)
    except ApiException as e:
        print("Exception when calling EConsentControllerApi->get_e_consent_crf_pdf_by_subject_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subject ID | 
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
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

