# OutputDescriptionOutput

OutputDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]
**keywords** | **List[str]** |  | [optional]
**metadata** | [**List[MetadataOutput]**](MetadataOutput.md) |  | [optional]
**var_schema** | [**ModelSchemaOutput**](ModelSchemaOutput.md) |  |
**title** | **str** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.output_description_output import OutputDescriptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of OutputDescriptionOutput from a JSON string
output_description_output_instance = OutputDescriptionOutput.from_json(json)
# print the JSON string representation of the object
print(OutputDescriptionOutput.to_json())

# convert the object into a dict
output_description_output_dict = output_description_output_instance.to_dict()
# create an instance of OutputDescriptionOutput from a dict
output_description_output_from_dict = OutputDescriptionOutput.from_dict(output_description_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
