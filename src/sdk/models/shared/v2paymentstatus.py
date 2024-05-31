"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class V2PaymentStatus(str, Enum):
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    TERMINATED = 'TERMINATED'
    FAILED = 'FAILED'
    SUCCEEDED = 'SUCCEEDED'
    CANCELLED = 'CANCELLED'
