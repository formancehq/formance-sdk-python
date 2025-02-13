"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v3payment import V3Payment, V3PaymentTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class V3GetPaymentResponseTypedDict(TypedDict):
    data: V3PaymentTypedDict


class V3GetPaymentResponse(BaseModel):
    data: V3Payment
