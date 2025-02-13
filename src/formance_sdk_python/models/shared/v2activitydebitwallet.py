"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2debitwalletrequest import V2DebitWalletRequest, V2DebitWalletRequestTypedDict
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class V2ActivityDebitWalletTypedDict(TypedDict):
    data: NotRequired[V2DebitWalletRequestTypedDict]
    id: NotRequired[str]


class V2ActivityDebitWallet(BaseModel):
    data: Optional[V2DebitWalletRequest] = None

    id: Optional[str] = None
