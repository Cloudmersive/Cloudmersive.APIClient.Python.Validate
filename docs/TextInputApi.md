# cloudmersive_validate_api_client.TextInputApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**text_input_check_xss**](TextInputApi.md#text_input_check_xss) | **POST** /validate/text-input/check/xss | Check text input for Cross-Site-Scripting (XSS) attacks
[**text_input_protect_xss**](TextInputApi.md#text_input_protect_xss) | **POST** /validate/text-input/protect/xss | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization


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

