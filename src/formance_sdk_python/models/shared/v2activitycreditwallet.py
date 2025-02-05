"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2creditwalletrequest import V2CreditWalletRequest, V2CreditWalletRequestTypedDict
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class V2ActivityCreditWalletTypedDict(TypedDict):
    data: NotRequired[V2CreditWalletRequestTypedDict]
    id: NotRequired[str]


class V2ActivityCreditWallet(BaseModel):
    data: Optional[V2CreditWalletRequest] = None

    id: Optional[str] = None
