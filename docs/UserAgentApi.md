# cloudmersive_validate_api_client.UserAgentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_agent_parse**](UserAgentApi.md#user_agent_parse) | **POST** /validate/useragent/parse | Parse an HTTP User-Agent string, identify robots


# **user_agent_parse**
> UserAgentValidateResponse user_agent_parse(request)

Parse an HTTP User-Agent string, identify robots

Uses a parsing system and database to parse the User-Agent into its structured component parts, such as Browser, Browser Version, Browser Engine, Operating System, and importantly, Robot identification.

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
api_instance = cloudmersive_validate_api_client.UserAgentApi(cloudmersive_validate_api_client.ApiClient(configuration))
request = cloudmersive_validate_api_client.UserAgentValidateRequest() # UserAgentValidateRequest | Input parse request

try:
    # Parse an HTTP User-Agent string, identify robots
    api_response = api_instance.user_agent_parse(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAgentApi->user_agent_parse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UserAgentValidateRequest**](UserAgentValidateRequest.md)| Input parse request | 

### Return type

[**UserAgentValidateResponse**](UserAgentValidateResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

