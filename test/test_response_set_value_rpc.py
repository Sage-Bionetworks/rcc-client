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
from rcc.models.response_set_value_rpc import ResponseSetValueRpc  # noqa: E501
from rcc.rest import ApiException

class TestResponseSetValueRpc(unittest.TestCase):
    """ResponseSetValueRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResponseSetValueRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.response_set_value_rpc.ResponseSetValueRpc()  # noqa: E501
        if include_optional :
            return ResponseSetValueRpc(
                id = 56, 
                study_id = 56, 
                response_sets_id = 56, 
                options_text = '0', 
                value = '0', 
                display_sequence = 56
            )
        else :
            return ResponseSetValueRpc(
        )

    def testResponseSetValueRpc(self):
        """Test ResponseSetValueRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
