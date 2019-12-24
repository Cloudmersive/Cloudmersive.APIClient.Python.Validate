# LeadEnrichmentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation was successful, false otherwise | [optional] 
**lead_type** | **str** | The type of the lead; possible types are Junk (a single individual using a disposable/throwaway email address); Individual (a single individual, typically a consumer, not purchasing on behalf of a business); SmallBusiness (a small business, typically with fewer than 100 employees); MediumBusiness (a medium business, larger than 100 employees but fewer than 1000 employees); Enterprise (a large business with greater than 1000 employees); Business (a business customer of unknown size) | [optional] 
**contact_business_email** | **str** | The person&#39;s business email address for the lead | [optional] 
**contact_first_name** | **str** | The person&#39;s first name for the lead | [optional] 
**contact_last_name** | **str** | The person&#39;s last name for the lead | [optional] 
**contact_gender** | **str** | Gender for contact name; possible values are Male, Female, and Neutral (can be applied to Male or Female).  Requires ContactFirstName. | [optional] 
**company_name** | **str** | Name of the company for the lead | [optional] 
**company_domain_name** | **str** | Domain name / website for the lead | [optional] 
**company_house_number** | **str** | House number of the address of the company for the lead | [optional] 
**company_street** | **str** | Street name of the address of the company for the lead | [optional] 
**company_city** | **str** | City of the address of the company for the lead | [optional] 
**company_state_or_province** | **str** | State or Province of the address of the company for the lead | [optional] 
**company_postal_code** | **str** | Postal Code of the address of the company for the lead | [optional] 
**company_country** | **str** | Country Name of the address of the company for the lead | [optional] 
**company_country_code** | **str** | Country Code (2-letter ISO 3166-1) of the address of the company for the lead | [optional] 
**company_telephone** | **str** | Telephone of the company office for the lead | [optional] 
**company_vat_number** | **str** | VAT number of the company for the lead | [optional] 
**employee_count** | **int** | Count of employees at the company (estimated), if available | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


