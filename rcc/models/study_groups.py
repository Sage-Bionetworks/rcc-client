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


class StudyGroups(object):
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
        'study_group': 'list[StudyGroup]'
    }

    attribute_map = {
        'study_group': 'studyGroup'
    }

    def __init__(self, study_group=None, local_vars_configuration=None):  # noqa: E501
        """StudyGroups - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_group = None
        self.discriminator = None

        if study_group is not None:
            self.study_group = study_group

    @property
    def study_group(self):
        """Gets the study_group of this StudyGroups.  # noqa: E501


        :return: The study_group of this StudyGroups.  # noqa: E501
        :rtype: list[StudyGroup]
        """
        return self._study_group

    @study_group.setter
    def study_group(self, study_group):
        """Sets the study_group of this StudyGroups.


        :param study_group: The study_group of this StudyGroups.  # noqa: E501
        :type: list[StudyGroup]
        """

        self._study_group = study_group

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
        if not isinstance(other, StudyGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyGroups):
            return True

        return self.to_dict() != other.to_dict()
