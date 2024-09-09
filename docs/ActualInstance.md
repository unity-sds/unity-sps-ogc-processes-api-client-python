# ActualInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | [**ActualInstance1**](ActualInstance1.md) |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]
**oneof_schema_10_validator** | [**InputParameterized**](InputParameterized.md) |  | [optional]
**oneof_schema_1_validator** | **str** |  | [optional]
**oneof_schema_2_validator** | [**OneofSchema2Validator**](OneofSchema2Validator.md) |  | [optional]
**oneof_schema_3_validator** | **int** |  | [optional]
**oneof_schema_4_validator** | **bool** |  | [optional]
**oneof_schema_5_validator** | **List[object]** |  | [optional]
**oneof_schema_6_validator** | [**OneofSchema6Validator**](OneofSchema6Validator.md) |  | [optional]
**oneof_schema_7_validator** | [**Bbox1**](Bbox1.md) |  | [optional]
**oneof_schema_8_validator** | [**InputCollection**](InputCollection.md) |  | [optional]
**oneof_schema_9_validator** | [**InputProcess**](InputProcess.md) |  | [optional]
**href** | **str** |  |
**hreflang** | **str** |  | [optional]
**rel** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**filter** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]
**value** | [**InputValueWorkflows**](InputValueWorkflows.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.actual_instance import ActualInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance from a JSON string
actual_instance_instance = ActualInstance.from_json(json)
# print the JSON string representation of the object
print(ActualInstance.to_json())

# convert the object into a dict
actual_instance_dict = actual_instance_instance.to_dict()
# create an instance of ActualInstance from a dict
actual_instance_from_dict = ActualInstance.from_dict(actual_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
