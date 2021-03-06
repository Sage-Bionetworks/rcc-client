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


class ODMcomplexTypeDefinitionMethodDef(object):
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
        'description': 'ODMcomplexTypeDefinitionDescription',
        'formal_expression': 'list[ODMcomplexTypeDefinitionFormalExpression]',
        'alias': 'list[ODMcomplexTypeDefinitionAlias]',
        'oid': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'formal_expression': 'formalExpression',
        'alias': 'alias',
        'oid': 'oid',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, description=None, formal_expression=None, alias=None, oid=None, name=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionMethodDef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._formal_expression = None
        self._alias = None
        self._oid = None
        self._name = None
        self._type = None
        self.discriminator = None

        self.description = description
        if formal_expression is not None:
            self.formal_expression = formal_expression
        if alias is not None:
            self.alias = alias
        if oid is not None:
            self.oid = oid
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501


        :return: The description of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ODMcomplexTypeDefinitionMethodDef.


        :param description: The description of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :type: ODMcomplexTypeDefinitionDescription
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def formal_expression(self):
        """Gets the formal_expression of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501


        :return: The formal_expression of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionFormalExpression]
        """
        return self._formal_expression

    @formal_expression.setter
    def formal_expression(self, formal_expression):
        """Sets the formal_expression of this ODMcomplexTypeDefinitionMethodDef.


        :param formal_expression: The formal_expression of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionFormalExpression]
        """

        self._formal_expression = formal_expression

    @property
    def alias(self):
        """Gets the alias of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501


        :return: The alias of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ODMcomplexTypeDefinitionMethodDef.


        :param alias: The alias of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAlias]
        """

        self._alias = alias

    @property
    def oid(self):
        """Gets the oid of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501


        :return: The oid of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this ODMcomplexTypeDefinitionMethodDef.


        :param oid: The oid of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def name(self):
        """Gets the name of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501


        :return: The name of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ODMcomplexTypeDefinitionMethodDef.


        :param name: The name of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501


        :return: The type of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ODMcomplexTypeDefinitionMethodDef.


        :param type: The type of this ODMcomplexTypeDefinitionMethodDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMPUTATION", "IMPUTATION", "TRANSPOSE", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, ODMcomplexTypeDefinitionMethodDef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionMethodDef):
            return True

        return self.to_dict() != other.to_dict()
