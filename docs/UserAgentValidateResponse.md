# UserAgentValidateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation was successful, false otherwise | [optional] 
**is_bot** | **bool** | True if the request is a known robot, false otherwise | [optional] 
**bot_name** | **str** | Optional; name of the robot if the request was from a known robot, otherwise null | [optional] 
**bot_url** | **str** | Optional; if available, the URL to the robot | [optional] 
**operating_system** | **str** | Operating System of the User-Agent (e.g. Windows) | [optional] 
**operating_system_cpu_platform** | **str** | The CPU platform of the User-Agent (e.g. x64) | [optional] 
**operating_system_version** | **str** | The version of the operating system of the User-Agent (e.g. \&quot;10\&quot; for Windows 10) | [optional] 
**device_type** | **str** | Device type of the User-Agent; possible values are \&quot;DESKTOP\&quot;, \&quot;SMARTPHONE\&quot;, \&quot;TABLET\&quot; | [optional] 
**device_brand_name** | **str** | Brand name of the User-Agent | [optional] 
**device_model** | **str** | Model name or number of the User-Agent | [optional] 
**browser_name** | **str** | Name of the Browser | [optional] 
**browser_version** | **str** | Version of the Browser | [optional] 
**browser_engine_name** | **str** | Name of the Browser Engine | [optional] 
**browser_engine_version** | **str** | Version of the Browser Engine | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


