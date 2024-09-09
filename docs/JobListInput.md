# JobListInput

JobList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[StatusInfo]**](StatusInfo.md) |  |
**links** | [**List[Link]**](Link.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.job_list_input import JobListInput

# TODO update the JSON string below
json = "{}"
# create an instance of JobListInput from a JSON string
job_list_input_instance = JobListInput.from_json(json)
# print the JSON string representation of the object
print(JobListInput.to_json())

# convert the object into a dict
job_list_input_dict = job_list_input_instance.to_dict()
# create an instance of JobListInput from a dict
job_list_input_from_dict = JobListInput.from_dict(job_list_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
