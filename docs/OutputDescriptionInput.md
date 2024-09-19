# OutputDescriptionInput

OutputDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]
**keywords** | **List[str]** |  | [optional]
**metadata** | [**List[MetadataInput]**](MetadataInput.md) |  | [optional]
**var_schema** | [**ModelSchemaInput**](ModelSchemaInput.md) |  |
**title** | **str** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.output_description_input import OutputDescriptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of OutputDescriptionInput from a JSON string
output_description_input_instance = OutputDescriptionInput.from_json(json)
# print the JSON string representation of the object
print(OutputDescriptionInput.to_json())

# convert the object into a dict
output_description_input_dict = output_description_input_instance.to_dict()
# create an instance of OutputDescriptionInput from a dict
output_description_input_from_dict = OutputDescriptionInput.from_dict(output_description_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
