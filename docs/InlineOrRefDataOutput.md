# InlineOrRefDataOutput


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
**value** | [**InputValueOutput**](InputValueOutput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_output import InlineOrRefDataOutput

# TODO update the JSON string below
json = "{}"
# create an instance of InlineOrRefDataOutput from a JSON string
inline_or_ref_data_output_instance = InlineOrRefDataOutput.from_json(json)
# print the JSON string representation of the object
print(InlineOrRefDataOutput.to_json())

# convert the object into a dict
inline_or_ref_data_output_dict = inline_or_ref_data_output_instance.to_dict()
# create an instance of InlineOrRefDataOutput from a dict
inline_or_ref_data_output_from_dict = InlineOrRefDataOutput.from_dict(inline_or_ref_data_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
