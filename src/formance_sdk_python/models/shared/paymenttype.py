"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class PaymentType(str, Enum):
    PAY_IN = "PAY-IN"
    PAYOUT = "PAYOUT"
    TRANSFER = "TRANSFER"
    OTHER = "OTHER"