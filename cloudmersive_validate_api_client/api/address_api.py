# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudmersive_validate_api_client.api_client import ApiClient


class AddressApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def address_country(self, input, **kwargs):  # noqa: E501
        """Validate and normalize country information, return ISO 3166-1 country codes and country name  # noqa: E501

        Validates and normalizes country information, and returns key information about a country.  Also returns distinct time zones in the country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_country(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateCountryRequest input: Input request (required)
        :return: ValidateCountryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.address_country_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.address_country_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def address_country_with_http_info(self, input, **kwargs):  # noqa: E501
        """Validate and normalize country information, return ISO 3166-1 country codes and country name  # noqa: E501

        Validates and normalizes country information, and returns key information about a country.  Also returns distinct time zones in the country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_country_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateCountryRequest input: Input request (required)
        :return: ValidateCountryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method address_country" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `address_country`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/address/country', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateCountryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def address_get_timezone(self, input, **kwargs):  # noqa: E501
        """Gets IANA/Olsen time zones for a country  # noqa: E501

        Gets the IANA/Olsen time zones for a country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_get_timezone(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetTimezonesRequest input: Input request (required)
        :return: GetTimezonesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.address_get_timezone_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.address_get_timezone_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def address_get_timezone_with_http_info(self, input, **kwargs):  # noqa: E501
        """Gets IANA/Olsen time zones for a country  # noqa: E501

        Gets the IANA/Olsen time zones for a country.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_get_timezone_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetTimezonesRequest input: Input request (required)
        :return: GetTimezonesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method address_get_timezone" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `address_get_timezone`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/address/country/get-timezones', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetTimezonesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def address_parse_string(self, input, **kwargs):  # noqa: E501
        """Parse an unstructured input text string into an international, formatted address  # noqa: E501

        Uses machine learning and Natural Language Processing (NLP) to handle a wide array of cases, including non-standard and unstructured address strings across a wide array of countries and address formatting norms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_parse_string(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ParseAddressRequest input: Input parse request (required)
        :return: ParseAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.address_parse_string_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.address_parse_string_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def address_parse_string_with_http_info(self, input, **kwargs):  # noqa: E501
        """Parse an unstructured input text string into an international, formatted address  # noqa: E501

        Uses machine learning and Natural Language Processing (NLP) to handle a wide array of cases, including non-standard and unstructured address strings across a wide array of countries and address formatting norms.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_parse_string_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ParseAddressRequest input: Input parse request (required)
        :return: ParseAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method address_parse_string" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `address_parse_string`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/address/parse', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ParseAddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def address_validate_address(self, input, **kwargs):  # noqa: E501
        """Validate a street address  # noqa: E501

        Determines if an input structured street address is valid or invalid.  If the address is valid, also returns the latitude and longitude of the address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_validate_address(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateAddressRequest input: Input parse request (required)
        :return: ValidateAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.address_validate_address_with_http_info(input, **kwargs)  # noqa: E501
        else:
            (data) = self.address_validate_address_with_http_info(input, **kwargs)  # noqa: E501
            return data

    def address_validate_address_with_http_info(self, input, **kwargs):  # noqa: E501
        """Validate a street address  # noqa: E501

        Determines if an input structured street address is valid or invalid.  If the address is valid, also returns the latitude and longitude of the address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_validate_address_with_http_info(input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateAddressRequest input: Input parse request (required)
        :return: ValidateAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method address_validate_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'input' is set
        if ('input' not in params or
                params['input'] is None):
            raise ValueError("Missing the required parameter `input` when calling `address_validate_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input' in params:
            body_params = params['input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/address/street-address', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateAddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
