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
from rcc.models.od_mcomplex_type_definition_date_time_stamp import ODMcomplexTypeDefinitionDateTimeStamp  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionDateTimeStamp(unittest.TestCase):
    """ODMcomplexTypeDefinitionDateTimeStamp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionDateTimeStamp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_date_time_stamp.ODMcomplexTypeDefinitionDateTimeStamp()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionDateTimeStamp(
                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return ODMcomplexTypeDefinitionDateTimeStamp(
        )

    def testODMcomplexTypeDefinitionDateTimeStamp(self):
        """Test ODMcomplexTypeDefinitionDateTimeStamp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()