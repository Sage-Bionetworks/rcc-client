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
from rcc.models.event_definition_filter import EventDefinitionFilter  # noqa: E501
from rcc.rest import ApiException

class TestEventDefinitionFilter(unittest.TestCase):
    """EventDefinitionFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventDefinitionFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.event_definition_filter.EventDefinitionFilter()  # noqa: E501
        if include_optional :
            return EventDefinitionFilter(
                study_site_ids = [
                    56
                    ], 
                crf_ids = [
                    56
                    ], 
                crf_version_ids = [
                    56
                    ], 
                start_date = 56, 
                end_date = 56
            )
        else :
            return EventDefinitionFilter(
        )

    def testEventDefinitionFilter(self):
        """Test EventDefinitionFilter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
