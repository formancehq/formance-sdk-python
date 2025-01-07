"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .client import Client, ClientTypedDict
from formance_sdk_python.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListClientsResponseTypedDict(TypedDict):
    data: NotRequired[List[ClientTypedDict]]


class ListClientsResponse(BaseModel):
    data: Optional[List[Client]] = None