"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2MigrationInfoState(str, Enum):
    TO_DO = "TO DO"
    DONE = "DONE"


class V2MigrationInfoTypedDict(TypedDict):
    date_: NotRequired[datetime]
    name: NotRequired[str]
    state: NotRequired[V2MigrationInfoState]
    version: NotRequired[str]


class V2MigrationInfo(BaseModel):
    date_: Annotated[Optional[datetime], pydantic.Field(alias="date")] = None

    name: Optional[str] = None

    state: Optional[V2MigrationInfoState] = None

    version: Optional[str] = None
