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


class SurveyRpc(object):
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
        'logo_url': 'str',
        'acknowledgement': 'str',
        'question_auto_numbering': 'int',
        'question_by_section': 'int',
        'display_page_number': 'bool',
        'hide_back_button': 'bool',
        'show_required_field_text': 'bool',
        'view_results': 'int',
        'min_responses_view_results': 'int',
        'check_diversity_view_results': 'bool',
        'survey_expiration': 'int',
        'save_and_return': 'bool',
        'hide_submit': 'bool',
        'customize_time_availability': 'bool',
        'close_after_completion': 'bool',
        'availability_from_time': 'str',
        'availability_to_time': 'str',
        'edit_completed_response': 'bool',
        'end_survey_redirect_url': 'str',
        'end_survey_redirect_to_my_health': 'bool',
        'survey_redirect_message': 'str',
        'survey_thank_you_message': 'str',
        'promise_skip_question': 'bool',
        'survey_auth_enabled_single': 'bool',
        'send_confirmation_email': 'bool',
        'confirmation_email_subject': 'str',
        'confirmation_email_content': 'str',
        'confirmation_email_from': 'str',
        'study_id': 'int',
        'crf_version_id': 'int',
        'instructions': 'str',
        'enabled': 'bool',
        'hide_title': 'bool',
        'calendared_invitation_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'logo_url': 'logoUrl',
        'acknowledgement': 'acknowledgement',
        'question_auto_numbering': 'questionAutoNumbering',
        'question_by_section': 'questionBySection',
        'display_page_number': 'displayPageNumber',
        'hide_back_button': 'hideBackButton',
        'show_required_field_text': 'showRequiredFieldText',
        'view_results': 'viewResults',
        'min_responses_view_results': 'minResponsesViewResults',
        'check_diversity_view_results': 'checkDiversityViewResults',
        'survey_expiration': 'surveyExpiration',
        'save_and_return': 'saveAndReturn',
        'hide_submit': 'hideSubmit',
        'customize_time_availability': 'customizeTimeAvailability',
        'close_after_completion': 'closeAfterCompletion',
        'availability_from_time': 'availabilityFromTime',
        'availability_to_time': 'availabilityToTime',
        'edit_completed_response': 'editCompletedResponse',
        'end_survey_redirect_url': 'endSurveyRedirectUrl',
        'end_survey_redirect_to_my_health': 'endSurveyRedirectToMyHealth',
        'survey_redirect_message': 'surveyRedirectMessage',
        'survey_thank_you_message': 'surveyThankYouMessage',
        'promise_skip_question': 'promiseSkipQuestion',
        'survey_auth_enabled_single': 'surveyAuthEnabledSingle',
        'send_confirmation_email': 'sendConfirmationEmail',
        'confirmation_email_subject': 'confirmationEmailSubject',
        'confirmation_email_content': 'confirmationEmailContent',
        'confirmation_email_from': 'confirmationEmailFrom',
        'study_id': 'studyId',
        'crf_version_id': 'crfVersionId',
        'instructions': 'instructions',
        'enabled': 'enabled',
        'hide_title': 'hideTitle',
        'calendared_invitation_enabled': 'calendaredInvitationEnabled'
    }

    def __init__(self, id=None, title=None, logo_url=None, acknowledgement=None, question_auto_numbering=None, question_by_section=None, display_page_number=None, hide_back_button=None, show_required_field_text=None, view_results=None, min_responses_view_results=None, check_diversity_view_results=None, survey_expiration=None, save_and_return=None, hide_submit=None, customize_time_availability=None, close_after_completion=None, availability_from_time=None, availability_to_time=None, edit_completed_response=None, end_survey_redirect_url=None, end_survey_redirect_to_my_health=None, survey_redirect_message=None, survey_thank_you_message=None, promise_skip_question=None, survey_auth_enabled_single=None, send_confirmation_email=None, confirmation_email_subject=None, confirmation_email_content=None, confirmation_email_from=None, study_id=None, crf_version_id=None, instructions=None, enabled=None, hide_title=None, calendared_invitation_enabled=None, local_vars_configuration=None):  # noqa: E501
        """SurveyRpc - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._logo_url = None
        self._acknowledgement = None
        self._question_auto_numbering = None
        self._question_by_section = None
        self._display_page_number = None
        self._hide_back_button = None
        self._show_required_field_text = None
        self._view_results = None
        self._min_responses_view_results = None
        self._check_diversity_view_results = None
        self._survey_expiration = None
        self._save_and_return = None
        self._hide_submit = None
        self._customize_time_availability = None
        self._close_after_completion = None
        self._availability_from_time = None
        self._availability_to_time = None
        self._edit_completed_response = None
        self._end_survey_redirect_url = None
        self._end_survey_redirect_to_my_health = None
        self._survey_redirect_message = None
        self._survey_thank_you_message = None
        self._promise_skip_question = None
        self._survey_auth_enabled_single = None
        self._send_confirmation_email = None
        self._confirmation_email_subject = None
        self._confirmation_email_content = None
        self._confirmation_email_from = None
        self._study_id = None
        self._crf_version_id = None
        self._instructions = None
        self._enabled = None
        self._hide_title = None
        self._calendared_invitation_enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if logo_url is not None:
            self.logo_url = logo_url
        if acknowledgement is not None:
            self.acknowledgement = acknowledgement
        if question_auto_numbering is not None:
            self.question_auto_numbering = question_auto_numbering
        if question_by_section is not None:
            self.question_by_section = question_by_section
        if display_page_number is not None:
            self.display_page_number = display_page_number
        if hide_back_button is not None:
            self.hide_back_button = hide_back_button
        if show_required_field_text is not None:
            self.show_required_field_text = show_required_field_text
        if view_results is not None:
            self.view_results = view_results
        if min_responses_view_results is not None:
            self.min_responses_view_results = min_responses_view_results
        if check_diversity_view_results is not None:
            self.check_diversity_view_results = check_diversity_view_results
        if survey_expiration is not None:
            self.survey_expiration = survey_expiration
        if save_and_return is not None:
            self.save_and_return = save_and_return
        if hide_submit is not None:
            self.hide_submit = hide_submit
        if customize_time_availability is not None:
            self.customize_time_availability = customize_time_availability
        if close_after_completion is not None:
            self.close_after_completion = close_after_completion
        if availability_from_time is not None:
            self.availability_from_time = availability_from_time
        if availability_to_time is not None:
            self.availability_to_time = availability_to_time
        if edit_completed_response is not None:
            self.edit_completed_response = edit_completed_response
        if end_survey_redirect_url is not None:
            self.end_survey_redirect_url = end_survey_redirect_url
        if end_survey_redirect_to_my_health is not None:
            self.end_survey_redirect_to_my_health = end_survey_redirect_to_my_health
        if survey_redirect_message is not None:
            self.survey_redirect_message = survey_redirect_message
        if survey_thank_you_message is not None:
            self.survey_thank_you_message = survey_thank_you_message
        if promise_skip_question is not None:
            self.promise_skip_question = promise_skip_question
        if survey_auth_enabled_single is not None:
            self.survey_auth_enabled_single = survey_auth_enabled_single
        if send_confirmation_email is not None:
            self.send_confirmation_email = send_confirmation_email
        if confirmation_email_subject is not None:
            self.confirmation_email_subject = confirmation_email_subject
        if confirmation_email_content is not None:
            self.confirmation_email_content = confirmation_email_content
        if confirmation_email_from is not None:
            self.confirmation_email_from = confirmation_email_from
        if study_id is not None:
            self.study_id = study_id
        if crf_version_id is not None:
            self.crf_version_id = crf_version_id
        if instructions is not None:
            self.instructions = instructions
        if enabled is not None:
            self.enabled = enabled
        if hide_title is not None:
            self.hide_title = hide_title
        if calendared_invitation_enabled is not None:
            self.calendared_invitation_enabled = calendared_invitation_enabled

    @property
    def id(self):
        """Gets the id of this SurveyRpc.  # noqa: E501


        :return: The id of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SurveyRpc.


        :param id: The id of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this SurveyRpc.  # noqa: E501


        :return: The title of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SurveyRpc.


        :param title: The title of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def logo_url(self):
        """Gets the logo_url of this SurveyRpc.  # noqa: E501


        :return: The logo_url of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this SurveyRpc.


        :param logo_url: The logo_url of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def acknowledgement(self):
        """Gets the acknowledgement of this SurveyRpc.  # noqa: E501


        :return: The acknowledgement of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._acknowledgement

    @acknowledgement.setter
    def acknowledgement(self, acknowledgement):
        """Sets the acknowledgement of this SurveyRpc.


        :param acknowledgement: The acknowledgement of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._acknowledgement = acknowledgement

    @property
    def question_auto_numbering(self):
        """Gets the question_auto_numbering of this SurveyRpc.  # noqa: E501


        :return: The question_auto_numbering of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._question_auto_numbering

    @question_auto_numbering.setter
    def question_auto_numbering(self, question_auto_numbering):
        """Sets the question_auto_numbering of this SurveyRpc.


        :param question_auto_numbering: The question_auto_numbering of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._question_auto_numbering = question_auto_numbering

    @property
    def question_by_section(self):
        """Gets the question_by_section of this SurveyRpc.  # noqa: E501


        :return: The question_by_section of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._question_by_section

    @question_by_section.setter
    def question_by_section(self, question_by_section):
        """Sets the question_by_section of this SurveyRpc.


        :param question_by_section: The question_by_section of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._question_by_section = question_by_section

    @property
    def display_page_number(self):
        """Gets the display_page_number of this SurveyRpc.  # noqa: E501


        :return: The display_page_number of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._display_page_number

    @display_page_number.setter
    def display_page_number(self, display_page_number):
        """Sets the display_page_number of this SurveyRpc.


        :param display_page_number: The display_page_number of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._display_page_number = display_page_number

    @property
    def hide_back_button(self):
        """Gets the hide_back_button of this SurveyRpc.  # noqa: E501


        :return: The hide_back_button of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._hide_back_button

    @hide_back_button.setter
    def hide_back_button(self, hide_back_button):
        """Sets the hide_back_button of this SurveyRpc.


        :param hide_back_button: The hide_back_button of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._hide_back_button = hide_back_button

    @property
    def show_required_field_text(self):
        """Gets the show_required_field_text of this SurveyRpc.  # noqa: E501


        :return: The show_required_field_text of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._show_required_field_text

    @show_required_field_text.setter
    def show_required_field_text(self, show_required_field_text):
        """Sets the show_required_field_text of this SurveyRpc.


        :param show_required_field_text: The show_required_field_text of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._show_required_field_text = show_required_field_text

    @property
    def view_results(self):
        """Gets the view_results of this SurveyRpc.  # noqa: E501


        :return: The view_results of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._view_results

    @view_results.setter
    def view_results(self, view_results):
        """Sets the view_results of this SurveyRpc.


        :param view_results: The view_results of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._view_results = view_results

    @property
    def min_responses_view_results(self):
        """Gets the min_responses_view_results of this SurveyRpc.  # noqa: E501


        :return: The min_responses_view_results of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._min_responses_view_results

    @min_responses_view_results.setter
    def min_responses_view_results(self, min_responses_view_results):
        """Sets the min_responses_view_results of this SurveyRpc.


        :param min_responses_view_results: The min_responses_view_results of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._min_responses_view_results = min_responses_view_results

    @property
    def check_diversity_view_results(self):
        """Gets the check_diversity_view_results of this SurveyRpc.  # noqa: E501


        :return: The check_diversity_view_results of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._check_diversity_view_results

    @check_diversity_view_results.setter
    def check_diversity_view_results(self, check_diversity_view_results):
        """Sets the check_diversity_view_results of this SurveyRpc.


        :param check_diversity_view_results: The check_diversity_view_results of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._check_diversity_view_results = check_diversity_view_results

    @property
    def survey_expiration(self):
        """Gets the survey_expiration of this SurveyRpc.  # noqa: E501


        :return: The survey_expiration of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._survey_expiration

    @survey_expiration.setter
    def survey_expiration(self, survey_expiration):
        """Sets the survey_expiration of this SurveyRpc.


        :param survey_expiration: The survey_expiration of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._survey_expiration = survey_expiration

    @property
    def save_and_return(self):
        """Gets the save_and_return of this SurveyRpc.  # noqa: E501


        :return: The save_and_return of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._save_and_return

    @save_and_return.setter
    def save_and_return(self, save_and_return):
        """Sets the save_and_return of this SurveyRpc.


        :param save_and_return: The save_and_return of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._save_and_return = save_and_return

    @property
    def hide_submit(self):
        """Gets the hide_submit of this SurveyRpc.  # noqa: E501


        :return: The hide_submit of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._hide_submit

    @hide_submit.setter
    def hide_submit(self, hide_submit):
        """Sets the hide_submit of this SurveyRpc.


        :param hide_submit: The hide_submit of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._hide_submit = hide_submit

    @property
    def customize_time_availability(self):
        """Gets the customize_time_availability of this SurveyRpc.  # noqa: E501


        :return: The customize_time_availability of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._customize_time_availability

    @customize_time_availability.setter
    def customize_time_availability(self, customize_time_availability):
        """Sets the customize_time_availability of this SurveyRpc.


        :param customize_time_availability: The customize_time_availability of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._customize_time_availability = customize_time_availability

    @property
    def close_after_completion(self):
        """Gets the close_after_completion of this SurveyRpc.  # noqa: E501


        :return: The close_after_completion of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._close_after_completion

    @close_after_completion.setter
    def close_after_completion(self, close_after_completion):
        """Sets the close_after_completion of this SurveyRpc.


        :param close_after_completion: The close_after_completion of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._close_after_completion = close_after_completion

    @property
    def availability_from_time(self):
        """Gets the availability_from_time of this SurveyRpc.  # noqa: E501


        :return: The availability_from_time of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._availability_from_time

    @availability_from_time.setter
    def availability_from_time(self, availability_from_time):
        """Sets the availability_from_time of this SurveyRpc.


        :param availability_from_time: The availability_from_time of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._availability_from_time = availability_from_time

    @property
    def availability_to_time(self):
        """Gets the availability_to_time of this SurveyRpc.  # noqa: E501


        :return: The availability_to_time of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._availability_to_time

    @availability_to_time.setter
    def availability_to_time(self, availability_to_time):
        """Sets the availability_to_time of this SurveyRpc.


        :param availability_to_time: The availability_to_time of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._availability_to_time = availability_to_time

    @property
    def edit_completed_response(self):
        """Gets the edit_completed_response of this SurveyRpc.  # noqa: E501


        :return: The edit_completed_response of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._edit_completed_response

    @edit_completed_response.setter
    def edit_completed_response(self, edit_completed_response):
        """Sets the edit_completed_response of this SurveyRpc.


        :param edit_completed_response: The edit_completed_response of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._edit_completed_response = edit_completed_response

    @property
    def end_survey_redirect_url(self):
        """Gets the end_survey_redirect_url of this SurveyRpc.  # noqa: E501


        :return: The end_survey_redirect_url of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._end_survey_redirect_url

    @end_survey_redirect_url.setter
    def end_survey_redirect_url(self, end_survey_redirect_url):
        """Sets the end_survey_redirect_url of this SurveyRpc.


        :param end_survey_redirect_url: The end_survey_redirect_url of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._end_survey_redirect_url = end_survey_redirect_url

    @property
    def end_survey_redirect_to_my_health(self):
        """Gets the end_survey_redirect_to_my_health of this SurveyRpc.  # noqa: E501


        :return: The end_survey_redirect_to_my_health of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._end_survey_redirect_to_my_health

    @end_survey_redirect_to_my_health.setter
    def end_survey_redirect_to_my_health(self, end_survey_redirect_to_my_health):
        """Sets the end_survey_redirect_to_my_health of this SurveyRpc.


        :param end_survey_redirect_to_my_health: The end_survey_redirect_to_my_health of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._end_survey_redirect_to_my_health = end_survey_redirect_to_my_health

    @property
    def survey_redirect_message(self):
        """Gets the survey_redirect_message of this SurveyRpc.  # noqa: E501


        :return: The survey_redirect_message of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._survey_redirect_message

    @survey_redirect_message.setter
    def survey_redirect_message(self, survey_redirect_message):
        """Sets the survey_redirect_message of this SurveyRpc.


        :param survey_redirect_message: The survey_redirect_message of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._survey_redirect_message = survey_redirect_message

    @property
    def survey_thank_you_message(self):
        """Gets the survey_thank_you_message of this SurveyRpc.  # noqa: E501


        :return: The survey_thank_you_message of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._survey_thank_you_message

    @survey_thank_you_message.setter
    def survey_thank_you_message(self, survey_thank_you_message):
        """Sets the survey_thank_you_message of this SurveyRpc.


        :param survey_thank_you_message: The survey_thank_you_message of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._survey_thank_you_message = survey_thank_you_message

    @property
    def promise_skip_question(self):
        """Gets the promise_skip_question of this SurveyRpc.  # noqa: E501


        :return: The promise_skip_question of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._promise_skip_question

    @promise_skip_question.setter
    def promise_skip_question(self, promise_skip_question):
        """Sets the promise_skip_question of this SurveyRpc.


        :param promise_skip_question: The promise_skip_question of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._promise_skip_question = promise_skip_question

    @property
    def survey_auth_enabled_single(self):
        """Gets the survey_auth_enabled_single of this SurveyRpc.  # noqa: E501


        :return: The survey_auth_enabled_single of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._survey_auth_enabled_single

    @survey_auth_enabled_single.setter
    def survey_auth_enabled_single(self, survey_auth_enabled_single):
        """Sets the survey_auth_enabled_single of this SurveyRpc.


        :param survey_auth_enabled_single: The survey_auth_enabled_single of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._survey_auth_enabled_single = survey_auth_enabled_single

    @property
    def send_confirmation_email(self):
        """Gets the send_confirmation_email of this SurveyRpc.  # noqa: E501


        :return: The send_confirmation_email of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._send_confirmation_email

    @send_confirmation_email.setter
    def send_confirmation_email(self, send_confirmation_email):
        """Sets the send_confirmation_email of this SurveyRpc.


        :param send_confirmation_email: The send_confirmation_email of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._send_confirmation_email = send_confirmation_email

    @property
    def confirmation_email_subject(self):
        """Gets the confirmation_email_subject of this SurveyRpc.  # noqa: E501


        :return: The confirmation_email_subject of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_email_subject

    @confirmation_email_subject.setter
    def confirmation_email_subject(self, confirmation_email_subject):
        """Sets the confirmation_email_subject of this SurveyRpc.


        :param confirmation_email_subject: The confirmation_email_subject of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._confirmation_email_subject = confirmation_email_subject

    @property
    def confirmation_email_content(self):
        """Gets the confirmation_email_content of this SurveyRpc.  # noqa: E501


        :return: The confirmation_email_content of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_email_content

    @confirmation_email_content.setter
    def confirmation_email_content(self, confirmation_email_content):
        """Sets the confirmation_email_content of this SurveyRpc.


        :param confirmation_email_content: The confirmation_email_content of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._confirmation_email_content = confirmation_email_content

    @property
    def confirmation_email_from(self):
        """Gets the confirmation_email_from of this SurveyRpc.  # noqa: E501


        :return: The confirmation_email_from of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._confirmation_email_from

    @confirmation_email_from.setter
    def confirmation_email_from(self, confirmation_email_from):
        """Sets the confirmation_email_from of this SurveyRpc.


        :param confirmation_email_from: The confirmation_email_from of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._confirmation_email_from = confirmation_email_from

    @property
    def study_id(self):
        """Gets the study_id of this SurveyRpc.  # noqa: E501


        :return: The study_id of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this SurveyRpc.


        :param study_id: The study_id of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._study_id = study_id

    @property
    def crf_version_id(self):
        """Gets the crf_version_id of this SurveyRpc.  # noqa: E501


        :return: The crf_version_id of this SurveyRpc.  # noqa: E501
        :rtype: int
        """
        return self._crf_version_id

    @crf_version_id.setter
    def crf_version_id(self, crf_version_id):
        """Sets the crf_version_id of this SurveyRpc.


        :param crf_version_id: The crf_version_id of this SurveyRpc.  # noqa: E501
        :type: int
        """

        self._crf_version_id = crf_version_id

    @property
    def instructions(self):
        """Gets the instructions of this SurveyRpc.  # noqa: E501


        :return: The instructions of this SurveyRpc.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this SurveyRpc.


        :param instructions: The instructions of this SurveyRpc.  # noqa: E501
        :type: str
        """

        self._instructions = instructions

    @property
    def enabled(self):
        """Gets the enabled of this SurveyRpc.  # noqa: E501


        :return: The enabled of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SurveyRpc.


        :param enabled: The enabled of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def hide_title(self):
        """Gets the hide_title of this SurveyRpc.  # noqa: E501


        :return: The hide_title of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._hide_title

    @hide_title.setter
    def hide_title(self, hide_title):
        """Sets the hide_title of this SurveyRpc.


        :param hide_title: The hide_title of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._hide_title = hide_title

    @property
    def calendared_invitation_enabled(self):
        """Gets the calendared_invitation_enabled of this SurveyRpc.  # noqa: E501


        :return: The calendared_invitation_enabled of this SurveyRpc.  # noqa: E501
        :rtype: bool
        """
        return self._calendared_invitation_enabled

    @calendared_invitation_enabled.setter
    def calendared_invitation_enabled(self, calendared_invitation_enabled):
        """Sets the calendared_invitation_enabled of this SurveyRpc.


        :param calendared_invitation_enabled: The calendared_invitation_enabled of this SurveyRpc.  # noqa: E501
        :type: bool
        """

        self._calendared_invitation_enabled = calendared_invitation_enabled

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
        if not isinstance(other, SurveyRpc):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SurveyRpc):
            return True

        return self.to_dict() != other.to_dict()
