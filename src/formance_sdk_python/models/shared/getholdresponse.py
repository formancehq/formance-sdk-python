"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .expandeddebithold import ExpandedDebitHold, ExpandedDebitHoldTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class GetHoldResponseTypedDict(TypedDict):
    data: ExpandedDebitHoldTypedDict


class GetHoldResponse(BaseModel):
    data: ExpandedDebitHold
