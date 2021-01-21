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
from rcc.models.file_base64 import FileBase64  # noqa: E501
from rcc.rest import ApiException

class TestFileBase64(unittest.TestCase):
    """FileBase64 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileBase64
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.file_base64.FileBase64()  # noqa: E501
        if include_optional :
            return FileBase64(
                value = '0', 
                file_name = '0', 
                content_type = '0', 
                file_size = 56
            )
        else :
            return FileBase64(
        )

    def testFileBase64(self):
        """Test FileBase64"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
