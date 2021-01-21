# rcc.AuditLogsControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_codes_event_type_list**](AuditLogsControllerApi.md#get_audit_codes_event_type_list) | **GET** /v2/audit-logs/event-types | Get list of all Event Types in Audit log
[**get_audit_log_items_list**](AuditLogsControllerApi.md#get_audit_log_items_list) | **POST** /v2/audit-logs/filter | Get filtered list of Audit log records


# **get_audit_codes_event_type_list**
> list[GenericItem] get_audit_codes_event_type_list(token)

Get list of all Event Types in Audit log

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
    api_instance = rcc.AuditLogsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get list of all Event Types in Audit log
        api_response = api_instance.get_audit_codes_event_type_list(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuditLogsControllerApi->get_audit_codes_event_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 

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
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_items_list**
> AuditLogRecordsResultRpc get_audit_log_items_list(token, body)

Get filtered list of Audit log records

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
    api_instance = rcc.AuditLogsControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.AuditLogFilter() # AuditLogFilter | Subject Details to Save

    try:
        # Get filtered list of Audit log records
        api_response = api_instance.get_audit_log_items_list(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuditLogsControllerApi->get_audit_log_items_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**AuditLogFilter**](AuditLogFilter.md)| Subject Details to Save | 

### Return type

[**AuditLogRecordsResultRpc**](AuditLogRecordsResultRpc.md)

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

