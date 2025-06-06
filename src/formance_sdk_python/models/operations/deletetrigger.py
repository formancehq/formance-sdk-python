"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import pydantic
from typing_extensions import Annotated, TypedDict


class DeleteTriggerRequestTypedDict(TypedDict):
    trigger_id: str
    r"""The trigger id"""


class DeleteTriggerRequest(BaseModel):
    trigger_id: Annotated[
        str,
        pydantic.Field(alias="triggerID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The trigger id"""


class DeleteTriggerResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class DeleteTriggerResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
