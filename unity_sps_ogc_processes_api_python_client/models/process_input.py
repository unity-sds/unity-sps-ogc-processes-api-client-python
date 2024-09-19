# coding: utf-8

"""
    Unity Processing API conforming to the Draft of OGC API - Processes - Part 2: Deploy, Replace, Undeploy

    This document is an API definition document provided alongside the OGC API - Processes standard. The OGC API - Processes Standard specifies a processing interface to communicate over a RESTful protocol using JavaScript Object Notation (JSON) encodings. The specification allows for the wrapping of computational tasks into executable processes that can be offered by a server and be invoked by a client application.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from unity_sps_ogc_processes_api_python_client.models.input_description_input import (
    InputDescriptionInput,
)
from unity_sps_ogc_processes_api_python_client.models.job_control_options import (
    JobControlOptions,
)
from unity_sps_ogc_processes_api_python_client.models.link import Link
from unity_sps_ogc_processes_api_python_client.models.metadata_input import (
    MetadataInput,
)
from unity_sps_ogc_processes_api_python_client.models.output_description_input import (
    OutputDescriptionInput,
)


class ProcessInput(BaseModel):
    """
    Process
    """  # noqa: E501

    description: Optional[StrictStr] = None
    id: StrictStr
    inputs: Optional[Dict[str, InputDescriptionInput]] = None
    job_control_options: Optional[List[JobControlOptions]] = Field(
        default=None, alias="jobControlOptions"
    )
    keywords: Optional[List[StrictStr]] = None
    links: Optional[List[Link]] = None
    metadata: Optional[List[MetadataInput]] = None
    outputs: Optional[Dict[str, OutputDescriptionInput]] = None
    title: Optional[StrictStr] = None
    version: StrictStr
    __properties: ClassVar[List[str]] = [
        "description",
        "id",
        "inputs",
        "jobControlOptions",
        "keywords",
        "links",
        "metadata",
        "outputs",
        "title",
        "version",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProcessInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in inputs (dict)
        _field_dict = {}
        if self.inputs:
            for _key in self.inputs:
                if self.inputs[_key]:
                    _field_dict[_key] = self.inputs[_key].to_dict()
            _dict["inputs"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict["links"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict["metadata"] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in outputs (dict)
        _field_dict = {}
        if self.outputs:
            for _key in self.outputs:
                if self.outputs[_key]:
                    _field_dict[_key] = self.outputs[_key].to_dict()
            _dict["outputs"] = _field_dict
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict["description"] = None

        # set to None if inputs (nullable) is None
        # and model_fields_set contains the field
        if self.inputs is None and "inputs" in self.model_fields_set:
            _dict["inputs"] = None

        # set to None if job_control_options (nullable) is None
        # and model_fields_set contains the field
        if (
            self.job_control_options is None
            and "job_control_options" in self.model_fields_set
        ):
            _dict["jobControlOptions"] = None

        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict["keywords"] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict["links"] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict["metadata"] = None

        # set to None if outputs (nullable) is None
        # and model_fields_set contains the field
        if self.outputs is None and "outputs" in self.model_fields_set:
            _dict["outputs"] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict["title"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProcessInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "id": obj.get("id"),
                "inputs": (
                    dict(
                        (_k, InputDescriptionInput.from_dict(_v))
                        for _k, _v in obj["inputs"].items()
                    )
                    if obj.get("inputs") is not None
                    else None
                ),
                "jobControlOptions": obj.get("jobControlOptions"),
                "keywords": obj.get("keywords"),
                "links": (
                    [Link.from_dict(_item) for _item in obj["links"]]
                    if obj.get("links") is not None
                    else None
                ),
                "metadata": (
                    [MetadataInput.from_dict(_item) for _item in obj["metadata"]]
                    if obj.get("metadata") is not None
                    else None
                ),
                "outputs": (
                    dict(
                        (_k, OutputDescriptionInput.from_dict(_v))
                        for _k, _v in obj["outputs"].items()
                    )
                    if obj.get("outputs") is not None
                    else None
                ),
                "title": obj.get("title"),
                "version": obj.get("version"),
            }
        )
        return _obj
