# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.models.execute200_response_output_any_of_value import (
    Execute200ResponseOutputAnyOfValue,
)


class TestExecute200ResponseOutputAnyOfValue(unittest.TestCase):
    """Execute200ResponseOutputAnyOfValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Execute200ResponseOutputAnyOfValue:
        """Test Execute200ResponseOutputAnyOfValue
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Execute200ResponseOutputAnyOfValue`
        """
        model = Execute200ResponseOutputAnyOfValue()
        if include_optional:
            return Execute200ResponseOutputAnyOfValue(
                bbox = [
                    null
                    ],
                crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                    anyof_schema_1_validator = '',
                    anyof_schema_2_validator = '',
                    actual_instance = null,
                    any_of_schemas = [
                        ''
                        ], ),
                href = '',
                rel = '',
                type = '',
                hreflang = '',
                title = '',
                media_type = '',
                encoding = '',
                var_schema = unity_sps_ogc_processes_api_python_client.models.format_schema.FormatSchema(
                    oneof_schema_1_validator = '',
                    oneof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.oneof_schema_2_validator.oneof_schema_2_validator(),
                    actual_instance = '',
                    one_of_schemas = [
                        ''
                        ], ),
                value = unity_sps_ogc_processes_api_python_client.models.input_value.InputValue(
                    anyof_schema_1_validator = unity_sps_ogc_processes_api_python_client.models.input_value_no_object.InputValueNoObject(
                        oneof_schema_1_validator = '',
                        oneof_schema_2_validator = null,
                        oneof_schema_3_validator = 56,
                        oneof_schema_4_validator = True,
                        oneof_schema_5_validator = [
                            None
                            ],
                        oneof_schema_6_validator = null,
                        oneof_schema_7_validator = unity_sps_ogc_processes_api_python_client.models.bbox.Bbox(
                            bbox = [
                                null
                                ],
                            crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                                anyof_schema_2_validator = '',
                                actual_instance = null,
                                any_of_schemas = [
                                    ''
                                    ], ), ),
                        actual_instance = null,
                        one_of_schemas = [
                            ''
                            ], ),
                    anyof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.anyof_schema_2_validator.anyof_schema_2_validator(),
                    actual_instance = null,
                    any_of_schemas = [
                        ''
                        ], )
            )
        else:
            return Execute200ResponseOutputAnyOfValue(
                bbox = [
                    null
                    ],
                href = '',
                value = unity_sps_ogc_processes_api_python_client.models.input_value.InputValue(
                    anyof_schema_1_validator = unity_sps_ogc_processes_api_python_client.models.input_value_no_object.InputValueNoObject(
                        oneof_schema_1_validator = '',
                        oneof_schema_2_validator = null,
                        oneof_schema_3_validator = 56,
                        oneof_schema_4_validator = True,
                        oneof_schema_5_validator = [
                            None
                            ],
                        oneof_schema_6_validator = null,
                        oneof_schema_7_validator = unity_sps_ogc_processes_api_python_client.models.bbox.Bbox(
                            bbox = [
                                null
                                ],
                            crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                                anyof_schema_2_validator = '',
                                actual_instance = null,
                                any_of_schemas = [
                                    ''
                                    ], ), ),
                        actual_instance = null,
                        one_of_schemas = [
                            ''
                            ], ),
                    anyof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.anyof_schema_2_validator.anyof_schema_2_validator(),
                    actual_instance = null,
                    any_of_schemas = [
                        ''
                        ], ),
        )
        """

    def testExecute200ResponseOutputAnyOfValue(self):
        """Test Execute200ResponseOutputAnyOfValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
