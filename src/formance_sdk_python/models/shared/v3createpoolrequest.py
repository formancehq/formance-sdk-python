"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class V3CreatePoolRequestTypedDict(TypedDict):
    account_i_ds: List[str]
    name: str


class V3CreatePoolRequest(BaseModel):
    account_i_ds: Annotated[List[str], pydantic.Field(alias="accountIDs")]

    name: str
