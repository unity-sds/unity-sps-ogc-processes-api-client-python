# InputWorkflows1

InputWorkflows1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance2**](ActualInstance2.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**InlineOrRefDataWorkflows**](InlineOrRefDataWorkflows.md) |  | [optional]
**oneof_schema_2_validator** | [**List[InlineOrRefDataWorkflows]**](InlineOrRefDataWorkflows.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_workflows1 import InputWorkflows1

# TODO update the JSON string below
json = "{}"
# create an instance of InputWorkflows1 from a JSON string
input_workflows1_instance = InputWorkflows1.from_json(json)
# print the JSON string representation of the object
print(InputWorkflows1.to_json())

# convert the object into a dict
input_workflows1_dict = input_workflows1_instance.to_dict()
# create an instance of InputWorkflows1 from a dict
input_workflows1_from_dict = InputWorkflows1.from_dict(input_workflows1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
