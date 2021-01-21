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


class EventCrfsRpc(object):
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
        'study_event_id': 'int',
        'crf_version_id': 'int',
        'crf_id': 'int',
        'subject_id': 'int',
        'event_definition_crf_id': 'int',
        'event_definition_id': 'int',
        'status_id': 'int',
        'status_code': 'str',
        'crf_sequence': 'int',
        'event_sequence': 'int',
        'event_occurence': 'int',
        'crf_occurence': 'int'
    }

    attribute_map = {
        'id': 'id',
        'study_event_id': 'studyEventId',
        'crf_version_id': 'crfVersionId',
        'crf_id': 'crfId',
        'subject_id': 'subjectId',
        'event_definition_crf_id': 'eventDefinitionCrfId',
        'event_definition_id': 'eventDefinitionId',
        'status_id': 'statusId',
        'status_code': 'statusCode',
        'crf_sequence': 'crfSequence',
        'event_sequence': 'eventSequence',
        'event_occurence': 'eventOccurence',
        'crf_occurence': 'crfOccurence'
    }

    def __init__(self, id=None, study_event_id=None, crf_version_id=None, crf_id=None, subject_id=None, event_definition_crf_id=None, event_definition_id=None, status_id=None, status_code=None, crf_sequence=None, event_sequence=None, event_occurence=None, crf_occurence=None, local_vars_configuration=None):  # noqa: E501
        """EventCrfsRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._study_event_id = None
        self._crf_version_id = None
        self._crf_id = None
        self._subject_id = None
        self._event_definition_crf_id = None
        self._event_definition_id = None
        self._status_id = None
        self._status_code = None
        self._crf_sequence = None
        self._event_sequence = None
        self._event_occurence = None
        self._crf_occurence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if study_event_id is not None:
            self.study_event_id = study_event_id
        if crf_version_id is not None:
            self.crf_version_id = crf_version_id
        if crf_id is not None:
            self.crf_id = crf_id
        if subject_id is not None:
            self.subject_id = subject_id
        if event_definition_crf_id is not None:
            self.event_definition_crf_id = event_definition_crf_id
        if event_definition_id is not None:
            self.event_definition_id = event_definition_id
        if status_id is not None:
            self.status_id = status_id
        if status_code is not None:
            self.status_code = status_code
        if crf_sequence is not None:
            self.crf_sequence = crf_sequence
        if event_sequence is not None:
            self.event_sequence = event_sequence
        if event_occurence is not None:
            self.event_occurence = event_occurence
        if crf_occurence is not None:
            self.crf_occurence = crf_occurence

    @property
    def id(self):
        """Gets the id of this EventCrfsRpc.  # noqa: E501


        :return: The id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventCrfsRpc.


        :param id: The id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def study_event_id(self):
        """Gets the study_event_id of this EventCrfsRpc.  # noqa: E501


        :return: The study_event_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_event_id

    @study_event_id.setter
    def study_event_id(self, study_event_id):
        """Sets the study_event_id of this EventCrfsRpc.


        :param study_event_id: The study_event_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._study_event_id = study_event_id

    @property
    def crf_version_id(self):
        """Gets the crf_version_id of this EventCrfsRpc.  # noqa: E501


        :return: The crf_version_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_version_id

    @crf_version_id.setter
    def crf_version_id(self, crf_version_id):
        """Sets the crf_version_id of this EventCrfsRpc.


        :param crf_version_id: The crf_version_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._crf_version_id = crf_version_id

    @property
    def crf_id(self):
        """Gets the crf_id of this EventCrfsRpc.  # noqa: E501


        :return: The crf_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_id

    @crf_id.setter
    def crf_id(self, crf_id):
        """Sets the crf_id of this EventCrfsRpc.


        :param crf_id: The crf_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._crf_id = crf_id

    @property
    def subject_id(self):
        """Gets the subject_id of this EventCrfsRpc.  # noqa: E501


        :return: The subject_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this EventCrfsRpc.


        :param subject_id: The subject_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._subject_id = subject_id

    @property
    def event_definition_crf_id(self):
        """Gets the event_definition_crf_id of this EventCrfsRpc.  # noqa: E501


        :return: The event_definition_crf_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._event_definition_crf_id

    @event_definition_crf_id.setter
    def event_definition_crf_id(self, event_definition_crf_id):
        """Sets the event_definition_crf_id of this EventCrfsRpc.


        :param event_definition_crf_id: The event_definition_crf_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._event_definition_crf_id = event_definition_crf_id

    @property
    def event_definition_id(self):
        """Gets the event_definition_id of this EventCrfsRpc.  # noqa: E501


        :return: The event_definition_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._event_definition_id

    @event_definition_id.setter
    def event_definition_id(self, event_definition_id):
        """Sets the event_definition_id of this EventCrfsRpc.


        :param event_definition_id: The event_definition_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._event_definition_id = event_definition_id

    @property
    def status_id(self):
        """Gets the status_id of this EventCrfsRpc.  # noqa: E501


        :return: The status_id of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this EventCrfsRpc.


        :param status_id: The status_id of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._status_id = status_id

    @property
    def status_code(self):
        """Gets the status_code of this EventCrfsRpc.  # noqa: E501


        :return: The status_code of this EventCrfsRpc.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this EventCrfsRpc.


        :param status_code: The status_code of this EventCrfsRpc.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

    @property
    def crf_sequence(self):
        """Gets the crf_sequence of this EventCrfsRpc.  # noqa: E501


        :return: The crf_sequence of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_sequence

    @crf_sequence.setter
    def crf_sequence(self, crf_sequence):
        """Sets the crf_sequence of this EventCrfsRpc.


        :param crf_sequence: The crf_sequence of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._crf_sequence = crf_sequence

    @property
    def event_sequence(self):
        """Gets the event_sequence of this EventCrfsRpc.  # noqa: E501


        :return: The event_sequence of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._event_sequence

    @event_sequence.setter
    def event_sequence(self, event_sequence):
        """Sets the event_sequence of this EventCrfsRpc.


        :param event_sequence: The event_sequence of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._event_sequence = event_sequence

    @property
    def event_occurence(self):
        """Gets the event_occurence of this EventCrfsRpc.  # noqa: E501


        :return: The event_occurence of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._event_occurence

    @event_occurence.setter
    def event_occurence(self, event_occurence):
        """Sets the event_occurence of this EventCrfsRpc.


        :param event_occurence: The event_occurence of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._event_occurence = event_occurence

    @property
    def crf_occurence(self):
        """Gets the crf_occurence of this EventCrfsRpc.  # noqa: E501


        :return: The crf_occurence of this EventCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_occurence

    @crf_occurence.setter
    def crf_occurence(self, crf_occurence):
        """Sets the crf_occurence of this EventCrfsRpc.


        :param crf_occurence: The crf_occurence of this EventCrfsRpc.  # noqa: E501
        :type: int
        """

        self._crf_occurence = crf_occurence

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
        if not isinstance(other, EventCrfsRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventCrfsRpc):
            return True

        return self.to_dict() != other.to_dict()
