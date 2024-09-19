# QualifiedInputValueOutput

QualifiedInputValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueOutput**](InputValueOutput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.qualified_input_value_output import QualifiedInputValueOutput

# TODO update the JSON string below
json = "{}"
# create an instance of QualifiedInputValueOutput from a JSON string
qualified_input_value_output_instance = QualifiedInputValueOutput.from_json(json)
# print the JSON string representation of the object
print(QualifiedInputValueOutput.to_json())

# convert the object into a dict
qualified_input_value_output_dict = qualified_input_value_output_instance.to_dict()
# create an instance of QualifiedInputValueOutput from a dict
qualified_input_value_output_from_dict = QualifiedInputValueOutput.from_dict(qualified_input_value_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
