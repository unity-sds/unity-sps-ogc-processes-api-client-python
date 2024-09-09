# Execute200ResponseInputAnyOfValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**List[BboxBboxInner]**](BboxBboxInner.md) |  |
**crs** | [**BboxDefCrs**](BboxDefCrs.md) |  | [optional]
**href** | **str** |  |
**hreflang** | **str** |  | [optional]
**rel** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueInput**](InputValueInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.execute200_response_input_any_of_value import Execute200ResponseInputAnyOfValue

# TODO update the JSON string below
json = "{}"
# create an instance of Execute200ResponseInputAnyOfValue from a JSON string
execute200_response_input_any_of_value_instance = Execute200ResponseInputAnyOfValue.from_json(json)
# print the JSON string representation of the object
print(Execute200ResponseInputAnyOfValue.to_json())

# convert the object into a dict
execute200_response_input_any_of_value_dict = execute200_response_input_any_of_value_instance.to_dict()
# create an instance of Execute200ResponseInputAnyOfValue from a dict
execute200_response_input_any_of_value_from_dict = Execute200ResponseInputAnyOfValue.from_dict(execute200_response_input_any_of_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
