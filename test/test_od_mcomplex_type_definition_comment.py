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
from rcc.models.od_mcomplex_type_definition_comment import ODMcomplexTypeDefinitionComment  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionComment(unittest.TestCase):
    """ODMcomplexTypeDefinitionComment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionComment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_comment.ODMcomplexTypeDefinitionComment()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionComment(
                value = '0', 
                sponsor_or_site = 'SPONSOR'
            )
        else :
            return ODMcomplexTypeDefinitionComment(
        )

    def testODMcomplexTypeDefinitionComment(self):
        """Test ODMcomplexTypeDefinitionComment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
