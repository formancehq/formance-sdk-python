"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .balancewithassets import BalanceWithAssets, BalanceWithAssetsTypedDict
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import validate_int
import pydantic
from pydantic.functional_validators import BeforeValidator
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetWalletSummaryResponseTypedDict(TypedDict):
    available_funds: Dict[str, int]
    balances: List[BalanceWithAssetsTypedDict]
    expirable_funds: Dict[str, int]
    expired_funds: Dict[str, int]
    hold_funds: Dict[str, int]


class GetWalletSummaryResponse(BaseModel):
    available_funds: Annotated[
        Dict[str, Annotated[int, BeforeValidator(validate_int)]],
        pydantic.Field(alias="availableFunds"),
    ]

    balances: List[BalanceWithAssets]

    expirable_funds: Annotated[
        Dict[str, Annotated[int, BeforeValidator(validate_int)]],
        pydantic.Field(alias="expirableFunds"),
    ]

    expired_funds: Annotated[
        Dict[str, Annotated[int, BeforeValidator(validate_int)]],
        pydantic.Field(alias="expiredFunds"),
    ]

    hold_funds: Annotated[
        Dict[str, Annotated[int, BeforeValidator(validate_int)]],
        pydantic.Field(alias="holdFunds"),
    ]
