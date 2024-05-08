# ProcessOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) |  | [optional] 
**id** | **str** |  | 
**version** | **str** |  | 
**job_control_options** | [**List[JobControlOptions]**](JobControlOptions.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**inputs** | [**List[InputValueOutput]**](InputValueOutput.md) |  | [optional] 
**outputs** | [**List[InputValueOutput]**](InputValueOutput.md) |  | [optional] 

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.process_output import ProcessOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessOutput from a JSON string
process_output_instance = ProcessOutput.from_json(json)
# print the JSON string representation of the object
print(ProcessOutput.to_json())

# convert the object into a dict
process_output_dict = process_output_instance.to_dict()
# create an instance of ProcessOutput from a dict
process_output_from_dict = ProcessOutput.from_dict(process_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


