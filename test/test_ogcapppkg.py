# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.models.ogcapppkg import Ogcapppkg


class TestOgcapppkg(unittest.TestCase):
    """Ogcapppkg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Ogcapppkg:
        """Test Ogcapppkg
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Ogcapppkg`
        """
        model = Ogcapppkg()
        if include_optional:
            return Ogcapppkg(
                process_description = unity_sps_ogc_processes_api_python_client.models.process.Process(
                    title = '',
                    description = '',
                    keywords = [
                        ''
                        ],
                    metadata = [
                        null
                        ],
                    id = '',
                    version = '',
                    job_control_options = [
                        'sync-execute'
                        ],
                    links = [
                        unity_sps_ogc_processes_api_python_client.models.link.Link(
                            href = '',
                            rel = '',
                            type = '',
                            hreflang = '',
                            title = '', )
                        ],
                    inputs = {
                        'key' : unity_sps_ogc_processes_api_python_client.models.input_description.InputDescription(
                            title = '',
                            description = '',
                            schema = null,
                            min_occurs = 56,
                            max_occurs = 56,
                            value_passing = [
                                ''
                                ], )
                        },
                    outputs = {
                        'key' : unity_sps_ogc_processes_api_python_client.models.output_description.OutputDescription(
                            title = '',
                            description = '',
                            schema = null, )
                        }, ),
                execution_unit = None
            )
        else:
            return Ogcapppkg(
                process_description = unity_sps_ogc_processes_api_python_client.models.process.Process(
                    title = '',
                    description = '',
                    keywords = [
                        ''
                        ],
                    metadata = [
                        null
                        ],
                    id = '',
                    version = '',
                    job_control_options = [
                        'sync-execute'
                        ],
                    links = [
                        unity_sps_ogc_processes_api_python_client.models.link.Link(
                            href = '',
                            rel = '',
                            type = '',
                            hreflang = '',
                            title = '', )
                        ],
                    inputs = {
                        'key' : unity_sps_ogc_processes_api_python_client.models.input_description.InputDescription(
                            title = '',
                            description = '',
                            schema = null,
                            min_occurs = 56,
                            max_occurs = 56,
                            value_passing = [
                                ''
                                ], )
                        },
                    outputs = {
                        'key' : unity_sps_ogc_processes_api_python_client.models.output_description.OutputDescription(
                            title = '',
                            description = '',
                            schema = null, )
                        }, ),
                execution_unit = None,
        )
        """

    def testOgcapppkg(self):
        """Test Ogcapppkg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
