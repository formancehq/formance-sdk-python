"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import v2createledgerrequest as shared_v2createledgerrequest
from ..shared import v2errorresponse as shared_v2errorresponse
from typing import Optional


@dataclasses.dataclass
class V2CreateLedgerRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    v2_create_ledger_request: Optional[shared_v2createledgerrequest.V2CreateLedgerRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class V2CreateLedgerResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_error_response: Optional[shared_v2errorresponse.V2ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    

