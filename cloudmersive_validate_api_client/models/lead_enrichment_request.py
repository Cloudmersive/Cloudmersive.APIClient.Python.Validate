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


class LeadEnrichmentRequest(object):
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
        'contact_business_email': 'str',
        'contact_first_name': 'str',
        'contact_last_name': 'str',
        'company_name': 'str',
        'company_domain_name': 'str',
        'company_house_number': 'str',
        'company_street': 'str',
        'company_city': 'str',
        'company_state_or_province': 'str',
        'company_postal_code': 'str',
        'company_country': 'str',
        'company_country_code': 'str',
        'company_telephone': 'str',
        'company_vat_number': 'str'
    }

    attribute_map = {
        'contact_business_email': 'ContactBusinessEmail',
        'contact_first_name': 'ContactFirstName',
        'contact_last_name': 'ContactLastName',
        'company_name': 'CompanyName',
        'company_domain_name': 'CompanyDomainName',
        'company_house_number': 'CompanyHouseNumber',
        'company_street': 'CompanyStreet',
        'company_city': 'CompanyCity',
        'company_state_or_province': 'CompanyStateOrProvince',
        'company_postal_code': 'CompanyPostalCode',
        'company_country': 'CompanyCountry',
        'company_country_code': 'CompanyCountryCode',
        'company_telephone': 'CompanyTelephone',
        'company_vat_number': 'CompanyVATNumber'
    }

    def __init__(self, contact_business_email=None, contact_first_name=None, contact_last_name=None, company_name=None, company_domain_name=None, company_house_number=None, company_street=None, company_city=None, company_state_or_province=None, company_postal_code=None, company_country=None, company_country_code=None, company_telephone=None, company_vat_number=None):  # noqa: E501
        """LeadEnrichmentRequest - a model defined in Swagger"""  # noqa: E501

        self._contact_business_email = None
        self._contact_first_name = None
        self._contact_last_name = None
        self._company_name = None
        self._company_domain_name = None
        self._company_house_number = None
        self._company_street = None
        self._company_city = None
        self._company_state_or_province = None
        self._company_postal_code = None
        self._company_country = None
        self._company_country_code = None
        self._company_telephone = None
        self._company_vat_number = None
        self.discriminator = None

        if contact_business_email is not None:
            self.contact_business_email = contact_business_email
        if contact_first_name is not None:
            self.contact_first_name = contact_first_name
        if contact_last_name is not None:
            self.contact_last_name = contact_last_name
        if company_name is not None:
            self.company_name = company_name
        if company_domain_name is not None:
            self.company_domain_name = company_domain_name
        if company_house_number is not None:
            self.company_house_number = company_house_number
        if company_street is not None:
            self.company_street = company_street
        if company_city is not None:
            self.company_city = company_city
        if company_state_or_province is not None:
            self.company_state_or_province = company_state_or_province
        if company_postal_code is not None:
            self.company_postal_code = company_postal_code
        if company_country is not None:
            self.company_country = company_country
        if company_country_code is not None:
            self.company_country_code = company_country_code
        if company_telephone is not None:
            self.company_telephone = company_telephone
        if company_vat_number is not None:
            self.company_vat_number = company_vat_number

    @property
    def contact_business_email(self):
        """Gets the contact_business_email of this LeadEnrichmentRequest.  # noqa: E501

        The person's business email address for the lead  # noqa: E501

        :return: The contact_business_email of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_business_email

    @contact_business_email.setter
    def contact_business_email(self, contact_business_email):
        """Sets the contact_business_email of this LeadEnrichmentRequest.

        The person's business email address for the lead  # noqa: E501

        :param contact_business_email: The contact_business_email of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._contact_business_email = contact_business_email

    @property
    def contact_first_name(self):
        """Gets the contact_first_name of this LeadEnrichmentRequest.  # noqa: E501

        The person's first name for the lead  # noqa: E501

        :return: The contact_first_name of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_first_name

    @contact_first_name.setter
    def contact_first_name(self, contact_first_name):
        """Sets the contact_first_name of this LeadEnrichmentRequest.

        The person's first name for the lead  # noqa: E501

        :param contact_first_name: The contact_first_name of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._contact_first_name = contact_first_name

    @property
    def contact_last_name(self):
        """Gets the contact_last_name of this LeadEnrichmentRequest.  # noqa: E501

        The person's last name for the lead  # noqa: E501

        :return: The contact_last_name of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_last_name

    @contact_last_name.setter
    def contact_last_name(self, contact_last_name):
        """Sets the contact_last_name of this LeadEnrichmentRequest.

        The person's last name for the lead  # noqa: E501

        :param contact_last_name: The contact_last_name of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._contact_last_name = contact_last_name

    @property
    def company_name(self):
        """Gets the company_name of this LeadEnrichmentRequest.  # noqa: E501

        Name of the company for the lead  # noqa: E501

        :return: The company_name of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this LeadEnrichmentRequest.

        Name of the company for the lead  # noqa: E501

        :param company_name: The company_name of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def company_domain_name(self):
        """Gets the company_domain_name of this LeadEnrichmentRequest.  # noqa: E501

        Domain name / website for the lead  # noqa: E501

        :return: The company_domain_name of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_domain_name

    @company_domain_name.setter
    def company_domain_name(self, company_domain_name):
        """Sets the company_domain_name of this LeadEnrichmentRequest.

        Domain name / website for the lead  # noqa: E501

        :param company_domain_name: The company_domain_name of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_domain_name = company_domain_name

    @property
    def company_house_number(self):
        """Gets the company_house_number of this LeadEnrichmentRequest.  # noqa: E501

        House number of the address of the company for the lead  # noqa: E501

        :return: The company_house_number of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_house_number

    @company_house_number.setter
    def company_house_number(self, company_house_number):
        """Sets the company_house_number of this LeadEnrichmentRequest.

        House number of the address of the company for the lead  # noqa: E501

        :param company_house_number: The company_house_number of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_house_number = company_house_number

    @property
    def company_street(self):
        """Gets the company_street of this LeadEnrichmentRequest.  # noqa: E501

        Street name of the address of the company for the lead  # noqa: E501

        :return: The company_street of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_street

    @company_street.setter
    def company_street(self, company_street):
        """Sets the company_street of this LeadEnrichmentRequest.

        Street name of the address of the company for the lead  # noqa: E501

        :param company_street: The company_street of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_street = company_street

    @property
    def company_city(self):
        """Gets the company_city of this LeadEnrichmentRequest.  # noqa: E501

        City of the address of the company for the lead  # noqa: E501

        :return: The company_city of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_city

    @company_city.setter
    def company_city(self, company_city):
        """Sets the company_city of this LeadEnrichmentRequest.

        City of the address of the company for the lead  # noqa: E501

        :param company_city: The company_city of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_city = company_city

    @property
    def company_state_or_province(self):
        """Gets the company_state_or_province of this LeadEnrichmentRequest.  # noqa: E501

        State or Province of the address of the company for the lead  # noqa: E501

        :return: The company_state_or_province of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_state_or_province

    @company_state_or_province.setter
    def company_state_or_province(self, company_state_or_province):
        """Sets the company_state_or_province of this LeadEnrichmentRequest.

        State or Province of the address of the company for the lead  # noqa: E501

        :param company_state_or_province: The company_state_or_province of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_state_or_province = company_state_or_province

    @property
    def company_postal_code(self):
        """Gets the company_postal_code of this LeadEnrichmentRequest.  # noqa: E501

        Postal Code of the address of the company for the lead  # noqa: E501

        :return: The company_postal_code of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_postal_code

    @company_postal_code.setter
    def company_postal_code(self, company_postal_code):
        """Sets the company_postal_code of this LeadEnrichmentRequest.

        Postal Code of the address of the company for the lead  # noqa: E501

        :param company_postal_code: The company_postal_code of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_postal_code = company_postal_code

    @property
    def company_country(self):
        """Gets the company_country of this LeadEnrichmentRequest.  # noqa: E501

        Country of the address of the company for the lead  # noqa: E501

        :return: The company_country of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_country

    @company_country.setter
    def company_country(self, company_country):
        """Sets the company_country of this LeadEnrichmentRequest.

        Country of the address of the company for the lead  # noqa: E501

        :param company_country: The company_country of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_country = company_country

    @property
    def company_country_code(self):
        """Gets the company_country_code of this LeadEnrichmentRequest.  # noqa: E501

        Country Code (2-letter ISO 3166-1) of the address of the company for the lead  # noqa: E501

        :return: The company_country_code of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_country_code

    @company_country_code.setter
    def company_country_code(self, company_country_code):
        """Sets the company_country_code of this LeadEnrichmentRequest.

        Country Code (2-letter ISO 3166-1) of the address of the company for the lead  # noqa: E501

        :param company_country_code: The company_country_code of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_country_code = company_country_code

    @property
    def company_telephone(self):
        """Gets the company_telephone of this LeadEnrichmentRequest.  # noqa: E501

        Telephone of the company office for the lead  # noqa: E501

        :return: The company_telephone of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_telephone

    @company_telephone.setter
    def company_telephone(self, company_telephone):
        """Sets the company_telephone of this LeadEnrichmentRequest.

        Telephone of the company office for the lead  # noqa: E501

        :param company_telephone: The company_telephone of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_telephone = company_telephone

    @property
    def company_vat_number(self):
        """Gets the company_vat_number of this LeadEnrichmentRequest.  # noqa: E501

        VAT number of the company for the lead  # noqa: E501

        :return: The company_vat_number of this LeadEnrichmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_vat_number

    @company_vat_number.setter
    def company_vat_number(self, company_vat_number):
        """Sets the company_vat_number of this LeadEnrichmentRequest.

        VAT number of the company for the lead  # noqa: E501

        :param company_vat_number: The company_vat_number of this LeadEnrichmentRequest.  # noqa: E501
        :type: str
        """

        self._company_vat_number = company_vat_number

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
        if issubclass(LeadEnrichmentRequest, dict):
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
        if not isinstance(other, LeadEnrichmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
