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


class Rule(object):
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
        'rule_target_section': 'list[RuleTargetSection]',
        'rule_target_event': 'list[RuleTargetEvent]',
        'name': 'str',
        'description': 'str',
        'target_item_var_name': 'str',
        'expression': 'str',
        'enabled': 'bool',
        'display_sequence': 'int',
        'action': 'int',
        'item_metadata_oid': 'str',
        'action_message': 'str',
        'action_addresses': 'str',
        'email_subject': 'str',
        'secondary_act_email': 'str',
        'target_event_name': 'str',
        'destination_event_name': 'str',
        'destination_crf_name': 'str',
        'add_repeating_crf_message': 'str',
        'assign_role_name': 'str',
        'assign_user_name': 'str',
        'add_dynamic_form_to_one_occurrence': 'bool'
    }

    attribute_map = {
        'rule_target_section': 'ruleTargetSection',
        'rule_target_event': 'ruleTargetEvent',
        'name': 'name',
        'description': 'description',
        'target_item_var_name': 'targetItemVarName',
        'expression': 'expression',
        'enabled': 'enabled',
        'display_sequence': 'displaySequence',
        'action': 'action',
        'item_metadata_oid': 'itemMetadataOID',
        'action_message': 'actionMessage',
        'action_addresses': 'actionAddresses',
        'email_subject': 'emailSubject',
        'secondary_act_email': 'secondaryActEmail',
        'target_event_name': 'targetEventName',
        'destination_event_name': 'destinationEventName',
        'destination_crf_name': 'destinationCrfName',
        'add_repeating_crf_message': 'addRepeatingCrfMessage',
        'assign_role_name': 'assignRoleName',
        'assign_user_name': 'assignUserName',
        'add_dynamic_form_to_one_occurrence': 'addDynamicFormToOneOccurrence'
    }

    def __init__(self, rule_target_section=None, rule_target_event=None, name=None, description=None, target_item_var_name=None, expression=None, enabled=None, display_sequence=None, action=None, item_metadata_oid=None, action_message=None, action_addresses=None, email_subject=None, secondary_act_email=None, target_event_name=None, destination_event_name=None, destination_crf_name=None, add_repeating_crf_message=None, assign_role_name=None, assign_user_name=None, add_dynamic_form_to_one_occurrence=None, local_vars_configuration=None):  # noqa: E501
        """Rule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rule_target_section = None
        self._rule_target_event = None
        self._name = None
        self._description = None
        self._target_item_var_name = None
        self._expression = None
        self._enabled = None
        self._display_sequence = None
        self._action = None
        self._item_metadata_oid = None
        self._action_message = None
        self._action_addresses = None
        self._email_subject = None
        self._secondary_act_email = None
        self._target_event_name = None
        self._destination_event_name = None
        self._destination_crf_name = None
        self._add_repeating_crf_message = None
        self._assign_role_name = None
        self._assign_user_name = None
        self._add_dynamic_form_to_one_occurrence = None
        self.discriminator = None

        if rule_target_section is not None:
            self.rule_target_section = rule_target_section
        if rule_target_event is not None:
            self.rule_target_event = rule_target_event
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if target_item_var_name is not None:
            self.target_item_var_name = target_item_var_name
        if expression is not None:
            self.expression = expression
        if enabled is not None:
            self.enabled = enabled
        if display_sequence is not None:
            self.display_sequence = display_sequence
        if action is not None:
            self.action = action
        if item_metadata_oid is not None:
            self.item_metadata_oid = item_metadata_oid
        if action_message is not None:
            self.action_message = action_message
        if action_addresses is not None:
            self.action_addresses = action_addresses
        if email_subject is not None:
            self.email_subject = email_subject
        if secondary_act_email is not None:
            self.secondary_act_email = secondary_act_email
        if target_event_name is not None:
            self.target_event_name = target_event_name
        if destination_event_name is not None:
            self.destination_event_name = destination_event_name
        if destination_crf_name is not None:
            self.destination_crf_name = destination_crf_name
        if add_repeating_crf_message is not None:
            self.add_repeating_crf_message = add_repeating_crf_message
        if assign_role_name is not None:
            self.assign_role_name = assign_role_name
        if assign_user_name is not None:
            self.assign_user_name = assign_user_name
        if add_dynamic_form_to_one_occurrence is not None:
            self.add_dynamic_form_to_one_occurrence = add_dynamic_form_to_one_occurrence

    @property
    def rule_target_section(self):
        """Gets the rule_target_section of this Rule.  # noqa: E501


        :return: The rule_target_section of this Rule.  # noqa: E501
        :rtype: list[RuleTargetSection]
        """
        return self._rule_target_section

    @rule_target_section.setter
    def rule_target_section(self, rule_target_section):
        """Sets the rule_target_section of this Rule.


        :param rule_target_section: The rule_target_section of this Rule.  # noqa: E501
        :type: list[RuleTargetSection]
        """

        self._rule_target_section = rule_target_section

    @property
    def rule_target_event(self):
        """Gets the rule_target_event of this Rule.  # noqa: E501


        :return: The rule_target_event of this Rule.  # noqa: E501
        :rtype: list[RuleTargetEvent]
        """
        return self._rule_target_event

    @rule_target_event.setter
    def rule_target_event(self, rule_target_event):
        """Sets the rule_target_event of this Rule.


        :param rule_target_event: The rule_target_event of this Rule.  # noqa: E501
        :type: list[RuleTargetEvent]
        """

        self._rule_target_event = rule_target_event

    @property
    def name(self):
        """Gets the name of this Rule.  # noqa: E501


        :return: The name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.


        :param name: The name of this Rule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Rule.  # noqa: E501


        :return: The description of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.


        :param description: The description of this Rule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def target_item_var_name(self):
        """Gets the target_item_var_name of this Rule.  # noqa: E501


        :return: The target_item_var_name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._target_item_var_name

    @target_item_var_name.setter
    def target_item_var_name(self, target_item_var_name):
        """Sets the target_item_var_name of this Rule.


        :param target_item_var_name: The target_item_var_name of this Rule.  # noqa: E501
        :type: str
        """

        self._target_item_var_name = target_item_var_name

    @property
    def expression(self):
        """Gets the expression of this Rule.  # noqa: E501


        :return: The expression of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Rule.


        :param expression: The expression of this Rule.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def enabled(self):
        """Gets the enabled of this Rule.  # noqa: E501


        :return: The enabled of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Rule.


        :param enabled: The enabled of this Rule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def display_sequence(self):
        """Gets the display_sequence of this Rule.  # noqa: E501


        :return: The display_sequence of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._display_sequence

    @display_sequence.setter
    def display_sequence(self, display_sequence):
        """Sets the display_sequence of this Rule.


        :param display_sequence: The display_sequence of this Rule.  # noqa: E501
        :type: int
        """

        self._display_sequence = display_sequence

    @property
    def action(self):
        """Gets the action of this Rule.  # noqa: E501


        :return: The action of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Rule.


        :param action: The action of this Rule.  # noqa: E501
        :type: int
        """

        self._action = action

    @property
    def item_metadata_oid(self):
        """Gets the item_metadata_oid of this Rule.  # noqa: E501


        :return: The item_metadata_oid of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._item_metadata_oid

    @item_metadata_oid.setter
    def item_metadata_oid(self, item_metadata_oid):
        """Sets the item_metadata_oid of this Rule.


        :param item_metadata_oid: The item_metadata_oid of this Rule.  # noqa: E501
        :type: str
        """

        self._item_metadata_oid = item_metadata_oid

    @property
    def action_message(self):
        """Gets the action_message of this Rule.  # noqa: E501


        :return: The action_message of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._action_message

    @action_message.setter
    def action_message(self, action_message):
        """Sets the action_message of this Rule.


        :param action_message: The action_message of this Rule.  # noqa: E501
        :type: str
        """

        self._action_message = action_message

    @property
    def action_addresses(self):
        """Gets the action_addresses of this Rule.  # noqa: E501


        :return: The action_addresses of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._action_addresses

    @action_addresses.setter
    def action_addresses(self, action_addresses):
        """Sets the action_addresses of this Rule.


        :param action_addresses: The action_addresses of this Rule.  # noqa: E501
        :type: str
        """

        self._action_addresses = action_addresses

    @property
    def email_subject(self):
        """Gets the email_subject of this Rule.  # noqa: E501


        :return: The email_subject of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this Rule.


        :param email_subject: The email_subject of this Rule.  # noqa: E501
        :type: str
        """

        self._email_subject = email_subject

    @property
    def secondary_act_email(self):
        """Gets the secondary_act_email of this Rule.  # noqa: E501


        :return: The secondary_act_email of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._secondary_act_email

    @secondary_act_email.setter
    def secondary_act_email(self, secondary_act_email):
        """Sets the secondary_act_email of this Rule.


        :param secondary_act_email: The secondary_act_email of this Rule.  # noqa: E501
        :type: str
        """

        self._secondary_act_email = secondary_act_email

    @property
    def target_event_name(self):
        """Gets the target_event_name of this Rule.  # noqa: E501


        :return: The target_event_name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._target_event_name

    @target_event_name.setter
    def target_event_name(self, target_event_name):
        """Sets the target_event_name of this Rule.


        :param target_event_name: The target_event_name of this Rule.  # noqa: E501
        :type: str
        """

        self._target_event_name = target_event_name

    @property
    def destination_event_name(self):
        """Gets the destination_event_name of this Rule.  # noqa: E501


        :return: The destination_event_name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._destination_event_name

    @destination_event_name.setter
    def destination_event_name(self, destination_event_name):
        """Sets the destination_event_name of this Rule.


        :param destination_event_name: The destination_event_name of this Rule.  # noqa: E501
        :type: str
        """

        self._destination_event_name = destination_event_name

    @property
    def destination_crf_name(self):
        """Gets the destination_crf_name of this Rule.  # noqa: E501


        :return: The destination_crf_name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._destination_crf_name

    @destination_crf_name.setter
    def destination_crf_name(self, destination_crf_name):
        """Sets the destination_crf_name of this Rule.


        :param destination_crf_name: The destination_crf_name of this Rule.  # noqa: E501
        :type: str
        """

        self._destination_crf_name = destination_crf_name

    @property
    def add_repeating_crf_message(self):
        """Gets the add_repeating_crf_message of this Rule.  # noqa: E501


        :return: The add_repeating_crf_message of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._add_repeating_crf_message

    @add_repeating_crf_message.setter
    def add_repeating_crf_message(self, add_repeating_crf_message):
        """Sets the add_repeating_crf_message of this Rule.


        :param add_repeating_crf_message: The add_repeating_crf_message of this Rule.  # noqa: E501
        :type: str
        """

        self._add_repeating_crf_message = add_repeating_crf_message

    @property
    def assign_role_name(self):
        """Gets the assign_role_name of this Rule.  # noqa: E501


        :return: The assign_role_name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._assign_role_name

    @assign_role_name.setter
    def assign_role_name(self, assign_role_name):
        """Sets the assign_role_name of this Rule.


        :param assign_role_name: The assign_role_name of this Rule.  # noqa: E501
        :type: str
        """

        self._assign_role_name = assign_role_name

    @property
    def assign_user_name(self):
        """Gets the assign_user_name of this Rule.  # noqa: E501


        :return: The assign_user_name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._assign_user_name

    @assign_user_name.setter
    def assign_user_name(self, assign_user_name):
        """Sets the assign_user_name of this Rule.


        :param assign_user_name: The assign_user_name of this Rule.  # noqa: E501
        :type: str
        """

        self._assign_user_name = assign_user_name

    @property
    def add_dynamic_form_to_one_occurrence(self):
        """Gets the add_dynamic_form_to_one_occurrence of this Rule.  # noqa: E501


        :return: The add_dynamic_form_to_one_occurrence of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._add_dynamic_form_to_one_occurrence

    @add_dynamic_form_to_one_occurrence.setter
    def add_dynamic_form_to_one_occurrence(self, add_dynamic_form_to_one_occurrence):
        """Sets the add_dynamic_form_to_one_occurrence of this Rule.


        :param add_dynamic_form_to_one_occurrence: The add_dynamic_form_to_one_occurrence of this Rule.  # noqa: E501
        :type: bool
        """

        self._add_dynamic_form_to_one_occurrence = add_dynamic_form_to_one_occurrence

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
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
