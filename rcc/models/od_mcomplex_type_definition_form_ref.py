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


class ODMcomplexTypeDefinitionFormRef(object):
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
        'default_version': 'str',
        'source_data_verification': 'str',
        'double_data_entry': 'bool',
        'display_sequence': 'int',
        'required_crf': 'bool',
        'hide_crf': 'bool',
        'accept_new_crf_versions': 'bool',
        'dynamic_form': 'bool',
        'source_data_verification_code': 'int',
        'repeating': 'str',
        'use_in_progress': 'bool',
        'form_oid': 'str',
        'order_number': 'int',
        'mandatory': 'str',
        'collection_exception_condition_oid': 'str',
        'monitoring': 'list[Monitoring]',
        'partial_sdv': 'list[PartialSDV]'
    }

    attribute_map = {
        'default_version': 'defaultVersion',
        'source_data_verification': 'sourceDataVerification',
        'double_data_entry': 'doubleDataEntry',
        'display_sequence': 'displaySequence',
        'required_crf': 'requiredCrf',
        'hide_crf': 'hideCrf',
        'accept_new_crf_versions': 'acceptNewCrfVersions',
        'dynamic_form': 'dynamicForm',
        'source_data_verification_code': 'sourceDataVerificationCode',
        'repeating': 'repeating',
        'use_in_progress': 'useInProgress',
        'form_oid': 'formOID',
        'order_number': 'orderNumber',
        'mandatory': 'mandatory',
        'collection_exception_condition_oid': 'collectionExceptionConditionOID',
        'monitoring': 'monitoring',
        'partial_sdv': 'partialSDV'
    }

    def __init__(self, default_version=None, source_data_verification=None, double_data_entry=None, display_sequence=None, required_crf=None, hide_crf=None, accept_new_crf_versions=None, dynamic_form=None, source_data_verification_code=None, repeating=None, use_in_progress=None, form_oid=None, order_number=None, mandatory=None, collection_exception_condition_oid=None, monitoring=None, partial_sdv=None, local_vars_configuration=None):  # noqa: E501
        """ODMcomplexTypeDefinitionFormRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_version = None
        self._source_data_verification = None
        self._double_data_entry = None
        self._display_sequence = None
        self._required_crf = None
        self._hide_crf = None
        self._accept_new_crf_versions = None
        self._dynamic_form = None
        self._source_data_verification_code = None
        self._repeating = None
        self._use_in_progress = None
        self._form_oid = None
        self._order_number = None
        self._mandatory = None
        self._collection_exception_condition_oid = None
        self._monitoring = None
        self._partial_sdv = None
        self.discriminator = None

        if default_version is not None:
            self.default_version = default_version
        if source_data_verification is not None:
            self.source_data_verification = source_data_verification
        if double_data_entry is not None:
            self.double_data_entry = double_data_entry
        if display_sequence is not None:
            self.display_sequence = display_sequence
        if required_crf is not None:
            self.required_crf = required_crf
        if hide_crf is not None:
            self.hide_crf = hide_crf
        if accept_new_crf_versions is not None:
            self.accept_new_crf_versions = accept_new_crf_versions
        if dynamic_form is not None:
            self.dynamic_form = dynamic_form
        if source_data_verification_code is not None:
            self.source_data_verification_code = source_data_verification_code
        if repeating is not None:
            self.repeating = repeating
        if use_in_progress is not None:
            self.use_in_progress = use_in_progress
        if form_oid is not None:
            self.form_oid = form_oid
        if order_number is not None:
            self.order_number = order_number
        if mandatory is not None:
            self.mandatory = mandatory
        if collection_exception_condition_oid is not None:
            self.collection_exception_condition_oid = collection_exception_condition_oid
        if monitoring is not None:
            self.monitoring = monitoring
        if partial_sdv is not None:
            self.partial_sdv = partial_sdv

    @property
    def default_version(self):
        """Gets the default_version of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The default_version of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: str
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        """Sets the default_version of this ODMcomplexTypeDefinitionFormRef.


        :param default_version: The default_version of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: str
        """

        self._default_version = default_version

    @property
    def source_data_verification(self):
        """Gets the source_data_verification of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The source_data_verification of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: str
        """
        return self._source_data_verification

    @source_data_verification.setter
    def source_data_verification(self, source_data_verification):
        """Sets the source_data_verification of this ODMcomplexTypeDefinitionFormRef.


        :param source_data_verification: The source_data_verification of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: str
        """

        self._source_data_verification = source_data_verification

    @property
    def double_data_entry(self):
        """Gets the double_data_entry of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The double_data_entry of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: bool
        """
        return self._double_data_entry

    @double_data_entry.setter
    def double_data_entry(self, double_data_entry):
        """Sets the double_data_entry of this ODMcomplexTypeDefinitionFormRef.


        :param double_data_entry: The double_data_entry of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: bool
        """

        self._double_data_entry = double_data_entry

    @property
    def display_sequence(self):
        """Gets the display_sequence of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The display_sequence of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: int
        """
        return self._display_sequence

    @display_sequence.setter
    def display_sequence(self, display_sequence):
        """Sets the display_sequence of this ODMcomplexTypeDefinitionFormRef.


        :param display_sequence: The display_sequence of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: int
        """

        self._display_sequence = display_sequence

    @property
    def required_crf(self):
        """Gets the required_crf of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The required_crf of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: bool
        """
        return self._required_crf

    @required_crf.setter
    def required_crf(self, required_crf):
        """Sets the required_crf of this ODMcomplexTypeDefinitionFormRef.


        :param required_crf: The required_crf of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: bool
        """

        self._required_crf = required_crf

    @property
    def hide_crf(self):
        """Gets the hide_crf of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The hide_crf of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: bool
        """
        return self._hide_crf

    @hide_crf.setter
    def hide_crf(self, hide_crf):
        """Sets the hide_crf of this ODMcomplexTypeDefinitionFormRef.


        :param hide_crf: The hide_crf of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: bool
        """

        self._hide_crf = hide_crf

    @property
    def accept_new_crf_versions(self):
        """Gets the accept_new_crf_versions of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The accept_new_crf_versions of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: bool
        """
        return self._accept_new_crf_versions

    @accept_new_crf_versions.setter
    def accept_new_crf_versions(self, accept_new_crf_versions):
        """Sets the accept_new_crf_versions of this ODMcomplexTypeDefinitionFormRef.


        :param accept_new_crf_versions: The accept_new_crf_versions of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: bool
        """

        self._accept_new_crf_versions = accept_new_crf_versions

    @property
    def dynamic_form(self):
        """Gets the dynamic_form of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The dynamic_form of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_form

    @dynamic_form.setter
    def dynamic_form(self, dynamic_form):
        """Sets the dynamic_form of this ODMcomplexTypeDefinitionFormRef.


        :param dynamic_form: The dynamic_form of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: bool
        """

        self._dynamic_form = dynamic_form

    @property
    def source_data_verification_code(self):
        """Gets the source_data_verification_code of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The source_data_verification_code of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: int
        """
        return self._source_data_verification_code

    @source_data_verification_code.setter
    def source_data_verification_code(self, source_data_verification_code):
        """Sets the source_data_verification_code of this ODMcomplexTypeDefinitionFormRef.


        :param source_data_verification_code: The source_data_verification_code of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: int
        """

        self._source_data_verification_code = source_data_verification_code

    @property
    def repeating(self):
        """Gets the repeating of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The repeating of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: str
        """
        return self._repeating

    @repeating.setter
    def repeating(self, repeating):
        """Sets the repeating of this ODMcomplexTypeDefinitionFormRef.


        :param repeating: The repeating of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and repeating not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `repeating` ({0}), must be one of {1}"  # noqa: E501
                .format(repeating, allowed_values)
            )

        self._repeating = repeating

    @property
    def use_in_progress(self):
        """Gets the use_in_progress of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The use_in_progress of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: bool
        """
        return self._use_in_progress

    @use_in_progress.setter
    def use_in_progress(self, use_in_progress):
        """Sets the use_in_progress of this ODMcomplexTypeDefinitionFormRef.


        :param use_in_progress: The use_in_progress of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: bool
        """

        self._use_in_progress = use_in_progress

    @property
    def form_oid(self):
        """Gets the form_oid of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The form_oid of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: str
        """
        return self._form_oid

    @form_oid.setter
    def form_oid(self, form_oid):
        """Sets the form_oid of this ODMcomplexTypeDefinitionFormRef.


        :param form_oid: The form_oid of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: str
        """

        self._form_oid = form_oid

    @property
    def order_number(self):
        """Gets the order_number of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The order_number of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: int
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this ODMcomplexTypeDefinitionFormRef.


        :param order_number: The order_number of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: int
        """

        self._order_number = order_number

    @property
    def mandatory(self):
        """Gets the mandatory of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The mandatory of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: str
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this ODMcomplexTypeDefinitionFormRef.


        :param mandatory: The mandatory of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mandatory not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mandatory` ({0}), must be one of {1}"  # noqa: E501
                .format(mandatory, allowed_values)
            )

        self._mandatory = mandatory

    @property
    def collection_exception_condition_oid(self):
        """Gets the collection_exception_condition_oid of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The collection_exception_condition_oid of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: str
        """
        return self._collection_exception_condition_oid

    @collection_exception_condition_oid.setter
    def collection_exception_condition_oid(self, collection_exception_condition_oid):
        """Sets the collection_exception_condition_oid of this ODMcomplexTypeDefinitionFormRef.


        :param collection_exception_condition_oid: The collection_exception_condition_oid of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: str
        """

        self._collection_exception_condition_oid = collection_exception_condition_oid

    @property
    def monitoring(self):
        """Gets the monitoring of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The monitoring of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: list[Monitoring]
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this ODMcomplexTypeDefinitionFormRef.


        :param monitoring: The monitoring of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: list[Monitoring]
        """

        self._monitoring = monitoring

    @property
    def partial_sdv(self):
        """Gets the partial_sdv of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501


        :return: The partial_sdv of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :rtype: list[PartialSDV]
        """
        return self._partial_sdv

    @partial_sdv.setter
    def partial_sdv(self, partial_sdv):
        """Sets the partial_sdv of this ODMcomplexTypeDefinitionFormRef.


        :param partial_sdv: The partial_sdv of this ODMcomplexTypeDefinitionFormRef.  # noqa: E501
        :type: list[PartialSDV]
        """

        self._partial_sdv = partial_sdv

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
        if not isinstance(other, ODMcomplexTypeDefinitionFormRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ODMcomplexTypeDefinitionFormRef):
            return True

        return self.to_dict() != other.to_dict()
