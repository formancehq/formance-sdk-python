"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2StageStatusTypedDict(TypedDict):
    instance_id: str
    stage: float
    started_at: datetime
    error: NotRequired[str]
    terminated_at: NotRequired[datetime]


class V2StageStatus(BaseModel):
    instance_id: Annotated[str, pydantic.Field(alias="instanceID")]

    stage: float

    started_at: Annotated[datetime, pydantic.Field(alias="startedAt")]

    error: Optional[str] = None

    terminated_at: Annotated[
        Optional[datetime], pydantic.Field(alias="terminatedAt")
    ] = None
