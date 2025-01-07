"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .transaction import Transaction, TransactionTypedDict
from formance_sdk_python.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class TransactionsResponseTypedDict(TypedDict):
    data: List[TransactionTypedDict]


class TransactionsResponse(BaseModel):
    data: List[Transaction]
