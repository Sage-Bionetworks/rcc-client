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


class CRFFormSectionDefinition(object):
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
        'title': 'str',
        'subtitle': 'str',
        'status': 'str',
        'instructions': 'str',
        'page_number_label': 'str',
        'display_sequence': 'int',
        'borders': 'int',
        'fields_total_width': 'int',
        'fields_label_width': 'int',
        'section_branching_equation': 'str'
    }

    attribute_map = {
        'title': 'title',
        'subtitle': 'subtitle',
        'status': 'status',
        'instructions': 'instructions',
        'page_number_label': 'pageNumberLabel',
        'display_sequence': 'displaySequence',
        'borders': 'borders',
        'fields_total_width': 'fieldsTotalWidth',
        'fields_label_width': 'fieldsLabelWidth',
        'section_branching_equation': 'sectionBranchingEquation'
    }

    def __init__(self, title=None, subtitle=None, status=None, instructions=None, page_number_label=None, display_sequence=None, borders=None, fields_total_width=None, fields_label_width=None, section_branching_equation=None, local_vars_configuration=None):  # noqa: E501
        """CRFFormSectionDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._subtitle = None
        self._status = None
        self._instructions = None
        self._page_number_label = None
        self._display_sequence = None
        self._borders = None
        self._fields_total_width = None
        self._fields_label_width = None
        self._section_branching_equation = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if subtitle is not None:
            self.subtitle = subtitle
        if status is not None:
            self.status = status
        if instructions is not None:
            self.instructions = instructions
        if page_number_label is not None:
            self.page_number_label = page_number_label
        if display_sequence is not None:
            self.display_sequence = display_sequence
        if borders is not None:
            self.borders = borders
        if fields_total_width is not None:
            self.fields_total_width = fields_total_width
        if fields_label_width is not None:
            self.fields_label_width = fields_label_width
        if section_branching_equation is not None:
            self.section_branching_equation = section_branching_equation

    @property
    def title(self):
        """Gets the title of this CRFFormSectionDefinition.  # noqa: E501


        :return: The title of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CRFFormSectionDefinition.


        :param title: The title of this CRFFormSectionDefinition.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subtitle(self):
        """Gets the subtitle of this CRFFormSectionDefinition.  # noqa: E501


        :return: The subtitle of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this CRFFormSectionDefinition.


        :param subtitle: The subtitle of this CRFFormSectionDefinition.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def status(self):
        """Gets the status of this CRFFormSectionDefinition.  # noqa: E501


        :return: The status of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CRFFormSectionDefinition.


        :param status: The status of this CRFFormSectionDefinition.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def instructions(self):
        """Gets the instructions of this CRFFormSectionDefinition.  # noqa: E501


        :return: The instructions of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this CRFFormSectionDefinition.


        :param instructions: The instructions of this CRFFormSectionDefinition.  # noqa: E501
        :type: str
        """

        self._instructions = instructions

    @property
    def page_number_label(self):
        """Gets the page_number_label of this CRFFormSectionDefinition.  # noqa: E501


        :return: The page_number_label of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._page_number_label

    @page_number_label.setter
    def page_number_label(self, page_number_label):
        """Sets the page_number_label of this CRFFormSectionDefinition.


        :param page_number_label: The page_number_label of this CRFFormSectionDefinition.  # noqa: E501
        :type: str
        """

        self._page_number_label = page_number_label

    @property
    def display_sequence(self):
        """Gets the display_sequence of this CRFFormSectionDefinition.  # noqa: E501


        :return: The display_sequence of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._display_sequence

    @display_sequence.setter
    def display_sequence(self, display_sequence):
        """Sets the display_sequence of this CRFFormSectionDefinition.


        :param display_sequence: The display_sequence of this CRFFormSectionDefinition.  # noqa: E501
        :type: int
        """

        self._display_sequence = display_sequence

    @property
    def borders(self):
        """Gets the borders of this CRFFormSectionDefinition.  # noqa: E501


        :return: The borders of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._borders

    @borders.setter
    def borders(self, borders):
        """Sets the borders of this CRFFormSectionDefinition.


        :param borders: The borders of this CRFFormSectionDefinition.  # noqa: E501
        :type: int
        """

        self._borders = borders

    @property
    def fields_total_width(self):
        """Gets the fields_total_width of this CRFFormSectionDefinition.  # noqa: E501


        :return: The fields_total_width of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._fields_total_width

    @fields_total_width.setter
    def fields_total_width(self, fields_total_width):
        """Sets the fields_total_width of this CRFFormSectionDefinition.


        :param fields_total_width: The fields_total_width of this CRFFormSectionDefinition.  # noqa: E501
        :type: int
        """

        self._fields_total_width = fields_total_width

    @property
    def fields_label_width(self):
        """Gets the fields_label_width of this CRFFormSectionDefinition.  # noqa: E501


        :return: The fields_label_width of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: int
        """
        return self._fields_label_width

    @fields_label_width.setter
    def fields_label_width(self, fields_label_width):
        """Sets the fields_label_width of this CRFFormSectionDefinition.


        :param fields_label_width: The fields_label_width of this CRFFormSectionDefinition.  # noqa: E501
        :type: int
        """

        self._fields_label_width = fields_label_width

    @property
    def section_branching_equation(self):
        """Gets the section_branching_equation of this CRFFormSectionDefinition.  # noqa: E501


        :return: The section_branching_equation of this CRFFormSectionDefinition.  # noqa: E501
        :rtype: str
        """
        return self._section_branching_equation

    @section_branching_equation.setter
    def section_branching_equation(self, section_branching_equation):
        """Sets the section_branching_equation of this CRFFormSectionDefinition.


        :param section_branching_equation: The section_branching_equation of this CRFFormSectionDefinition.  # noqa: E501
        :type: str
        """

        self._section_branching_equation = section_branching_equation

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
        if not isinstance(other, CRFFormSectionDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CRFFormSectionDefinition):
            return True

        return self.to_dict() != other.to_dict()
