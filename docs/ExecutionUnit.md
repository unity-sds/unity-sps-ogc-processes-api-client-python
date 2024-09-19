# ExecutionUnit

Resource containing an executable or runtime information for executing the process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **object** |  | [optional]
**config** | [**ExecutionUnitConfig**](ExecutionUnitConfig.md) |  | [optional]
**deployment** | **str** |  | [optional]
**image** | **str** | Container image reference for the execution unit. |
**type** | **str** | Type of execution unit. |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.execution_unit import ExecutionUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionUnit from a JSON string
execution_unit_instance = ExecutionUnit.from_json(json)
# print the JSON string representation of the object
print(ExecutionUnit.to_json())

# convert the object into a dict
execution_unit_dict = execution_unit_instance.to_dict()
# create an instance of ExecutionUnit from a dict
execution_unit_from_dict = ExecutionUnit.from_dict(execution_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
