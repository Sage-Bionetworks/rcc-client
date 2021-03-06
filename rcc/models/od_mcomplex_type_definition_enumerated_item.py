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


class ODMcomplexTypeDefinitionEnumeratedItem(object):
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
        'alias': 'list[ODMcomplexTypeDefinitionAlias]',
        'coded_value': 'str',
        'ui_width': 'str',
        'rank': 'float',
        'order_number': 'int'
    }

    attribute_map = {
        'alias': 'alias',
        'coded_value': 'codedValue',
        'ui_width': 'uiWidth',
        'rank': 'rank',
        'order_number': 'orderNumber'
    }

    def __init__(self, alias=None, coded_value=None, ui_width=None, rank=None, order_number=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionEnumeratedItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alias = None
        self._coded_value = None
        self._ui_width = None
        self._rank = None
        self._order_number = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if coded_value is not None:
            self.coded_value = coded_value
        if ui_width is not None:
            self.ui_width = ui_width
        if rank is not None:
            self.rank = rank
        if order_number is not None:
            self.order_number = order_number

    @property
    def alias(self):
        """Gets the alias of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501


        :return: The alias of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ODMcomplexTypeDefinitionEnumeratedItem.


        :param alias: The alias of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAlias]
        """

        self._alias = alias

    @property
    def coded_value(self):
        """Gets the coded_value of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501


        :return: The coded_value of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :rtype: str
        """
        return self._coded_value

    @coded_value.setter
    def coded_value(self, coded_value):
        """Sets the coded_value of this ODMcomplexTypeDefinitionEnumeratedItem.


        :param coded_value: The coded_value of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :type: str
        """

        self._coded_value = coded_value

    @property
    def ui_width(self):
        """Gets the ui_width of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501


        :return: The ui_width of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :rtype: str
        """
        return self._ui_width

    @ui_width.setter
    def ui_width(self, ui_width):
        """Sets the ui_width of this ODMcomplexTypeDefinitionEnumeratedItem.


        :param ui_width: The ui_width of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :type: str
        """

        self._ui_width = ui_width

    @property
    def rank(self):
        """Gets the rank of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501


        :return: The rank of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :rtype: float
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this ODMcomplexTypeDefinitionEnumeratedItem.


        :param rank: The rank of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :type: float
        """

        self._rank = rank

    @property
    def order_number(self):
        """Gets the order_number of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501


        :return: The order_number of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this ODMcomplexTypeDefinitionEnumeratedItem.


        :param order_number: The order_number of this ODMcomplexTypeDefinitionEnumeratedItem.  # noqa: E501
        :type: int
        """

        self._order_number = order_number

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
        if not isinstance(other, ODMcomplexTypeDefinitionEnumeratedItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionEnumeratedItem):
            return True

        return self.to_dict() != other.to_dict()
