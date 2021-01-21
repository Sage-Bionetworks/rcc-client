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


class MedicalCodedItemsRpc(object):
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
        'dictionary_id': 'int',
        'coded_item': 'MedicalCodedItem'
    }

    attribute_map = {
        'dictionary_id': 'dictionaryId',
        'coded_item': 'codedItem'
    }

    def __init__(self, dictionary_id=None, coded_item=None, local_vars_configuration=None):  # noqa: E501
        """MedicalCodedItemsRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dictionary_id = None
        self._coded_item = None
        self.discriminator = None

        if dictionary_id is not None:
            self.dictionary_id = dictionary_id
        if coded_item is not None:
            self.coded_item = coded_item

    @property
    def dictionary_id(self):
        """Gets the dictionary_id of this MedicalCodedItemsRpc.  # noqa: E501


        :return: The dictionary_id of this MedicalCodedItemsRpc.  # noqa: E501
        :rtype: int
        """
        return self._dictionary_id

    @dictionary_id.setter
    def dictionary_id(self, dictionary_id):
        """Sets the dictionary_id of this MedicalCodedItemsRpc.


        :param dictionary_id: The dictionary_id of this MedicalCodedItemsRpc.  # noqa: E501
        :type: int
        """

        self._dictionary_id = dictionary_id

    @property
    def coded_item(self):
        """Gets the coded_item of this MedicalCodedItemsRpc.  # noqa: E501


        :return: The coded_item of this MedicalCodedItemsRpc.  # noqa: E501
        :rtype: MedicalCodedItem
        """
        return self._coded_item

    @coded_item.setter
    def coded_item(self, coded_item):
        """Sets the coded_item of this MedicalCodedItemsRpc.


        :param coded_item: The coded_item of this MedicalCodedItemsRpc.  # noqa: E501
        :type: MedicalCodedItem
        """

        self._coded_item = coded_item

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
        if not isinstance(other, MedicalCodedItemsRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MedicalCodedItemsRpc):
            return True

        return self.to_dict() != other.to_dict()
