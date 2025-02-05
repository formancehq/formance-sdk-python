"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import validate_int
import pydantic
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated, TypedDict


class AccountBalanceTypedDict(TypedDict):
    account_id: str
    asset: str
    balance: int
    created_at: datetime
    currency: str
    last_updated_at: datetime


class AccountBalance(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountId")]

    asset: str

    balance: Annotated[int, BeforeValidator(validate_int)]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    currency: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]

    last_updated_at: Annotated[datetime, pydantic.Field(alias="lastUpdatedAt")]
