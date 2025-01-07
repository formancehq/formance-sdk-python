"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v2volume import V2Volume, V2VolumeTypedDict
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V2AccountTypedDict(TypedDict):
    address: str
    metadata: Dict[str, str]
    effective_volumes: NotRequired[Dict[str, V2VolumeTypedDict]]
    volumes: NotRequired[Dict[str, V2VolumeTypedDict]]


class V2Account(BaseModel):
    address: str

    metadata: Dict[str, str]

    effective_volumes: Annotated[
        Optional[Dict[str, V2Volume]], pydantic.Field(alias="effectiveVolumes")
    ] = None

    volumes: Optional[Dict[str, V2Volume]] = None
