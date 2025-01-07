"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class AddAccountToPoolRequestTypedDict(TypedDict):
    account_id: str


class AddAccountToPoolRequest(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountID")]
