# ActualInstance3


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
from unity_sps_ogc_processes_api_python_client.models.actual_instance3 import ActualInstance3

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance3 from a JSON string
actual_instance3_instance = ActualInstance3.from_json(json)
# print the JSON string representation of the object
print(ActualInstance3.to_json())

# convert the object into a dict
actual_instance3_dict = actual_instance3_instance.to_dict()
# create an instance of ActualInstance3 from a dict
actual_instance3_from_dict = ActualInstance3.from_dict(actual_instance3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
