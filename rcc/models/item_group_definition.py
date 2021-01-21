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


class ItemGroupDefinition(object):
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
        'item_group_row': 'list[ItemGroupRow]',
        'item_group_col': 'list[ItemGroupCol]',
        'group_status': 'str',
        'group_type': 'str',
        'section_oid': 'str',
        'name': 'str',
        'oid': 'str',
        'display_sequence': 'int',
        'group_branching_equation': 'str',
        'max_repeating_rows': 'int',
        'is_fixed_rows': 'bool',
        'is_dummy_flag': 'bool',
        'original_item_groups_oid': 'str'
    }

    attribute_map = {
        'item_group_row': 'itemGroupRow',
        'item_group_col': 'itemGroupCol',
        'group_status': 'groupStatus',
        'group_type': 'groupType',
        'section_oid': 'sectionOID',
        'name': 'name',
        'oid': 'oid',
        'display_sequence': 'displaySequence',
        'group_branching_equation': 'groupBranchingEquation',
        'max_repeating_rows': 'maxRepeatingRows',
        'is_fixed_rows': 'isFixedRows',
        'is_dummy_flag': 'isDummyFlag',
        'original_item_groups_oid': 'originalItemGroupsOID'
    }

    def __init__(self, item_group_row=None, item_group_col=None, group_status=None, group_type=None, section_oid=None, name=None, oid=None, display_sequence=None, group_branching_equation=None, max_repeating_rows=None, is_fixed_rows=None, is_dummy_flag=None, original_item_groups_oid=None, local_vars_configuration=None):  # noqa: E501
        """ItemGroupDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_group_row = None
        self._item_group_col = None
        self._group_status = None
        self._group_type = None
        self._section_oid = None
        self._name = None
        self._oid = None
        self._display_sequence = None
        self._group_branching_equation = None
        self._max_repeating_rows = None
        self._is_fixed_rows = None
        self._is_dummy_flag = None
        self._original_item_groups_oid = None
        self.discriminator = None

        if item_group_row is not None:
            self.item_group_row = item_group_row
        if item_group_col is not None:
            self.item_group_col = item_group_col
        if group_status is not None:
            self.group_status = group_status
        if group_type is not None:
            self.group_type = group_type
        if section_oid is not None:
            self.section_oid = section_oid
        if name is not None:
            self.name = name
        if oid is not None:
            self.oid = oid
        if display_sequence is not None:
            self.display_sequence = display_sequence
        if group_branching_equation is not None:
            self.group_branching_equation = group_branching_equation
        if max_repeating_rows is not None:
            self.max_repeating_rows = max_repeating_rows
        if is_fixed_rows is not None:
            self.is_fixed_rows = is_fixed_rows
        if is_dummy_flag is not None:
            self.is_dummy_flag = is_dummy_flag
        if original_item_groups_oid is not None:
            self.original_item_groups_oid = original_item_groups_oid

    @property
    def item_group_row(self):
        """Gets the item_group_row of this ItemGroupDefinition.  # noqa: E501


        :return: The item_group_row of this ItemGroupDefinition.  # noqa: E501
        :rtype: list[ItemGroupRow]
        """
        return self._item_group_row

    @item_group_row.setter
    def item_group_row(self, item_group_row):
        """Sets the item_group_row of this ItemGroupDefinition.


        :param item_group_row: The item_group_row of this ItemGroupDefinition.  # noqa: E501
        :type: list[ItemGroupRow]
        """

        self._item_group_row = item_group_row

    @property
    def item_group_col(self):
        """Gets the item_group_col of this ItemGroupDefinition.  # noqa: E501


        :return: The item_group_col of this ItemGroupDefinition.  # noqa: E501
        :rtype: list[ItemGroupCol]
        """
        return self._item_group_col

    @item_group_col.setter
    def item_group_col(self, item_group_col):
        """Sets the item_group_col of this ItemGroupDefinition.


        :param item_group_col: The item_group_col of this ItemGroupDefinition.  # noqa: E501
        :type: list[ItemGroupCol]
        """

        self._item_group_col = item_group_col

    @property
    def group_status(self):
        """Gets the group_status of this ItemGroupDefinition.  # noqa: E501


        :return: The group_status of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._group_status

    @group_status.setter
    def group_status(self, group_status):
        """Sets the group_status of this ItemGroupDefinition.


        :param group_status: The group_status of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._group_status = group_status

    @property
    def group_type(self):
        """Gets the group_type of this ItemGroupDefinition.  # noqa: E501


        :return: The group_type of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this ItemGroupDefinition.


        :param group_type: The group_type of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def section_oid(self):
        """Gets the section_oid of this ItemGroupDefinition.  # noqa: E501


        :return: The section_oid of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._section_oid

    @section_oid.setter
    def section_oid(self, section_oid):
        """Sets the section_oid of this ItemGroupDefinition.


        :param section_oid: The section_oid of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._section_oid = section_oid

    @property
    def name(self):
        """Gets the name of this ItemGroupDefinition.  # noqa: E501


        :return: The name of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemGroupDefinition.


        :param name: The name of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oid(self):
        """Gets the oid of this ItemGroupDefinition.  # noqa: E501


        :return: The oid of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this ItemGroupDefinition.


        :param oid: The oid of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def display_sequence(self):
        """Gets the display_sequence of this ItemGroupDefinition.  # noqa: E501


        :return: The display_sequence of this ItemGroupDefinition.  # noqa: E501
        :rtype: int
        """
        return self._display_sequence

    @display_sequence.setter
    def display_sequence(self, display_sequence):
        """Sets the display_sequence of this ItemGroupDefinition.


        :param display_sequence: The display_sequence of this ItemGroupDefinition.  # noqa: E501
        :type: int
        """

        self._display_sequence = display_sequence

    @property
    def group_branching_equation(self):
        """Gets the group_branching_equation of this ItemGroupDefinition.  # noqa: E501


        :return: The group_branching_equation of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._group_branching_equation

    @group_branching_equation.setter
    def group_branching_equation(self, group_branching_equation):
        """Sets the group_branching_equation of this ItemGroupDefinition.


        :param group_branching_equation: The group_branching_equation of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._group_branching_equation = group_branching_equation

    @property
    def max_repeating_rows(self):
        """Gets the max_repeating_rows of this ItemGroupDefinition.  # noqa: E501


        :return: The max_repeating_rows of this ItemGroupDefinition.  # noqa: E501
        :rtype: int
        """
        return self._max_repeating_rows

    @max_repeating_rows.setter
    def max_repeating_rows(self, max_repeating_rows):
        """Sets the max_repeating_rows of this ItemGroupDefinition.


        :param max_repeating_rows: The max_repeating_rows of this ItemGroupDefinition.  # noqa: E501
        :type: int
        """

        self._max_repeating_rows = max_repeating_rows

    @property
    def is_fixed_rows(self):
        """Gets the is_fixed_rows of this ItemGroupDefinition.  # noqa: E501


        :return: The is_fixed_rows of this ItemGroupDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_fixed_rows

    @is_fixed_rows.setter
    def is_fixed_rows(self, is_fixed_rows):
        """Sets the is_fixed_rows of this ItemGroupDefinition.


        :param is_fixed_rows: The is_fixed_rows of this ItemGroupDefinition.  # noqa: E501
        :type: bool
        """

        self._is_fixed_rows = is_fixed_rows

    @property
    def is_dummy_flag(self):
        """Gets the is_dummy_flag of this ItemGroupDefinition.  # noqa: E501


        :return: The is_dummy_flag of this ItemGroupDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_dummy_flag

    @is_dummy_flag.setter
    def is_dummy_flag(self, is_dummy_flag):
        """Sets the is_dummy_flag of this ItemGroupDefinition.


        :param is_dummy_flag: The is_dummy_flag of this ItemGroupDefinition.  # noqa: E501
        :type: bool
        """

        self._is_dummy_flag = is_dummy_flag

    @property
    def original_item_groups_oid(self):
        """Gets the original_item_groups_oid of this ItemGroupDefinition.  # noqa: E501


        :return: The original_item_groups_oid of this ItemGroupDefinition.  # noqa: E501
        :rtype: str
        """
        return self._original_item_groups_oid

    @original_item_groups_oid.setter
    def original_item_groups_oid(self, original_item_groups_oid):
        """Sets the original_item_groups_oid of this ItemGroupDefinition.


        :param original_item_groups_oid: The original_item_groups_oid of this ItemGroupDefinition.  # noqa: E501
        :type: str
        """

        self._original_item_groups_oid = original_item_groups_oid

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
        if not isinstance(other, ItemGroupDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemGroupDefinition):
            return True

        return self.to_dict() != other.to_dict()