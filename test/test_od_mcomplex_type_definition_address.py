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
from rcc.models.od_mcomplex_type_definition_address import ODMcomplexTypeDefinitionAddress  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionAddress(unittest.TestCase):
    """ODMcomplexTypeDefinitionAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_address.ODMcomplexTypeDefinitionAddress()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionAddress(
                street_name = [
                    rcc.models.od_mcomplex_type_definition_street_name.ODMcomplexTypeDefinitionStreetName(
                        value = '0', )
                    ], 
                city = rcc.models.od_mcomplex_type_definition_city.ODMcomplexTypeDefinitionCity(
                    value = '0', ), 
                state_prov = rcc.models.od_mcomplex_type_definition_state_prov.ODMcomplexTypeDefinitionStateProv(
                    value = '0', ), 
                country = rcc.models.od_mcomplex_type_definition_country.ODMcomplexTypeDefinitionCountry(
                    value = '0', ), 
                postal_code = rcc.models.od_mcomplex_type_definition_postal_code.ODMcomplexTypeDefinitionPostalCode(
                    value = '0', ), 
                other_text = rcc.models.od_mcomplex_type_definition_other_text.ODMcomplexTypeDefinitionOtherText(
                    value = '0', )
            )
        else :
            return ODMcomplexTypeDefinitionAddress(
        )

    def testODMcomplexTypeDefinitionAddress(self):
        """Test ODMcomplexTypeDefinitionAddress"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
