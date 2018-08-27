# PhoneNumberValidationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | True if the phone number is valid, false otherwise | [optional] 
**successful** | **bool** | True if the operation was successful, false if there was an error during validation.  See IsValid for validation result. | [optional] 
**phone_number_type** | **str** | Type of phone number; possible values are: FixedLine, Mobile, FixedLineOrMobile, TollFree, PremiumRate,   SharedCost, Voip, PersonalNumber, Pager, Uan, Voicemail, Unknown | [optional] 
**e164_format** | **str** | E.164 format of the phone number | [optional] 
**international_format** | **str** | Internaltional format of the phone number | [optional] 
**national_format** | **str** | National format of the phone number | [optional] 
**country_code** | **str** | Two digit country code of the phone number | [optional] 
**country_name** | **str** | User-friendly long name of the country for the phone number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


