# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties_input import (
    SchemaOneOfAdditionalPropertiesInput,
)


class TestSchemaOneOfAdditionalPropertiesInput(unittest.TestCase):
    """SchemaOneOfAdditionalPropertiesInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemaOneOfAdditionalPropertiesInput:
        """Test SchemaOneOfAdditionalPropertiesInput
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SchemaOneOfAdditionalPropertiesInput`
        """
        model = SchemaOneOfAdditionalPropertiesInput()
        if include_optional:
            return SchemaOneOfAdditionalPropertiesInput(
                oneof_schema_1_validator = unity_sps_ogc_processes_api_python_client.models.schema1.Schema1(
                    oneof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.schema_one_of.SchemaOneOf(
                        title = '',
                        multiple_of = null,
                        maximum = null,
                        exclusive_maximum = True,
                        minimum = null,
                        exclusive_minimum = True,
                        max_length = 0.0,
                        min_length = 0.0,
                        pattern = '',
                        max_items = 0.0,
                        min_items = 0.0,
                        unique_items = True,
                        max_properties = 0.0,
                        min_properties = 0.0,
                        required = [
                            ''
                            ],
                        enum = [
                            None
                            ],
                        type = '',
                        not = unity_sps_ogc_processes_api_python_client.models.schema1.Schema1(
                            actual_instance = null,
                            one_of_schemas = [
                                ''
                                ], ),
                        all_of = [

                            ],
                        one_of = [

                            ],
                        any_of = [

                            ],
                        items = ,
                        properties = {
                            'key' :
                            },
                        additional_properties = unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties.SchemaOneOfAdditionalProperties(),
                        description = '',
                        format = '',
                        default = unity_sps_ogc_processes_api_python_client.models.default.default(),
                        nullable = True,
                        read_only = True,
                        write_only = True,
                        example = unity_sps_ogc_processes_api_python_client.models.example.example(),
                        deprecated = True,
                        content_media_type = '',
                        content_encoding = '',
                        content_schema = '', ),
                    actual_instance = null,
                    one_of_schemas = [
                        ''
                        ], ),
                oneof_schema_2_validator = True,
                actual_instance = None,
                one_of_schemas = [
                    ''
                    ]
            )
        else:
            return SchemaOneOfAdditionalPropertiesInput(
        )
        """

    def testSchemaOneOfAdditionalPropertiesInput(self):
        """Test SchemaOneOfAdditionalPropertiesInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()