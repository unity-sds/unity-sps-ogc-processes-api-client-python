# InputProcess

InputProcess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** |  | [optional]
**inputs** | [**Dict[str, InputWorkflows1]**](InputWorkflows1.md) |  | [optional]
**outputs** | [**Dict[str, OutputWorkflows1]**](OutputWorkflows1.md) |  | [optional]
**process** | **str** | URI to the process execution end point (i.e., &#x60;.../processes/{processId}/execution&#x60;) |
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]
**subscriber** | [**Subscriber**](Subscriber.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_process import InputProcess

# TODO update the JSON string below
json = "{}"
# create an instance of InputProcess from a JSON string
input_process_instance = InputProcess.from_json(json)
# print the JSON string representation of the object
print(InputProcess.to_json())

# convert the object into a dict
input_process_dict = input_process_instance.to_dict()
# create an instance of InputProcess from a dict
input_process_from_dict = InputProcess.from_dict(input_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
