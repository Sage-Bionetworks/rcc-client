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


class ODMcomplexTypeDefinitionStudyEventRef(object):
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
        'study_event_oid': 'str',
        'order_number': 'int',
        'mandatory': 'str',
        'collection_exception_condition_oid': 'str'
    }

    attribute_map = {
        'study_event_oid': 'studyEventOID',
        'order_number': 'orderNumber',
        'mandatory': 'mandatory',
        'collection_exception_condition_oid': 'collectionExceptionConditionOID'
    }

    def __init__(self, study_event_oid=None, order_number=None, mandatory=None, collection_exception_condition_oid=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionStudyEventRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_event_oid = None
        self._order_number = None
        self._mandatory = None
        self._collection_exception_condition_oid = None
        self.discriminator = None

        if study_event_oid is not None:
            self.study_event_oid = study_event_oid
        if order_number is not None:
            self.order_number = order_number
        if mandatory is not None:
            self.mandatory = mandatory
        if collection_exception_condition_oid is not None:
            self.collection_exception_condition_oid = collection_exception_condition_oid

    @property
    def study_event_oid(self):
        """Gets the study_event_oid of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501


        :return: The study_event_oid of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :rtype: str
        """
        return self._study_event_oid

    @study_event_oid.setter
    def study_event_oid(self, study_event_oid):
        """Sets the study_event_oid of this ODMcomplexTypeDefinitionStudyEventRef.


        :param study_event_oid: The study_event_oid of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :type: str
        """

        self._study_event_oid = study_event_oid

    @property
    def order_number(self):
        """Gets the order_number of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501


        :return: The order_number of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this ODMcomplexTypeDefinitionStudyEventRef.


        :param order_number: The order_number of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :type: int
        """

        self._order_number = order_number

    @property
    def mandatory(self):
        """Gets the mandatory of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501


        :return: The mandatory of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :rtype: str
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this ODMcomplexTypeDefinitionStudyEventRef.


        :param mandatory: The mandatory of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mandatory not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mandatory` ({0}), must be one of {1}"  # noqa: E501
                .format(mandatory, allowed_values)
            )

        self._mandatory = mandatory

    @property
    def collection_exception_condition_oid(self):
        """Gets the collection_exception_condition_oid of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501


        :return: The collection_exception_condition_oid of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :rtype: str
        """
        return self._collection_exception_condition_oid

    @collection_exception_condition_oid.setter
    def collection_exception_condition_oid(self, collection_exception_condition_oid):
        """Sets the collection_exception_condition_oid of this ODMcomplexTypeDefinitionStudyEventRef.


        :param collection_exception_condition_oid: The collection_exception_condition_oid of this ODMcomplexTypeDefinitionStudyEventRef.  # noqa: E501
        :type: str
        """

        self._collection_exception_condition_oid = collection_exception_condition_oid

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
        if not isinstance(other, ODMcomplexTypeDefinitionStudyEventRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionStudyEventRef):
            return True

        return self.to_dict() != other.to_dict()
