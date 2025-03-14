"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3bankaccount import V3BankAccount, V3BankAccountTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V3BankAccountsCursorResponseCursorTypedDict(TypedDict):
    data: List[V3BankAccountTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class V3BankAccountsCursorResponseCursor(BaseModel):
    data: List[V3BankAccount]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class V3BankAccountsCursorResponseTypedDict(TypedDict):
    cursor: V3BankAccountsCursorResponseCursorTypedDict


class V3BankAccountsCursorResponse(BaseModel):
    cursor: V3BankAccountsCursorResponseCursor
