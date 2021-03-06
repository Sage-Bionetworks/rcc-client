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
from rcc.models.survey_link import SurveyLink  # noqa: E501
from rcc.rest import ApiException

class TestSurveyLink(unittest.TestCase):
    """SurveyLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SurveyLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.survey_link.SurveyLink()  # noqa: E501
        if include_optional :
            return SurveyLink(
                subject_oid = '0', 
                subject_id = '0', 
                study_event_definition_oid = '0', 
                event_name = '0', 
                crf_oid = '0', 
                crf_name = '0', 
                crf_version_oid = '0', 
                code = '0', 
                failed_attempts = 56, 
                locked_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                preview_only = 56, 
                public_survey = 56, 
                site_oid = '0', 
                recent = 56
            )
        else :
            return SurveyLink(
        )

    def testSurveyLink(self):
        """Test SurveyLink"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
