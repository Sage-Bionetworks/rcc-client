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


class MigrationSoftValidationItems(object):
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
        'item_metadata_oid': 'str',
        'bypass_comment': 'str',
        'bypassed': 'bool'
    }

    attribute_map = {
        'item_metadata_oid': 'itemMetadataOID',
        'bypass_comment': 'bypassComment',
        'bypassed': 'bypassed'
    }

    def __init__(self, item_metadata_oid=None, bypass_comment=None, bypassed=None, local_vars_configuration=None):  # noqa: E501
        """MigrationSoftValidationItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_metadata_oid = None
        self._bypass_comment = None
        self._bypassed = None
        self.discriminator = None

        if item_metadata_oid is not None:
            self.item_metadata_oid = item_metadata_oid
        if bypass_comment is not None:
            self.bypass_comment = bypass_comment
        if bypassed is not None:
            self.bypassed = bypassed

    @property
    def item_metadata_oid(self):
        """Gets the item_metadata_oid of this MigrationSoftValidationItems.  # noqa: E501


        :return: The item_metadata_oid of this MigrationSoftValidationItems.  # noqa: E501
        :rtype: str
        """
        return self._item_metadata_oid

    @item_metadata_oid.setter
    def item_metadata_oid(self, item_metadata_oid):
        """Sets the item_metadata_oid of this MigrationSoftValidationItems.


        :param item_metadata_oid: The item_metadata_oid of this MigrationSoftValidationItems.  # noqa: E501
        :type: str
        """

        self._item_metadata_oid = item_metadata_oid

    @property
    def bypass_comment(self):
        """Gets the bypass_comment of this MigrationSoftValidationItems.  # noqa: E501


        :return: The bypass_comment of this MigrationSoftValidationItems.  # noqa: E501
        :rtype: str
        """
        return self._bypass_comment

    @bypass_comment.setter
    def bypass_comment(self, bypass_comment):
        """Sets the bypass_comment of this MigrationSoftValidationItems.


        :param bypass_comment: The bypass_comment of this MigrationSoftValidationItems.  # noqa: E501
        :type: str
        """

        self._bypass_comment = bypass_comment

    @property
    def bypassed(self):
        """Gets the bypassed of this MigrationSoftValidationItems.  # noqa: E501


        :return: The bypassed of this MigrationSoftValidationItems.  # noqa: E501
        :rtype: bool
        """
        return self._bypassed

    @bypassed.setter
    def bypassed(self, bypassed):
        """Sets the bypassed of this MigrationSoftValidationItems.


        :param bypassed: The bypassed of this MigrationSoftValidationItems.  # noqa: E501
        :type: bool
        """

        self._bypassed = bypassed

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
        if not isinstance(other, MigrationSoftValidationItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationSoftValidationItems):
            return True

        return self.to_dict() != other.to_dict()