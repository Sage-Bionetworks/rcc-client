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
from rcc.models.study_event import StudyEvent  # noqa: E501
from rcc.rest import ApiException

class TestStudyEvent(unittest.TestCase):
    """StudyEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StudyEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.study_event.StudyEvent()  # noqa: E501
        if include_optional :
            return StudyEvent(
                study_event_crf = [
                    rcc.models.study_event_crf.StudyEventCrf(
                        crf_version_oid = '0', 
                        date_interviewed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        interviewer_name = '0', 
                        status_code = '0', 
                        annotations = '0', 
                        validator_annotations = '0', 
                        validate_string = '0', 
                        owner = '0', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        electronic_signature_status = True, 
                        lock_status = True, 
                        date_completed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date_dde_started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date_dde_completed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        date_sdv = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        medical_reviwed_by_id = '0', 
                        medical_reviwed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        medical_reviwed_status = True, 
                        medical_review_comment = '0', 
                        study_reviwed_by_id = '0', 
                        study_reviwed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        study_reviwed_status = True, 
                        study_review_comment = '0', 
                        disable_trigger = True, 
                        signature_history = True, 
                        signature_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        signature_owner = '0', 
                        states = '0', 
                        date_de_started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        migration_locked = True, 
                        sdvcomment = '0', 
                        ddecompleted_by_id = '0', 
                        destarted_by_id = '0', )
                    ], 
                subject_oid = '0', 
                event_definition_oid = '0', 
                location = '0', 
                occurence = 56, 
                date_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                date_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                status = '0', 
                start_time_flag = True, 
                end_time_flag = True, 
                reference_visit_oid = '0', 
                signature_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                signature_owner = '0', 
                signature_history = True, 
                states = '0', 
                study_event_oid = '0', 
                repeating_form_parent_oid = '0', 
                migration_locked = True
            )
        else :
            return StudyEvent(
        )

    def testStudyEvent(self):
        """Test StudyEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
