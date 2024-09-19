# InlineOrRefDataWorkflows

InlineOrRefDataWorkflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance**](ActualInstance.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**InputValueNoObjectWorkflows**](InputValueNoObjectWorkflows.md) |  | [optional]
**oneof_schema_2_validator** | [**QualifiedInputValueWorkflows**](QualifiedInputValueWorkflows.md) |  | [optional]
**oneof_schema_3_validator** | [**Link**](Link.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_workflows import InlineOrRefDataWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of InlineOrRefDataWorkflows from a JSON string
inline_or_ref_data_workflows_instance = InlineOrRefDataWorkflows.from_json(json)
# print the JSON string representation of the object
print(InlineOrRefDataWorkflows.to_json())

# convert the object into a dict
inline_or_ref_data_workflows_dict = inline_or_ref_data_workflows_instance.to_dict()
# create an instance of InlineOrRefDataWorkflows from a dict
inline_or_ref_data_workflows_from_dict = InlineOrRefDataWorkflows.from_dict(inline_or_ref_data_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
