from __future__ import print_function
import time
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.DomainApi()
domain = 'cloudmersive.com' # str | Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes.

# Configure API key authorization: Apikey

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = 'f0c513bc-8c00-4491-830e-3e83b015feb6'

try:
    # Validate a domain name
    api_response = api_instance.domain_check(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_check: %s\n" % e)