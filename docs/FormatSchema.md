# FormatSchema

FormatSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneof_schema_1_validator** | **str** |  | [optional]
**oneof_schema_2_validator** | **object** |  | [optional]
**actual_instance** | **str** |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.format_schema import FormatSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FormatSchema from a JSON string
format_schema_instance = FormatSchema.from_json(json)
# print the JSON string representation of the object
print(FormatSchema.to_json())

# convert the object into a dict
format_schema_dict = format_schema_instance.to_dict()
# create an instance of FormatSchema from a dict
format_schema_from_dict = FormatSchema.from_dict(format_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
