# ActualInstance2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance**](ActualInstance.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**InputValueNoObjectWorkflows**](InputValueNoObjectWorkflows.md) |  | [optional]
**oneof_schema_2_validator** | [**QualifiedInputValueWorkflows**](QualifiedInputValueWorkflows.md) |  | [optional]
**oneof_schema_3_validator** | [**Link**](Link.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.actual_instance2 import ActualInstance2

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance2 from a JSON string
actual_instance2_instance = ActualInstance2.from_json(json)
# print the JSON string representation of the object
print(ActualInstance2.to_json())

# convert the object into a dict
actual_instance2_dict = actual_instance2_instance.to_dict()
# create an instance of ActualInstance2 from a dict
actual_instance2_from_dict = ActualInstance2.from_dict(actual_instance2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
