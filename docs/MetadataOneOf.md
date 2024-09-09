# MetadataOneOf

MetadataOneOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  |
**rel** | **str** |  | [optional]
**type** | **str** |  | [optional]
**hreflang** | **str** |  | [optional]
**title** | **str** |  | [optional]
**role** | **str** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.metadata_one_of import MetadataOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOneOf from a JSON string
metadata_one_of_instance = MetadataOneOf.from_json(json)
# print the JSON string representation of the object
print(MetadataOneOf.to_json())

# convert the object into a dict
metadata_one_of_dict = metadata_one_of_instance.to_dict()
# create an instance of MetadataOneOf from a dict
metadata_one_of_from_dict = MetadataOneOf.from_dict(metadata_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
