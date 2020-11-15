# cloudmersive_validate_api_client.DateTimeApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**date_time_get_now_simple**](DateTimeApi.md#date_time_get_now_simple) | **GET** /validate/date-time/get/now | Get current date and time as of now
[**date_time_get_public_holidays**](DateTimeApi.md#date_time_get_public_holidays) | **POST** /validate/date-time/get/holidays | Get public holidays in the specified country and year
[**date_time_parse_natural_language_date_time**](DateTimeApi.md#date_time_parse_natural_language_date_time) | **POST** /validate/date-time/parse/date-time/natural-language | Parses a free-form natural language date and time string into a date and time
[**date_time_parse_standard_date_time**](DateTimeApi.md#date_time_parse_standard_date_time) | **POST** /validate/date-time/parse/date-time/structured | Parses a standardized date and time string into a date and time


# **date_time_get_now_simple**
> DateTimeNowResult date_time_get_now_simple()

Get current date and time as of now

Gets the current date and time.  Response time is syncronized with atomic clocks, and represents a monotonic, centrally available, consistent clock.

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
api_instance = cloudmersive_validate_api_client.DateTimeApi(cloudmersive_validate_api_client.ApiClient(configuration))

try:
    # Get current date and time as of now
    api_response = api_instance.date_time_get_now_simple()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DateTimeApi->date_time_get_now_simple: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DateTimeNowResult**](DateTimeNowResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **date_time_get_public_holidays**
> PublicHolidaysResponse date_time_get_public_holidays(input)

Get public holidays in the specified country and year

Enumerates all public holidays in a given country for a given year.  Supports over 100 countries.

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
api_instance = cloudmersive_validate_api_client.DateTimeApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.GetPublicHolidaysRequest() # GetPublicHolidaysRequest | Input request

try:
    # Get public holidays in the specified country and year
    api_response = api_instance.date_time_get_public_holidays(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DateTimeApi->date_time_get_public_holidays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**GetPublicHolidaysRequest**](GetPublicHolidaysRequest.md)| Input request | 

### Return type

[**PublicHolidaysResponse**](PublicHolidaysResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **date_time_parse_natural_language_date_time**
> DateTimeStandardizedParseResponse date_time_parse_natural_language_date_time(input)

Parses a free-form natural language date and time string into a date and time

Parses an unstructured, free-form, natural language date and time string into a date time object.  This is intended for lightweight human-entered input, such as \"tomorrow at 3pm\" or \"tuesday\".

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
api_instance = cloudmersive_validate_api_client.DateTimeApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.DateTimeNaturalLanguageParseRequest() # DateTimeNaturalLanguageParseRequest | Input request

try:
    # Parses a free-form natural language date and time string into a date and time
    api_response = api_instance.date_time_parse_natural_language_date_time(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DateTimeApi->date_time_parse_natural_language_date_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**DateTimeNaturalLanguageParseRequest**](DateTimeNaturalLanguageParseRequest.md)| Input request | 

### Return type

[**DateTimeStandardizedParseResponse**](DateTimeStandardizedParseResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **date_time_parse_standard_date_time**
> DateTimeStandardizedParseResponse date_time_parse_standard_date_time(input)

Parses a standardized date and time string into a date and time

Parses a structured date and time string into a date time object.  This is intended for standardized date strings that adhere to formatting conventions, rather than natural language input.

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
api_instance = cloudmersive_validate_api_client.DateTimeApi(cloudmersive_validate_api_client.ApiClient(configuration))
input = cloudmersive_validate_api_client.DateTimeStandardizedParseRequest() # DateTimeStandardizedParseRequest | Input request

try:
    # Parses a standardized date and time string into a date and time
    api_response = api_instance.date_time_parse_standard_date_time(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DateTimeApi->date_time_parse_standard_date_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**DateTimeStandardizedParseRequest**](DateTimeStandardizedParseRequest.md)| Input request | 

### Return type

[**DateTimeStandardizedParseResponse**](DateTimeStandardizedParseResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

