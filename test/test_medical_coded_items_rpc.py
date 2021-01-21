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
from rcc.models.medical_coded_items_rpc import MedicalCodedItemsRpc  # noqa: E501
from rcc.rest import ApiException

class TestMedicalCodedItemsRpc(unittest.TestCase):
    """MedicalCodedItemsRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MedicalCodedItemsRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.medical_coded_items_rpc.MedicalCodedItemsRpc()  # noqa: E501
        if include_optional :
            return MedicalCodedItemsRpc(
                dictionary_id = 56, 
                coded_item = rcc.models.medical_coded_item.MedicalCodedItem(
                    preferred_name = '0', 
                    item_details = '0', )
            )
        else :
            return MedicalCodedItemsRpc(
        )

    def testMedicalCodedItemsRpc(self):
        """Test MedicalCodedItemsRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
