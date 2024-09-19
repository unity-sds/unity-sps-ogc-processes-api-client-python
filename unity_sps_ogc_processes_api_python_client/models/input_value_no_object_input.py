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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing_extensions import Self

from unity_sps_ogc_processes_api_python_client.models.bbox import Bbox
from unity_sps_ogc_processes_api_python_client.models.oneof_schema2_validator import (
    OneofSchema2Validator,
)
from unity_sps_ogc_processes_api_python_client.models.oneof_schema6_validator import (
    OneofSchema6Validator,
)


class InputValueNoObjectInput(BaseModel):
    """
    InputValueNoObject
    """  # noqa: E501

    actual_instance: Optional[Any] = None
    one_of_schemas: Optional[List[StrictStr]] = None
    oneof_schema_1_validator: Optional[StrictStr] = None
    oneof_schema_2_validator: Optional[OneofSchema2Validator] = None
    oneof_schema_3_validator: Optional[StrictInt] = None
    oneof_schema_4_validator: Optional[StrictBool] = None
    oneof_schema_5_validator: Optional[List[Dict[str, Any]]] = None
    oneof_schema_6_validator: Optional[OneofSchema6Validator] = None
    oneof_schema_7_validator: Optional[Bbox] = None
    __properties: ClassVar[List[str]] = [
        "actual_instance",
        "one_of_schemas",
        "oneof_schema_1_validator",
        "oneof_schema_2_validator",
        "oneof_schema_3_validator",
        "oneof_schema_4_validator",
        "oneof_schema_5_validator",
        "oneof_schema_6_validator",
        "oneof_schema_7_validator",
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
        """Create an instance of InputValueNoObjectInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of oneof_schema_2_validator
        if self.oneof_schema_2_validator:
            _dict["oneof_schema_2_validator"] = self.oneof_schema_2_validator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneof_schema_6_validator
        if self.oneof_schema_6_validator:
            _dict["oneof_schema_6_validator"] = self.oneof_schema_6_validator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oneof_schema_7_validator
        if self.oneof_schema_7_validator:
            _dict["oneof_schema_7_validator"] = self.oneof_schema_7_validator.to_dict()
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

        # set to None if oneof_schema_3_validator (nullable) is None
        # and model_fields_set contains the field
        if (
            self.oneof_schema_3_validator is None
            and "oneof_schema_3_validator" in self.model_fields_set
        ):
            _dict["oneof_schema_3_validator"] = None

        # set to None if oneof_schema_4_validator (nullable) is None
        # and model_fields_set contains the field
        if (
            self.oneof_schema_4_validator is None
            and "oneof_schema_4_validator" in self.model_fields_set
        ):
            _dict["oneof_schema_4_validator"] = None

        # set to None if oneof_schema_6_validator (nullable) is None
        # and model_fields_set contains the field
        if (
            self.oneof_schema_6_validator is None
            and "oneof_schema_6_validator" in self.model_fields_set
        ):
            _dict["oneof_schema_6_validator"] = None

        # set to None if oneof_schema_7_validator (nullable) is None
        # and model_fields_set contains the field
        if (
            self.oneof_schema_7_validator is None
            and "oneof_schema_7_validator" in self.model_fields_set
        ):
            _dict["oneof_schema_7_validator"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InputValueNoObjectInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "actual_instance": obj.get("actual_instance"),
                "one_of_schemas": obj.get("one_of_schemas"),
                "oneof_schema_1_validator": obj.get("oneof_schema_1_validator"),
                "oneof_schema_2_validator": (
                    OneofSchema2Validator.from_dict(obj["oneof_schema_2_validator"])
                    if obj.get("oneof_schema_2_validator") is not None
                    else None
                ),
                "oneof_schema_3_validator": obj.get("oneof_schema_3_validator"),
                "oneof_schema_4_validator": obj.get("oneof_schema_4_validator"),
                "oneof_schema_5_validator": obj.get("oneof_schema_5_validator"),
                "oneof_schema_6_validator": (
                    OneofSchema6Validator.from_dict(obj["oneof_schema_6_validator"])
                    if obj.get("oneof_schema_6_validator") is not None
                    else None
                ),
                "oneof_schema_7_validator": (
                    Bbox.from_dict(obj["oneof_schema_7_validator"])
                    if obj.get("oneof_schema_7_validator") is not None
                    else None
                ),
            }
        )
        return _obj
