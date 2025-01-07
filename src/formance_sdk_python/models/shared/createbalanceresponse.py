"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .balance import Balance, BalanceTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class CreateBalanceResponseTypedDict(TypedDict):
    data: BalanceTypedDict


class CreateBalanceResponse(BaseModel):
    data: Balance