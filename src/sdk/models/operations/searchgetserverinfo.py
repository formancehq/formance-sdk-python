"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serverinfo as shared_serverinfo
from typing import Optional


@dataclasses.dataclass
class SearchgetServerInfoResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    r"""Server information"""
    

