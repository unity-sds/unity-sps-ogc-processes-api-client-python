# InputCollection

InputCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional]
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]
**collection** | **str** |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_collection import InputCollection

# TODO update the JSON string below
json = "{}"
# create an instance of InputCollection from a JSON string
input_collection_instance = InputCollection.from_json(json)
# print the JSON string representation of the object
print(InputCollection.to_json())

# convert the object into a dict
input_collection_dict = input_collection_instance.to_dict()
# create an instance of InputCollection from a dict
input_collection_from_dict = InputCollection.from_dict(input_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
