# ProcessInput


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
**inputs** | [**List[InputValueInput]**](InputValueInput.md) |  | [optional]
**outputs** | [**List[InputValueInput]**](InputValueInput.md) |  | [optional]

## Example

```python
from unity_sps_ogc_processes_api_python_client.models.process_input import ProcessInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessInput from a JSON string
process_input_instance = ProcessInput.from_json(json)
# print the JSON string representation of the object
print(ProcessInput.to_json())

# convert the object into a dict
process_input_dict = process_input_instance.to_dict()
# create an instance of ProcessInput from a dict
process_input_from_dict = ProcessInput.from_dict(process_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
