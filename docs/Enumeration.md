# Enumeration

Enumeration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  |
**enum** | **List[str]** |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.enumeration import Enumeration

# TODO update the JSON string below
json = "{}"
# create an instance of Enumeration from a JSON string
enumeration_instance = Enumeration.from_json(json)
# print the JSON string representation of the object
print(Enumeration.to_json())

# convert the object into a dict
enumeration_dict = enumeration_instance.to_dict()
# create an instance of Enumeration from a dict
enumeration_from_dict = Enumeration.from_dict(enumeration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
