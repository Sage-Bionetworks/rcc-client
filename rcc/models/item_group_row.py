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


class ItemGroupRow(object):
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
        'label': 'str',
        'display_sequence': 'int'
    }

    attribute_map = {
        'label': 'label',
        'display_sequence': 'displaySequence'
    }

    def __init__(self, label=None, display_sequence=None, local_vars_configuration=None):  # noqa: E501
        """ItemGroupRow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._display_sequence = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if display_sequence is not None:
            self.display_sequence = display_sequence

    @property
    def label(self):
        """Gets the label of this ItemGroupRow.  # noqa: E501


        :return: The label of this ItemGroupRow.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ItemGroupRow.


        :param label: The label of this ItemGroupRow.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def display_sequence(self):
        """Gets the display_sequence of this ItemGroupRow.  # noqa: E501


        :return: The display_sequence of this ItemGroupRow.  # noqa: E501
        :rtype: int
        """
        return self._display_sequence

    @display_sequence.setter
    def display_sequence(self, display_sequence):
        """Sets the display_sequence of this ItemGroupRow.


        :param display_sequence: The display_sequence of this ItemGroupRow.  # noqa: E501
        :type: int
        """

        self._display_sequence = display_sequence

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
        if not isinstance(other, ItemGroupRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemGroupRow):
            return True

        return self.to_dict() != other.to_dict()
