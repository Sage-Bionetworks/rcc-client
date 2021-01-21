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
from rcc.models.parent_global_sites import ParentGlobalSites  # noqa: E501
from rcc.rest import ApiException

class TestParentGlobalSites(unittest.TestCase):
    """ParentGlobalSites unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParentGlobalSites
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.parent_global_sites.ParentGlobalSites()  # noqa: E501
        if include_optional :
            return ParentGlobalSites(
                global_site = [
                    rcc.models.global_site.GlobalSite(
                        global_site_parent = rcc.models.global_site_parent.GlobalSiteParent(
                            parent_site_name = '0', 
                            parent_site_oid = '0', 
                            parent_site_initial_id = 56, ), 
                        source_site_initial_id = 56, 
                        name = '0', 
                        site_oid = '0', 
                        site_type_oid = '0', 
                        enabled = True, 
                        data_collection_enabled = True, 
                        facility_name = '0', 
                        facility_city = '0', 
                        facility_state = '0', 
                        facility_zip = '0', 
                        facility_country = '0', 
                        facility_contact_name = '0', 
                        facility_contact_degree = '0', 
                        facility_phone = '0', 
                        facility_email = '0', )
                    ]
            )
        else :
            return ParentGlobalSites(
        )

    def testParentGlobalSites(self):
        """Test ParentGlobalSites"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
