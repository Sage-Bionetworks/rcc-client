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


class ODMcomplexTypeDefinitionUser(object):
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
        'login_name': 'ODMcomplexTypeDefinitionLoginName',
        'display_name': 'ODMcomplexTypeDefinitionDisplayName',
        'full_name': 'ODMcomplexTypeDefinitionFullName',
        'first_name': 'ODMcomplexTypeDefinitionFirstName',
        'last_name': 'ODMcomplexTypeDefinitionLastName',
        'organization': 'ODMcomplexTypeDefinitionOrganization',
        'address': 'list[ODMcomplexTypeDefinitionAddress]',
        'email': 'list[ODMcomplexTypeDefinitionEmail]',
        'picture': 'ODMcomplexTypeDefinitionPicture',
        'pager': 'ODMcomplexTypeDefinitionPager',
        'fax': 'list[ODMcomplexTypeDefinitionFax]',
        'phone': 'list[ODMcomplexTypeDefinitionPhone]',
        'location_ref': 'list[ODMcomplexTypeDefinitionLocationRef]',
        'certificate': 'list[ODMcomplexTypeDefinitionCertificate]',
        'oid': 'str',
        'user_type': 'str'
    }

    attribute_map = {
        'login_name': 'loginName',
        'display_name': 'displayName',
        'full_name': 'fullName',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'organization': 'organization',
        'address': 'address',
        'email': 'email',
        'picture': 'picture',
        'pager': 'pager',
        'fax': 'fax',
        'phone': 'phone',
        'location_ref': 'locationRef',
        'certificate': 'certificate',
        'oid': 'oid',
        'user_type': 'userType'
    }

    def __init__(self, login_name=None, display_name=None, full_name=None, first_name=None, last_name=None, organization=None, address=None, email=None, picture=None, pager=None, fax=None, phone=None, location_ref=None, certificate=None, oid=None, user_type=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._login_name = None
        self._display_name = None
        self._full_name = None
        self._first_name = None
        self._last_name = None
        self._organization = None
        self._address = None
        self._email = None
        self._picture = None
        self._pager = None
        self._fax = None
        self._phone = None
        self._location_ref = None
        self._certificate = None
        self._oid = None
        self._user_type = None
        self.discriminator = None

        if login_name is not None:
            self.login_name = login_name
        if display_name is not None:
            self.display_name = display_name
        if full_name is not None:
            self.full_name = full_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if organization is not None:
            self.organization = organization
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if picture is not None:
            self.picture = picture
        if pager is not None:
            self.pager = pager
        if fax is not None:
            self.fax = fax
        if phone is not None:
            self.phone = phone
        if location_ref is not None:
            self.location_ref = location_ref
        if certificate is not None:
            self.certificate = certificate
        if oid is not None:
            self.oid = oid
        if user_type is not None:
            self.user_type = user_type

    @property
    def login_name(self):
        """Gets the login_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The login_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionLoginName
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this ODMcomplexTypeDefinitionUser.


        :param login_name: The login_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionLoginName
        """

        self._login_name = login_name

    @property
    def display_name(self):
        """Gets the display_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The display_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionDisplayName
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ODMcomplexTypeDefinitionUser.


        :param display_name: The display_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionDisplayName
        """

        self._display_name = display_name

    @property
    def full_name(self):
        """Gets the full_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The full_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionFullName
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ODMcomplexTypeDefinitionUser.


        :param full_name: The full_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionFullName
        """

        self._full_name = full_name

    @property
    def first_name(self):
        """Gets the first_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The first_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionFirstName
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ODMcomplexTypeDefinitionUser.


        :param first_name: The first_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionFirstName
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The last_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionLastName
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ODMcomplexTypeDefinitionUser.


        :param last_name: The last_name of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionLastName
        """

        self._last_name = last_name

    @property
    def organization(self):
        """Gets the organization of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The organization of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ODMcomplexTypeDefinitionUser.


        :param organization: The organization of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionOrganization
        """

        self._organization = organization

    @property
    def address(self):
        """Gets the address of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The address of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionAddress]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ODMcomplexTypeDefinitionUser.


        :param address: The address of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionAddress]
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The email of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionEmail]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ODMcomplexTypeDefinitionUser.


        :param email: The email of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionEmail]
        """

        self._email = email

    @property
    def picture(self):
        """Gets the picture of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The picture of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionPicture
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this ODMcomplexTypeDefinitionUser.


        :param picture: The picture of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionPicture
        """

        self._picture = picture

    @property
    def pager(self):
        """Gets the pager of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The pager of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: ODMcomplexTypeDefinitionPager
        """
        return self._pager

    @pager.setter
    def pager(self, pager):
        """Sets the pager of this ODMcomplexTypeDefinitionUser.


        :param pager: The pager of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: ODMcomplexTypeDefinitionPager
        """

        self._pager = pager

    @property
    def fax(self):
        """Gets the fax of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The fax of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionFax]
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this ODMcomplexTypeDefinitionUser.


        :param fax: The fax of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionFax]
        """

        self._fax = fax

    @property
    def phone(self):
        """Gets the phone of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The phone of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionPhone]
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ODMcomplexTypeDefinitionUser.


        :param phone: The phone of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionPhone]
        """

        self._phone = phone

    @property
    def location_ref(self):
        """Gets the location_ref of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The location_ref of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionLocationRef]
        """
        return self._location_ref

    @location_ref.setter
    def location_ref(self, location_ref):
        """Sets the location_ref of this ODMcomplexTypeDefinitionUser.


        :param location_ref: The location_ref of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionLocationRef]
        """

        self._location_ref = location_ref

    @property
    def certificate(self):
        """Gets the certificate of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The certificate of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: list[ODMcomplexTypeDefinitionCertificate]
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ODMcomplexTypeDefinitionUser.


        :param certificate: The certificate of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: list[ODMcomplexTypeDefinitionCertificate]
        """

        self._certificate = certificate

    @property
    def oid(self):
        """Gets the oid of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The oid of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this ODMcomplexTypeDefinitionUser.


        :param oid: The oid of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def user_type(self):
        """Gets the user_type of this ODMcomplexTypeDefinitionUser.  # noqa: E501


        :return: The user_type of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this ODMcomplexTypeDefinitionUser.


        :param user_type: The user_type of this ODMcomplexTypeDefinitionUser.  # noqa: E501
        :type: str
        """
        allowed_values = ["SPONSOR", "INVESTIGATOR", "LAB", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and user_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

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
        if not isinstance(other, ODMcomplexTypeDefinitionUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionUser):
            return True

        return self.to_dict() != other.to_dict()