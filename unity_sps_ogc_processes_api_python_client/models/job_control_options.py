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
from enum import Enum

from typing_extensions import Self


class JobControlOptions(str, Enum):
    """
    JobControlOptions
    """

    """
    allowed enum values
    """
    SYNC_MINUS_EXECUTE = "sync-execute"
    ASYNC_MINUS_EXECUTE = "async-execute"
    DISMISS = "dismiss"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobControlOptions from a JSON string"""
        return cls(json.loads(json_str))