# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.models.actual_instance import (
    ActualInstance,
)


class TestActualInstance(unittest.TestCase):
    """ActualInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActualInstance:
        """Test ActualInstance
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ActualInstance`
        """
        model = ActualInstance()
        if include_optional:
            return ActualInstance(
                oneof_schema_1_validator = '',
                oneof_schema_2_validator = None,
                oneof_schema_3_validator = 56,
                oneof_schema_4_validator = True,
                oneof_schema_5_validator = [
                    None
                    ],
                oneof_schema_6_validator = None,
                oneof_schema_7_validator = unity_sps_ogc_processes_api_python_client.models.bbox1.Bbox1(
                    bbox = [
                        null
                        ],
                    crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                        anyof_schema_1_validator = '',
                        anyof_schema_2_validator = '',
                        actual_instance = null,
                        any_of_schemas = [
                            ''
                            ], ), ),
                oneof_schema_8_validator = unity_sps_ogc_processes_api_python_client.models.input_collection.InputCollection(
                    filter = '',
                    properties = null,
                    sort_by = [
                        ''
                        ],
                    collection = '', ),
                oneof_schema_9_validator = unity_sps_ogc_processes_api_python_client.models.input_process.InputProcess(
                    process = '',
                    inputs = {
                        'key' : unity_sps_ogc_processes_api_python_client.models.input_workflows1.InputWorkflows1(
                            oneof_schema_1_validator = unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_workflows.InlineOrRefDataWorkflows(
                                oneof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.qualified_input_value_workflows.QualifiedInputValueWorkflows(
                                    media_type = '',
                                    encoding = '',
                                    schema = unity_sps_ogc_processes_api_python_client.models.format_schema.FormatSchema(
                                        actual_instance = '',
                                        one_of_schemas = [
                                            ''
                                            ], ),
                                    filter = '',
                                    properties = null,
                                    sort_by = [
                                        ''
                                        ],
                                    value = unity_sps_ogc_processes_api_python_client.models.input_value_workflows.InputValueWorkflows(
                                        actual_instance = unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows.InputValueNoObjectWorkflows(
                                            oneof_schema_3_validator = 56,
                                            oneof_schema_4_validator = True,
                                            oneof_schema_5_validator = [
                                                None
                                                ],
                                            oneof_schema_6_validator = null,
                                            oneof_schema_7_validator = unity_sps_ogc_processes_api_python_client.models.bbox1.Bbox1(
                                                bbox = [
                                                    null
                                                    ],
                                                crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                                                    anyof_schema_1_validator = '',
                                                    anyof_schema_2_validator = '',
                                                    any_of_schemas = [
                                                        ''
                                                        ], ), ),
                                            oneof_schema_8_validator = unity_sps_ogc_processes_api_python_client.models.input_collection.InputCollection(
                                                filter = '',
                                                collection = '', ),
                                            oneof_schema_10_validator = unity_sps_ogc_processes_api_python_client.models.input_parameterized.InputParameterized(
                                                filter = '',
                                                __input = '', ), ), ), ),
                                oneof_schema_3_validator = unity_sps_ogc_processes_api_python_client.models.link.Link(
                                    href = '',
                                    rel = '',
                                    type = '',
                                    hreflang = '',
                                    title = '', ),
                                actual_instance = null,
                                one_of_schemas = [
                                    ''
                                    ], ),
                            oneof_schema_2_validator = [
                                unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_workflows.InlineOrRefDataWorkflows()
                                ],
                            actual_instance = null,
                            one_of_schemas = , )
                        },
                    outputs = {
                        'key' : unity_sps_ogc_processes_api_python_client.models.output_workflows1.OutputWorkflows1(
                            format = unity_sps_ogc_processes_api_python_client.models.format.Format(
                                media_type = '',
                                encoding = '', ),
                            __output = '', )
                        },
                    subscriber = unity_sps_ogc_processes_api_python_client.models.subscriber.Subscriber(
                        success_uri = '',
                        in_progress_uri = '',
                        failed_uri = '', ),
                    filter = '',
                    properties = null,
                    sort_by = [
                        ''
                        ], ),
                oneof_schema_10_validator = unity_sps_ogc_processes_api_python_client.models.input_parameterized.InputParameterized(
                    filter = '',
                    properties = null,
                    sort_by = [
                        ''
                        ],
                    __input = '', ),
                actual_instance = None,
                one_of_schemas = [
                    ''
                    ],
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
                filter = '',
                properties = None,
                sort_by = [
                    ''
                    ],
                value = unity_sps_ogc_processes_api_python_client.models.input_value_workflows.InputValueWorkflows(
                    oneof_schema_1_validator = unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows.InputValueNoObjectWorkflows(
                        oneof_schema_2_validator = null,
                        oneof_schema_3_validator = 56,
                        oneof_schema_4_validator = True,
                        oneof_schema_5_validator = [
                            None
                            ],
                        oneof_schema_6_validator = null,
                        oneof_schema_7_validator = unity_sps_ogc_processes_api_python_client.models.bbox1.Bbox1(
                            bbox = [
                                null
                                ],
                            crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                                anyof_schema_1_validator = '',
                                anyof_schema_2_validator = '',
                                actual_instance = null,
                                any_of_schemas = [
                                    ''
                                    ], ), ),
                        oneof_schema_8_validator = unity_sps_ogc_processes_api_python_client.models.input_collection.InputCollection(
                            filter = '',
                            properties = null,
                            sort_by = [
                                ''
                                ],
                            collection = '', ),
                        oneof_schema_9_validator = unity_sps_ogc_processes_api_python_client.models.input_process.InputProcess(
                            process = '',
                            inputs = {
                                'key' : unity_sps_ogc_processes_api_python_client.models.input_workflows1.InputWorkflows1(
                                    actual_instance = null,
                                    one_of_schemas = [
                                        ''
                                        ], )
                                },
                            outputs = {
                                'key' : unity_sps_ogc_processes_api_python_client.models.output_workflows1.OutputWorkflows1(
                                    format = unity_sps_ogc_processes_api_python_client.models.format.Format(
                                        media_type = '',
                                        encoding = '',
                                        schema = unity_sps_ogc_processes_api_python_client.models.format_schema.FormatSchema(), ),
                                    __output = '', )
                                },
                            subscriber = unity_sps_ogc_processes_api_python_client.models.subscriber.Subscriber(
                                success_uri = '',
                                in_progress_uri = '',
                                failed_uri = '', ),
                            filter = '', ),
                        oneof_schema_10_validator = unity_sps_ogc_processes_api_python_client.models.input_parameterized.InputParameterized(
                            filter = '',
                            __input = '', ),
                        actual_instance = null,
                        one_of_schemas = [
                            ''
                            ], ),
                    oneof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.oneof_schema_2_validator.oneof_schema_2_validator(),
                    actual_instance = unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows.InputValueNoObjectWorkflows(
                        oneof_schema_3_validator = 56,
                        oneof_schema_4_validator = True, ),
                    one_of_schemas = , )
            )
        else:
            return ActualInstance(
                href = '',
                value = unity_sps_ogc_processes_api_python_client.models.input_value_workflows.InputValueWorkflows(
                    oneof_schema_1_validator = unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows.InputValueNoObjectWorkflows(
                        oneof_schema_2_validator = null,
                        oneof_schema_3_validator = 56,
                        oneof_schema_4_validator = True,
                        oneof_schema_5_validator = [
                            None
                            ],
                        oneof_schema_6_validator = null,
                        oneof_schema_7_validator = unity_sps_ogc_processes_api_python_client.models.bbox1.Bbox1(
                            bbox = [
                                null
                                ],
                            crs = unity_sps_ogc_processes_api_python_client.models.bbox_def_crs.BboxDefCrs(
                                anyof_schema_1_validator = '',
                                anyof_schema_2_validator = '',
                                actual_instance = null,
                                any_of_schemas = [
                                    ''
                                    ], ), ),
                        oneof_schema_8_validator = unity_sps_ogc_processes_api_python_client.models.input_collection.InputCollection(
                            filter = '',
                            properties = null,
                            sort_by = [
                                ''
                                ],
                            collection = '', ),
                        oneof_schema_9_validator = unity_sps_ogc_processes_api_python_client.models.input_process.InputProcess(
                            process = '',
                            inputs = {
                                'key' : unity_sps_ogc_processes_api_python_client.models.input_workflows1.InputWorkflows1(
                                    actual_instance = null,
                                    one_of_schemas = [
                                        ''
                                        ], )
                                },
                            outputs = {
                                'key' : unity_sps_ogc_processes_api_python_client.models.output_workflows1.OutputWorkflows1(
                                    format = unity_sps_ogc_processes_api_python_client.models.format.Format(
                                        media_type = '',
                                        encoding = '',
                                        schema = unity_sps_ogc_processes_api_python_client.models.format_schema.FormatSchema(), ),
                                    __output = '', )
                                },
                            subscriber = unity_sps_ogc_processes_api_python_client.models.subscriber.Subscriber(
                                success_uri = '',
                                in_progress_uri = '',
                                failed_uri = '', ),
                            filter = '', ),
                        oneof_schema_10_validator = unity_sps_ogc_processes_api_python_client.models.input_parameterized.InputParameterized(
                            filter = '',
                            __input = '', ),
                        actual_instance = null,
                        one_of_schemas = [
                            ''
                            ], ),
                    oneof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.oneof_schema_2_validator.oneof_schema_2_validator(),
                    actual_instance = unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows.InputValueNoObjectWorkflows(
                        oneof_schema_3_validator = 56,
                        oneof_schema_4_validator = True, ),
                    one_of_schemas = , ),
        )
        """

    def testActualInstance(self):
        """Test ActualInstance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
