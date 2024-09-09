# QualifiedInputValueInput

QualifiedInputValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueInput**](InputValueInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.qualified_input_value_input import QualifiedInputValueInput

# TODO update the JSON string below
json = "{}"
# create an instance of QualifiedInputValueInput from a JSON string
qualified_input_value_input_instance = QualifiedInputValueInput.from_json(json)
# print the JSON string representation of the object
print(QualifiedInputValueInput.to_json())

# convert the object into a dict
qualified_input_value_input_dict = qualified_input_value_input_instance.to_dict()
# create an instance of QualifiedInputValueInput from a dict
qualified_input_value_input_from_dict = QualifiedInputValueInput.from_dict(qualified_input_value_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
