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
from rcc.models.randomization import Randomization  # noqa: E501
from rcc.rest import ApiException

class TestRandomization(unittest.TestCase):
    """Randomization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Randomization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.randomization.Randomization()  # noqa: E501
        if include_optional :
            return Randomization(
                randomization_config = [
                    rcc.models.randomization_config.RandomizationConfig(
                        block_size = 56, 
                        mimimum_block_size = 56, 
                        maximum_block_size = 56, 
                        initial_balls = 56, 
                        success = 56, 
                        failure = 56, 
                        description = '0', 
                        first_option = '0', 
                        second_option = '0', 
                        replaced_balls = 56, 
                        data_oid = '0', 
                        stratify_study_site = True, 
                        status = '0', 
                        algorythm_type = '0', 
                        block_randomization_type = '0', 
                        block_randomization_constraint = '0', 
                        block_history = '0', 
                        block_history_printout = '0', 
                        mti = 56, 
                        probability = 1.337, 
                        dtype = '0', 
                        pvalue = 1.337, 
                        dname = '0', )
                    ], 
                study_group_randomization = [
                    rcc.models.study_group_randomization.StudyGroupRandomization(
                        randomization_oid = '0', 
                        subject = '0', 
                        study_group_class = '0', 
                        properties = '0', 
                        index = 56, )
                    ], 
                custom_schedule_randomization = [
                    rcc.models.custom_schedule_randomization.CustomScheduleRandomization(
                        study_group_name = '0', 
                        site_name = '0', 
                        subject_number = '0', 
                        processed = True, )
                    ], 
                custom_schedule_randomization_mapping = [
                    rcc.models.custom_schedule_randomization_mapping.CustomScheduleRandomizationMapping(
                        mapping_oid = '0', 
                        column_name = '0', 
                        crf_variable_name = '0', 
                        study_level_variable = '0', 
                        show_on_ui = True, )
                    ], 
                custom_schedule_randomization_values = [
                    rcc.models.custom_schedule_randomization_values.CustomScheduleRandomizationValues(
                        mapping_oid = '0', 
                        randomization_oid = '0', 
                        value = '0', 
                        index = 56, 
                        processed = True, )
                    ]
            )
        else :
            return Randomization(
        )

    def testRandomization(self):
        """Test Randomization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
