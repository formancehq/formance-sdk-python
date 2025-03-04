"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetholder import AssetHolder, AssetHolderTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Dict
from typing_extensions import Annotated, TypedDict


class WalletWithBalancesBalancesTypedDict(TypedDict):
    main: AssetHolderTypedDict


class WalletWithBalancesBalances(BaseModel):
    main: AssetHolder


class WalletWithBalancesTypedDict(TypedDict):
    balances: WalletWithBalancesBalancesTypedDict
    created_at: datetime
    id: str
    r"""The unique ID of the wallet."""
    ledger: str
    metadata: Dict[str, str]
    r"""Metadata associated with the wallet."""
    name: str


class WalletWithBalances(BaseModel):
    balances: WalletWithBalancesBalances

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    id: str
    r"""The unique ID of the wallet."""

    ledger: str

    metadata: Dict[str, str]
    r"""Metadata associated with the wallet."""

    name: str
