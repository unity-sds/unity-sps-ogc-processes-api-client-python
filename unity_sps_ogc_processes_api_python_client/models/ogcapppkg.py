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

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Self

from unity_sps_ogc_processes_api_python_client.models.ogcapppkg_execution_unit import (
    OgcapppkgExecutionUnit,
)
from unity_sps_ogc_processes_api_python_client.models.process_input import ProcessInput


class Ogcapppkg(BaseModel):
    """
    Ogcapppkg
    """  # noqa: E501

    execution_unit: OgcapppkgExecutionUnit = Field(alias="executionUnit")
    process_description: ProcessInput = Field(alias="processDescription")
    __properties: ClassVar[List[str]] = ["executionUnit", "processDescription"]

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
        """Create an instance of Ogcapppkg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of execution_unit
        if self.execution_unit:
            _dict["executionUnit"] = self.execution_unit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of process_description
        if self.process_description:
            _dict["processDescription"] = self.process_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Ogcapppkg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "executionUnit": (
                    OgcapppkgExecutionUnit.from_dict(obj["executionUnit"])
                    if obj.get("executionUnit") is not None
                    else None
                ),
                "processDescription": (
                    ProcessInput.from_dict(obj["processDescription"])
                    if obj.get("processDescription") is not None
                    else None
                ),
            }
        )
        return _obj
