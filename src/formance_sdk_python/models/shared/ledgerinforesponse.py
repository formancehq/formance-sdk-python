"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ledgerinfo import LedgerInfo, LedgerInfoTypedDict
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LedgerInfoResponseTypedDict(TypedDict):
    data: NotRequired[LedgerInfoTypedDict]


class LedgerInfoResponse(BaseModel):
    data: Optional[LedgerInfo] = None
