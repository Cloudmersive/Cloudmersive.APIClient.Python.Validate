# cloudmersive_validate_api_client.LeadEnrichmentApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lead_enrichment_enrich_lead**](LeadEnrichmentApi.md#lead_enrichment_enrich_lead) | **POST** /validate/lead-enrichment/lead/enrich | Enrich an input lead with additional fields of data
[**lead_enrichment_get_company_information**](LeadEnrichmentApi.md#lead_enrichment_get_company_information) | **POST** /validate/lead-enrichment/lead/email/company-information | Get company information from email address


# **lead_enrichment_enrich_lead**
> LeadEnrichmentResponse lead_enrichment_enrich_lead(request)

Enrich an input lead with additional fields of data

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
api_instance = cloudmersive_validate_api_client.LeadEnrichmentApi(cloudmersive_validate_api_client.ApiClient(configuration))
request = cloudmersive_validate_api_client.LeadEnrichmentRequest() # LeadEnrichmentRequest | Input lead with known fields set, and unknown fields left blank (null)

try:
    # Enrich an input lead with additional fields of data
    api_response = api_instance.lead_enrichment_enrich_lead(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeadEnrichmentApi->lead_enrichment_enrich_lead: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LeadEnrichmentRequest**](LeadEnrichmentRequest.md)| Input lead with known fields set, and unknown fields left blank (null) | 

### Return type

[**LeadEnrichmentResponse**](LeadEnrichmentResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_enrichment_get_company_information**
> LeadEnrichmentResponse lead_enrichment_get_company_information(request)

Get company information from email address

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
api_instance = cloudmersive_validate_api_client.LeadEnrichmentApi(cloudmersive_validate_api_client.ApiClient(configuration))
request = cloudmersive_validate_api_client.EmailLead() # EmailLead | Input email address lead

try:
    # Get company information from email address
    api_response = api_instance.lead_enrichment_get_company_information(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeadEnrichmentApi->lead_enrichment_get_company_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailLead**](EmailLead.md)| Input email address lead | 

### Return type

[**LeadEnrichmentResponse**](LeadEnrichmentResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

