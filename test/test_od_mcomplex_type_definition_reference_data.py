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
from rcc.models.od_mcomplex_type_definition_reference_data import ODMcomplexTypeDefinitionReferenceData  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionReferenceData(unittest.TestCase):
    """ODMcomplexTypeDefinitionReferenceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionReferenceData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_reference_data.ODMcomplexTypeDefinitionReferenceData()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionReferenceData(
                item_group_data = [
                    rcc.models.od_mcomplex_type_definition_item_group_data.ODMcomplexTypeDefinitionItemGroupData(
                        audit_record = rcc.models.od_mcomplex_type_definition_audit_record.ODMcomplexTypeDefinitionAuditRecord(
                            user_ref = rcc.models.od_mcomplex_type_definition_user_ref.ODMcomplexTypeDefinitionUserRef(
                                user_oid = '0', ), 
                            location_ref = rcc.models.od_mcomplex_type_definition_location_ref.ODMcomplexTypeDefinitionLocationRef(
                                location_oid = '0', ), 
                            date_time_stamp = rcc.models.od_mcomplex_type_definition_date_time_stamp.ODMcomplexTypeDefinitionDateTimeStamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            reason_for_change = rcc.models.od_mcomplex_type_definition_reason_for_change.ODMcomplexTypeDefinitionReasonForChange(
                                value = '0', ), 
                            source_id = rcc.models.od_mcomplex_type_definition_source_id.ODMcomplexTypeDefinitionSourceID(
                                value = '0', ), 
                            edit_point = 'MONITORING', 
                            used_imputation_method = 'YES', 
                            id = '0', ), 
                        signature = rcc.models.od_mcomplex_type_definition_signature.ODMcomplexTypeDefinitionSignature(
                            user_ref = rcc.models.od_mcomplex_type_definition_user_ref.ODMcomplexTypeDefinitionUserRef(
                                user_oid = '0', ), 
                            location_ref = rcc.models.od_mcomplex_type_definition_location_ref.ODMcomplexTypeDefinitionLocationRef(
                                location_oid = '0', ), 
                            signature_ref = rcc.models.od_mcomplex_type_definition_signature_ref.ODMcomplexTypeDefinitionSignatureRef(
                                signature_oid = '0', ), 
                            date_time_stamp = rcc.models.od_mcomplex_type_definition_date_time_stamp.ODMcomplexTypeDefinitionDateTimeStamp(
                                value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            crypto_binding_manifest = rcc.models.od_mcomplex_type_definition_crypto_binding_manifest.ODMcomplexTypeDefinitionCryptoBindingManifest(
                                value = '0', ), 
                            id = '0', ), 
                        annotation = [
                            rcc.models.od_mcomplex_type_definition_annotation.ODMcomplexTypeDefinitionAnnotation(
                                comment = rcc.models.od_mcomplex_type_definition_comment.ODMcomplexTypeDefinitionComment(
                                    value = '0', 
                                    sponsor_or_site = 'SPONSOR', ), 
                                flag = [
                                    rcc.models.od_mcomplex_type_definition_flag.ODMcomplexTypeDefinitionFlag(
                                        flag_value = rcc.models.od_mcomplex_type_definition_flag_value.ODMcomplexTypeDefinitionFlagValue(
                                            value = '0', 
                                            code_list_oid = '0', ), 
                                        flag_type = rcc.models.od_mcomplex_type_definition_flag_type.ODMcomplexTypeDefinitionFlagType(
                                            value = '0', 
                                            code_list_oid = '0', ), )
                                    ], 
                                seq_num = 56, 
                                transaction_type = 'INSERT', 
                                id = '0', )
                            ], 
                        item_data_group = [
                            rcc.models.od_mcomplex_type_definition_item_data.ODMcomplexTypeDefinitionItemData(
                                measurement_unit_ref = rcc.models.od_mcomplex_type_definition_measurement_unit_ref.ODMcomplexTypeDefinitionMeasurementUnitRef(
                                    measurement_unit_oid = '0', ), 
                                item_oid = '0', 
                                transaction_type = 'INSERT', 
                                is_null = 'YES', 
                                value = '0', 
                                updated_by = '0', 
                                updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                sdv = True, 
                                mrv = True, 
                                drv = True, 
                                sdvby = '0', 
                                sdvdate = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                mrvby = '0', 
                                mrvdate = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                drvby = '0', 
                                drvdate = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        item_data_star_group = [
                            None
                            ], 
                        item_group_oid = '0', 
                        item_group_repeat_key = '0', 
                        transaction_type = 'INSERT', )
                    ], 
                audit_records = [
                    rcc.models.od_mcomplex_type_definition_audit_records.ODMcomplexTypeDefinitionAuditRecords(
                        audit_record = [
                            rcc.models.od_mcomplex_type_definition_audit_record.ODMcomplexTypeDefinitionAuditRecord(
                                user_ref = rcc.models.od_mcomplex_type_definition_user_ref.ODMcomplexTypeDefinitionUserRef(
                                    user_oid = '0', ), 
                                location_ref = rcc.models.od_mcomplex_type_definition_location_ref.ODMcomplexTypeDefinitionLocationRef(
                                    location_oid = '0', ), 
                                date_time_stamp = rcc.models.od_mcomplex_type_definition_date_time_stamp.ODMcomplexTypeDefinitionDateTimeStamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                reason_for_change = rcc.models.od_mcomplex_type_definition_reason_for_change.ODMcomplexTypeDefinitionReasonForChange(
                                    value = '0', ), 
                                source_id = rcc.models.od_mcomplex_type_definition_source_id.ODMcomplexTypeDefinitionSourceID(
                                    value = '0', ), 
                                edit_point = 'MONITORING', 
                                used_imputation_method = 'YES', 
                                id = '0', )
                            ], )
                    ], 
                signatures = [
                    rcc.models.od_mcomplex_type_definition_signatures.ODMcomplexTypeDefinitionSignatures(
                        signature = [
                            rcc.models.od_mcomplex_type_definition_signature.ODMcomplexTypeDefinitionSignature(
                                user_ref = rcc.models.od_mcomplex_type_definition_user_ref.ODMcomplexTypeDefinitionUserRef(
                                    user_oid = '0', ), 
                                location_ref = rcc.models.od_mcomplex_type_definition_location_ref.ODMcomplexTypeDefinitionLocationRef(
                                    location_oid = '0', ), 
                                signature_ref = rcc.models.od_mcomplex_type_definition_signature_ref.ODMcomplexTypeDefinitionSignatureRef(
                                    signature_oid = '0', ), 
                                date_time_stamp = rcc.models.od_mcomplex_type_definition_date_time_stamp.ODMcomplexTypeDefinitionDateTimeStamp(
                                    value = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                crypto_binding_manifest = rcc.models.od_mcomplex_type_definition_crypto_binding_manifest.ODMcomplexTypeDefinitionCryptoBindingManifest(
                                    value = '0', ), 
                                id = '0', )
                            ], )
                    ], 
                annotations = [
                    rcc.models.od_mcomplex_type_definition_annotations.ODMcomplexTypeDefinitionAnnotations(
                        annotation = [
                            rcc.models.od_mcomplex_type_definition_annotation.ODMcomplexTypeDefinitionAnnotation(
                                comment = rcc.models.od_mcomplex_type_definition_comment.ODMcomplexTypeDefinitionComment(
                                    value = '0', 
                                    sponsor_or_site = 'SPONSOR', ), 
                                flag = [
                                    rcc.models.od_mcomplex_type_definition_flag.ODMcomplexTypeDefinitionFlag(
                                        flag_value = rcc.models.od_mcomplex_type_definition_flag_value.ODMcomplexTypeDefinitionFlagValue(
                                            value = '0', 
                                            code_list_oid = '0', ), 
                                        flag_type = rcc.models.od_mcomplex_type_definition_flag_type.ODMcomplexTypeDefinitionFlagType(
                                            value = '0', 
                                            code_list_oid = '0', ), )
                                    ], 
                                seq_num = 56, 
                                transaction_type = 'INSERT', 
                                id = '0', )
                            ], )
                    ], 
                study_oid = '0', 
                meta_data_version_oid = '0'
            )
        else :
            return ODMcomplexTypeDefinitionReferenceData(
        )

    def testODMcomplexTypeDefinitionReferenceData(self):
        """Test ODMcomplexTypeDefinitionReferenceData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()