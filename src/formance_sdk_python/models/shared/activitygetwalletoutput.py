"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .walletwithbalances import WalletWithBalances, WalletWithBalancesTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class ActivityGetWalletOutputTypedDict(TypedDict):
    data: WalletWithBalancesTypedDict


class ActivityGetWalletOutput(BaseModel):
    data: WalletWithBalances