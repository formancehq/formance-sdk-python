"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .policy import Policy, PolicyTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class PolicyResponseTypedDict(TypedDict):
    r"""OK"""

    data: PolicyTypedDict


class PolicyResponse(BaseModel):
    r"""OK"""

    data: Policy
