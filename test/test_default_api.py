# coding: utf-8

"""
    Unity Processing API conforming to the OGC API - Processes - Part 1 standard

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_conformance_declaration_conformance_get(self) -> None:
        """Test case for conformance_declaration_conformance_get

        Information about standards that this API conforms to
        """
        pass

    def test_dismiss_jobs_job_id_delete(self) -> None:
        """Test case for dismiss_jobs_job_id_delete

        Cancel a job execution, remove a finished job
        """
        pass

    def test_execute_processes_process_id_execution_post(self) -> None:
        """Test case for execute_processes_process_id_execution_post

        Execute a process
        """
        pass

    def test_get_health_health_get(self) -> None:
        """Test case for get_health_health_get

        Perform a Health Check
        """
        pass

    def test_job_list_jobs_get(self) -> None:
        """Test case for job_list_jobs_get

        Retrieve the list of jobs
        """
        pass

    def test_landing_page_get(self) -> None:
        """Test case for landing_page_get

        Landing page of this API
        """
        pass

    def test_process_description_processes_process_id_get(self) -> None:
        """Test case for process_description_processes_process_id_get

        Retrieve a process description
        """
        pass

    def test_process_list_processes_get(self) -> None:
        """Test case for process_list_processes_get

        Retrieve the list of available processes
        """
        pass

    def test_register_process_processes_post(self) -> None:
        """Test case for register_process_processes_post

        Register a process
        """
        pass

    def test_results_jobs_job_id_results_get(self) -> None:
        """Test case for results_jobs_job_id_results_get

        Retrieve the result(s) of a job
        """
        pass

    def test_status_jobs_job_id_get(self) -> None:
        """Test case for status_jobs_job_id_get

        Retrieve the status of a job
        """
        pass

    def test_unregister_process_processes_process_id_delete(self) -> None:
        """Test case for unregister_process_processes_process_id_delete

        Unregister a process
        """
        pass


if __name__ == "__main__":
    unittest.main()
