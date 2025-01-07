"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .orchestrationwallet import OrchestrationWallet, OrchestrationWalletTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OrchestrationListWalletsResponseCursorTypedDict(TypedDict):
    data: List[OrchestrationWalletTypedDict]
    page_size: int
    has_more: NotRequired[bool]
    next: NotRequired[str]
    previous: NotRequired[str]


class OrchestrationListWalletsResponseCursor(BaseModel):
    data: List[OrchestrationWallet]

    page_size: Annotated[int, pydantic.Field(alias="pageSize")]

    has_more: Annotated[Optional[bool], pydantic.Field(alias="hasMore")] = None

    next: Optional[str] = None

    previous: Optional[str] = None


class OrchestrationListWalletsResponseTypedDict(TypedDict):
    cursor: OrchestrationListWalletsResponseCursorTypedDict


class OrchestrationListWalletsResponse(BaseModel):
    cursor: OrchestrationListWalletsResponseCursor