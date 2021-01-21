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
from rcc.api.i_paa_s_subject_controller_api import IPaaSSubjectControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestIPaaSSubjectControllerApi(unittest.TestCase):
    """IPaaSSubjectControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.i_paa_s_subject_controller_api.IPaaSSubjectControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_subject_encounters(self):
        """Test case for get_subject_encounters

        Get subjects Encounters eligible for integration.  # noqa: E501
        """
        pass

    def test_get_subject_mr_ns(self):
        """Test case for get_subject_mr_ns

        Get subjects MRNs eligible for integration.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()