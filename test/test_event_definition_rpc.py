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
from rcc.models.event_definition_rpc import EventDefinitionRpc  # noqa: E501
from rcc.rest import ApiException

class TestEventDefinitionRpc(unittest.TestCase):
    """EventDefinitionRpc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventDefinitionRpc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.event_definition_rpc.EventDefinitionRpc()  # noqa: E501
        if include_optional :
            return EventDefinitionRpc(
                id = 56, 
                study_id = 56, 
                name = '0', 
                unique_event_name = '0', 
                description = '0', 
                ad_lookup_code_by_event_def_type_id = 56, 
                ad_lookup_codes_by_status_id = 56, 
                disp_sequence = 56, 
                repeating = False, 
                repeating_frequency = 1, 
                repeating_daily_how_many_days = 56, 
                repeating_how_many_times = 56, 
                created_by_rule = False, 
                ad_lookup_code_by_category_id = 56, 
                reference_visit = False, 
                day_schedule = 56, 
                day_min = 56, 
                day_max = 56, 
                calendared_type_lc_id = 56, 
                grace_hour_min = 56, 
                grace_hour_max = 56, 
                grace_minute_min = 56, 
                grace_minute_max = 56, 
                can_edit_before_event = False, 
                can_edit_after_event = False, 
                weekdays_only = False, 
                dynamic_event = False, 
                create_date = 56, 
                update_date = 56
            )
        else :
            return EventDefinitionRpc(
        )

    def testEventDefinitionRpc(self):
        """Test EventDefinitionRpc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
