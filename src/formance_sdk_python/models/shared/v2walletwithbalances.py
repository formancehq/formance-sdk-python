"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2assetholder import V2AssetHolder, V2AssetHolderTypedDict
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Dict
from typing_extensions import Annotated, TypedDict


class BalancesTypedDict(TypedDict):
    main: V2AssetHolderTypedDict


class Balances(BaseModel):
    main: V2AssetHolder


class V2WalletWithBalancesTypedDict(TypedDict):
    balances: BalancesTypedDict
    created_at: datetime
    id: str
    r"""The unique ID of the wallet."""
    ledger: str
    metadata: Dict[str, str]
    r"""Metadata associated with the wallet."""
    name: str


class V2WalletWithBalances(BaseModel):
    balances: Balances

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    id: str
    r"""The unique ID of the wallet."""

    ledger: str

    metadata: Dict[str, str]
    r"""Metadata associated with the wallet."""

    name: str