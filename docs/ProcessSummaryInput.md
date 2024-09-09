# ProcessSummaryInput

ProcessSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional]
**description** | **str** |  | [optional]
**keywords** | **List[str]** |  | [optional]
**metadata** | [**List[MetadataInput]**](MetadataInput.md) |  | [optional]
**id** | **str** |  |
**version** | **str** |  |
**job_control_options** | [**List[JobControlOptions]**](JobControlOptions.md) |  | [optional]
**links** | [**List[Link]**](Link.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.process_summary_input import ProcessSummaryInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessSummaryInput from a JSON string
process_summary_input_instance = ProcessSummaryInput.from_json(json)
# print the JSON string representation of the object
print(ProcessSummaryInput.to_json())

# convert the object into a dict
process_summary_input_dict = process_summary_input_instance.to_dict()
# create an instance of ProcessSummaryInput from a dict
process_summary_input_from_dict = ProcessSummaryInput.from_dict(process_summary_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
