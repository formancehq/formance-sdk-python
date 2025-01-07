"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .wallet import Wallet, WalletTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class CreateWalletResponseTypedDict(TypedDict):
    data: WalletTypedDict


class CreateWalletResponse(BaseModel):
    data: Wallet
