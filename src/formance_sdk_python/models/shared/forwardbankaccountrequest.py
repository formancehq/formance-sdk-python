"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class ForwardBankAccountRequestTypedDict(TypedDict):
    connector_id: str


class ForwardBankAccountRequest(BaseModel):
    connector_id: Annotated[str, pydantic.Field(alias="connectorID")]
