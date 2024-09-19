# coding: utf-8

# flake8: noqa
"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from unity_sps_ogc_processes_api_python_client.models.actual_instance import (
    ActualInstance,
)
from unity_sps_ogc_processes_api_python_client.models.actual_instance1 import (
    ActualInstance1,
)
from unity_sps_ogc_processes_api_python_client.models.actual_instance2 import (
    ActualInstance2,
)
from unity_sps_ogc_processes_api_python_client.models.actual_instance3 import (
    ActualInstance3,
)
from unity_sps_ogc_processes_api_python_client.models.actual_instance4 import (
    ActualInstance4,
)
from unity_sps_ogc_processes_api_python_client.models.actual_instance5 import (
    ActualInstance5,
)
from unity_sps_ogc_processes_api_python_client.models.actual_instance6 import (
    ActualInstance6,
)
from unity_sps_ogc_processes_api_python_client.models.bbox import Bbox
from unity_sps_ogc_processes_api_python_client.models.bbox1 import Bbox1
from unity_sps_ogc_processes_api_python_client.models.bbox_bbox_inner import (
    BboxBboxInner,
)
from unity_sps_ogc_processes_api_python_client.models.bbox_def_crs import BboxDefCrs
from unity_sps_ogc_processes_api_python_client.models.conf_classes import ConfClasses
from unity_sps_ogc_processes_api_python_client.models.cpumax import Cpumax
from unity_sps_ogc_processes_api_python_client.models.cpumin import Cpumin
from unity_sps_ogc_processes_api_python_client.models.enumeration import Enumeration
from unity_sps_ogc_processes_api_python_client.models.exception import Exception
from unity_sps_ogc_processes_api_python_client.models.execute200_response_input import (
    Execute200ResponseInput,
)
from unity_sps_ogc_processes_api_python_client.models.execute200_response_input_any_of_value import (
    Execute200ResponseInputAnyOfValue,
)
from unity_sps_ogc_processes_api_python_client.models.execute200_response_output import (
    Execute200ResponseOutput,
)
from unity_sps_ogc_processes_api_python_client.models.execute200_response_output_any_of_value import (
    Execute200ResponseOutputAnyOfValue,
)
from unity_sps_ogc_processes_api_python_client.models.execute_workflows import (
    ExecuteWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.execution_unit import (
    ExecutionUnit,
)
from unity_sps_ogc_processes_api_python_client.models.execution_unit_config import (
    ExecutionUnitConfig,
)
from unity_sps_ogc_processes_api_python_client.models.fields_modifiers_properties import (
    FieldsModifiersProperties,
)
from unity_sps_ogc_processes_api_python_client.models.format import Format
from unity_sps_ogc_processes_api_python_client.models.format_schema import FormatSchema
from unity_sps_ogc_processes_api_python_client.models.health_check import HealthCheck
from unity_sps_ogc_processes_api_python_client.models.http_validation_error import (
    HTTPValidationError,
)
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_input import (
    InlineOrRefDataInput,
)
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_output import (
    InlineOrRefDataOutput,
)
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_workflows import (
    InlineOrRefDataWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.input_collection import (
    InputCollection,
)
from unity_sps_ogc_processes_api_python_client.models.input_description_input import (
    InputDescriptionInput,
)
from unity_sps_ogc_processes_api_python_client.models.input_description_output import (
    InputDescriptionOutput,
)
from unity_sps_ogc_processes_api_python_client.models.input_parameterized import (
    InputParameterized,
)
from unity_sps_ogc_processes_api_python_client.models.input_process import InputProcess
from unity_sps_ogc_processes_api_python_client.models.input_value_input import (
    InputValueInput,
)
from unity_sps_ogc_processes_api_python_client.models.input_value_no_object_input import (
    InputValueNoObjectInput,
)
from unity_sps_ogc_processes_api_python_client.models.input_value_no_object_output import (
    InputValueNoObjectOutput,
)
from unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows import (
    InputValueNoObjectWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.input_value_output import (
    InputValueOutput,
)
from unity_sps_ogc_processes_api_python_client.models.input_value_workflows import (
    InputValueWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.input_workflows import (
    InputWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.input_workflows1 import (
    InputWorkflows1,
)
from unity_sps_ogc_processes_api_python_client.models.input_workflows_any_of_inner import (
    InputWorkflowsAnyOfInner,
)
from unity_sps_ogc_processes_api_python_client.models.job_control_options import (
    JobControlOptions,
)
from unity_sps_ogc_processes_api_python_client.models.job_list_input import JobListInput
from unity_sps_ogc_processes_api_python_client.models.job_list_output import (
    JobListOutput,
)
from unity_sps_ogc_processes_api_python_client.models.jobtimeout import Jobtimeout
from unity_sps_ogc_processes_api_python_client.models.landing_page import LandingPage
from unity_sps_ogc_processes_api_python_client.models.link import Link
from unity_sps_ogc_processes_api_python_client.models.maximum import Maximum
from unity_sps_ogc_processes_api_python_client.models.memorymax import Memorymax
from unity_sps_ogc_processes_api_python_client.models.memorymin import Memorymin
from unity_sps_ogc_processes_api_python_client.models.metadata_input import (
    MetadataInput,
)
from unity_sps_ogc_processes_api_python_client.models.metadata_one_of import (
    MetadataOneOf,
)
from unity_sps_ogc_processes_api_python_client.models.metadata_one_of1 import (
    MetadataOneOf1,
)
from unity_sps_ogc_processes_api_python_client.models.metadata_one_of1_value import (
    MetadataOneOf1Value,
)
from unity_sps_ogc_processes_api_python_client.models.metadata_output import (
    MetadataOutput,
)
from unity_sps_ogc_processes_api_python_client.models.minimum import Minimum
from unity_sps_ogc_processes_api_python_client.models.model_schema_input import (
    ModelSchemaInput,
)
from unity_sps_ogc_processes_api_python_client.models.model_schema_output import (
    ModelSchemaOutput,
)
from unity_sps_ogc_processes_api_python_client.models.multipleof import Multipleof
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg import Ogcapppkg
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg_execution_unit import (
    OgcapppkgExecutionUnit,
)
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg_execution_unit_any_of_inner import (
    OgcapppkgExecutionUnitAnyOfInner,
)
from unity_sps_ogc_processes_api_python_client.models.oneof_schema2_validator import (
    OneofSchema2Validator,
)
from unity_sps_ogc_processes_api_python_client.models.oneof_schema6_validator import (
    OneofSchema6Validator,
)
from unity_sps_ogc_processes_api_python_client.models.output_description_input import (
    OutputDescriptionInput,
)
from unity_sps_ogc_processes_api_python_client.models.output_description_output import (
    OutputDescriptionOutput,
)
from unity_sps_ogc_processes_api_python_client.models.output_workflows import (
    OutputWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.output_workflows1 import (
    OutputWorkflows1,
)
from unity_sps_ogc_processes_api_python_client.models.process_input import ProcessInput
from unity_sps_ogc_processes_api_python_client.models.process_list_input import (
    ProcessListInput,
)
from unity_sps_ogc_processes_api_python_client.models.process_list_output import (
    ProcessListOutput,
)
from unity_sps_ogc_processes_api_python_client.models.process_output import (
    ProcessOutput,
)
from unity_sps_ogc_processes_api_python_client.models.process_summary_input import (
    ProcessSummaryInput,
)
from unity_sps_ogc_processes_api_python_client.models.process_summary_output import (
    ProcessSummaryOutput,
)
from unity_sps_ogc_processes_api_python_client.models.qualified_input_value_input import (
    QualifiedInputValueInput,
)
from unity_sps_ogc_processes_api_python_client.models.qualified_input_value_output import (
    QualifiedInputValueOutput,
)
from unity_sps_ogc_processes_api_python_client.models.qualified_input_value_workflows import (
    QualifiedInputValueWorkflows,
)
from unity_sps_ogc_processes_api_python_client.models.reference import Reference
from unity_sps_ogc_processes_api_python_client.models.schema1_input import Schema1Input
from unity_sps_ogc_processes_api_python_client.models.schema1_output import (
    Schema1Output,
)
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties_input import (
    SchemaOneOfAdditionalPropertiesInput,
)
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties_output import (
    SchemaOneOfAdditionalPropertiesOutput,
)
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_input import (
    SchemaOneOfInput,
)
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_output import (
    SchemaOneOfOutput,
)
from unity_sps_ogc_processes_api_python_client.models.status_code import StatusCode
from unity_sps_ogc_processes_api_python_client.models.status_info import StatusInfo
from unity_sps_ogc_processes_api_python_client.models.storageoutputsmin import (
    Storageoutputsmin,
)
from unity_sps_ogc_processes_api_python_client.models.storagetempmin import (
    Storagetempmin,
)
from unity_sps_ogc_processes_api_python_client.models.subscriber import Subscriber
from unity_sps_ogc_processes_api_python_client.models.validation_error import (
    ValidationError,
)
from unity_sps_ogc_processes_api_python_client.models.validation_error_loc_inner import (
    ValidationErrorLocInner,
)
