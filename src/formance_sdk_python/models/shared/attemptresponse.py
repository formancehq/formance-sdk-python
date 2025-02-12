"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attempt import Attempt, AttemptTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class AttemptResponseTypedDict(TypedDict):
    data: AttemptTypedDict


class AttemptResponse(BaseModel):
    data: Attempt
