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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing_extensions import Self


class InputWorkflows1(BaseModel):
    """
    InputWorkflows1
    """  # noqa: E501

    actual_instance: Optional[ActualInstance2] = None
    one_of_schemas: Optional[List[StrictStr]] = None
    oneof_schema_1_validator: Optional[InlineOrRefDataWorkflows] = None
    oneof_schema_2_validator: Optional[List[InlineOrRefDataWorkflows]] = None
    __properties: ClassVar[List[str]] = [
        "actual_instance",
        "one_of_schemas",
        "oneof_schema_1_validator",
        "oneof_schema_2_validator",
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
        """Create an instance of InputWorkflows1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actual_instance
        if self.actual_instance:
            _dict["actual_instance"] = self.actual_instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneof_schema_1_validator
        if self.oneof_schema_1_validator:
            _dict["oneof_schema_1_validator"] = self.oneof_schema_1_validator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in oneof_schema_2_validator (list)
        _items = []
        if self.oneof_schema_2_validator:
            for _item in self.oneof_schema_2_validator:
                if _item:
                    _items.append(_item.to_dict())
            _dict["oneof_schema_2_validator"] = _items
        # set to None if actual_instance (nullable) is None
        # and model_fields_set contains the field
        if self.actual_instance is None and "actual_instance" in self.model_fields_set:
            _dict["actual_instance"] = None

        # set to None if oneof_schema_1_validator (nullable) is None
        # and model_fields_set contains the field
        if (
            self.oneof_schema_1_validator is None
            and "oneof_schema_1_validator" in self.model_fields_set
        ):
            _dict["oneof_schema_1_validator"] = None

        # set to None if oneof_schema_2_validator (nullable) is None
        # and model_fields_set contains the field
        if (
            self.oneof_schema_2_validator is None
            and "oneof_schema_2_validator" in self.model_fields_set
        ):
            _dict["oneof_schema_2_validator"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InputWorkflows1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "actual_instance": (
                    ActualInstance2.from_dict(obj["actual_instance"])
                    if obj.get("actual_instance") is not None
                    else None
                ),
                "one_of_schemas": obj.get("one_of_schemas"),
                "oneof_schema_1_validator": (
                    InlineOrRefDataWorkflows.from_dict(obj["oneof_schema_1_validator"])
                    if obj.get("oneof_schema_1_validator") is not None
                    else None
                ),
                "oneof_schema_2_validator": (
                    [
                        InlineOrRefDataWorkflows.from_dict(_item)
                        for _item in obj["oneof_schema_2_validator"]
                    ]
                    if obj.get("oneof_schema_2_validator") is not None
                    else None
                ),
            }
        )
        return _obj


from unity_sps_ogc_processes_api_python_client.models.actual_instance2 import (
    ActualInstance2,
)
from unity_sps_ogc_processes_api_python_client.models.inline_or_ref_data_workflows import (
    InlineOrRefDataWorkflows,
)

# TODO: Rewrite to not use raise_errors
InputWorkflows1.model_rebuild(raise_errors=False)
