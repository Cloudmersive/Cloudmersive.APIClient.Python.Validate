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


class ValidateCountryResponse(object):
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
        'successful': 'bool',
        'country_full_name': 'str',
        'iso_two_letter_code': 'str',
        'fips_two_letter_code': 'str',
        'three_letter_code': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'country_full_name': 'CountryFullName',
        'iso_two_letter_code': 'ISOTwoLetterCode',
        'fips_two_letter_code': 'FIPSTwoLetterCode',
        'three_letter_code': 'ThreeLetterCode'
    }

    def __init__(self, successful=None, country_full_name=None, iso_two_letter_code=None, fips_two_letter_code=None, three_letter_code=None):  # noqa: E501
        """ValidateCountryResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._country_full_name = None
        self._iso_two_letter_code = None
        self._fips_two_letter_code = None
        self._three_letter_code = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if country_full_name is not None:
            self.country_full_name = country_full_name
        if iso_two_letter_code is not None:
            self.iso_two_letter_code = iso_two_letter_code
        if fips_two_letter_code is not None:
            self.fips_two_letter_code = fips_two_letter_code
        if three_letter_code is not None:
            self.three_letter_code = three_letter_code

    @property
    def successful(self):
        """Gets the successful of this ValidateCountryResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this ValidateCountryResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ValidateCountryResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this ValidateCountryResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def country_full_name(self):
        """Gets the country_full_name of this ValidateCountryResponse.  # noqa: E501

        Full name of the country  # noqa: E501

        :return: The country_full_name of this ValidateCountryResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_full_name

    @country_full_name.setter
    def country_full_name(self, country_full_name):
        """Sets the country_full_name of this ValidateCountryResponse.

        Full name of the country  # noqa: E501

        :param country_full_name: The country_full_name of this ValidateCountryResponse.  # noqa: E501
        :type: str
        """

        self._country_full_name = country_full_name

    @property
    def iso_two_letter_code(self):
        """Gets the iso_two_letter_code of this ValidateCountryResponse.  # noqa: E501

        Two-letter ISO 3166-1 country code  # noqa: E501

        :return: The iso_two_letter_code of this ValidateCountryResponse.  # noqa: E501
        :rtype: str
        """
        return self._iso_two_letter_code

    @iso_two_letter_code.setter
    def iso_two_letter_code(self, iso_two_letter_code):
        """Sets the iso_two_letter_code of this ValidateCountryResponse.

        Two-letter ISO 3166-1 country code  # noqa: E501

        :param iso_two_letter_code: The iso_two_letter_code of this ValidateCountryResponse.  # noqa: E501
        :type: str
        """

        self._iso_two_letter_code = iso_two_letter_code

    @property
    def fips_two_letter_code(self):
        """Gets the fips_two_letter_code of this ValidateCountryResponse.  # noqa: E501

        Two-letter FIPS 10-4 country code  # noqa: E501

        :return: The fips_two_letter_code of this ValidateCountryResponse.  # noqa: E501
        :rtype: str
        """
        return self._fips_two_letter_code

    @fips_two_letter_code.setter
    def fips_two_letter_code(self, fips_two_letter_code):
        """Sets the fips_two_letter_code of this ValidateCountryResponse.

        Two-letter FIPS 10-4 country code  # noqa: E501

        :param fips_two_letter_code: The fips_two_letter_code of this ValidateCountryResponse.  # noqa: E501
        :type: str
        """

        self._fips_two_letter_code = fips_two_letter_code

    @property
    def three_letter_code(self):
        """Gets the three_letter_code of this ValidateCountryResponse.  # noqa: E501

        Three-letter ISO 3166-1 country code  # noqa: E501

        :return: The three_letter_code of this ValidateCountryResponse.  # noqa: E501
        :rtype: str
        """
        return self._three_letter_code

    @three_letter_code.setter
    def three_letter_code(self, three_letter_code):
        """Sets the three_letter_code of this ValidateCountryResponse.

        Three-letter ISO 3166-1 country code  # noqa: E501

        :param three_letter_code: The three_letter_code of this ValidateCountryResponse.  # noqa: E501
        :type: str
        """

        self._three_letter_code = three_letter_code

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
        if issubclass(ValidateCountryResponse, dict):
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
        if not isinstance(other, ValidateCountryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
