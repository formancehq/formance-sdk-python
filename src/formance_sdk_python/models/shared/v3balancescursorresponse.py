"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3balance import V3Balance, V3BalanceTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3BalancesCursorResponseCursorTypedDict(TypedDict):
    data: List[V3BalanceTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class V3BalancesCursorResponseCursor(BaseModel):
    data: List[V3Balance]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class V3BalancesCursorResponseTypedDict(TypedDict):
    cursor: V3BalancesCursorResponseCursorTypedDict


class V3BalancesCursorResponse(BaseModel):
    cursor: V3BalancesCursorResponseCursor
