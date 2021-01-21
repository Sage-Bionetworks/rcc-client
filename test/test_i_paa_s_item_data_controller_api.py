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
from rcc.api.i_paa_s_item_data_controller_api import IPaaSItemDataControllerApi  # noqa: E501
from rcc.rest import ApiException


class TestIPaaSItemDataControllerApi(unittest.TestCase):
    """IPaaSItemDataControllerApi unit test stubs"""

    def setUp(self):
        self.api = rcc.api.i_paa_s_item_data_controller_api.IPaaSItemDataControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_save_coded_item_data(self):
        """Test case for bulk_save_coded_item_data

        Starts processing temporary observation data for key-based repeating groups.  # noqa: E501
        """
        pass

    def test_bulk_save_coded_item_data1(self):
        """Test case for bulk_save_coded_item_data1

        Save a collection of values for coded CRF variables.  # noqa: E501
        """
        pass

    def test_prepare_coded_item_data_for_saving(self):
        """Test case for prepare_coded_item_data_for_saving

        Prepare value for coded CRF variable to be stored in RCC. No changes will be reflected in RCC. This is an intermediate operation.  # noqa: E501
        """
        pass

    def test_save_coded_item_data(self):
        """Test case for save_coded_item_data

        Submit prepared values for coded CRF variables making them visible in RCC. This is a terminal operation.  # noqa: E501
        """
        pass

    def test_save_coded_item_data1(self):
        """Test case for save_coded_item_data1

        Save value for coded CRF variable.  # noqa: E501
        """
        pass

    def test_save_named_item_data(self):
        """Test case for save_named_item_data

        Save values for named CRF variables.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
