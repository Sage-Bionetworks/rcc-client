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


class ODMcomplexTypeDefinitionCodeList(object):
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
        'description': 'ODMcomplexTypeDefinitionDescription',
        'code_list_item': 'list[ODMcomplexTypeDefinitionCodeListItem]',
        'external_code_list': 'ODMcomplexTypeDefinitionExternalCodeList',
        'enumerated_item': 'list[ODMcomplexTypeDefinitionEnumeratedItem]',
        'alias': 'list[ODMcomplexTypeDefinitionAlias]',
        'oid': 'str',
        'name': 'str',
        'data_type': 'str',
        'label': 'str',
        'form_oid': 'str',
        'response_type': 'str',
        'hidden': 'bool',
        'is_global': 'bool',
        'sasformat_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'code_list_item': 'codeListItem',
        'external_code_list': 'externalCodeList',
        'enumerated_item': 'enumeratedItem',
        'alias': 'alias',
        'oid': 'oid',
        'name': 'name',
        'data_type': 'dataType',
        'label': 'label',
        'form_oid': 'formOID',
        'response_type': 'responseType',
        'hidden': 'hidden',
        'is_global': 'isGlobal',
        'sasformat_name': 'sasformatName'
    }

    def __init__(self, description=None, code_list_item=None, external_code_list=None, enumerated_item=None, alias=None, oid=None, name=None, data_type=None, label=None, form_oid=None, response_type=None, hidden=None, is_global=None, sasformat_name=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionCodeList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._code_list_item = None
        self._external_code_list = None
        self._enumerated_item = None
        self._alias = None
        self._oid = None
        self._name = None
        self._data_type = None
        self._label = None
        self._form_oid = None
        self._response_type = None
        self._hidden = None
        self._is_global = None
        self._sasformat_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if code_list_item is not None:
            self.code_list_item = code_list_item
        if external_code_list is not None:
            self.external_code_list = external_code_list
        if enumerated_item is not None:
            self.enumerated_item = enumerated_item
        if alias is not None:
            self.alias = alias
        if oid is not None:
            self.oid = oid
        if name is not None:
            self.name = name
        if data_type is not None:
            self.data_type = data_type
        if label is not None:
            self.label = label
        if form_oid is not None:
            self.form_oid = form_oid
        if response_type is not None:
            self.response_type = response_type
        if hidden is not None:
            self.hidden = hidden
        if is_global is not None:
            self.is_global = is_global
        if sasformat_name is not None:
            self.sasformat_name = sasformat_name

    @property
    def description(self):
        """Gets the description of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The description of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ODMcomplexTypeDefinitionCodeList.


        :param description: The description of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: ODMcomplexTypeDefinitionDescription
        """

        self._description = description

    @property
    def code_list_item(self):
        """Gets the code_list_item of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The code_list_item of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionCodeListItem]
        """
        return self._code_list_item

    @code_list_item.setter
    def code_list_item(self, code_list_item):
        """Sets the code_list_item of this ODMcomplexTypeDefinitionCodeList.


        :param code_list_item: The code_list_item of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionCodeListItem]
        """

        self._code_list_item = code_list_item

    @property
    def external_code_list(self):
        """Gets the external_code_list of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The external_code_list of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionExternalCodeList
        """
        return self._external_code_list

    @external_code_list.setter
    def external_code_list(self, external_code_list):
        """Sets the external_code_list of this ODMcomplexTypeDefinitionCodeList.


        :param external_code_list: The external_code_list of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: ODMcomplexTypeDefinitionExternalCodeList
        """

        self._external_code_list = external_code_list

    @property
    def enumerated_item(self):
        """Gets the enumerated_item of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The enumerated_item of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionEnumeratedItem]
        """
        return self._enumerated_item

    @enumerated_item.setter
    def enumerated_item(self, enumerated_item):
        """Sets the enumerated_item of this ODMcomplexTypeDefinitionCodeList.


        :param enumerated_item: The enumerated_item of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionEnumeratedItem]
        """

        self._enumerated_item = enumerated_item

    @property
    def alias(self):
        """Gets the alias of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The alias of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ODMcomplexTypeDefinitionCodeList.


        :param alias: The alias of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAlias]
        """

        self._alias = alias

    @property
    def oid(self):
        """Gets the oid of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The oid of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this ODMcomplexTypeDefinitionCodeList.


        :param oid: The oid of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def name(self):
        """Gets the name of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The name of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ODMcomplexTypeDefinitionCodeList.


        :param name: The name of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The data_type of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ODMcomplexTypeDefinitionCodeList.


        :param data_type: The data_type of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTEGER", "FLOAT", "TEXT", "STRING"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def label(self):
        """Gets the label of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The label of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ODMcomplexTypeDefinitionCodeList.


        :param label: The label of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def form_oid(self):
        """Gets the form_oid of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The form_oid of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._form_oid

    @form_oid.setter
    def form_oid(self, form_oid):
        """Sets the form_oid of this ODMcomplexTypeDefinitionCodeList.


        :param form_oid: The form_oid of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """

        self._form_oid = form_oid

    @property
    def response_type(self):
        """Gets the response_type of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The response_type of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this ODMcomplexTypeDefinitionCodeList.


        :param response_type: The response_type of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """

        self._response_type = response_type

    @property
    def hidden(self):
        """Gets the hidden of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The hidden of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ODMcomplexTypeDefinitionCodeList.


        :param hidden: The hidden of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def is_global(self):
        """Gets the is_global of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The is_global of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: bool
        """
        return self._is_global

    @is_global.setter
    def is_global(self, is_global):
        """Sets the is_global of this ODMcomplexTypeDefinitionCodeList.


        :param is_global: The is_global of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: bool
        """

        self._is_global = is_global

    @property
    def sasformat_name(self):
        """Gets the sasformat_name of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501


        :return: The sasformat_name of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :rtype: str
        """
        return self._sasformat_name

    @sasformat_name.setter
    def sasformat_name(self, sasformat_name):
        """Sets the sasformat_name of this ODMcomplexTypeDefinitionCodeList.


        :param sasformat_name: The sasformat_name of this ODMcomplexTypeDefinitionCodeList.  # noqa: E501
        :type: str
        """

        self._sasformat_name = sasformat_name

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
        if not isinstance(other, ODMcomplexTypeDefinitionCodeList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionCodeList):
            return True

        return self.to_dict() != other.to_dict()
