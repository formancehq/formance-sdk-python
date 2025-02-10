"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3schedule import V3Schedule, V3ScheduleTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class V3ConnectorScheduleResponseTypedDict(TypedDict):
    data: V3ScheduleTypedDict


class V3ConnectorScheduleResponse(BaseModel):
    data: V3Schedule
