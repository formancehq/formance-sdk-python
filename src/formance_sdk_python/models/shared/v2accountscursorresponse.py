"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2account import V2Account, V2AccountTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2AccountsCursorResponseCursorTypedDict(TypedDict):
    data: List[V2AccountTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class V2AccountsCursorResponseCursor(BaseModel):
    data: List[V2Account]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class V2AccountsCursorResponseTypedDict(TypedDict):
    cursor: V2AccountsCursorResponseCursorTypedDict


class V2AccountsCursorResponse(BaseModel):
    cursor: V2AccountsCursorResponseCursor
