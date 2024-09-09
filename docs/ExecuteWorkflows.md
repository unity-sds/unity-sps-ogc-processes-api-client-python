# ExecuteWorkflows

ExecuteWorkflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional]
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]
**process** | **str** |  | [optional]
**inputs** | [**Dict[str, InputWorkflows]**](InputWorkflows.md) |  | [optional]
**outputs** | [**Dict[str, OutputWorkflows]**](OutputWorkflows.md) |  | [optional]
**subscriber** | [**Subscriber**](Subscriber.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.execute_workflows import ExecuteWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteWorkflows from a JSON string
execute_workflows_instance = ExecuteWorkflows.from_json(json)
# print the JSON string representation of the object
print(ExecuteWorkflows.to_json())

# convert the object into a dict
execute_workflows_dict = execute_workflows_instance.to_dict()
# create an instance of ExecuteWorkflows from a dict
execute_workflows_from_dict = ExecuteWorkflows.from_dict(execute_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
