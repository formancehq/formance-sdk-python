"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2transaction import V2Transaction, V2TransactionTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class V2CreateTransactionResponseTypedDict(TypedDict):
    data: V2TransactionTypedDict


class V2CreateTransactionResponse(BaseModel):
    data: V2Transaction
