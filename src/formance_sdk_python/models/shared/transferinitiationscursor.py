"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transferinitiation import TransferInitiation, TransferInitiationTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TransferInitiationsCursorCursorTypedDict(TypedDict):
    data: List[TransferInitiationTypedDict]
    has_more: bool
    page_size: int
    next: NotRequired[str]
    previous: NotRequired[str]


class TransferInitiationsCursorCursor(BaseModel):
    data: List[TransferInitiation]

    has_more: Annotated[bool, pydantic.Field(alias="hasMore")]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    next: Optional[str] = None

    previous: Optional[str] = None


class TransferInitiationsCursorTypedDict(TypedDict):
    r"""OK"""

    cursor: TransferInitiationsCursorCursorTypedDict


class TransferInitiationsCursor(BaseModel):
    r"""OK"""

    cursor: TransferInitiationsCursorCursor
