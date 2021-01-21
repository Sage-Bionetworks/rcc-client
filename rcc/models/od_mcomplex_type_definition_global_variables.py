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


class ODMcomplexTypeDefinitionGlobalVariables(object):
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
        'study_name': 'ODMcomplexTypeDefinitionStudyName',
        'study_description': 'ODMcomplexTypeDefinitionStudyDescription',
        'protocol_name': 'ODMcomplexTypeDefinitionProtocolName',
        'global_site': 'GlobalSite',
        'parent_global_sites': 'ParentGlobalSites',
        'secondary_ids': 'str',
        'summary': 'str',
        'principal_investigator': 'str',
        'expected_enrollment': 'int',
        'protocol_approval_date': 'datetime',
        'start_date': 'datetime',
        'completion_date': 'datetime',
        'interview_date_editable': 'bool',
        'interviewer_name_editable': 'bool',
        'enabled': 'bool',
        'my_health_enabled': 'bool'
    }

    attribute_map = {
        'study_name': 'studyName',
        'study_description': 'studyDescription',
        'protocol_name': 'protocolName',
        'global_site': 'globalSite',
        'parent_global_sites': 'parentGlobalSites',
        'secondary_ids': 'secondaryIds',
        'summary': 'summary',
        'principal_investigator': 'principalInvestigator',
        'expected_enrollment': 'expectedEnrollment',
        'protocol_approval_date': 'protocolApprovalDate',
        'start_date': 'startDate',
        'completion_date': 'completionDate',
        'interview_date_editable': 'interviewDateEditable',
        'interviewer_name_editable': 'interviewerNameEditable',
        'enabled': 'enabled',
        'my_health_enabled': 'myHealthEnabled'
    }

    def __init__(self, study_name=None, study_description=None, protocol_name=None, global_site=None, parent_global_sites=None, secondary_ids=None, summary=None, principal_investigator=None, expected_enrollment=None, protocol_approval_date=None, start_date=None, completion_date=None, interview_date_editable=None, interviewer_name_editable=None, enabled=None, my_health_enabled=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionGlobalVariables - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_name = None
        self._study_description = None
        self._protocol_name = None
        self._global_site = None
        self._parent_global_sites = None
        self._secondary_ids = None
        self._summary = None
        self._principal_investigator = None
        self._expected_enrollment = None
        self._protocol_approval_date = None
        self._start_date = None
        self._completion_date = None
        self._interview_date_editable = None
        self._interviewer_name_editable = None
        self._enabled = None
        self._my_health_enabled = None
        self.discriminator = None

        self.study_name = study_name
        self.study_description = study_description
        self.protocol_name = protocol_name
        self.global_site = global_site
        self.parent_global_sites = parent_global_sites
        if secondary_ids is not None:
            self.secondary_ids = secondary_ids
        if summary is not None:
            self.summary = summary
        if principal_investigator is not None:
            self.principal_investigator = principal_investigator
        if expected_enrollment is not None:
            self.expected_enrollment = expected_enrollment
        if protocol_approval_date is not None:
            self.protocol_approval_date = protocol_approval_date
        if start_date is not None:
            self.start_date = start_date
        if completion_date is not None:
            self.completion_date = completion_date
        if interview_date_editable is not None:
            self.interview_date_editable = interview_date_editable
        if interviewer_name_editable is not None:
            self.interviewer_name_editable = interviewer_name_editable
        if enabled is not None:
            self.enabled = enabled
        if my_health_enabled is not None:
            self.my_health_enabled = my_health_enabled

    @property
    def study_name(self):
        """Gets the study_name of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The study_name of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionStudyName
        """
        return self._study_name

    @study_name.setter
    def study_name(self, study_name):
        """Sets the study_name of this ODMcomplexTypeDefinitionGlobalVariables.


        :param study_name: The study_name of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: ODMcomplexTypeDefinitionStudyName
        """
        if self.local_vars_configuration.client_side_validation and study_name is None:  # noqa: E501
            raise ValueError("Invalid value for `study_name`, must not be `None`")  # noqa: E501

        self._study_name = study_name

    @property
    def study_description(self):
        """Gets the study_description of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The study_description of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionStudyDescription
        """
        return self._study_description

    @study_description.setter
    def study_description(self, study_description):
        """Sets the study_description of this ODMcomplexTypeDefinitionGlobalVariables.


        :param study_description: The study_description of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: ODMcomplexTypeDefinitionStudyDescription
        """
        if self.local_vars_configuration.client_side_validation and study_description is None:  # noqa: E501
            raise ValueError("Invalid value for `study_description`, must not be `None`")  # noqa: E501

        self._study_description = study_description

    @property
    def protocol_name(self):
        """Gets the protocol_name of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The protocol_name of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionProtocolName
        """
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, protocol_name):
        """Sets the protocol_name of this ODMcomplexTypeDefinitionGlobalVariables.


        :param protocol_name: The protocol_name of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: ODMcomplexTypeDefinitionProtocolName
        """
        if self.local_vars_configuration.client_side_validation and protocol_name is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol_name`, must not be `None`")  # noqa: E501

        self._protocol_name = protocol_name

    @property
    def global_site(self):
        """Gets the global_site of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The global_site of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: GlobalSite
        """
        return self._global_site

    @global_site.setter
    def global_site(self, global_site):
        """Sets the global_site of this ODMcomplexTypeDefinitionGlobalVariables.


        :param global_site: The global_site of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: GlobalSite
        """
        if self.local_vars_configuration.client_side_validation and global_site is None:  # noqa: E501
            raise ValueError("Invalid value for `global_site`, must not be `None`")  # noqa: E501

        self._global_site = global_site

    @property
    def parent_global_sites(self):
        """Gets the parent_global_sites of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The parent_global_sites of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: ParentGlobalSites
        """
        return self._parent_global_sites

    @parent_global_sites.setter
    def parent_global_sites(self, parent_global_sites):
        """Sets the parent_global_sites of this ODMcomplexTypeDefinitionGlobalVariables.


        :param parent_global_sites: The parent_global_sites of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: ParentGlobalSites
        """
        if self.local_vars_configuration.client_side_validation and parent_global_sites is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_global_sites`, must not be `None`")  # noqa: E501

        self._parent_global_sites = parent_global_sites

    @property
    def secondary_ids(self):
        """Gets the secondary_ids of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The secondary_ids of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: str
        """
        return self._secondary_ids

    @secondary_ids.setter
    def secondary_ids(self, secondary_ids):
        """Sets the secondary_ids of this ODMcomplexTypeDefinitionGlobalVariables.


        :param secondary_ids: The secondary_ids of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: str
        """

        self._secondary_ids = secondary_ids

    @property
    def summary(self):
        """Gets the summary of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The summary of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ODMcomplexTypeDefinitionGlobalVariables.


        :param summary: The summary of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def principal_investigator(self):
        """Gets the principal_investigator of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The principal_investigator of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: str
        """
        return self._principal_investigator

    @principal_investigator.setter
    def principal_investigator(self, principal_investigator):
        """Sets the principal_investigator of this ODMcomplexTypeDefinitionGlobalVariables.


        :param principal_investigator: The principal_investigator of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: str
        """

        self._principal_investigator = principal_investigator

    @property
    def expected_enrollment(self):
        """Gets the expected_enrollment of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The expected_enrollment of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: int
        """
        return self._expected_enrollment

    @expected_enrollment.setter
    def expected_enrollment(self, expected_enrollment):
        """Sets the expected_enrollment of this ODMcomplexTypeDefinitionGlobalVariables.


        :param expected_enrollment: The expected_enrollment of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: int
        """

        self._expected_enrollment = expected_enrollment

    @property
    def protocol_approval_date(self):
        """Gets the protocol_approval_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The protocol_approval_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: datetime
        """
        return self._protocol_approval_date

    @protocol_approval_date.setter
    def protocol_approval_date(self, protocol_approval_date):
        """Sets the protocol_approval_date of this ODMcomplexTypeDefinitionGlobalVariables.


        :param protocol_approval_date: The protocol_approval_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: datetime
        """

        self._protocol_approval_date = protocol_approval_date

    @property
    def start_date(self):
        """Gets the start_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The start_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ODMcomplexTypeDefinitionGlobalVariables.


        :param start_date: The start_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def completion_date(self):
        """Gets the completion_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The completion_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this ODMcomplexTypeDefinitionGlobalVariables.


        :param completion_date: The completion_date of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: datetime
        """

        self._completion_date = completion_date

    @property
    def interview_date_editable(self):
        """Gets the interview_date_editable of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The interview_date_editable of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: bool
        """
        return self._interview_date_editable

    @interview_date_editable.setter
    def interview_date_editable(self, interview_date_editable):
        """Sets the interview_date_editable of this ODMcomplexTypeDefinitionGlobalVariables.


        :param interview_date_editable: The interview_date_editable of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: bool
        """

        self._interview_date_editable = interview_date_editable

    @property
    def interviewer_name_editable(self):
        """Gets the interviewer_name_editable of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The interviewer_name_editable of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: bool
        """
        return self._interviewer_name_editable

    @interviewer_name_editable.setter
    def interviewer_name_editable(self, interviewer_name_editable):
        """Sets the interviewer_name_editable of this ODMcomplexTypeDefinitionGlobalVariables.


        :param interviewer_name_editable: The interviewer_name_editable of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: bool
        """

        self._interviewer_name_editable = interviewer_name_editable

    @property
    def enabled(self):
        """Gets the enabled of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The enabled of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ODMcomplexTypeDefinitionGlobalVariables.


        :param enabled: The enabled of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def my_health_enabled(self):
        """Gets the my_health_enabled of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501


        :return: The my_health_enabled of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :rtype: bool
        """
        return self._my_health_enabled

    @my_health_enabled.setter
    def my_health_enabled(self, my_health_enabled):
        """Sets the my_health_enabled of this ODMcomplexTypeDefinitionGlobalVariables.


        :param my_health_enabled: The my_health_enabled of this ODMcomplexTypeDefinitionGlobalVariables.  # noqa: E501
        :type: bool
        """

        self._my_health_enabled = my_health_enabled

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
        if not isinstance(other, ODMcomplexTypeDefinitionGlobalVariables):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionGlobalVariables):
            return True

        return self.to_dict() != other.to_dict()