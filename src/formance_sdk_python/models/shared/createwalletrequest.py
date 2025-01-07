"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from typing import Dict
from typing_extensions import TypedDict


class CreateWalletRequestTypedDict(TypedDict):
    metadata: Dict[str, str]
    r"""Custom metadata to attach to this wallet."""
    name: str


class CreateWalletRequest(BaseModel):
    metadata: Dict[str, str]
    r"""Custom metadata to attach to this wallet."""

    name: str