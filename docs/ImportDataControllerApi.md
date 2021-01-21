# rcc.ImportDataControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_csv**](ImportDataControllerApi.md#import_csv) | **POST** /v2/import/csv | Import list of user Records for specified Study
[**import_metadata**](ImportDataControllerApi.md#import_metadata) | **POST** /v2/import/metadata | Import Metadata for specified Study
[**import_odm**](ImportDataControllerApi.md#import_odm) | **POST** /v2/import/odm | Import list of user Records for specified Study
[**import_odm_string_inflated_to_tenant**](ImportDataControllerApi.md#import_odm_string_inflated_to_tenant) | **POST** /v2/import/odm/extended-inflated | Import full Study using ODM (SDM Extended Data)
[**import_odm_to_tenant**](ImportDataControllerApi.md#import_odm_to_tenant) | **POST** /v2/import/odm/extended | Import full Study using ODM (SDM Extended Data)
[**import_records**](ImportDataControllerApi.md#import_records) | **POST** /v2/import/records | Import list of user Records for specified Study
[**survey_assignments**](ImportDataControllerApi.md#survey_assignments) | **POST** /v2/import/survey-assignments | Import list of Survey Assignments Records for specified Study


# **import_csv**
> list[StudyEventRecord] import_csv(token, body, create_discrepancy=create_discrepancy, send_email=send_email, hide_crf=hide_crf, hide_crf_section=hide_crf_section, create_dynamic_event=create_dynamic_event, remove_dynamic_event=remove_dynamic_event, add_crf=add_crf, send_notification=send_notification, generate_schedule=generate_schedule, skip_rules_run=skip_rules_run, disable_emails_and_notifications=disable_emails_and_notifications)

Import list of user Records for specified Study

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = 'body_example' # str | Records Collection in CSV format
create_discrepancy = True # bool | Enables Create Query rule runs on imported data (optional)
send_email = True # bool | Enables Send e-mail rule runs on imported data (optional)
hide_crf = True # bool | Enables Hide CRF rule runs on imported data (optional)
hide_crf_section = True # bool | Enables Hide CRFs Sections rule runs on imported data (optional)
create_dynamic_event = True # bool | Enables Create Dynamic Event rule runs on imported data (optional)
remove_dynamic_event = True # bool | Enables Remove Dynamic Event rule runs on imported data (optional)
add_crf = True # bool | Enables Add CRF rule runs on imported data (optional)
send_notification = True # bool | Enables Send Notification rule runs on imported data (optional)
generate_schedule = True # bool | Enables Schedule Calendared Events rule runs on imported data (optional)
skip_rules_run = True # bool | Skip all rule runs (optional)
disable_emails_and_notifications = True # bool | Don't send any e-mails as part of this import (optional)

    try:
        # Import list of user Records for specified Study
        api_response = api_instance.import_csv(token, body, create_discrepancy=create_discrepancy, send_email=send_email, hide_crf=hide_crf, hide_crf_section=hide_crf_section, create_dynamic_event=create_dynamic_event, remove_dynamic_event=remove_dynamic_event, add_crf=add_crf, send_notification=send_notification, generate_schedule=generate_schedule, skip_rules_run=skip_rules_run, disable_emails_and_notifications=disable_emails_and_notifications)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->import_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | **str**| Records Collection in CSV format | 
 **create_discrepancy** | **bool**| Enables Create Query rule runs on imported data | [optional] 
 **send_email** | **bool**| Enables Send e-mail rule runs on imported data | [optional] 
 **hide_crf** | **bool**| Enables Hide CRF rule runs on imported data | [optional] 
 **hide_crf_section** | **bool**| Enables Hide CRFs Sections rule runs on imported data | [optional] 
 **create_dynamic_event** | **bool**| Enables Create Dynamic Event rule runs on imported data | [optional] 
 **remove_dynamic_event** | **bool**| Enables Remove Dynamic Event rule runs on imported data | [optional] 
 **add_crf** | **bool**| Enables Add CRF rule runs on imported data | [optional] 
 **send_notification** | **bool**| Enables Send Notification rule runs on imported data | [optional] 
 **generate_schedule** | **bool**| Enables Schedule Calendared Events rule runs on imported data | [optional] 
 **skip_rules_run** | **bool**| Skip all rule runs | [optional] 
 **disable_emails_and_notifications** | **bool**| Don&#39;t send any e-mails as part of this import | [optional] 

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_metadata**
> list[Metadata] import_metadata(token, body)

Import Metadata for specified Study

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.Metadata()] # list[Metadata] | Study Metadata Collection

    try:
        # Import Metadata for specified Study
        api_response = api_instance.import_metadata(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->import_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[Metadata]**](Metadata.md)| Study Metadata Collection | 

### Return type

[**list[Metadata]**](Metadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_odm**
> list[StudyEventRecord] import_odm(token, body, create_discrepancy=create_discrepancy, send_email=send_email, hide_crf=hide_crf, hide_crf_section=hide_crf_section, create_dynamic_event=create_dynamic_event, remove_dynamic_event=remove_dynamic_event, add_crf=add_crf, send_notification=send_notification, generate_schedule=generate_schedule, skip_rules_run=skip_rules_run, disable_emails_and_notifications=disable_emails_and_notifications)

Import list of user Records for specified Study

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.ODM() # ODM | ODM model mapping
create_discrepancy = True # bool | Enables Create Query rule runs on imported data (optional)
send_email = True # bool | Enables Send e-mail rule runs on imported data (optional)
hide_crf = True # bool | Enables Hide CRF rule runs on imported data (optional)
hide_crf_section = True # bool | Enables Hide CRFs Sections rule runs on imported data (optional)
create_dynamic_event = True # bool | Enables Create Dynamic Event rule runs on imported data (optional)
remove_dynamic_event = True # bool | Enables Remove Dynamic Event rule runs on imported data (optional)
add_crf = True # bool | Enables Add CRF rule runs on imported data (optional)
send_notification = True # bool | Enables Send Notification rule runs on imported data (optional)
generate_schedule = True # bool | Enables Schedule Calendared Events rule runs on imported data (optional)
skip_rules_run = True # bool | Skip all rule runs (optional)
disable_emails_and_notifications = True # bool | Don't send any e-mails as part of this import (optional)

    try:
        # Import list of user Records for specified Study
        api_response = api_instance.import_odm(token, body, create_discrepancy=create_discrepancy, send_email=send_email, hide_crf=hide_crf, hide_crf_section=hide_crf_section, create_dynamic_event=create_dynamic_event, remove_dynamic_event=remove_dynamic_event, add_crf=add_crf, send_notification=send_notification, generate_schedule=generate_schedule, skip_rules_run=skip_rules_run, disable_emails_and_notifications=disable_emails_and_notifications)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->import_odm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**ODM**](ODM.md)| ODM model mapping | 
 **create_discrepancy** | **bool**| Enables Create Query rule runs on imported data | [optional] 
 **send_email** | **bool**| Enables Send e-mail rule runs on imported data | [optional] 
 **hide_crf** | **bool**| Enables Hide CRF rule runs on imported data | [optional] 
 **hide_crf_section** | **bool**| Enables Hide CRFs Sections rule runs on imported data | [optional] 
 **create_dynamic_event** | **bool**| Enables Create Dynamic Event rule runs on imported data | [optional] 
 **remove_dynamic_event** | **bool**| Enables Remove Dynamic Event rule runs on imported data | [optional] 
 **add_crf** | **bool**| Enables Add CRF rule runs on imported data | [optional] 
 **send_notification** | **bool**| Enables Send Notification rule runs on imported data | [optional] 
 **generate_schedule** | **bool**| Enables Schedule Calendared Events rule runs on imported data | [optional] 
 **skip_rules_run** | **bool**| Skip all rule runs | [optional] 
 **disable_emails_and_notifications** | **bool**| Don&#39;t send any e-mails as part of this import | [optional] 

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_odm_string_inflated_to_tenant**
> list[StudyEventRecord] import_odm_string_inflated_to_tenant(token, body, study_id=study_id)

Import full Study using ODM (SDM Extended Data)

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Tenant access token. Used to get current context.
body = 'body_example' # str | ODM model mapping
study_id = 56 # int |  (optional)

    try:
        # Import full Study using ODM (SDM Extended Data)
        api_response = api_instance.import_odm_string_inflated_to_tenant(token, body, study_id=study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->import_odm_string_inflated_to_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Tenant access token. Used to get current context. | 
 **body** | **str**| ODM model mapping | 
 **study_id** | **int**|  | [optional] 

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_odm_to_tenant**
> list[StudyEventRecord] import_odm_to_tenant(token, body, study_id=study_id)

Import full Study using ODM (SDM Extended Data)

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Tenant access token. Used to get current context.
body = rcc.ODM() # ODM | ODM model mapping
study_id = 56 # int |  (optional)

    try:
        # Import full Study using ODM (SDM Extended Data)
        api_response = api_instance.import_odm_to_tenant(token, body, study_id=study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->import_odm_to_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Tenant access token. Used to get current context. | 
 **body** | [**ODM**](ODM.md)| ODM model mapping | 
 **study_id** | **int**|  | [optional] 

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_records**
> list[StudyEventRecord] import_records(token, body, create_discrepancy=create_discrepancy, send_email=send_email, hide_crf=hide_crf, hide_crf_section=hide_crf_section, create_dynamic_event=create_dynamic_event, remove_dynamic_event=remove_dynamic_event, add_crf=add_crf, send_notification=send_notification, generate_schedule=generate_schedule, skip_rules_run=skip_rules_run, disable_emails_and_notifications=disable_emails_and_notifications)

Import list of user Records for specified Study

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.StudyEventRecord()] # list[StudyEventRecord] | Records Collection
create_discrepancy = True # bool | Enables Create Query rule runs on imported data (optional)
send_email = True # bool | Enables Send e-mail rule runs on imported data (optional)
hide_crf = True # bool | Enables Hide CRF rule runs on imported data (optional)
hide_crf_section = True # bool | Enables Hide CRFs Sections rule runs on imported data (optional)
create_dynamic_event = True # bool | Enables Create Dynamic Event rule runs on imported data (optional)
remove_dynamic_event = True # bool | Enables Remove Dynamic Event rule runs on imported data (optional)
add_crf = True # bool | Enables Add CRF rule runs on imported data (optional)
send_notification = True # bool | Enables Send Notification rule runs on imported data (optional)
generate_schedule = True # bool | Enables Schedule Calendared Events rule runs on imported data (optional)
skip_rules_run = True # bool | Skip all rule runs (optional)
disable_emails_and_notifications = True # bool | Don't send any e-mails as part of this import (optional)

    try:
        # Import list of user Records for specified Study
        api_response = api_instance.import_records(token, body, create_discrepancy=create_discrepancy, send_email=send_email, hide_crf=hide_crf, hide_crf_section=hide_crf_section, create_dynamic_event=create_dynamic_event, remove_dynamic_event=remove_dynamic_event, add_crf=add_crf, send_notification=send_notification, generate_schedule=generate_schedule, skip_rules_run=skip_rules_run, disable_emails_and_notifications=disable_emails_and_notifications)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->import_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[StudyEventRecord]**](StudyEventRecord.md)| Records Collection | 
 **create_discrepancy** | **bool**| Enables Create Query rule runs on imported data | [optional] 
 **send_email** | **bool**| Enables Send e-mail rule runs on imported data | [optional] 
 **hide_crf** | **bool**| Enables Hide CRF rule runs on imported data | [optional] 
 **hide_crf_section** | **bool**| Enables Hide CRFs Sections rule runs on imported data | [optional] 
 **create_dynamic_event** | **bool**| Enables Create Dynamic Event rule runs on imported data | [optional] 
 **remove_dynamic_event** | **bool**| Enables Remove Dynamic Event rule runs on imported data | [optional] 
 **add_crf** | **bool**| Enables Add CRF rule runs on imported data | [optional] 
 **send_notification** | **bool**| Enables Send Notification rule runs on imported data | [optional] 
 **generate_schedule** | **bool**| Enables Schedule Calendared Events rule runs on imported data | [optional] 
 **skip_rules_run** | **bool**| Skip all rule runs | [optional] 
 **disable_emails_and_notifications** | **bool**| Don&#39;t send any e-mails as part of this import | [optional] 

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **survey_assignments**
> list[RecordSurveyAssignment] survey_assignments(token, body)

Import list of Survey Assignments Records for specified Study

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
    api_instance = rcc.ImportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = [rcc.RecordSurveyAssignment()] # list[RecordSurveyAssignment] | Survey Assignments Collection

    try:
        # Import list of Survey Assignments Records for specified Study
        api_response = api_instance.survey_assignments(token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImportDataControllerApi->survey_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**list[RecordSurveyAssignment]**](RecordSurveyAssignment.md)| Survey Assignments Collection | 

### Return type

[**list[RecordSurveyAssignment]**](RecordSurveyAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

