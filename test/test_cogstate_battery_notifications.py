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
from rcc.models.cogstate_battery_notifications import CogstateBatteryNotifications  # noqa: E501
from rcc.rest import ApiException

class TestCogstateBatteryNotifications(unittest.TestCase):
    """CogstateBatteryNotifications unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CogstateBatteryNotifications
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.cogstate_battery_notifications.CogstateBatteryNotifications()  # noqa: E501
        if include_optional :
            return CogstateBatteryNotifications(
                study_role = [
                    rcc.models.study_role.StudyRole(
                        role_component_permission = [
                            rcc.models.role_component_permission.RoleComponentPermission(
                                permission_id = [
                                    rcc.models.permission_id.PermissionId(
                                        permission_type = 56, 
                                        allowed = True, )
                                    ], 
                                component = '0', 
                                component_oid = '0', )
                            ], 
                        name = '0', 
                        description = '0', 
                        object_data = '0', 
                        enabled = True, 
                        use_classical_menu = True, )
                    ]
            )
        else :
            return CogstateBatteryNotifications(
        )

    def testCogstateBatteryNotifications(self):
        """Test CogstateBatteryNotifications"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
