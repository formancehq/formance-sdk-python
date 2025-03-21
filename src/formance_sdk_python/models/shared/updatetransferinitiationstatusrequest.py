"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class Status(str, Enum):
    REJECTED = "REJECTED"
    VALIDATED = "VALIDATED"


class UpdateTransferInitiationStatusRequestTypedDict(TypedDict):
    status: Status


class UpdateTransferInitiationStatusRequest(BaseModel):
    status: Status
