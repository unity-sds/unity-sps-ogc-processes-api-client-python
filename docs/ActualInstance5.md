# ActualInstance5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance3**](ActualInstance3.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**Reference**](Reference.md) |  | [optional]
**oneof_schema_2_validator** | [**SchemaOneOfInput**](SchemaOneOfInput.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.actual_instance5 import ActualInstance5

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance5 from a JSON string
actual_instance5_instance = ActualInstance5.from_json(json)
# print the JSON string representation of the object
print(ActualInstance5.to_json())

# convert the object into a dict
actual_instance5_dict = actual_instance5_instance.to_dict()
# create an instance of ActualInstance5 from a dict
actual_instance5_from_dict = ActualInstance5.from_dict(actual_instance5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
