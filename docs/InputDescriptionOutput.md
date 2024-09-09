# InputDescriptionOutput

InputDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional]
**keywords** | **List[str]** |  | [optional]
**max_occurs** | **int** |  |
**metadata** | [**List[MetadataOutput]**](MetadataOutput.md) |  | [optional]
**min_occurs** | **int** |  | [optional]
**var_schema** | [**ModelSchemaOutput**](ModelSchemaOutput.md) |  |
**title** | **str** |  | [optional]
**value_passing** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_description_output import InputDescriptionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of InputDescriptionOutput from a JSON string
input_description_output_instance = InputDescriptionOutput.from_json(json)
# print the JSON string representation of the object
print(InputDescriptionOutput.to_json())

# convert the object into a dict
input_description_output_dict = input_description_output_instance.to_dict()
# create an instance of InputDescriptionOutput from a dict
input_description_output_from_dict = InputDescriptionOutput.from_dict(input_description_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
