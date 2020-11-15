# cloudmersive_validate_api_client.AddressApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**address_check_eu_membership**](AddressApi.md#address_check_eu_membership) | **POST** /validate/address/country/check-eu-membership | Check if a country is a member of the European Union (EU)
[**address_country**](AddressApi.md#address_country) | **POST** /validate/address/country | Validate and normalize country information, return ISO 3166-1 country codes and country name
[**address_country_list**](AddressApi.md#address_country_list) | **POST** /validate/address/country/list | Get a list of ISO 3166-1 countries
[**address_geocode**](AddressApi.md#address_geocode) | **POST** /validate/address/geocode | Geocode a street address into latitude and longitude
[**address_get_country_currency**](AddressApi.md#address_get_country_currency) | **POST** /validate/address/country/get-currency | Get the currency of the input country
[**address_get_country_region**](AddressApi.md#address_get_country_region) | **POST** /validate/address/country/get-region | Get the region, subregion and continent of the country
[**address_get_timezone**](AddressApi.md#address_get_timezone) | **POST** /validate/address/country/get-timezones | Gets IANA/Olsen time zones for a country
[**address_normalize_address**](AddressApi.md#address_normalize_address) | **POST** /validate/address/street-address/normalize | Normalize a street address
[**address_parse_string**](AddressApi.md#address_parse_string) | **POST** /validate/address/parse | Parse an unstructured input text string into an international, formatted address
[**address_reverse_geocode_address**](AddressApi.md#address_reverse_geocode_address) | **POST** /validate/address/geocode/reverse | Reverse geocode a lattitude and longitude into an address
[**address_validate_address**](AddressApi.md#address_validate_address) | **POST** /validate/address/street-address | Validate a street address
[**address_validate_city**](AddressApi.md#address_validate_city) | **POST** /validate/address/city | Validate a City and State/Province combination, get location information about it
[**address_validate_postal_code**](AddressApi.md#address_validate_postal_code) | **POST** /validate/address/postal-code | Validate a postal code, get location information about it
[**address_validate_state**](AddressApi.md#address_validate_state) | **POST** /validate/address/state | Validate a state or province, name or abbreviation, get location information about it


# **address_check_eu_membership**
> ValidateCountryResponse address_check_eu_membership(input)

Check if a country is a member of the European Union (EU)

Checks if the input country is a member of the European Union or not.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateCountryRequest() # ValidateCountryRequest | Input request

try:
    # Check if a country is a member of the European Union (EU)
    api_response = api_instance.address_check_eu_membership(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_check_eu_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateCountryRequest**](ValidateCountryRequest.md)| Input request | 

### Return type

[**ValidateCountryResponse**](ValidateCountryResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_country**
> ValidateCountryResponse address_country(input)

Validate and normalize country information, return ISO 3166-1 country codes and country name

Validates and normalizes country information, and returns key information about a country, as well as whether it is a member of the European Union.  Also returns distinct time zones in the country.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateCountryRequest() # ValidateCountryRequest | Input request

try:
    # Validate and normalize country information, return ISO 3166-1 country codes and country name
    api_response = api_instance.address_country(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateCountryRequest**](ValidateCountryRequest.md)| Input request | 

### Return type

[**ValidateCountryResponse**](ValidateCountryResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_country_list**
> CountryListResult address_country_list()

Get a list of ISO 3166-1 countries

Enumerates the list of ISO 3166-1 countries, including name, country codes, and more.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))

try:
    # Get a list of ISO 3166-1 countries
    api_response = api_instance.address_country_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_country_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountryListResult**](CountryListResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_geocode**
> ValidateAddressResponse address_geocode(input)

Geocode a street address into latitude and longitude

Geocodes a street address into latitude and longitude.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateAddressRequest() # ValidateAddressRequest | Input parse request

try:
    # Geocode a street address into latitude and longitude
    api_response = api_instance.address_geocode(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_geocode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateAddressRequest**](ValidateAddressRequest.md)| Input parse request | 

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_get_country_currency**
> ValidateCountryResponse address_get_country_currency(input)

Get the currency of the input country

Gets the currency information for the input country, including the ISO three-letter country code, currency symbol, and English currency name.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateCountryRequest() # ValidateCountryRequest | Input request

try:
    # Get the currency of the input country
    api_response = api_instance.address_get_country_currency(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_get_country_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateCountryRequest**](ValidateCountryRequest.md)| Input request | 

### Return type

[**ValidateCountryResponse**](ValidateCountryResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_get_country_region**
> ValidateCountryResponse address_get_country_region(input)

Get the region, subregion and continent of the country

Gets the continent information including region and subregion for the input country.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateCountryRequest() # ValidateCountryRequest | Input request

try:
    # Get the region, subregion and continent of the country
    api_response = api_instance.address_get_country_region(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_get_country_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateCountryRequest**](ValidateCountryRequest.md)| Input request | 

### Return type

[**ValidateCountryResponse**](ValidateCountryResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_get_timezone**
> GetTimezonesResponse address_get_timezone(input)

Gets IANA/Olsen time zones for a country

Gets the IANA/Olsen time zones for a country.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.GetTimezonesRequest() # GetTimezonesRequest | Input request

try:
    # Gets IANA/Olsen time zones for a country
    api_response = api_instance.address_get_timezone(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_get_timezone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetTimezonesRequest**](GetTimezonesRequest.md)| Input request | 

### Return type

[**GetTimezonesResponse**](GetTimezonesResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_normalize_address**
> NormalizeAddressResponse address_normalize_address(input)

Normalize a street address

Normalizes an input structured street address is valid or invalid.  If the address is valid, also returns the latitude and longitude of the address.  Supports all major international addresses.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateAddressRequest() # ValidateAddressRequest | Input parse request

try:
    # Normalize a street address
    api_response = api_instance.address_normalize_address(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_normalize_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateAddressRequest**](ValidateAddressRequest.md)| Input parse request | 

### Return type

[**NormalizeAddressResponse**](NormalizeAddressResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_parse_string**
> ParseAddressResponse address_parse_string(input)

Parse an unstructured input text string into an international, formatted address

Uses machine learning and Natural Language Processing (NLP) to handle a wide array of cases, including non-standard and unstructured address strings across a wide array of countries and address formatting norms.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ParseAddressRequest() # ParseAddressRequest | Input parse request

try:
    # Parse an unstructured input text string into an international, formatted address
    api_response = api_instance.address_parse_string(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_parse_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ParseAddressRequest**](ParseAddressRequest.md)| Input parse request | 

### Return type

[**ParseAddressResponse**](ParseAddressResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_reverse_geocode_address**
> ReverseGeocodeAddressResponse address_reverse_geocode_address(input)

Reverse geocode a lattitude and longitude into an address

Converts lattitude and longitude coordinates into an address through reverse-geocoding.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ReverseGeocodeAddressRequest() # ReverseGeocodeAddressRequest | Input reverse geocoding request

try:
    # Reverse geocode a lattitude and longitude into an address
    api_response = api_instance.address_reverse_geocode_address(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_reverse_geocode_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ReverseGeocodeAddressRequest**](ReverseGeocodeAddressRequest.md)| Input reverse geocoding request | 

### Return type

[**ReverseGeocodeAddressResponse**](ReverseGeocodeAddressResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_validate_address**
> ValidateAddressResponse address_validate_address(input)

Validate a street address

Determines if an input structured street address is valid or invalid.  If the address is valid, also returns the latitude and longitude of the address.  Supports all major international addresses.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateAddressRequest() # ValidateAddressRequest | Input parse request

try:
    # Validate a street address
    api_response = api_instance.address_validate_address(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_validate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateAddressRequest**](ValidateAddressRequest.md)| Input parse request | 

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_validate_city**
> ValidateCityResponse address_validate_city(input)

Validate a City and State/Province combination, get location information about it

Checks if the input city and state name or code is valid, and returns information about it such as normalized City name, State name and more.  Supports all major international addresses.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateCityRequest() # ValidateCityRequest | Input parse request

try:
    # Validate a City and State/Province combination, get location information about it
    api_response = api_instance.address_validate_city(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_validate_city: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateCityRequest**](ValidateCityRequest.md)| Input parse request | 

### Return type

[**ValidateCityResponse**](ValidateCityResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_validate_postal_code**
> ValidatePostalCodeResponse address_validate_postal_code(input)

Validate a postal code, get location information about it

Checks if the input postal code is valid, and returns information about it such as City, State and more.  Supports all major countries.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidatePostalCodeRequest() # ValidatePostalCodeRequest | Input parse request

try:
    # Validate a postal code, get location information about it
    api_response = api_instance.address_validate_postal_code(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_validate_postal_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidatePostalCodeRequest**](ValidatePostalCodeRequest.md)| Input parse request | 

### Return type

[**ValidatePostalCodeResponse**](ValidatePostalCodeResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_validate_state**
> ValidateStateResponse address_validate_state(input)

Validate a state or province, name or abbreviation, get location information about it

Checks if the input state name or code is valid, and returns information about it such as normalized State name and more.  Supports all major countries.

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
api_instance = cloudmersive_validate_api_client.AddressApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.ValidateStateRequest() # ValidateStateRequest | Input parse request

try:
    # Validate a state or province, name or abbreviation, get location information about it
    api_response = api_instance.address_validate_state(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_validate_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**ValidateStateRequest**](ValidateStateRequest.md)| Input parse request | 

### Return type

[**ValidateStateResponse**](ValidateStateResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

