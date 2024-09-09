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
from typing import TYPE_CHECKING, Any, Dict, Optional, Set, Union

from pydantic import BaseModel, ValidationError, field_validator
from typing_extensions import Self

from unity_sps_ogc_processes_api_python_client.models.reference import Reference
from unity_sps_ogc_processes_api_python_client.models.schema_one_of_output import (
    SchemaOneOfOutput,
)

MODELSCHEMAOUTPUT_ANY_OF_SCHEMAS = ["Reference", "SchemaOneOfOutput"]


class ModelSchemaOutput(BaseModel):
    """
    ModelSchemaOutput
    """

    # data type: Reference
    anyof_schema_1_validator: Optional[Reference] = None
    # data type: SchemaOneOfOutput
    anyof_schema_2_validator: Optional[SchemaOneOfOutput] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[Reference, SchemaOneOfOutput]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = {"Reference", "SchemaOneOfOutput"}

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        ModelSchemaOutput.model_construct()
        error_messages = []
        # validate data type: Reference
        if not isinstance(v, Reference):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Reference`")
        else:
            return v

        # validate data type: SchemaOneOfOutput
        if not isinstance(v, SchemaOneOfOutput):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `SchemaOneOfOutput`"
            )
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when setting the actual_instance in ModelSchemaOutput with anyOf schemas: Reference, SchemaOneOfOutput. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[Reference] = None
        try:
            instance.actual_instance = Reference.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[SchemaOneOfOutput] = None
        try:
            instance.actual_instance = SchemaOneOfOutput.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into ModelSchemaOutput with anyOf schemas: Reference, SchemaOneOfOutput. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(
            self.actual_instance.to_json
        ):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], Reference, SchemaOneOfOutput]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(
            self.actual_instance.to_dict
        ):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
