# ExecutionUnitConfig

Hardware requirements and configuration properties for executing the process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_min** | [**Cpumin**](Cpumin.md) |  | [optional]
**cpu_max** | [**Cpumax**](Cpumax.md) |  | [optional]
**memory_min** | [**Memorymin**](Memorymin.md) |  | [optional]
**memory_max** | [**Memorymax**](Memorymax.md) |  | [optional]
**storage_temp_min** | [**Storagetempmin**](Storagetempmin.md) |  | [optional]
**storage_outputs_min** | [**Storageoutputsmin**](Storageoutputsmin.md) |  | [optional]
**job_timeout** | [**Jobtimeout**](Jobtimeout.md) |  | [optional]
**additional_properties** | **object** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.execution_unit_config import ExecutionUnitConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionUnitConfig from a JSON string
execution_unit_config_instance = ExecutionUnitConfig.from_json(json)
# print the JSON string representation of the object
print(ExecutionUnitConfig.to_json())

# convert the object into a dict
execution_unit_config_dict = execution_unit_config_instance.to_dict()
# create an instance of ExecutionUnitConfig from a dict
execution_unit_config_from_dict = ExecutionUnitConfig.from_dict(execution_unit_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
