# InputParameterized

InputParameterized

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** |  |
**filter** | **str** |  | [optional]
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_parameterized import InputParameterized

# TODO update the JSON string below
json = "{}"
# create an instance of InputParameterized from a JSON string
input_parameterized_instance = InputParameterized.from_json(json)
# print the JSON string representation of the object
print(InputParameterized.to_json())

# convert the object into a dict
input_parameterized_dict = input_parameterized_instance.to_dict()
# create an instance of InputParameterized from a dict
input_parameterized_from_dict = InputParameterized.from_dict(input_parameterized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
