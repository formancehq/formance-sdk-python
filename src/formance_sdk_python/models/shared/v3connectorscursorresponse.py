"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3connector import V3Connector, V3ConnectorTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3ConnectorsCursorResponseCursorTypedDict(TypedDict):
    data: List[V3ConnectorTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class V3ConnectorsCursorResponseCursor(BaseModel):
    data: List[V3Connector]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class V3ConnectorsCursorResponseTypedDict(TypedDict):
    cursor: V3ConnectorsCursorResponseCursorTypedDict


class V3ConnectorsCursorResponse(BaseModel):
    cursor: V3ConnectorsCursorResponseCursor
