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


class SubjectViewRpc(object):
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
        'client_id': 'int',
        'study_id': 'int',
        'unique_identifier': 'str',
        'rc_oid': 'str',
        'study_site_id': 'int',
        'study_site_name': 'str',
        'protocol_id': 'str',
        'date_screened': 'int',
        'update_date': 'int',
        'status_id': 'int',
        'status': 'str',
        'initials': 'str',
        'email': 'str',
        'screening_number': 'str',
        'randomization_id': 'int',
        'crf_version_screening_id': 'int',
        'force_manual_subject_number': 'bool',
        'custom_enroll_crf_used': 'bool',
        'mrn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'client_id': 'clientId',
        'study_id': 'studyId',
        'unique_identifier': 'uniqueIdentifier',
        'rc_oid': 'rcOid',
        'study_site_id': 'studySiteId',
        'study_site_name': 'studySiteName',
        'protocol_id': 'protocolId',
        'date_screened': 'dateScreened',
        'update_date': 'updateDate',
        'status_id': 'statusId',
        'status': 'status',
        'initials': 'initials',
        'email': 'email',
        'screening_number': 'screeningNumber',
        'randomization_id': 'randomizationId',
        'crf_version_screening_id': 'crfVersionScreeningId',
        'force_manual_subject_number': 'forceManualSubjectNumber',
        'custom_enroll_crf_used': 'customEnrollCrfUsed',
        'mrn': 'mrn'
    }

    def __init__(self, id=None, client_id=None, study_id=None, unique_identifier=None, rc_oid=None, study_site_id=None, study_site_name=None, protocol_id=None, date_screened=None, update_date=None, status_id=None, status=None, initials=None, email=None, screening_number=None, randomization_id=None, crf_version_screening_id=None, force_manual_subject_number=None, custom_enroll_crf_used=None, mrn=None, local_vars_configuration=None):  # noqa: E501
        """SubjectViewRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._client_id = None
        self._study_id = None
        self._unique_identifier = None
        self._rc_oid = None
        self._study_site_id = None
        self._study_site_name = None
        self._protocol_id = None
        self._date_screened = None
        self._update_date = None
        self._status_id = None
        self._status = None
        self._initials = None
        self._email = None
        self._screening_number = None
        self._randomization_id = None
        self._crf_version_screening_id = None
        self._force_manual_subject_number = None
        self._custom_enroll_crf_used = None
        self._mrn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if client_id is not None:
            self.client_id = client_id
        if study_id is not None:
            self.study_id = study_id
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if rc_oid is not None:
            self.rc_oid = rc_oid
        if study_site_id is not None:
            self.study_site_id = study_site_id
        if study_site_name is not None:
            self.study_site_name = study_site_name
        if protocol_id is not None:
            self.protocol_id = protocol_id
        if date_screened is not None:
            self.date_screened = date_screened
        if update_date is not None:
            self.update_date = update_date
        if status_id is not None:
            self.status_id = status_id
        if status is not None:
            self.status = status
        if initials is not None:
            self.initials = initials
        if email is not None:
            self.email = email
        if screening_number is not None:
            self.screening_number = screening_number
        if randomization_id is not None:
            self.randomization_id = randomization_id
        if crf_version_screening_id is not None:
            self.crf_version_screening_id = crf_version_screening_id
        if force_manual_subject_number is not None:
            self.force_manual_subject_number = force_manual_subject_number
        if custom_enroll_crf_used is not None:
            self.custom_enroll_crf_used = custom_enroll_crf_used
        if mrn is not None:
            self.mrn = mrn

    @property
    def id(self):
        """Gets the id of this SubjectViewRpc.  # noqa: E501


        :return: The id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubjectViewRpc.


        :param id: The id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def client_id(self):
        """Gets the client_id of this SubjectViewRpc.  # noqa: E501


        :return: The client_id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SubjectViewRpc.


        :param client_id: The client_id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def study_id(self):
        """Gets the study_id of this SubjectViewRpc.  # noqa: E501


        :return: The study_id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this SubjectViewRpc.


        :param study_id: The study_id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._study_id = study_id

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this SubjectViewRpc.  # noqa: E501

        Unique Subject Identifier. Used to refer the subject.  # noqa: E501

        :return: The unique_identifier of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this SubjectViewRpc.

        Unique Subject Identifier. Used to refer the subject.  # noqa: E501

        :param unique_identifier: The unique_identifier of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def rc_oid(self):
        """Gets the rc_oid of this SubjectViewRpc.  # noqa: E501


        :return: The rc_oid of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._rc_oid

    @rc_oid.setter
    def rc_oid(self, rc_oid):
        """Sets the rc_oid of this SubjectViewRpc.


        :param rc_oid: The rc_oid of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._rc_oid = rc_oid

    @property
    def study_site_id(self):
        """Gets the study_site_id of this SubjectViewRpc.  # noqa: E501


        :return: The study_site_id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_site_id

    @study_site_id.setter
    def study_site_id(self, study_site_id):
        """Sets the study_site_id of this SubjectViewRpc.


        :param study_site_id: The study_site_id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._study_site_id = study_site_id

    @property
    def study_site_name(self):
        """Gets the study_site_name of this SubjectViewRpc.  # noqa: E501

        Site name for Subject Site. Virtual field.  # noqa: E501

        :return: The study_site_name of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._study_site_name

    @study_site_name.setter
    def study_site_name(self, study_site_name):
        """Sets the study_site_name of this SubjectViewRpc.

        Site name for Subject Site. Virtual field.  # noqa: E501

        :param study_site_name: The study_site_name of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._study_site_name = study_site_name

    @property
    def protocol_id(self):
        """Gets the protocol_id of this SubjectViewRpc.  # noqa: E501


        :return: The protocol_id of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._protocol_id

    @protocol_id.setter
    def protocol_id(self, protocol_id):
        """Sets the protocol_id of this SubjectViewRpc.


        :param protocol_id: The protocol_id of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._protocol_id = protocol_id

    @property
    def date_screened(self):
        """Gets the date_screened of this SubjectViewRpc.  # noqa: E501


        :return: The date_screened of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._date_screened

    @date_screened.setter
    def date_screened(self, date_screened):
        """Sets the date_screened of this SubjectViewRpc.


        :param date_screened: The date_screened of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._date_screened = date_screened

    @property
    def update_date(self):
        """Gets the update_date of this SubjectViewRpc.  # noqa: E501


        :return: The update_date of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this SubjectViewRpc.


        :param update_date: The update_date of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._update_date = update_date

    @property
    def status_id(self):
        """Gets the status_id of this SubjectViewRpc.  # noqa: E501


        :return: The status_id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this SubjectViewRpc.


        :param status_id: The status_id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._status_id = status_id

    @property
    def status(self):
        """Gets the status of this SubjectViewRpc.  # noqa: E501

        Subject status property  # noqa: E501

        :return: The status of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubjectViewRpc.

        Subject status property  # noqa: E501

        :param status: The status of this SubjectViewRpc.  # noqa: E501
        :type: str
        """
        allowed_values = ["Enrolled", "Not Enrolled", "Incomplete", "Removed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def initials(self):
        """Gets the initials of this SubjectViewRpc.  # noqa: E501


        :return: The initials of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._initials

    @initials.setter
    def initials(self, initials):
        """Sets the initials of this SubjectViewRpc.


        :param initials: The initials of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._initials = initials

    @property
    def email(self):
        """Gets the email of this SubjectViewRpc.  # noqa: E501


        :return: The email of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SubjectViewRpc.


        :param email: The email of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def screening_number(self):
        """Gets the screening_number of this SubjectViewRpc.  # noqa: E501


        :return: The screening_number of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._screening_number

    @screening_number.setter
    def screening_number(self, screening_number):
        """Sets the screening_number of this SubjectViewRpc.


        :param screening_number: The screening_number of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._screening_number = screening_number

    @property
    def randomization_id(self):
        """Gets the randomization_id of this SubjectViewRpc.  # noqa: E501


        :return: The randomization_id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._randomization_id

    @randomization_id.setter
    def randomization_id(self, randomization_id):
        """Sets the randomization_id of this SubjectViewRpc.


        :param randomization_id: The randomization_id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._randomization_id = randomization_id

    @property
    def crf_version_screening_id(self):
        """Gets the crf_version_screening_id of this SubjectViewRpc.  # noqa: E501

        ID of Screening CRF Version  # noqa: E501

        :return: The crf_version_screening_id of this SubjectViewRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_version_screening_id

    @crf_version_screening_id.setter
    def crf_version_screening_id(self, crf_version_screening_id):
        """Sets the crf_version_screening_id of this SubjectViewRpc.

        ID of Screening CRF Version  # noqa: E501

        :param crf_version_screening_id: The crf_version_screening_id of this SubjectViewRpc.  # noqa: E501
        :type: int
        """

        self._crf_version_screening_id = crf_version_screening_id

    @property
    def force_manual_subject_number(self):
        """Gets the force_manual_subject_number of this SubjectViewRpc.  # noqa: E501

        Flag shows how to generate Subject Number. By default it is manual subject number.  # noqa: E501

        :return: The force_manual_subject_number of this SubjectViewRpc.  # noqa: E501
        :rtype: bool
        """
        return self._force_manual_subject_number

    @force_manual_subject_number.setter
    def force_manual_subject_number(self, force_manual_subject_number):
        """Sets the force_manual_subject_number of this SubjectViewRpc.

        Flag shows how to generate Subject Number. By default it is manual subject number.  # noqa: E501

        :param force_manual_subject_number: The force_manual_subject_number of this SubjectViewRpc.  # noqa: E501
        :type: bool
        """

        self._force_manual_subject_number = force_manual_subject_number

    @property
    def custom_enroll_crf_used(self):
        """Gets the custom_enroll_crf_used of this SubjectViewRpc.  # noqa: E501


        :return: The custom_enroll_crf_used of this SubjectViewRpc.  # noqa: E501
        :rtype: bool
        """
        return self._custom_enroll_crf_used

    @custom_enroll_crf_used.setter
    def custom_enroll_crf_used(self, custom_enroll_crf_used):
        """Sets the custom_enroll_crf_used of this SubjectViewRpc.


        :param custom_enroll_crf_used: The custom_enroll_crf_used of this SubjectViewRpc.  # noqa: E501
        :type: bool
        """

        self._custom_enroll_crf_used = custom_enroll_crf_used

    @property
    def mrn(self):
        """Gets the mrn of this SubjectViewRpc.  # noqa: E501


        :return: The mrn of this SubjectViewRpc.  # noqa: E501
        :rtype: str
        """
        return self._mrn

    @mrn.setter
    def mrn(self, mrn):
        """Sets the mrn of this SubjectViewRpc.


        :param mrn: The mrn of this SubjectViewRpc.  # noqa: E501
        :type: str
        """

        self._mrn = mrn

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
        if not isinstance(other, SubjectViewRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubjectViewRpc):
            return True

        return self.to_dict() != other.to_dict()
