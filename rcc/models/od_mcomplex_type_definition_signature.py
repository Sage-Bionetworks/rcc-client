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


class ODMcomplexTypeDefinitionSignature(object):
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
        'user_ref': 'ODMcomplexTypeDefinitionUserRef',
        'location_ref': 'ODMcomplexTypeDefinitionLocationRef',
        'signature_ref': 'ODMcomplexTypeDefinitionSignatureRef',
        'date_time_stamp': 'ODMcomplexTypeDefinitionDateTimeStamp',
        'crypto_binding_manifest': 'ODMcomplexTypeDefinitionCryptoBindingManifest',
        'id': 'str'
    }

    attribute_map = {
        'user_ref': 'userRef',
        'location_ref': 'locationRef',
        'signature_ref': 'signatureRef',
        'date_time_stamp': 'dateTimeStamp',
        'crypto_binding_manifest': 'cryptoBindingManifest',
        'id': 'id'
    }

    def __init__(self, user_ref=None, location_ref=None, signature_ref=None, date_time_stamp=None, crypto_binding_manifest=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionSignature - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_ref = None
        self._location_ref = None
        self._signature_ref = None
        self._date_time_stamp = None
        self._crypto_binding_manifest = None
        self._id = None
        self.discriminator = None

        self.user_ref = user_ref
        self.location_ref = location_ref
        self.signature_ref = signature_ref
        self.date_time_stamp = date_time_stamp
        if crypto_binding_manifest is not None:
            self.crypto_binding_manifest = crypto_binding_manifest
        if id is not None:
            self.id = id

    @property
    def user_ref(self):
        """Gets the user_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501


        :return: The user_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionUserRef
        """
        return self._user_ref

    @user_ref.setter
    def user_ref(self, user_ref):
        """Sets the user_ref of this ODMcomplexTypeDefinitionSignature.


        :param user_ref: The user_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :type: ODMcomplexTypeDefinitionUserRef
        """
        if self.local_vars_configuration.client_side_validation and user_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `user_ref`, must not be `None`")  # noqa: E501

        self._user_ref = user_ref

    @property
    def location_ref(self):
        """Gets the location_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501


        :return: The location_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionLocationRef
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this ODMcomplexTypeDefinitionSignature.


        :param location_ref: The location_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :type: ODMcomplexTypeDefinitionLocationRef
        """
        if self.local_vars_configuration.client_side_validation and location_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `location_ref`, must not be `None`")  # noqa: E501

        self._location_ref = location_ref

    @property
    def signature_ref(self):
        """Gets the signature_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501


        :return: The signature_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionSignatureRef
        """
        return self._signature_ref

    @signature_ref.setter
    def signature_ref(self, signature_ref):
        """Sets the signature_ref of this ODMcomplexTypeDefinitionSignature.


        :param signature_ref: The signature_ref of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :type: ODMcomplexTypeDefinitionSignatureRef
        """
        if self.local_vars_configuration.client_side_validation and signature_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_ref`, must not be `None`")  # noqa: E501

        self._signature_ref = signature_ref

    @property
    def date_time_stamp(self):
        """Gets the date_time_stamp of this ODMcomplexTypeDefinitionSignature.  # noqa: E501


        :return: The date_time_stamp of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionDateTimeStamp
        """
        return self._date_time_stamp

    @date_time_stamp.setter
    def date_time_stamp(self, date_time_stamp):
        """Sets the date_time_stamp of this ODMcomplexTypeDefinitionSignature.


        :param date_time_stamp: The date_time_stamp of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :type: ODMcomplexTypeDefinitionDateTimeStamp
        """
        if self.local_vars_configuration.client_side_validation and date_time_stamp is None:  # noqa: E501
            raise ValueError("Invalid value for `date_time_stamp`, must not be `None`")  # noqa: E501

        self._date_time_stamp = date_time_stamp

    @property
    def crypto_binding_manifest(self):
        """Gets the crypto_binding_manifest of this ODMcomplexTypeDefinitionSignature.  # noqa: E501


        :return: The crypto_binding_manifest of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionCryptoBindingManifest
        """
        return self._crypto_binding_manifest

    @crypto_binding_manifest.setter
    def crypto_binding_manifest(self, crypto_binding_manifest):
        """Sets the crypto_binding_manifest of this ODMcomplexTypeDefinitionSignature.


        :param crypto_binding_manifest: The crypto_binding_manifest of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :type: ODMcomplexTypeDefinitionCryptoBindingManifest
        """

        self._crypto_binding_manifest = crypto_binding_manifest

    @property
    def id(self):
        """Gets the id of this ODMcomplexTypeDefinitionSignature.  # noqa: E501


        :return: The id of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ODMcomplexTypeDefinitionSignature.


        :param id: The id of this ODMcomplexTypeDefinitionSignature.  # noqa: E501
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
        if not isinstance(other, ODMcomplexTypeDefinitionSignature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionSignature):
            return True

        return self.to_dict() != other.to_dict()