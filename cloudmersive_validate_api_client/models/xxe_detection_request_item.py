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


class XxeDetectionRequestItem(object):
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
        'input_text': 'str',
        'allow_internet_urls': 'bool',
        'known_safe_urls': 'list[str]',
        'known_unsafe_urls': 'list[str]'
    }

    attribute_map = {
        'input_text': 'InputText',
        'allow_internet_urls': 'AllowInternetUrls',
        'known_safe_urls': 'KnownSafeUrls',
        'known_unsafe_urls': 'KnownUnsafeUrls'
    }

    def __init__(self, input_text=None, allow_internet_urls=None, known_safe_urls=None, known_unsafe_urls=None):  # noqa: E501
        """XxeDetectionRequestItem - a model defined in Swagger"""  # noqa: E501

        self._input_text = None
        self._allow_internet_urls = None
        self._known_safe_urls = None
        self._known_unsafe_urls = None
        self.discriminator = None

        if input_text is not None:
            self.input_text = input_text
        if allow_internet_urls is not None:
            self.allow_internet_urls = allow_internet_urls
        if known_safe_urls is not None:
            self.known_safe_urls = known_safe_urls
        if known_unsafe_urls is not None:
            self.known_unsafe_urls = known_unsafe_urls

    @property
    def input_text(self):
        """Gets the input_text of this XxeDetectionRequestItem.  # noqa: E501

        Individual input text item to protect from XXE  # noqa: E501

        :return: The input_text of this XxeDetectionRequestItem.  # noqa: E501
        :rtype: str
        """
        return self._input_text

    @input_text.setter
    def input_text(self, input_text):
        """Sets the input_text of this XxeDetectionRequestItem.

        Individual input text item to protect from XXE  # noqa: E501

        :param input_text: The input_text of this XxeDetectionRequestItem.  # noqa: E501
        :type: str
        """

        self._input_text = input_text

    @property
    def allow_internet_urls(self):
        """Gets the allow_internet_urls of this XxeDetectionRequestItem.  # noqa: E501

        Optional: Set to true to allow Internet-based dependency URLs for DTDs and other XML External Entitites, set to false to block.  Default is false.  # noqa: E501

        :return: The allow_internet_urls of this XxeDetectionRequestItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_internet_urls

    @allow_internet_urls.setter
    def allow_internet_urls(self, allow_internet_urls):
        """Sets the allow_internet_urls of this XxeDetectionRequestItem.

        Optional: Set to true to allow Internet-based dependency URLs for DTDs and other XML External Entitites, set to false to block.  Default is false.  # noqa: E501

        :param allow_internet_urls: The allow_internet_urls of this XxeDetectionRequestItem.  # noqa: E501
        :type: bool
        """

        self._allow_internet_urls = allow_internet_urls

    @property
    def known_safe_urls(self):
        """Gets the known_safe_urls of this XxeDetectionRequestItem.  # noqa: E501

        Optional: Comma separated list of fully-qualified URLs that will automatically be considered safe.  # noqa: E501

        :return: The known_safe_urls of this XxeDetectionRequestItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._known_safe_urls

    @known_safe_urls.setter
    def known_safe_urls(self, known_safe_urls):
        """Sets the known_safe_urls of this XxeDetectionRequestItem.

        Optional: Comma separated list of fully-qualified URLs that will automatically be considered safe.  # noqa: E501

        :param known_safe_urls: The known_safe_urls of this XxeDetectionRequestItem.  # noqa: E501
        :type: list[str]
        """

        self._known_safe_urls = known_safe_urls

    @property
    def known_unsafe_urls(self):
        """Gets the known_unsafe_urls of this XxeDetectionRequestItem.  # noqa: E501

        Optional: Comma separated list of fully-qualified URLs that will automatically be considered unsafe.  # noqa: E501

        :return: The known_unsafe_urls of this XxeDetectionRequestItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._known_unsafe_urls

    @known_unsafe_urls.setter
    def known_unsafe_urls(self, known_unsafe_urls):
        """Sets the known_unsafe_urls of this XxeDetectionRequestItem.

        Optional: Comma separated list of fully-qualified URLs that will automatically be considered unsafe.  # noqa: E501

        :param known_unsafe_urls: The known_unsafe_urls of this XxeDetectionRequestItem.  # noqa: E501
        :type: list[str]
        """

        self._known_unsafe_urls = known_unsafe_urls

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
        if issubclass(XxeDetectionRequestItem, dict):
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
        if not isinstance(other, XxeDetectionRequestItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other