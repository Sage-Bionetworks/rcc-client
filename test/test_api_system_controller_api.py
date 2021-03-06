# coding: utf-8

"""
    nPhase REST Resource

    REDCap REST API v.2  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rcc
from rcc.api.api_system_controller_api import APISystemControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestAPISystemControllerApi(unittest.TestCase):
    """APISystemControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.api_system_controller_api.APISystemControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_signature(self):
        """Test case for get_api_signature

        Get API version  # noqa: E501
        """
        pass

    def test_get_api_version(self):
        """Test case for get_api_version

        Get API version  # noqa: E501
        """
        pass

    def test_get_current_study(self):
        """Test case for get_current_study

        Get current study ID  # noqa: E501
        """
        pass

    def test_get_rc_version(self):
        """Test case for get_rc_version

        Get API version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
