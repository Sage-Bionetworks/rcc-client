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


class ODMcomplexTypeDefinitionItemGroupData(object):
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
        'audit_record': 'ODMcomplexTypeDefinitionAuditRecord',
        'signature': 'ODMcomplexTypeDefinitionSignature',
        'annotation': 'list[ODMcomplexTypeDefinitionAnnotation]',
        'item_data_group': 'list[ODMcomplexTypeDefinitionItemData]',
        'item_data_star_group': 'list[object]',
        'item_group_oid': 'str',
        'item_group_repeat_key': 'str',
        'transaction_type': 'str'
    }

    attribute_map = {
        'audit_record': 'auditRecord',
        'signature': 'signature',
        'annotation': 'annotation',
        'item_data_group': 'itemDataGroup',
        'item_data_star_group': 'itemDataStarGroup',
        'item_group_oid': 'itemGroupOID',
        'item_group_repeat_key': 'itemGroupRepeatKey',
        'transaction_type': 'transactionType'
    }

    def __init__(self, audit_record=None, signature=None, annotation=None, item_data_group=None, item_data_star_group=None, item_group_oid=None, item_group_repeat_key=None, transaction_type=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionItemGroupData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audit_record = None
        self._signature = None
        self._annotation = None
        self._item_data_group = None
        self._item_data_star_group = None
        self._item_group_oid = None
        self._item_group_repeat_key = None
        self._transaction_type = None
        self.discriminator = None

        if audit_record is not None:
            self.audit_record = audit_record
        if signature is not None:
            self.signature = signature
        if annotation is not None:
            self.annotation = annotation
        if item_data_group is not None:
            self.item_data_group = item_data_group
        if item_data_star_group is not None:
            self.item_data_star_group = item_data_star_group
        if item_group_oid is not None:
            self.item_group_oid = item_group_oid
        if item_group_repeat_key is not None:
            self.item_group_repeat_key = item_group_repeat_key
        if transaction_type is not None:
            self.transaction_type = transaction_type

    @property
    def audit_record(self):
        """Gets the audit_record of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The audit_record of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionAuditRecord
        """
        return self._audit_record

    @audit_record.setter
    def audit_record(self, audit_record):
        """Sets the audit_record of this ODMcomplexTypeDefinitionItemGroupData.


        :param audit_record: The audit_record of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: ODMcomplexTypeDefinitionAuditRecord
        """

        self._audit_record = audit_record

    @property
    def signature(self):
        """Gets the signature of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The signature of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionSignature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ODMcomplexTypeDefinitionItemGroupData.


        :param signature: The signature of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: ODMcomplexTypeDefinitionSignature
        """

        self._signature = signature

    @property
    def annotation(self):
        """Gets the annotation of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The annotation of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAnnotation]
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this ODMcomplexTypeDefinitionItemGroupData.


        :param annotation: The annotation of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAnnotation]
        """

        self._annotation = annotation

    @property
    def item_data_group(self):
        """Gets the item_data_group of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The item_data_group of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionItemData]
        """
        return self._item_data_group

    @item_data_group.setter
    def item_data_group(self, item_data_group):
        """Sets the item_data_group of this ODMcomplexTypeDefinitionItemGroupData.


        :param item_data_group: The item_data_group of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionItemData]
        """

        self._item_data_group = item_data_group

    @property
    def item_data_star_group(self):
        """Gets the item_data_star_group of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The item_data_star_group of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: list[object]
        """
        return self._item_data_star_group

    @item_data_star_group.setter
    def item_data_star_group(self, item_data_star_group):
        """Sets the item_data_star_group of this ODMcomplexTypeDefinitionItemGroupData.


        :param item_data_star_group: The item_data_star_group of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: list[object]
        """

        self._item_data_star_group = item_data_star_group

    @property
    def item_group_oid(self):
        """Gets the item_group_oid of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The item_group_oid of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: str
        """
        return self._item_group_oid

    @item_group_oid.setter
    def item_group_oid(self, item_group_oid):
        """Sets the item_group_oid of this ODMcomplexTypeDefinitionItemGroupData.


        :param item_group_oid: The item_group_oid of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: str
        """

        self._item_group_oid = item_group_oid

    @property
    def item_group_repeat_key(self):
        """Gets the item_group_repeat_key of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The item_group_repeat_key of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: str
        """
        return self._item_group_repeat_key

    @item_group_repeat_key.setter
    def item_group_repeat_key(self, item_group_repeat_key):
        """Sets the item_group_repeat_key of this ODMcomplexTypeDefinitionItemGroupData.


        :param item_group_repeat_key: The item_group_repeat_key of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: str
        """

        self._item_group_repeat_key = item_group_repeat_key

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501


        :return: The transaction_type of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ODMcomplexTypeDefinitionItemGroupData.


        :param transaction_type: The transaction_type of this ODMcomplexTypeDefinitionItemGroupData.  # noqa: E501
        :type: str
        """
        allowed_values = ["INSERT", "UPDATE", "REMOVE", "UPSERT", "CONTEXT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and transaction_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `transaction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transaction_type, allowed_values)
            )

        self._transaction_type = transaction_type

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
        if not isinstance(other, ODMcomplexTypeDefinitionItemGroupData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionItemGroupData):
            return True

        return self.to_dict() != other.to_dict()
