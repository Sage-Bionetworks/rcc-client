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
from rcc.models.ehr_observation_dto import EhrObservationDto  # noqa: E501
from rcc.rest import ApiException

class TestEhrObservationDto(unittest.TestCase):
    """EhrObservationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EhrObservationDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.ehr_observation_dto.EhrObservationDto()  # noqa: E501
        if include_optional :
            return EhrObservationDto(
                encounter_id = '0', 
                encounter_id_aux = '0', 
                variable_codes = [
                    '0'
                    ], 
                variable_code = '0', 
                value = '0', 
                value_index = 56, 
                codeable_concept_value_text = '0', 
                codeable_concept_values = [
                    rcc.models.codeable_concept_dto.CodeableConceptDto(
                        system = '0', 
                        value = '0', )
                    ], 
                codeable_concept_value = rcc.models.codeable_concept_dto.CodeableConceptDto(
                    system = '0', 
                    value = '0', ), 
                quantity_value = '0', 
                quantity_comparator = '0', 
                quantity_unit = '0', 
                boolean_value = True, 
                date_time_value = '0', 
                time_value = '0', 
                reference_range_low = '0', 
                reference_range_high = '0', 
                date_performed = '0', 
                performer = '0', 
                version = '0', 
                first_not_empty_encounter_id = '0'
            )
        else :
            return EhrObservationDto(
        )

    def testEhrObservationDto(self):
        """Test EhrObservationDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
