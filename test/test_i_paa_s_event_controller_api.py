# coding: utf-8

"""
    nPhase REST Resource

    REDCap REST API v.2  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import rcc
from rcc.api.i_paa_s_event_controller_api import IPaaSEventControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestIPaaSEventControllerApi(unittest.TestCase):
    """IPaaSEventControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.i_paa_s_event_controller_api.IPaaSEventControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_batch_prepare_encounter(self):
        """Test case for batch_prepare_encounter

        Prepares subject event or event CRF to be stored in RCC. No changes will be reflected in RCC immediately. This is an intermediate operation.  # noqa: E501
        """
        pass

    def test_batch_save_encounter(self):
        """Test case for batch_save_encounter

        Submits prepared subject events and event CRFs making them visible in RCC. This is a terminal operation.  # noqa: E501
        """
        pass

    def test_bulk_save_encounter(self):
        """Test case for bulk_save_encounter

        Mass insert of subject events and event CRFs  # noqa: E501
        """
        pass

    def test_save_encounter(self):
        """Test case for save_encounter

        Inserts subject event or event CRF.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
