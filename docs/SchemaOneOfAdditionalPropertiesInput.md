# SchemaOneOfAdditionalPropertiesInput

SchemaOneOfAdditionalProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance5**](ActualInstance5.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**Schema1Input**](Schema1Input.md) |  | [optional]
**oneof_schema_2_validator** | **bool** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties_input import SchemaOneOfAdditionalPropertiesInput

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaOneOfAdditionalPropertiesInput from a JSON string
schema_one_of_additional_properties_input_instance = SchemaOneOfAdditionalPropertiesInput.from_json(json)
# print the JSON string representation of the object
print(SchemaOneOfAdditionalPropertiesInput.to_json())

# convert the object into a dict
schema_one_of_additional_properties_input_dict = schema_one_of_additional_properties_input_instance.to_dict()
# create an instance of SchemaOneOfAdditionalPropertiesInput from a dict
schema_one_of_additional_properties_input_from_dict = SchemaOneOfAdditionalPropertiesInput.from_dict(schema_one_of_additional_properties_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
