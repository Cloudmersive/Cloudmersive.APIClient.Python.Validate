# ValidatePostalCodeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_postal_code** | **bool** | True if the Postal Code is valid, false otherwise | [optional] 
**city** | **str** | If valid, City corresponding to the input postal code, such as &#39;Walnut Creek&#39; | [optional] 
**state_or_province** | **str** | If valid; State or province corresponding to the input postal code, such as &#39;CA&#39; or &#39;California&#39; | [optional] 
**latitude** | **float** | If the postal code is valid, the degrees latitude of the centroid of the postal code, null otherwise | [optional] 
**longitude** | **float** | If the postal code is valid, the degrees longitude of the centroid of the postal code, null otherwise | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


