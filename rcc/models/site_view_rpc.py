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


class SiteViewRpc(object):
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
        'site_name': 'str',
        'facility': 'str',
        'site_type': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'site_name': 'siteName',
        'facility': 'facility',
        'site_type': 'siteType',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, site_name=None, facility=None, site_type=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """SiteViewRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._site_name = None
        self._facility = None
        self._site_type = None
        self._enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if site_name is not None:
            self.site_name = site_name
        if facility is not None:
            self.facility = facility
        if site_type is not None:
            self.site_type = site_type
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this SiteViewRpc.  # noqa: E501


        :return: The id of this SiteViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteViewRpc.


        :param id: The id of this SiteViewRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def site_name(self):
        """Gets the site_name of this SiteViewRpc.  # noqa: E501


        :return: The site_name of this SiteViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        """Sets the site_name of this SiteViewRpc.


        :param site_name: The site_name of this SiteViewRpc.  # noqa: E501
        :type: str
        """

        self._site_name = site_name

    @property
    def facility(self):
        """Gets the facility of this SiteViewRpc.  # noqa: E501


        :return: The facility of this SiteViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this SiteViewRpc.


        :param facility: The facility of this SiteViewRpc.  # noqa: E501
        :type: str
        """

        self._facility = facility

    @property
    def site_type(self):
        """Gets the site_type of this SiteViewRpc.  # noqa: E501


        :return: The site_type of this SiteViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        """Sets the site_type of this SiteViewRpc.


        :param site_type: The site_type of this SiteViewRpc.  # noqa: E501
        :type: str
        """

        self._site_type = site_type

    @property
    def enabled(self):
        """Gets the enabled of this SiteViewRpc.  # noqa: E501


        :return: The enabled of this SiteViewRpc.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SiteViewRpc.


        :param enabled: The enabled of this SiteViewRpc.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, SiteViewRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SiteViewRpc):
            return True

        return self.to_dict() != other.to_dict()