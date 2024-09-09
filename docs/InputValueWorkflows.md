# InputValueWorkflows

InputValueWorkflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneof_schema_1_validator** | [**InputValueNoObjectWorkflows**](InputValueNoObjectWorkflows.md) |  | [optional]
**oneof_schema_2_validator** | **object** |  | [optional]
**actual_instance** | [**InputValueNoObjectWorkflows**](InputValueNoObjectWorkflows.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_value_workflows import InputValueWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of InputValueWorkflows from a JSON string
input_value_workflows_instance = InputValueWorkflows.from_json(json)
# print the JSON string representation of the object
print(InputValueWorkflows.to_json())

# convert the object into a dict
input_value_workflows_dict = input_value_workflows_instance.to_dict()
# create an instance of InputValueWorkflows from a dict
input_value_workflows_from_dict = InputValueWorkflows.from_dict(input_value_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
