"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class StageWaitEventTypedDict(TypedDict):
    event: str


class StageWaitEvent(BaseModel):
    event: str