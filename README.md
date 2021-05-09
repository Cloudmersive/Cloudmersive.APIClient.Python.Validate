# cloudmersive_validate_api_client
The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.

This Python package provides a native API client for [Cloudmersive Data Validation](https://www.cloudmersive.com/validate-api)

- API version: v1
- Package version: 3.2.3
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_validate_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_validate_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressApi* | [**address_check_eu_membership**](docs/AddressApi.md#address_check_eu_membership) | **POST** /validate/address/country/check-eu-membership | Check if a country is a member of the European Union (EU)
*AddressApi* | [**address_country**](docs/AddressApi.md#address_country) | **POST** /validate/address/country | Validate and normalize country information, return ISO 3166-1 country codes and country name
*AddressApi* | [**address_country_list**](docs/AddressApi.md#address_country_list) | **POST** /validate/address/country/list | Get a list of ISO 3166-1 countries
*AddressApi* | [**address_geocode**](docs/AddressApi.md#address_geocode) | **POST** /validate/address/geocode | Geocode a street address into latitude and longitude
*AddressApi* | [**address_get_country_currency**](docs/AddressApi.md#address_get_country_currency) | **POST** /validate/address/country/get-currency | Get the currency of the input country
*AddressApi* | [**address_get_country_region**](docs/AddressApi.md#address_get_country_region) | **POST** /validate/address/country/get-region | Get the region, subregion and continent of the country
*AddressApi* | [**address_get_timezone**](docs/AddressApi.md#address_get_timezone) | **POST** /validate/address/country/get-timezones | Gets IANA/Olsen time zones for a country
*AddressApi* | [**address_normalize_address**](docs/AddressApi.md#address_normalize_address) | **POST** /validate/address/street-address/normalize | Normalize a street address
*AddressApi* | [**address_parse_string**](docs/AddressApi.md#address_parse_string) | **POST** /validate/address/parse | Parse an unstructured input text string into an international, formatted address
*AddressApi* | [**address_reverse_geocode_address**](docs/AddressApi.md#address_reverse_geocode_address) | **POST** /validate/address/geocode/reverse | Reverse geocode a lattitude and longitude into an address
*AddressApi* | [**address_validate_address**](docs/AddressApi.md#address_validate_address) | **POST** /validate/address/street-address | Validate a street address
*AddressApi* | [**address_validate_city**](docs/AddressApi.md#address_validate_city) | **POST** /validate/address/city | Validate a City and State/Province combination, get location information about it
*AddressApi* | [**address_validate_postal_code**](docs/AddressApi.md#address_validate_postal_code) | **POST** /validate/address/postal-code | Validate a postal code, get location information about it
*AddressApi* | [**address_validate_state**](docs/AddressApi.md#address_validate_state) | **POST** /validate/address/state | Validate a state or province, name or abbreviation, get location information about it
*DateTimeApi* | [**date_time_get_now_simple**](docs/DateTimeApi.md#date_time_get_now_simple) | **GET** /validate/date-time/get/now | Get current date and time as of now
*DateTimeApi* | [**date_time_get_public_holidays**](docs/DateTimeApi.md#date_time_get_public_holidays) | **POST** /validate/date-time/get/holidays | Get public holidays in the specified country and year
*DateTimeApi* | [**date_time_parse_natural_language_date_time**](docs/DateTimeApi.md#date_time_parse_natural_language_date_time) | **POST** /validate/date-time/parse/date-time/natural-language | Parses a free-form natural language date and time string into a date and time
*DateTimeApi* | [**date_time_parse_standard_date_time**](docs/DateTimeApi.md#date_time_parse_standard_date_time) | **POST** /validate/date-time/parse/date-time/structured | Parses a standardized date and time string into a date and time
*DomainApi* | [**domain_check**](docs/DomainApi.md#domain_check) | **POST** /validate/domain/check | Validate a domain name
*DomainApi* | [**domain_get_top_level_domain_from_url**](docs/DomainApi.md#domain_get_top_level_domain_from_url) | **POST** /validate/domain/url/get-top-level-domain | Get top-level domain name from URL
*DomainApi* | [**domain_is_admin_path**](docs/DomainApi.md#domain_is_admin_path) | **POST** /validate/domain/url/is-admin-path | Check if path is a high-risk or vulnerable server administration path
*DomainApi* | [**domain_phishing_check**](docs/DomainApi.md#domain_phishing_check) | **POST** /validate/domain/url/phishing-threat-check | Check a URL for Phishing threats
*DomainApi* | [**domain_post**](docs/DomainApi.md#domain_post) | **POST** /validate/domain/whois | Get WHOIS information for a domain
*DomainApi* | [**domain_quality_score**](docs/DomainApi.md#domain_quality_score) | **POST** /validate/domain/quality-score | Validate a domain name&#39;s quality score
*DomainApi* | [**domain_safety_check**](docs/DomainApi.md#domain_safety_check) | **POST** /validate/domain/url/safety-threat-check | Check a URL for safety threats
*DomainApi* | [**domain_ssrf_check**](docs/DomainApi.md#domain_ssrf_check) | **POST** /validate/domain/url/ssrf-threat-check | Check a URL for SSRF threats
*DomainApi* | [**domain_ssrf_check_batch**](docs/DomainApi.md#domain_ssrf_check_batch) | **POST** /validate/domain/url/ssrf-threat-check/batch | Check a URL for SSRF threats in batches
*DomainApi* | [**domain_url_full**](docs/DomainApi.md#domain_url_full) | **POST** /validate/domain/url/full | Validate a URL fully
*DomainApi* | [**domain_url_html_ssrf_check**](docs/DomainApi.md#domain_url_html_ssrf_check) | **POST** /validate/domain/url/ssrf-threat-check/html-embedded | Check a URL for HTML embedded SSRF threats
*DomainApi* | [**domain_url_syntax_only**](docs/DomainApi.md#domain_url_syntax_only) | **POST** /validate/domain/url/syntax-only | Validate a URL syntactically
*EmailApi* | [**email_address_get_servers**](docs/EmailApi.md#email_address_get_servers) | **POST** /validate/email/address/servers | Partially check whether an email address is valid
*EmailApi* | [**email_full_validation**](docs/EmailApi.md#email_full_validation) | **POST** /validate/email/address/full | Fully validate an email address
*EmailApi* | [**email_post**](docs/EmailApi.md#email_post) | **POST** /validate/email/address/syntaxOnly | Validate email adddress for syntactic correctness only
*IPAddressApi* | [**i_p_address_geolocate_street_address**](docs/IPAddressApi.md#i_p_address_geolocate_street_address) | **POST** /validate/ip/geolocate/street-address | Geolocate an IP address to a street address
*IPAddressApi* | [**i_p_address_ip_intelligence**](docs/IPAddressApi.md#i_p_address_ip_intelligence) | **POST** /validate/ip/intelligence | Get intelligence on an IP address
*IPAddressApi* | [**i_p_address_is_bot**](docs/IPAddressApi.md#i_p_address_is_bot) | **POST** /validate/ip/is-bot | Check if IP address is a Bot client
*IPAddressApi* | [**i_p_address_is_threat**](docs/IPAddressApi.md#i_p_address_is_threat) | **POST** /validate/ip/is-threat | Check if IP address is a known threat
*IPAddressApi* | [**i_p_address_is_tor_node**](docs/IPAddressApi.md#i_p_address_is_tor_node) | **POST** /validate/ip/is-tor-node | Check if IP address is a Tor node server
*IPAddressApi* | [**i_p_address_post**](docs/IPAddressApi.md#i_p_address_post) | **POST** /validate/ip/geolocate | Geolocate an IP address
*IPAddressApi* | [**i_p_address_reverse_domain_lookup**](docs/IPAddressApi.md#i_p_address_reverse_domain_lookup) | **POST** /validate/ip/reverse-domain-lookup | Perform a reverse domain name (DNS) lookup on an IP address
*LeadEnrichmentApi* | [**lead_enrichment_enrich_lead**](docs/LeadEnrichmentApi.md#lead_enrichment_enrich_lead) | **POST** /validate/lead-enrichment/lead/enrich | Enrich an input lead with additional fields of data
*NameApi* | [**name_get_gender**](docs/NameApi.md#name_get_gender) | **POST** /validate/name/get-gender | Get the gender of a first name
*NameApi* | [**name_identifier**](docs/NameApi.md#name_identifier) | **POST** /validate/name/identifier | Validate a code identifier
*NameApi* | [**name_validate_first_name**](docs/NameApi.md#name_validate_first_name) | **POST** /validate/name/first | Validate a first name
*NameApi* | [**name_validate_full_name**](docs/NameApi.md#name_validate_full_name) | **POST** /validate/name/full-name | Parse and validate a full name
*NameApi* | [**name_validate_last_name**](docs/NameApi.md#name_validate_last_name) | **POST** /validate/name/last | Validate a last name
*PhoneNumberApi* | [**phone_number_syntax_only**](docs/PhoneNumberApi.md#phone_number_syntax_only) | **POST** /validate/phonenumber/basic | Validate phone number (basic)
*TextInputApi* | [**text_input_check_html_ssrf**](docs/TextInputApi.md#text_input_check_html_ssrf) | **POST** /validate/text-input/html/check/ssrf | Protect html input from Server-side Request Forgery (SSRF) attacks
*TextInputApi* | [**text_input_check_sql_injection**](docs/TextInputApi.md#text_input_check_sql_injection) | **POST** /validate/text-input/check/sql-injection | Check text input for SQL Injection (SQLI) attacks
*TextInputApi* | [**text_input_check_sql_injection_batch**](docs/TextInputApi.md#text_input_check_sql_injection_batch) | **POST** /validate/text-input/check/sql-injection/batch | Check and protect multiple text inputs for SQL Injection (SQLI) attacks in batch
*TextInputApi* | [**text_input_check_xss**](docs/TextInputApi.md#text_input_check_xss) | **POST** /validate/text-input/check/xss | Check text input for Cross-Site-Scripting (XSS) attacks
*TextInputApi* | [**text_input_check_xss_batch**](docs/TextInputApi.md#text_input_check_xss_batch) | **POST** /validate/text-input/check-and-protect/xss/batch | Check and protect multiple text inputs for Cross-Site-Scripting (XSS) attacks in batch
*TextInputApi* | [**text_input_check_xxe**](docs/TextInputApi.md#text_input_check_xxe) | **POST** /validate/text-input/check/xxe | Protect text input from XML External Entity (XXE) attacks
*TextInputApi* | [**text_input_check_xxe_batch**](docs/TextInputApi.md#text_input_check_xxe_batch) | **POST** /validate/text-input/check/xxe/batch | Protect text input from XML External Entity (XXE) attacks
*TextInputApi* | [**text_input_protect_xss**](docs/TextInputApi.md#text_input_protect_xss) | **POST** /validate/text-input/protect/xss | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization
*UserAgentApi* | [**user_agent_parse**](docs/UserAgentApi.md#user_agent_parse) | **POST** /validate/useragent/parse | Parse an HTTP User-Agent string, identify robots
*VatApi* | [**vat_vat_lookup**](docs/VatApi.md#vat_vat_lookup) | **POST** /validate/vat/lookup | Validate a VAT number


## Documentation For Models

 - [AddressGetServersResponse](docs/AddressGetServersResponse.md)
 - [AddressVerifySyntaxOnlyResponse](docs/AddressVerifySyntaxOnlyResponse.md)
 - [BotCheckResponse](docs/BotCheckResponse.md)
 - [CheckResponse](docs/CheckResponse.md)
 - [CountryDetails](docs/CountryDetails.md)
 - [CountryListResult](docs/CountryListResult.md)
 - [DateTimeNaturalLanguageParseRequest](docs/DateTimeNaturalLanguageParseRequest.md)
 - [DateTimeNowResult](docs/DateTimeNowResult.md)
 - [DateTimeStandardizedParseRequest](docs/DateTimeStandardizedParseRequest.md)
 - [DateTimeStandardizedParseResponse](docs/DateTimeStandardizedParseResponse.md)
 - [DomainQualityResponse](docs/DomainQualityResponse.md)
 - [FirstNameValidationRequest](docs/FirstNameValidationRequest.md)
 - [FirstNameValidationResponse](docs/FirstNameValidationResponse.md)
 - [FullEmailValidationResponse](docs/FullEmailValidationResponse.md)
 - [FullNameValidationRequest](docs/FullNameValidationRequest.md)
 - [FullNameValidationResponse](docs/FullNameValidationResponse.md)
 - [GeolocateResponse](docs/GeolocateResponse.md)
 - [GeolocateStreetAddressResponse](docs/GeolocateStreetAddressResponse.md)
 - [GetGenderRequest](docs/GetGenderRequest.md)
 - [GetGenderResponse](docs/GetGenderResponse.md)
 - [GetPublicHolidaysRequest](docs/GetPublicHolidaysRequest.md)
 - [GetTimezonesRequest](docs/GetTimezonesRequest.md)
 - [GetTimezonesResponse](docs/GetTimezonesResponse.md)
 - [HtmlSsrfDetectionResult](docs/HtmlSsrfDetectionResult.md)
 - [IPIntelligenceResponse](docs/IPIntelligenceResponse.md)
 - [IPReverseDNSLookupResponse](docs/IPReverseDNSLookupResponse.md)
 - [IPThreatResponse](docs/IPThreatResponse.md)
 - [IsAdminPathResponse](docs/IsAdminPathResponse.md)
 - [LastNameValidationRequest](docs/LastNameValidationRequest.md)
 - [LastNameValidationResponse](docs/LastNameValidationResponse.md)
 - [LeadEnrichmentRequest](docs/LeadEnrichmentRequest.md)
 - [LeadEnrichmentResponse](docs/LeadEnrichmentResponse.md)
 - [NormalizeAddressResponse](docs/NormalizeAddressResponse.md)
 - [ParseAddressRequest](docs/ParseAddressRequest.md)
 - [ParseAddressResponse](docs/ParseAddressResponse.md)
 - [PhishingCheckRequest](docs/PhishingCheckRequest.md)
 - [PhishingCheckResponse](docs/PhishingCheckResponse.md)
 - [PhoneNumberValidateRequest](docs/PhoneNumberValidateRequest.md)
 - [PhoneNumberValidationResponse](docs/PhoneNumberValidationResponse.md)
 - [PublicHolidayOccurrence](docs/PublicHolidayOccurrence.md)
 - [PublicHolidaysResponse](docs/PublicHolidaysResponse.md)
 - [ReverseGeocodeAddressRequest](docs/ReverseGeocodeAddressRequest.md)
 - [ReverseGeocodeAddressResponse](docs/ReverseGeocodeAddressResponse.md)
 - [SqlInjectionCheckBatchRequest](docs/SqlInjectionCheckBatchRequest.md)
 - [SqlInjectionCheckBatchResponse](docs/SqlInjectionCheckBatchResponse.md)
 - [SqlInjectionCheckRequestItem](docs/SqlInjectionCheckRequestItem.md)
 - [SqlInjectionDetectionResult](docs/SqlInjectionDetectionResult.md)
 - [Timezone](docs/Timezone.md)
 - [TorNodeResponse](docs/TorNodeResponse.md)
 - [UrlHtmlSsrfRequestFull](docs/UrlHtmlSsrfRequestFull.md)
 - [UrlHtmlSsrfResponseFull](docs/UrlHtmlSsrfResponseFull.md)
 - [UrlSafetyCheckRequestFull](docs/UrlSafetyCheckRequestFull.md)
 - [UrlSafetyCheckResponseFull](docs/UrlSafetyCheckResponseFull.md)
 - [UrlSsrfRequestBatch](docs/UrlSsrfRequestBatch.md)
 - [UrlSsrfRequestFull](docs/UrlSsrfRequestFull.md)
 - [UrlSsrfResponseBatch](docs/UrlSsrfResponseBatch.md)
 - [UrlSsrfResponseFull](docs/UrlSsrfResponseFull.md)
 - [UserAgentValidateRequest](docs/UserAgentValidateRequest.md)
 - [UserAgentValidateResponse](docs/UserAgentValidateResponse.md)
 - [ValidateAddressRequest](docs/ValidateAddressRequest.md)
 - [ValidateAddressResponse](docs/ValidateAddressResponse.md)
 - [ValidateCityRequest](docs/ValidateCityRequest.md)
 - [ValidateCityResponse](docs/ValidateCityResponse.md)
 - [ValidateCountryRequest](docs/ValidateCountryRequest.md)
 - [ValidateCountryResponse](docs/ValidateCountryResponse.md)
 - [ValidateIdentifierRequest](docs/ValidateIdentifierRequest.md)
 - [ValidateIdentifierResponse](docs/ValidateIdentifierResponse.md)
 - [ValidatePostalCodeRequest](docs/ValidatePostalCodeRequest.md)
 - [ValidatePostalCodeResponse](docs/ValidatePostalCodeResponse.md)
 - [ValidateStateRequest](docs/ValidateStateRequest.md)
 - [ValidateStateResponse](docs/ValidateStateResponse.md)
 - [ValidateUrlRequestFull](docs/ValidateUrlRequestFull.md)
 - [ValidateUrlRequestSyntaxOnly](docs/ValidateUrlRequestSyntaxOnly.md)
 - [ValidateUrlResponseFull](docs/ValidateUrlResponseFull.md)
 - [ValidateUrlResponseSyntaxOnly](docs/ValidateUrlResponseSyntaxOnly.md)
 - [VatLookupRequest](docs/VatLookupRequest.md)
 - [VatLookupResponse](docs/VatLookupResponse.md)
 - [WhoisResponse](docs/WhoisResponse.md)
 - [XssProtectionBatchRequest](docs/XssProtectionBatchRequest.md)
 - [XssProtectionBatchResponse](docs/XssProtectionBatchResponse.md)
 - [XssProtectionRequestItem](docs/XssProtectionRequestItem.md)
 - [XssProtectionResult](docs/XssProtectionResult.md)
 - [XxeDetectionBatchRequest](docs/XxeDetectionBatchRequest.md)
 - [XxeDetectionBatchResponse](docs/XxeDetectionBatchResponse.md)
 - [XxeDetectionRequestItem](docs/XxeDetectionRequestItem.md)
 - [XxeDetectionResult](docs/XxeDetectionResult.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



