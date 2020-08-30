# cloudmersive_validate_api_client.IPAddressApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_p_address_is_tor_node**](IPAddressApi.md#i_p_address_is_tor_node) | **POST** /validate/ip/is-tor-node | Check if IP address is a Tor node server
[**i_p_address_post**](IPAddressApi.md#i_p_address_post) | **POST** /validate/ip/geolocate | Geolocate an IP address


# **i_p_address_is_tor_node**
> TorNodeResponse i_p_address_is_tor_node(value)

Check if IP address is a Tor node server

Check if the input IP address is a Tor exit node server.  Tor servers are a type of privacy-preserving technology that can hide the original IP address who makes a request.

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
api_instance = cloudmersive_validate_api_client.IPAddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = 'value_example' # str | IP address to check, e.g. \"55.55.55.55\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Check if IP address is a Tor node server
    api_response = api_instance.i_p_address_is_tor_node(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAddressApi->i_p_address_is_tor_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| IP address to check, e.g. \&quot;55.55.55.55\&quot;.  The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**TorNodeResponse**](TorNodeResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: text/javascript, application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_address_post**
> GeolocateResponse i_p_address_post(value)

Geolocate an IP address

Identify an IP address Country, State/Provence, City, Zip/Postal Code, etc.  Useful for security and UX applications.

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
api_instance = cloudmersive_validate_api_client.IPAddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
value = 'value_example' # str | IP address to geolocate, e.g. \"55.55.55.55\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Geolocate an IP address
    api_response = api_instance.i_p_address_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAddressApi->i_p_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| IP address to geolocate, e.g. \&quot;55.55.55.55\&quot;.  The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**GeolocateResponse**](GeolocateResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: text/javascript, application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

