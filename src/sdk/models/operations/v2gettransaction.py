"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import v2errorresponse as shared_v2errorresponse
from ..shared import v2gettransactionresponse as shared_v2gettransactionresponse
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class V2GetTransactionRequest:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Transaction ID."""
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    r"""Name of the ledger."""
    expand: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expand', 'style': 'form', 'explode': True }})
    pit: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pit', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class V2GetTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    v2_error_response: Optional[shared_v2errorresponse.V2ErrorResponse] = dataclasses.field(default=None)
    r"""Error"""
    v2_get_transaction_response: Optional[shared_v2gettransactionresponse.V2GetTransactionResponse] = dataclasses.field(default=None)
    r"""OK"""
    
