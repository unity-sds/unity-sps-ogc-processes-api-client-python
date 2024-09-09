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

from unity_sps_ogc_processes_api_python_client.models.fields_modifiers_properties import (
    FieldsModifiersProperties,
)
from unity_sps_ogc_processes_api_python_client.models.input_workflows1 import (
    InputWorkflows1,
)
from unity_sps_ogc_processes_api_python_client.models.output_workflows1 import (
    OutputWorkflows1,
)
from unity_sps_ogc_processes_api_python_client.models.subscriber import Subscriber


class InputProcess(BaseModel):
    """
    InputProcess
    """  # noqa: E501

    process: StrictStr = Field(
        description="URI to the process execution end point (i.e., `.../processes/{processId}/execution`)"
    )
    inputs: Optional[Dict[str, InputWorkflows1]] = None
    outputs: Optional[Dict[str, OutputWorkflows1]] = None
    subscriber: Optional[Subscriber] = None
    filter: Optional[StrictStr] = None
    properties: Optional[FieldsModifiersProperties] = None
    sort_by: Optional[List[StrictStr]] = Field(default=None, alias="sortBy")
    __properties: ClassVar[List[str]] = [
        "process",
        "inputs",
        "outputs",
        "subscriber",
        "filter",
        "properties",
        "sortBy",
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
        """Create an instance of InputProcess from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in outputs (dict)
        _field_dict = {}
        if self.outputs:
            for _key in self.outputs:
                if self.outputs[_key]:
                    _field_dict[_key] = self.outputs[_key].to_dict()
            _dict["outputs"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of subscriber
        if self.subscriber:
            _dict["subscriber"] = self.subscriber.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict["properties"] = self.properties.to_dict()
        # set to None if inputs (nullable) is None
        # and model_fields_set contains the field
        if self.inputs is None and "inputs" in self.model_fields_set:
            _dict["inputs"] = None

        # set to None if outputs (nullable) is None
        # and model_fields_set contains the field
        if self.outputs is None and "outputs" in self.model_fields_set:
            _dict["outputs"] = None

        # set to None if subscriber (nullable) is None
        # and model_fields_set contains the field
        if self.subscriber is None and "subscriber" in self.model_fields_set:
            _dict["subscriber"] = None

        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict["filter"] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict["properties"] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict["sortBy"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InputProcess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "process": obj.get("process"),
                "inputs": (
                    dict(
                        (_k, InputWorkflows1.from_dict(_v))
                        for _k, _v in obj["inputs"].items()
                    )
                    if obj.get("inputs") is not None
                    else None
                ),
                "outputs": (
                    dict(
                        (_k, OutputWorkflows1.from_dict(_v))
                        for _k, _v in obj["outputs"].items()
                    )
                    if obj.get("outputs") is not None
                    else None
                ),
                "subscriber": (
                    Subscriber.from_dict(obj["subscriber"])
                    if obj.get("subscriber") is not None
                    else None
                ),
                "filter": obj.get("filter"),
                "properties": (
                    FieldsModifiersProperties.from_dict(obj["properties"])
                    if obj.get("properties") is not None
                    else None
                ),
                "sortBy": obj.get("sortBy"),
            }
        )
        return _obj


# TODO: Rewrite to not use raise_errors
InputProcess.model_rebuild(raise_errors=False)
