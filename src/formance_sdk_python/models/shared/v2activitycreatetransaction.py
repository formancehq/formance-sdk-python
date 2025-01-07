"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2posttransaction import V2PostTransaction, V2PostTransactionTypedDict
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class V2ActivityCreateTransactionTypedDict(TypedDict):
    data: NotRequired[V2PostTransactionTypedDict]
    ledger: NotRequired[str]


class V2ActivityCreateTransaction(BaseModel):
    data: Optional[V2PostTransaction] = None

    ledger: Optional[str] = None
