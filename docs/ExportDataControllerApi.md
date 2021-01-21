# rcc.ExportDataControllerApi

All URIs are relative to *http://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_all_records_csv**](ExportDataControllerApi.md#export_all_records_csv) | **GET** /v2/export/records | Get list of user Records for specified Study
[**export_all_records_json2**](ExportDataControllerApi.md#export_all_records_json2) | **GET** /v2/export/records/json | Get list of user Records for specified Study
[**export_all_records_odm**](ExportDataControllerApi.md#export_all_records_odm) | **GET** /v2/export/odm | Get Study definitions in ODM format
[**export_all_records_xml2**](ExportDataControllerApi.md#export_all_records_xml2) | **GET** /v2/export/records/xml | Get list of user Records for specified Study
[**export_all_site_records_csv**](ExportDataControllerApi.md#export_all_site_records_csv) | **GET** /v2/export/records/{id} | Get list of user Records for specified Study Site
[**export_all_site_records_odm**](ExportDataControllerApi.md#export_all_site_records_odm) | **GET** /v2/export/odm/{id} | Get definitions in ODM format for specified Study Site
[**export_extended_records_odm_for_tenant_study**](ExportDataControllerApi.md#export_extended_records_odm_for_tenant_study) | **GET** /v2/export/odm/extended | Get definitions in ODM (SDM Extended Data) format for specified Tenant Study
[**export_extended_records_odm_for_tenant_study_post**](ExportDataControllerApi.md#export_extended_records_odm_for_tenant_study_post) | **POST** /v2/export/odm/extended | Get definitions in ODM (SDM Extended Data) format for specified Tenant Study
[**export_records_csv**](ExportDataControllerApi.md#export_records_csv) | **POST** /v2/export/records | Get list of user Records for specified Study and filters
[**export_records_odm**](ExportDataControllerApi.md#export_records_odm) | **POST** /v2/export/odm | Get list of user Records for specified Study and filters (Snapshot ODM Export)
[**export_records_todm**](ExportDataControllerApi.md#export_records_todm) | **POST** /v2/export/todm | Get list of user Records for specified Study and filters (Transactional ODM Export)


# **export_all_records_csv**
> str export_all_records_csv(token, generate_metadata=generate_metadata, use_concept_value=use_concept_value, export_empty_values=export_empty_values, date_from=date_from, date_to=date_to, extract_data_delta=extract_data_delta)

Get list of user Records for specified Study

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
generate_metadata = False # bool | Need to generate metadata for records (optional) (default to False)
use_concept_value = False # bool | Use Concept terms instead of Verbatim terms (optional) (default to False)
export_empty_values = False # bool | Use Empty values instead of null-value (optional) (default to False)
date_from = 'date_from_example' # str | All data from subjects with enrollmentDate &gt;= dateFrom. Format: <b>2019-12-10</b> or <b>2019-12-10 10:20</b> (optional)
date_to = 'date_to_example' # str | All data from subjects with enrollmentDate &lt;= dateTo. Format: <b>2019-12-10</b>  or <b>2019-12-10 10:20</b>  (optional)
extract_data_delta = False # bool | By default dateFrom & dateTo are used to extract all subjects and its data with enrollmentDate between those dates. Use this parameter if you want to extract data that was inserted / updated between those dates. (optional) (default to False)

    try:
        # Get list of user Records for specified Study
        api_response = api_instance.export_all_records_csv(token, generate_metadata=generate_metadata, use_concept_value=use_concept_value, export_empty_values=export_empty_values, date_from=date_from, date_to=date_to, extract_data_delta=extract_data_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_all_records_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **generate_metadata** | **bool**| Need to generate metadata for records | [optional] [default to False]
 **use_concept_value** | **bool**| Use Concept terms instead of Verbatim terms | [optional] [default to False]
 **export_empty_values** | **bool**| Use Empty values instead of null-value | [optional] [default to False]
 **date_from** | **str**| All data from subjects with enrollmentDate &amp;gt;&#x3D; dateFrom. Format: &lt;b&gt;2019-12-10&lt;/b&gt; or &lt;b&gt;2019-12-10 10:20&lt;/b&gt; | [optional] 
 **date_to** | **str**| All data from subjects with enrollmentDate &amp;lt;&#x3D; dateTo. Format: &lt;b&gt;2019-12-10&lt;/b&gt;  or &lt;b&gt;2019-12-10 10:20&lt;/b&gt;  | [optional] 
 **extract_data_delta** | **bool**| By default dateFrom &amp; dateTo are used to extract all subjects and its data with enrollmentDate between those dates. Use this parameter if you want to extract data that was inserted / updated between those dates. | [optional] [default to False]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_all_records_json2**
> list[StudyEventRecord] export_all_records_json2(token, use_concept_value=use_concept_value, export_empty_values=export_empty_values, date_from=date_from, date_to=date_to, extract_data_delta=extract_data_delta)

Get list of user Records for specified Study

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
use_concept_value = False # bool | Use Concept terms instead of Verbatim terms (optional) (default to False)
export_empty_values = False # bool | Use Empty values instead of null-value (optional) (default to False)
date_from = 'date_from_example' # str | All data from subjects with enrollmentDate &gt;= dateFrom. Format: <b>2019-12-10</b> or <b>2019-12-10 10:20</b> (optional)
date_to = 'date_to_example' # str | All data from subjects with enrollmentDate &lt;= dateTo. Format: <b>2019-12-10</b>  or <b>2019-12-10 10:20</b>  (optional)
extract_data_delta = False # bool | By default dateFrom & dateTo are used to extract all subjects and its data with enrollmentDate between those dates. Use this parameter if you want to extract data that was inserted / updated between those dates. (optional) (default to False)

    try:
        # Get list of user Records for specified Study
        api_response = api_instance.export_all_records_json2(token, use_concept_value=use_concept_value, export_empty_values=export_empty_values, date_from=date_from, date_to=date_to, extract_data_delta=extract_data_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_all_records_json2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **use_concept_value** | **bool**| Use Concept terms instead of Verbatim terms | [optional] [default to False]
 **export_empty_values** | **bool**| Use Empty values instead of null-value | [optional] [default to False]
 **date_from** | **str**| All data from subjects with enrollmentDate &amp;gt;&#x3D; dateFrom. Format: &lt;b&gt;2019-12-10&lt;/b&gt; or &lt;b&gt;2019-12-10 10:20&lt;/b&gt; | [optional] 
 **date_to** | **str**| All data from subjects with enrollmentDate &amp;lt;&#x3D; dateTo. Format: &lt;b&gt;2019-12-10&lt;/b&gt;  or &lt;b&gt;2019-12-10 10:20&lt;/b&gt;  | [optional] 
 **extract_data_delta** | **bool**| By default dateFrom &amp; dateTo are used to extract all subjects and its data with enrollmentDate between those dates. Use this parameter if you want to extract data that was inserted / updated between those dates. | [optional] [default to False]

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_all_records_odm**
> export_all_records_odm(token)

Get Study definitions in ODM format

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get Study definitions in ODM format
        api_instance.export_all_records_odm(token)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_all_records_odm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_all_records_xml2**
> list[StudyEventRecord] export_all_records_xml2(token, use_concept_value=use_concept_value, export_empty_values=export_empty_values, date_from=date_from, date_to=date_to, extract_data_delta=extract_data_delta)

Get list of user Records for specified Study

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
use_concept_value = False # bool | Use Concept terms instead of Verbatim terms (optional) (default to False)
export_empty_values = False # bool | Use Empty values instead of null-value (optional) (default to False)
date_from = 'date_from_example' # str | All data from subjects with enrollmentDate &gt;= dateFrom. Format: <b>2019-12-10</b> or <b>2019-12-10 10:20</b> (optional)
date_to = 'date_to_example' # str | All data from subjects with enrollmentDate &lt;= dateTo. Format: <b>2019-12-10</b>  or <b>2019-12-10 10:20</b>  (optional)
extract_data_delta = False # bool | By default dateFrom & dateTo are used to extract all subjects and its data with enrollmentDate between those dates. Use this parameter if you want to extract data that was inserted / updated between those dates. (optional) (default to False)

    try:
        # Get list of user Records for specified Study
        api_response = api_instance.export_all_records_xml2(token, use_concept_value=use_concept_value, export_empty_values=export_empty_values, date_from=date_from, date_to=date_to, extract_data_delta=extract_data_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_all_records_xml2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **use_concept_value** | **bool**| Use Concept terms instead of Verbatim terms | [optional] [default to False]
 **export_empty_values** | **bool**| Use Empty values instead of null-value | [optional] [default to False]
 **date_from** | **str**| All data from subjects with enrollmentDate &amp;gt;&#x3D; dateFrom. Format: &lt;b&gt;2019-12-10&lt;/b&gt; or &lt;b&gt;2019-12-10 10:20&lt;/b&gt; | [optional] 
 **date_to** | **str**| All data from subjects with enrollmentDate &amp;lt;&#x3D; dateTo. Format: &lt;b&gt;2019-12-10&lt;/b&gt;  or &lt;b&gt;2019-12-10 10:20&lt;/b&gt;  | [optional] 
 **extract_data_delta** | **bool**| By default dateFrom &amp; dateTo are used to extract all subjects and its data with enrollmentDate between those dates. Use this parameter if you want to extract data that was inserted / updated between those dates. | [optional] [default to False]

### Return type

[**list[StudyEventRecord]**](StudyEventRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_all_site_records_csv**
> export_all_site_records_csv(id, token, generate_metadata=generate_metadata)

Get list of user Records for specified Study Site

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    id = 56 # int | Study Site ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.
generate_metadata = False # bool | Need to generate metadata for records (optional) (default to False)

    try:
        # Get list of user Records for specified Study Site
        api_instance.export_all_site_records_csv(id, token, generate_metadata=generate_metadata)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_all_site_records_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Study Site ID | 
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **generate_metadata** | **bool**| Need to generate metadata for records | [optional] [default to False]

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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_all_site_records_odm**
> export_all_site_records_odm(id, token)

Get definitions in ODM format for specified Study Site

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    id = 56 # int | Study Site ID
token = 'token_example' # str | Study access token. Used to get current study ID parameter.

    try:
        # Get definitions in ODM format for specified Study Site
        api_instance.export_all_site_records_odm(id, token)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_all_site_records_odm: %s\n" % e)
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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_extended_records_odm_for_tenant_study**
> export_extended_records_odm_for_tenant_study(study_id, token)

Get definitions in ODM (SDM Extended Data) format for specified Tenant Study

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    study_id = 56 # int | Study ID in RedCap
token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.

    try:
        # Get definitions in ODM (SDM Extended Data) format for specified Tenant Study
        api_instance.export_extended_records_odm_for_tenant_study(study_id, token)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_extended_records_odm_for_tenant_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID in RedCap | 
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 

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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_extended_records_odm_for_tenant_study_post**
> export_extended_records_odm_for_tenant_study_post(study_id, token, body=body)

Get definitions in ODM (SDM Extended Data) format for specified Tenant Study

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    study_id = 56 # int | Study ID in RedCap
token = 'token_example' # str | User access token to corresponding RedCap Cloud Tenant.
body = rcc.ExportOptions() # ExportOptions | Export Options (optional)

    try:
        # Get definitions in ODM (SDM Extended Data) format for specified Tenant Study
        api_instance.export_extended_records_odm_for_tenant_study_post(study_id, token, body=body)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_extended_records_odm_for_tenant_study_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **int**| Study ID in RedCap | 
 **token** | **str**| User access token to corresponding RedCap Cloud Tenant. | 
 **body** | [**ExportOptions**](ExportOptions.md)| Export Options | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/csv, application/odm
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_records_csv**
> export_records_csv(token, body)

Get list of user Records for specified Study and filters

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.ExportOptions() # ExportOptions | Record Export Options

    try:
        # Get list of user Records for specified Study and filters
        api_instance.export_records_csv(token, body)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_records_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**ExportOptions**](ExportOptions.md)| Record Export Options | 

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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_records_odm**
> export_records_odm(token, body)

Get list of user Records for specified Study and filters (Snapshot ODM Export)

Example: 

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.ExportOptions() # ExportOptions | Record Export Options

    try:
        # Get list of user Records for specified Study and filters (Snapshot ODM Export)
        api_instance.export_records_odm(token, body)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_records_odm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**ExportOptions**](ExportOptions.md)| Record Export Options | 

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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_records_todm**
> export_records_todm(token, body)

Get list of user Records for specified Study and filters (Transactional ODM Export)

Example: 

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
    api_instance = rcc.ExportDataControllerApi(api_client)
    token = 'token_example' # str | Study access token. Used to get current study ID parameter.
body = rcc.TodmExportOptions() # TodmExportOptions | Record Export Options

    try:
        # Get list of user Records for specified Study and filters (Transactional ODM Export)
        api_instance.export_records_todm(token, body)
    except ApiException as e:
        print("Exception when calling ExportDataControllerApi->export_records_todm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Study access token. Used to get current study ID parameter. | 
 **body** | [**TodmExportOptions**](TodmExportOptions.md)| Record Export Options | 

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
**400** | Invalid input data. |  -  |
**401** | Study Authorization token header must be defined. |  -  |
**403** | Token is not allowed for EXPORT/READ operations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

