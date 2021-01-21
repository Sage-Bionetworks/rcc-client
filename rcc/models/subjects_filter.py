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


class SubjectsFilter(object):
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
        'study_site_id': 'int',
        'subject_ids': 'list[int]',
        'subject_unique_ids': 'list[str]',
        'subject_randomization_ids': 'list[int]',
        'subject_screening_ids': 'list[str]',
        'start_date': 'int',
        'end_date': 'int'
    }

    attribute_map = {
        'study_site_id': 'studySiteId',
        'subject_ids': 'subjectIds',
        'subject_unique_ids': 'subjectUniqueIds',
        'subject_randomization_ids': 'subjectRandomizationIds',
        'subject_screening_ids': 'subjectScreeningIds',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, study_site_id=None, subject_ids=None, subject_unique_ids=None, subject_randomization_ids=None, subject_screening_ids=None, start_date=None, end_date=None, local_vars_configuration=None):  # noqa: E501
        """SubjectsFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_site_id = None
        self._subject_ids = None
        self._subject_unique_ids = None
        self._subject_randomization_ids = None
        self._subject_screening_ids = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if study_site_id is not None:
            self.study_site_id = study_site_id
        if subject_ids is not None:
            self.subject_ids = subject_ids
        if subject_unique_ids is not None:
            self.subject_unique_ids = subject_unique_ids
        if subject_randomization_ids is not None:
            self.subject_randomization_ids = subject_randomization_ids
        if subject_screening_ids is not None:
            self.subject_screening_ids = subject_screening_ids
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def study_site_id(self):
        """Gets the study_site_id of this SubjectsFilter.  # noqa: E501


        :return: The study_site_id of this SubjectsFilter.  # noqa: E501
        :rtype: int
        """
        return self._study_site_id

    @study_site_id.setter
    def study_site_id(self, study_site_id):
        """Sets the study_site_id of this SubjectsFilter.


        :param study_site_id: The study_site_id of this SubjectsFilter.  # noqa: E501
        :type: int
        """

        self._study_site_id = study_site_id

    @property
    def subject_ids(self):
        """Gets the subject_ids of this SubjectsFilter.  # noqa: E501


        :return: The subject_ids of this SubjectsFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._subject_ids

    @subject_ids.setter
    def subject_ids(self, subject_ids):
        """Sets the subject_ids of this SubjectsFilter.


        :param subject_ids: The subject_ids of this SubjectsFilter.  # noqa: E501
        :type: list[int]
        """

        self._subject_ids = subject_ids

    @property
    def subject_unique_ids(self):
        """Gets the subject_unique_ids of this SubjectsFilter.  # noqa: E501


        :return: The subject_unique_ids of this SubjectsFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_unique_ids

    @subject_unique_ids.setter
    def subject_unique_ids(self, subject_unique_ids):
        """Sets the subject_unique_ids of this SubjectsFilter.


        :param subject_unique_ids: The subject_unique_ids of this SubjectsFilter.  # noqa: E501
        :type: list[str]
        """

        self._subject_unique_ids = subject_unique_ids

    @property
    def subject_randomization_ids(self):
        """Gets the subject_randomization_ids of this SubjectsFilter.  # noqa: E501


        :return: The subject_randomization_ids of this SubjectsFilter.  # noqa: E501
        :rtype: list[int]
        """
        return self._subject_randomization_ids

    @subject_randomization_ids.setter
    def subject_randomization_ids(self, subject_randomization_ids):
        """Sets the subject_randomization_ids of this SubjectsFilter.


        :param subject_randomization_ids: The subject_randomization_ids of this SubjectsFilter.  # noqa: E501
        :type: list[int]
        """

        self._subject_randomization_ids = subject_randomization_ids

    @property
    def subject_screening_ids(self):
        """Gets the subject_screening_ids of this SubjectsFilter.  # noqa: E501


        :return: The subject_screening_ids of this SubjectsFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_screening_ids

    @subject_screening_ids.setter
    def subject_screening_ids(self, subject_screening_ids):
        """Sets the subject_screening_ids of this SubjectsFilter.


        :param subject_screening_ids: The subject_screening_ids of this SubjectsFilter.  # noqa: E501
        :type: list[str]
        """

        self._subject_screening_ids = subject_screening_ids

    @property
    def start_date(self):
        """Gets the start_date of this SubjectsFilter.  # noqa: E501


        :return: The start_date of this SubjectsFilter.  # noqa: E501
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SubjectsFilter.


        :param start_date: The start_date of this SubjectsFilter.  # noqa: E501
        :type: int
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SubjectsFilter.  # noqa: E501


        :return: The end_date of this SubjectsFilter.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SubjectsFilter.


        :param end_date: The end_date of this SubjectsFilter.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

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
        if not isinstance(other, SubjectsFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubjectsFilter):
            return True

        return self.to_dict() != other.to_dict()
