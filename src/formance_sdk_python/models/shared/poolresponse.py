"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .pool import Pool, PoolTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class PoolResponseTypedDict(TypedDict):
    r"""OK"""

    data: PoolTypedDict


class PoolResponse(BaseModel):
    r"""OK"""

    data: Pool
