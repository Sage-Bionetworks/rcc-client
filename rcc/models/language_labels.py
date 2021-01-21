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


class LanguageLabels(object):
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
        'language_label': 'list[LanguageLabel]'
    }

    attribute_map = {
        'language_label': 'languageLabel'
    }

    def __init__(self, language_label=None, local_vars_configuration=None):  # noqa: E501
        """LanguageLabels - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._language_label = None
        self.discriminator = None

        if language_label is not None:
            self.language_label = language_label

    @property
    def language_label(self):
        """Gets the language_label of this LanguageLabels.  # noqa: E501


        :return: The language_label of this LanguageLabels.  # noqa: E501
        :rtype: list[LanguageLabel]
        """
        return self._language_label

    @language_label.setter
    def language_label(self, language_label):
        """Sets the language_label of this LanguageLabels.


        :param language_label: The language_label of this LanguageLabels.  # noqa: E501
        :type: list[LanguageLabel]
        """

        self._language_label = language_label

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
        if not isinstance(other, LanguageLabels):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LanguageLabels):
            return True

        return self.to_dict() != other.to_dict()