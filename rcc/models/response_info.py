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


class ResponseInfo(object):
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
        'field_name': 'str',
        'field_value': 'object',
        'value_index': 'int',
        'message': 'str'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'field_value': 'fieldValue',
        'value_index': 'valueIndex',
        'message': 'message'
    }

    def __init__(self, field_name=None, field_value=None, value_index=None, message=None, local_vars_configuration=None):  # noqa: E501
        """ResponseInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_name = None
        self._field_value = None
        self._value_index = None
        self._message = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if field_value is not None:
            self.field_value = field_value
        if value_index is not None:
            self.value_index = value_index
        if message is not None:
            self.message = message

    @property
    def field_name(self):
        """Gets the field_name of this ResponseInfo.  # noqa: E501


        :return: The field_name of this ResponseInfo.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ResponseInfo.


        :param field_name: The field_name of this ResponseInfo.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def field_value(self):
        """Gets the field_value of this ResponseInfo.  # noqa: E501


        :return: The field_value of this ResponseInfo.  # noqa: E501
        :rtype: object
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        """Sets the field_value of this ResponseInfo.


        :param field_value: The field_value of this ResponseInfo.  # noqa: E501
        :type: object
        """

        self._field_value = field_value

    @property
    def value_index(self):
        """Gets the value_index of this ResponseInfo.  # noqa: E501


        :return: The value_index of this ResponseInfo.  # noqa: E501
        :rtype: int
        """
        return self._value_index

    @value_index.setter
    def value_index(self, value_index):
        """Sets the value_index of this ResponseInfo.


        :param value_index: The value_index of this ResponseInfo.  # noqa: E501
        :type: int
        """

        self._value_index = value_index

    @property
    def message(self):
        """Gets the message of this ResponseInfo.  # noqa: E501


        :return: The message of this ResponseInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseInfo.


        :param message: The message of this ResponseInfo.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ResponseInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseInfo):
            return True

        return self.to_dict() != other.to_dict()
