# cloudmersive_validate_api_client.VatApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vat_vat_lookup**](VatApi.md#vat_vat_lookup) | **POST** /validate/vat/lookup | Lookup a VAT code


# **vat_vat_lookup**
> VatLookupResponse vat_vat_lookup(input)

Lookup a VAT code

Checks if a VAT code is valid, and if it is, returns more information about it

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
api_instance = cloudmersive_validate_api_client.VatApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.VatLookupRequest() # VatLookupRequest | Input VAT code

try:
    # Lookup a VAT code
    api_response = api_instance.vat_vat_lookup(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VatApi->vat_vat_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**VatLookupRequest**](VatLookupRequest.md)| Input VAT code | 

### Return type

[**VatLookupResponse**](VatLookupResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

