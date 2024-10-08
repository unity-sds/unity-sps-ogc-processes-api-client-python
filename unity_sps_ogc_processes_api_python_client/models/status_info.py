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
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Annotated, Self

from unity_sps_ogc_processes_api_python_client.models.exception import Exception
from unity_sps_ogc_processes_api_python_client.models.link import Link
from unity_sps_ogc_processes_api_python_client.models.status_code import StatusCode


class StatusInfo(BaseModel):
    """
    StatusInfo
    """  # noqa: E501

    created: Optional[datetime] = None
    exception: Optional[Exception] = None
    finished: Optional[datetime] = None
    job_id: StrictStr = Field(alias="jobID")
    links: Optional[List[Link]] = None
    message: Optional[StrictStr] = None
    process_id: Optional[StrictStr] = Field(default=None, alias="processID")
    progress: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = None
    started: Optional[datetime] = None
    status: StatusCode
    type: StrictStr
    updated: Optional[datetime] = None
    __properties: ClassVar[List[str]] = [
        "created",
        "exception",
        "finished",
        "jobID",
        "links",
        "message",
        "processID",
        "progress",
        "started",
        "status",
        "type",
        "updated",
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
        """Create an instance of StatusInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of exception
        if self.exception:
            _dict["exception"] = self.exception.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict["links"] = _items
        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict["created"] = None

        # set to None if exception (nullable) is None
        # and model_fields_set contains the field
        if self.exception is None and "exception" in self.model_fields_set:
            _dict["exception"] = None

        # set to None if finished (nullable) is None
        # and model_fields_set contains the field
        if self.finished is None and "finished" in self.model_fields_set:
            _dict["finished"] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict["links"] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict["message"] = None

        # set to None if process_id (nullable) is None
        # and model_fields_set contains the field
        if self.process_id is None and "process_id" in self.model_fields_set:
            _dict["processID"] = None

        # set to None if progress (nullable) is None
        # and model_fields_set contains the field
        if self.progress is None and "progress" in self.model_fields_set:
            _dict["progress"] = None

        # set to None if started (nullable) is None
        # and model_fields_set contains the field
        if self.started is None and "started" in self.model_fields_set:
            _dict["started"] = None

        # set to None if updated (nullable) is None
        # and model_fields_set contains the field
        if self.updated is None and "updated" in self.model_fields_set:
            _dict["updated"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatusInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created": obj.get("created"),
                "exception": (
                    Exception.from_dict(obj["exception"])
                    if obj.get("exception") is not None
                    else None
                ),
                "finished": obj.get("finished"),
                "jobID": obj.get("jobID"),
                "links": (
                    [Link.from_dict(_item) for _item in obj["links"]]
                    if obj.get("links") is not None
                    else None
                ),
                "message": obj.get("message"),
                "processID": obj.get("processID"),
                "progress": obj.get("progress"),
                "started": obj.get("started"),
                "status": obj.get("status"),
                "type": obj.get("type"),
                "updated": obj.get("updated"),
            }
        )
        return _obj
