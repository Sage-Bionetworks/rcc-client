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
from rcc.models.batch_result import BatchResult  # noqa: E501
from rcc.rest import ApiException

class TestBatchResult(unittest.TestCase):
    """BatchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BatchResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.batch_result.BatchResult()  # noqa: E501
        if include_optional :
            return BatchResult(
                success = [
                    rcc.models.id_map_item.IdMapItem(
                        source_id = 56, 
                        target_id = 56, 
                        description = '0', )
                    ], 
                error = [
                    rcc.models.id_map_item.IdMapItem(
                        source_id = 56, 
                        target_id = 56, 
                        description = '0', )
                    ], 
                comments = '0'
            )
        else :
            return BatchResult(
        )

    def testBatchResult(self):
        """Test BatchResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
