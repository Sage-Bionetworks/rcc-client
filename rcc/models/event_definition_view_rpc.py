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


class EventDefinitionViewRpc(object):
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
        'id': 'int',
        'study_id': 'int',
        'name': 'str',
        'unique_event_name': 'str',
        'repeating': 'bool',
        'create_date': 'int',
        'update_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'study_id': 'studyId',
        'name': 'name',
        'unique_event_name': 'uniqueEventName',
        'repeating': 'repeating',
        'create_date': 'createDate',
        'update_date': 'updateDate'
    }

    def __init__(self, id=None, study_id=None, name=None, unique_event_name=None, repeating=None, create_date=None, update_date=None, local_vars_configuration=None):  # noqa: E501
        """EventDefinitionViewRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._study_id = None
        self._name = None
        self._unique_event_name = None
        self._repeating = None
        self._create_date = None
        self._update_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if study_id is not None:
            self.study_id = study_id
        if name is not None:
            self.name = name
        if unique_event_name is not None:
            self.unique_event_name = unique_event_name
        if repeating is not None:
            self.repeating = repeating
        if create_date is not None:
            self.create_date = create_date
        if update_date is not None:
            self.update_date = update_date

    @property
    def id(self):
        """Gets the id of this EventDefinitionViewRpc.  # noqa: E501


        :return: The id of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventDefinitionViewRpc.


        :param id: The id of this EventDefinitionViewRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def study_id(self):
        """Gets the study_id of this EventDefinitionViewRpc.  # noqa: E501


        :return: The study_id of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this EventDefinitionViewRpc.


        :param study_id: The study_id of this EventDefinitionViewRpc.  # noqa: E501
        :type: int
        """

        self._study_id = study_id

    @property
    def name(self):
        """Gets the name of this EventDefinitionViewRpc.  # noqa: E501


        :return: The name of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventDefinitionViewRpc.


        :param name: The name of this EventDefinitionViewRpc.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unique_event_name(self):
        """Gets the unique_event_name of this EventDefinitionViewRpc.  # noqa: E501


        :return: The unique_event_name of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._unique_event_name

    @unique_event_name.setter
    def unique_event_name(self, unique_event_name):
        """Sets the unique_event_name of this EventDefinitionViewRpc.


        :param unique_event_name: The unique_event_name of this EventDefinitionViewRpc.  # noqa: E501
        :type: str
        """

        self._unique_event_name = unique_event_name

    @property
    def repeating(self):
        """Gets the repeating of this EventDefinitionViewRpc.  # noqa: E501


        :return: The repeating of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: bool
        """
        return self._repeating

    @repeating.setter
    def repeating(self, repeating):
        """Sets the repeating of this EventDefinitionViewRpc.


        :param repeating: The repeating of this EventDefinitionViewRpc.  # noqa: E501
        :type: bool
        """

        self._repeating = repeating

    @property
    def create_date(self):
        """Gets the create_date of this EventDefinitionViewRpc.  # noqa: E501


        :return: The create_date of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this EventDefinitionViewRpc.


        :param create_date: The create_date of this EventDefinitionViewRpc.  # noqa: E501
        :type: int
        """

        self._create_date = create_date

    @property
    def update_date(self):
        """Gets the update_date of this EventDefinitionViewRpc.  # noqa: E501


        :return: The update_date of this EventDefinitionViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EventDefinitionViewRpc.


        :param update_date: The update_date of this EventDefinitionViewRpc.  # noqa: E501
        :type: int
        """

        self._update_date = update_date

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
        if not isinstance(other, EventDefinitionViewRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventDefinitionViewRpc):
            return True

        return self.to_dict() != other.to_dict()
