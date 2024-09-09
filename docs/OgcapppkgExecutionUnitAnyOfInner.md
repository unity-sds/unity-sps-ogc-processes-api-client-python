# OgcapppkgExecutionUnitAnyOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**image** | **str** | Container image reference for the execution unit. |
**deployment** | **str** |  | [optional]
**config** | [**ExecutionUnitConfig**](ExecutionUnitConfig.md) |  | [optional]
**additional_properties** | **object** |  | [optional]
**href** | **str** |  |
**rel** | **str** |  | [optional]
**hreflang** | **str** |  | [optional]
**title** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueInput**](InputValueInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg_execution_unit_any_of_inner import OgcapppkgExecutionUnitAnyOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of OgcapppkgExecutionUnitAnyOfInner from a JSON string
ogcapppkg_execution_unit_any_of_inner_instance = OgcapppkgExecutionUnitAnyOfInner.from_json(json)
# print the JSON string representation of the object
print(OgcapppkgExecutionUnitAnyOfInner.to_json())

# convert the object into a dict
ogcapppkg_execution_unit_any_of_inner_dict = ogcapppkg_execution_unit_any_of_inner_instance.to_dict()
# create an instance of OgcapppkgExecutionUnitAnyOfInner from a dict
ogcapppkg_execution_unit_any_of_inner_from_dict = OgcapppkgExecutionUnitAnyOfInner.from_dict(ogcapppkg_execution_unit_any_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
