# Schema1Input

Schema1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneof_schema_1_validator** | [**Reference**](Reference.md) |  | [optional]
**oneof_schema_2_validator** | [**SchemaOneOfInput**](SchemaOneOfInput.md) |  | [optional]
**actual_instance** | [**ActualInstance3**](ActualInstance3.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.schema1_input import Schema1Input

# TODO update the JSON string below
json = "{}"
# create an instance of Schema1Input from a JSON string
schema1_input_instance = Schema1Input.from_json(json)
# print the JSON string representation of the object
print(Schema1Input.to_json())

# convert the object into a dict
schema1_input_dict = schema1_input_instance.to_dict()
# create an instance of Schema1Input from a dict
schema1_input_from_dict = Schema1Input.from_dict(schema1_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
