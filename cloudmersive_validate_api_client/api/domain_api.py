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


class DomainApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def domain_check(self, domain, **kwargs):  # noqa: E501
        """Validate a domain name  # noqa: E501

        Check whether a domain name is valid or not.  API performs a live validation by contacting DNS services to validate the existence of the domain name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_check(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes. (required)
        :return: CheckResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_check_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_check_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def domain_check_with_http_info(self, domain, **kwargs):  # noqa: E501
        """Validate a domain name  # noqa: E501

        Check whether a domain name is valid or not.  API performs a live validation by contacting DNS services to validate the existence of the domain name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_check_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes. (required)
        :return: CheckResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_check" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `domain_check`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'domain' in params:
            body_params = params['domain']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/check', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_get_top_level_domain_from_url(self, request, **kwargs):  # noqa: E501
        """Get top-level domain name from URL  # noqa: E501

        Gets the top-level domain name from a URL, such as mydomain.com.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_get_top_level_domain_from_url(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateUrlRequestSyntaxOnly request: Input URL information (required)
        :return: ValidateUrlResponseSyntaxOnly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_get_top_level_domain_from_url_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_get_top_level_domain_from_url_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def domain_get_top_level_domain_from_url_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get top-level domain name from URL  # noqa: E501

        Gets the top-level domain name from a URL, such as mydomain.com.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_get_top_level_domain_from_url_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateUrlRequestSyntaxOnly request: Input URL information (required)
        :return: ValidateUrlResponseSyntaxOnly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_get_top_level_domain_from_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `domain_get_top_level_domain_from_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/url/get-top-level-domain', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateUrlResponseSyntaxOnly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_post(self, domain, **kwargs):  # noqa: E501
        """Get WHOIS information for a domain  # noqa: E501

        Validate whether a domain name exists, and also return the full WHOIS record for that domain name.  WHOIS records include all the registration details of the domain name, such as information about the domain's owners.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_post(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain name to check, for example \"cloudmersive.com\".   The input is a string so be sure to enclose it in double-quotes. (required)
        :return: WhoisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_post_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_post_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def domain_post_with_http_info(self, domain, **kwargs):  # noqa: E501
        """Get WHOIS information for a domain  # noqa: E501

        Validate whether a domain name exists, and also return the full WHOIS record for that domain name.  WHOIS records include all the registration details of the domain name, such as information about the domain's owners.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_post_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain name to check, for example \"cloudmersive.com\".   The input is a string so be sure to enclose it in double-quotes. (required)
        :return: WhoisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `domain_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'domain' in params:
            body_params = params['domain']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/whois', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WhoisResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_quality_score(self, domain, **kwargs):  # noqa: E501
        """Validate a domain name's quality score  # noqa: E501

        Check the quality of a domain name.  Supports over 9 million domain names.  Higher quality scores indicate more trust and authority in the domain name, with values ranging from 0.0 (low quality) to 10.0 (maximum quality).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_quality_score(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain name to check, for example \"cloudmersive.com\". (required)
        :return: DomainQualityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_quality_score_with_http_info(domain, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_quality_score_with_http_info(domain, **kwargs)  # noqa: E501
            return data

    def domain_quality_score_with_http_info(self, domain, **kwargs):  # noqa: E501
        """Validate a domain name's quality score  # noqa: E501

        Check the quality of a domain name.  Supports over 9 million domain names.  Higher quality scores indicate more trust and authority in the domain name, with values ranging from 0.0 (low quality) to 10.0 (maximum quality).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_quality_score_with_http_info(domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str domain: Domain name to check, for example \"cloudmersive.com\". (required)
        :return: DomainQualityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_quality_score" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params or
                params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `domain_quality_score`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'domain' in params:
            body_params = params['domain']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/quality-score', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomainQualityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_ssrf_check(self, request, **kwargs):  # noqa: E501
        """Check a URL for SSRF threats  # noqa: E501

        Checks if an input URL is at risk of being an SSRF (Server-side request forgery) threat or attack.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_ssrf_check(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UrlSsrfRequestFull request: Input URL request (required)
        :return: UrlSsrfResponseFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_ssrf_check_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_ssrf_check_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def domain_ssrf_check_with_http_info(self, request, **kwargs):  # noqa: E501
        """Check a URL for SSRF threats  # noqa: E501

        Checks if an input URL is at risk of being an SSRF (Server-side request forgery) threat or attack.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_ssrf_check_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UrlSsrfRequestFull request: Input URL request (required)
        :return: UrlSsrfResponseFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_ssrf_check" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `domain_ssrf_check`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/url/ssrf-threat-check', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UrlSsrfResponseFull',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_ssrf_check_batch(self, request, **kwargs):  # noqa: E501
        """Check a URL for SSRF threats in batches  # noqa: E501

        Batch-checks if input URLs are at risk of being an SSRF (Server-side request forgery) threat or attack.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_ssrf_check_batch(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UrlSsrfRequestBatch request: Input URL request as a batch of multiple URLs (required)
        :return: UrlSsrfResponseBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_ssrf_check_batch_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_ssrf_check_batch_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def domain_ssrf_check_batch_with_http_info(self, request, **kwargs):  # noqa: E501
        """Check a URL for SSRF threats in batches  # noqa: E501

        Batch-checks if input URLs are at risk of being an SSRF (Server-side request forgery) threat or attack.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_ssrf_check_batch_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UrlSsrfRequestBatch request: Input URL request as a batch of multiple URLs (required)
        :return: UrlSsrfResponseBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_ssrf_check_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `domain_ssrf_check_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/url/ssrf-threat-check/batch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UrlSsrfResponseBatch',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_url_full(self, request, **kwargs):  # noqa: E501
        """Validate a URL fully  # noqa: E501

        Validate whether a URL is syntactically valid (does not check endpoint for validity), whether it exists, and whether the endpoint is up and passes virus scan checks.  Accepts various types of input and produces a well-formed URL as output.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_url_full(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateUrlRequestFull request: Input URL request (required)
        :return: ValidateUrlResponseFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_url_full_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_url_full_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def domain_url_full_with_http_info(self, request, **kwargs):  # noqa: E501
        """Validate a URL fully  # noqa: E501

        Validate whether a URL is syntactically valid (does not check endpoint for validity), whether it exists, and whether the endpoint is up and passes virus scan checks.  Accepts various types of input and produces a well-formed URL as output.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_url_full_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateUrlRequestFull request: Input URL request (required)
        :return: ValidateUrlResponseFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_url_full" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `domain_url_full`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/url/full', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateUrlResponseFull',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def domain_url_syntax_only(self, request, **kwargs):  # noqa: E501
        """Validate a URL syntactically  # noqa: E501

        Validate whether a URL is syntactically valid (does not check endpoint for validity).  Accepts various types of input and produces a well-formed URL as output.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_url_syntax_only(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateUrlRequestSyntaxOnly request: Input URL information (required)
        :return: ValidateUrlResponseSyntaxOnly
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.domain_url_syntax_only_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.domain_url_syntax_only_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def domain_url_syntax_only_with_http_info(self, request, **kwargs):  # noqa: E501
        """Validate a URL syntactically  # noqa: E501

        Validate whether a URL is syntactically valid (does not check endpoint for validity).  Accepts various types of input and produces a well-formed URL as output.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.domain_url_syntax_only_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ValidateUrlRequestSyntaxOnly request: Input URL information (required)
        :return: ValidateUrlResponseSyntaxOnly
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method domain_url_syntax_only" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `domain_url_syntax_only`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/validate/domain/url/syntax-only', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateUrlResponseSyntaxOnly',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
