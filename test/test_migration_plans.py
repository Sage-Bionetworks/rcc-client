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
from rcc.models.migration_plans import MigrationPlans  # noqa: E501
from rcc.rest import ApiException

class TestMigrationPlans(unittest.TestCase):
    """MigrationPlans unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MigrationPlans
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.migration_plans.MigrationPlans()  # noqa: E501
        if include_optional :
            return MigrationPlans(
                migration_plan = [
                    rcc.models.migration_plan.MigrationPlan(
                        migration_branching_logic = [
                            rcc.models.migration_branching_logic.MigrationBranchingLogic(
                                item_metadata_oid = '0', 
                                branching_equation = '0', 
                                reason = '0', 
                                violation_source = '0', )
                            ], 
                        migration_calculated_fields = [
                            rcc.models.migration_calculated_fields.MigrationCalculatedFields(
                                item_metadata_oid = '0', 
                                calculated_field_expression = '0', 
                                reason = '0', 
                                violation_source = '0', )
                            ], 
                        migration_cr_fs = [
                            rcc.models.migration_cr_fs.MigrationCRFs(
                                origin_event_oid = '0', 
                                origin_crf_version_oid = '0', 
                                destination_crf_version_oid = '0', )
                            ], 
                        migration_events = [
                            rcc.models.migration_events.MigrationEvents(
                                not_migrated_event_oid = '0', )
                            ], 
                        migration_mapped_items = [
                            rcc.models.migration_mapped_items.MigrationMappedItems(
                                item_metadata_oid = '0', 
                                mapping_expression = '0', )
                            ], 
                        migration_obsolete_cr_fs = [
                            rcc.models.migration_obsolete_cr_fs.MigrationObsoleteCRFs(
                                origin_event_oid = '0', 
                                obsolete_crf_version_oid = '0', )
                            ], 
                        migration_obsolete_items = [
                            rcc.models.migration_obsolete_items.MigrationObsoleteItems(
                                item_metadata_oid = '0', )
                            ], 
                        migration_plan_subjects = [
                            rcc.models.migration_plan_subjects.MigrationPlanSubjects(
                                subject_oid = '0', )
                            ], 
                        migration_resolved_branching_logic = [
                            rcc.models.migration_resolved_branching_logic.MigrationResolvedBranchingLogic(
                                item_metadata_oid = '0', 
                                branching_equation = '0', )
                            ], 
                        migration_resolved_calculated_fields = [
                            rcc.models.migration_resolved_calculated_fields.MigrationResolvedCalculatedFields(
                                item_metadata_oid = '0', 
                                calculated_equation = '0', )
                            ], 
                        migration_soft_validation_items = [
                            rcc.models.migration_soft_validation_items.MigrationSoftValidationItems(
                                item_metadata_oid = '0', 
                                bypass_comment = '0', 
                                bypassed = True, )
                            ], 
                        migration_subjects = [
                            rcc.models.migration_subjects.MigrationSubjects(
                                subject_oid = '0', 
                                status = '0', )
                            ], 
                        migration_violations = [
                            rcc.models.migration_violations.MigrationViolations(
                                origin_item_metadata_oid = '0', 
                                target_item_metadata_oid = '0', 
                                violation = '0', 
                                violation_factor = '0', 
                                details = '0', )
                            ], 
                        migration_sites = [
                            rcc.models.migration_sites.MigrationSites(
                                site_oid = '0', )
                            ], 
                        title = '0', 
                        status = 56, 
                        migration_subject_option_code = '0', 
                        condition_send_time_option_code = '0', 
                        condition_send_time_lag_days = 56, 
                        condition_send_time_lag_hours = 56, 
                        condition_send_time_lag_minutes = 56, 
                        condition_send_next_day_type_code = '0', 
                        condition_send_next_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        condition_send_next_time_exact = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        subject_number = 56, 
                        owner = '0', 
                        create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return MigrationPlans(
        )

    def testMigrationPlans(self):
        """Test MigrationPlans"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
