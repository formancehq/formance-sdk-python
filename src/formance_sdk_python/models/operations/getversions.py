"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import (
    getversionsresponse as shared_getversionsresponse,
)
from formance_sdk_python.types import BaseModel
import httpx
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GetVersionsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    get_versions_response: NotRequired[
        shared_getversionsresponse.GetVersionsResponseTypedDict
    ]
    r"""OK"""


class GetVersionsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    get_versions_response: Optional[shared_getversionsresponse.GetVersionsResponse] = (
        None
    )
    r"""OK"""
