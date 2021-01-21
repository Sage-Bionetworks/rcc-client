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
from rcc.api.surveys_controller_api import SurveysControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestSurveysControllerApi(unittest.TestCase):
    """SurveysControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.surveys_controller_api.SurveysControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create14(self):
        """Test case for create14

        Create new Survey for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_delete11(self):
        """Test case for delete11

        Delete Survey for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_get_details11(self):
        """Test case for get_details11

        Get specified Survey details  # noqa: E501
        """
        pass

    def test_get_filtered_survey_links(self):
        """Test case for get_filtered_survey_links

        Get filtered list of Survey Links  # noqa: E501
        """
        pass

    def test_get_list12(self):
        """Test case for get_list12

        Get list of all Surveys for specified Study  # noqa: E501
        """
        pass

    def test_get_study_event_definitions_list(self):
        """Test case for get_study_event_definitions_list

        Get list of all Event Definitions for specified Study  # noqa: E501
        """
        pass

    def test_get_survey_event_definitions_list(self):
        """Test case for get_survey_event_definitions_list

        Get list of all Survey Event Definitions for specified Study  # noqa: E501
        """
        pass

    def test_update13(self):
        """Test case for update13

        Update Survey for current Study based on auth token provided  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
