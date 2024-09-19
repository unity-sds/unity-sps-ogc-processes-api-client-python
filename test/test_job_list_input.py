# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from unity_sps_ogc_processes_api_python_client.models.job_list_input import JobListInput


class TestJobListInput(unittest.TestCase):
    """JobListInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobListInput:
        """Test JobListInput
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `JobListInput`
        """
        model = JobListInput()
        if include_optional:
            return JobListInput(
                jobs = [
                    unity_sps_ogc_processes_api_python_client.models.status_info.StatusInfo(
                        process_id = '',
                        type = '',
                        job_id = '',
                        status = 'accepted',
                        message = '',
                        exception = unity_sps_ogc_processes_api_python_client.models.exception.Exception(
                            type = '',
                            title = '',
                            detail = '',
                            instance = '',
                            additional_properties = unity_sps_ogc_processes_api_python_client.models.additional_properties.Additional Properties(), ),
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        finished = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        progress = 0.0,
                        links = [
                            unity_sps_ogc_processes_api_python_client.models.link.Link(
                                href = '',
                                rel = '',
                                type = '',
                                hreflang = '',
                                title = '', )
                            ], )
                    ],
                links = [
                    unity_sps_ogc_processes_api_python_client.models.link.Link(
                        href = '',
                        rel = '',
                        type = '',
                        hreflang = '',
                        title = '', )
                    ]
            )
        else:
            return JobListInput(
                jobs = [
                    unity_sps_ogc_processes_api_python_client.models.status_info.StatusInfo(
                        process_id = '',
                        type = '',
                        job_id = '',
                        status = 'accepted',
                        message = '',
                        exception = unity_sps_ogc_processes_api_python_client.models.exception.Exception(
                            type = '',
                            title = '',
                            detail = '',
                            instance = '',
                            additional_properties = unity_sps_ogc_processes_api_python_client.models.additional_properties.Additional Properties(), ),
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        finished = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        progress = 0.0,
                        links = [
                            unity_sps_ogc_processes_api_python_client.models.link.Link(
                                href = '',
                                rel = '',
                                type = '',
                                hreflang = '',
                                title = '', )
                            ], )
                    ],
                links = [
                    unity_sps_ogc_processes_api_python_client.models.link.Link(
                        href = '',
                        rel = '',
                        type = '',
                        hreflang = '',
                        title = '', )
                    ],
        )
        """

    def testJobListInput(self):
        """Test JobListInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
