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
from rcc.models.study_sequence import StudySequence  # noqa: E501
from rcc.rest import ApiException

class TestStudySequence(unittest.TestCase):
    """StudySequence unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudySequence
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.study_sequence.StudySequence()  # noqa: E501
        if include_optional :
            return StudySequence(
                entity_type = '0', 
                next_available_sequence = 56, 
                site_oid = '0'
            )
        else :
            return StudySequence(
        )

    def testStudySequence(self):
        """Test StudySequence"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
