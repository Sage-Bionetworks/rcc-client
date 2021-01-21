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
from rcc.models.item_data_value_rpc import ItemDataValueRpc  # noqa: E501
from rcc.rest import ApiException

class TestItemDataValueRpc(unittest.TestCase):
    """ItemDataValueRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ItemDataValueRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.item_data_value_rpc.ItemDataValueRpc()  # noqa: E501
        if include_optional :
            return ItemDataValueRpc(
                item_data_id = 56, 
                item_data_id_client = 56, 
                item_form_metadata_id = 56, 
                variable_name = '0', 
                data_type_id = 56, 
                data_type = '0', 
                old_values_in_readable_format = [
                    '0'
                    ], 
                values = [
                    '0'
                    ], 
                reason_for_change = '0', 
                coded_items_rpc = rcc.models.medical_coded_items_rpc.MedicalCodedItemsRpc(
                    dictionary_id = 56, 
                    coded_item = rcc.models.medical_coded_item.MedicalCodedItem(
                        preferred_name = '0', 
                        item_details = '0', ), ), 
                new_values_in_readable_format = [
                    '0'
                    ], 
                temp_file_names = [
                    '0'
                    ], 
                delete_files = [
                    56
                    ], 
                value_index = 56, 
                old_value_index = 56, 
                update_audit_logs_and_queries_row_index = True, 
                update_only_index = True, 
                marked_for_complete_delete = True, 
                item_data_sdv_state = True
            )
        else :
            return ItemDataValueRpc(
        )

    def testItemDataValueRpc(self):
        """Test ItemDataValueRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()