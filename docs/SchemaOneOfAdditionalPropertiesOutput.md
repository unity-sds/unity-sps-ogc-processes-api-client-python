# SchemaOneOfAdditionalPropertiesOutput

SchemaOneOfAdditionalProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneof_schema_1_validator** | [**Schema1Output**](Schema1Output.md) |  | [optional]
**oneof_schema_2_validator** | **bool** |  | [optional]
**actual_instance** | [**ActualInstance6**](ActualInstance6.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties_output import SchemaOneOfAdditionalPropertiesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaOneOfAdditionalPropertiesOutput from a JSON string
schema_one_of_additional_properties_output_instance = SchemaOneOfAdditionalPropertiesOutput.from_json(json)
# print the JSON string representation of the object
print(SchemaOneOfAdditionalPropertiesOutput.to_json())

# convert the object into a dict
schema_one_of_additional_properties_output_dict = schema_one_of_additional_properties_output_instance.to_dict()
# create an instance of SchemaOneOfAdditionalPropertiesOutput from a dict
schema_one_of_additional_properties_output_from_dict = SchemaOneOfAdditionalPropertiesOutput.from_dict(schema_one_of_additional_properties_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
