# ProcessListOutput

ProcessList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  |
**processes** | [**List[ProcessSummaryOutput]**](ProcessSummaryOutput.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.process_list_output import ProcessListOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessListOutput from a JSON string
process_list_output_instance = ProcessListOutput.from_json(json)
# print the JSON string representation of the object
print(ProcessListOutput.to_json())

# convert the object into a dict
process_list_output_dict = process_list_output_instance.to_dict()
# create an instance of ProcessListOutput from a dict
process_list_output_from_dict = ProcessListOutput.from_dict(process_list_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
