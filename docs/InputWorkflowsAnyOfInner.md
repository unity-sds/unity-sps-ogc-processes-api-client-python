# InputWorkflowsAnyOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**List[BboxBboxInner]**](BboxBboxInner.md) |  |
**crs** | [**BboxDefCrs**](BboxDefCrs.md) |  | [optional]
**filter** | **str** |  | [optional]
**properties** | [**FieldsModifiersProperties**](FieldsModifiersProperties.md) |  | [optional]
**sort_by** | **List[str]** |  | [optional]
**collection** | **str** |  |
**input** | **str** |  |
**process** | **str** | URI to the process execution end point (i.e., &#x60;.../processes/{processId}/execution&#x60;) |
**inputs** | [**Dict[str, InputWorkflows1]**](InputWorkflows1.md) |  | [optional]
**outputs** | [**Dict[str, OutputWorkflows1]**](OutputWorkflows1.md) |  | [optional]
**subscriber** | [**Subscriber**](Subscriber.md) |  | [optional]
**href** | **str** |  |
**rel** | **str** |  | [optional]
**type** | **str** |  | [optional]
**hreflang** | **str** |  | [optional]
**title** | **str** |  | [optional]
**media_type** | **str** |  | [optional]
**encoding** | **str** |  | [optional]
**var_schema** | [**FormatSchema**](FormatSchema.md) |  | [optional]
**value** | [**InputValueWorkflows**](InputValueWorkflows.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.input_workflows_any_of_inner import InputWorkflowsAnyOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of InputWorkflowsAnyOfInner from a JSON string
input_workflows_any_of_inner_instance = InputWorkflowsAnyOfInner.from_json(json)
# print the JSON string representation of the object
print(InputWorkflowsAnyOfInner.to_json())

# convert the object into a dict
input_workflows_any_of_inner_dict = input_workflows_any_of_inner_instance.to_dict()
# create an instance of InputWorkflowsAnyOfInner from a dict
input_workflows_any_of_inner_from_dict = InputWorkflowsAnyOfInner.from_dict(input_workflows_any_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
