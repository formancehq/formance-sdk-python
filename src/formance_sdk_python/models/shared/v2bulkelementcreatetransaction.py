"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2posttransaction import V2PostTransaction, V2PostTransactionTypedDict
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class V2BulkElementCreateTransactionTypedDict(TypedDict):
    action: str
    data: NotRequired[V2PostTransactionTypedDict]
    ik: NotRequired[str]


class V2BulkElementCreateTransaction(BaseModel):
    action: str

    data: Optional[V2PostTransaction] = None

    ik: Optional[str] = None
