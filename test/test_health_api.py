# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.api.health_api import HealthApi


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HealthApi()

    def tearDown(self) -> None:
        pass

    def test_get_health_health_get(self) -> None:
        """Test case for get_health_health_get

        Retrieve the health status of the API.
        """
        pass


if __name__ == "__main__":
    unittest.main()