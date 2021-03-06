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
from rcc.api.study_roles_controller_api import StudyRolesControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestStudyRolesControllerApi(unittest.TestCase):
    """StudyRolesControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.study_roles_controller_api.StudyRolesControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_study_role(self):
        """Test case for delete_study_role

        Delete study role  # noqa: E501
        """
        pass

    def test_get_study_components_list(self):
        """Test case for get_study_components_list

        Get tenant components  # noqa: E501
        """
        pass

    def test_get_study_role_details(self):
        """Test case for get_study_role_details

        Get study role  # noqa: E501
        """
        pass

    def test_get_study_roles_list1(self):
        """Test case for get_study_roles_list1

        Get study roles  # noqa: E501
        """
        pass

    def test_get_tenant_applications(self):
        """Test case for get_tenant_applications

        Get tenant applications  # noqa: E501
        """
        pass

    def test_get_tenant_components(self):
        """Test case for get_tenant_components

        Get tenant components  # noqa: E501
        """
        pass

    def test_save_study_role_details(self):
        """Test case for save_study_role_details

        Save study role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
