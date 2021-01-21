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
from rcc.models.site_view_rpc import SiteViewRpc  # noqa: E501
from rcc.rest import ApiException

class TestSiteViewRpc(unittest.TestCase):
    """SiteViewRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SiteViewRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.site_view_rpc.SiteViewRpc()  # noqa: E501
        if include_optional :
            return SiteViewRpc(
                id = 56, 
                site_name = '0', 
                facility = '0', 
                site_type = '0', 
                enabled = True
            )
        else :
            return SiteViewRpc(
        )

    def testSiteViewRpc(self):
        """Test SiteViewRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()