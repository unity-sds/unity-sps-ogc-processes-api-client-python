# InlineOrRefDataInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**List[BboxBboxInner]**](BboxBboxInner.md) |  |
**crs** | [**BboxDefCrs**](BboxDefCrs.md) |  | [optional]
**href** | **str** |  |
**rel** | **str** |  | [optional]
**type** | **str** |  | [optional]
**hreflang** | **str** |  | [optional]
**title** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueInput**](InputValueInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_input import InlineOrRefDataInput

# TODO update the JSON string below
json = "{}"
# create an instance of InlineOrRefDataInput from a JSON string
inline_or_ref_data_input_instance = InlineOrRefDataInput.from_json(json)
# print the JSON string representation of the object
print(InlineOrRefDataInput.to_json())

# convert the object into a dict
inline_or_ref_data_input_dict = inline_or_ref_data_input_instance.to_dict()
# create an instance of InlineOrRefDataInput from a dict
inline_or_ref_data_input_from_dict = InlineOrRefDataInput.from_dict(inline_or_ref_data_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
