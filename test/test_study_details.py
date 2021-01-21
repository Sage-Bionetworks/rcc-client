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
from rcc.models.study_details import StudyDetails  # noqa: E501
from rcc.rest import ApiException

class TestStudyDetails(unittest.TestCase):
    """StudyDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudyDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.study_details.StudyDetails()  # noqa: E501
        if include_optional :
            return StudyDetails(
                name = '0', 
                unique_identifier = '0', 
                category = '0', 
                brief_title = '0', 
                status = '0', 
                study_version = '0', 
                official_title = '0', 
                secondary_ids = '0', 
                summary = '0', 
                protocol_id = '0', 
                detailed_description = '0', 
                sponsor = '0', 
                collaborators = '0', 
                screening_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                study_phase = '0', 
                protocol_verification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                study_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                study_completion_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                purpose = '0', 
                allocation = '0', 
                masking = '0', 
                control = '0', 
                intervention_model = '0', 
                study_classification = '0', 
                duration = '0', 
                selection = '0', 
                timing = '0', 
                study_type = '0', 
                gender = '0', 
                principal_investigator = '0', 
                info = '0', 
                conditions = '0', 
                keywords = '0', 
                eligibility_criteria = '0', 
                minimum_age = 56, 
                maximum_age = 56, 
                healthy_volunteer_accepted = True, 
                expected_total_enrollment = 56, 
                facility_name = '0', 
                facility_city = '0', 
                facility_state = '0', 
                facility_zip = '0', 
                facility_country = '0', 
                facility_contact_name = '0', 
                facility_contact_degree = '0', 
                facility_contact_phone = '0', 
                facility_contact_email = '0', 
                medline_identifier = '0', 
                result_referense = True, 
                url_reference = '0', 
                url_description = '0', 
                branding_logo = '0', 
                branding_logo_file_name = '0', 
                branding_logo_content_type = '0', 
                pdf_footnote = '0', 
                help_desk = '0'
            )
        else :
            return StudyDetails(
        )

    def testStudyDetails(self):
        """Test StudyDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
