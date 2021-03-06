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


class JAXBElementObject(object):
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
        'name': 'QName',
        'value': 'object',
        'nil': 'bool',
        'global_scope': 'bool',
        'type_substituted': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'nil': 'nil',
        'global_scope': 'globalScope',
        'type_substituted': 'typeSubstituted'
    }

    def __init__(self, name=None, value=None, nil=None, global_scope=None, type_substituted=None, local_vars_configuration=None):  # noqa: E501
        """JAXBElementObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self._nil = None
        self._global_scope = None
        self._type_substituted = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if nil is not None:
            self.nil = nil
        if global_scope is not None:
            self.global_scope = global_scope
        if type_substituted is not None:
            self.type_substituted = type_substituted

    @property
    def name(self):
        """Gets the name of this JAXBElementObject.  # noqa: E501


        :return: The name of this JAXBElementObject.  # noqa: E501
        :rtype: QName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JAXBElementObject.


        :param name: The name of this JAXBElementObject.  # noqa: E501
        :type: QName
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this JAXBElementObject.  # noqa: E501


        :return: The value of this JAXBElementObject.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JAXBElementObject.


        :param value: The value of this JAXBElementObject.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def nil(self):
        """Gets the nil of this JAXBElementObject.  # noqa: E501


        :return: The nil of this JAXBElementObject.  # noqa: E501
        :rtype: bool
        """
        return self._nil

    @nil.setter
    def nil(self, nil):
        """Sets the nil of this JAXBElementObject.


        :param nil: The nil of this JAXBElementObject.  # noqa: E501
        :type: bool
        """

        self._nil = nil

    @property
    def global_scope(self):
        """Gets the global_scope of this JAXBElementObject.  # noqa: E501


        :return: The global_scope of this JAXBElementObject.  # noqa: E501
        :rtype: bool
        """
        return self._global_scope

    @global_scope.setter
    def global_scope(self, global_scope):
        """Sets the global_scope of this JAXBElementObject.


        :param global_scope: The global_scope of this JAXBElementObject.  # noqa: E501
        :type: bool
        """

        self._global_scope = global_scope

    @property
    def type_substituted(self):
        """Gets the type_substituted of this JAXBElementObject.  # noqa: E501


        :return: The type_substituted of this JAXBElementObject.  # noqa: E501
        :rtype: bool
        """
        return self._type_substituted

    @type_substituted.setter
    def type_substituted(self, type_substituted):
        """Sets the type_substituted of this JAXBElementObject.


        :param type_substituted: The type_substituted of this JAXBElementObject.  # noqa: E501
        :type: bool
        """

        self._type_substituted = type_substituted

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
        if not isinstance(other, JAXBElementObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JAXBElementObject):
            return True

        return self.to_dict() != other.to_dict()
