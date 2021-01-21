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
from rcc.models.survey_scheduler import SurveyScheduler  # noqa: E501
from rcc.rest import ApiException

class TestSurveyScheduler(unittest.TestCase):
    """SurveyScheduler unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SurveyScheduler
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.survey_scheduler.SurveyScheduler()  # noqa: E501
        if include_optional :
            return SurveyScheduler(
                study_event_definition_oid = '0', 
                active = 56, 
                email_subject = '0', 
                email_content = '0', 
                email_sender = '0', 
                condition_surveycomplete_survey_oid = '0', 
                condition_surveycomplete_event_oid = '0', 
                condition_andor_code = '0', 
                condition_logic = '0', 
                condition_send_time_option_code = '0', 
                condition_send_time_lag_days = 56, 
                condition_send_time_lag_hours = 56, 
                condition_send_time_lag_minutes = 56, 
                condition_send_next_day_type_code = '0', 
                condition_send_next_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                condition_send_next_time_exact = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                delivery_type = '0', 
                reminder_type = '0', 
                reminder_time_lag_days = 56, 
                reminder_time_lag_hours = 56, 
                reminder_time_lag_minutes = 56, 
                reminder_next_day_type = '0', 
                reminder_next_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                reminder_exact_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                reminder_num = 56, 
                survey_duration = 56
            )
        else :
            return SurveyScheduler(
        )

    def testSurveyScheduler(self):
        """Test SurveyScheduler"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
