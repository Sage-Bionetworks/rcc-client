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
from rcc.models.role_component_permission import RoleComponentPermission  # noqa: E501
from rcc.rest import ApiException

class TestRoleComponentPermission(unittest.TestCase):
    """RoleComponentPermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleComponentPermission
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.role_component_permission.RoleComponentPermission()  # noqa: E501
        if include_optional :
            return RoleComponentPermission(
                permission_id = [
                    rcc.models.permission_id.PermissionId(
                        permission_type = 56, 
                        allowed = True, )
                    ], 
                component = '0', 
                component_oid = '0'
            )
        else :
            return RoleComponentPermission(
        )

    def testRoleComponentPermission(self):
        """Test RoleComponentPermission"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
