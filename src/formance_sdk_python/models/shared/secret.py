"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
import pydantic
from typing import Any, Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SecretTypedDict(TypedDict):
    clear: str
    id: str
    last_digits: str
    name: str
    metadata: NotRequired[Dict[str, Any]]


class Secret(BaseModel):
    clear: str

    id: str

    last_digits: Annotated[str, pydantic.Field(alias="lastDigits")]

    name: str

    metadata: Optional[Dict[str, Any]] = None
