# MetadataOneOf1

MetadataOneOf1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional]
**title** | **str** |  | [optional]
**lang** | **str** |  | [optional]
**value** | [**MetadataOneOf1Value**](MetadataOneOf1Value.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.metadata_one_of1 import MetadataOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOneOf1 from a JSON string
metadata_one_of1_instance = MetadataOneOf1.from_json(json)
# print the JSON string representation of the object
print(MetadataOneOf1.to_json())

# convert the object into a dict
metadata_one_of1_dict = metadata_one_of1_instance.to_dict()
# create an instance of MetadataOneOf1 from a dict
metadata_one_of1_from_dict = MetadataOneOf1.from_dict(metadata_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
