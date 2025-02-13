"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class BankAccountRelatedAccountsTypedDict(TypedDict):
    account_id: str
    connector_id: str
    created_at: datetime
    id: str
    provider: str


class BankAccountRelatedAccounts(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountID")]

    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]

    created_at: Annotated[datetime, pydantic.Field(alias="createdAt")]

    id: str

    provider: str
