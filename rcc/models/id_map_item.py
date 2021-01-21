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


class IdMapItem(object):
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
        'source_id': 'int',
        'target_id': 'int',
        'description': 'str'
    }

    attribute_map = {
        'source_id': 'sourceId',
        'target_id': 'targetId',
        'description': 'description'
    }

    def __init__(self, source_id=None, target_id=None, description=None, local_vars_configuration=None):  # noqa: E501
        """IdMapItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_id = None
        self._target_id = None
        self._description = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if target_id is not None:
            self.target_id = target_id
        if description is not None:
            self.description = description

    @property
    def source_id(self):
        """Gets the source_id of this IdMapItem.  # noqa: E501


        :return: The source_id of this IdMapItem.  # noqa: E501
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this IdMapItem.


        :param source_id: The source_id of this IdMapItem.  # noqa: E501
        :type: int
        """

        self._source_id = source_id

    @property
    def target_id(self):
        """Gets the target_id of this IdMapItem.  # noqa: E501


        :return: The target_id of this IdMapItem.  # noqa: E501
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this IdMapItem.


        :param target_id: The target_id of this IdMapItem.  # noqa: E501
        :type: int
        """

        self._target_id = target_id

    @property
    def description(self):
        """Gets the description of this IdMapItem.  # noqa: E501


        :return: The description of this IdMapItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdMapItem.


        :param description: The description of this IdMapItem.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, IdMapItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdMapItem):
            return True

        return self.to_dict() != other.to_dict()
