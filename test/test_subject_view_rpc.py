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
from rcc.models.subject_view_rpc import SubjectViewRpc  # noqa: E501
from rcc.rest import ApiException

class TestSubjectViewRpc(unittest.TestCase):
    """SubjectViewRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubjectViewRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.subject_view_rpc.SubjectViewRpc()  # noqa: E501
        if include_optional :
            return SubjectViewRpc(
                id = 56, 
                client_id = 56, 
                study_id = 56, 
                unique_identifier = '0', 
                rc_oid = '0', 
                study_site_id = 56, 
                study_site_name = '0', 
                protocol_id = '0', 
                date_screened = 56, 
                update_date = 56, 
                status_id = 56, 
                status = 'Enrolled', 
                initials = '0', 
                email = '0', 
                screening_number = '0', 
                randomization_id = 56, 
                crf_version_screening_id = 56, 
                force_manual_subject_number = True, 
                custom_enroll_crf_used = True, 
                mrn = '0'
            )
        else :
            return SubjectViewRpc(
        )

    def testSubjectViewRpc(self):
        """Test SubjectViewRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
