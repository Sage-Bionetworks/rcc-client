# coding: utf-8

"""
    nPhase REST Resource

    REDCap REST API v.2  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from rcc.configuration import Configuration


class ExportOptions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'study_site_id': 'int',
        'subjects': 'list[str]',
        'events': 'list[str]',
        'crf_forms': 'list[str]',
        'crf_versions': 'list[str]',
        'crf_items': 'list[str]',
        'sites': 'list[str]',
        'date_from': 'str',
        'date_to': 'str',
        'extract_data_delta': 'bool',
        'decoded_values': 'bool',
        'use_odm_extended_format': 'bool',
        'use_sdm_mode': 'bool',
        'use_redcap_record_metadata': 'bool',
        'use_concept_value': 'bool',
        'export_empty_values': 'bool'
    }

    attribute_map = {
        'study_site_id': 'studySiteId',
        'subjects': 'subjects',
        'events': 'events',
        'crf_forms': 'crfForms',
        'crf_versions': 'crfVersions',
        'crf_items': 'crfItems',
        'sites': 'sites',
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'extract_data_delta': 'extractDataDelta',
        'decoded_values': 'decodedValues',
        'use_odm_extended_format': 'useODMExtendedFormat',
        'use_sdm_mode': 'useSDMMode',
        'use_redcap_record_metadata': 'useRedcapRecordMetadata',
        'use_concept_value': 'useConceptValue',
        'export_empty_values': 'exportEmptyValues'
    }

    def __init__(self, study_site_id=None, subjects=None, events=None, crf_forms=None, crf_versions=None, crf_items=None, sites=None, date_from=None, date_to=None, extract_data_delta=None, decoded_values=None, use_odm_extended_format=None, use_sdm_mode=None, use_redcap_record_metadata=None, use_concept_value=None, export_empty_values=None, local_vars_configuration=None):  # noqa: E501
        """ExportOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_site_id = None
        self._subjects = None
        self._events = None
        self._crf_forms = None
        self._crf_versions = None
        self._crf_items = None
        self._sites = None
        self._date_from = None
        self._date_to = None
        self._extract_data_delta = None
        self._decoded_values = None
        self._use_odm_extended_format = None
        self._use_sdm_mode = None
        self._use_redcap_record_metadata = None
        self._use_concept_value = None
        self._export_empty_values = None
        self.discriminator = None

        if study_site_id is not None:
            self.study_site_id = study_site_id
        if subjects is not None:
            self.subjects = subjects
        if events is not None:
            self.events = events
        if crf_forms is not None:
            self.crf_forms = crf_forms
        if crf_versions is not None:
            self.crf_versions = crf_versions
        if crf_items is not None:
            self.crf_items = crf_items
        if sites is not None:
            self.sites = sites
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if extract_data_delta is not None:
            self.extract_data_delta = extract_data_delta
        if decoded_values is not None:
            self.decoded_values = decoded_values
        if use_odm_extended_format is not None:
            self.use_odm_extended_format = use_odm_extended_format
        if use_sdm_mode is not None:
            self.use_sdm_mode = use_sdm_mode
        if use_redcap_record_metadata is not None:
            self.use_redcap_record_metadata = use_redcap_record_metadata
        if use_concept_value is not None:
            self.use_concept_value = use_concept_value
        if export_empty_values is not None:
            self.export_empty_values = export_empty_values

    @property
    def study_site_id(self):
        """Gets the study_site_id of this ExportOptions.  # noqa: E501


        :return: The study_site_id of this ExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._study_site_id

    @study_site_id.setter
    def study_site_id(self, study_site_id):
        """Sets the study_site_id of this ExportOptions.


        :param study_site_id: The study_site_id of this ExportOptions.  # noqa: E501
        :type: int
        """

        self._study_site_id = study_site_id

    @property
    def subjects(self):
        """Gets the subjects of this ExportOptions.  # noqa: E501


        :return: The subjects of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this ExportOptions.


        :param subjects: The subjects of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._subjects = subjects

    @property
    def events(self):
        """Gets the events of this ExportOptions.  # noqa: E501


        :return: The events of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ExportOptions.


        :param events: The events of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def crf_forms(self):
        """Gets the crf_forms of this ExportOptions.  # noqa: E501


        :return: The crf_forms of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._crf_forms

    @crf_forms.setter
    def crf_forms(self, crf_forms):
        """Sets the crf_forms of this ExportOptions.


        :param crf_forms: The crf_forms of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._crf_forms = crf_forms

    @property
    def crf_versions(self):
        """Gets the crf_versions of this ExportOptions.  # noqa: E501


        :return: The crf_versions of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._crf_versions

    @crf_versions.setter
    def crf_versions(self, crf_versions):
        """Sets the crf_versions of this ExportOptions.


        :param crf_versions: The crf_versions of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._crf_versions = crf_versions

    @property
    def crf_items(self):
        """Gets the crf_items of this ExportOptions.  # noqa: E501


        :return: The crf_items of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._crf_items

    @crf_items.setter
    def crf_items(self, crf_items):
        """Sets the crf_items of this ExportOptions.


        :param crf_items: The crf_items of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._crf_items = crf_items

    @property
    def sites(self):
        """Gets the sites of this ExportOptions.  # noqa: E501


        :return: The sites of this ExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ExportOptions.


        :param sites: The sites of this ExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._sites = sites

    @property
    def date_from(self):
        """Gets the date_from of this ExportOptions.  # noqa: E501


        :return: The date_from of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this ExportOptions.


        :param date_from: The date_from of this ExportOptions.  # noqa: E501
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this ExportOptions.  # noqa: E501


        :return: The date_to of this ExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this ExportOptions.


        :param date_to: The date_to of this ExportOptions.  # noqa: E501
        :type: str
        """

        self._date_to = date_to

    @property
    def extract_data_delta(self):
        """Gets the extract_data_delta of this ExportOptions.  # noqa: E501


        :return: The extract_data_delta of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._extract_data_delta

    @extract_data_delta.setter
    def extract_data_delta(self, extract_data_delta):
        """Sets the extract_data_delta of this ExportOptions.


        :param extract_data_delta: The extract_data_delta of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._extract_data_delta = extract_data_delta

    @property
    def decoded_values(self):
        """Gets the decoded_values of this ExportOptions.  # noqa: E501


        :return: The decoded_values of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._decoded_values

    @decoded_values.setter
    def decoded_values(self, decoded_values):
        """Sets the decoded_values of this ExportOptions.


        :param decoded_values: The decoded_values of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._decoded_values = decoded_values

    @property
    def use_odm_extended_format(self):
        """Gets the use_odm_extended_format of this ExportOptions.  # noqa: E501


        :return: The use_odm_extended_format of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_odm_extended_format

    @use_odm_extended_format.setter
    def use_odm_extended_format(self, use_odm_extended_format):
        """Sets the use_odm_extended_format of this ExportOptions.


        :param use_odm_extended_format: The use_odm_extended_format of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._use_odm_extended_format = use_odm_extended_format

    @property
    def use_sdm_mode(self):
        """Gets the use_sdm_mode of this ExportOptions.  # noqa: E501


        :return: The use_sdm_mode of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_sdm_mode

    @use_sdm_mode.setter
    def use_sdm_mode(self, use_sdm_mode):
        """Sets the use_sdm_mode of this ExportOptions.


        :param use_sdm_mode: The use_sdm_mode of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._use_sdm_mode = use_sdm_mode

    @property
    def use_redcap_record_metadata(self):
        """Gets the use_redcap_record_metadata of this ExportOptions.  # noqa: E501


        :return: The use_redcap_record_metadata of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_redcap_record_metadata

    @use_redcap_record_metadata.setter
    def use_redcap_record_metadata(self, use_redcap_record_metadata):
        """Sets the use_redcap_record_metadata of this ExportOptions.


        :param use_redcap_record_metadata: The use_redcap_record_metadata of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._use_redcap_record_metadata = use_redcap_record_metadata

    @property
    def use_concept_value(self):
        """Gets the use_concept_value of this ExportOptions.  # noqa: E501


        :return: The use_concept_value of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_concept_value

    @use_concept_value.setter
    def use_concept_value(self, use_concept_value):
        """Sets the use_concept_value of this ExportOptions.


        :param use_concept_value: The use_concept_value of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._use_concept_value = use_concept_value

    @property
    def export_empty_values(self):
        """Gets the export_empty_values of this ExportOptions.  # noqa: E501


        :return: The export_empty_values of this ExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._export_empty_values

    @export_empty_values.setter
    def export_empty_values(self, export_empty_values):
        """Sets the export_empty_values of this ExportOptions.


        :param export_empty_values: The export_empty_values of this ExportOptions.  # noqa: E501
        :type: bool
        """

        self._export_empty_values = export_empty_values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExportOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExportOptions):
            return True

        return self.to_dict() != other.to_dict()