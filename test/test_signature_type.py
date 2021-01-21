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
from rcc.models.signature_type import SignatureType  # noqa: E501
from rcc.rest import ApiException

class TestSignatureType(unittest.TestCase):
    """SignatureType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SignatureType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = rcc.models.signature_type.SignatureType()  # noqa: E501
        if include_optional :
            return SignatureType(
                signed_info = rcc.models.signed_info_type.SignedInfoType(
                    canonicalization_method = rcc.models.canonicalization_method_type.CanonicalizationMethodType(
                        content = [
                            None
                            ], 
                        algorithm = '0', ), 
                    signature_method = rcc.models.signature_method_type.SignatureMethodType(
                        algorithm = '0', ), 
                    reference = [
                        rcc.models.reference_type.ReferenceType(
                            transforms = rcc.models.transforms_type.TransformsType(
                                transform = [
                                    rcc.models.transform_type.TransformType(
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
                    id = '0', ), 
                signature_value = rcc.models.signature_value_type.SignatureValueType(
                    value = [
                        'YQ=='
                        ], 
                    id = '0', ), 
                key_info = rcc.models.key_info_type.KeyInfoType(
                    content = [
                        None
                        ], 
                    id = '0', ), 
                object = [
                    rcc.models.object_type.ObjectType(
                        content = [
                            None
                            ], 
                        id = '0', 
                        mime_type = '0', 
                        encoding = '0', )
                    ], 
                id = '0'
            )
        else :
            return SignatureType(
                signed_info = rcc.models.signed_info_type.SignedInfoType(
                    canonicalization_method = rcc.models.canonicalization_method_type.CanonicalizationMethodType(
                        content = [
                            None
                            ], 
                        algorithm = '0', ), 
                    signature_method = rcc.models.signature_method_type.SignatureMethodType(
                        algorithm = '0', ), 
                    reference = [
                        rcc.models.reference_type.ReferenceType(
                            transforms = rcc.models.transforms_type.TransformsType(
                                transform = [
                                    rcc.models.transform_type.TransformType(
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
                    id = '0', ),
                signature_value = rcc.models.signature_value_type.SignatureValueType(
                    value = [
                        'YQ=='
                        ], 
                    id = '0', ),
        )

    def testSignatureType(self):
        """Test SignatureType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
