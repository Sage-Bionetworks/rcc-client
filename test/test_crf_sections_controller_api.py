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
from rcc.api.crf_sections_controller_api import CRFSectionsControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestCRFSectionsControllerApi(unittest.TestCase):
    """CRFSectionsControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.crf_sections_controller_api.CRFSectionsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create6(self):
        """Test case for create6

        Create new CRF Section for specified CRF Version  # noqa: E501
        """
        pass

    def test_delete4(self):
        """Test case for delete4

        Delete CRF Section for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_get_details4(self):
        """Test case for get_details4

        Get CRF details for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_get_list5(self):
        """Test case for get_list5

        Get list of all CRF Sections for specified study  # noqa: E501
        """
        pass

    def test_get_list_for_crf(self):
        """Test case for get_list_for_crf

        Get list of all Section for CRF form in specified study  # noqa: E501
        """
        pass

    def test_get_list_for_crf_version(self):
        """Test case for get_list_for_crf_version

        Get list of all Section for CRF form Version in specified study  # noqa: E501
        """
        pass

    def test_patch1(self):
        """Test case for patch1

        Update some specific CRF Section fields  # noqa: E501
        """
        pass

    def test_update5(self):
        """Test case for update5

        Update CRF Section for specified CRF Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()