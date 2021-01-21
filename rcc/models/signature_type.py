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


class SignatureType(object):
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
        'signed_info': 'SignedInfoType',
        'signature_value': 'SignatureValueType',
        'key_info': 'KeyInfoType',
        'object': 'list[ObjectType]',
        'id': 'str'
    }

    attribute_map = {
        'signed_info': 'signedInfo',
        'signature_value': 'signatureValue',
        'key_info': 'keyInfo',
        'object': 'object',
        'id': 'id'
    }

    def __init__(self, signed_info=None, signature_value=None, key_info=None, object=None, id=None, local_vars_configuration=None):  # noqa: E501
        """SignatureType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signed_info = None
        self._signature_value = None
        self._key_info = None
        self._object = None
        self._id = None
        self.discriminator = None

        self.signed_info = signed_info
        self.signature_value = signature_value
        if key_info is not None:
            self.key_info = key_info
        if object is not None:
            self.object = object
        if id is not None:
            self.id = id

    @property
    def signed_info(self):
        """Gets the signed_info of this SignatureType.  # noqa: E501


        :return: The signed_info of this SignatureType.  # noqa: E501
        :rtype: SignedInfoType
        """
        return self._signed_info

    @signed_info.setter
    def signed_info(self, signed_info):
        """Sets the signed_info of this SignatureType.


        :param signed_info: The signed_info of this SignatureType.  # noqa: E501
        :type: SignedInfoType
        """
        if self.local_vars_configuration.client_side_validation and signed_info is None:  # noqa: E501
            raise ValueError("Invalid value for `signed_info`, must not be `None`")  # noqa: E501

        self._signed_info = signed_info

    @property
    def signature_value(self):
        """Gets the signature_value of this SignatureType.  # noqa: E501


        :return: The signature_value of this SignatureType.  # noqa: E501
        :rtype: SignatureValueType
        """
        return self._signature_value

    @signature_value.setter
    def signature_value(self, signature_value):
        """Sets the signature_value of this SignatureType.


        :param signature_value: The signature_value of this SignatureType.  # noqa: E501
        :type: SignatureValueType
        """
        if self.local_vars_configuration.client_side_validation and signature_value is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_value`, must not be `None`")  # noqa: E501

        self._signature_value = signature_value

    @property
    def key_info(self):
        """Gets the key_info of this SignatureType.  # noqa: E501


        :return: The key_info of this SignatureType.  # noqa: E501
        :rtype: KeyInfoType
        """
        return self._key_info

    @key_info.setter
    def key_info(self, key_info):
        """Sets the key_info of this SignatureType.


        :param key_info: The key_info of this SignatureType.  # noqa: E501
        :type: KeyInfoType
        """

        self._key_info = key_info

    @property
    def object(self):
        """Gets the object of this SignatureType.  # noqa: E501


        :return: The object of this SignatureType.  # noqa: E501
        :rtype: list[ObjectType]
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this SignatureType.


        :param object: The object of this SignatureType.  # noqa: E501
        :type: list[ObjectType]
        """

        self._object = object

    @property
    def id(self):
        """Gets the id of this SignatureType.  # noqa: E501


        :return: The id of this SignatureType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignatureType.


        :param id: The id of this SignatureType.  # noqa: E501
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
        if not isinstance(other, SignatureType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignatureType):
            return True

        return self.to_dict() != other.to_dict()
