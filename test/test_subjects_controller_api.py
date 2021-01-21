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
from rcc.api.subjects_controller_api import SubjectsControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestSubjectsControllerApi(unittest.TestCase):
    """SubjectsControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.subjects_controller_api.SubjectsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create13(self):
        """Test case for create13

        Create new Subject for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_create_batch(self):
        """Test case for create_batch

        Batch create new Subjects for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_delete10(self):
        """Test case for delete10

        Delete Subject for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_export_subject_by_enrolled_date(self):
        """Test case for export_subject_by_enrolled_date

        Get list of Subjects by Enrolled Date for specified Study  # noqa: E501
        """
        pass

    def test_filter_subjects(self):
        """Test case for filter_subjects

        Get list of Subjects for Filter  # noqa: E501
        """
        pass

    def test_get_details10(self):
        """Test case for get_details10

        Get specified Subject details  # noqa: E501
        """
        pass

    def test_get_list11(self):
        """Test case for get_list11

        Get list of all Subjects for specified Study  # noqa: E501
        """
        pass

    def test_get_list_for_site(self):
        """Test case for get_list_for_site

        Get list of all Subjects for specified Study Site  # noqa: E501
        """
        pass

    def test_update12(self):
        """Test case for update12

        Update Subject for current Study based on auth token provided  # noqa: E501
        """
        pass

    def test_update_batch(self):
        """Test case for update_batch

        Butch update Subjects List for current Study based on auth token provided  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
