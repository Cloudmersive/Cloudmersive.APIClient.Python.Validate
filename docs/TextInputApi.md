# cloudmersive_validate_api_client.TextInputApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_input_check_sql_injection**](TextInputApi.md#text_input_check_sql_injection) | **POST** /validate/text-input/check/sql-injection | Check text input for SQL Injection (SQLI) attacks
[**text_input_check_sql_injection_batch**](TextInputApi.md#text_input_check_sql_injection_batch) | **POST** /validate/text-input/check/sql-injection/batch | Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch
[**text_input_check_xss**](TextInputApi.md#text_input_check_xss) | **POST** /validate/text-input/check/xss | Check text input for Cross-Site-Scripting (XSS) attacks
[**text_input_check_xss_batch**](TextInputApi.md#text_input_check_xss_batch) | **POST** /validate/text-input/check-and-protect/xss/batch | Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch
[**text_input_check_xxe**](TextInputApi.md#text_input_check_xxe) | **POST** /validate/text-input/check/xxe | Protect text input from XML External Entity (XXE) attacks
[**text_input_check_xxe_batch**](TextInputApi.md#text_input_check_xxe_batch) | **POST** /validate/text-input/check/xxe/batch | Protect text input from XML External Entity (XXE) attacks
[**text_input_protect_xss**](TextInputApi.md#text_input_protect_xss) | **POST** /validate/text-input/protect/xss | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization


# **text_input_check_sql_injection**
> SqlInjectionDetectionResult text_input_check_sql_injection(value, detection_level=detection_level)

Check text input for SQL Injection (SQLI) attacks

Detects SQL Injection (SQLI) attacks from text input.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.
detection_level = 'detection_level_example' # str | Set to Normal to target a high-security SQL Injection detection level with a very low false positive rate; select High to target a very-high security SQL Injection detection level with higher false positives.  Default is Normal (recommended). (optional)

try:
    # Check text input for SQL Injection (SQLI) attacks
    api_response = api_instance.text_input_check_sql_injection(value, detection_level=detection_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_check_sql_injection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 
 **detection_level** | **str**| Set to Normal to target a high-security SQL Injection detection level with a very low false positive rate; select High to target a very-high security SQL Injection detection level with higher false positives.  Default is Normal (recommended). | [optional] 

### Return type

[**SqlInjectionDetectionResult**](SqlInjectionDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_input_check_sql_injection_batch**
> SqlInjectionCheckBatchResponse text_input_check_sql_injection_batch(value)

Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch

Detects SQL Injection (SQLI) attacks from multiple text inputs.  Output preverses order of input items.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = cloudmersive_validate_api_client.SqlInjectionCheckBatchRequest() # SqlInjectionCheckBatchRequest | User-facing text input.

try:
    # Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch
    api_response = api_instance.text_input_check_sql_injection_batch(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_check_sql_injection_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**SqlInjectionCheckBatchRequest**](SqlInjectionCheckBatchRequest.md)| User-facing text input. | 

### Return type

[**SqlInjectionCheckBatchResponse**](SqlInjectionCheckBatchResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_input_check_xss**
> XssProtectionResult text_input_check_xss(value)

Check text input for Cross-Site-Scripting (XSS) attacks

Detects XSS (Cross-Site-Scripting) attacks from text input.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Check text input for Cross-Site-Scripting (XSS) attacks
    api_response = api_instance.text_input_check_xss(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_check_xss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**XssProtectionResult**](XssProtectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_input_check_xss_batch**
> XssProtectionBatchResponse text_input_check_xss_batch(value)

Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch

Detects XSS (Cross-Site-Scripting) attacks from multiple text inputs.  Output preverses order of input items.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = cloudmersive_validate_api_client.XssProtectionBatchRequest() # XssProtectionBatchRequest | User-facing text input.

try:
    # Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch
    api_response = api_instance.text_input_check_xss_batch(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_check_xss_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**XssProtectionBatchRequest**](XssProtectionBatchRequest.md)| User-facing text input. | 

### Return type

[**XssProtectionBatchResponse**](XssProtectionBatchResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_input_check_xxe**
> XxeDetectionResult text_input_check_xxe(value, allow_internet_urls=allow_internet_urls, known_safe_urls=known_safe_urls, known_unsafe_urls=known_unsafe_urls)

Protect text input from XML External Entity (XXE) attacks

Detects XXE (XML External Entity) attacks from text input.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.
allow_internet_urls = true # bool | Optional: Set to true to allow Internet-based dependency URLs for DTDs and other XML External Entitites, set to false to block.  Default is false. (optional)
known_safe_urls = 'known_safe_urls_example' # str | Optional: Comma separated list of fully-qualified URLs that will automatically be considered safe. (optional)
known_unsafe_urls = 'known_unsafe_urls_example' # str | Optional: Comma separated list of fully-qualified URLs that will automatically be considered unsafe. (optional)

try:
    # Protect text input from XML External Entity (XXE) attacks
    api_response = api_instance.text_input_check_xxe(value, allow_internet_urls=allow_internet_urls, known_safe_urls=known_safe_urls, known_unsafe_urls=known_unsafe_urls)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_check_xxe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 
 **allow_internet_urls** | **bool**| Optional: Set to true to allow Internet-based dependency URLs for DTDs and other XML External Entitites, set to false to block.  Default is false. | [optional] 
 **known_safe_urls** | **str**| Optional: Comma separated list of fully-qualified URLs that will automatically be considered safe. | [optional] 
 **known_unsafe_urls** | **str**| Optional: Comma separated list of fully-qualified URLs that will automatically be considered unsafe. | [optional] 

### Return type

[**XxeDetectionResult**](XxeDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_input_check_xxe_batch**
> XxeDetectionBatchResponse text_input_check_xxe_batch(request)

Protect text input from XML External Entity (XXE) attacks

Detects XXE (XML External Entity) attacks from text input.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
request = cloudmersive_validate_api_client.XxeDetectionBatchRequest() # XxeDetectionBatchRequest | 

try:
    # Protect text input from XML External Entity (XXE) attacks
    api_response = api_instance.text_input_check_xxe_batch(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_check_xxe_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**XxeDetectionBatchRequest**](XxeDetectionBatchRequest.md)|  | 

### Return type

[**XxeDetectionBatchResponse**](XxeDetectionBatchResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_input_protect_xss**
> XssProtectionResult text_input_protect_xss(value)

Protect text input from Cross-Site-Scripting (XSS) attacks through normalization

Detects and removes XSS (Cross-Site-Scripting) attacks from text input through normalization.  Returns the normalized result, as well as information on whether the original input contained an XSS risk.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.TextInputApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Protect text input from Cross-Site-Scripting (XSS) attacks through normalization
    api_response = api_instance.text_input_protect_xss(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextInputApi->text_input_protect_xss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**XssProtectionResult**](XssProtectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

