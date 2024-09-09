# OutputWorkflows1

OutputWorkflows1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | [optional]
**format** | [**Format**](Format.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.output_workflows1 import OutputWorkflows1

# TODO update the JSON string below
json = "{}"
# create an instance of OutputWorkflows1 from a JSON string
output_workflows1_instance = OutputWorkflows1.from_json(json)
# print the JSON string representation of the object
print(OutputWorkflows1.to_json())

# convert the object into a dict
output_workflows1_dict = output_workflows1_instance.to_dict()
# create an instance of OutputWorkflows1 from a dict
output_workflows1_from_dict = OutputWorkflows1.from_dict(output_workflows1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
