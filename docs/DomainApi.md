# cloudmersive_validate_api_client.DomainApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_check**](DomainApi.md#domain_check) | **POST** /validate/domain/check | Validate a domain name
[**domain_post**](DomainApi.md#domain_post) | **POST** /validate/domain/whois | Get WHOIS information for a domain
[**domain_url_full**](DomainApi.md#domain_url_full) | **POST** /validate/domain/url/full | Validate a URL fully
[**domain_url_syntax_only**](DomainApi.md#domain_url_syntax_only) | **POST** /validate/domain/url/syntax-only | Validate a URL syntactically


# **domain_check**
> CheckResponse domain_check(domain)

Validate a domain name

Check whether a domain name is valid or not.  API performs a live validation by contacting DNS services to validate the existence of the domain name.

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
api_instance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
domain = 'domain_example' # str | Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Validate a domain name
    api_response = api_instance.domain_check(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name to check, for example \&quot;cloudmersive.com\&quot;.  The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: text/javascript, application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_post**
> WhoisResponse domain_post(domain)

Get WHOIS information for a domain

Validate whether a domain name exists, and also return the full WHOIS record for that domain name.  WHOIS records include all the registration details of the domain name, such as information about the domain's owners.

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
api_instance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
domain = 'domain_example' # str | Domain name to check, for example \"cloudmersive.com\".   The input is a string so be sure to enclose it in double-quotes.

try:
    # Get WHOIS information for a domain
    api_response = api_instance.domain_post(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name to check, for example \&quot;cloudmersive.com\&quot;.   The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**WhoisResponse**](WhoisResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: text/javascript, application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_url_full**
> ValidateUrlResponseFull domain_url_full(request)

Validate a URL fully

Validate whether a URL is syntactically valid (does not check endpoint for validity), whether it exists, and whether the endpoint is up and passes virus scan checks.  Accepts various types of input and produces a well-formed URL as output.

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
api_instance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
request = cloudmersive_validate_api_client.ValidateUrlRequestFull() # ValidateUrlRequestFull | Input URL request

try:
    # Validate a URL fully
    api_response = api_instance.domain_url_full(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_url_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ValidateUrlRequestFull**](ValidateUrlRequestFull.md)| Input URL request | 

### Return type

[**ValidateUrlResponseFull**](ValidateUrlResponseFull.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_url_syntax_only**
> ValidateUrlResponseSyntaxOnly domain_url_syntax_only(request)

Validate a URL syntactically

Validate whether a URL is syntactically valid (does not check endpoint for validity).  Accepts various types of input and produces a well-formed URL as output.

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
api_instance = cloudmersive_validate_api_client.DomainApi(cloudmersive_validate_api_client.ApiClient(configuration))
request = cloudmersive_validate_api_client.ValidateUrlRequestSyntaxOnly() # ValidateUrlRequestSyntaxOnly | Input URL information

try:
    # Validate a URL syntactically
    api_response = api_instance.domain_url_syntax_only(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_url_syntax_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ValidateUrlRequestSyntaxOnly**](ValidateUrlRequestSyntaxOnly.md)| Input URL information | 

### Return type

[**ValidateUrlResponseSyntaxOnly**](ValidateUrlResponseSyntaxOnly.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

