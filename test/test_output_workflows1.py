# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.models.output_workflows1 import (
    OutputWorkflows1,
)


class TestOutputWorkflows1(unittest.TestCase):
    """OutputWorkflows1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OutputWorkflows1:
        """Test OutputWorkflows1
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `OutputWorkflows1`
        """
        model = OutputWorkflows1()
        if include_optional:
            return OutputWorkflows1(
                format = unity_sps_ogc_processes_api_python_client.models.format.Format(
                    media_type = '',
                    encoding = '',
                    schema = unity_sps_ogc_processes_api_python_client.models.format_schema.FormatSchema(
                        oneof_schema_1_validator = '',
                        oneof_schema_2_validator = unity_sps_ogc_processes_api_python_client.models.oneof_schema_2_validator.oneof_schema_2_validator(),
                        actual_instance = '',
                        one_of_schemas = [
                            ''
                            ], ), ),
                output = ''
            )
        else:
            return OutputWorkflows1(
        )
        """

    def testOutputWorkflows1(self):
        """Test OutputWorkflows1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
