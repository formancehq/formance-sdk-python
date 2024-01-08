"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import v2errorresponse as errors_v2errorresponse
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclasses.dataclass
class V2CountAccountsRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    pit: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pit', 'style': 'form', 'explode': True }})
    request_body: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class V2CountAccountsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    headers: Dict[str, List[str]] = dataclasses.field()
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    v2_error_response: Optional[errors_v2errorresponse.V2ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

