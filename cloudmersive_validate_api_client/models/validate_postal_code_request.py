# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ValidatePostalCodeRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'postal_code': 'str',
        'country_full_name': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'postal_code': 'PostalCode',
        'country_full_name': 'CountryFullName',
        'country_code': 'CountryCode'
    }

    def __init__(self, postal_code=None, country_full_name=None, country_code=None):  # noqa: E501
        """ValidatePostalCodeRequest - a model defined in Swagger"""  # noqa: E501

        self._postal_code = None
        self._country_full_name = None
        self._country_code = None
        self.discriminator = None

        if postal_code is not None:
            self.postal_code = postal_code
        if country_full_name is not None:
            self.country_full_name = country_full_name
        if country_code is not None:
            self.country_code = country_code

    @property
    def postal_code(self):
        """Gets the postal_code of this ValidatePostalCodeRequest.  # noqa: E501

        Required: Zip code or postal code of the address to validate, such as '94597'  # noqa: E501

        :return: The postal_code of this ValidatePostalCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this ValidatePostalCodeRequest.

        Required: Zip code or postal code of the address to validate, such as '94597'  # noqa: E501

        :param postal_code: The postal_code of this ValidatePostalCodeRequest.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_full_name(self):
        """Gets the country_full_name of this ValidatePostalCodeRequest.  # noqa: E501

        Optional (recommended); Name of the country, such as 'United States'.  If left blank, and CountryCode is also left blank, will default to United States.  Global countries are supported.  # noqa: E501

        :return: The country_full_name of this ValidatePostalCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._country_full_name

    @country_full_name.setter
    def country_full_name(self, country_full_name):
        """Sets the country_full_name of this ValidatePostalCodeRequest.

        Optional (recommended); Name of the country, such as 'United States'.  If left blank, and CountryCode is also left blank, will default to United States.  Global countries are supported.  # noqa: E501

        :param country_full_name: The country_full_name of this ValidatePostalCodeRequest.  # noqa: E501
        :type: str
        """

        self._country_full_name = country_full_name

    @property
    def country_code(self):
        """Gets the country_code of this ValidatePostalCodeRequest.  # noqa: E501

        Optional; two-letter country code (Two-letter ISO 3166-1 country code) of the country.  If left blank, and CountryFullName is also left blank, will default to United States.  Global countries are supported.  # noqa: E501

        :return: The country_code of this ValidatePostalCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ValidatePostalCodeRequest.

        Optional; two-letter country code (Two-letter ISO 3166-1 country code) of the country.  If left blank, and CountryFullName is also left blank, will default to United States.  Global countries are supported.  # noqa: E501

        :param country_code: The country_code of this ValidatePostalCodeRequest.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ValidatePostalCodeRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValidatePostalCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
