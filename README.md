# unity-sps-ogc-processes-api-python-client

This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 2.0.1
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements

Python 3.7+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import unity_sps_ogc_processes_api_python_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import unity_sps_ogc_processes_api_python_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import unity_sps_ogc_processes_api_python_client
from unity_sps_ogc_processes_api_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = unity_sps_ogc_processes_api_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with unity_sps_ogc_processes_api_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = unity_sps_ogc_processes_api_python_client.APIApi(api_client)
    f = 'f_example' # str | The format of the response. If no value is provided, the accept header is used to determine the format. Accepted values are &#39;json&#39; or &#39;html&#39;. (optional)

    try:
        # Retrieve this API definition.
        api_response = api_instance.get_api_api_get(f=f)
        print("The response of APIApi->get_api_api_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIApi->get_api_api_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *<http://localhost>*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIApi* | [**get_api_api_get**](docs/APIApi.md#get_api_api_get) | **GET** /api | Retrieve this API definition.
*APIApi* | [**get_api_processes_api_processes_list_get**](docs/APIApi.md#get_api_processes_api_processes_list_get) | **GET** /api/processes-list | Retrieve the list of processes available from this API implementation &amp;amp; deployment.
*ConformanceApi* | [**get_conformance_conformance_get**](docs/ConformanceApi.md#get_conformance_conformance_get) | **GET** /conformance | Retrieve the set of OGC API conformance classes that are supported by this service.
*DRUApi* | [**deploy_processes_post**](docs/DRUApi.md#deploy_processes_post) | **POST** /processes | deploy a process.
*DRUApi* | [**replace_processes_process_id_put**](docs/DRUApi.md#replace_processes_process_id_put) | **PUT** /processes/{processId} | replace a process.
*DRUApi* | [**undeploy_processes_process_id_delete**](docs/DRUApi.md#undeploy_processes_process_id_delete) | **DELETE** /processes/{processId} | undeploy a process.
*HealthApi* | [**get_health_health_get**](docs/HealthApi.md#get_health_health_get) | **GET** /health | Retrieve the health status of the API.
*JobsApi* | [**dismiss_jobs_job_id_delete**](docs/JobsApi.md#dismiss_jobs_job_id_delete) | **DELETE** /jobs/{jobId} | cancel a job execution, remove a finished job
*JobsApi* | [**get_jobs_jobs_get**](docs/JobsApi.md#get_jobs_jobs_get) | **GET** /jobs | retrieve the list of jobs.
*JobsApi* | [**get_result_jobs_job_id_results_get**](docs/JobsApi.md#get_result_jobs_job_id_results_get) | **GET** /jobs/{jobId}/results | retrieve the result(s) of a job
*JobsApi* | [**get_status_jobs_job_id_get**](docs/JobsApi.md#get_status_jobs_job_id_get) | **GET** /jobs/{jobId} | retrieve the status of a job
*LandingPageApi* | [**get_landing_page_get**](docs/LandingPageApi.md#get_landing_page_get) | **GET** / | Retrieve the OGC API landing page for this service.
*ProcessesApi* | [**execute_processes_process_id_execution_post**](docs/ProcessesApi.md#execute_processes_process_id_execution_post) | **POST** /processes/{processId}/execution | execute a process.
*ProcessesApi* | [**get_process_description_processes_process_id_get**](docs/ProcessesApi.md#get_process_description_processes_process_id_get) | **GET** /processes/{processId} | retrieve a process description
*ProcessesApi* | [**get_processes_processes_get**](docs/ProcessesApi.md#get_processes_processes_get) | **GET** /processes | retrieve the list of available processes

## Documentation For Models

- [ActualInstance](docs/ActualInstance.md)
- [ActualInstance1](docs/ActualInstance1.md)
- [ActualInstance2](docs/ActualInstance2.md)
- [ActualInstance3](docs/ActualInstance3.md)
- [ActualInstance4](docs/ActualInstance4.md)
- [ActualInstance5](docs/ActualInstance5.md)
- [ActualInstance6](docs/ActualInstance6.md)
- [Bbox](docs/Bbox.md)
- [Bbox1](docs/Bbox1.md)
- [BboxBboxInner](docs/BboxBboxInner.md)
- [BboxDefCrs](docs/BboxDefCrs.md)
- [ConfClasses](docs/ConfClasses.md)
- [Cpumax](docs/Cpumax.md)
- [Cpumin](docs/Cpumin.md)
- [Enumeration](docs/Enumeration.md)
- [Exception](docs/Exception.md)
- [Execute200ResponseInput](docs/Execute200ResponseInput.md)
- [Execute200ResponseInputAnyOfValue](docs/Execute200ResponseInputAnyOfValue.md)
- [Execute200ResponseOutput](docs/Execute200ResponseOutput.md)
- [Execute200ResponseOutputAnyOfValue](docs/Execute200ResponseOutputAnyOfValue.md)
- [ExecuteWorkflows](docs/ExecuteWorkflows.md)
- [ExecutionUnit](docs/ExecutionUnit.md)
- [ExecutionUnitConfig](docs/ExecutionUnitConfig.md)
- [FieldsModifiersProperties](docs/FieldsModifiersProperties.md)
- [Format](docs/Format.md)
- [FormatSchema](docs/FormatSchema.md)
- [HTTPValidationError](docs/HTTPValidationError.md)
- [HealthCheck](docs/HealthCheck.md)
- [InlineOrRefDataInput](docs/InlineOrRefDataInput.md)
- [InlineOrRefDataOutput](docs/InlineOrRefDataOutput.md)
- [InlineOrRefDataWorkflows](docs/InlineOrRefDataWorkflows.md)
- [InputCollection](docs/InputCollection.md)
- [InputDescriptionInput](docs/InputDescriptionInput.md)
- [InputDescriptionOutput](docs/InputDescriptionOutput.md)
- [InputParameterized](docs/InputParameterized.md)
- [InputProcess](docs/InputProcess.md)
- [InputValueInput](docs/InputValueInput.md)
- [InputValueNoObjectInput](docs/InputValueNoObjectInput.md)
- [InputValueNoObjectOutput](docs/InputValueNoObjectOutput.md)
- [InputValueNoObjectWorkflows](docs/InputValueNoObjectWorkflows.md)
- [InputValueOutput](docs/InputValueOutput.md)
- [InputValueWorkflows](docs/InputValueWorkflows.md)
- [InputWorkflows](docs/InputWorkflows.md)
- [InputWorkflows1](docs/InputWorkflows1.md)
- [InputWorkflowsAnyOfInner](docs/InputWorkflowsAnyOfInner.md)
- [JobControlOptions](docs/JobControlOptions.md)
- [JobListInput](docs/JobListInput.md)
- [JobListOutput](docs/JobListOutput.md)
- [Jobtimeout](docs/Jobtimeout.md)
- [LandingPage](docs/LandingPage.md)
- [Link](docs/Link.md)
- [Maximum](docs/Maximum.md)
- [Memorymax](docs/Memorymax.md)
- [Memorymin](docs/Memorymin.md)
- [MetadataInput](docs/MetadataInput.md)
- [MetadataOneOf](docs/MetadataOneOf.md)
- [MetadataOneOf1](docs/MetadataOneOf1.md)
- [MetadataOneOf1Value](docs/MetadataOneOf1Value.md)
- [MetadataOutput](docs/MetadataOutput.md)
- [Minimum](docs/Minimum.md)
- [ModelSchemaInput](docs/ModelSchemaInput.md)
- [ModelSchemaOutput](docs/ModelSchemaOutput.md)
- [Multipleof](docs/Multipleof.md)
- [Ogcapppkg](docs/Ogcapppkg.md)
- [OgcapppkgExecutionUnit](docs/OgcapppkgExecutionUnit.md)
- [OgcapppkgExecutionUnitAnyOfInner](docs/OgcapppkgExecutionUnitAnyOfInner.md)
- [OneofSchema2Validator](docs/OneofSchema2Validator.md)
- [OneofSchema6Validator](docs/OneofSchema6Validator.md)
- [OutputDescriptionInput](docs/OutputDescriptionInput.md)
- [OutputDescriptionOutput](docs/OutputDescriptionOutput.md)
- [OutputWorkflows](docs/OutputWorkflows.md)
- [OutputWorkflows1](docs/OutputWorkflows1.md)
- [ProcessInput](docs/ProcessInput.md)
- [ProcessListInput](docs/ProcessListInput.md)
- [ProcessListOutput](docs/ProcessListOutput.md)
- [ProcessOutput](docs/ProcessOutput.md)
- [ProcessSummaryInput](docs/ProcessSummaryInput.md)
- [ProcessSummaryOutput](docs/ProcessSummaryOutput.md)
- [QualifiedInputValueInput](docs/QualifiedInputValueInput.md)
- [QualifiedInputValueOutput](docs/QualifiedInputValueOutput.md)
- [QualifiedInputValueWorkflows](docs/QualifiedInputValueWorkflows.md)
- [Reference](docs/Reference.md)
- [Schema1Input](docs/Schema1Input.md)
- [Schema1Output](docs/Schema1Output.md)
- [SchemaOneOfAdditionalPropertiesInput](docs/SchemaOneOfAdditionalPropertiesInput.md)
- [SchemaOneOfAdditionalPropertiesOutput](docs/SchemaOneOfAdditionalPropertiesOutput.md)
- [SchemaOneOfInput](docs/SchemaOneOfInput.md)
- [SchemaOneOfOutput](docs/SchemaOneOfOutput.md)
- [StatusCode](docs/StatusCode.md)
- [StatusInfo](docs/StatusInfo.md)
- [Storageoutputsmin](docs/Storageoutputsmin.md)
- [Storagetempmin](docs/Storagetempmin.md)
- [Subscriber](docs/Subscriber.md)
- [ValidationError](docs/ValidationError.md)
- [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="bearerAuth"></a>

### bearerAuth

- **Type**: Bearer authentication (JWT)

## Author
