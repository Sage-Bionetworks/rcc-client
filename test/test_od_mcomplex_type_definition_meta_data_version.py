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
from rcc.models.od_mcomplex_type_definition_meta_data_version import ODMcomplexTypeDefinitionMetaDataVersion  # noqa: E501
from rcc.rest import ApiException

class TestODMcomplexTypeDefinitionMetaDataVersion(unittest.TestCase):
    """ODMcomplexTypeDefinitionMetaDataVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ODMcomplexTypeDefinitionMetaDataVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.od_mcomplex_type_definition_meta_data_version.ODMcomplexTypeDefinitionMetaDataVersion()  # noqa: E501
        if include_optional :
            return ODMcomplexTypeDefinitionMetaDataVersion(
                include = rcc.models.od_mcomplex_type_definition_include.ODMcomplexTypeDefinitionInclude(
                    study_oid = '0', 
                    meta_data_version_oid = '0', ), 
                protocol = rcc.models.od_mcomplex_type_definition_protocol.ODMcomplexTypeDefinitionProtocol(
                    description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                        translated_text = [
                            rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                value = '0', 
                                lang = '0', )
                            ], ), 
                    study_event_ref = [
                        rcc.models.od_mcomplex_type_definition_study_event_ref.ODMcomplexTypeDefinitionStudyEventRef(
                            study_event_oid = '0', 
                            order_number = 56, 
                            mandatory = 'YES', 
                            collection_exception_condition_oid = '0', )
                        ], 
                    alias = [
                        rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                            context = '0', 
                            name = '0', )
                        ], ), 
                study_event_def = [
                    rcc.models.od_mcomplex_type_definition_study_event_def.ODMcomplexTypeDefinitionStudyEventDef(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        form_ref = [
                            rcc.models.od_mcomplex_type_definition_form_ref.ODMcomplexTypeDefinitionFormRef(
                                default_version = '0', 
                                source_data_verification = '0', 
                                double_data_entry = True, 
                                display_sequence = 56, 
                                required_crf = True, 
                                hide_crf = True, 
                                accept_new_crf_versions = True, 
                                dynamic_form = True, 
                                source_data_verification_code = 56, 
                                repeating = 'YES', 
                                use_in_progress = True, 
                                form_oid = '0', 
                                order_number = 56, 
                                mandatory = 'YES', 
                                collection_exception_condition_oid = '0', 
                                monitoring = [
                                    rcc.models.monitoring.Monitoring(
                                        partial_item = [
                                            rcc.models.partial_item.PartialItem(
                                                item_name = '0', 
                                                item_oid = '0', 
                                                comment_required = True, 
                                                required = True, )
                                            ], 
                                        type = '0', 
                                        crf_type = '0', 
                                        display_sequence = 56, 
                                        comment_required = True, 
                                        optional = True, )
                                    ], 
                                partial_sdv = [
                                    rcc.models.partial_sdv.PartialSDV(
                                        item_name = '0', 
                                        item_oid = '0', )
                                    ], )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        unique_event_name = '0', 
                        study_event_definition_type = '0', 
                        display_sequence = 56, 
                        day_schedule = 56, 
                        day_min = 56, 
                        day_max = 56, 
                        grace_hour_min = 56, 
                        grace_hour_max = 56, 
                        grace_minute_min = 56, 
                        grace_minute_max = 56, 
                        can_edit_before = True, 
                        can_edit_after = True, 
                        weekdays_only = True, 
                        dynamic_event = True, 
                        repeat_frequency = 56, 
                        repeat_for_how_many_days = 56, 
                        created_by_rule = True, 
                        oid = '0', 
                        name = '0', 
                        repeating = 'YES', 
                        type = 'SCHEDULED', 
                        category = '0', 
                        econsent_event = True, )
                    ], 
                form_def = [
                    rcc.models.od_mcomplex_type_definition_form_def.ODMcomplexTypeDefinitionFormDef(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        item_group_ref = [
                            rcc.models.od_mcomplex_type_definition_item_group_ref.ODMcomplexTypeDefinitionItemGroupRef(
                                order_number = 56, 
                                mandatory = 'YES', 
                                collection_exception_condition_oid = '0', 
                                item_group_oid = '0', )
                            ], 
                        archive_layout = [
                            rcc.models.od_mcomplex_type_definition_archive_layout.ODMcomplexTypeDefinitionArchiveLayout(
                                oid = '0', 
                                pdf_file_name = '0', 
                                presentation_oid = '0', )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        oid = '0', 
                        name = '0', 
                        repeating = 'YES', 
                        available_crf_languages = rcc.models.available_crf_languages.AvailableCrfLanguages(
                            available_crf_language = [
                                rcc.models.available_crf_language.AvailableCrfLanguage(
                                    language_code = '0', )
                                ], ), 
                        language_labels = rcc.models.language_labels.LanguageLabels(
                            language_label = [
                                rcc.models.language_label.LanguageLabel(
                                    object_oid = '0', 
                                    object_type = '0', 
                                    translation = '0', 
                                    translation_plain_text = '0', 
                                    lang_code = '0', )
                                ], ), 
                        crfform_version_definition = rcc.models.crf_form_version_definition.CRFFormVersionDefinition(
                            version_name = '0', 
                            revision_notes = '0', 
                            version_oid = '0', 
                            fields = 56, 
                            revision_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            primary_flag = True, 
                            disp_sequence = 56, 
                            enabled = True, 
                            screening_expression = '0', 
                            screening_flag = True, 
                            custom_enroll_flag = True, 
                            used_at_enroll = True, 
                            randomization_expression = '0', 
                            irb_approval_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            valid_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            valid_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            screening_e_consent_flag = True, 
                            econsent = True, 
                            crfform_definition = rcc.models.crf_form_definition.CRFFormDefinition(
                                name = '0', 
                                sas_name = '0', 
                                show_lock = True, 
                                show_esignature = True, 
                                custom_text = '0', 
                                enable_survey = True, 
                                randomization_flag = True, 
                                available_on_mobile = True, 
                                enable_subject_source = True, 
                                dynamic_form = True, 
                                form_type = '0', 
                                promis_form_oid = '0', 
                                enable_phir_integration = True, 
                                available_in_patient_portal = True, ), 
                            crfform_section = [
                                rcc.models.crf_form_section_definition.CRFFormSectionDefinition(
                                    title = '0', 
                                    subtitle = '0', 
                                    status = '0', 
                                    instructions = '0', 
                                    page_number_label = '0', 
                                    display_sequence = 56, 
                                    borders = 56, 
                                    fields_total_width = 56, 
                                    fields_label_width = 56, 
                                    section_branching_equation = '0', )
                                ], ), )
                    ], 
                item_group_def = [
                    rcc.models.od_mcomplex_type_definition_item_group_def.ODMcomplexTypeDefinitionItemGroupDef(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        item_ref = [
                            rcc.models.od_mcomplex_type_definition_item_ref.ODMcomplexTypeDefinitionItemRef(
                                item_oid = '0', 
                                key_sequence = 56, 
                                method_oid = '0', 
                                imputation_method_oid = '0', 
                                role = '0', 
                                role_code_list_oid = '0', 
                                order_number = 56, 
                                mandatory = 'YES', 
                                collection_exception_condition_oid = '0', )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        oid = '0', 
                        name = '0', 
                        repeating = 'YES', 
                        is_reference_data = 'YES', 
                        domain = '0', 
                        origin = '0', 
                        role = '0', 
                        purpose = '0', 
                        comment = '0', 
                        item_group_definition = rcc.models.item_group_definition.ItemGroupDefinition(
                            item_group_row = [
                                rcc.models.item_group_row.ItemGroupRow(
                                    label = '0', 
                                    display_sequence = 56, )
                                ], 
                            item_group_col = [
                                rcc.models.item_group_col.ItemGroupCol(
                                    label = '0', 
                                    display_sequence = 56, )
                                ], 
                            group_status = '0', 
                            group_type = '0', 
                            section_oid = '0', 
                            name = '0', 
                            oid = '0', 
                            display_sequence = 56, 
                            group_branching_equation = '0', 
                            max_repeating_rows = 56, 
                            is_fixed_rows = True, 
                            is_dummy_flag = True, 
                            original_item_groups_oid = '0', ), 
                        sasdataset_name = '0', )
                    ], 
                item_def = [
                    rcc.models.od_mcomplex_type_definition_item_def.ODMcomplexTypeDefinitionItemDef(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        question = rcc.models.od_mcomplex_type_definition_question.ODMcomplexTypeDefinitionQuestion(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        external_question = rcc.models.od_mcomplex_type_definition_external_question.ODMcomplexTypeDefinitionExternalQuestion(
                            dictionary = '0', 
                            version = '0', 
                            code = '0', ), 
                        measurement_unit_ref = [
                            rcc.models.od_mcomplex_type_definition_measurement_unit_ref.ODMcomplexTypeDefinitionMeasurementUnitRef(
                                measurement_unit_oid = '0', )
                            ], 
                        range_check = [
                            rcc.models.od_mcomplex_type_definition_range_check.ODMcomplexTypeDefinitionRangeCheck(
                                check_value = [
                                    rcc.models.od_mcomplex_type_definition_check_value.ODMcomplexTypeDefinitionCheckValue(
                                        value = '0', )
                                    ], 
                                formal_expression = [
                                    rcc.models.od_mcomplex_type_definition_formal_expression.ODMcomplexTypeDefinitionFormalExpression(
                                        value = '0', 
                                        context = '0', )
                                    ], 
                                error_message = rcc.models.od_mcomplex_type_definition_error_message.ODMcomplexTypeDefinitionErrorMessage(
                                    translated_text = [
                                        rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                            value = '0', 
                                            lang = '0', )
                                        ], ), 
                                comparator = 'LT', 
                                soft_hard = 'SOFT', )
                            ], 
                        code_list_ref = rcc.models.od_mcomplex_type_definition_code_list_ref.ODMcomplexTypeDefinitionCodeListRef(
                            code_list_oid = '0', ), 
                        role = [
                            rcc.models.od_mcomplex_type_definition_role.ODMcomplexTypeDefinitionRole(
                                value = '0', )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        response_type = '0', 
                        oid = '0', 
                        name = '0', 
                        data_type = 'INTEGER', 
                        length = 56, 
                        significant_digits = 56, 
                        origin = '0', 
                        comment = '0', 
                        crfitem_definition = rcc.models.crf_item_definition.CRFItemDefinition(
                            item_document_file = rcc.models.file_base64.FileBase64(
                                value = '0', 
                                file_name = '0', 
                                content_type = '0', 
                                file_size = 56, ), 
                            item_data_type = '0', 
                            measurement_unit_name = '0', 
                            variable_name = '0', 
                            label = '0', 
                            label_plain_text = '0', 
                            phi_status = True, 
                            left_alignment = True, 
                            rc_oid = '0', 
                            field_width = 56, 
                            info_text = '0', 
                            min_value = '0', 
                            max_value = '0', 
                            show_validator = True, 
                            soft_validation = True, 
                            calc_field_equation = '0', 
                            custom_info1 = '0', 
                            custom_info2 = '0', 
                            warning_when_left_empty = '0', 
                            stratification_variable = True, 
                            study_dictionary = '0', 
                            default_value = '0', 
                            subject_group = True, 
                            creation_source = '0', 
                            promis_oid = '0', 
                            promis_final_score = True, 
                            item_fhir_metadata = '0', 
                            required_query_description = '0', 
                            crfitem_metadata = rcc.models.crf_item_metadata.CRFItemMetadata(
                                item_metadata_oid = '0', 
                                column_number = 56, 
                                page_number_label = '0', 
                                question_number_label = '0', 
                                left_item_text = '0', 
                                right_item_text = '0', 
                                regexp = '0', 
                                regexp_error_msg = '0', 
                                ordinal = 56, 
                                required = True, 
                                response_layout = '0', 
                                width_decimal = '0', 
                                show_item = True, 
                                code_ref = '0', 
                                group_oid = '0', 
                                is_required = True, 
                                disp_sequence = 56, 
                                branching_equation = '0', 
                                crf_version_oid = '0', 
                                hide_from_survey = True, 
                                position_row = 56, 
                                position_column = 56, 
                                item_data_type = '0', 
                                measurement_unit_name = '0', 
                                variable_name = '0', 
                                label = '0', 
                                label_plain_text = '0', 
                                phi_status = True, 
                                left_alignment = True, 
                                field_width = 56, 
                                info_text = '0', 
                                min_value = '0', 
                                max_value = '0', 
                                show_validator = True, 
                                soft_validation = True, 
                                calc_field_equation = '0', 
                                custom_info1 = '0', 
                                custom_info2 = '0', 
                                stratification_variable = True, 
                                show_response_set_value_too = True, 
                                study_dictionary = '0', 
                                default_value = '0', 
                                subject_group = True, 
                                required_query_description = '0', 
                                warning_when_left_empty = '0', 
                                dynamic_list_rs_values_eq = '0', 
                                dynamic_list_type = '0', 
                                dynamic_list_no_duplicates = True, 
                                used_in_dys_fields = True, 
                                econsent_signature = True, ), 
                            crfitem_metadata_group = rcc.models.crf_item_metadata_group.CRFItemMetadataGroup(), ), 
                        sasfield_name = '0', 
                        sdsvar_name = '0', )
                    ], 
                repeating_crf_custom_columns_def = [
                    rcc.models.od_mcomplex_type_definition_repeating_crf_custom_columns_def.ODMcomplexTypeDefinitionRepeatingCrfCustomColumnsDef(
                        repeating_crf_custom_columns_ref = [
                            rcc.models.od_mcomplex_type_definition_repeating_crf_custom_columns_ref.ODMcomplexTypeDefinitionRepeatingCrfCustomColumnsRef(
                                item_metadata_oid = '0', 
                                site_oid = '0', 
                                event_definition_oid = '0', 
                                display_sequence = 56, )
                            ], 
                        item_metadata_oid = '0', 
                        site_oid = '0', 
                        event_definition_oid = '0', 
                        display_sequence = 56, )
                    ], 
                code_list = [
                    rcc.models.od_mcomplex_type_definition_code_list.ODMcomplexTypeDefinitionCodeList(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        code_list_item = [
                            rcc.models.od_mcomplex_type_definition_code_list_item.ODMcomplexTypeDefinitionCodeListItem(
                                decode = rcc.models.od_mcomplex_type_definition_decode.ODMcomplexTypeDefinitionDecode(
                                    translated_text = [
                                        rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                            value = '0', 
                                            lang = '0', )
                                        ], ), 
                                alias = [
                                    rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                        context = '0', 
                                        name = '0', )
                                    ], 
                                coded_value = '0', 
                                ui_width = '0', 
                                rank = 1.337, 
                                order_number = 56, )
                            ], 
                        external_code_list = rcc.models.od_mcomplex_type_definition_external_code_list.ODMcomplexTypeDefinitionExternalCodeList(
                            dictionary = '0', 
                            version = '0', 
                            href = '0', 
                            ref = '0', ), 
                        enumerated_item = [
                            rcc.models.od_mcomplex_type_definition_enumerated_item.ODMcomplexTypeDefinitionEnumeratedItem(
                                coded_value = '0', 
                                ui_width = '0', 
                                rank = 1.337, 
                                order_number = 56, )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        oid = '0', 
                        name = '0', 
                        data_type = 'INTEGER', 
                        label = '0', 
                        form_oid = '0', 
                        response_type = '0', 
                        hidden = True, 
                        is_global = True, 
                        sasformat_name = '0', )
                    ], 
                imputation_method = [
                    rcc.models.od_mcomplex_type_definition_imputation_method.ODMcomplexTypeDefinitionImputationMethod(
                        value = '0', 
                        oid = '0', )
                    ], 
                presentation = [
                    rcc.models.od_mcomplex_type_definition_presentation.ODMcomplexTypeDefinitionPresentation(
                        value = '0', 
                        oid = '0', 
                        lang = '0', )
                    ], 
                condition_def = [
                    rcc.models.od_mcomplex_type_definition_condition_def.ODMcomplexTypeDefinitionConditionDef(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        formal_expression = [
                            rcc.models.od_mcomplex_type_definition_formal_expression.ODMcomplexTypeDefinitionFormalExpression(
                                value = '0', 
                                context = '0', )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        oid = '0', 
                        name = '0', )
                    ], 
                method_def = [
                    rcc.models.od_mcomplex_type_definition_method_def.ODMcomplexTypeDefinitionMethodDef(
                        description = rcc.models.od_mcomplex_type_definition_description.ODMcomplexTypeDefinitionDescription(
                            translated_text = [
                                rcc.models.od_mcomplex_type_definition_translated_text.ODMcomplexTypeDefinitionTranslatedText(
                                    value = '0', 
                                    lang = '0', )
                                ], ), 
                        formal_expression = [
                            rcc.models.od_mcomplex_type_definition_formal_expression.ODMcomplexTypeDefinitionFormalExpression(
                                value = '0', 
                                context = '0', )
                            ], 
                        alias = [
                            rcc.models.od_mcomplex_type_definition_alias.ODMcomplexTypeDefinitionAlias(
                                context = '0', 
                                name = '0', )
                            ], 
                        oid = '0', 
                        name = '0', 
                        type = 'COMPUTATION', )
                    ], 
                oid = '0', 
                name = '0', 
                description = '0'
            )
        else :
            return ODMcomplexTypeDefinitionMetaDataVersion(
        )

    def testODMcomplexTypeDefinitionMetaDataVersion(self):
        """Test ODMcomplexTypeDefinitionMetaDataVersion"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()