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
from rcc.models.item_group_rpc import ItemGroupRpc  # noqa: E501
from rcc.rest import ApiException

class TestItemGroupRpc(unittest.TestCase):
    """ItemGroupRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ItemGroupRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.item_group_rpc.ItemGroupRpc()  # noqa: E501
        if include_optional :
            return ItemGroupRpc(
                id = 56, 
                add_lookup_code_by_group_type = '0', 
                section_rpc = rcc.models.section_rpc.SectionRpc(
                    id = 56, 
                    crf_id = 56, 
                    rc_crf_versions_id = 56, 
                    label = '0', 
                    title = '0', 
                    subtitle = '0', 
                    instructions = '0', 
                    page_number_label = '0', 
                    display_sequence = 56, 
                    parent_id = 56, 
                    borders = 56, 
                    fields_total_width = 56, 
                    field_labels_width = 56, ), 
                name = '0', 
                rc_oid = '0', 
                display_sequence = 1.337, 
                group_branching_equation = '0', 
                dummy_flag = True, 
                fixed_rows_flag = True, 
                group_row_list = [
                    rcc.models.item_group_row_rpc.ItemGroupRowRpc(
                        id = 56, 
                        rc_item_groups_id = 56, 
                        label = '0', 
                        display_sequence = 56, )
                    ], 
                group_column_list = [
                    rcc.models.item_group_column_rpc.ItemGroupColumnRpc(
                        id = 56, 
                        rc_item_groups_id = 56, 
                        label = '0', 
                        display_sequence = 56, )
                    ]
            )
        else :
            return ItemGroupRpc(
        )

    def testItemGroupRpc(self):
        """Test ItemGroupRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
