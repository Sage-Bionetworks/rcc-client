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


class Randomization(object):
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
        'randomization_config': 'list[RandomizationConfig]',
        'study_group_randomization': 'list[StudyGroupRandomization]',
        'custom_schedule_randomization': 'list[CustomScheduleRandomization]',
        'custom_schedule_randomization_mapping': 'list[CustomScheduleRandomizationMapping]',
        'custom_schedule_randomization_values': 'list[CustomScheduleRandomizationValues]'
    }

    attribute_map = {
        'randomization_config': 'randomizationConfig',
        'study_group_randomization': 'studyGroupRandomization',
        'custom_schedule_randomization': 'customScheduleRandomization',
        'custom_schedule_randomization_mapping': 'customScheduleRandomizationMapping',
        'custom_schedule_randomization_values': 'customScheduleRandomizationValues'
    }

    def __init__(self, randomization_config=None, study_group_randomization=None, custom_schedule_randomization=None, custom_schedule_randomization_mapping=None, custom_schedule_randomization_values=None, local_vars_configuration=None):  # noqa: E501
        """Randomization - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._randomization_config = None
        self._study_group_randomization = None
        self._custom_schedule_randomization = None
        self._custom_schedule_randomization_mapping = None
        self._custom_schedule_randomization_values = None
        self.discriminator = None

        if randomization_config is not None:
            self.randomization_config = randomization_config
        if study_group_randomization is not None:
            self.study_group_randomization = study_group_randomization
        if custom_schedule_randomization is not None:
            self.custom_schedule_randomization = custom_schedule_randomization
        if custom_schedule_randomization_mapping is not None:
            self.custom_schedule_randomization_mapping = custom_schedule_randomization_mapping
        if custom_schedule_randomization_values is not None:
            self.custom_schedule_randomization_values = custom_schedule_randomization_values

    @property
    def randomization_config(self):
        """Gets the randomization_config of this Randomization.  # noqa: E501


        :return: The randomization_config of this Randomization.  # noqa: E501
        :rtype: list[RandomizationConfig]
        """
        return self._randomization_config

    @randomization_config.setter
    def randomization_config(self, randomization_config):
        """Sets the randomization_config of this Randomization.


        :param randomization_config: The randomization_config of this Randomization.  # noqa: E501
        :type: list[RandomizationConfig]
        """

        self._randomization_config = randomization_config

    @property
    def study_group_randomization(self):
        """Gets the study_group_randomization of this Randomization.  # noqa: E501


        :return: The study_group_randomization of this Randomization.  # noqa: E501
        :rtype: list[StudyGroupRandomization]
        """
        return self._study_group_randomization

    @study_group_randomization.setter
    def study_group_randomization(self, study_group_randomization):
        """Sets the study_group_randomization of this Randomization.


        :param study_group_randomization: The study_group_randomization of this Randomization.  # noqa: E501
        :type: list[StudyGroupRandomization]
        """

        self._study_group_randomization = study_group_randomization

    @property
    def custom_schedule_randomization(self):
        """Gets the custom_schedule_randomization of this Randomization.  # noqa: E501


        :return: The custom_schedule_randomization of this Randomization.  # noqa: E501
        :rtype: list[CustomScheduleRandomization]
        """
        return self._custom_schedule_randomization

    @custom_schedule_randomization.setter
    def custom_schedule_randomization(self, custom_schedule_randomization):
        """Sets the custom_schedule_randomization of this Randomization.


        :param custom_schedule_randomization: The custom_schedule_randomization of this Randomization.  # noqa: E501
        :type: list[CustomScheduleRandomization]
        """

        self._custom_schedule_randomization = custom_schedule_randomization

    @property
    def custom_schedule_randomization_mapping(self):
        """Gets the custom_schedule_randomization_mapping of this Randomization.  # noqa: E501


        :return: The custom_schedule_randomization_mapping of this Randomization.  # noqa: E501
        :rtype: list[CustomScheduleRandomizationMapping]
        """
        return self._custom_schedule_randomization_mapping

    @custom_schedule_randomization_mapping.setter
    def custom_schedule_randomization_mapping(self, custom_schedule_randomization_mapping):
        """Sets the custom_schedule_randomization_mapping of this Randomization.


        :param custom_schedule_randomization_mapping: The custom_schedule_randomization_mapping of this Randomization.  # noqa: E501
        :type: list[CustomScheduleRandomizationMapping]
        """

        self._custom_schedule_randomization_mapping = custom_schedule_randomization_mapping

    @property
    def custom_schedule_randomization_values(self):
        """Gets the custom_schedule_randomization_values of this Randomization.  # noqa: E501


        :return: The custom_schedule_randomization_values of this Randomization.  # noqa: E501
        :rtype: list[CustomScheduleRandomizationValues]
        """
        return self._custom_schedule_randomization_values

    @custom_schedule_randomization_values.setter
    def custom_schedule_randomization_values(self, custom_schedule_randomization_values):
        """Sets the custom_schedule_randomization_values of this Randomization.


        :param custom_schedule_randomization_values: The custom_schedule_randomization_values of this Randomization.  # noqa: E501
        :type: list[CustomScheduleRandomizationValues]
        """

        self._custom_schedule_randomization_values = custom_schedule_randomization_values

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
        if not isinstance(other, Randomization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Randomization):
            return True

        return self.to_dict() != other.to_dict()