# StatusInfo

StatusInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional]
**exception** | [**Exception**](Exception.md) |  | [optional]
**finished** | **datetime** |  | [optional]
**job_id** | **str** |  |
**links** | [**List[Link]**](Link.md) |  | [optional]
**message** | **str** |  | [optional]
**process_id** | **str** |  | [optional]
**progress** | **int** |  | [optional]
**started** | **datetime** |  | [optional]
**status** | [**StatusCode**](StatusCode.md) |  |
**type** | **str** |  |
**updated** | **datetime** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.status_info import StatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StatusInfo from a JSON string
status_info_instance = StatusInfo.from_json(json)
# print the JSON string representation of the object
print(StatusInfo.to_json())

# convert the object into a dict
status_info_dict = status_info_instance.to_dict()
# create an instance of StatusInfo from a dict
status_info_from_dict = StatusInfo.from_dict(status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
