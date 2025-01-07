"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .payment import Payment, PaymentTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PaymentsCursorCursorTypedDict(TypedDict):
    data: List[PaymentTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class PaymentsCursorCursor(BaseModel):
    data: List[Payment]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class PaymentsCursorTypedDict(TypedDict):
    r"""OK"""

    cursor: PaymentsCursorCursorTypedDict


class PaymentsCursor(BaseModel):
    r"""OK"""

    cursor: PaymentsCursorCursor
