# BboxDefCrs

BboxDefCrs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_instance** | **object** |  | [optional]
**any_of_schemas** | **List[str]** |  | [optional]
**anyof_schema_1_validator** | **str** |  | [optional]
**anyof_schema_2_validator** | **str** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.bbox_def_crs import BboxDefCrs

# TODO update the JSON string below
json = "{}"
# create an instance of BboxDefCrs from a JSON string
bbox_def_crs_instance = BboxDefCrs.from_json(json)
# print the JSON string representation of the object
print(BboxDefCrs.to_json())

# convert the object into a dict
bbox_def_crs_dict = bbox_def_crs_instance.to_dict()
# create an instance of BboxDefCrs from a dict
bbox_def_crs_from_dict = BboxDefCrs.from_dict(bbox_def_crs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
