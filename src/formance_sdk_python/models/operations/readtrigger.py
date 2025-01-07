"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    readtriggerresponse as shared_readtriggerresponse,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import FieldMetadata, PathParamMetadata
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ReadTriggerRequestTypedDict(TypedDict):
    trigger_id: str
    r"""The trigger id"""


class ReadTriggerRequest(BaseModel):
    trigger_id: Annotated[
        str,
        pydantic.Field(alias="triggerID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The trigger id"""


class ReadTriggerResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    read_trigger_response: NotRequired[
        shared_readtriggerresponse.ReadTriggerResponseTypedDict
    ]
    r"""A specific trigger"""


class ReadTriggerResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    read_trigger_response: Optional[shared_readtriggerresponse.ReadTriggerResponse] = (
        None
    )
    r"""A specific trigger"""
