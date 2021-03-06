# coding: utf-8

"""
    nPhase REST Resource

    REDCap REST API v.2  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import rcc
from rcc.models.language_labels import LanguageLabels  # noqa: E501
from rcc.rest import ApiException

class TestLanguageLabels(unittest.TestCase):
    """LanguageLabels unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LanguageLabels
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.language_labels.LanguageLabels()  # noqa: E501
        if include_optional :
            return LanguageLabels(
                language_label = [
                    rcc.models.language_label.LanguageLabel(
                        object_oid = '0', 
                        object_type = '0', 
                        translation = '0', 
                        translation_plain_text = '0', 
                        lang_code = '0', )
                    ]
            )
        else :
            return LanguageLabels(
        )

    def testLanguageLabels(self):
        """Test LanguageLabels"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
