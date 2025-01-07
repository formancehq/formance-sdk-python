"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from typing import Dict
from typing_extensions import TypedDict


class ActivityAddAccountMetadataTypedDict(TypedDict):
    id: str
    ledger: str
    metadata: Dict[str, str]


class ActivityAddAccountMetadata(BaseModel):
    id: str

    ledger: str

    metadata: Dict[str, str]
