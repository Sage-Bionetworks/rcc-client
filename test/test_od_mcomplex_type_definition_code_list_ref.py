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
from rcc.models.od_mcomplex_type_definition_code_list_ref import ODMcomplexTypeDefinitionCodeListRef  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionCodeListRef(unittest.TestCase):
    """ODMcomplexTypeDefinitionCodeListRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionCodeListRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_code_list_ref.ODMcomplexTypeDefinitionCodeListRef()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionCodeListRef(
                code_list_oid = '0'
            )
        else :
            return ODMcomplexTypeDefinitionCodeListRef(
        )

    def testODMcomplexTypeDefinitionCodeListRef(self):
        """Test ODMcomplexTypeDefinitionCodeListRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
