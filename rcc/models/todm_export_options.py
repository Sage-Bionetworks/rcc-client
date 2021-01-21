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


class TodmExportOptions(object):
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
        'subjects': 'list[str]',
        'events': 'list[str]',
        'crf_forms': 'list[str]',
        'crf_versions': 'list[str]',
        'sites': 'list[str]',
        'date_from': 'str',
        'date_to': 'str'
    }

    attribute_map = {
        'study_site_id': 'studySiteId',
        'subjects': 'subjects',
        'events': 'events',
        'crf_forms': 'crfForms',
        'crf_versions': 'crfVersions',
        'sites': 'sites',
        'date_from': 'dateFrom',
        'date_to': 'dateTo'
    }

    def __init__(self, study_site_id=None, subjects=None, events=None, crf_forms=None, crf_versions=None, sites=None, date_from=None, date_to=None, local_vars_configuration=None):  # noqa: E501
        """TodmExportOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._study_site_id = None
        self._subjects = None
        self._events = None
        self._crf_forms = None
        self._crf_versions = None
        self._sites = None
        self._date_from = None
        self._date_to = None
        self.discriminator = None

        if study_site_id is not None:
            self.study_site_id = study_site_id
        if subjects is not None:
            self.subjects = subjects
        if events is not None:
            self.events = events
        if crf_forms is not None:
            self.crf_forms = crf_forms
        if crf_versions is not None:
            self.crf_versions = crf_versions
        if sites is not None:
            self.sites = sites
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to

    @property
    def study_site_id(self):
        """Gets the study_site_id of this TodmExportOptions.  # noqa: E501


        :return: The study_site_id of this TodmExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._study_site_id

    @study_site_id.setter
    def study_site_id(self, study_site_id):
        """Sets the study_site_id of this TodmExportOptions.


        :param study_site_id: The study_site_id of this TodmExportOptions.  # noqa: E501
        :type: int
        """

        self._study_site_id = study_site_id

    @property
    def subjects(self):
        """Gets the subjects of this TodmExportOptions.  # noqa: E501


        :return: The subjects of this TodmExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this TodmExportOptions.


        :param subjects: The subjects of this TodmExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._subjects = subjects

    @property
    def events(self):
        """Gets the events of this TodmExportOptions.  # noqa: E501


        :return: The events of this TodmExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this TodmExportOptions.


        :param events: The events of this TodmExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def crf_forms(self):
        """Gets the crf_forms of this TodmExportOptions.  # noqa: E501


        :return: The crf_forms of this TodmExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._crf_forms

    @crf_forms.setter
    def crf_forms(self, crf_forms):
        """Sets the crf_forms of this TodmExportOptions.


        :param crf_forms: The crf_forms of this TodmExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._crf_forms = crf_forms

    @property
    def crf_versions(self):
        """Gets the crf_versions of this TodmExportOptions.  # noqa: E501


        :return: The crf_versions of this TodmExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._crf_versions

    @crf_versions.setter
    def crf_versions(self, crf_versions):
        """Sets the crf_versions of this TodmExportOptions.


        :param crf_versions: The crf_versions of this TodmExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._crf_versions = crf_versions

    @property
    def sites(self):
        """Gets the sites of this TodmExportOptions.  # noqa: E501


        :return: The sites of this TodmExportOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this TodmExportOptions.


        :param sites: The sites of this TodmExportOptions.  # noqa: E501
        :type: list[str]
        """

        self._sites = sites

    @property
    def date_from(self):
        """Gets the date_from of this TodmExportOptions.  # noqa: E501


        :return: The date_from of this TodmExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this TodmExportOptions.


        :param date_from: The date_from of this TodmExportOptions.  # noqa: E501
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this TodmExportOptions.  # noqa: E501


        :return: The date_to of this TodmExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this TodmExportOptions.


        :param date_to: The date_to of this TodmExportOptions.  # noqa: E501
        :type: str
        """

        self._date_to = date_to

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
        if not isinstance(other, TodmExportOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TodmExportOptions):
            return True

        return self.to_dict() != other.to_dict()