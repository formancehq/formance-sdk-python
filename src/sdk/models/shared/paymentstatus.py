"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class PaymentStatus(str, Enum):
    PENDING = 'PENDING'
    SUCCEEDED = 'SUCCEEDED'
    CANCELLED = 'CANCELLED'
    FAILED = 'FAILED'
    EXPIRED = 'EXPIRED'
    REFUNDED = 'REFUNDED'
    REFUNDED_FAILURE = 'REFUNDED_FAILURE'
    DISPUTE = 'DISPUTE'
    DISPUTE_WON = 'DISPUTE_WON'
    DISPUTE_LOST = 'DISPUTE_LOST'
    OTHER = 'OTHER'
