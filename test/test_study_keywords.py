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
from rcc.models.study_keywords import StudyKeywords  # noqa: E501
from rcc.rest import ApiException

class TestStudyKeywords(unittest.TestCase):
    """StudyKeywords unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudyKeywords
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.study_keywords.StudyKeywords()  # noqa: E501
        if include_optional :
            return StudyKeywords(
                study_keyword = [
                    rcc.models.study_keyword.StudyKeyword(
                        study_keyword_value = [
                            rcc.models.study_keyword_value.StudyKeywordValue(
                                language = '0', 
                                language_code = '0', 
                                language_name = '0', 
                                translation = '0', )
                            ], 
                        keyword = '0', )
                    ]
            )
        else :
            return StudyKeywords(
        )

    def testStudyKeywords(self):
        """Test StudyKeywords"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()