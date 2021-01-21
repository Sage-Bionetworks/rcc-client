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


class SignedInfoType(object):
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
        'canonicalization_method': 'CanonicalizationMethodType',
        'signature_method': 'SignatureMethodType',
        'reference': 'list[ReferenceType]',
        'id': 'str'
    }

    attribute_map = {
        'canonicalization_method': 'canonicalizationMethod',
        'signature_method': 'signatureMethod',
        'reference': 'reference',
        'id': 'id'
    }

    def __init__(self, canonicalization_method=None, signature_method=None, reference=None, id=None, local_vars_configuration=None):  # noqa: E501
        """SignedInfoType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._canonicalization_method = None
        self._signature_method = None
        self._reference = None
        self._id = None
        self.discriminator = None

        self.canonicalization_method = canonicalization_method
        self.signature_method = signature_method
        self.reference = reference
        if id is not None:
            self.id = id

    @property
    def canonicalization_method(self):
        """Gets the canonicalization_method of this SignedInfoType.  # noqa: E501


        :return: The canonicalization_method of this SignedInfoType.  # noqa: E501
        :rtype: CanonicalizationMethodType
        """
        return self._canonicalization_method

    @canonicalization_method.setter
    def canonicalization_method(self, canonicalization_method):
        """Sets the canonicalization_method of this SignedInfoType.


        :param canonicalization_method: The canonicalization_method of this SignedInfoType.  # noqa: E501
        :type: CanonicalizationMethodType
        """
        if self.local_vars_configuration.client_side_validation and canonicalization_method is None:  # noqa: E501
            raise ValueError("Invalid value for `canonicalization_method`, must not be `None`")  # noqa: E501

        self._canonicalization_method = canonicalization_method

    @property
    def signature_method(self):
        """Gets the signature_method of this SignedInfoType.  # noqa: E501


        :return: The signature_method of this SignedInfoType.  # noqa: E501
        :rtype: SignatureMethodType
        """
        return self._signature_method

    @signature_method.setter
    def signature_method(self, signature_method):
        """Sets the signature_method of this SignedInfoType.


        :param signature_method: The signature_method of this SignedInfoType.  # noqa: E501
        :type: SignatureMethodType
        """
        if self.local_vars_configuration.client_side_validation and signature_method is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_method`, must not be `None`")  # noqa: E501

        self._signature_method = signature_method

    @property
    def reference(self):
        """Gets the reference of this SignedInfoType.  # noqa: E501


        :return: The reference of this SignedInfoType.  # noqa: E501
        :rtype: list[ReferenceType]
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SignedInfoType.


        :param reference: The reference of this SignedInfoType.  # noqa: E501
        :type: list[ReferenceType]
        """
        if self.local_vars_configuration.client_side_validation and reference is None:  # noqa: E501
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def id(self):
        """Gets the id of this SignedInfoType.  # noqa: E501


        :return: The id of this SignedInfoType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignedInfoType.


        :param id: The id of this SignedInfoType.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, SignedInfoType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignedInfoType):
            return True

        return self.to_dict() != other.to_dict()