"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class V3BankAccountRelatedAccountTypedDict(TypedDict):
    account_id: str
    created_at: datetime


class V3BankAccountRelatedAccount(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]
