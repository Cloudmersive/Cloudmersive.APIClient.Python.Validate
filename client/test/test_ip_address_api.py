# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ip_address_api import IPAddressApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIPAddressApi(unittest.TestCase):
    """IPAddressApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ip_address_api.IPAddressApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_i_p_address_post(self):
        """Test case for i_p_address_post

        Geolocate an IP address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
