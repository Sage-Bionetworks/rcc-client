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


class ODMcomplexTypeDefinitionLocation(object):
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
        'meta_data_version_ref': 'list[ODMcomplexTypeDefinitionMetaDataVersionRef]',
        'oid': 'str',
        'name': 'str',
        'location_type': 'str'
    }

    attribute_map = {
        'meta_data_version_ref': 'metaDataVersionRef',
        'oid': 'oid',
        'name': 'name',
        'location_type': 'locationType'
    }

    def __init__(self, meta_data_version_ref=None, oid=None, name=None, location_type=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._meta_data_version_ref = None
        self._oid = None
        self._name = None
        self._location_type = None
        self.discriminator = None

        self.meta_data_version_ref = meta_data_version_ref
        if oid is not None:
            self.oid = oid
        if name is not None:
            self.name = name
        if location_type is not None:
            self.location_type = location_type

    @property
    def meta_data_version_ref(self):
        """Gets the meta_data_version_ref of this ODMcomplexTypeDefinitionLocation.  # noqa: E501


        :return: The meta_data_version_ref of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionMetaDataVersionRef]
        """
        return self._meta_data_version_ref

    @meta_data_version_ref.setter
    def meta_data_version_ref(self, meta_data_version_ref):
        """Sets the meta_data_version_ref of this ODMcomplexTypeDefinitionLocation.


        :param meta_data_version_ref: The meta_data_version_ref of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionMetaDataVersionRef]
        """
        if self.local_vars_configuration.client_side_validation and meta_data_version_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `meta_data_version_ref`, must not be `None`")  # noqa: E501

        self._meta_data_version_ref = meta_data_version_ref

    @property
    def oid(self):
        """Gets the oid of this ODMcomplexTypeDefinitionLocation.  # noqa: E501


        :return: The oid of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this ODMcomplexTypeDefinitionLocation.


        :param oid: The oid of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def name(self):
        """Gets the name of this ODMcomplexTypeDefinitionLocation.  # noqa: E501


        :return: The name of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ODMcomplexTypeDefinitionLocation.


        :param name: The name of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def location_type(self):
        """Gets the location_type of this ODMcomplexTypeDefinitionLocation.  # noqa: E501


        :return: The location_type of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this ODMcomplexTypeDefinitionLocation.


        :param location_type: The location_type of this ODMcomplexTypeDefinitionLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["SPONSOR", "SITE", "CRO", "LAB", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and location_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `location_type` ({0}), must be one of {1}"  # noqa: E501
                .format(location_type, allowed_values)
            )

        self._location_type = location_type

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
        if not isinstance(other, ODMcomplexTypeDefinitionLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionLocation):
            return True

        return self.to_dict() != other.to_dict()
