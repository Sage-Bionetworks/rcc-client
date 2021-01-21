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


class CRFFormVersionDefinition(object):
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
        'version_name': 'str',
        'revision_notes': 'str',
        'version_oid': 'str',
        'fields': 'int',
        'revision_date': 'datetime',
        'primary_flag': 'bool',
        'disp_sequence': 'int',
        'enabled': 'bool',
        'screening_expression': 'str',
        'screening_flag': 'bool',
        'custom_enroll_flag': 'bool',
        'used_at_enroll': 'bool',
        'randomization_expression': 'str',
        'irb_approval_date': 'datetime',
        'valid_from': 'datetime',
        'valid_to': 'datetime',
        'screening_e_consent_flag': 'bool',
        'econsent': 'bool',
        'crfform_definition': 'CRFFormDefinition',
        'crfform_section': 'list[CRFFormSectionDefinition]'
    }

    attribute_map = {
        'version_name': 'versionName',
        'revision_notes': 'revisionNotes',
        'version_oid': 'versionOID',
        'fields': 'fields',
        'revision_date': 'revisionDate',
        'primary_flag': 'primaryFlag',
        'disp_sequence': 'dispSequence',
        'enabled': 'enabled',
        'screening_expression': 'screeningExpression',
        'screening_flag': 'screeningFlag',
        'custom_enroll_flag': 'customEnrollFlag',
        'used_at_enroll': 'usedAtEnroll',
        'randomization_expression': 'randomizationExpression',
        'irb_approval_date': 'irbApprovalDate',
        'valid_from': 'validFrom',
        'valid_to': 'validTo',
        'screening_e_consent_flag': 'screeningEConsentFlag',
        'econsent': 'econsent',
        'crfform_definition': 'crfformDefinition',
        'crfform_section': 'crfformSection'
    }

    def __init__(self, version_name=None, revision_notes=None, version_oid=None, fields=None, revision_date=None, primary_flag=None, disp_sequence=None, enabled=None, screening_expression=None, screening_flag=None, custom_enroll_flag=None, used_at_enroll=None, randomization_expression=None, irb_approval_date=None, valid_from=None, valid_to=None, screening_e_consent_flag=None, econsent=None, crfform_definition=None, crfform_section=None, local_vars_configuration=None):  # noqa: E501
        """CRFFormVersionDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version_name = None
        self._revision_notes = None
        self._version_oid = None
        self._fields = None
        self._revision_date = None
        self._primary_flag = None
        self._disp_sequence = None
        self._enabled = None
        self._screening_expression = None
        self._screening_flag = None
        self._custom_enroll_flag = None
        self._used_at_enroll = None
        self._randomization_expression = None
        self._irb_approval_date = None
        self._valid_from = None
        self._valid_to = None
        self._screening_e_consent_flag = None
        self._econsent = None
        self._crfform_definition = None
        self._crfform_section = None
        self.discriminator = None

        if version_name is not None:
            self.version_name = version_name
        if revision_notes is not None:
            self.revision_notes = revision_notes
        if version_oid is not None:
            self.version_oid = version_oid
        if fields is not None:
            self.fields = fields
        if revision_date is not None:
            self.revision_date = revision_date
        if primary_flag is not None:
            self.primary_flag = primary_flag
        if disp_sequence is not None:
            self.disp_sequence = disp_sequence
        if enabled is not None:
            self.enabled = enabled
        if screening_expression is not None:
            self.screening_expression = screening_expression
        if screening_flag is not None:
            self.screening_flag = screening_flag
        if custom_enroll_flag is not None:
            self.custom_enroll_flag = custom_enroll_flag
        if used_at_enroll is not None:
            self.used_at_enroll = used_at_enroll
        if randomization_expression is not None:
            self.randomization_expression = randomization_expression
        if irb_approval_date is not None:
            self.irb_approval_date = irb_approval_date
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to
        if screening_e_consent_flag is not None:
            self.screening_e_consent_flag = screening_e_consent_flag
        if econsent is not None:
            self.econsent = econsent
        if crfform_definition is not None:
            self.crfform_definition = crfform_definition
        if crfform_section is not None:
            self.crfform_section = crfform_section

    @property
    def version_name(self):
        """Gets the version_name of this CRFFormVersionDefinition.  # noqa: E501


        :return: The version_name of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this CRFFormVersionDefinition.


        :param version_name: The version_name of this CRFFormVersionDefinition.  # noqa: E501
        :type: str
        """

        self._version_name = version_name

    @property
    def revision_notes(self):
        """Gets the revision_notes of this CRFFormVersionDefinition.  # noqa: E501


        :return: The revision_notes of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._revision_notes

    @revision_notes.setter
    def revision_notes(self, revision_notes):
        """Sets the revision_notes of this CRFFormVersionDefinition.


        :param revision_notes: The revision_notes of this CRFFormVersionDefinition.  # noqa: E501
        :type: str
        """

        self._revision_notes = revision_notes

    @property
    def version_oid(self):
        """Gets the version_oid of this CRFFormVersionDefinition.  # noqa: E501


        :return: The version_oid of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._version_oid

    @version_oid.setter
    def version_oid(self, version_oid):
        """Sets the version_oid of this CRFFormVersionDefinition.


        :param version_oid: The version_oid of this CRFFormVersionDefinition.  # noqa: E501
        :type: str
        """

        self._version_oid = version_oid

    @property
    def fields(self):
        """Gets the fields of this CRFFormVersionDefinition.  # noqa: E501


        :return: The fields of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CRFFormVersionDefinition.


        :param fields: The fields of this CRFFormVersionDefinition.  # noqa: E501
        :type: int
        """

        self._fields = fields

    @property
    def revision_date(self):
        """Gets the revision_date of this CRFFormVersionDefinition.  # noqa: E501


        :return: The revision_date of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._revision_date

    @revision_date.setter
    def revision_date(self, revision_date):
        """Sets the revision_date of this CRFFormVersionDefinition.


        :param revision_date: The revision_date of this CRFFormVersionDefinition.  # noqa: E501
        :type: datetime
        """

        self._revision_date = revision_date

    @property
    def primary_flag(self):
        """Gets the primary_flag of this CRFFormVersionDefinition.  # noqa: E501


        :return: The primary_flag of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._primary_flag

    @primary_flag.setter
    def primary_flag(self, primary_flag):
        """Sets the primary_flag of this CRFFormVersionDefinition.


        :param primary_flag: The primary_flag of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._primary_flag = primary_flag

    @property
    def disp_sequence(self):
        """Gets the disp_sequence of this CRFFormVersionDefinition.  # noqa: E501


        :return: The disp_sequence of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._disp_sequence

    @disp_sequence.setter
    def disp_sequence(self, disp_sequence):
        """Sets the disp_sequence of this CRFFormVersionDefinition.


        :param disp_sequence: The disp_sequence of this CRFFormVersionDefinition.  # noqa: E501
        :type: int
        """

        self._disp_sequence = disp_sequence

    @property
    def enabled(self):
        """Gets the enabled of this CRFFormVersionDefinition.  # noqa: E501


        :return: The enabled of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CRFFormVersionDefinition.


        :param enabled: The enabled of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def screening_expression(self):
        """Gets the screening_expression of this CRFFormVersionDefinition.  # noqa: E501


        :return: The screening_expression of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._screening_expression

    @screening_expression.setter
    def screening_expression(self, screening_expression):
        """Sets the screening_expression of this CRFFormVersionDefinition.


        :param screening_expression: The screening_expression of this CRFFormVersionDefinition.  # noqa: E501
        :type: str
        """

        self._screening_expression = screening_expression

    @property
    def screening_flag(self):
        """Gets the screening_flag of this CRFFormVersionDefinition.  # noqa: E501


        :return: The screening_flag of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._screening_flag

    @screening_flag.setter
    def screening_flag(self, screening_flag):
        """Sets the screening_flag of this CRFFormVersionDefinition.


        :param screening_flag: The screening_flag of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._screening_flag = screening_flag

    @property
    def custom_enroll_flag(self):
        """Gets the custom_enroll_flag of this CRFFormVersionDefinition.  # noqa: E501


        :return: The custom_enroll_flag of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._custom_enroll_flag

    @custom_enroll_flag.setter
    def custom_enroll_flag(self, custom_enroll_flag):
        """Sets the custom_enroll_flag of this CRFFormVersionDefinition.


        :param custom_enroll_flag: The custom_enroll_flag of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._custom_enroll_flag = custom_enroll_flag

    @property
    def used_at_enroll(self):
        """Gets the used_at_enroll of this CRFFormVersionDefinition.  # noqa: E501


        :return: The used_at_enroll of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._used_at_enroll

    @used_at_enroll.setter
    def used_at_enroll(self, used_at_enroll):
        """Sets the used_at_enroll of this CRFFormVersionDefinition.


        :param used_at_enroll: The used_at_enroll of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._used_at_enroll = used_at_enroll

    @property
    def randomization_expression(self):
        """Gets the randomization_expression of this CRFFormVersionDefinition.  # noqa: E501


        :return: The randomization_expression of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._randomization_expression

    @randomization_expression.setter
    def randomization_expression(self, randomization_expression):
        """Sets the randomization_expression of this CRFFormVersionDefinition.


        :param randomization_expression: The randomization_expression of this CRFFormVersionDefinition.  # noqa: E501
        :type: str
        """

        self._randomization_expression = randomization_expression

    @property
    def irb_approval_date(self):
        """Gets the irb_approval_date of this CRFFormVersionDefinition.  # noqa: E501


        :return: The irb_approval_date of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._irb_approval_date

    @irb_approval_date.setter
    def irb_approval_date(self, irb_approval_date):
        """Sets the irb_approval_date of this CRFFormVersionDefinition.


        :param irb_approval_date: The irb_approval_date of this CRFFormVersionDefinition.  # noqa: E501
        :type: datetime
        """

        self._irb_approval_date = irb_approval_date

    @property
    def valid_from(self):
        """Gets the valid_from of this CRFFormVersionDefinition.  # noqa: E501


        :return: The valid_from of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this CRFFormVersionDefinition.


        :param valid_from: The valid_from of this CRFFormVersionDefinition.  # noqa: E501
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this CRFFormVersionDefinition.  # noqa: E501


        :return: The valid_to of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: datetime
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this CRFFormVersionDefinition.


        :param valid_to: The valid_to of this CRFFormVersionDefinition.  # noqa: E501
        :type: datetime
        """

        self._valid_to = valid_to

    @property
    def screening_e_consent_flag(self):
        """Gets the screening_e_consent_flag of this CRFFormVersionDefinition.  # noqa: E501


        :return: The screening_e_consent_flag of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._screening_e_consent_flag

    @screening_e_consent_flag.setter
    def screening_e_consent_flag(self, screening_e_consent_flag):
        """Sets the screening_e_consent_flag of this CRFFormVersionDefinition.


        :param screening_e_consent_flag: The screening_e_consent_flag of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._screening_e_consent_flag = screening_e_consent_flag

    @property
    def econsent(self):
        """Gets the econsent of this CRFFormVersionDefinition.  # noqa: E501


        :return: The econsent of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._econsent

    @econsent.setter
    def econsent(self, econsent):
        """Sets the econsent of this CRFFormVersionDefinition.


        :param econsent: The econsent of this CRFFormVersionDefinition.  # noqa: E501
        :type: bool
        """

        self._econsent = econsent

    @property
    def crfform_definition(self):
        """Gets the crfform_definition of this CRFFormVersionDefinition.  # noqa: E501


        :return: The crfform_definition of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: CRFFormDefinition
        """
        return self._crfform_definition

    @crfform_definition.setter
    def crfform_definition(self, crfform_definition):
        """Sets the crfform_definition of this CRFFormVersionDefinition.


        :param crfform_definition: The crfform_definition of this CRFFormVersionDefinition.  # noqa: E501
        :type: CRFFormDefinition
        """

        self._crfform_definition = crfform_definition

    @property
    def crfform_section(self):
        """Gets the crfform_section of this CRFFormVersionDefinition.  # noqa: E501


        :return: The crfform_section of this CRFFormVersionDefinition.  # noqa: E501
        :rtype: list[CRFFormSectionDefinition]
        """
        return self._crfform_section

    @crfform_section.setter
    def crfform_section(self, crfform_section):
        """Sets the crfform_section of this CRFFormVersionDefinition.


        :param crfform_section: The crfform_section of this CRFFormVersionDefinition.  # noqa: E501
        :type: list[CRFFormSectionDefinition]
        """

        self._crfform_section = crfform_section

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
        if not isinstance(other, CRFFormVersionDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CRFFormVersionDefinition):
            return True

        return self.to_dict() != other.to_dict()
