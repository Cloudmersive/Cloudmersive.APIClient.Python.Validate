# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.api.lead_enrichment_api import LeadEnrichmentApi  # noqa: E501
from cloudmersive_validate_api_client.rest import ApiException


class TestLeadEnrichmentApi(unittest.TestCase):
    """LeadEnrichmentApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_validate_api_client.api.lead_enrichment_api.LeadEnrichmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lead_enrichment_enrich_lead(self):
        """Test case for lead_enrichment_enrich_lead

        Enrich an input lead with additional fields of data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()