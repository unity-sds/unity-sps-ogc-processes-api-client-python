# ActualInstance6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance4**](ActualInstance4.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_1_validator** | [**Reference**](Reference.md) |  | [optional]
**oneof_schema_2_validator** | [**SchemaOneOfOutput**](SchemaOneOfOutput.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.actual_instance6 import ActualInstance6

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance6 from a JSON string
actual_instance6_instance = ActualInstance6.from_json(json)
# print the JSON string representation of the object
print(ActualInstance6.to_json())

# convert the object into a dict
actual_instance6_dict = actual_instance6_instance.to_dict()
# create an instance of ActualInstance6 from a dict
actual_instance6_from_dict = ActualInstance6.from_dict(actual_instance6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
