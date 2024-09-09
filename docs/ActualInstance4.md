# ActualInstance4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  |
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
**var_not** | [**Schema1Output**](Schema1Output.md) |  | [optional]
**all_of** | [**List[Schema1Output]**](Schema1Output.md) |  | [optional]
**one_of** | [**List[Schema1Output]**](Schema1Output.md) |  | [optional]
**any_of** | [**List[Schema1Output]**](Schema1Output.md) |  | [optional]
**items** | [**Schema1Output**](Schema1Output.md) |  | [optional]
**properties** | [**Dict[str, Schema1Output]**](Schema1Output.md) |  | [optional]
**additional_properties** | [**SchemaOneOfAdditionalPropertiesOutput**](SchemaOneOfAdditionalPropertiesOutput.md) |  | [optional]
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
from unity_sps_ogc_processes_api_python_client.models.actual_instance4 import ActualInstance4

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance4 from a JSON string
actual_instance4_instance = ActualInstance4.from_json(json)
# print the JSON string representation of the object
print(ActualInstance4.to_json())

# convert the object into a dict
actual_instance4_dict = actual_instance4_instance.to_dict()
# create an instance of ActualInstance4 from a dict
actual_instance4_from_dict = ActualInstance4.from_dict(actual_instance4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
