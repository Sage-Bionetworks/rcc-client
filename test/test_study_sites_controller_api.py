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
from rcc.api.study_sites_controller_api import StudySitesControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestStudySitesControllerApi(unittest.TestCase):
    """StudySitesControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.study_sites_controller_api.StudySitesControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create12(self):
        """Test case for create12

        Create new Study Site for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_delete9(self):
        """Test case for delete9

        Delete Survey for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_get_details9(self):
        """Test case for get_details9

        Get specified Study Site details  # noqa: E501
        """
        pass

    def test_get_list10(self):
        """Test case for get_list10

        Get list of all Study Sites for specified Study  # noqa: E501
        """
        pass

    def test_update11(self):
        """Test case for update11

        Update Study Site for current Study based on auth token provided  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
