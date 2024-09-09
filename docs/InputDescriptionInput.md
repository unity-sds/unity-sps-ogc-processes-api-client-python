# InputDescriptionInput

InputDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional]
**description** | **str** |  | [optional]
**keywords** | **List[str]** |  | [optional]
**metadata** | [**List[MetadataInput]**](MetadataInput.md) |  | [optional]
**var_schema** | [**ModelSchemaInput**](ModelSchemaInput.md) |  |
**min_occurs** | **int** |  | [optional]
**max_occurs** | **int** |  |
**value_passing** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_description_input import InputDescriptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of InputDescriptionInput from a JSON string
input_description_input_instance = InputDescriptionInput.from_json(json)
# print the JSON string representation of the object
print(InputDescriptionInput.to_json())

# convert the object into a dict
input_description_input_dict = input_description_input_instance.to_dict()
# create an instance of InputDescriptionInput from a dict
input_description_input_from_dict = InputDescriptionInput.from_dict(input_description_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
