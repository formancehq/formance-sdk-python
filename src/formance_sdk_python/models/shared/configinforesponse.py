"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .configinfo import ConfigInfo, ConfigInfoTypedDict
from formance_sdk_python.types import BaseModel
from typing_extensions import TypedDict


class ConfigInfoResponseTypedDict(TypedDict):
    data: ConfigInfoTypedDict


class ConfigInfoResponse(BaseModel):
    data: ConfigInfo
