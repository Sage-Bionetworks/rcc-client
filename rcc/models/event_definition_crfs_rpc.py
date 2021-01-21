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


class EventDefinitionCrfsRpc(object):
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
        'parent_id': 'int',
        'required_flag': 'bool',
        'repeating_flag': 'bool',
        'double_data_entry': 'bool',
        'dynamic_form': 'bool',
        'used_in_progress_bar': 'bool',
        'version_id': 'int',
        'source_data_verification_id': 'int',
        'source_data_verification_code': 'str',
        'crf_id': 'int',
        'crf_caption': 'str',
        'event_definitions_id': 'int',
        'site_id': 'int',
        'update_date': 'int',
        'ordinal': 'int'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parentId',
        'required_flag': 'requiredFlag',
        'repeating_flag': 'repeatingFlag',
        'double_data_entry': 'doubleDataEntry',
        'dynamic_form': 'dynamicForm',
        'used_in_progress_bar': 'usedInProgressBar',
        'version_id': 'versionId',
        'source_data_verification_id': 'sourceDataVerificationId',
        'source_data_verification_code': 'sourceDataVerificationCode',
        'crf_id': 'crfId',
        'crf_caption': 'crfCaption',
        'event_definitions_id': 'eventDefinitionsId',
        'site_id': 'siteId',
        'update_date': 'updateDate',
        'ordinal': 'ordinal'
    }

    def __init__(self, id=None, parent_id=None, required_flag=None, repeating_flag=None, double_data_entry=None, dynamic_form=None, used_in_progress_bar=None, version_id=None, source_data_verification_id=None, source_data_verification_code=None, crf_id=None, crf_caption=None, event_definitions_id=None, site_id=None, update_date=None, ordinal=None, local_vars_configuration=None):  # noqa: E501
        """EventDefinitionCrfsRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._parent_id = None
        self._required_flag = None
        self._repeating_flag = None
        self._double_data_entry = None
        self._dynamic_form = None
        self._used_in_progress_bar = None
        self._version_id = None
        self._source_data_verification_id = None
        self._source_data_verification_code = None
        self._crf_id = None
        self._crf_caption = None
        self._event_definitions_id = None
        self._site_id = None
        self._update_date = None
        self._ordinal = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        if required_flag is not None:
            self.required_flag = required_flag
        if repeating_flag is not None:
            self.repeating_flag = repeating_flag
        if double_data_entry is not None:
            self.double_data_entry = double_data_entry
        if dynamic_form is not None:
            self.dynamic_form = dynamic_form
        if used_in_progress_bar is not None:
            self.used_in_progress_bar = used_in_progress_bar
        if version_id is not None:
            self.version_id = version_id
        if source_data_verification_id is not None:
            self.source_data_verification_id = source_data_verification_id
        if source_data_verification_code is not None:
            self.source_data_verification_code = source_data_verification_code
        if crf_id is not None:
            self.crf_id = crf_id
        if crf_caption is not None:
            self.crf_caption = crf_caption
        if event_definitions_id is not None:
            self.event_definitions_id = event_definitions_id
        if site_id is not None:
            self.site_id = site_id
        if update_date is not None:
            self.update_date = update_date
        if ordinal is not None:
            self.ordinal = ordinal

    @property
    def id(self):
        """Gets the id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventDefinitionCrfsRpc.


        :param id: The id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The parent_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this EventDefinitionCrfsRpc.


        :param parent_id: The parent_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def required_flag(self):
        """Gets the required_flag of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The required_flag of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: bool
        """
        return self._required_flag

    @required_flag.setter
    def required_flag(self, required_flag):
        """Sets the required_flag of this EventDefinitionCrfsRpc.


        :param required_flag: The required_flag of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: bool
        """

        self._required_flag = required_flag

    @property
    def repeating_flag(self):
        """Gets the repeating_flag of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The repeating_flag of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: bool
        """
        return self._repeating_flag

    @repeating_flag.setter
    def repeating_flag(self, repeating_flag):
        """Sets the repeating_flag of this EventDefinitionCrfsRpc.


        :param repeating_flag: The repeating_flag of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: bool
        """

        self._repeating_flag = repeating_flag

    @property
    def double_data_entry(self):
        """Gets the double_data_entry of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The double_data_entry of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: bool
        """
        return self._double_data_entry

    @double_data_entry.setter
    def double_data_entry(self, double_data_entry):
        """Sets the double_data_entry of this EventDefinitionCrfsRpc.


        :param double_data_entry: The double_data_entry of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: bool
        """

        self._double_data_entry = double_data_entry

    @property
    def dynamic_form(self):
        """Gets the dynamic_form of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The dynamic_form of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_form

    @dynamic_form.setter
    def dynamic_form(self, dynamic_form):
        """Sets the dynamic_form of this EventDefinitionCrfsRpc.


        :param dynamic_form: The dynamic_form of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: bool
        """

        self._dynamic_form = dynamic_form

    @property
    def used_in_progress_bar(self):
        """Gets the used_in_progress_bar of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The used_in_progress_bar of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: bool
        """
        return self._used_in_progress_bar

    @used_in_progress_bar.setter
    def used_in_progress_bar(self, used_in_progress_bar):
        """Sets the used_in_progress_bar of this EventDefinitionCrfsRpc.


        :param used_in_progress_bar: The used_in_progress_bar of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: bool
        """

        self._used_in_progress_bar = used_in_progress_bar

    @property
    def version_id(self):
        """Gets the version_id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The version_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this EventDefinitionCrfsRpc.


        :param version_id: The version_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._version_id = version_id

    @property
    def source_data_verification_id(self):
        """Gets the source_data_verification_id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The source_data_verification_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._source_data_verification_id

    @source_data_verification_id.setter
    def source_data_verification_id(self, source_data_verification_id):
        """Sets the source_data_verification_id of this EventDefinitionCrfsRpc.


        :param source_data_verification_id: The source_data_verification_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._source_data_verification_id = source_data_verification_id

    @property
    def source_data_verification_code(self):
        """Gets the source_data_verification_code of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The source_data_verification_code of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: str
        """
        return self._source_data_verification_code

    @source_data_verification_code.setter
    def source_data_verification_code(self, source_data_verification_code):
        """Sets the source_data_verification_code of this EventDefinitionCrfsRpc.


        :param source_data_verification_code: The source_data_verification_code of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: str
        """

        self._source_data_verification_code = source_data_verification_code

    @property
    def crf_id(self):
        """Gets the crf_id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The crf_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_id

    @crf_id.setter
    def crf_id(self, crf_id):
        """Sets the crf_id of this EventDefinitionCrfsRpc.


        :param crf_id: The crf_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._crf_id = crf_id

    @property
    def crf_caption(self):
        """Gets the crf_caption of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The crf_caption of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: str
        """
        return self._crf_caption

    @crf_caption.setter
    def crf_caption(self, crf_caption):
        """Sets the crf_caption of this EventDefinitionCrfsRpc.


        :param crf_caption: The crf_caption of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: str
        """

        self._crf_caption = crf_caption

    @property
    def event_definitions_id(self):
        """Gets the event_definitions_id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The event_definitions_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._event_definitions_id

    @event_definitions_id.setter
    def event_definitions_id(self, event_definitions_id):
        """Sets the event_definitions_id of this EventDefinitionCrfsRpc.


        :param event_definitions_id: The event_definitions_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._event_definitions_id = event_definitions_id

    @property
    def site_id(self):
        """Gets the site_id of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The site_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this EventDefinitionCrfsRpc.


        :param site_id: The site_id of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def update_date(self):
        """Gets the update_date of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The update_date of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this EventDefinitionCrfsRpc.


        :param update_date: The update_date of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._update_date = update_date

    @property
    def ordinal(self):
        """Gets the ordinal of this EventDefinitionCrfsRpc.  # noqa: E501


        :return: The ordinal of this EventDefinitionCrfsRpc.  # noqa: E501
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this EventDefinitionCrfsRpc.


        :param ordinal: The ordinal of this EventDefinitionCrfsRpc.  # noqa: E501
        :type: int
        """

        self._ordinal = ordinal

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
        if not isinstance(other, EventDefinitionCrfsRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventDefinitionCrfsRpc):
            return True

        return self.to_dict() != other.to_dict()
