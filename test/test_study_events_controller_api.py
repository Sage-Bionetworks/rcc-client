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
from rcc.api.study_events_controller_api import StudyEventsControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestStudyEventsControllerApi(unittest.TestCase):
    """StudyEventsControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.study_events_controller_api.StudyEventsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create9(self):
        """Test case for create9

        Create new Study Event for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_delete6(self):
        """Test case for delete6

        Delete Study Event for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_filter_list1(self):
        """Test case for filter_list1

        Get filtered list of Study Events for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_get_list7(self):
        """Test case for get_list7

        Get list of all Study Events for specified Study  # noqa: E501
        """
        pass

    def test_get_statuses_list(self):
        """Test case for get_statuses_list

        Get list of Available Statuses for Study Events  # noqa: E501
        """
        pass

    def test_save_batch1(self):
        """Test case for save_batch1

        Batch save of Study Events  # noqa: E501
        """
        pass

    def test_update8(self):
        """Test case for update8

        Update existing Study Event for current Study based on auth token provided  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()