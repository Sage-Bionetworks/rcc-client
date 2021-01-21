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


class ODMcomplexTypeDefinitionMetaDataVersionRef(object):
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
        'study_oid': 'str',
        'meta_data_version_oid': 'str',
        'effective_date': 'datetime'
    }

    attribute_map = {
        'study_oid': 'studyOID',
        'meta_data_version_oid': 'metaDataVersionOID',
        'effective_date': 'effectiveDate'
    }

    def __init__(self, study_oid=None, meta_data_version_oid=None, effective_date=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionMetaDataVersionRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_oid = None
        self._meta_data_version_oid = None
        self._effective_date = None
        self.discriminator = None

        if study_oid is not None:
            self.study_oid = study_oid
        if meta_data_version_oid is not None:
            self.meta_data_version_oid = meta_data_version_oid
        if effective_date is not None:
            self.effective_date = effective_date

    @property
    def study_oid(self):
        """Gets the study_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501


        :return: The study_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501
        :rtype: str
        """
        return self._study_oid

    @study_oid.setter
    def study_oid(self, study_oid):
        """Sets the study_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.


        :param study_oid: The study_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501
        :type: str
        """

        self._study_oid = study_oid

    @property
    def meta_data_version_oid(self):
        """Gets the meta_data_version_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501


        :return: The meta_data_version_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501
        :rtype: str
        """
        return self._meta_data_version_oid

    @meta_data_version_oid.setter
    def meta_data_version_oid(self, meta_data_version_oid):
        """Sets the meta_data_version_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.


        :param meta_data_version_oid: The meta_data_version_oid of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501
        :type: str
        """

        self._meta_data_version_oid = meta_data_version_oid

    @property
    def effective_date(self):
        """Gets the effective_date of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501


        :return: The effective_date of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ODMcomplexTypeDefinitionMetaDataVersionRef.


        :param effective_date: The effective_date of this ODMcomplexTypeDefinitionMetaDataVersionRef.  # noqa: E501
        :type: datetime
        """

        self._effective_date = effective_date

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
        if not isinstance(other, ODMcomplexTypeDefinitionMetaDataVersionRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionMetaDataVersionRef):
            return True

        return self.to_dict() != other.to_dict()
