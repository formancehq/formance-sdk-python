"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2stats import V2Stats, V2StatsTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class V2StatsResponseTypedDict(TypedDict):
    data: V2StatsTypedDict


class V2StatsResponse(BaseModel):
    data: V2Stats
