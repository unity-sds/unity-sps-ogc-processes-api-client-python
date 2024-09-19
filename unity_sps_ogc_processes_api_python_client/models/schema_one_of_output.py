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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing_extensions import Annotated, Self

from unity_sps_ogc_processes_api_python_client.models.maximum import Maximum
from unity_sps_ogc_processes_api_python_client.models.minimum import Minimum
from unity_sps_ogc_processes_api_python_client.models.multipleof import Multipleof


class SchemaOneOfOutput(BaseModel):
    """
    SchemaOneOf
    """  # noqa: E501

    additional_properties: Optional[SchemaOneOfAdditionalPropertiesOutput] = Field(
        default=None, alias="additionalProperties"
    )
    all_of: Optional[List[Schema1Output]] = Field(default=None, alias="allOf")
    any_of: Optional[List[Schema1Output]] = Field(default=None, alias="anyOf")
    content_encoding: Optional[StrictStr] = Field(default=None, alias="contentEncoding")
    content_media_type: Optional[StrictStr] = Field(
        default=None, alias="contentMediaType"
    )
    content_schema: Optional[StrictStr] = Field(default=None, alias="contentSchema")
    default: Optional[Dict[str, Any]] = None
    deprecated: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    enum: Optional[Annotated[List[Dict[str, Any]], Field(min_length=1)]] = None
    example: Optional[Dict[str, Any]] = None
    exclusive_maximum: Optional[StrictBool] = Field(
        default=None, alias="exclusiveMaximum"
    )
    exclusive_minimum: Optional[StrictBool] = Field(
        default=None, alias="exclusiveMinimum"
    )
    format: Optional[StrictStr] = None
    items: Optional[Schema1Output] = None
    max_items: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="maxItems"
    )
    max_length: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="maxLength"
    )
    max_properties: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="maxProperties"
    )
    maximum: Optional[Maximum] = None
    min_items: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="minItems"
    )
    min_length: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="minLength"
    )
    min_properties: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(
        default=None, alias="minProperties"
    )
    minimum: Optional[Minimum] = None
    multiple_of: Optional[Multipleof] = Field(default=None, alias="multipleOf")
    var_not: Optional[Schema1Output] = Field(default=None, alias="not")
    nullable: Optional[StrictBool] = None
    one_of: Optional[List[Schema1Output]] = Field(default=None, alias="oneOf")
    pattern: Optional[StrictStr] = None
    properties: Optional[Dict[str, Schema1Output]] = None
    read_only: Optional[StrictBool] = Field(default=None, alias="readOnly")
    required: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = None
    title: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    unique_items: Optional[StrictBool] = Field(default=None, alias="uniqueItems")
    write_only: Optional[StrictBool] = Field(default=None, alias="writeOnly")
    __properties: ClassVar[List[str]] = [
        "additionalProperties",
        "allOf",
        "anyOf",
        "contentEncoding",
        "contentMediaType",
        "contentSchema",
        "default",
        "deprecated",
        "description",
        "enum",
        "example",
        "exclusiveMaximum",
        "exclusiveMinimum",
        "format",
        "items",
        "maxItems",
        "maxLength",
        "maxProperties",
        "maximum",
        "minItems",
        "minLength",
        "minProperties",
        "minimum",
        "multipleOf",
        "not",
        "nullable",
        "oneOf",
        "pattern",
        "properties",
        "readOnly",
        "required",
        "title",
        "type",
        "uniqueItems",
        "writeOnly",
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
        """Create an instance of SchemaOneOfOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_properties
        if self.additional_properties:
            _dict["additionalProperties"] = self.additional_properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in all_of (list)
        _items = []
        if self.all_of:
            for _item in self.all_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict["allOf"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in any_of (list)
        _items = []
        if self.any_of:
            for _item in self.any_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict["anyOf"] = _items
        # override the default output from pydantic by calling `to_dict()` of items
        if self.items:
            _dict["items"] = self.items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum
        if self.maximum:
            _dict["maximum"] = self.maximum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minimum
        if self.minimum:
            _dict["minimum"] = self.minimum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of multiple_of
        if self.multiple_of:
            _dict["multipleOf"] = self.multiple_of.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_not
        if self.var_not:
            _dict["not"] = self.var_not.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in one_of (list)
        _items = []
        if self.one_of:
            for _item in self.one_of:
                if _item:
                    _items.append(_item.to_dict())
            _dict["oneOf"] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict["properties"] = _field_dict
        # set to None if additional_properties (nullable) is None
        # and model_fields_set contains the field
        if (
            self.additional_properties is None
            and "additional_properties" in self.model_fields_set
        ):
            _dict["additionalProperties"] = None

        # set to None if all_of (nullable) is None
        # and model_fields_set contains the field
        if self.all_of is None and "all_of" in self.model_fields_set:
            _dict["allOf"] = None

        # set to None if any_of (nullable) is None
        # and model_fields_set contains the field
        if self.any_of is None and "any_of" in self.model_fields_set:
            _dict["anyOf"] = None

        # set to None if content_encoding (nullable) is None
        # and model_fields_set contains the field
        if (
            self.content_encoding is None
            and "content_encoding" in self.model_fields_set
        ):
            _dict["contentEncoding"] = None

        # set to None if content_media_type (nullable) is None
        # and model_fields_set contains the field
        if (
            self.content_media_type is None
            and "content_media_type" in self.model_fields_set
        ):
            _dict["contentMediaType"] = None

        # set to None if content_schema (nullable) is None
        # and model_fields_set contains the field
        if self.content_schema is None and "content_schema" in self.model_fields_set:
            _dict["contentSchema"] = None

        # set to None if default (nullable) is None
        # and model_fields_set contains the field
        if self.default is None and "default" in self.model_fields_set:
            _dict["default"] = None

        # set to None if deprecated (nullable) is None
        # and model_fields_set contains the field
        if self.deprecated is None and "deprecated" in self.model_fields_set:
            _dict["deprecated"] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict["description"] = None

        # set to None if enum (nullable) is None
        # and model_fields_set contains the field
        if self.enum is None and "enum" in self.model_fields_set:
            _dict["enum"] = None

        # set to None if example (nullable) is None
        # and model_fields_set contains the field
        if self.example is None and "example" in self.model_fields_set:
            _dict["example"] = None

        # set to None if exclusive_maximum (nullable) is None
        # and model_fields_set contains the field
        if (
            self.exclusive_maximum is None
            and "exclusive_maximum" in self.model_fields_set
        ):
            _dict["exclusiveMaximum"] = None

        # set to None if exclusive_minimum (nullable) is None
        # and model_fields_set contains the field
        if (
            self.exclusive_minimum is None
            and "exclusive_minimum" in self.model_fields_set
        ):
            _dict["exclusiveMinimum"] = None

        # set to None if format (nullable) is None
        # and model_fields_set contains the field
        if self.format is None and "format" in self.model_fields_set:
            _dict["format"] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict["items"] = None

        # set to None if max_items (nullable) is None
        # and model_fields_set contains the field
        if self.max_items is None and "max_items" in self.model_fields_set:
            _dict["maxItems"] = None

        # set to None if max_length (nullable) is None
        # and model_fields_set contains the field
        if self.max_length is None and "max_length" in self.model_fields_set:
            _dict["maxLength"] = None

        # set to None if max_properties (nullable) is None
        # and model_fields_set contains the field
        if self.max_properties is None and "max_properties" in self.model_fields_set:
            _dict["maxProperties"] = None

        # set to None if maximum (nullable) is None
        # and model_fields_set contains the field
        if self.maximum is None and "maximum" in self.model_fields_set:
            _dict["maximum"] = None

        # set to None if min_items (nullable) is None
        # and model_fields_set contains the field
        if self.min_items is None and "min_items" in self.model_fields_set:
            _dict["minItems"] = None

        # set to None if min_length (nullable) is None
        # and model_fields_set contains the field
        if self.min_length is None and "min_length" in self.model_fields_set:
            _dict["minLength"] = None

        # set to None if min_properties (nullable) is None
        # and model_fields_set contains the field
        if self.min_properties is None and "min_properties" in self.model_fields_set:
            _dict["minProperties"] = None

        # set to None if minimum (nullable) is None
        # and model_fields_set contains the field
        if self.minimum is None and "minimum" in self.model_fields_set:
            _dict["minimum"] = None

        # set to None if multiple_of (nullable) is None
        # and model_fields_set contains the field
        if self.multiple_of is None and "multiple_of" in self.model_fields_set:
            _dict["multipleOf"] = None

        # set to None if var_not (nullable) is None
        # and model_fields_set contains the field
        if self.var_not is None and "var_not" in self.model_fields_set:
            _dict["not"] = None

        # set to None if nullable (nullable) is None
        # and model_fields_set contains the field
        if self.nullable is None and "nullable" in self.model_fields_set:
            _dict["nullable"] = None

        # set to None if one_of (nullable) is None
        # and model_fields_set contains the field
        if self.one_of is None and "one_of" in self.model_fields_set:
            _dict["oneOf"] = None

        # set to None if pattern (nullable) is None
        # and model_fields_set contains the field
        if self.pattern is None and "pattern" in self.model_fields_set:
            _dict["pattern"] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict["properties"] = None

        # set to None if read_only (nullable) is None
        # and model_fields_set contains the field
        if self.read_only is None and "read_only" in self.model_fields_set:
            _dict["readOnly"] = None

        # set to None if required (nullable) is None
        # and model_fields_set contains the field
        if self.required is None and "required" in self.model_fields_set:
            _dict["required"] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict["title"] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict["type"] = None

        # set to None if unique_items (nullable) is None
        # and model_fields_set contains the field
        if self.unique_items is None and "unique_items" in self.model_fields_set:
            _dict["uniqueItems"] = None

        # set to None if write_only (nullable) is None
        # and model_fields_set contains the field
        if self.write_only is None and "write_only" in self.model_fields_set:
            _dict["writeOnly"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaOneOfOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "additionalProperties": (
                    SchemaOneOfAdditionalPropertiesOutput.from_dict(
                        obj["additionalProperties"]
                    )
                    if obj.get("additionalProperties") is not None
                    else None
                ),
                "allOf": (
                    [Schema1Output.from_dict(_item) for _item in obj["allOf"]]
                    if obj.get("allOf") is not None
                    else None
                ),
                "anyOf": (
                    [Schema1Output.from_dict(_item) for _item in obj["anyOf"]]
                    if obj.get("anyOf") is not None
                    else None
                ),
                "contentEncoding": obj.get("contentEncoding"),
                "contentMediaType": obj.get("contentMediaType"),
                "contentSchema": obj.get("contentSchema"),
                "default": obj.get("default"),
                "deprecated": obj.get("deprecated"),
                "description": obj.get("description"),
                "enum": obj.get("enum"),
                "example": obj.get("example"),
                "exclusiveMaximum": obj.get("exclusiveMaximum"),
                "exclusiveMinimum": obj.get("exclusiveMinimum"),
                "format": obj.get("format"),
                "items": (
                    Schema1Output.from_dict(obj["items"])
                    if obj.get("items") is not None
                    else None
                ),
                "maxItems": obj.get("maxItems"),
                "maxLength": obj.get("maxLength"),
                "maxProperties": obj.get("maxProperties"),
                "maximum": (
                    Maximum.from_dict(obj["maximum"])
                    if obj.get("maximum") is not None
                    else None
                ),
                "minItems": obj.get("minItems"),
                "minLength": obj.get("minLength"),
                "minProperties": obj.get("minProperties"),
                "minimum": (
                    Minimum.from_dict(obj["minimum"])
                    if obj.get("minimum") is not None
                    else None
                ),
                "multipleOf": (
                    Multipleof.from_dict(obj["multipleOf"])
                    if obj.get("multipleOf") is not None
                    else None
                ),
                "not": (
                    Schema1Output.from_dict(obj["not"])
                    if obj.get("not") is not None
                    else None
                ),
                "nullable": obj.get("nullable"),
                "oneOf": (
                    [Schema1Output.from_dict(_item) for _item in obj["oneOf"]]
                    if obj.get("oneOf") is not None
                    else None
                ),
                "pattern": obj.get("pattern"),
                "properties": (
                    dict(
                        (_k, Schema1Output.from_dict(_v))
                        for _k, _v in obj["properties"].items()
                    )
                    if obj.get("properties") is not None
                    else None
                ),
                "readOnly": obj.get("readOnly"),
                "required": obj.get("required"),
                "title": obj.get("title"),
                "type": obj.get("type"),
                "uniqueItems": obj.get("uniqueItems"),
                "writeOnly": obj.get("writeOnly"),
            }
        )
        return _obj


from unity_sps_ogc_processes_api_python_client.models.schema1_output import (
    Schema1Output,
)
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_additional_properties_output import (
    SchemaOneOfAdditionalPropertiesOutput,
)

# TODO: Rewrite to not use raise_errors
SchemaOneOfOutput.model_rebuild(raise_errors=False)
