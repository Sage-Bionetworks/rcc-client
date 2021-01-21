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


class StudyGroup(object):
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
        'study_group_value': 'list[StudyGroupValue]',
        'study_group_event': 'list[StudyGroupEvent]',
        'name': 'str',
        'group_type': 'str',
        'planned_size': 'int'
    }

    attribute_map = {
        'study_group_value': 'studyGroupValue',
        'study_group_event': 'studyGroupEvent',
        'name': 'name',
        'group_type': 'groupType',
        'planned_size': 'plannedSize'
    }

    def __init__(self, study_group_value=None, study_group_event=None, name=None, group_type=None, planned_size=None, local_vars_configuration=None):  # noqa: E501
        """StudyGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_group_value = None
        self._study_group_event = None
        self._name = None
        self._group_type = None
        self._planned_size = None
        self.discriminator = None

        if study_group_value is not None:
            self.study_group_value = study_group_value
        if study_group_event is not None:
            self.study_group_event = study_group_event
        if name is not None:
            self.name = name
        if group_type is not None:
            self.group_type = group_type
        if planned_size is not None:
            self.planned_size = planned_size

    @property
    def study_group_value(self):
        """Gets the study_group_value of this StudyGroup.  # noqa: E501


        :return: The study_group_value of this StudyGroup.  # noqa: E501
        :rtype: list[StudyGroupValue]
        """
        return self._study_group_value

    @study_group_value.setter
    def study_group_value(self, study_group_value):
        """Sets the study_group_value of this StudyGroup.


        :param study_group_value: The study_group_value of this StudyGroup.  # noqa: E501
        :type: list[StudyGroupValue]
        """

        self._study_group_value = study_group_value

    @property
    def study_group_event(self):
        """Gets the study_group_event of this StudyGroup.  # noqa: E501


        :return: The study_group_event of this StudyGroup.  # noqa: E501
        :rtype: list[StudyGroupEvent]
        """
        return self._study_group_event

    @study_group_event.setter
    def study_group_event(self, study_group_event):
        """Sets the study_group_event of this StudyGroup.


        :param study_group_event: The study_group_event of this StudyGroup.  # noqa: E501
        :type: list[StudyGroupEvent]
        """

        self._study_group_event = study_group_event

    @property
    def name(self):
        """Gets the name of this StudyGroup.  # noqa: E501


        :return: The name of this StudyGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyGroup.


        :param name: The name of this StudyGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group_type(self):
        """Gets the group_type of this StudyGroup.  # noqa: E501


        :return: The group_type of this StudyGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this StudyGroup.


        :param group_type: The group_type of this StudyGroup.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def planned_size(self):
        """Gets the planned_size of this StudyGroup.  # noqa: E501


        :return: The planned_size of this StudyGroup.  # noqa: E501
        :rtype: int
        """
        return self._planned_size

    @planned_size.setter
    def planned_size(self, planned_size):
        """Sets the planned_size of this StudyGroup.


        :param planned_size: The planned_size of this StudyGroup.  # noqa: E501
        :type: int
        """

        self._planned_size = planned_size

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
        if not isinstance(other, StudyGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyGroup):
            return True

        return self.to_dict() != other.to_dict()