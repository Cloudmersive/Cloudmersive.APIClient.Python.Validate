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


class CountryDetails(object):
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
        'country_name': 'str',
        'three_letter_code': 'str',
        'iso_two_letter_code': 'str',
        'is_european_union_member': 'bool',
        'iso_currency_code': 'str',
        'currency_symbol': 'str',
        'currency_english_name': 'str'
    }

    attribute_map = {
        'country_name': 'CountryName',
        'three_letter_code': 'ThreeLetterCode',
        'iso_two_letter_code': 'ISOTwoLetterCode',
        'is_european_union_member': 'IsEuropeanUnionMember',
        'iso_currency_code': 'ISOCurrencyCode',
        'currency_symbol': 'CurrencySymbol',
        'currency_english_name': 'CurrencyEnglishName'
    }

    def __init__(self, country_name=None, three_letter_code=None, iso_two_letter_code=None, is_european_union_member=None, iso_currency_code=None, currency_symbol=None, currency_english_name=None):  # noqa: E501
        """CountryDetails - a model defined in Swagger"""  # noqa: E501

        self._country_name = None
        self._three_letter_code = None
        self._iso_two_letter_code = None
        self._is_european_union_member = None
        self._iso_currency_code = None
        self._currency_symbol = None
        self._currency_english_name = None
        self.discriminator = None

        if country_name is not None:
            self.country_name = country_name
        if three_letter_code is not None:
            self.three_letter_code = three_letter_code
        if iso_two_letter_code is not None:
            self.iso_two_letter_code = iso_two_letter_code
        if is_european_union_member is not None:
            self.is_european_union_member = is_european_union_member
        if iso_currency_code is not None:
            self.iso_currency_code = iso_currency_code
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if currency_english_name is not None:
            self.currency_english_name = currency_english_name

    @property
    def country_name(self):
        """Gets the country_name of this CountryDetails.  # noqa: E501

        Name of the country  # noqa: E501

        :return: The country_name of this CountryDetails.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this CountryDetails.

        Name of the country  # noqa: E501

        :param country_name: The country_name of this CountryDetails.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def three_letter_code(self):
        """Gets the three_letter_code of this CountryDetails.  # noqa: E501

        Three-letter ISO 3166-1 country code  # noqa: E501

        :return: The three_letter_code of this CountryDetails.  # noqa: E501
        :rtype: str
        """
        return self._three_letter_code

    @three_letter_code.setter
    def three_letter_code(self, three_letter_code):
        """Sets the three_letter_code of this CountryDetails.

        Three-letter ISO 3166-1 country code  # noqa: E501

        :param three_letter_code: The three_letter_code of this CountryDetails.  # noqa: E501
        :type: str
        """

        self._three_letter_code = three_letter_code

    @property
    def iso_two_letter_code(self):
        """Gets the iso_two_letter_code of this CountryDetails.  # noqa: E501

        Two-letter ISO 3166-1 country code  # noqa: E501

        :return: The iso_two_letter_code of this CountryDetails.  # noqa: E501
        :rtype: str
        """
        return self._iso_two_letter_code

    @iso_two_letter_code.setter
    def iso_two_letter_code(self, iso_two_letter_code):
        """Sets the iso_two_letter_code of this CountryDetails.

        Two-letter ISO 3166-1 country code  # noqa: E501

        :param iso_two_letter_code: The iso_two_letter_code of this CountryDetails.  # noqa: E501
        :type: str
        """

        self._iso_two_letter_code = iso_two_letter_code

    @property
    def is_european_union_member(self):
        """Gets the is_european_union_member of this CountryDetails.  # noqa: E501

        True if this country is currently a member of the European Union (EU), false otherwise  # noqa: E501

        :return: The is_european_union_member of this CountryDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_european_union_member

    @is_european_union_member.setter
    def is_european_union_member(self, is_european_union_member):
        """Sets the is_european_union_member of this CountryDetails.

        True if this country is currently a member of the European Union (EU), false otherwise  # noqa: E501

        :param is_european_union_member: The is_european_union_member of this CountryDetails.  # noqa: E501
        :type: bool
        """

        self._is_european_union_member = is_european_union_member

    @property
    def iso_currency_code(self):
        """Gets the iso_currency_code of this CountryDetails.  # noqa: E501

        ISO 4217 currency three-letter code associated with the country  # noqa: E501

        :return: The iso_currency_code of this CountryDetails.  # noqa: E501
        :rtype: str
        """
        return self._iso_currency_code

    @iso_currency_code.setter
    def iso_currency_code(self, iso_currency_code):
        """Sets the iso_currency_code of this CountryDetails.

        ISO 4217 currency three-letter code associated with the country  # noqa: E501

        :param iso_currency_code: The iso_currency_code of this CountryDetails.  # noqa: E501
        :type: str
        """

        self._iso_currency_code = iso_currency_code

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this CountryDetails.  # noqa: E501

        Symbol associated with the currency  # noqa: E501

        :return: The currency_symbol of this CountryDetails.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this CountryDetails.

        Symbol associated with the currency  # noqa: E501

        :param currency_symbol: The currency_symbol of this CountryDetails.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def currency_english_name(self):
        """Gets the currency_english_name of this CountryDetails.  # noqa: E501

        Full name of the currency  # noqa: E501

        :return: The currency_english_name of this CountryDetails.  # noqa: E501
        :rtype: str
        """
        return self._currency_english_name

    @currency_english_name.setter
    def currency_english_name(self, currency_english_name):
        """Sets the currency_english_name of this CountryDetails.

        Full name of the currency  # noqa: E501

        :param currency_english_name: The currency_english_name of this CountryDetails.  # noqa: E501
        :type: str
        """

        self._currency_english_name = currency_english_name

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
        if issubclass(CountryDetails, dict):
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
        if not isinstance(other, CountryDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
