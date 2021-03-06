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
from rcc.models.site_rpc import SiteRpc  # noqa: E501
from rcc.rest import ApiException

class TestSiteRpc(unittest.TestCase):
    """SiteRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SiteRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.site_rpc.SiteRpc()  # noqa: E501
        if include_optional :
            return SiteRpc(
                id = 56, 
                tenant_id = 56, 
                parent_site_id = 56, 
                name = '0', 
                site_id = '0', 
                time_zone_id = 56, 
                site_type_id = 56, 
                enabled = True, 
                opened = True, 
                locale = '0', 
                summary = '0', 
                facility_name = '0', 
                facility_city = '0', 
                facility_state = '0', 
                facility_zip = '0', 
                facility_country = '0', 
                facility_contact_name = '0', 
                facility_contact_degree = '0', 
                facility_phone = '0', 
                facility_email = '0', 
                children = [
                    rcc.models.site_rpc.SiteRpc(
                        id = 56, 
                        tenant_id = 56, 
                        parent_site_id = 56, 
                        name = '0', 
                        site_id = '0', 
                        time_zone_id = 56, 
                        site_type_id = 56, 
                        enabled = True, 
                        opened = True, 
                        locale = '0', 
                        summary = '0', 
                        facility_name = '0', 
                        facility_city = '0', 
                        facility_state = '0', 
                        facility_zip = '0', 
                        facility_country = '0', 
                        facility_contact_name = '0', 
                        facility_contact_degree = '0', 
                        facility_phone = '0', 
                        facility_email = '0', 
                        children = [
                            rcc.models.site_rpc.SiteRpc(
                                id = 56, 
                                tenant_id = 56, 
                                parent_site_id = 56, 
                                name = '0', 
                                site_id = '0', 
                                time_zone_id = 56, 
                                site_type_id = 56, 
                                enabled = True, 
                                opened = True, 
                                locale = '0', 
                                summary = '0', 
                                facility_name = '0', 
                                facility_city = '0', 
                                facility_state = '0', 
                                facility_zip = '0', 
                                facility_country = '0', 
                                facility_contact_name = '0', 
                                facility_contact_degree = '0', 
                                facility_phone = '0', 
                                facility_email = '0', 
                                site_type_label = '0', 
                                parent_site_name = '0', 
                                time_zone_name = '0', 
                                parent_id = 56, 
                                caption = '0', )
                            ], 
                        site_type_label = '0', 
                        parent_site_name = '0', 
                        time_zone_name = '0', 
                        parent_id = 56, 
                        caption = '0', )
                    ], 
                site_type_label = '0', 
                parent_site_name = '0', 
                time_zone_name = '0', 
                parent_id = 56, 
                caption = '0'
            )
        else :
            return SiteRpc(
        )

    def testSiteRpc(self):
        """Test SiteRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
