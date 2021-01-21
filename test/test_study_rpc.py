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
from rcc.models.study_rpc import StudyRpc  # noqa: E501
from rcc.rest import ApiException

class TestStudyRpc(unittest.TestCase):
    """StudyRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudyRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.study_rpc.StudyRpc()  # noqa: E501
        if include_optional :
            return StudyRpc(
                id = 56, 
                study_version_id = 56, 
                study_version = '1.3', 
                unique_identifier = '0', 
                name = '0', 
                official_title = '0', 
                secondary_identifier = '0', 
                principal_investigator = '0', 
                principal_investigator_user_id = 56, 
                principal_investigator_role_name = '0', 
                ad_lookup_code_by_protocol_type_id = 56, 
                protocol_type = 'Interventional', 
                admin_role_name = '0', 
                summary = '0', 
                sponsor = '0', 
                collaborators = '0', 
                oid = '0', 
                ad_lookup_code_by_purpose_id = 56, 
                purpose_type = 'Treatment', 
                ad_lookup_code_by_control_id = 56, 
                control_type = 'Placebo', 
                ad_lookup_code_by_phase_id = 56, 
                phase_type = 'N/A', 
                ad_lookup_code_by_classification_id = 56, 
                classification_type = 'Safety', 
                ad_lookup_code_by_allocation_id = 56, 
                allocation_type = 'Randomized Clinical Trial', 
                ad_lookup_code_by_intervention_id = 56, 
                ad_lookup_code_by_masking_id = 56, 
                masking_type = 'Open', 
                ad_lookup_code_by_status_id = 56, 
                status_name = 'Development', 
                category_id = 56, 
                screening_start_date = '0', 
                screening_start_date_value = 56, 
                date_planned_start = '0', 
                date_planned_end = '0', 
                protocol_id = '0', 
                protocol_description = '0', 
                protocol_date_verification = '0', 
                ad_lookup_code_by_gender_id = 56, 
                gender_name = 'Male', 
                ad_lookup_code_by_assignment_id = 56, 
                assignment_type = 'Single Group', 
                ad_lookup_code_by_duration_id = 56, 
                duration_type = 'Longitudinal', 
                ad_lookup_code_by_selection_id = 56, 
                selection_type = 'Convenience Sample', 
                ad_lookup_code_by_timing_id = 56, 
                timing_type = 'Retrospective', 
                ad_lookup_code_by_study_type_id = 56, 
                study_type = 'genetic', 
                conditions = '0', 
                keywords = '0', 
                eligibility = '0', 
                study_category = '0', 
                study_status = '0', 
                age_min = 56, 
                age_max = 56, 
                healthy_volunteer_accepted = True, 
                expected_total_enrollment = 56, 
                facility_name = '0', 
                facility_city = '0', 
                facility_state = '0', 
                facility_zip = '0', 
                facility_country = '0', 
                facility_contact_name = '0', 
                facility_contact_degree = '0', 
                facility_phone = '0', 
                facility_email = '0', 
                medline = '0', 
                result_reference = True, 
                url_reference = '0', 
                url_description = '0', 
                is_not_using_sites = True, 
                copy_from_template = True, 
                settings = {
                    'key' : '0'
                    }, 
                other_category = True
            )
        else :
            return StudyRpc(
        )

    def testStudyRpc(self):
        """Test StudyRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
