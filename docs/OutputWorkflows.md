# OutputWorkflows

OutputWorkflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | [optional]
**format** | [**Format**](Format.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.output_workflows import OutputWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of OutputWorkflows from a JSON string
output_workflows_instance = OutputWorkflows.from_json(json)
# print the JSON string representation of the object
print(OutputWorkflows.to_json())

# convert the object into a dict
output_workflows_dict = output_workflows_instance.to_dict()
# create an instance of OutputWorkflows from a dict
output_workflows_from_dict = OutputWorkflows.from_dict(output_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
