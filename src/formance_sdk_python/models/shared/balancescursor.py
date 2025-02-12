"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountbalance import AccountBalance, AccountBalanceTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BalancesCursorCursorTypedDict(TypedDict):
    data: List[AccountBalanceTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class BalancesCursorCursor(BaseModel):
    data: List[AccountBalance]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class BalancesCursorTypedDict(TypedDict):
    r"""OK"""

    cursor: BalancesCursorCursorTypedDict


class BalancesCursor(BaseModel):
    r"""OK"""

    cursor: BalancesCursorCursor
