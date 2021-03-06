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
from rcc.models.od_mcomplex_type_definition_method_def import ODMcomplexTypeDefinitionMethodDef  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionMethodDef(unittest.TestCase):
    """ODMcomplexTypeDefinitionMethodDef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionMethodDef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_method_def.ODMcomplexTypeDefinitionMethodDef()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionMethodDef(
                description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                    translated_text = [
                        rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                            value = '0', 
                            lang = '0', )
                        ], ), 
                formal_expression = [
                    rcc.models.od_mcomplex_type_definition_formal_expression.ODMcomplexTypeDefinitionFormalExpression(
                        value = '0', 
                        context = '0', )
                    ], 
                alias = [
                    rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                        context = '0', 
                        name = '0', )
                    ], 
                oid = '0', 
                name = '0', 
                type = 'COMPUTATION'
            )
        else :
            return ODMcomplexTypeDefinitionMethodDef(
                description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                    translated_text = [
                        rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                            value = '0', 
                            lang = '0', )
                        ], ),
        )

    def testODMcomplexTypeDefinitionMethodDef(self):
        """Test ODMcomplexTypeDefinitionMethodDef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
