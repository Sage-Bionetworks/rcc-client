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
from rcc.models.od_mcomplex_type_definition_enumerated_item import ODMcomplexTypeDefinitionEnumeratedItem  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionEnumeratedItem(unittest.TestCase):
    """ODMcomplexTypeDefinitionEnumeratedItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionEnumeratedItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_enumerated_item.ODMcomplexTypeDefinitionEnumeratedItem()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionEnumeratedItem(
                alias = [
                    rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                        context = '0', 
                        name = '0', )
                    ], 
                coded_value = '0', 
                ui_width = '0', 
                rank = 1.337, 
                order_number = 56
            )
        else :
            return ODMcomplexTypeDefinitionEnumeratedItem(
        )

    def testODMcomplexTypeDefinitionEnumeratedItem(self):
        """Test ODMcomplexTypeDefinitionEnumeratedItem"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
