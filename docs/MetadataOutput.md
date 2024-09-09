# MetadataOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  |
**rel** | **str** |  | [optional]
**type** | **str** |  | [optional]
**hreflang** | **str** |  | [optional]
**title** | **str** |  | [optional]
**role** | **str** |  | [optional]
**lang** | **str** |  | [optional]
**value** | [**MetadataOneOf1Value**](MetadataOneOf1Value.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.metadata_output import MetadataOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOutput from a JSON string
metadata_output_instance = MetadataOutput.from_json(json)
# print the JSON string representation of the object
print(MetadataOutput.to_json())

# convert the object into a dict
metadata_output_dict = metadata_output_instance.to_dict()
# create an instance of MetadataOutput from a dict
metadata_output_from_dict = MetadataOutput.from_dict(metadata_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
