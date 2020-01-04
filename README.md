# cloudmersive_validate_api_client
The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.

This Python package provides a native API client for [Cloudmersive Data Validation](https://www.cloudmersive.com/validate-api)

- API version: v1
- Package version: 2.1.1
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
    # Validate and normalize country information, return ISO 3166-1 country codes and country name
    api_response = api_instance.address_country(input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->address_country: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddressApi* | [**address_country**](docs/AddressApi.md#address_country) | **POST** /validate/address/country | Validate and normalize country information, return ISO 3166-1 country codes and country name
*AddressApi* | [**address_get_timezone**](docs/AddressApi.md#address_get_timezone) | **POST** /validate/address/country/get-timezones | Gets IANA/Olsen time zones for a country
*AddressApi* | [**address_parse_string**](docs/AddressApi.md#address_parse_string) | **POST** /validate/address/parse | Parse an unstructured input text string into an international, formatted address
*DomainApi* | [**domain_check**](docs/DomainApi.md#domain_check) | **POST** /validate/domain/check | Validate a domain name
*DomainApi* | [**domain_post**](docs/DomainApi.md#domain_post) | **POST** /validate/domain/whois | Get WHOIS information for a domain
*DomainApi* | [**domain_url_full**](docs/DomainApi.md#domain_url_full) | **POST** /validate/domain/url/full | Validate a URL fully
*DomainApi* | [**domain_url_syntax_only**](docs/DomainApi.md#domain_url_syntax_only) | **POST** /validate/domain/url/syntax-only | Validate a URL syntactically
*EmailApi* | [**email_address_get_servers**](docs/EmailApi.md#email_address_get_servers) | **POST** /validate/email/address/servers | Partially check whether an email address is valid
*EmailApi* | [**email_full_validation**](docs/EmailApi.md#email_full_validation) | **POST** /validate/email/address/full | Fully validate an email address
*EmailApi* | [**email_post**](docs/EmailApi.md#email_post) | **POST** /validate/email/address/syntaxOnly | Validate email adddress for syntactic correctness only
*IPAddressApi* | [**i_p_address_post**](docs/IPAddressApi.md#i_p_address_post) | **POST** /validate/ip/geolocate | Geolocate an IP address
*LeadEnrichmentApi* | [**lead_enrichment_enrich_lead**](docs/LeadEnrichmentApi.md#lead_enrichment_enrich_lead) | **POST** /validate/lead-enrichment/lead/enrich | Enrich an input lead with additional fields of data
*NameApi* | [**name_get_gender**](docs/NameApi.md#name_get_gender) | **POST** /validate/name/get-gender | Get the gender of a first name
*NameApi* | [**name_identifier**](docs/NameApi.md#name_identifier) | **POST** /validate/name/identifier | Validate a code identifier
*NameApi* | [**name_validate_first_name**](docs/NameApi.md#name_validate_first_name) | **POST** /validate/name/first | Validate a first name
*NameApi* | [**name_validate_full_name**](docs/NameApi.md#name_validate_full_name) | **POST** /validate/name/full-name | Parse and validate a full name
*NameApi* | [**name_validate_last_name**](docs/NameApi.md#name_validate_last_name) | **POST** /validate/name/last | Validate a last name
*PhoneNumberApi* | [**phone_number_syntax_only**](docs/PhoneNumberApi.md#phone_number_syntax_only) | **POST** /validate/phonenumber/basic | Validate phone number (basic)
*UserAgentApi* | [**user_agent_parse**](docs/UserAgentApi.md#user_agent_parse) | **POST** /validate/useragent/parse | Parse an HTTP User-Agent string, identify robots
*VatApi* | [**vat_vat_lookup**](docs/VatApi.md#vat_vat_lookup) | **POST** /validate/vat/lookup | Lookup a VAT code


## Documentation For Models

 - [AddressGetServersResponse](docs/AddressGetServersResponse.md)
 - [AddressVerifySyntaxOnlyResponse](docs/AddressVerifySyntaxOnlyResponse.md)
 - [CheckResponse](docs/CheckResponse.md)
 - [FirstNameValidationRequest](docs/FirstNameValidationRequest.md)
 - [FirstNameValidationResponse](docs/FirstNameValidationResponse.md)
 - [FullEmailValidationResponse](docs/FullEmailValidationResponse.md)
 - [FullNameValidationRequest](docs/FullNameValidationRequest.md)
 - [FullNameValidationResponse](docs/FullNameValidationResponse.md)
 - [GeolocateResponse](docs/GeolocateResponse.md)
 - [GetGenderRequest](docs/GetGenderRequest.md)
 - [GetGenderResponse](docs/GetGenderResponse.md)
 - [GetTimezonesRequest](docs/GetTimezonesRequest.md)
 - [GetTimezonesResponse](docs/GetTimezonesResponse.md)
 - [LastNameValidationRequest](docs/LastNameValidationRequest.md)
 - [LastNameValidationResponse](docs/LastNameValidationResponse.md)
 - [LeadEnrichmentRequest](docs/LeadEnrichmentRequest.md)
 - [LeadEnrichmentResponse](docs/LeadEnrichmentResponse.md)
 - [ParseAddressRequest](docs/ParseAddressRequest.md)
 - [ParseAddressResponse](docs/ParseAddressResponse.md)
 - [PhoneNumberValidateRequest](docs/PhoneNumberValidateRequest.md)
 - [PhoneNumberValidationResponse](docs/PhoneNumberValidationResponse.md)
 - [Timezone](docs/Timezone.md)
 - [UserAgentValidateRequest](docs/UserAgentValidateRequest.md)
 - [UserAgentValidateResponse](docs/UserAgentValidateResponse.md)
 - [ValidateCountryRequest](docs/ValidateCountryRequest.md)
 - [ValidateCountryResponse](docs/ValidateCountryResponse.md)
 - [ValidateIdentifierRequest](docs/ValidateIdentifierRequest.md)
 - [ValidateIdentifierResponse](docs/ValidateIdentifierResponse.md)
 - [ValidateUrlRequestFull](docs/ValidateUrlRequestFull.md)
 - [ValidateUrlRequestSyntaxOnly](docs/ValidateUrlRequestSyntaxOnly.md)
 - [ValidateUrlResponseFull](docs/ValidateUrlResponseFull.md)
 - [ValidateUrlResponseSyntaxOnly](docs/ValidateUrlResponseSyntaxOnly.md)
 - [VatLookupRequest](docs/VatLookupRequest.md)
 - [VatLookupResponse](docs/VatLookupResponse.md)
 - [WhoisResponse](docs/WhoisResponse.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



