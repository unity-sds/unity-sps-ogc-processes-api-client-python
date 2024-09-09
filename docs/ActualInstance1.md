# ActualInstance1


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

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.actual_instance1 import ActualInstance1

# TODO update the JSON string below
json = "{}"
# create an instance of ActualInstance1 from a JSON string
actual_instance1_instance = ActualInstance1.from_json(json)
# print the JSON string representation of the object
print(ActualInstance1.to_json())

# convert the object into a dict
actual_instance1_dict = actual_instance1_instance.to_dict()
# create an instance of ActualInstance1 from a dict
actual_instance1_from_dict = ActualInstance1.from_dict(actual_instance1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
