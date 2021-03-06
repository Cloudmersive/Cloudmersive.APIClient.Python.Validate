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
from swagger_client.api.email_api import EmailApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEmailApi(unittest.TestCase):
    """EmailApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.email_api.EmailApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_email_address_get_servers(self):
        """Test case for email_address_get_servers

        Partially check whether an email address is valid  # noqa: E501
        """
        pass

    def test_email_full_validation(self):
        """Test case for email_full_validation

        Fully validate an email address  # noqa: E501
        """
        pass

    def test_email_post(self):
        """Test case for email_post

        Validate email adddress for syntactic correctness only  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
