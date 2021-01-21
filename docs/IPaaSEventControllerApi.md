# rcc.IPaaSEventControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_prepare_encounter**](IPaaSEventControllerApi.md#batch_prepare_encounter) | **POST** /v2/integration/study-events/batch/prepare | Prepares subject event or event CRF to be stored in RCC. No changes will be reflected in RCC immediately. This is an intermediate operation.
[**batch_save_encounter**](IPaaSEventControllerApi.md#batch_save_encounter) | **POST** /v2/integration/study-events/batch/save | Submits prepared subject events and event CRFs making them visible in RCC. This is a terminal operation.
[**bulk_save_encounter**](IPaaSEventControllerApi.md#bulk_save_encounter) | **POST** /v2/integration/study-events/bulk | Mass insert of subject events and event CRFs
[**save_encounter**](IPaaSEventControllerApi.md#save_encounter) | **POST** /v2/integration/study-events | Inserts subject event or event CRF.


# **batch_prepare_encounter**
> EhrEncounterRequiredDto batch_prepare_encounter(token, body)

Prepares subject event or event CRF to be stored in RCC. No changes will be reflected in RCC immediately. This is an intermediate operation.

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
    api_instance = rcc.IPaaSEventControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EhrEncounterRequiredDto() # EhrEncounterRequiredDto | Encounter data.

    try:
        # Prepares subject event or event CRF to be stored in RCC. No changes will be reflected in RCC immediately. This is an intermediate operation.
        api_response = api_instance.batch_prepare_encounter(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSEventControllerApi->batch_prepare_encounter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EhrEncounterRequiredDto**](EhrEncounterRequiredDto.md)| Encounter data. | 

### Return type

[**EhrEncounterRequiredDto**](EhrEncounterRequiredDto.md)

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

# **batch_save_encounter**
> list[EhrEncounterRequiredDto] batch_save_encounter(token)

Submits prepared subject events and event CRFs making them visible in RCC. This is a terminal operation.

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
    api_instance = rcc.IPaaSEventControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Submits prepared subject events and event CRFs making them visible in RCC. This is a terminal operation.
        api_response = api_instance.batch_save_encounter(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSEventControllerApi->batch_save_encounter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

### Return type

[**list[EhrEncounterRequiredDto]**](EhrEncounterRequiredDto.md)

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

# **bulk_save_encounter**
> bulk_save_encounter(token, body)

Mass insert of subject events and event CRFs

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
    api_instance = rcc.IPaaSEventControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.EhrEncounterRequiredDto()] # list[EhrEncounterRequiredDto] | Encounters data.

    try:
        # Mass insert of subject events and event CRFs
        api_instance.bulk_save_encounter(token, body)
    except ApiException as e:
        print("Exception when calling IPaaSEventControllerApi->bulk_save_encounter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[EhrEncounterRequiredDto]**](EhrEncounterRequiredDto.md)| Encounters data. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_encounter**
> list[EhrEncounterRequiredDto] save_encounter(token, body)

Inserts subject event or event CRF.

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
    api_instance = rcc.IPaaSEventControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.EhrEncounterRequiredDto() # EhrEncounterRequiredDto | Encounter data.

    try:
        # Inserts subject event or event CRF.
        api_response = api_instance.save_encounter(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IPaaSEventControllerApi->save_encounter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**EhrEncounterRequiredDto**](EhrEncounterRequiredDto.md)| Encounter data. | 

### Return type

[**list[EhrEncounterRequiredDto]**](EhrEncounterRequiredDto.md)

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

