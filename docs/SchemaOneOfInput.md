# SchemaOneOfInput

SchemaOneOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional]
**multiple_of** | [**Multipleof**](Multipleof.md) |  | [optional]
**maximum** | [**Maximum**](Maximum.md) |  | [optional]
**exclusive_maximum** | **bool** |  | [optional]
**minimum** | [**Minimum**](Minimum.md) |  | [optional]
**exclusive_minimum** | **bool** |  | [optional]
**max_length** | **int** |  | [optional]
**min_length** | **int** |  | [optional]
**pattern** | **str** |  | [optional]
**max_items** | **int** |  | [optional]
**min_items** | **int** |  | [optional]
**unique_items** | **bool** |  | [optional]
**max_properties** | **int** |  | [optional]
**min_properties** | **int** |  | [optional]
**required** | **List[str]** |  | [optional]
**enum** | **List[object]** |  | [optional]
**type** | **str** |  | [optional]
**var_not** | [**Schema1Input**](Schema1Input.md) |  | [optional]
**all_of** | [**List[Schema1Input]**](Schema1Input.md) |  | [optional]
**one_of** | [**List[Schema1Input]**](Schema1Input.md) |  | [optional]
**any_of** | [**List[Schema1Input]**](Schema1Input.md) |  | [optional]
**items** | [**Schema1Input**](Schema1Input.md) |  | [optional]
**properties** | [**Dict[str, Schema1Input]**](Schema1Input.md) |  | [optional]
**additional_properties** | [**SchemaOneOfAdditionalPropertiesInput**](SchemaOneOfAdditionalPropertiesInput.md) |  | [optional]
**description** | **str** |  | [optional]
**format** | **str** |  | [optional]
**default** | **object** |  | [optional]
**nullable** | **bool** |  | [optional]
**read_only** | **bool** |  | [optional]
**write_only** | **bool** |  | [optional]
**example** | **object** |  | [optional]
**deprecated** | **bool** |  | [optional]
**content_media_type** | **str** |  | [optional]
**content_encoding** | **str** |  | [optional]
**content_schema** | **str** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_input import SchemaOneOfInput

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaOneOfInput from a JSON string
schema_one_of_input_instance = SchemaOneOfInput.from_json(json)
# print the JSON string representation of the object
print(SchemaOneOfInput.to_json())

# convert the object into a dict
schema_one_of_input_dict = schema_one_of_input_instance.to_dict()
# create an instance of SchemaOneOfInput from a dict
schema_one_of_input_from_dict = SchemaOneOfInput.from_dict(schema_one_of_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
