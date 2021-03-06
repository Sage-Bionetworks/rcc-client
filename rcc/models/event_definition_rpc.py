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


class EventDefinitionRpc(object):
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
        'description': 'str',
        'ad_lookup_code_by_event_def_type_id': 'int',
        'ad_lookup_codes_by_status_id': 'int',
        'disp_sequence': 'int',
        'repeating': 'bool',
        'repeating_frequency': 'int',
        'repeating_daily_how_many_days': 'int',
        'repeating_how_many_times': 'int',
        'created_by_rule': 'bool',
        'ad_lookup_code_by_category_id': 'int',
        'reference_visit': 'bool',
        'day_schedule': 'int',
        'day_min': 'int',
        'day_max': 'int',
        'calendared_type_lc_id': 'int',
        'grace_hour_min': 'int',
        'grace_hour_max': 'int',
        'grace_minute_min': 'int',
        'grace_minute_max': 'int',
        'can_edit_before_event': 'bool',
        'can_edit_after_event': 'bool',
        'weekdays_only': 'bool',
        'dynamic_event': 'bool',
        'create_date': 'int',
        'update_date': 'int'
    }

    attribute_map = {
        'id': 'id',
        'study_id': 'studyId',
        'name': 'name',
        'unique_event_name': 'uniqueEventName',
        'description': 'description',
        'ad_lookup_code_by_event_def_type_id': 'adLookupCodeByEventDefTypeId',
        'ad_lookup_codes_by_status_id': 'adLookupCodesByStatusId',
        'disp_sequence': 'dispSequence',
        'repeating': 'repeating',
        'repeating_frequency': 'repeatingFrequency',
        'repeating_daily_how_many_days': 'repeatingDailyHowManyDays',
        'repeating_how_many_times': 'repeatingHowManyTimes',
        'created_by_rule': 'createdByRule',
        'ad_lookup_code_by_category_id': 'adLookupCodeByCategoryId',
        'reference_visit': 'referenceVisit',
        'day_schedule': 'daySchedule',
        'day_min': 'dayMin',
        'day_max': 'dayMax',
        'calendared_type_lc_id': 'calendaredTypeLcId',
        'grace_hour_min': 'graceHourMin',
        'grace_hour_max': 'graceHourMax',
        'grace_minute_min': 'graceMinuteMin',
        'grace_minute_max': 'graceMinuteMax',
        'can_edit_before_event': 'canEditBeforeEvent',
        'can_edit_after_event': 'canEditAfterEvent',
        'weekdays_only': 'weekdaysOnly',
        'dynamic_event': 'dynamicEvent',
        'create_date': 'createDate',
        'update_date': 'updateDate'
    }

    def __init__(self, id=None, study_id=None, name=None, unique_event_name=None, description=None, ad_lookup_code_by_event_def_type_id=None, ad_lookup_codes_by_status_id=None, disp_sequence=None, repeating=None, repeating_frequency=None, repeating_daily_how_many_days=None, repeating_how_many_times=None, created_by_rule=None, ad_lookup_code_by_category_id=None, reference_visit=None, day_schedule=None, day_min=None, day_max=None, calendared_type_lc_id=None, grace_hour_min=None, grace_hour_max=None, grace_minute_min=None, grace_minute_max=None, can_edit_before_event=None, can_edit_after_event=None, weekdays_only=None, dynamic_event=None, create_date=None, update_date=None, local_vars_configuration=None):  # noqa: E501
        """EventDefinitionRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._study_id = None
        self._name = None
        self._unique_event_name = None
        self._description = None
        self._ad_lookup_code_by_event_def_type_id = None
        self._ad_lookup_codes_by_status_id = None
        self._disp_sequence = None
        self._repeating = None
        self._repeating_frequency = None
        self._repeating_daily_how_many_days = None
        self._repeating_how_many_times = None
        self._created_by_rule = None
        self._ad_lookup_code_by_category_id = None
        self._reference_visit = None
        self._day_schedule = None
        self._day_min = None
        self._day_max = None
        self._calendared_type_lc_id = None
        self._grace_hour_min = None
        self._grace_hour_max = None
        self._grace_minute_min = None
        self._grace_minute_max = None
        self._can_edit_before_event = None
        self._can_edit_after_event = None
        self._weekdays_only = None
        self._dynamic_event = None
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
        if description is not None:
            self.description = description
        if ad_lookup_code_by_event_def_type_id is not None:
            self.ad_lookup_code_by_event_def_type_id = ad_lookup_code_by_event_def_type_id
        if ad_lookup_codes_by_status_id is not None:
            self.ad_lookup_codes_by_status_id = ad_lookup_codes_by_status_id
        if disp_sequence is not None:
            self.disp_sequence = disp_sequence
        if repeating is not None:
            self.repeating = repeating
        if repeating_frequency is not None:
            self.repeating_frequency = repeating_frequency
        if repeating_daily_how_many_days is not None:
            self.repeating_daily_how_many_days = repeating_daily_how_many_days
        if repeating_how_many_times is not None:
            self.repeating_how_many_times = repeating_how_many_times
        if created_by_rule is not None:
            self.created_by_rule = created_by_rule
        if ad_lookup_code_by_category_id is not None:
            self.ad_lookup_code_by_category_id = ad_lookup_code_by_category_id
        if reference_visit is not None:
            self.reference_visit = reference_visit
        if day_schedule is not None:
            self.day_schedule = day_schedule
        if day_min is not None:
            self.day_min = day_min
        if day_max is not None:
            self.day_max = day_max
        if calendared_type_lc_id is not None:
            self.calendared_type_lc_id = calendared_type_lc_id
        if grace_hour_min is not None:
            self.grace_hour_min = grace_hour_min
        if grace_hour_max is not None:
            self.grace_hour_max = grace_hour_max
        if grace_minute_min is not None:
            self.grace_minute_min = grace_minute_min
        if grace_minute_max is not None:
            self.grace_minute_max = grace_minute_max
        if can_edit_before_event is not None:
            self.can_edit_before_event = can_edit_before_event
        if can_edit_after_event is not None:
            self.can_edit_after_event = can_edit_after_event
        if weekdays_only is not None:
            self.weekdays_only = weekdays_only
        if dynamic_event is not None:
            self.dynamic_event = dynamic_event
        if create_date is not None:
            self.create_date = create_date
        if update_date is not None:
            self.update_date = update_date

    @property
    def id(self):
        """Gets the id of this EventDefinitionRpc.  # noqa: E501


        :return: The id of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventDefinitionRpc.


        :param id: The id of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def study_id(self):
        """Gets the study_id of this EventDefinitionRpc.  # noqa: E501


        :return: The study_id of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this EventDefinitionRpc.


        :param study_id: The study_id of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._study_id = study_id

    @property
    def name(self):
        """Gets the name of this EventDefinitionRpc.  # noqa: E501


        :return: The name of this EventDefinitionRpc.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventDefinitionRpc.


        :param name: The name of this EventDefinitionRpc.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unique_event_name(self):
        """Gets the unique_event_name of this EventDefinitionRpc.  # noqa: E501


        :return: The unique_event_name of this EventDefinitionRpc.  # noqa: E501
        :rtype: str
        """
        return self._unique_event_name

    @unique_event_name.setter
    def unique_event_name(self, unique_event_name):
        """Sets the unique_event_name of this EventDefinitionRpc.


        :param unique_event_name: The unique_event_name of this EventDefinitionRpc.  # noqa: E501
        :type: str
        """

        self._unique_event_name = unique_event_name

    @property
    def description(self):
        """Gets the description of this EventDefinitionRpc.  # noqa: E501


        :return: The description of this EventDefinitionRpc.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventDefinitionRpc.


        :param description: The description of this EventDefinitionRpc.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ad_lookup_code_by_event_def_type_id(self):
        """Gets the ad_lookup_code_by_event_def_type_id of this EventDefinitionRpc.  # noqa: E501


        :return: The ad_lookup_code_by_event_def_type_id of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._ad_lookup_code_by_event_def_type_id

    @ad_lookup_code_by_event_def_type_id.setter
    def ad_lookup_code_by_event_def_type_id(self, ad_lookup_code_by_event_def_type_id):
        """Sets the ad_lookup_code_by_event_def_type_id of this EventDefinitionRpc.


        :param ad_lookup_code_by_event_def_type_id: The ad_lookup_code_by_event_def_type_id of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._ad_lookup_code_by_event_def_type_id = ad_lookup_code_by_event_def_type_id

    @property
    def ad_lookup_codes_by_status_id(self):
        """Gets the ad_lookup_codes_by_status_id of this EventDefinitionRpc.  # noqa: E501


        :return: The ad_lookup_codes_by_status_id of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._ad_lookup_codes_by_status_id

    @ad_lookup_codes_by_status_id.setter
    def ad_lookup_codes_by_status_id(self, ad_lookup_codes_by_status_id):
        """Sets the ad_lookup_codes_by_status_id of this EventDefinitionRpc.


        :param ad_lookup_codes_by_status_id: The ad_lookup_codes_by_status_id of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._ad_lookup_codes_by_status_id = ad_lookup_codes_by_status_id

    @property
    def disp_sequence(self):
        """Gets the disp_sequence of this EventDefinitionRpc.  # noqa: E501


        :return: The disp_sequence of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._disp_sequence

    @disp_sequence.setter
    def disp_sequence(self, disp_sequence):
        """Sets the disp_sequence of this EventDefinitionRpc.


        :param disp_sequence: The disp_sequence of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._disp_sequence = disp_sequence

    @property
    def repeating(self):
        """Gets the repeating of this EventDefinitionRpc.  # noqa: E501


        :return: The repeating of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._repeating

    @repeating.setter
    def repeating(self, repeating):
        """Sets the repeating of this EventDefinitionRpc.


        :param repeating: The repeating of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._repeating = repeating

    @property
    def repeating_frequency(self):
        """Gets the repeating_frequency of this EventDefinitionRpc.  # noqa: E501


        :return: The repeating_frequency of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._repeating_frequency

    @repeating_frequency.setter
    def repeating_frequency(self, repeating_frequency):
        """Sets the repeating_frequency of this EventDefinitionRpc.


        :param repeating_frequency: The repeating_frequency of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._repeating_frequency = repeating_frequency

    @property
    def repeating_daily_how_many_days(self):
        """Gets the repeating_daily_how_many_days of this EventDefinitionRpc.  # noqa: E501


        :return: The repeating_daily_how_many_days of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._repeating_daily_how_many_days

    @repeating_daily_how_many_days.setter
    def repeating_daily_how_many_days(self, repeating_daily_how_many_days):
        """Sets the repeating_daily_how_many_days of this EventDefinitionRpc.


        :param repeating_daily_how_many_days: The repeating_daily_how_many_days of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._repeating_daily_how_many_days = repeating_daily_how_many_days

    @property
    def repeating_how_many_times(self):
        """Gets the repeating_how_many_times of this EventDefinitionRpc.  # noqa: E501


        :return: The repeating_how_many_times of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._repeating_how_many_times

    @repeating_how_many_times.setter
    def repeating_how_many_times(self, repeating_how_many_times):
        """Sets the repeating_how_many_times of this EventDefinitionRpc.


        :param repeating_how_many_times: The repeating_how_many_times of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._repeating_how_many_times = repeating_how_many_times

    @property
    def created_by_rule(self):
        """Gets the created_by_rule of this EventDefinitionRpc.  # noqa: E501


        :return: The created_by_rule of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._created_by_rule

    @created_by_rule.setter
    def created_by_rule(self, created_by_rule):
        """Sets the created_by_rule of this EventDefinitionRpc.


        :param created_by_rule: The created_by_rule of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._created_by_rule = created_by_rule

    @property
    def ad_lookup_code_by_category_id(self):
        """Gets the ad_lookup_code_by_category_id of this EventDefinitionRpc.  # noqa: E501


        :return: The ad_lookup_code_by_category_id of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._ad_lookup_code_by_category_id

    @ad_lookup_code_by_category_id.setter
    def ad_lookup_code_by_category_id(self, ad_lookup_code_by_category_id):
        """Sets the ad_lookup_code_by_category_id of this EventDefinitionRpc.


        :param ad_lookup_code_by_category_id: The ad_lookup_code_by_category_id of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._ad_lookup_code_by_category_id = ad_lookup_code_by_category_id

    @property
    def reference_visit(self):
        """Gets the reference_visit of this EventDefinitionRpc.  # noqa: E501


        :return: The reference_visit of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._reference_visit

    @reference_visit.setter
    def reference_visit(self, reference_visit):
        """Sets the reference_visit of this EventDefinitionRpc.


        :param reference_visit: The reference_visit of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._reference_visit = reference_visit

    @property
    def day_schedule(self):
        """Gets the day_schedule of this EventDefinitionRpc.  # noqa: E501


        :return: The day_schedule of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._day_schedule

    @day_schedule.setter
    def day_schedule(self, day_schedule):
        """Sets the day_schedule of this EventDefinitionRpc.


        :param day_schedule: The day_schedule of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._day_schedule = day_schedule

    @property
    def day_min(self):
        """Gets the day_min of this EventDefinitionRpc.  # noqa: E501


        :return: The day_min of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._day_min

    @day_min.setter
    def day_min(self, day_min):
        """Sets the day_min of this EventDefinitionRpc.


        :param day_min: The day_min of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._day_min = day_min

    @property
    def day_max(self):
        """Gets the day_max of this EventDefinitionRpc.  # noqa: E501


        :return: The day_max of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._day_max

    @day_max.setter
    def day_max(self, day_max):
        """Sets the day_max of this EventDefinitionRpc.


        :param day_max: The day_max of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._day_max = day_max

    @property
    def calendared_type_lc_id(self):
        """Gets the calendared_type_lc_id of this EventDefinitionRpc.  # noqa: E501


        :return: The calendared_type_lc_id of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._calendared_type_lc_id

    @calendared_type_lc_id.setter
    def calendared_type_lc_id(self, calendared_type_lc_id):
        """Sets the calendared_type_lc_id of this EventDefinitionRpc.


        :param calendared_type_lc_id: The calendared_type_lc_id of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._calendared_type_lc_id = calendared_type_lc_id

    @property
    def grace_hour_min(self):
        """Gets the grace_hour_min of this EventDefinitionRpc.  # noqa: E501


        :return: The grace_hour_min of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._grace_hour_min

    @grace_hour_min.setter
    def grace_hour_min(self, grace_hour_min):
        """Sets the grace_hour_min of this EventDefinitionRpc.


        :param grace_hour_min: The grace_hour_min of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._grace_hour_min = grace_hour_min

    @property
    def grace_hour_max(self):
        """Gets the grace_hour_max of this EventDefinitionRpc.  # noqa: E501


        :return: The grace_hour_max of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._grace_hour_max

    @grace_hour_max.setter
    def grace_hour_max(self, grace_hour_max):
        """Sets the grace_hour_max of this EventDefinitionRpc.


        :param grace_hour_max: The grace_hour_max of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._grace_hour_max = grace_hour_max

    @property
    def grace_minute_min(self):
        """Gets the grace_minute_min of this EventDefinitionRpc.  # noqa: E501


        :return: The grace_minute_min of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._grace_minute_min

    @grace_minute_min.setter
    def grace_minute_min(self, grace_minute_min):
        """Sets the grace_minute_min of this EventDefinitionRpc.


        :param grace_minute_min: The grace_minute_min of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._grace_minute_min = grace_minute_min

    @property
    def grace_minute_max(self):
        """Gets the grace_minute_max of this EventDefinitionRpc.  # noqa: E501


        :return: The grace_minute_max of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._grace_minute_max

    @grace_minute_max.setter
    def grace_minute_max(self, grace_minute_max):
        """Sets the grace_minute_max of this EventDefinitionRpc.


        :param grace_minute_max: The grace_minute_max of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._grace_minute_max = grace_minute_max

    @property
    def can_edit_before_event(self):
        """Gets the can_edit_before_event of this EventDefinitionRpc.  # noqa: E501


        :return: The can_edit_before_event of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_before_event

    @can_edit_before_event.setter
    def can_edit_before_event(self, can_edit_before_event):
        """Sets the can_edit_before_event of this EventDefinitionRpc.


        :param can_edit_before_event: The can_edit_before_event of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._can_edit_before_event = can_edit_before_event

    @property
    def can_edit_after_event(self):
        """Gets the can_edit_after_event of this EventDefinitionRpc.  # noqa: E501


        :return: The can_edit_after_event of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_after_event

    @can_edit_after_event.setter
    def can_edit_after_event(self, can_edit_after_event):
        """Sets the can_edit_after_event of this EventDefinitionRpc.


        :param can_edit_after_event: The can_edit_after_event of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._can_edit_after_event = can_edit_after_event

    @property
    def weekdays_only(self):
        """Gets the weekdays_only of this EventDefinitionRpc.  # noqa: E501


        :return: The weekdays_only of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._weekdays_only

    @weekdays_only.setter
    def weekdays_only(self, weekdays_only):
        """Sets the weekdays_only of this EventDefinitionRpc.


        :param weekdays_only: The weekdays_only of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._weekdays_only = weekdays_only

    @property
    def dynamic_event(self):
        """Gets the dynamic_event of this EventDefinitionRpc.  # noqa: E501


        :return: The dynamic_event of this EventDefinitionRpc.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_event

    @dynamic_event.setter
    def dynamic_event(self, dynamic_event):
        """Sets the dynamic_event of this EventDefinitionRpc.


        :param dynamic_event: The dynamic_event of this EventDefinitionRpc.  # noqa: E501
        :type: bool
        """

        self._dynamic_event = dynamic_event

    @property
    def create_date(self):
        """Gets the create_date of this EventDefinitionRpc.  # noqa: E501


        :return: The create_date of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this EventDefinitionRpc.


        :param create_date: The create_date of this EventDefinitionRpc.  # noqa: E501
        :type: int
        """

        self._create_date = create_date

    @property
    def update_date(self):
        """Gets the update_date of this EventDefinitionRpc.  # noqa: E501


        :return: The update_date of this EventDefinitionRpc.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EventDefinitionRpc.


        :param update_date: The update_date of this EventDefinitionRpc.  # noqa: E501
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
        if not isinstance(other, EventDefinitionRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventDefinitionRpc):
            return True

        return self.to_dict() != other.to_dict()
