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


class ODMcomplexTypeDefinitionRangeCheck(object):
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
        'check_value': 'list[ODMcomplexTypeDefinitionCheckValue]',
        'formal_expression': 'list[ODMcomplexTypeDefinitionFormalExpression]',
        'measurement_unit_ref': 'ODMcomplexTypeDefinitionMeasurementUnitRef',
        'error_message': 'ODMcomplexTypeDefinitionErrorMessage',
        'comparator': 'str',
        'soft_hard': 'str'
    }

    attribute_map = {
        'check_value': 'checkValue',
        'formal_expression': 'formalExpression',
        'measurement_unit_ref': 'measurementUnitRef',
        'error_message': 'errorMessage',
        'comparator': 'comparator',
        'soft_hard': 'softHard'
    }

    def __init__(self, check_value=None, formal_expression=None, measurement_unit_ref=None, error_message=None, comparator=None, soft_hard=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionRangeCheck - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._check_value = None
        self._formal_expression = None
        self._measurement_unit_ref = None
        self._error_message = None
        self._comparator = None
        self._soft_hard = None
        self.discriminator = None

        if check_value is not None:
            self.check_value = check_value
        if formal_expression is not None:
            self.formal_expression = formal_expression
        if measurement_unit_ref is not None:
            self.measurement_unit_ref = measurement_unit_ref
        if error_message is not None:
            self.error_message = error_message
        if comparator is not None:
            self.comparator = comparator
        if soft_hard is not None:
            self.soft_hard = soft_hard

    @property
    def check_value(self):
        """Gets the check_value of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501


        :return: The check_value of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionCheckValue]
        """
        return self._check_value

    @check_value.setter
    def check_value(self, check_value):
        """Sets the check_value of this ODMcomplexTypeDefinitionRangeCheck.


        :param check_value: The check_value of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionCheckValue]
        """

        self._check_value = check_value

    @property
    def formal_expression(self):
        """Gets the formal_expression of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501


        :return: The formal_expression of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionFormalExpression]
        """
        return self._formal_expression

    @formal_expression.setter
    def formal_expression(self, formal_expression):
        """Sets the formal_expression of this ODMcomplexTypeDefinitionRangeCheck.


        :param formal_expression: The formal_expression of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionFormalExpression]
        """

        self._formal_expression = formal_expression

    @property
    def measurement_unit_ref(self):
        """Gets the measurement_unit_ref of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501


        :return: The measurement_unit_ref of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionMeasurementUnitRef
        """
        return self._measurement_unit_ref

    @measurement_unit_ref.setter
    def measurement_unit_ref(self, measurement_unit_ref):
        """Sets the measurement_unit_ref of this ODMcomplexTypeDefinitionRangeCheck.


        :param measurement_unit_ref: The measurement_unit_ref of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :type: ODMcomplexTypeDefinitionMeasurementUnitRef
        """

        self._measurement_unit_ref = measurement_unit_ref

    @property
    def error_message(self):
        """Gets the error_message of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501


        :return: The error_message of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionErrorMessage
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ODMcomplexTypeDefinitionRangeCheck.


        :param error_message: The error_message of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :type: ODMcomplexTypeDefinitionErrorMessage
        """

        self._error_message = error_message

    @property
    def comparator(self):
        """Gets the comparator of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501


        :return: The comparator of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :rtype: str
        """
        return self._comparator

    @comparator.setter
    def comparator(self, comparator):
        """Sets the comparator of this ODMcomplexTypeDefinitionRangeCheck.


        :param comparator: The comparator of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :type: str
        """
        allowed_values = ["LT", "LE", "GT", "GE", "EQ", "NE", "IN", "NOTIN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and comparator not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `comparator` ({0}), must be one of {1}"  # noqa: E501
                .format(comparator, allowed_values)
            )

        self._comparator = comparator

    @property
    def soft_hard(self):
        """Gets the soft_hard of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501


        :return: The soft_hard of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :rtype: str
        """
        return self._soft_hard

    @soft_hard.setter
    def soft_hard(self, soft_hard):
        """Sets the soft_hard of this ODMcomplexTypeDefinitionRangeCheck.


        :param soft_hard: The soft_hard of this ODMcomplexTypeDefinitionRangeCheck.  # noqa: E501
        :type: str
        """
        allowed_values = ["SOFT", "HARD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and soft_hard not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `soft_hard` ({0}), must be one of {1}"  # noqa: E501
                .format(soft_hard, allowed_values)
            )

        self._soft_hard = soft_hard

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
        if not isinstance(other, ODMcomplexTypeDefinitionRangeCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionRangeCheck):
            return True

        return self.to_dict() != other.to_dict()
