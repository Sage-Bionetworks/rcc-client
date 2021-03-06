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
from rcc.models.survey_rpc import SurveyRpc  # noqa: E501
from rcc.rest import ApiException

class TestSurveyRpc(unittest.TestCase):
    """SurveyRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SurveyRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.survey_rpc.SurveyRpc()  # noqa: E501
        if include_optional :
            return SurveyRpc(
                id = 56, 
                title = '0', 
                logo_url = '0', 
                acknowledgement = '0', 
                question_auto_numbering = 56, 
                question_by_section = 56, 
                display_page_number = True, 
                hide_back_button = True, 
                show_required_field_text = True, 
                view_results = 56, 
                min_responses_view_results = 56, 
                check_diversity_view_results = True, 
                survey_expiration = 56, 
                save_and_return = True, 
                hide_submit = True, 
                customize_time_availability = True, 
                close_after_completion = True, 
                availability_from_time = '0', 
                availability_to_time = '0', 
                edit_completed_response = True, 
                end_survey_redirect_url = '0', 
                end_survey_redirect_to_my_health = True, 
                survey_redirect_message = '0', 
                survey_thank_you_message = '0', 
                promise_skip_question = True, 
                survey_auth_enabled_single = True, 
                send_confirmation_email = True, 
                confirmation_email_subject = '0', 
                confirmation_email_content = '0', 
                confirmation_email_from = '0', 
                study_id = 56, 
                crf_version_id = 56, 
                instructions = '0', 
                enabled = True, 
                hide_title = True, 
                calendared_invitation_enabled = True
            )
        else :
            return SurveyRpc(
        )

    def testSurveyRpc(self):
        """Test SurveyRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
