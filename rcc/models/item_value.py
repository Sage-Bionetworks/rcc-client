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


class ItemValue(object):
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
        'item_name': 'str',
        'item_value': 'str',
        'updated_by': 'str',
        'updated_date': 'str',
        'states_history': 'str',
        'started_by': 'str',
        'started_date': 'str',
        'completed_by': 'str',
        'completed_date': 'str',
        'crf_occurrence': 'int',
        'sdv': 'bool',
        'sdv_by': 'str',
        'sdv_date': 'str',
        'mrv': 'bool',
        'mrv_by': 'str',
        'mrv_date': 'str',
        'drv': 'bool',
        'drv_by': 'str',
        'drv_date': 'str',
        'response_set': 'ResponseSetRpc'
    }

    attribute_map = {
        'item_name': 'itemName',
        'item_value': 'itemValue',
        'updated_by': 'updatedBy',
        'updated_date': 'updatedDate',
        'states_history': 'statesHistory',
        'started_by': 'startedBy',
        'started_date': 'startedDate',
        'completed_by': 'completedBy',
        'completed_date': 'completedDate',
        'crf_occurrence': 'crfOccurrence',
        'sdv': 'sdv',
        'sdv_by': 'sdvBy',
        'sdv_date': 'sdvDate',
        'mrv': 'mrv',
        'mrv_by': 'mrvBy',
        'mrv_date': 'mrvDate',
        'drv': 'drv',
        'drv_by': 'drvBy',
        'drv_date': 'drvDate',
        'response_set': 'responseSet'
    }

    def __init__(self, item_name=None, item_value=None, updated_by=None, updated_date=None, states_history=None, started_by=None, started_date=None, completed_by=None, completed_date=None, crf_occurrence=None, sdv=None, sdv_by=None, sdv_date=None, mrv=None, mrv_by=None, mrv_date=None, drv=None, drv_by=None, drv_date=None, response_set=None, local_vars_configuration=None):  # noqa: E501
        """ItemValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._item_name = None
        self._item_value = None
        self._updated_by = None
        self._updated_date = None
        self._states_history = None
        self._started_by = None
        self._started_date = None
        self._completed_by = None
        self._completed_date = None
        self._crf_occurrence = None
        self._sdv = None
        self._sdv_by = None
        self._sdv_date = None
        self._mrv = None
        self._mrv_by = None
        self._mrv_date = None
        self._drv = None
        self._drv_by = None
        self._drv_date = None
        self._response_set = None
        self.discriminator = None

        if item_name is not None:
            self.item_name = item_name
        if item_value is not None:
            self.item_value = item_value
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_date is not None:
            self.updated_date = updated_date
        if states_history is not None:
            self.states_history = states_history
        if started_by is not None:
            self.started_by = started_by
        if started_date is not None:
            self.started_date = started_date
        if completed_by is not None:
            self.completed_by = completed_by
        if completed_date is not None:
            self.completed_date = completed_date
        if crf_occurrence is not None:
            self.crf_occurrence = crf_occurrence
        if sdv is not None:
            self.sdv = sdv
        if sdv_by is not None:
            self.sdv_by = sdv_by
        if sdv_date is not None:
            self.sdv_date = sdv_date
        if mrv is not None:
            self.mrv = mrv
        if mrv_by is not None:
            self.mrv_by = mrv_by
        if mrv_date is not None:
            self.mrv_date = mrv_date
        if drv is not None:
            self.drv = drv
        if drv_by is not None:
            self.drv_by = drv_by
        if drv_date is not None:
            self.drv_date = drv_date
        if response_set is not None:
            self.response_set = response_set

    @property
    def item_name(self):
        """Gets the item_name of this ItemValue.  # noqa: E501


        :return: The item_name of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """Sets the item_name of this ItemValue.


        :param item_name: The item_name of this ItemValue.  # noqa: E501
        :type: str
        """

        self._item_name = item_name

    @property
    def item_value(self):
        """Gets the item_value of this ItemValue.  # noqa: E501


        :return: The item_value of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._item_value

    @item_value.setter
    def item_value(self, item_value):
        """Sets the item_value of this ItemValue.


        :param item_value: The item_value of this ItemValue.  # noqa: E501
        :type: str
        """

        self._item_value = item_value

    @property
    def updated_by(self):
        """Gets the updated_by of this ItemValue.  # noqa: E501


        :return: The updated_by of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this ItemValue.


        :param updated_by: The updated_by of this ItemValue.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def updated_date(self):
        """Gets the updated_date of this ItemValue.  # noqa: E501


        :return: The updated_date of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ItemValue.


        :param updated_date: The updated_date of this ItemValue.  # noqa: E501
        :type: str
        """

        self._updated_date = updated_date

    @property
    def states_history(self):
        """Gets the states_history of this ItemValue.  # noqa: E501


        :return: The states_history of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._states_history

    @states_history.setter
    def states_history(self, states_history):
        """Sets the states_history of this ItemValue.


        :param states_history: The states_history of this ItemValue.  # noqa: E501
        :type: str
        """

        self._states_history = states_history

    @property
    def started_by(self):
        """Gets the started_by of this ItemValue.  # noqa: E501


        :return: The started_by of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._started_by

    @started_by.setter
    def started_by(self, started_by):
        """Sets the started_by of this ItemValue.


        :param started_by: The started_by of this ItemValue.  # noqa: E501
        :type: str
        """

        self._started_by = started_by

    @property
    def started_date(self):
        """Gets the started_date of this ItemValue.  # noqa: E501


        :return: The started_date of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._started_date

    @started_date.setter
    def started_date(self, started_date):
        """Sets the started_date of this ItemValue.


        :param started_date: The started_date of this ItemValue.  # noqa: E501
        :type: str
        """

        self._started_date = started_date

    @property
    def completed_by(self):
        """Gets the completed_by of this ItemValue.  # noqa: E501


        :return: The completed_by of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._completed_by

    @completed_by.setter
    def completed_by(self, completed_by):
        """Sets the completed_by of this ItemValue.


        :param completed_by: The completed_by of this ItemValue.  # noqa: E501
        :type: str
        """

        self._completed_by = completed_by

    @property
    def completed_date(self):
        """Gets the completed_date of this ItemValue.  # noqa: E501


        :return: The completed_date of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this ItemValue.


        :param completed_date: The completed_date of this ItemValue.  # noqa: E501
        :type: str
        """

        self._completed_date = completed_date

    @property
    def crf_occurrence(self):
        """Gets the crf_occurrence of this ItemValue.  # noqa: E501


        :return: The crf_occurrence of this ItemValue.  # noqa: E501
        :rtype: int
        """
        return self._crf_occurrence

    @crf_occurrence.setter
    def crf_occurrence(self, crf_occurrence):
        """Sets the crf_occurrence of this ItemValue.


        :param crf_occurrence: The crf_occurrence of this ItemValue.  # noqa: E501
        :type: int
        """

        self._crf_occurrence = crf_occurrence

    @property
    def sdv(self):
        """Gets the sdv of this ItemValue.  # noqa: E501


        :return: The sdv of this ItemValue.  # noqa: E501
        :rtype: bool
        """
        return self._sdv

    @sdv.setter
    def sdv(self, sdv):
        """Sets the sdv of this ItemValue.


        :param sdv: The sdv of this ItemValue.  # noqa: E501
        :type: bool
        """

        self._sdv = sdv

    @property
    def sdv_by(self):
        """Gets the sdv_by of this ItemValue.  # noqa: E501


        :return: The sdv_by of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._sdv_by

    @sdv_by.setter
    def sdv_by(self, sdv_by):
        """Sets the sdv_by of this ItemValue.


        :param sdv_by: The sdv_by of this ItemValue.  # noqa: E501
        :type: str
        """

        self._sdv_by = sdv_by

    @property
    def sdv_date(self):
        """Gets the sdv_date of this ItemValue.  # noqa: E501


        :return: The sdv_date of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._sdv_date

    @sdv_date.setter
    def sdv_date(self, sdv_date):
        """Sets the sdv_date of this ItemValue.


        :param sdv_date: The sdv_date of this ItemValue.  # noqa: E501
        :type: str
        """

        self._sdv_date = sdv_date

    @property
    def mrv(self):
        """Gets the mrv of this ItemValue.  # noqa: E501


        :return: The mrv of this ItemValue.  # noqa: E501
        :rtype: bool
        """
        return self._mrv

    @mrv.setter
    def mrv(self, mrv):
        """Sets the mrv of this ItemValue.


        :param mrv: The mrv of this ItemValue.  # noqa: E501
        :type: bool
        """

        self._mrv = mrv

    @property
    def mrv_by(self):
        """Gets the mrv_by of this ItemValue.  # noqa: E501


        :return: The mrv_by of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._mrv_by

    @mrv_by.setter
    def mrv_by(self, mrv_by):
        """Sets the mrv_by of this ItemValue.


        :param mrv_by: The mrv_by of this ItemValue.  # noqa: E501
        :type: str
        """

        self._mrv_by = mrv_by

    @property
    def mrv_date(self):
        """Gets the mrv_date of this ItemValue.  # noqa: E501


        :return: The mrv_date of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._mrv_date

    @mrv_date.setter
    def mrv_date(self, mrv_date):
        """Sets the mrv_date of this ItemValue.


        :param mrv_date: The mrv_date of this ItemValue.  # noqa: E501
        :type: str
        """

        self._mrv_date = mrv_date

    @property
    def drv(self):
        """Gets the drv of this ItemValue.  # noqa: E501


        :return: The drv of this ItemValue.  # noqa: E501
        :rtype: bool
        """
        return self._drv

    @drv.setter
    def drv(self, drv):
        """Sets the drv of this ItemValue.


        :param drv: The drv of this ItemValue.  # noqa: E501
        :type: bool
        """

        self._drv = drv

    @property
    def drv_by(self):
        """Gets the drv_by of this ItemValue.  # noqa: E501


        :return: The drv_by of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._drv_by

    @drv_by.setter
    def drv_by(self, drv_by):
        """Sets the drv_by of this ItemValue.


        :param drv_by: The drv_by of this ItemValue.  # noqa: E501
        :type: str
        """

        self._drv_by = drv_by

    @property
    def drv_date(self):
        """Gets the drv_date of this ItemValue.  # noqa: E501


        :return: The drv_date of this ItemValue.  # noqa: E501
        :rtype: str
        """
        return self._drv_date

    @drv_date.setter
    def drv_date(self, drv_date):
        """Sets the drv_date of this ItemValue.


        :param drv_date: The drv_date of this ItemValue.  # noqa: E501
        :type: str
        """

        self._drv_date = drv_date

    @property
    def response_set(self):
        """Gets the response_set of this ItemValue.  # noqa: E501


        :return: The response_set of this ItemValue.  # noqa: E501
        :rtype: ResponseSetRpc
        """
        return self._response_set

    @response_set.setter
    def response_set(self, response_set):
        """Sets the response_set of this ItemValue.


        :param response_set: The response_set of this ItemValue.  # noqa: E501
        :type: ResponseSetRpc
        """

        self._response_set = response_set

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
        if not isinstance(other, ItemValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemValue):
            return True

        return self.to_dict() != other.to_dict()
