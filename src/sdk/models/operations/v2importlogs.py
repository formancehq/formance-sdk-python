"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class V2ImportLogsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    request_body: Optional[str] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/octet-stream' }})
    



@dataclasses.dataclass
class V2ImportLogsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    
