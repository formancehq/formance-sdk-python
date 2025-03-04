"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .orchestrationaccount import OrchestrationAccount, OrchestrationAccountTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class ActivityGetAccountOutputTypedDict(TypedDict):
    data: OrchestrationAccountTypedDict


class ActivityGetAccountOutput(BaseModel):
    data: OrchestrationAccount
