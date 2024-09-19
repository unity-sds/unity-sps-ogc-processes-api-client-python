# ProcessListInput

ProcessList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  |
**processes** | [**List[ProcessSummaryInput]**](ProcessSummaryInput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.process_list_input import ProcessListInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessListInput from a JSON string
process_list_input_instance = ProcessListInput.from_json(json)
# print the JSON string representation of the object
print(ProcessListInput.to_json())

# convert the object into a dict
process_list_input_dict = process_list_input_instance.to_dict()
# create an instance of ProcessListInput from a dict
process_list_input_from_dict = ProcessListInput.from_dict(process_list_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
