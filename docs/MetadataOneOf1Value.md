# MetadataOneOf1Value

MetadataOneOf1Value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oneof_schema_1_validator** | **str** |  | [optional]
**oneof_schema_2_validator** | **object** |  | [optional]
**actual_instance** | **str** |  | [optional]
**one_of_schemas** | **List[str]** |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.metadata_one_of1_value import MetadataOneOf1Value

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOneOf1Value from a JSON string
metadata_one_of1_value_instance = MetadataOneOf1Value.from_json(json)
# print the JSON string representation of the object
print(MetadataOneOf1Value.to_json())

# convert the object into a dict
metadata_one_of1_value_dict = metadata_one_of1_value_instance.to_dict()
# create an instance of MetadataOneOf1Value from a dict
metadata_one_of1_value_from_dict = MetadataOneOf1Value.from_dict(metadata_one_of1_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
