"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .orchestrationpayment import OrchestrationPayment, OrchestrationPaymentTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class ActivityGetPaymentOutputTypedDict(TypedDict):
    data: OrchestrationPaymentTypedDict


class ActivityGetPaymentOutput(BaseModel):
    data: OrchestrationPayment