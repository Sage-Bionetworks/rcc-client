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


class SurveyQueue(object):
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
        'study_event_definition_oid': 'str',
        'active': 'int',
        'auto_start': 'int',
        'condition_surveycomplete_survey_oid': 'str',
        'condition_surveycomplete_event_oid': 'str',
        'condition_andor_code': 'str',
        'condition_logic': 'str'
    }

    attribute_map = {
        'study_event_definition_oid': 'studyEventDefinitionOID',
        'active': 'active',
        'auto_start': 'autoStart',
        'condition_surveycomplete_survey_oid': 'conditionSurveycompleteSurveyOID',
        'condition_surveycomplete_event_oid': 'conditionSurveycompleteEventOID',
        'condition_andor_code': 'conditionAndorCode',
        'condition_logic': 'conditionLogic'
    }

    def __init__(self, study_event_definition_oid=None, active=None, auto_start=None, condition_surveycomplete_survey_oid=None, condition_surveycomplete_event_oid=None, condition_andor_code=None, condition_logic=None, local_vars_configuration=None):  # noqa: E501
        """SurveyQueue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_event_definition_oid = None
        self._active = None
        self._auto_start = None
        self._condition_surveycomplete_survey_oid = None
        self._condition_surveycomplete_event_oid = None
        self._condition_andor_code = None
        self._condition_logic = None
        self.discriminator = None

        if study_event_definition_oid is not None:
            self.study_event_definition_oid = study_event_definition_oid
        if active is not None:
            self.active = active
        if auto_start is not None:
            self.auto_start = auto_start
        if condition_surveycomplete_survey_oid is not None:
            self.condition_surveycomplete_survey_oid = condition_surveycomplete_survey_oid
        if condition_surveycomplete_event_oid is not None:
            self.condition_surveycomplete_event_oid = condition_surveycomplete_event_oid
        if condition_andor_code is not None:
            self.condition_andor_code = condition_andor_code
        if condition_logic is not None:
            self.condition_logic = condition_logic

    @property
    def study_event_definition_oid(self):
        """Gets the study_event_definition_oid of this SurveyQueue.  # noqa: E501


        :return: The study_event_definition_oid of this SurveyQueue.  # noqa: E501
        :rtype: str
        """
        return self._study_event_definition_oid

    @study_event_definition_oid.setter
    def study_event_definition_oid(self, study_event_definition_oid):
        """Sets the study_event_definition_oid of this SurveyQueue.


        :param study_event_definition_oid: The study_event_definition_oid of this SurveyQueue.  # noqa: E501
        :type: str
        """

        self._study_event_definition_oid = study_event_definition_oid

    @property
    def active(self):
        """Gets the active of this SurveyQueue.  # noqa: E501


        :return: The active of this SurveyQueue.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SurveyQueue.


        :param active: The active of this SurveyQueue.  # noqa: E501
        :type: int
        """

        self._active = active

    @property
    def auto_start(self):
        """Gets the auto_start of this SurveyQueue.  # noqa: E501


        :return: The auto_start of this SurveyQueue.  # noqa: E501
        :rtype: int
        """
        return self._auto_start

    @auto_start.setter
    def auto_start(self, auto_start):
        """Sets the auto_start of this SurveyQueue.


        :param auto_start: The auto_start of this SurveyQueue.  # noqa: E501
        :type: int
        """

        self._auto_start = auto_start

    @property
    def condition_surveycomplete_survey_oid(self):
        """Gets the condition_surveycomplete_survey_oid of this SurveyQueue.  # noqa: E501


        :return: The condition_surveycomplete_survey_oid of this SurveyQueue.  # noqa: E501
        :rtype: str
        """
        return self._condition_surveycomplete_survey_oid

    @condition_surveycomplete_survey_oid.setter
    def condition_surveycomplete_survey_oid(self, condition_surveycomplete_survey_oid):
        """Sets the condition_surveycomplete_survey_oid of this SurveyQueue.


        :param condition_surveycomplete_survey_oid: The condition_surveycomplete_survey_oid of this SurveyQueue.  # noqa: E501
        :type: str
        """

        self._condition_surveycomplete_survey_oid = condition_surveycomplete_survey_oid

    @property
    def condition_surveycomplete_event_oid(self):
        """Gets the condition_surveycomplete_event_oid of this SurveyQueue.  # noqa: E501


        :return: The condition_surveycomplete_event_oid of this SurveyQueue.  # noqa: E501
        :rtype: str
        """
        return self._condition_surveycomplete_event_oid

    @condition_surveycomplete_event_oid.setter
    def condition_surveycomplete_event_oid(self, condition_surveycomplete_event_oid):
        """Sets the condition_surveycomplete_event_oid of this SurveyQueue.


        :param condition_surveycomplete_event_oid: The condition_surveycomplete_event_oid of this SurveyQueue.  # noqa: E501
        :type: str
        """

        self._condition_surveycomplete_event_oid = condition_surveycomplete_event_oid

    @property
    def condition_andor_code(self):
        """Gets the condition_andor_code of this SurveyQueue.  # noqa: E501


        :return: The condition_andor_code of this SurveyQueue.  # noqa: E501
        :rtype: str
        """
        return self._condition_andor_code

    @condition_andor_code.setter
    def condition_andor_code(self, condition_andor_code):
        """Sets the condition_andor_code of this SurveyQueue.


        :param condition_andor_code: The condition_andor_code of this SurveyQueue.  # noqa: E501
        :type: str
        """

        self._condition_andor_code = condition_andor_code

    @property
    def condition_logic(self):
        """Gets the condition_logic of this SurveyQueue.  # noqa: E501


        :return: The condition_logic of this SurveyQueue.  # noqa: E501
        :rtype: str
        """
        return self._condition_logic

    @condition_logic.setter
    def condition_logic(self, condition_logic):
        """Sets the condition_logic of this SurveyQueue.


        :param condition_logic: The condition_logic of this SurveyQueue.  # noqa: E501
        :type: str
        """

        self._condition_logic = condition_logic

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
        if not isinstance(other, SurveyQueue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SurveyQueue):
            return True

        return self.to_dict() != other.to_dict()
