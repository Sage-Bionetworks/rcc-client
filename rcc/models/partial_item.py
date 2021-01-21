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


class PartialItem(object):
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
        'item_name': 'str',
        'item_oid': 'str',
        'comment_required': 'bool',
        'required': 'bool'
    }

    attribute_map = {
        'item_name': 'itemName',
        'item_oid': 'itemOID',
        'comment_required': 'commentRequired',
        'required': 'required'
    }

    def __init__(self, item_name=None, item_oid=None, comment_required=None, required=None, local_vars_configuration=None):  # noqa: E501
        """PartialItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_name = None
        self._item_oid = None
        self._comment_required = None
        self._required = None
        self.discriminator = None

        if item_name is not None:
            self.item_name = item_name
        if item_oid is not None:
            self.item_oid = item_oid
        if comment_required is not None:
            self.comment_required = comment_required
        if required is not None:
            self.required = required

    @property
    def item_name(self):
        """Gets the item_name of this PartialItem.  # noqa: E501


        :return: The item_name of this PartialItem.  # noqa: E501
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this PartialItem.


        :param item_name: The item_name of this PartialItem.  # noqa: E501
        :type: str
        """

        self._item_name = item_name

    @property
    def item_oid(self):
        """Gets the item_oid of this PartialItem.  # noqa: E501


        :return: The item_oid of this PartialItem.  # noqa: E501
        :rtype: str
        """
        return self._item_oid

    @item_oid.setter
    def item_oid(self, item_oid):
        """Sets the item_oid of this PartialItem.


        :param item_oid: The item_oid of this PartialItem.  # noqa: E501
        :type: str
        """

        self._item_oid = item_oid

    @property
    def comment_required(self):
        """Gets the comment_required of this PartialItem.  # noqa: E501


        :return: The comment_required of this PartialItem.  # noqa: E501
        :rtype: bool
        """
        return self._comment_required

    @comment_required.setter
    def comment_required(self, comment_required):
        """Sets the comment_required of this PartialItem.


        :param comment_required: The comment_required of this PartialItem.  # noqa: E501
        :type: bool
        """

        self._comment_required = comment_required

    @property
    def required(self):
        """Gets the required of this PartialItem.  # noqa: E501


        :return: The required of this PartialItem.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this PartialItem.


        :param required: The required of this PartialItem.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if not isinstance(other, PartialItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartialItem):
            return True

        return self.to_dict() != other.to_dict()
