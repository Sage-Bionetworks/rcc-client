# coding: utf-8

"""
    nPhase REST Resource

    REDCap REST API v.2  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rcc
from rcc.models.academic_study_group_class_view_rpc import AcademicStudyGroupClassViewRpc  # noqa: E501
from rcc.rest import ApiException

class TestAcademicStudyGroupClassViewRpc(unittest.TestCase):
    """AcademicStudyGroupClassViewRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AcademicStudyGroupClassViewRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.academic_study_group_class_view_rpc.AcademicStudyGroupClassViewRpc()  # noqa: E501
        if include_optional :
            return AcademicStudyGroupClassViewRpc(
                id = 56, 
                study_id = 56, 
                group_class_type_id = 56, 
                group_class_type_name = '0', 
                subject_assignment_id = 56, 
                subject_assignment_name = '0', 
                name = '0', 
                is_default = True, 
                disp_sequence = 56, 
                planned_size = 56, 
                enabled = True, 
                names = [
                    '0'
                    ]
            )
        else :
            return AcademicStudyGroupClassViewRpc(
        )

    def testAcademicStudyGroupClassViewRpc(self):
        """Test AcademicStudyGroupClassViewRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()