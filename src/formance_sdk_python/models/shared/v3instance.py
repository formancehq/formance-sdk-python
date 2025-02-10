"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3InstanceTypedDict(TypedDict):
    connector_id: str
    created_at: datetime
    id: str
    schedule_id: str
    terminated: bool
    error: NotRequired[str]
    terminated_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class V3Instance(BaseModel):
    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    id: str

    schedule_id: Annotated[str, pydantic.Field(alias="scheduleID")]

    terminated: bool

    error: Optional[str] = None

    terminated_at: Annotated[
        Optional[datetime], pydantic.Field(alias="terminatedAt")
    ] = None

    updated_at: Annotated[Optional[datetime], pydantic.Field(alias="updatedAt")] = None
