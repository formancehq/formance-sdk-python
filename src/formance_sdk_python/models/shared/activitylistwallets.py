"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ActivityListWalletsTypedDict(TypedDict):
    name: NotRequired[str]


class ActivityListWallets(BaseModel):
    name: Optional[str] = None