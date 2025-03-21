"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    confirmholdrequest as shared_confirmholdrequest,
)
from formance_sdk_python.types import BaseModel
from formance_sdk_python.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import httpx
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConfirmHoldRequestTypedDict(TypedDict):
    hold_id: str
    confirm_hold_request: NotRequired[
        shared_confirmholdrequest.ConfirmHoldRequestTypedDict
    ]
    idempotency_key: NotRequired[str]
    r"""Use an idempotency key"""


class ConfirmHoldRequest(BaseModel):
    hold_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    confirm_hold_request: Annotated[
        Optional[shared_confirmholdrequest.ConfirmHoldRequest],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Use an idempotency key"""


class ConfirmHoldResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class ConfirmHoldResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
