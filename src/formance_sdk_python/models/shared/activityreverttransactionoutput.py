"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .orchestrationtransaction import (
    OrchestrationTransaction,
    OrchestrationTransactionTypedDict,
)
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class ActivityRevertTransactionOutputTypedDict(TypedDict):
    data: OrchestrationTransactionTypedDict


class ActivityRevertTransactionOutput(BaseModel):
    data: OrchestrationTransaction