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


class RoleComponentPermission(object):
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
        'permission_id': 'list[PermissionId]',
        'component': 'str',
        'component_oid': 'str'
    }

    attribute_map = {
        'permission_id': 'permissionId',
        'component': 'component',
        'component_oid': 'componentOID'
    }

    def __init__(self, permission_id=None, component=None, component_oid=None, local_vars_configuration=None):  # noqa: E501
        """RoleComponentPermission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._permission_id = None
        self._component = None
        self._component_oid = None
        self.discriminator = None

        if permission_id is not None:
            self.permission_id = permission_id
        if component is not None:
            self.component = component
        if component_oid is not None:
            self.component_oid = component_oid

    @property
    def permission_id(self):
        """Gets the permission_id of this RoleComponentPermission.  # noqa: E501


        :return: The permission_id of this RoleComponentPermission.  # noqa: E501
        :rtype: list[PermissionId]
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        """Sets the permission_id of this RoleComponentPermission.


        :param permission_id: The permission_id of this RoleComponentPermission.  # noqa: E501
        :type: list[PermissionId]
        """

        self._permission_id = permission_id

    @property
    def component(self):
        """Gets the component of this RoleComponentPermission.  # noqa: E501


        :return: The component of this RoleComponentPermission.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this RoleComponentPermission.


        :param component: The component of this RoleComponentPermission.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def component_oid(self):
        """Gets the component_oid of this RoleComponentPermission.  # noqa: E501


        :return: The component_oid of this RoleComponentPermission.  # noqa: E501
        :rtype: str
        """
        return self._component_oid

    @component_oid.setter
    def component_oid(self, component_oid):
        """Sets the component_oid of this RoleComponentPermission.


        :param component_oid: The component_oid of this RoleComponentPermission.  # noqa: E501
        :type: str
        """

        self._component_oid = component_oid

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
        if not isinstance(other, RoleComponentPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleComponentPermission):
            return True

        return self.to_dict() != other.to_dict()
