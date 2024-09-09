# MetadataInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  |
**hreflang** | **str** |  | [optional]
**rel** | **str** |  | [optional]
**role** | **str** |  | [optional]
**title** | **str** |  | [optional]
**type** | **str** |  | [optional]
**lang** | **str** |  | [optional]
**value** | [**MetadataOneOf1Value**](MetadataOneOf1Value.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.metadata_input import MetadataInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataInput from a JSON string
metadata_input_instance = MetadataInput.from_json(json)
# print the JSON string representation of the object
print(MetadataInput.to_json())

# convert the object into a dict
metadata_input_dict = metadata_input_instance.to_dict()
# create an instance of MetadataInput from a dict
metadata_input_from_dict = MetadataInput.from_dict(metadata_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
