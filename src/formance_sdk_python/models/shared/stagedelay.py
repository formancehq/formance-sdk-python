"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from formance_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class StageDelayTypedDict(TypedDict):
    duration: NotRequired[str]
    until: NotRequired[datetime]


class StageDelay(BaseModel):
    duration: Optional[str] = None

    until: Optional[datetime] = None
