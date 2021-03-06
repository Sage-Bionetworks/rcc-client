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
from rcc.models.event_crfs_rpc import EventCrfsRpc  # noqa: E501
from rcc.rest import ApiException

class TestEventCrfsRpc(unittest.TestCase):
    """EventCrfsRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventCrfsRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.event_crfs_rpc.EventCrfsRpc()  # noqa: E501
        if include_optional :
            return EventCrfsRpc(
                id = 56, 
                study_event_id = 56, 
                crf_version_id = 56, 
                crf_id = 56, 
                subject_id = 56, 
                event_definition_crf_id = 56, 
                event_definition_id = 56, 
                status_id = 56, 
                status_code = '0', 
                crf_sequence = 56, 
                event_sequence = 56, 
                event_occurence = 56, 
                crf_occurence = 56
            )
        else :
            return EventCrfsRpc(
        )

    def testEventCrfsRpc(self):
        """Test EventCrfsRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
