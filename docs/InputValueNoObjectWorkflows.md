# InputValueNoObjectWorkflows

InputValueNoObjectWorkflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneof_schema_1_validator** | **str** |  | [optional]
**oneof_schema_2_validator** | [**OneofSchema2Validator**](OneofSchema2Validator.md) |  | [optional]
**oneof_schema_3_validator** | **int** |  | [optional]
**oneof_schema_4_validator** | **bool** |  | [optional]
**oneof_schema_5_validator** | **List[object]** |  | [optional]
**oneof_schema_6_validator** | [**OneofSchema6Validator**](OneofSchema6Validator.md) |  | [optional]
**oneof_schema_7_validator** | [**Bbox1**](Bbox1.md) |  | [optional]
**oneof_schema_8_validator** | [**InputCollection**](InputCollection.md) |  | [optional]
**oneof_schema_9_validator** | [**InputProcess**](InputProcess.md) |  | [optional]
**oneof_schema_10_validator** | [**InputParameterized**](InputParameterized.md) |  | [optional]
**actual_instance** | [**ActualInstance1**](ActualInstance1.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_value_no_object_workflows import InputValueNoObjectWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of InputValueNoObjectWorkflows from a JSON string
input_value_no_object_workflows_instance = InputValueNoObjectWorkflows.from_json(json)
# print the JSON string representation of the object
print(InputValueNoObjectWorkflows.to_json())

# convert the object into a dict
input_value_no_object_workflows_dict = input_value_no_object_workflows_instance.to_dict()
# create an instance of InputValueNoObjectWorkflows from a dict
input_value_no_object_workflows_from_dict = InputValueNoObjectWorkflows.from_dict(input_value_no_object_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
