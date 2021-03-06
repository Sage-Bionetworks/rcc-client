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


class ODMcomplexTypeDefinitionAuditRecord(object):
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
        'user_ref': 'ODMcomplexTypeDefinitionUserRef',
        'location_ref': 'ODMcomplexTypeDefinitionLocationRef',
        'date_time_stamp': 'ODMcomplexTypeDefinitionDateTimeStamp',
        'reason_for_change': 'ODMcomplexTypeDefinitionReasonForChange',
        'source_id': 'ODMcomplexTypeDefinitionSourceID',
        'edit_point': 'str',
        'used_imputation_method': 'str',
        'id': 'str'
    }

    attribute_map = {
        'user_ref': 'userRef',
        'location_ref': 'locationRef',
        'date_time_stamp': 'dateTimeStamp',
        'reason_for_change': 'reasonForChange',
        'source_id': 'sourceID',
        'edit_point': 'editPoint',
        'used_imputation_method': 'usedImputationMethod',
        'id': 'id'
    }

    def __init__(self, user_ref=None, location_ref=None, date_time_stamp=None, reason_for_change=None, source_id=None, edit_point=None, used_imputation_method=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionAuditRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_ref = None
        self._location_ref = None
        self._date_time_stamp = None
        self._reason_for_change = None
        self._source_id = None
        self._edit_point = None
        self._used_imputation_method = None
        self._id = None
        self.discriminator = None

        self.user_ref = user_ref
        self.location_ref = location_ref
        self.date_time_stamp = date_time_stamp
        if reason_for_change is not None:
            self.reason_for_change = reason_for_change
        if source_id is not None:
            self.source_id = source_id
        if edit_point is not None:
            self.edit_point = edit_point
        if used_imputation_method is not None:
            self.used_imputation_method = used_imputation_method
        if id is not None:
            self.id = id

    @property
    def user_ref(self):
        """Gets the user_ref of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The user_ref of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionUserRef
        """
        return self._user_ref

    @user_ref.setter
    def user_ref(self, user_ref):
        """Sets the user_ref of this ODMcomplexTypeDefinitionAuditRecord.


        :param user_ref: The user_ref of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: ODMcomplexTypeDefinitionUserRef
        """
        if self.local_vars_configuration.client_side_validation and user_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `user_ref`, must not be `None`")  # noqa: E501

        self._user_ref = user_ref

    @property
    def location_ref(self):
        """Gets the location_ref of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The location_ref of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionLocationRef
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this ODMcomplexTypeDefinitionAuditRecord.


        :param location_ref: The location_ref of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: ODMcomplexTypeDefinitionLocationRef
        """
        if self.local_vars_configuration.client_side_validation and location_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `location_ref`, must not be `None`")  # noqa: E501

        self._location_ref = location_ref

    @property
    def date_time_stamp(self):
        """Gets the date_time_stamp of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The date_time_stamp of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionDateTimeStamp
        """
        return self._date_time_stamp

    @date_time_stamp.setter
    def date_time_stamp(self, date_time_stamp):
        """Sets the date_time_stamp of this ODMcomplexTypeDefinitionAuditRecord.


        :param date_time_stamp: The date_time_stamp of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: ODMcomplexTypeDefinitionDateTimeStamp
        """
        if self.local_vars_configuration.client_side_validation and date_time_stamp is None:  # noqa: E501
            raise ValueError("Invalid value for `date_time_stamp`, must not be `None`")  # noqa: E501

        self._date_time_stamp = date_time_stamp

    @property
    def reason_for_change(self):
        """Gets the reason_for_change of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The reason_for_change of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionReasonForChange
        """
        return self._reason_for_change

    @reason_for_change.setter
    def reason_for_change(self, reason_for_change):
        """Sets the reason_for_change of this ODMcomplexTypeDefinitionAuditRecord.


        :param reason_for_change: The reason_for_change of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: ODMcomplexTypeDefinitionReasonForChange
        """

        self._reason_for_change = reason_for_change

    @property
    def source_id(self):
        """Gets the source_id of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The source_id of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionSourceID
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ODMcomplexTypeDefinitionAuditRecord.


        :param source_id: The source_id of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: ODMcomplexTypeDefinitionSourceID
        """

        self._source_id = source_id

    @property
    def edit_point(self):
        """Gets the edit_point of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The edit_point of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: str
        """
        return self._edit_point

    @edit_point.setter
    def edit_point(self, edit_point):
        """Sets the edit_point of this ODMcomplexTypeDefinitionAuditRecord.


        :param edit_point: The edit_point of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: str
        """
        allowed_values = ["MONITORING", "DATA_MANAGEMENT", "DB_AUDIT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and edit_point not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `edit_point` ({0}), must be one of {1}"  # noqa: E501
                .format(edit_point, allowed_values)
            )

        self._edit_point = edit_point

    @property
    def used_imputation_method(self):
        """Gets the used_imputation_method of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The used_imputation_method of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: str
        """
        return self._used_imputation_method

    @used_imputation_method.setter
    def used_imputation_method(self, used_imputation_method):
        """Sets the used_imputation_method of this ODMcomplexTypeDefinitionAuditRecord.


        :param used_imputation_method: The used_imputation_method of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and used_imputation_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `used_imputation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(used_imputation_method, allowed_values)
            )

        self._used_imputation_method = used_imputation_method

    @property
    def id(self):
        """Gets the id of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501


        :return: The id of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ODMcomplexTypeDefinitionAuditRecord.


        :param id: The id of this ODMcomplexTypeDefinitionAuditRecord.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, ODMcomplexTypeDefinitionAuditRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionAuditRecord):
            return True

        return self.to_dict() != other.to_dict()
