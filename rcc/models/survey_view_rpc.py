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


class SurveyViewRpc(object):
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
        'title': 'str',
        'enabled': 'bool',
        'crf_id': 'int',
        'study_id': 'int',
        'crf_name': 'str',
        'survey_expiration': 'int',
        'survey_scheduler_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'enabled': 'enabled',
        'crf_id': 'crfId',
        'study_id': 'studyId',
        'crf_name': 'crfName',
        'survey_expiration': 'surveyExpiration',
        'survey_scheduler_id': 'surveySchedulerId'
    }

    def __init__(self, id=None, title=None, enabled=None, crf_id=None, study_id=None, crf_name=None, survey_expiration=None, survey_scheduler_id=None, local_vars_configuration=None):  # noqa: E501
        """SurveyViewRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._enabled = None
        self._crf_id = None
        self._study_id = None
        self._crf_name = None
        self._survey_expiration = None
        self._survey_scheduler_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if enabled is not None:
            self.enabled = enabled
        if crf_id is not None:
            self.crf_id = crf_id
        if study_id is not None:
            self.study_id = study_id
        if crf_name is not None:
            self.crf_name = crf_name
        if survey_expiration is not None:
            self.survey_expiration = survey_expiration
        if survey_scheduler_id is not None:
            self.survey_scheduler_id = survey_scheduler_id

    @property
    def id(self):
        """Gets the id of this SurveyViewRpc.  # noqa: E501


        :return: The id of this SurveyViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SurveyViewRpc.


        :param id: The id of this SurveyViewRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this SurveyViewRpc.  # noqa: E501


        :return: The title of this SurveyViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SurveyViewRpc.


        :param title: The title of this SurveyViewRpc.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def enabled(self):
        """Gets the enabled of this SurveyViewRpc.  # noqa: E501


        :return: The enabled of this SurveyViewRpc.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SurveyViewRpc.


        :param enabled: The enabled of this SurveyViewRpc.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def crf_id(self):
        """Gets the crf_id of this SurveyViewRpc.  # noqa: E501


        :return: The crf_id of this SurveyViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_id

    @crf_id.setter
    def crf_id(self, crf_id):
        """Sets the crf_id of this SurveyViewRpc.


        :param crf_id: The crf_id of this SurveyViewRpc.  # noqa: E501
        :type: int
        """

        self._crf_id = crf_id

    @property
    def study_id(self):
        """Gets the study_id of this SurveyViewRpc.  # noqa: E501


        :return: The study_id of this SurveyViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this SurveyViewRpc.


        :param study_id: The study_id of this SurveyViewRpc.  # noqa: E501
        :type: int
        """

        self._study_id = study_id

    @property
    def crf_name(self):
        """Gets the crf_name of this SurveyViewRpc.  # noqa: E501


        :return: The crf_name of this SurveyViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._crf_name

    @crf_name.setter
    def crf_name(self, crf_name):
        """Sets the crf_name of this SurveyViewRpc.


        :param crf_name: The crf_name of this SurveyViewRpc.  # noqa: E501
        :type: str
        """

        self._crf_name = crf_name

    @property
    def survey_expiration(self):
        """Gets the survey_expiration of this SurveyViewRpc.  # noqa: E501


        :return: The survey_expiration of this SurveyViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._survey_expiration

    @survey_expiration.setter
    def survey_expiration(self, survey_expiration):
        """Sets the survey_expiration of this SurveyViewRpc.


        :param survey_expiration: The survey_expiration of this SurveyViewRpc.  # noqa: E501
        :type: int
        """

        self._survey_expiration = survey_expiration

    @property
    def survey_scheduler_id(self):
        """Gets the survey_scheduler_id of this SurveyViewRpc.  # noqa: E501


        :return: The survey_scheduler_id of this SurveyViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._survey_scheduler_id

    @survey_scheduler_id.setter
    def survey_scheduler_id(self, survey_scheduler_id):
        """Sets the survey_scheduler_id of this SurveyViewRpc.


        :param survey_scheduler_id: The survey_scheduler_id of this SurveyViewRpc.  # noqa: E501
        :type: int
        """

        self._survey_scheduler_id = survey_scheduler_id

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
        if not isinstance(other, SurveyViewRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SurveyViewRpc):
            return True

        return self.to_dict() != other.to_dict()
