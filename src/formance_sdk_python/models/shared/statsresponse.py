"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .stats import Stats, StatsTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class StatsResponseTypedDict(TypedDict):
    data: StatsTypedDict


class StatsResponse(BaseModel):
    data: Stats