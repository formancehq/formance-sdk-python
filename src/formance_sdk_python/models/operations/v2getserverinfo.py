"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from formance_sdk_python.models.shared import v2serverinfo as shared_v2serverinfo
from formance_sdk_python.types import BaseModel
import httpx
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class V2GetServerInfoResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_server_info: NotRequired[shared_v2serverinfo.V2ServerInfoTypedDict]
    r"""Server information"""


class V2GetServerInfoResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    v2_server_info: Optional[shared_v2serverinfo.V2ServerInfo] = None
    r"""Server information"""
