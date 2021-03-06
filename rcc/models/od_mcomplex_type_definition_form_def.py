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


class ODMcomplexTypeDefinitionFormDef(object):
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
        'item_group_ref': 'list[ODMcomplexTypeDefinitionItemGroupRef]',
        'archive_layout': 'list[ODMcomplexTypeDefinitionArchiveLayout]',
        'alias': 'list[ODMcomplexTypeDefinitionAlias]',
        'oid': 'str',
        'name': 'str',
        'repeating': 'str',
        'available_crf_languages': 'AvailableCrfLanguages',
        'language_labels': 'LanguageLabels',
        'crfform_version_definition': 'CRFFormVersionDefinition'
    }

    attribute_map = {
        'description': 'description',
        'item_group_ref': 'itemGroupRef',
        'archive_layout': 'archiveLayout',
        'alias': 'alias',
        'oid': 'oid',
        'name': 'name',
        'repeating': 'repeating',
        'available_crf_languages': 'availableCrfLanguages',
        'language_labels': 'languageLabels',
        'crfform_version_definition': 'crfformVersionDefinition'
    }

    def __init__(self, description=None, item_group_ref=None, archive_layout=None, alias=None, oid=None, name=None, repeating=None, available_crf_languages=None, language_labels=None, crfform_version_definition=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionFormDef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._item_group_ref = None
        self._archive_layout = None
        self._alias = None
        self._oid = None
        self._name = None
        self._repeating = None
        self._available_crf_languages = None
        self._language_labels = None
        self._crfform_version_definition = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if item_group_ref is not None:
            self.item_group_ref = item_group_ref
        if archive_layout is not None:
            self.archive_layout = archive_layout
        if alias is not None:
            self.alias = alias
        if oid is not None:
            self.oid = oid
        if name is not None:
            self.name = name
        if repeating is not None:
            self.repeating = repeating
        self.available_crf_languages = available_crf_languages
        self.language_labels = language_labels
        if crfform_version_definition is not None:
            self.crfform_version_definition = crfform_version_definition

    @property
    def description(self):
        """Gets the description of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The description of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ODMcomplexTypeDefinitionFormDef.


        :param description: The description of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: ODMcomplexTypeDefinitionDescription
        """

        self._description = description

    @property
    def item_group_ref(self):
        """Gets the item_group_ref of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The item_group_ref of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionItemGroupRef]
        """
        return self._item_group_ref

    @item_group_ref.setter
    def item_group_ref(self, item_group_ref):
        """Sets the item_group_ref of this ODMcomplexTypeDefinitionFormDef.


        :param item_group_ref: The item_group_ref of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionItemGroupRef]
        """

        self._item_group_ref = item_group_ref

    @property
    def archive_layout(self):
        """Gets the archive_layout of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The archive_layout of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionArchiveLayout]
        """
        return self._archive_layout

    @archive_layout.setter
    def archive_layout(self, archive_layout):
        """Sets the archive_layout of this ODMcomplexTypeDefinitionFormDef.


        :param archive_layout: The archive_layout of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionArchiveLayout]
        """

        self._archive_layout = archive_layout

    @property
    def alias(self):
        """Gets the alias of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The alias of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAlias]
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ODMcomplexTypeDefinitionFormDef.


        :param alias: The alias of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAlias]
        """

        self._alias = alias

    @property
    def oid(self):
        """Gets the oid of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The oid of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this ODMcomplexTypeDefinitionFormDef.


        :param oid: The oid of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def name(self):
        """Gets the name of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The name of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ODMcomplexTypeDefinitionFormDef.


        :param name: The name of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def repeating(self):
        """Gets the repeating of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The repeating of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: str
        """
        return self._repeating

    @repeating.setter
    def repeating(self, repeating):
        """Sets the repeating of this ODMcomplexTypeDefinitionFormDef.


        :param repeating: The repeating of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and repeating not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `repeating` ({0}), must be one of {1}"  # noqa: E501
                .format(repeating, allowed_values)
            )

        self._repeating = repeating

    @property
    def available_crf_languages(self):
        """Gets the available_crf_languages of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The available_crf_languages of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: AvailableCrfLanguages
        """
        return self._available_crf_languages

    @available_crf_languages.setter
    def available_crf_languages(self, available_crf_languages):
        """Sets the available_crf_languages of this ODMcomplexTypeDefinitionFormDef.


        :param available_crf_languages: The available_crf_languages of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: AvailableCrfLanguages
        """
        if self.local_vars_configuration.client_side_validation and available_crf_languages is None:  # noqa: E501
            raise ValueError("Invalid value for `available_crf_languages`, must not be `None`")  # noqa: E501

        self._available_crf_languages = available_crf_languages

    @property
    def language_labels(self):
        """Gets the language_labels of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The language_labels of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: LanguageLabels
        """
        return self._language_labels

    @language_labels.setter
    def language_labels(self, language_labels):
        """Sets the language_labels of this ODMcomplexTypeDefinitionFormDef.


        :param language_labels: The language_labels of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: LanguageLabels
        """
        if self.local_vars_configuration.client_side_validation and language_labels is None:  # noqa: E501
            raise ValueError("Invalid value for `language_labels`, must not be `None`")  # noqa: E501

        self._language_labels = language_labels

    @property
    def crfform_version_definition(self):
        """Gets the crfform_version_definition of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501


        :return: The crfform_version_definition of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :rtype: CRFFormVersionDefinition
        """
        return self._crfform_version_definition

    @crfform_version_definition.setter
    def crfform_version_definition(self, crfform_version_definition):
        """Sets the crfform_version_definition of this ODMcomplexTypeDefinitionFormDef.


        :param crfform_version_definition: The crfform_version_definition of this ODMcomplexTypeDefinitionFormDef.  # noqa: E501
        :type: CRFFormVersionDefinition
        """

        self._crfform_version_definition = crfform_version_definition

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
        if not isinstance(other, ODMcomplexTypeDefinitionFormDef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionFormDef):
            return True

        return self.to_dict() != other.to_dict()
