"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    v3createaccountresponse as shared_v3createaccountresponse,
)
from formance_sdk_python.types import BaseModel
import httpx
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class V3CreateAccountResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v3_create_account_response: NotRequired[
        shared_v3createaccountresponse.V3CreateAccountResponseTypedDict
    ]
    r"""Created"""


class V3CreateAccountResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v3_create_account_response: Optional[
        shared_v3createaccountresponse.V3CreateAccountResponse
    ] = None
    r"""Created"""
