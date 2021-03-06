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


class ODMcomplexTypeDefinitionClinicalData(object):
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
        'subject_data': 'list[ODMcomplexTypeDefinitionSubjectData]',
        'audit_records': 'list[ODMcomplexTypeDefinitionAuditRecords]',
        'signatures': 'list[ODMcomplexTypeDefinitionSignatures]',
        'annotations': 'list[ODMcomplexTypeDefinitionAnnotations]',
        'study_oid': 'str',
        'meta_data_version_oid': 'str'
    }

    attribute_map = {
        'subject_data': 'subjectData',
        'audit_records': 'auditRecords',
        'signatures': 'signatures',
        'annotations': 'annotations',
        'study_oid': 'studyOID',
        'meta_data_version_oid': 'metaDataVersionOID'
    }

    def __init__(self, subject_data=None, audit_records=None, signatures=None, annotations=None, study_oid=None, meta_data_version_oid=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionClinicalData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subject_data = None
        self._audit_records = None
        self._signatures = None
        self._annotations = None
        self._study_oid = None
        self._meta_data_version_oid = None
        self.discriminator = None

        if subject_data is not None:
            self.subject_data = subject_data
        if audit_records is not None:
            self.audit_records = audit_records
        if signatures is not None:
            self.signatures = signatures
        if annotations is not None:
            self.annotations = annotations
        if study_oid is not None:
            self.study_oid = study_oid
        if meta_data_version_oid is not None:
            self.meta_data_version_oid = meta_data_version_oid

    @property
    def subject_data(self):
        """Gets the subject_data of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501


        :return: The subject_data of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionSubjectData]
        """
        return self._subject_data

    @subject_data.setter
    def subject_data(self, subject_data):
        """Sets the subject_data of this ODMcomplexTypeDefinitionClinicalData.


        :param subject_data: The subject_data of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionSubjectData]
        """

        self._subject_data = subject_data

    @property
    def audit_records(self):
        """Gets the audit_records of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501


        :return: The audit_records of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAuditRecords]
        """
        return self._audit_records

    @audit_records.setter
    def audit_records(self, audit_records):
        """Sets the audit_records of this ODMcomplexTypeDefinitionClinicalData.


        :param audit_records: The audit_records of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAuditRecords]
        """

        self._audit_records = audit_records

    @property
    def signatures(self):
        """Gets the signatures of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501


        :return: The signatures of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionSignatures]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this ODMcomplexTypeDefinitionClinicalData.


        :param signatures: The signatures of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionSignatures]
        """

        self._signatures = signatures

    @property
    def annotations(self):
        """Gets the annotations of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501


        :return: The annotations of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAnnotations]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ODMcomplexTypeDefinitionClinicalData.


        :param annotations: The annotations of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAnnotations]
        """

        self._annotations = annotations

    @property
    def study_oid(self):
        """Gets the study_oid of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501


        :return: The study_oid of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :rtype: str
        """
        return self._study_oid

    @study_oid.setter
    def study_oid(self, study_oid):
        """Sets the study_oid of this ODMcomplexTypeDefinitionClinicalData.


        :param study_oid: The study_oid of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :type: str
        """

        self._study_oid = study_oid

    @property
    def meta_data_version_oid(self):
        """Gets the meta_data_version_oid of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501


        :return: The meta_data_version_oid of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :rtype: str
        """
        return self._meta_data_version_oid

    @meta_data_version_oid.setter
    def meta_data_version_oid(self, meta_data_version_oid):
        """Sets the meta_data_version_oid of this ODMcomplexTypeDefinitionClinicalData.


        :param meta_data_version_oid: The meta_data_version_oid of this ODMcomplexTypeDefinitionClinicalData.  # noqa: E501
        :type: str
        """

        self._meta_data_version_oid = meta_data_version_oid

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
        if not isinstance(other, ODMcomplexTypeDefinitionClinicalData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionClinicalData):
            return True

        return self.to_dict() != other.to_dict()
