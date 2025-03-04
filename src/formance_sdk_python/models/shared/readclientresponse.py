"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .client import Client, ClientTypedDict
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ReadClientResponseTypedDict(TypedDict):
    data: NotRequired[ClientTypedDict]


class ReadClientResponse(BaseModel):
    data: Optional[Client] = None
