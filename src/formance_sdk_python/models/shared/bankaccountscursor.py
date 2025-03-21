"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bankaccount import BankAccount, BankAccountTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BankAccountsCursorCursorTypedDict(TypedDict):
    data: List[BankAccountTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class BankAccountsCursorCursor(BaseModel):
    data: List[BankAccount]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class BankAccountsCursorTypedDict(TypedDict):
    r"""OK"""

    cursor: BankAccountsCursorCursorTypedDict


class BankAccountsCursor(BaseModel):
    r"""OK"""

    cursor: BankAccountsCursorCursor
