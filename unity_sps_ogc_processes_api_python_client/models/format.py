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

from unity_sps_ogc_processes_api_python_client.models.format_schema import FormatSchema


class Format(BaseModel):
    """
    Format
    """  # noqa: E501

    encoding: Optional[StrictStr] = None
    media_type: Optional[StrictStr] = Field(default=None, alias="mediaType")
    var_schema: Optional[FormatSchema] = Field(default=None, alias="schema")
    __properties: ClassVar[List[str]] = ["encoding", "mediaType", "schema"]

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
        """Create an instance of Format from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        # set to None if encoding (nullable) is None
        # and model_fields_set contains the field
        if self.encoding is None and "encoding" in self.model_fields_set:
            _dict["encoding"] = None

        # set to None if media_type (nullable) is None
        # and model_fields_set contains the field
        if self.media_type is None and "media_type" in self.model_fields_set:
            _dict["mediaType"] = None

        # set to None if var_schema (nullable) is None
        # and model_fields_set contains the field
        if self.var_schema is None and "var_schema" in self.model_fields_set:
            _dict["schema"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Format from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "encoding": obj.get("encoding"),
                "mediaType": obj.get("mediaType"),
                "schema": (
                    FormatSchema.from_dict(obj["schema"])
                    if obj.get("schema") is not None
                    else None
                ),
            }
        )
        return _obj
