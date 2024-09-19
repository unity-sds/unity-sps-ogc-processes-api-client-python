# JobListOutput

JobList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[StatusInfo]**](StatusInfo.md) |  |
**links** | [**List[Link]**](Link.md) |  |

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.job_list_output import JobListOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JobListOutput from a JSON string
job_list_output_instance = JobListOutput.from_json(json)
# print the JSON string representation of the object
print(JobListOutput.to_json())

# convert the object into a dict
job_list_output_dict = job_list_output_instance.to_dict()
# create an instance of JobListOutput from a dict
job_list_output_from_dict = JobListOutput.from_dict(job_list_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
