"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .stage import Stage, StageTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WorkflowInstanceHistoryTypedDict(TypedDict):
    input: StageTypedDict
    name: str
    started_at: datetime
    terminated: bool
    error: NotRequired[str]
    terminated_at: NotRequired[datetime]


class WorkflowInstanceHistory(BaseModel):
    input: Stage

    name: str

    started_at: Annotated[datetime, pydantic.Field(alias="startedAt")]

    terminated: bool

    error: Optional[str] = None

    terminated_at: Annotated[
        Optional[datetime], pydantic.Field(alias="terminatedAt")
    ] = None
