# OgcapppkgExecutionUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **object** |  | [optional]
**config** | [**ExecutionUnitConfig**](ExecutionUnitConfig.md) |  | [optional]
**deployment** | **str** |  | [optional]
**image** | **str** | Container image reference for the execution unit. |
**type** | **str** |  |
**href** | **str** |  |
**hreflang** | **str** |  | [optional]
**rel** | **str** |  | [optional]
**title** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueInput**](InputValueInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg_execution_unit import OgcapppkgExecutionUnit

# TODO update the JSON string below
json = "{}"
# create an instance of OgcapppkgExecutionUnit from a JSON string
ogcapppkg_execution_unit_instance = OgcapppkgExecutionUnit.from_json(json)
# print the JSON string representation of the object
print(OgcapppkgExecutionUnit.to_json())

# convert the object into a dict
ogcapppkg_execution_unit_dict = ogcapppkg_execution_unit_instance.to_dict()
# create an instance of OgcapppkgExecutionUnit from a dict
ogcapppkg_execution_unit_from_dict = OgcapppkgExecutionUnit.from_dict(ogcapppkg_execution_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
