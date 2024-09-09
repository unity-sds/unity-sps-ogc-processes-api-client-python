# Bbox1

Bbox1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | [**List[BboxBboxInner]**](BboxBboxInner.md) |  |
**crs** | [**BboxDefCrs**](BboxDefCrs.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.bbox1 import Bbox1

# TODO update the JSON string below
json = "{}"
# create an instance of Bbox1 from a JSON string
bbox1_instance = Bbox1.from_json(json)
# print the JSON string representation of the object
print(Bbox1.to_json())

# convert the object into a dict
bbox1_dict = bbox1_instance.to_dict()
# create an instance of Bbox1 from a dict
bbox1_from_dict = Bbox1.from_dict(bbox1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
