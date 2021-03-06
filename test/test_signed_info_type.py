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
from rcc.models.signed_info_type import SignedInfoType  # noqa: E501
from rcc.rest import ApiException

class TestSignedInfoType(unittest.TestCase):
    """SignedInfoType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SignedInfoType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.signed_info_type.SignedInfoType()  # noqa: E501
        if include_optional :
            return SignedInfoType(
                canonicalization_method = rcc.models.canonicalization_method_type.CanonicalizationMethodType(
                    content = [
                        None
                        ], 
                    algorithm = '0', ), 
                signature_method = rcc.models.signature_method_type.SignatureMethodType(
                    content = [
                        None
                        ], 
                    algorithm = '0', ), 
                reference = [
                    rcc.models.reference_type.ReferenceType(
                        transforms = rcc.models.transforms_type.TransformsType(
                            transform = [
                                rcc.models.transform_type.TransformType(
                                    content = [
                                        None
                                        ], 
                                    algorithm = '0', )
                                ], ), 
                        digest_method = rcc.models.digest_method_type.DigestMethodType(
                            algorithm = '0', ), 
                        digest_value = [
                            'YQ=='
                            ], 
                        id = '0', 
                        uri = '0', 
                        type = '0', )
                    ], 
                id = '0'
            )
        else :
            return SignedInfoType(
                canonicalization_method = rcc.models.canonicalization_method_type.CanonicalizationMethodType(
                    content = [
                        None
                        ], 
                    algorithm = '0', ),
                signature_method = rcc.models.signature_method_type.SignatureMethodType(
                    content = [
                        None
                        ], 
                    algorithm = '0', ),
                reference = [
                    rcc.models.reference_type.ReferenceType(
                        transforms = rcc.models.transforms_type.TransformsType(
                            transform = [
                                rcc.models.transform_type.TransformType(
                                    content = [
                                        None
                                        ], 
                                    algorithm = '0', )
                                ], ), 
                        digest_method = rcc.models.digest_method_type.DigestMethodType(
                            algorithm = '0', ), 
                        digest_value = [
                            'YQ=='
                            ], 
                        id = '0', 
                        uri = '0', 
                        type = '0', )
                    ],
        )

    def testSignedInfoType(self):
        """Test SignedInfoType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
