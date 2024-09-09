# Ogcapppkg

Ogcapppkg

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_unit** | [**OgcapppkgExecutionUnit**](OgcapppkgExecutionUnit.md) |  |
**process_description** | [**ProcessInput**](ProcessInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.ogcapppkg import Ogcapppkg

# TODO update the JSON string below
json = "{}"
# create an instance of Ogcapppkg from a JSON string
ogcapppkg_instance = Ogcapppkg.from_json(json)
# print the JSON string representation of the object
print(Ogcapppkg.to_json())

# convert the object into a dict
ogcapppkg_dict = ogcapppkg_instance.to_dict()
# create an instance of Ogcapppkg from a dict
ogcapppkg_from_dict = Ogcapppkg.from_dict(ogcapppkg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
