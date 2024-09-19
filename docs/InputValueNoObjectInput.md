# InputValueNoObjectInput

InputValueNoObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | **object** |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | **str** |  | [optional]
**oneof_schema_2_validator** | [**OneofSchema2Validator**](OneofSchema2Validator.md) |  | [optional]
**oneof_schema_3_validator** | **int** |  | [optional]
**oneof_schema_4_validator** | **bool** |  | [optional]
**oneof_schema_5_validator** | **List[object]** |  | [optional]
**oneof_schema_6_validator** | [**OneofSchema6Validator**](OneofSchema6Validator.md) |  | [optional]
**oneof_schema_7_validator** | [**Bbox**](Bbox.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_value_no_object_input import InputValueNoObjectInput

# TODO update the JSON string below
json = "{}"
# create an instance of InputValueNoObjectInput from a JSON string
input_value_no_object_input_instance = InputValueNoObjectInput.from_json(json)
# print the JSON string representation of the object
print(InputValueNoObjectInput.to_json())

# convert the object into a dict
input_value_no_object_input_dict = input_value_no_object_input_instance.to_dict()
# create an instance of InputValueNoObjectInput from a dict
input_value_no_object_input_from_dict = InputValueNoObjectInput.from_dict(input_value_no_object_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
