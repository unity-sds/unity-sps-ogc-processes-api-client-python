# Schema1Output

Schema1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance4**](ActualInstance4.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**Reference**](Reference.md) |  | [optional]
**oneof_schema_2_validator** | [**SchemaOneOfOutput**](SchemaOneOfOutput.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.schema1_output import Schema1Output

# TODO update the JSON string below
json = "{}"
# create an instance of Schema1Output from a JSON string
schema1_output_instance = Schema1Output.from_json(json)
# print the JSON string representation of the object
print(Schema1Output.to_json())

# convert the object into a dict
schema1_output_dict = schema1_output_instance.to_dict()
# create an instance of Schema1Output from a dict
schema1_output_from_dict = Schema1Output.from_dict(schema1_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
