# QualifiedInputValueWorkflows

QualifiedInputValueWorkflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**filter** | **str** |  | [optional]
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]
**value** | [**InputValueWorkflows**](InputValueWorkflows.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.qualified_input_value_workflows import QualifiedInputValueWorkflows

# TODO update the JSON string below
json = "{}"
# create an instance of QualifiedInputValueWorkflows from a JSON string
qualified_input_value_workflows_instance = QualifiedInputValueWorkflows.from_json(json)
# print the JSON string representation of the object
print(QualifiedInputValueWorkflows.to_json())

# convert the object into a dict
qualified_input_value_workflows_dict = qualified_input_value_workflows_instance.to_dict()
# create an instance of QualifiedInputValueWorkflows from a dict
qualified_input_value_workflows_from_dict = QualifiedInputValueWorkflows.from_dict(qualified_input_value_workflows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
